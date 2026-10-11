# ESP-Miner PR #1743: Clean up SV2 NVS configuration

> Source: https://github.com/bitaxeorg/ESP-Miner/pull/1743
> Collected: 2026-10-10
> Published: 2026-06-01
> Registry ID: esp-miner

State: closed | Merged: 2026-06-02 | Author: mutatrum | +168/-142 | Labels: -

## Body

This should bring it more in line with the rest of the NVS config.

**Note**: this is a breaking change from beta3 and beta4. There's an upgrade path, but the downgrade path is not there. So if you install this, you most likely can't go back to beta3 or beta4 without a factory reset.

## Files changed

- `main/http_server/http_server.c` (+13/-61) — HTTP server + REST API handlers
- `main/nvs_config.c` (+36/-9) — NVS settings schema/keys
- `main/system.c` (+36/-4) — main app
- `main/http_server/system_api_json.c` (+13/-24) — HTTP server + REST API handlers
- `main/tasks/stratum_v2_task.c` (+15/-6) — Stratum V2 protocol task
- `main/tasks/create_jobs_task.c` (+7/-7) — firmware task module
- `main/tasks/protocol_coordinator.c` (+7/-7) — V1/V2 protocol coordinator task
- `main/global_state.h` (+6/-6) — shared global state structs/flags
- `main/nvs_config.h` (+6/-6) — NVS settings schema/keys
- `main/http_server/axe-os/src/app/components/home/home.component.ts` (+10/-1) — AxeOS Angular UI
- `main/http_server/axe-os/src/app/services/system.service.ts` (+6/-3) — AxeOS Angular service
- `components/stratum_v2/include/sv2_protocol.h` (+6/-2) — SV2 component (frames/Noise/protocol)
- `main/system.h` (+4/-0) — main app
- `main/http_server/openapi.yaml` (+0/-3) — OpenAPI spec
- `main/http_server/axe-os/src/app/components/home/home.component.html` (+1/-1) — AxeOS Angular UI
- `main/screen.c` (+1/-1) — display screen rendering
- `main/tasks/asic_result_task.c` (+1/-1) — firmware task module

## Key excerpts

### `main/tasks/stratum_v2_task.c` `@@ -77,11 +77,20 @@ static sv2_channel_type_t sv2_select_channel_type(GlobalState *GLOBAL_STATE, boo`

```diff
 {
     NvsConfigKey key = use_fallback ? NVS_CONFIG_FALLBACK_SV2_CHANNEL_TYPE
                                     : NVS_CONFIG_SV2_CHANNEL_TYPE;
-    uint16_t cfg = nvs_config_get_u16(key);
-    if (cfg == 1 && GLOBAL_STATE->DEVICE_CONFIG.family.asic.id != BM1397) {
-        return SV2_CHANNEL_STANDARD;
+    char *cfg_str = nvs_config_get_string(key);
+    sv2_channel_type_t type = SV2_CHANNEL_EXTENDED;  // default, and forced for BM1397
+    if (cfg_str) {
+        sv2_channel_type_t parsed = sv2_channel_type_from_string(cfg_str);
+        if (parsed == SV2_CHANNEL_STANDARD) {
+            if (GLOBAL_STATE->DEVICE_CONFIG.family.asic.id != BM1397) {
+                type = SV2_CHANNEL_STANDARD;
+            }
+        } else if (parsed == SV2_CHANNEL_UNKNOWN && cfg_str[0] != '\0') {
+            ESP_LOGW(TAG, "Invalid SV2 channel type in NVS: '%s', defaulting to extended", cfg_str);
+        }
+        free(cfg_str);
     }
-    return SV2_CHANNEL_EXTENDED;  // default, and forced for BM1397
+    return type;
 }
 
 void stratum_v2_close_connection(GlobalState *GLOBAL_STATE)
```

### `main/nvs_config.c` `@@ -112,15 +120,6 @@ static Settings settings[NVS_CONFIG_COUNT] = {`

```diff
     [NVS_CONFIG_TPS546]                                = {.nvs_key_name = "TPS546",          .type = TYPE_BOOL},
     [NVS_CONFIG_TMP1075]                               = {.nvs_key_name = "TMP1075",         .type = TYPE_BOOL},
     [NVS_CONFIG_POWER_CONSUMPTION_TARGET]              = {.nvs_key_name = "power_cons_tgt",  .type = TYPE_U16},
-    // Protocol and channel-type are TYPE_U16 internally but exposed as strings via the API
-    // (see http_server.c GET/PATCH special-case handling). rest_name is omitted so the generic
-    // PATCH loop does not handle them as numeric.
-    [NVS_CONFIG_STRATUM_PROTOCOL]                      = {.nvs_key_name = "stratumprot",     .type = TYPE_U16,   .default_value = {.u16 = 0},                           .min = 0,  .max = 1},
-    [NVS_CONFIG_SV2_AUTHORITY_PUBKEY]                  = {.nvs_key_name = "sv2authpubkey",   .type = TYPE_STR,   .default_value = {.str = ""},                           .rest_name = "stratumV2AuthorityPubkey",                 .min = 0,  .max = 52},
-    [NVS_CONFIG_FALLBACK_STRATUM_PROTOCOL]            = {.nvs_key_name = "fbstratumprot",   .type = TYPE_U16,   .default_value = {.u16 = 0},                            .min = 0,  .max = 1},
-    [NVS_CONFIG_FALLBACK_SV2_AUTHORITY_PUBKEY]        = {.nvs_key_name = "fbsv2authpubk",   .type = TYPE_STR,   .default_value = {.str = ""},                            .rest_name = "fallbackStratumV2AuthorityPubkey",          .min = 0,  .max = 52},
-    [NVS_CONFIG_SV2_CHANNEL_TYPE]                     = {.nvs_key_name = "sv2chantype",     .type = TYPE_U16,   .default_value = {.u16 = 0},                             .min = 0,  .max = 1},
-    [NVS_CONFIG_FALLBACK_SV2_CHANNEL_TYPE]            = {.nvs_key_name = "fbSv2ChanType",   .type = TYPE_U16,   .default_value = {.u16 = 0},                             .min = 0,  .max = 1},
 };
 
 Settings *nvs_config_get_settings(NvsConfigKey key)
```

