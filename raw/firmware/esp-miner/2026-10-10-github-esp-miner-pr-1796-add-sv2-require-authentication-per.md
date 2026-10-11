# ESP-Miner PR #1796: Add SV2 "require authentication" per-pool option

> Source: https://github.com/bitaxeorg/ESP-Miner/pull/1796
> Collected: 2026-10-10
> Published: 2026-07-01
> Registry ID: esp-miner

State: closed | Merged: 2026-08-08 | Author: cbyam | +56/-8 | Labels: enhancement

## Body

## Summary

Addresses the second gap in #1786. By default SV2 connects encrypted but
unauthenticated: with no authority pubkey set, the Noise_NX handshake takes
the "no authority pubkey" branch and mines anyway, so the user can't act on
the man-in-the-middle warning the UI shows on the Authority Pubkey field.

This adds a per-pool "Require Authentication" toggle. When it's on and no
authority pubkey is set, the SV2 task refuses to connect instead of falling
through to an unverifiable server. The verify path is unchanged.

## Changes

- New per-pool NVS bool `stratumV2RequireAuth` / `fallbackStratumV2RequireAuth`,
  default false, so existing configs behave as before.
- `stratum_v2_task` refuses to connect when auth is required but no pubkey
  resolves (status shows `SV2: Auth required - no key`).
- REST config exposes the new booleans; `openapi.yaml` updated.
- Frontend checkbox next to the Authority Pubkey field, with a tooltip pointing
  back to the MITM warning.

## Scope

Just the enforcement toggle, the small fix offered in #1786. The validity-window
check and boot-time SNTP clock from that issue are not here.

## Testing

- AxeOS production build passes (`ng build --configuration=production`).
- Each changed C file passes a syntax and semantic compile under ESP-IDF v5.4,
  and `sv2_noise.c` compiles to an object in a full build. A complete link needs
  v5.5.3 (the CI toolchain) because of a pre-existing `esp_transport_get_socket`
  call elsewhere in the tree, so the final .bin is left to CI. Not flashed to
  hardware yet.

## Files changed

- `main/tasks/stratum_v2_task.c` (+16/-1) — Stratum V2 protocol task
- `main/http_server/axe-os/src/app/components/pool/pool.component.html` (+14/-0) — AxeOS Angular UI
- `main/http_server/axe-os/src/app/components/pool/pool.component.ts` (+8/-4) — AxeOS Angular UI
- `main/http_server/axe-os/src/app/services/system.service.ts` (+4/-2) — AxeOS Angular service
- `main/system.c` (+6/-0) — main app
- `main/http_server/openapi.yaml` (+3/-0) — OpenAPI spec
- `main/http_server/system_api_json.c` (+2/-1) — HTTP server + REST API handlers
- `main/http_server/http_server.c` (+2/-0) — HTTP server + REST API handlers
- `main/global_state.h` (+1/-0) — shared global state structs/flags

## Key excerpts

### `main/tasks/stratum_v2_task.c` `@@ -714,9 +714,24 @@ void stratum_v2_task(void *pvParameters)`

```diff
         }
         GLOBAL_STATE->sv2_noise_ctx = noise_ctx;
 
-        // Load optional authority pubkey from NVS
+        // Load the optional authority pubkey and whether this pool requires it
         uint8_t auth_key[32];
         bool has_auth = stratum_v2_load_authority_pubkey(GLOBAL_STATE, auth_key, use_fallback);
+        uint16_t auth_pool_idx = use_fallback ? GLOBAL_STATE->SYSTEM_MODULE.secondary_pool_index
+                                              : GLOBAL_STATE->SYSTEM_MODULE.primary_pool_index;
+        bool require_auth = GLOBAL_STATE->SYSTEM_MODULE.pools[auth_pool_idx].sv2_require_auth;
+
+        // When auth is required but no usable authority key is configured,
+        // refuse to connect rather than mine against an unverifiable server
+        if (require_auth && !has_auth) {
+            ESP_LOGE(TAG, "SV2 authentication required but no authority pubkey configured, refusing to connect");
+            snprintf(GLOBAL_STATE->SYSTEM_MODULE.pool_connection_info,
+                     sizeof(GLOBAL_STATE->SYSTEM_MODULE.pool_connection_info), "SV2: Auth required - no key");
+            stratum_v2_close_connection(GLOBAL_STATE);
+            retry_attempts++;
+            continue;
+        }
+
         if (has_auth) {
             ESP_LOGI(TAG, "Authority pubkey configured, will verify server certificate");
         } else {
```

### `main/system.c` `@@ -136,6 +137,11 @@ static void parse_pool_config_json(const char *json_str, PoolConfig *cfg, int in`

```diff
         cfg->sv2_authority_pubkey = strdup(item->valuestring);
     }
 
+    item = cJSON_GetObjectItem(root, "stratumV2RequireAuth");
+    if (item && (cJSON_IsBool(item) || cJSON_IsNumber(item))) {
+        cfg->sv2_require_auth = cJSON_IsTrue(item) || (cJSON_IsNumber(item) && item->valueint != 0);
+    }
+
     cJSON_Delete(root);
 }
 
```

### `main/http_server/system_api_json.c` `@@ -181,7 +181,8 @@ static void system_api_add_config(cJSON *root, GlobalState *g) {`

```diff
             cJSON_AddBoolToObject(p_obj, "stratumDecodeCoinbase", p->decode_coinbase_tx);
             cJSON_AddStringToObject(p_obj, "stratumV2ChannelType", p->sv2_channel_type == SV2_CHANNEL_STANDARD ? SV2_CHANNEL_TYPE_STANDARD : SV2_CHANNEL_TYPE_EXTENDED);
             cJSON_AddStringToObject(p_obj, "stratumV2AuthorityPubkey", p->sv2_authority_pubkey ? p->sv2_authority_pubkey : "");
-            
+            cJSON_AddBoolToObject(p_obj, "stratumV2RequireAuth", p->sv2_require_auth);
+
             cJSON_AddItemToArray(pools_arr, p_obj);
         }
     }
```

### `main/global_state.h` `@@ -38,6 +38,7 @@ typedef struct PoolConfig`

```diff
     bool decode_coinbase_tx;
     uint16_t sv2_channel_type;
     char * sv2_authority_pubkey;
+    bool sv2_require_auth;
 } PoolConfig;
 
 #define HISTORY_LENGTH 100
```
