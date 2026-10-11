# ESP-Miner PR #717: Refactor Stratum code for Seamless Failover

> Source: https://github.com/bitaxeorg/ESP-Miner/pull/717
> Collected: 2026-10-10
> Published: 2025-02-18
> Registry ID: esp-miner

State: closed | Merged: 2025-03-09 | Author: eandersson | +523/-519 | Labels: enhancement

## Body

This refactor improves Stratum to support multiple simultaneous connections, enabling faster and more reliable failover. It also lays the foundation for more advanced connection strategies, monitoring, and metrics. In addition, the code supports more than two pools (primary and fallback) .

Each connection now maintains its own Stratum queue, with the active connection pushing its messages to a shared ASIC queue. During a failover event, the system seamlessly transitions to pulling messages from the failover connection's queue, minimizing disruption. Additionally, all ongoing work is completed before failing back to the primary pool, reducing wasted effort - especially critical in environments with frequent failovers due to pool or network instability.

## Files changed

- `main/tasks/stratum_task.c` (+259/-240) — firmware task module
- `components/stratum/stratum_api.c` (+66/-98) — stratum protocol component
- `main/tasks/create_jobs_task.c` (+40/-20) — firmware task module
- `main/tasks/stratum_task.h` (+44/-3) — firmware task module
- `components/stratum/test/test_stratum_json.c` (+14/-31) — stratum protocol component
- `components/asic/bm1366.c` (+8/-17) — C source
- `main/global_state.h` (+5/-20) — shared global state structs/flags
- `main/tasks/asic_task.c` (+18/-7) — firmware task module
- `components/asic/bm1370.c` (+8/-15) — C source
- `components/stratum/include/stratum_api.h` (+15/-7) — stratum protocol component
- `components/asic/bm1368.c` (+7/-14) — C source
- `components/asic/bm1397.c` (+7/-14) — C source
- `main/tasks/asic_result_task.c` (+11/-6) — firmware task module
- `components/asic/asic.c` (+6/-10) — C source
- `main/main.c` (+5/-8) — main app
- `main/self_test/self_test.c` (+0/-3) — factory self-test module
- `components/asic/include/asic.h` (+1/-1) — C header
- `components/asic/include/bm1366.h` (+1/-1) — C header
- `components/asic/include/bm1368.h` (+1/-1) — C header
- `components/asic/include/bm1370.h` (+1/-1) — C header
- `components/asic/include/bm1397.h` (+1/-1) — C header
- `components/stratum/include/mining.h` (+2/-0) — stratum protocol component
- `components/stratum/mining.c` (+2/-0) — stratum protocol component
- `main/http_server/http_server.c` (+1/-1) — HTTP server + REST API handlers

## Key excerpts

### `main/tasks/stratum_task.c` `@@ -23,18 +23,14 @@`

```diff
 #define FALLBACK_STRATUM_PW CONFIG_FALLBACK_STRATUM_PW
 #define STRATUM_DIFFICULTY CONFIG_STRATUM_DIFFICULTY
 
-#define MAX_RETRY_ATTEMPTS 3
-#define MAX_CRITICAL_RETRY_ATTEMPTS 5
-
-#define BUFFER_SIZE 1024
-
 static const char * TAG = "stratum_task";
 
-static StratumApiV1Message stratum_api_v1_message = {};
-static SystemTaskModule SYSTEM_TASK_MODULE = {.stratum_difficulty = 8192};
+static int addr_family = AF_INET;
+static int ip_protocol = IPPROTO_IP;
 
-static const char * primary_stratum_url;
-static uint16_t primary_stratum_port;
+void stratum_process(const char * POOL_TAG, GlobalState * GLOBAL_STATE, StratumConnection * connection);
+void stratum_task(const char * POOL_TAG, GlobalState * GLOBAL_STATE, StratumConnection * connection);
+void stratum_task_init_connection(StratumConnection * connection);
 
 struct timeval tcp_snd_timeout = {
     .tv_sec = 5,
```

