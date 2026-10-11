# ESP-Miner PR #1064: Extranonce subscribe and suggested difficulty pool options

> Source: https://github.com/bitaxeorg/ESP-Miner/pull/1064
> Collected: 2026-10-10
> Published: 2025-06-23
> Registry ID: esp-miner

State: closed | Merged: 2025-06-26 | Author: mutatrum | +194/-106 | Labels: enhancement, hashing, breaking api change

## Body

Added per pool settings for suggested difficulty and extranonce subscribe.

Added cards for primary and fallback pool configuration.

Cleaned up pool settings by extracting a component (by @duckAxe)

Moved stratum rx logging to `stratum_api` so tx/rx are logged with the same `TAG`.

Fixes #62
Fixes #193
Fixes #251 

![image](https://github.com/user-attachments/assets/99046c1f-d2c1-4321-b99e-0f04349ca110)

API CHANGE: `api/v1/info` field `stratumDiff` is renamed to `stratumDifficulty`.

## Files changed

- `main/http_server/axe-os/src/app/components/pool/pool.component.html` (+37/-55) — AxeOS Angular UI
- `components/stratum/stratum_api.c` (+21/-12) — stratum protocol component
- `main/http_server/axe-os/src/app/components/pool/pool.component.ts` (+16/-13) — AxeOS Angular UI
- `main/tasks/stratum_task.c` (+13/-14) — firmware task module
- `main/http_server/http_server.c` (+21/-4) — HTTP server + REST API handlers
- `main/http_server/openapi.yaml` (+18/-2) — OpenAPI spec
- `main/Kconfig.projbuild` (+19/-0) — main app
- `main/system.h` (+12/-0) — main app
- `main/http_server/axe-os/src/models/ISystemInfo.ts` (+7/-3) — AxeOS web UI
- `main/http_server/axe-os/src/app/services/system.service.ts` (+6/-2) — AxeOS Angular service
- `main/system.c` (+8/-0) — main app
- `main/global_state.h` (+5/-1) — shared global state structs/flags
- `config-601.cvs` (+4/-0) — changed file
- `main/nvs_config.h` (+4/-0) — NVS settings schema/keys
- `components/stratum/include/stratum_api.h` (+3/-0) — stratum protocol component

## Key excerpts

### `components/stratum/stratum_api.c` `@@ -383,6 +383,15 @@ int STRATUM_V1_suggest_difficulty(int socket, int send_uid, uint32_t difficulty)`

```diff
     return write(socket, difficulty_msg, strlen(difficulty_msg));
 }
 
+int STRATUM_V1_extranonce_subscribe(int socket, int send_uid)
+{
+    char extranonce_msg[BUFFER_SIZE];
+    sprintf(extranonce_msg, "{\"id\": %d, \"method\": \"mining.extranonce.subscribe\", \"params\": []}\n", send_uid);
+    debug_stratum_tx(extranonce_msg);
+
+    return write(socket, extranonce_msg, strlen(extranonce_msg));
+}
+
 int STRATUM_V1_authorize(int socket, int send_uid, const char * username, const char * pass)
 {
     char authorize_msg[BUFFER_SIZE];
```

### `main/tasks/stratum_task.c` `@@ -366,7 +362,10 @@ void stratum_task(void * pvParameters)`

```diff
                 if (stratum_api_v1_message.response_success) {
                     ESP_LOGI(TAG, "setup message accepted");
                     if (stratum_api_v1_message.message_id == authorize_message_id) {
-                        STRATUM_V1_suggest_difficulty(GLOBAL_STATE->sock, GLOBAL_STATE->send_uid++, STRATUM_DIFFICULTY);
+                        STRATUM_V1_suggest_difficulty(GLOBAL_STATE->sock, GLOBAL_STATE->send_uid++, difficulty);
+                    }
+                    if (extranonce_subscribe) {
+                        STRATUM_V1_extranonce_subscribe(GLOBAL_STATE->sock, GLOBAL_STATE->send_uid++);
                     }
                 } else {
                     ESP_LOGE(TAG, "setup message rejected: %s", stratum_api_v1_message.error_str);
```

### `components/stratum/include/stratum_api.h` `@@ -87,6 +88,8 @@ int STRATUM_V1_configure_version_rolling(int socket, int send_uid, uint32_t * ve`

```diff
 
 int STRATUM_V1_suggest_difficulty(int socket, int send_uid, uint32_t difficulty);
 
+int STRATUM_V1_extranonce_subscribe(int socket, int send_uid);
+
 int STRATUM_V1_submit_share(int socket, int send_uid, const char *username, const char *jobid,
                             const char *extranonce_2, const uint32_t ntime, const uint32_t nonce,
                             const uint32_t version);
```

### `main/system.c` `@@ -73,6 +73,14 @@ void SYSTEM_init_system(GlobalState * GLOBAL_STATE)`

```diff
     module->pool_pass = nvs_config_get_string(NVS_CONFIG_STRATUM_PASS, CONFIG_STRATUM_PW);
     module->fallback_pool_pass = nvs_config_get_string(NVS_CONFIG_FALLBACK_STRATUM_PASS, CONFIG_FALLBACK_STRATUM_PW);
 
+    // set the pool difficulty
+    module->pool_difficulty = nvs_config_get_u16(NVS_CONFIG_STRATUM_DIFFICULTY, CONFIG_STRATUM_DIFFICULTY);
+    module->fallback_pool_difficulty = nvs_config_get_u16(NVS_CONFIG_FALLBACK_STRATUM_DIFFICULTY, CONFIG_FALLBACK_STRATUM_DIFFICULTY);
+
+    // set the pool extranonce subscribe
+    module->pool_extranonce_subscribe = nvs_config_get_u16(NVS_CONFIG_STRATUM_EXTRANONCE_SUBSCRIBE, STRATUM_EXTRANONCE_SUBSCRIBE);
+    module->fallback_pool_extranonce_subscribe = nvs_config_get_u16(NVS_CONFIG_FALLBACK_STRATUM_EXTRANONCE_SUBSCRIBE, FALLBACK_STRATUM_EXTRANONCE_SUBSCRIBE);
+
     // set fallback to false.
     module->is_using_fallback = false;
 
```
