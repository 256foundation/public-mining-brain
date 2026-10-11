# ESP-Miner PR #1413: Add TLS support

> Source: https://github.com/bitaxeorg/ESP-Miner/pull/1413
> Collected: 2026-10-10
> Published: 2025-12-01
> Registry ID: esp-miner

State: closed | Merged: 2025-12-11 | Author: mutatrum | +536/-159 | Labels: enhancement

## Body

Rebase of #726

<img width="1964" height="1470" alt="Screenshot" src="https://github.com/user-attachments/assets/82f08563-98e0-4c51-a791-1668a2304806" />

<img width="429" height="192" alt="image" src="https://github.com/user-attachments/assets/93b63ffb-38ea-4774-92f1-7b6a9e8d03fc" />

Pools with TLS:

stratum+tls://public-pool.io:4333
```
I (14255) stratum_task: Opening connection to pool: public-pool.io:4333
I (14265) stratum_api: Using TLS transport
I (14285) stratum_api: Using default cert bundle
I (14295) stratum_task: Transport initialized, connecting to public-pool.io:4333
I (15685) esp-x509-crt-bundle: Certificate validated
```

stratum+tls://pool.noderunners.network:1336
```
I (14322) stratum_task: Opening connection to pool: pool.noderunners.network:1336
I (14330) stratum_api: Using TLS transport
I (14350) stratum_api: Using default cert bundle
I (14358) stratum_task: Transport initialized, connecting to pool.noderunners.network:1336
I (14987) esp-x509-crt-bundle: Certificate validated
```

stratum+tls://solo.atlaspool.io:4333
<img width="441" height="112" alt="image" src="https://github.com/user-attachments/assets/40126100-30c2-406a-9c2c-69c21caa9f0a" />

I didn't test the Custom CA Certificate option. I also couldn't test IPv6, with or without TLS, as my ISP doesn't support that. I don't know of any IPv6 pool with TLS.

Not sure if we need to add the options to every config file.

## Files changed

- `main/tasks/stratum_task.c` (+70/-57) — firmware task module
- `main/http_server/axe-os/src/app/components/pool/pool.component.ts` (+98/-7) — AxeOS Angular UI
- `components/stratum/stratum_api.c` (+78/-18) — stratum protocol component
- `main/http_server/axe-os/src/app/components/pool/pool.component.html` (+71/-21) — AxeOS Angular UI
- `main/Kconfig.projbuild` (+56/-0) — main app
- `components/stratum/include/stratum_api.h` (+16/-8) — stratum protocol component
- `main/http_server/axe-os/src/app/components/home/home.component.html` (+6/-8) — AxeOS Angular UI
- `main/http_server/axe-os/src/app/components/home/home.component.ts` (+0/-14) — AxeOS Angular UI
- `main/global_state.h` (+10/-3) — shared global state structs/flags
- `main/http_server/http_server.c` (+10/-2) — HTTP server + REST API handlers
- `main/system.c` (+10/-2) — main app
- `main/http_server/axe-os/src/styles.scss` (+7/-1) — AxeOS web UI
- `main/http_server/axe-os/src/app/components/logs/logs.component.scss` (+0/-7) — AxeOS Angular UI
- `main/http_server/axe-os/src/app/services/system.service.ts` (+5/-1) — AxeOS Angular service
- `main/http_server/axe-os/src/models/ISystemInfo.ts` (+5/-1) — AxeOS web UI
- `main/http_server/axe-os/src/app/components/home/home.component.scss` (+0/-5) — AxeOS Angular UI
- `config-102.cvs` (+4/-0) — changed file
- `config-201.cvs` (+4/-0) — changed file
- `config-202.cvs` (+4/-0) — changed file
- `config-203.cvs` (+4/-0) — changed file
- `config-204.cvs` (+4/-0) — changed file
- `config-205.cvs` (+4/-0) — changed file
- `config-207.cvs` (+4/-0) — changed file
- `config-302.cvs` (+4/-0) — changed file
- `config-303.cvs` (+4/-0) — changed file
- `config-400.cvs` (+4/-0) — changed file
- `config-401.cvs` (+4/-0) — changed file
- `config-402.cvs` (+4/-0) — changed file
- `config-403.cvs` (+4/-0) — changed file
- `config-601.cvs` (+4/-0) — changed file
- `config-602.cvs` (+4/-0) — changed file
- `config-701.cvs` (+4/-0) — changed file
- `config-702.cvs` (+4/-0) — changed file
- `config-800x.cvs` (+4/-0) — changed file
- `config.cvs.example` (+4/-0) — example config
- `main/http_server/axe-os/src/app/prime-ng.module.ts` (+3/-1) — AxeOS Angular UI
- `main/nvs_config.c` (+4/-0) — NVS settings schema/keys
- `main/nvs_config.h` (+4/-0) — NVS settings schema/keys
- `components/stratum/CMakeLists.txt` (+2/-1) — stratum protocol component
- `main/http_server/axe-os/src/app/components/logs/logs.component.ts` (+1/-1) — AxeOS Angular UI
- `main/tasks/asic_result_task.c` (+1/-1) — firmware task module
- `components/asic/CMakeLists.txt` (+1/-0) — changed file
- `main/CMakeLists.txt` (+1/-0) — main app
- `sdkconfig.defaults` (+1/-0) — changed file