### `main/tasks/asic_result_task.c` `@@ -46,11 +52,10 @@ void ASIC_result_task(void *pvParameters)`

```diff
 
         if (nonce_diff >= GLOBAL_STATE->ASIC_TASK_MODULE.active_jobs[job_id]->pool_diff)
         {
-            char * user = GLOBAL_STATE->SYSTEM_MODULE.is_using_fallback ? GLOBAL_STATE->SYSTEM_MODULE.fallback_pool_user : GLOBAL_STATE->SYSTEM_MODULE.pool_user;
             int ret = STRATUM_V1_submit_share(
-                GLOBAL_STATE->sock,
-                GLOBAL_STATE->send_uid++,
-                user,
+                current_connection->sock,
+                current_connection->send_uid++,
+                current_connection->username,
                 GLOBAL_STATE->ASIC_TASK_MODULE.active_jobs[job_id]->jobid,
                 GLOBAL_STATE->ASIC_TASK_MODULE.active_jobs[job_id]->extranonce2,
                 GLOBAL_STATE->ASIC_TASK_MODULE.active_jobs[job_id]->ntime,
```

### `main/tasks/asic_task.c` `@@ -35,17 +35,28 @@ void ASIC_task(void *pvParameters)`

```diff
 
     while (1)
     {
-
         bm_job *next_bm_job = (bm_job *)queue_dequeue(&GLOBAL_STATE->ASIC_jobs_queue);
+        StratumConnection *current_connection = &GLOBAL_STATE->connections[next_bm_job->connection_id];
+
+        if (next_bm_job->connection_id != GLOBAL_STATE->current_connection_id)
    …
+            continue;
+
+        if (current_connection->state != STRATUM_CONNECTED)
+        {
+            ESP_LOGW(TAG, "Connection for job no longer open. Skipping.");
+            continue;
+        }
 
-        if (next_bm_job->pool_diff != GLOBAL_STATE->stratum_difficulty)
+        if (current_connection->stratum_difficulty != next_bm_job->pool_diff)
         {
             ESP_LOGI(TAG, "New pool difficulty %lu", next_bm_job->pool_diff);
-            GLOBAL_STATE->stratum_difficulty = next_bm_job->pool_diff;
+            current_connection->stratum_difficulty = next_bm_job->pool_diff;
         }
 
-        //(*GLOBAL_STATE->ASIC_functions.send_work_fn)(GLOBAL_STATE, next_bm_job); // send the job to the ASIC
-        ASIC_send_work(GLOBAL_STATE, next_bm_job);
+        pthread_mutex_lock(&current_connection->jobs_lock);
+        int job_id = ASIC_send_work(GLOBAL_STATE, next_bm_job);
[… hunk truncated: showing head + densest window of 33 diff lines]
```

### `main/http_server/http_server.c` `@@ -544,7 +544,7 @@ static esp_err_t GET_system_info(httpd_req_t * req)`

```diff
     cJSON_AddNumberToObject(root, "hashRate", GLOBAL_STATE->SYSTEM_MODULE.current_hashrate);
     cJSON_AddStringToObject(root, "bestDiff", GLOBAL_STATE->SYSTEM_MODULE.best_diff_string);
     cJSON_AddStringToObject(root, "bestSessionDiff", GLOBAL_STATE->SYSTEM_MODULE.best_session_diff_string);
-    cJSON_AddNumberToObject(root, "stratumDiff", GLOBAL_STATE->stratum_difficulty);
+    cJSON_AddNumberToObject(root, "stratumDiff", GLOBAL_STATE->connections[GLOBAL_STATE->current_connection_id].stratum_difficulty);
 
     cJSON_AddNumberToObject(root, "isUsingFallbackStratum", GLOBAL_STATE->SYSTEM_MODULE.is_using_fallback);
 
```
