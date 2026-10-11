# ESP-Miner PR #336: Add stratum fallback support

> Source: https://github.com/bitaxeorg/ESP-Miner/pull/336
> Collected: 2026-10-10
> Published: 2024-09-11
> Registry ID: esp-miner

State: closed | Merged: 2024-10-05 | Author: eandersson | +376/-193 | Labels: enhancement, accepted

## Body

- Added fallback support.
- DNS will automatically update now in case the pool changes DNS.
- Tuning to TCP code to improve error handling.

## Files changed

- `main/tasks/stratum_task.c` (+234/-160) — firmware task module
- `main/http_server/axe-os/src/app/components/edit/edit.component.html` (+35/-11) — AxeOS Angular UI
- `main/Kconfig.projbuild` (+25/-0) — main app
- `components/stratum/stratum_api.c` (+9/-13) — stratum protocol component
- `main/http_server/http_server.c` (+19/-0) — HTTP server + REST API handlers
- `main/http_server/axe-os/src/app/components/home/home.component.html` (+12/-1) — AxeOS Angular UI
- `main/http_server/axe-os/src/app/components/edit/edit.component.ts` (+11/-0) — AxeOS Angular UI
- `main/tasks/asic_result_task.c` (+7/-3) — firmware task module
- `components/stratum/include/stratum_api.h` (+4/-4) — stratum protocol component
- `main/global_state.h` (+4/-1) — shared global state structs/flags
- `main/system.c` (+5/-0) — main app
- `main/nvs_config.h` (+4/-0) — NVS settings schema/keys
- `main/http_server/axe-os/src/app/services/system.service.ts` (+3/-0) — AxeOS Angular service
- `main/http_server/axe-os/src/models/ISystemInfo.ts` (+3/-0) — AxeOS web UI
- `main/tasks/stratum_task.h` (+1/-0) — firmware task module

## Key excerpts

### `main/http_server/http_server.c` `@@ -273,15 +273,27 @@ static esp_err_t PATCH_update_settings(httpd_req_t * req)`

```diff
     if ((item = cJSON_GetObjectItem(root, "stratumURL")) != NULL) {
         nvs_config_set_string(NVS_CONFIG_STRATUM_URL, item->valuestring);
     }
+    if ((item = cJSON_GetObjectItem(root, "fallbackStratumURL")) != NULL) {
+        nvs_config_set_string(NVS_CONFIG_FALLBACK_STRATUM_URL, item->valuestring);
+    }
     if ((item = cJSON_GetObjectItem(root, "stratumUser")) != NULL) {
         nvs_config_set_string(NVS_CONFIG_STRATUM_USER, item->valuestring);
     }
     if ((item = cJSON_GetObjectItem(root, "stratumPassword")) != NULL) {
         nvs_config_set_string(NVS_CONFIG_STRATUM_PASS, item->valuestring);
     }
+    if ((item = cJSON_GetObjectItem(root, "fallbackStratumUser")) != NULL) {
+        nvs_config_set_string(NVS_CONFIG_FALLBACK_STRATUM_USER, item->valuestring);
+    }
+    if ((item = cJSON_GetObjectItem(root, "fallbackStratumPassword")) != NULL) {
+        nvs_config_set_string(NVS_CONFIG_FALLBACK_STRATUM_PASS, item->valuestring);
+    }
     if ((item = cJSON_GetObjectItem(root, "stratumPort")) != NULL) {
         nvs_config_set_u16(NVS_CONFIG_STRATUM_PORT, item->valueint);
     }
+    if ((item = cJSON_GetObjectItem(root, "fallbackStratumPort")) != NULL) {
+        nvs_config_set_u16(NVS_CONFIG_FALLBACK_STRATUM_PORT, item->valueint);
+    }
     if ((item = cJSON_GetObjectItem(root, "ssid")) != NULL) {
         nvs_config_set_string(NVS_CONFIG_WIFI_SSID, item->valuestring);
     }
```

### `main/system.c` `@@ -76,9 +76,14 @@ static void _init_system(GlobalState * GLOBAL_STATE)`