## Key excerpts

### `components/stratum/stratum_api.c` `@@ -73,6 +78,46 @@ double STRATUM_V1_get_response_time_ms(int request_id)`

```diff
 static void debug_stratum_tx(const char *);
 int _parse_stratum_subscribe_result_message(const char * result_json_str, char ** extranonce, int * extranonce2_len);
 
+esp_transport_handle_t STRATUM_V1_transport_init(tls_mode tls, char * cert)
+{
+    esp_transport_handle_t transport;
+    // tls_transport
+    if (tls == DISABLED)
    …
+    {
+        // tcp_transport
+        ESP_LOGI(TAG, "TLS disabled, Using TCP transport");
+        transport = esp_transport_tcp_init();
+    }
+    else{
+        // tls_transport
+        ESP_LOGI(TAG, "Using TLS transport");
+        transport = esp_transport_ssl_init();
+        if (transport == NULL) {
+            ESP_LOGE(TAG, "Failed to initialize SSL transport");
+            return NULL;
+        }
+        switch(tls){
+            case BUNDLED_CRT:
+                ESP_LOGI(TAG, "Using default cert bundle");
+                esp_transport_ssl_crt_bundle_attach(transport, esp_crt_bundle_attach);
+                break;
+            case CUSTOM_CRT:
+                ESP_LOGI(TAG, "Using custom cert");
[… hunk truncated: showing head + densest window of 46 diff lines]
```

### `main/nvs_config.c` `@@ -54,12 +54,16 @@ static Settings settings[NVS_CONFIG_COUNT] = {`

```diff
     [NVS_CONFIG_STRATUM_PASS]                          = {.nvs_key_name = "stratumpass",     .type = TYPE_STR,   .default_value = {.str = (char *)CONFIG_STRATUM_PW},                   .rest_name = "stratumPassword",                    .min = 0,  .max = NVS_STR_LIMIT},
     [NVS_CONFIG_STRATUM_DIFFICULTY]                    = {.nvs_key_name = "stratumdiff",     .type = TYPE_U16,   .default_value = {.u16 = CONFIG_STRATUM_DIFFICULTY},                   .rest_name = "stratumSuggestedDifficulty",         .min = 0,  .max = UINT16_MAX},
     [NVS_CONFIG_STRATUM_EXTRANONCE_SUBSCRIBE]          = {.nvs_key_name = "stratumxnsub",    .type = TYPE_BOOL,  .default_value = {.b   = (bool)STRATUM_EXTRANONCE_SUBSCRIBE},          .rest_name = "stratumExtranonceSubscribe",         .min = 0,  .max = 1},
+    [NVS_CONFIG_STRATUM_TLS]                           = {.nvs_key_name = "stratumtls",      .type = TYPE_U16,   .default_value = {.u16 = (uint16_t)CONFIG_STRATUM_TLS},                .rest_name = "stratumTLS",                         .min = 0,  .max = 3},
+    [NVS_CONFIG_STRATUM_CERT]                          = {.nvs_key_name = "stratumcert",     .type = TYPE_STR,   .default_value = {.str = (char *)CONFIG_STRATUM_CERT},                 .rest_name = "stratumCert",                        .min = 0,  .max = NVS_STR_LIMIT},
     [NVS_CONFIG_FALLBACK_STRATUM_URL]                  = {.nvs_key_name = "fbstratumurl",    .type = TYPE_STR,   .default_value = {.str = (char *)CONFIG_FALLBACK_STRATUM_URL},         .rest_name = "fallbackStratumURL",                 .min = 0,  .max = NVS_STR_LIMIT},
     [NVS_CONFIG_FALLBACK_STRATUM_PORT]                 = {.nvs_key_name = "fbstratumport",   .type = TYPE_U16,   .default_value = {.u16 = CONFIG_FALLBACK_STRATUM_PORT},                .rest_name = "fallbackStratumPort",                .min = 0,  .max = UINT16_MAX},
     [NVS_CONFIG_FALLBACK_STRATUM_USER]                 = {.nvs_key_name = "fbstratumuser",   .type = TYPE_STR,   .default_value = {.str = (char *)CONFIG_FALLBACK_STRATUM_USER},        .rest_name = "fallbackStratumUser",                .min = 0,  .max = NVS_STR_LIMIT},
     [NVS_CONFIG_FALLBACK_STRATUM_PASS]                 = {.nvs_key_name = "fbstratumpass",   .type = TYPE_STR,   .default_value = {.str = (char *)CONFIG_FALLBACK_STRATUM_PW},          .rest_name = "fallbackStratumPassword",            .min = 0,  .max = NVS_STR_LIMIT},
     [NVS_CONFIG_FALLBACK_STRATUM_DIFFICULTY]           = {.nvs_key_name = "fbstratumdiff",   .type = TYPE_U16,   .default_value = {.u16 = CONFIG_FALLBACK_STRATUM_DIFFICULTY},          .rest_name = "fallbackStratumSuggestedDifficulty", .min = 0,  .max = UINT16_MAX},
     [NVS_CONFIG_FALLBACK_STRATUM_EXTRANONCE_SUBSCRIBE] = {.nvs_key_name = "stratumfbxnsub",  .type = TYPE_BOOL,  .default_value = {.b   = (bool)FALLBACK_STRATUM_EXTRANONCE_SUBSCRIBE}, .rest_name = "fallbackStratumExtranonceSubscribe", .min = 0,  .max = 1},
+    [NVS_CONFIG_FALLBACK_STRATUM_TLS]                  = {.nvs_key_name = "fbstratumtls",    .type = TYPE_U16,   .default_value = {.u16 = (uint16_t)CONFIG_FALLBACK_STRATUM_TLS},       .rest_name = "fallbackStratumTLS",                 .min = 0,  .max = 3},
+    [NVS_CONFIG_FALLBACK_STRATUM_CERT]                 = {.nvs_key_name = "fbstratumcert",   .type = TYPE_STR,   .default_value = {.str = (char *)CONFIG_FALLBACK_STRATUM_CERT},        .rest_name = "fallbackStratumCert",                .min = 0,  .max = NVS_STR_LIMIT},
     [NVS_CONFIG_USE_FALLBACK_STRATUM]                  = {.nvs_key_name = "usefbstartum",    .type = TYPE_BOOL,                                                                         .rest_name = "useFallbackStratum",                 .min = 0,  .max = 1},
 
     [NVS_CONFIG_ASIC_FREQUENCY]                        = {.nvs_key_name = "asicfrequency_f", .type = TYPE_FLOAT, .default_value = {.f   = CONFIG_ASIC_FREQUENCY},                       .rest_name = "frequency",                          .min = 1,  .max = UINT16_MAX},
```