### `main/http_server/system_api_json.c` `@@ -185,32 +177,29 @@ static void system_api_add_config(cJSON *root, GlobalState *g) {`

```diff
     free(f_cert);
     cJSON_AddBoolToObject(root, "fallbackStratumDecodeCoinbase", nvs_config_get_bool(NVS_CONFIG_FALLBACK_STRATUM_DECODE_COINBASE_TX));
 
-    cJSON_AddStringToObject(root, "stratumProtocol",
-                            stratum_protocol_to_string(nvs_config_get_u16(NVS_CONFIG_STRATUM_PROTOCOL)));
-
-    const char *protocol_label = "SV1";
-    if (g->stratum_protocol == STRATUM_V2) {
    …
-                            sv2_channel_type_to_string(nvs_config_get_u16(NVS_CONFIG_SV2_CHANNEL_TYPE)));
+    char *sv2_chan_type = nvs_config_get_string(NVS_CONFIG_SV2_CHANNEL_TYPE);
+    cJSON_AddStringToObject(root, "stratumV2ChannelType", sv2_chan_type ? sv2_chan_type : SV2_CHANNEL_TYPE_EXTENDED);
+    free(sv2_chan_type);
 
     char *fallbackSv2AuthPubkey = nvs_config_get_string(NVS_CONFIG_FALLBACK_SV2_AUTHORITY_PUBKEY);
     cJSON_AddStringToObject(root, "fallbackStratumV2AuthorityPubkey", fallbackSv2AuthPubkey ? fallbackSv2AuthPubkey : "");
     free(fallbackSv2AuthPubkey);
 
-    cJSON_AddStringToObject(root, "fallbackStratumV2ChannelType",
-                            sv2_channel_type_to_string(nvs_config_get_u16(NVS_CONFIG_FALLBACK_SV2_CHANNEL_TYPE)));
+    char *fallback_sv2_chan_type = nvs_config_get_string(NVS_CONFIG_FALLBACK_SV2_CHANNEL_TYPE);
+    cJSON_AddStringToObject(root, "fallbackStratumV2ChannelType", fallback_sv2_chan_type ? fallback_sv2_chan_type : SV2_CHANNEL_TYPE_EXTENDED);
+    free(fallback_sv2_chan_type);
 
-    cJSON_AddStringToObject(root, "fallbackStratumProtocol",
-                            stratum_protocol_to_string(nvs_config_get_u16(NVS_CONFIG_FALLBACK_STRATUM_PROTOCOL)));
+    char *fallback_proto = nvs_config_get_string(NVS_CONFIG_FALLBACK_STRATUM_PROTOCOL);
+    cJSON_AddStringToObject(root, "fallbackStratumProtocol", fallback_proto ? fallback_proto : STRATUM_V1);
+    free(fallback_proto);
[… hunk truncated: showing head + densest window of 44 diff lines]
```

### `main/http_server/http_server.c` `@@ -654,29 +629,6 @@ bool check_settings_and_update(const cJSON * const root)`

```diff
                     break;
             }
         }
-
-        // Special-case: protocol and channel-type are exposed as strings via the API
-        // (no rest_name in nvs_config table), parse to u16 here.
-        struct {
-            const char *json_key;
-            NvsConfigKey nvs_key;
-            int (*parse)(const char *, uint16_t *);
-        } string_enum_fields[] = {
-            { "stratumProtocol",              NVS_CONFIG_STRATUM_PROTOCOL,          stratum_protocol_from_string },
-            { "fallbackStratumProtocol",      NVS_CONFIG_FALLBACK_STRATUM_PROTOCOL, stratum_protocol_from_string },
-            { "stratumV2ChannelType",         NVS_CONFIG_SV2_CHANNEL_TYPE,          sv2_channel_type_from_string },
-            { "fallbackStratumV2ChannelType", NVS_CONFIG_FALLBACK_SV2_CHANNEL_TYPE, sv2_channel_type_from_string },
-        };
-        for (size_t i = 0; i < sizeof(string_enum_fields) / sizeof(string_enum_fields[0]); i++) {
-            cJSON *item = cJSON_GetObjectItem(root, string_enum_fields[i].json_key);
-            if (!item || !cJSON_IsString(item)) continue;
-            uint16_t v;
-            if (string_enum_fields[i].parse(item->valuestring, &v) == 0) {
-                nvs_config_set_u16(string_enum_fields[i].nvs_key, v);
-            } else {
-                ESP_LOGW(TAG, "Invalid value for %s: %s", string_enum_fields[i].json_key, item->valuestring);
-            }
-        }
     }
 
     return result;
```