```diff
     
     // set the pool url
     module->pool_url = nvs_config_get_string(NVS_CONFIG_STRATUM_URL, CONFIG_STRATUM_URL);
+    module->fallback_pool_url = nvs_config_get_string(NVS_CONFIG_FALLBACK_STRATUM_URL, CONFIG_FALLBACK_STRATUM_URL);
 
     //set the pool port
     module->pool_port = nvs_config_get_u16(NVS_CONFIG_STRATUM_PORT, CONFIG_STRATUM_PORT);
+    module->fallback_pool_port = nvs_config_get_u16(NVS_CONFIG_FALLBACK_STRATUM_PORT, CONFIG_FALLBACK_STRATUM_PORT);
+
+    // set fallback to false.
+    module->is_using_fallback = false;
 
     // Initialize overheat_mode
     module->overheat_mode = nvs_config_get_u16(NVS_CONFIG_OVERHEAT_MODE, 0);
```

### `main/tasks/stratum_task.c` `@@ -63,177 +56,258 @@ void cleanQueue(GlobalState * GLOBAL_STATE) {`

```diff
     pthread_mutex_unlock(&GLOBAL_STATE->valid_jobs_lock);
 }
 
+void stratum_close_connection(GlobalState * GLOBAL_STATE)
+{
+    if (GLOBAL_STATE->sock < 0) {
+        ESP_LOGE(TAG, "Socket already shutdown, not shutting down again..");
+        return;
    …
+        STRATUM_V1_reset_uid();
+        cleanQueue(GLOBAL_STATE);
 
-            char * username = nvs_config_get_string(NVS_CONFIG_STRATUM_USER, STRATUM_USER);
-            char * password = nvs_config_get_string(NVS_CONFIG_STRATUM_PASS, STRATUM_PW);
+        ///// Start Stratum Action
+        // mining.subscribe - ID: 1
+        STRATUM_V1_subscribe(GLOBAL_STATE->sock, GLOBAL_STATE->asic_model_str);
 
-            //mining.authorize - ID: 3
-            STRATUM_V1_authenticate(GLOBAL_STATE->sock, username, password);
-            free(password);
-            free(username);
+        // mining.configure - ID: 2
+        STRATUM_V1_configure_version_rolling(GLOBAL_STATE->sock, &GLOBAL_STATE->version_mask);
 
-            //mining.suggest_difficulty - ID: 4
-            STRATUM_V1_suggest_difficulty(GLOBAL_STATE->sock, STRATUM_DIFFICULTY);
+        char * username = GLOBAL_STATE->SYSTEM_MODULE.is_using_fallback ? nvs_config_get_string(NVS_CONFIG_FALLBACK_STRATUM_USER, FALLBACK_STRATUM_USER) : nvs_config_get_string(NVS_CONFIG_STRATUM_USER, STRATUM_USER);
+        char * password = GLOBAL_STATE->SYSTEM_MODULE.is_using_fallback ? nvs_config_get_string(NVS_CONFIG_FALLBACK_STRATUM_PASS, FALLBACK_STRATUM_PW) : nvs_config_get_string(NVS_CONFIG_STRATUM_PASS, STRATUM_PW);
[… hunk truncated: showing head + densest window of 401 diff lines]
```

### `main/nvs_config.h` `@@ -10,8 +10,12 @@`

```diff
 #define NVS_CONFIG_HOSTNAME "hostname"
 #define NVS_CONFIG_STRATUM_URL "stratumurl"
 #define NVS_CONFIG_STRATUM_PORT "stratumport"
+#define NVS_CONFIG_FALLBACK_STRATUM_URL "fbstratumurl"
+#define NVS_CONFIG_FALLBACK_STRATUM_PORT "fbstratumport"
 #define NVS_CONFIG_STRATUM_USER "stratumuser"
 #define NVS_CONFIG_STRATUM_PASS "stratumpass"
+#define NVS_CONFIG_FALLBACK_STRATUM_USER "fbstratumuser"
+#define NVS_CONFIG_FALLBACK_STRATUM_PASS "fbstratumpass"
 #define NVS_CONFIG_ASIC_FREQ "asicfrequency"
 #define NVS_CONFIG_ASIC_VOLTAGE "asicvoltage"
 #define NVS_CONFIG_ASIC_MODEL "asicmodel"
```