### `main/http_server/axe-os/src/app/components/pool/pool.component.ts` `@@ -122,15 +159,24 @@ export class PoolComponent implements OnInit {`

```diff
   public onUrlChange(poolType: PoolType) {
     const urlControl = this.form.get(`${poolType}URL`);
     const portControl = this.form.get(`${poolType}Port`);
-    if (!urlControl || !portControl) return;
+    const tlsControl = this.form.get(`${poolType}TLS`);
+    if (!urlControl || !portControl || !tlsControl) return;
 
-    let urlValue = urlControl.value || '';
+    let urlValue = urlControl.value.trim() || '';
 
     if (!urlValue) return;
 
-    const prefix = 'stratum+tcp://';
-    if (urlValue.startsWith(prefix)) {
-      urlValue = urlValue.slice(prefix.length);
+    const prefixes = [
+      { prefix: 'stratum+tcp://', tlsMode: false },
+      { prefix: 'stratum+tls://', tlsMode: true },
+      { prefix: 'stratum+ssl://', tlsMode: true }
+    ] as const;
+
+    let isTlsMode = 0;
+    const matched = prefixes.find(({ prefix }) => urlValue.startsWith(prefix));
+    if (matched) {
+      urlValue = urlValue.slice(matched.prefix.length);
+      isTlsMode = +matched.tlsMode;
     }
 
     const { cleanUrl, port } = this.extractPort(urlValue);
```

### `main/system.c` `@@ -62,6 +62,14 @@ void SYSTEM_init_system(GlobalState * GLOBAL_STATE)`

```diff
     module->pool_port = nvs_config_get_u16(NVS_CONFIG_STRATUM_PORT);
     module->fallback_pool_port = nvs_config_get_u16(NVS_CONFIG_FALLBACK_STRATUM_PORT);
 
+    // set the pool tls
+    module->pool_tls = nvs_config_get_u16(NVS_CONFIG_STRATUM_TLS);
+    module->fallback_pool_tls = nvs_config_get_u16(NVS_CONFIG_FALLBACK_STRATUM_TLS);
+
+    // set the pool cert
+    module->pool_cert = nvs_config_get_string(NVS_CONFIG_STRATUM_CERT);
+    module->fallback_pool_cert = nvs_config_get_string(NVS_CONFIG_FALLBACK_STRATUM_CERT);
+
     // set the pool user
     module->pool_user = nvs_config_get_string(NVS_CONFIG_STRATUM_USER);
     module->fallback_pool_user = nvs_config_get_string(NVS_CONFIG_FALLBACK_STRATUM_USER);
```
