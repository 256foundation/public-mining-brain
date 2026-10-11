# ESP-Miner PR #1553: Add Stratum V2 (SV2) protocol support

> Source: https://github.com/bitaxeorg/ESP-Miner/pull/1553
> Collected: 2026-10-10
> Published: 2026-02-14
> Registry ID: esp-miner

State: closed | Merged: 2026-05-16 | Author: warioishere | +3838/-288 | Labels: enhancement

## Body

## Summary

Adds Stratum V2 binary protocol support alongside the existing V1 JSON-RPC implementation. Tested on a BM1370 bitaxe against a local SRI server and the SRI reference pool — full 1.3 TH/s hashrate with shares accepted.

**What's included:**
- SV2 binary protocol: frame encoding/decoding, mining channel messages (SetupConnection, OpenStandardMiningChannel, NewMiningJob, SetNewPrevHash, SetTarget, SubmitSharesStandard)
- SV2 Noise encryption: Noise_NX handshake with ChaCha20-Poly1305 transport via libsecp256k1 (git submodule v0.6.0)
- Protocol coordinator with separate V1/V2 task files and fallback/recovery logic
- Protocol selectable via NVS config and AxeOS Pool Settings UI (both primary and fallback pool)

**What works:**
- Full hashrate (1.3 TH/s on BM1370)
- Encrypted connection via Noise protocol
- Share submission and acceptance
- Pool difficulty tracking via SetTarget
- V1/V2 protocol switching and fallback

## Open decisions

none

## Test plan

- [x] SV2 connection + Noise handshake against SRI server
- [x] Full hashrate (1.3 TH/s) with BM1370
- [x] Shares accepted, no duplicates
- [x] Dashboard loads in SV2 mode
- [x] V1 mode unaffected
- [x] Tested against SRI reference pool
- [x] Test on other ASIC variants (BM1366, BM1368, BM1397)

## Test servers

Our own server (confirmed working):
- **Host:** `blitzpool.yourdevice.ch`
- **Port:** `3333`
- **Authority Public Key:** `9bCoFxTszKCuffyywH5uS5o6WcU4vsjTH2axxc7wE86y2HhvULU`
- **running on mainnet**

SRI reference pool (confirmed working):
- **Host:** `75.119.150.111`
- **Port:** `3333`
- **Authority Public Key:** `9auqWEzQDVyd2oe1JVGFLMLHZtCo2FFqZwtKA5gd9xbuEu7PH72`

**For transparency: most of this implementation was done with the help of Claude (Opus 4.6). I hope that doesn't detract from the goal of bringing SV2 support to bitaxe.**

## Files changed

- `main/tasks/stratum_v2_task.c` (+984/-0) — Stratum V2 protocol task
- `components/stratum_v2/sv2_noise.c` (+591/-0) — SV2 component (frames/Noise/protocol)
- `components/stratum_v2/sv2_protocol.c` (+554/-0) — SV2 component (frames/Noise/protocol)
- `main/tasks/protocol_coordinator.c` (+422/-0) — V1/V2 protocol coordinator task
- `main/tasks/create_jobs_task.c` (+297/-18) — firmware task module
- `main/http_server/axe-os/src/app/components/pool/pool.component.html` (+159/-63) — AxeOS Angular UI
- `main/tasks/stratum_v1_task.c` (+69/-138) — Stratum V1 protocol task
- `components/stratum_v2/include/sv2_protocol.h` (+198/-0) — SV2 component (frames/Noise/protocol)
- `main/http_server/http_server.c` (+102/-1) — HTTP server + REST API handlers
- `main/tasks/asic_result_task.c` (+61/-30) — firmware task module
- `main/http_server/axe-os/src/app/components/pool/pool.component.ts` (+73/-2) — AxeOS Angular UI
- `main/http_server/openapi.yaml` (+66/-0) — OpenAPI spec
- `components/stratum_v2/include/sv2_noise.h` (+38/-0) — SV2 component (frames/Noise/protocol)
- `main/screen.c` (+21/-10) — display screen rendering
- `main/tasks/protocol_coordinator.h` (+27/-0) — V1/V2 protocol coordinator task
- `components/stratum/mining.c` (+20/-4) — stratum protocol component
- `main/global_state.h` (+18/-0) — shared global state structs/flags
- `main/tasks/stratum_v2_task.h` (+16/-0) — Stratum V2 protocol task
- `components/libsecp256k1/CMakeLists.txt` (+15/-0) — vendored libsecp256k1 (SV2 Noise crypto)
- `readme.md` (+14/-1) — documentation
- `main/main.c` (+6/-7) — main app
- `main/http_server/axe-os/src/app/components/home/home.component.ts` (+9/-1) — AxeOS Angular UI
- `main/work_queue.c` (+8/-2) — ASIC work queue
- `main/nvs_config.c` (+9/-0) — NVS settings schema/keys
- `main/tasks/stratum_v1_task.h` (+9/-0) — Stratum V1 protocol task
- `main/system.c` (+7/-0) — main app
- `main/tasks/stratum_task.h` (+0/-7) — firmware task module
- `components/stratum/include/mining.h` (+6/-0) — stratum protocol component
- `main/http_server/axe-os/src/app/components/home/home.component.html` (+6/-0) — AxeOS Angular UI
- `main/nvs_config.h` (+6/-0) — NVS settings schema/keys
- `components/stratum_v2/CMakeLists.txt` (+5/-0) — SV2 component (frames/Noise/protocol)
- `main/CMakeLists.txt` (+4/-1) — main app
- `main/work_queue.h` (+2/-2) — ASIC work queue
- `.gitmodules` (+3/-0) — changed file
- `components/stratum/stratum_api.c` (+3/-0) — stratum protocol component
- `main/http_server/axe-os/src/app/services/system.service.ts` (+3/-0) — AxeOS Angular service
- `sdkconfig.defaults` (+3/-0) — changed file
- `components/stratum/include/utils.h` (+2/-0) — stratum protocol component
- `components/stratum/utils.c` (+1/-1) — stratum protocol component
- `components/libsecp256k1/libsecp256k1` (+1/-0) — vendored libsecp256k1 (SV2 Noise crypto)

## Key excerpts

### `components/stratum_v2/include/sv2_protocol.h` `@@ -0,0 +1,198 @@`

```diff
+#ifndef SV2_PROTOCOL_H
+#define SV2_PROTOCOL_H
+
+#include <stdint.h>
+#include <stdbool.h>
+#include <stddef.h>
+
+// Frame header size (extension_type[2] + msg_type[1] + msg_length[3])
    …
+#define SV2_FRAME_HEADER_SIZE 6
+
+// Common message types
+#define SV2_MSG_SETUP_CONNECTION                        0x00
+#define SV2_MSG_SETUP_CONNECTION_SUCCESS                0x01
+#define SV2_MSG_SETUP_CONNECTION_ERROR                  0x02
+
+// Mining protocol message types (values from SV2 spec / SRI reference)
+#define SV2_MSG_OPEN_STANDARD_MINING_CHANNEL            0x10
+#define SV2_MSG_OPEN_STANDARD_MINING_CHANNEL_SUCCESS    0x11
+#define SV2_MSG_OPEN_MINING_CHANNEL_ERROR               0x12
+#define SV2_MSG_OPEN_EXTENDED_MINING_CHANNEL            0x13
+#define SV2_MSG_OPEN_EXTENDED_MINING_CHANNEL_SUCCESS    0x14
+#define SV2_MSG_NEW_MINING_JOB                          0x15
+#define SV2_MSG_NEW_EXTENDED_MINING_JOB                 0x1f
+#define SV2_MSG_SUBMIT_SHARES_STANDARD                  0x1a
+#define SV2_MSG_SUBMIT_SHARES_EXTENDED                  0x1b
+#define SV2_MSG_SUBMIT_SHARES_SUCCESS                   0x1c
+#define SV2_MSG_SUBMIT_SHARES_ERROR                     0x1d
+#define SV2_MSG_SET_NEW_PREV_HASH                       0x20
+#define SV2_MSG_SET_TARGET                              0x21
+
+#define SV2_MAX_MERKLE_BRANCHES 20
+
+// Extension type flag for channel messages
+#define SV2_CHANNEL_MSG_FLAG 0x8000
+
+// Channel type selection
[… hunk truncated: showing head + densest window of 198 diff lines]
```

### `main/tasks/asic_result_task.c` `@@ -60,36 +60,67 @@ void ASIC_result_task(void *pvParameters)`

```diff
         uint32_t version_bits = asic_result->rolled_version ^ active_job->version;
         if (nonce_diff >= active_job->pool_diff)
         {
-            char * user = GLOBAL_STATE->SYSTEM_MODULE.is_using_fallback ? GLOBAL_STATE->SYSTEM_MODULE.fallback_pool_user : GLOBAL_STATE->SYSTEM_MODULE.pool_user;
-
-            taskENTER_CRITICAL(&GLOBAL_STATE->stratum_mux);
-            esp_transport_handle_t transport = GLOBAL_STATE->transport;
-            int uid = GLOBAL_STATE->send_uid++;
    …
+                if (stratum_v2_is_extended_channel(GLOBAL_STATE)) {
+                    sv2_conn_t *conn = GLOBAL_STATE->sv2_conn;
+                    // SV2 spec: extranonce_size is the miner's rollable portion.
+                    // The pool prepends its extranonce_prefix separately.
+                    uint8_t en2_len = conn->extranonce_size;
+                    uint8_t extranonce_2[32];
+                    hex2bin(active_job->extranonce2, extranonce_2, en2_len);
+                    ret = stratum_v2_submit_share_extended(GLOBAL_STATE, sv2_job_id,
+                                                           asic_result->nonce,
+                                                           active_job->ntime,
+                                                           asic_result->rolled_version,
+                                                           extranonce_2, en2_len);
+                } else {
+                    ret = stratum_v2_submit_share(GLOBAL_STATE, sv2_job_id,
+                                                   asic_result->nonce,
+                                                   active_job->ntime,
+                                                   asic_result->rolled_version);
+                }
 
                 if (ret < 0) {
-                    ESP_LOGW(TAG, "Unable to write share to socket (ret: %d, errno %d: %s)", ret, errno, strerror(errno));
-                    // stratum_task recv loop will detect a broken connection on its next read and handle reconnection
+                    ESP_LOGW(TAG, "Failed to submit SV2 share (ret=%d, errno=%d: %s)",
+                             ret, errno, strerror(errno));
+                }
+            } else {
+                // V1: submit with JSON-RPC
+                char * user = GLOBAL_STATE->SYSTEM_MODULE.is_using_fallback ? GLOBAL_STATE->SYSTEM_MODULE.fallback_pool_user : GLOBAL_STATE->SYSTEM_MODULE.pool_user;
[… hunk truncated: showing head + densest window of 94 diff lines]
```

### `components/stratum_v2/include/sv2_noise.h` `@@ -0,0 +1,38 @@`

```diff
+#ifndef SV2_NOISE_H
+#define SV2_NOISE_H
+
+#include <stdint.h>
+#include <stdbool.h>
+#include "esp_transport.h"
+
+typedef struct sv2_noise_ctx sv2_noise_ctx_t;
+
+// Create a new Noise context (allocates secp256k1 context internally).
+sv2_noise_ctx_t *sv2_noise_create(void);
+
+// Destroy a Noise context and free all resources.
+void sv2_noise_destroy(sv2_noise_ctx_t *ctx);
+
+// Perform Noise_NX handshake as initiator over the given transport.
+// authority_pubkey is an optional 32-byte x-only public key for Schnorr
+// signature verification of the responder's certificate. Pass NULL to skip.
+// Returns 0 on success, -1 on error.
+int sv2_noise_handshake(sv2_noise_ctx_t *ctx, esp_transport_handle_t transport,
+                        const uint8_t *authority_pubkey);
+
+// Send an SV2 frame (header + payload) encrypted via Noise.
+// frame points to the complete plaintext frame (header + payload).
+// Returns 0 on success, -1 on error.
+int sv2_noise_send(sv2_noise_ctx_t *ctx, esp_transport_handle_t transport,
+                   const uint8_t *frame, int frame_len);
+
+// Receive and decrypt an SV2 frame via Noise.
+// hdr_out receives the 6-byte decrypted frame header.
+// payload_out receives the decrypted payload (up to max_payload_len bytes).
+// payload_len_out receives the actual payload length.
+// Returns 0 on success, -1 on error.
+int sv2_noise_recv(sv2_noise_ctx_t *ctx, esp_transport_handle_t transport,
+                   uint8_t hdr_out[6], uint8_t *payload_out,
+                   int max_payload_len, int *payload_len_out);
+
+#endif /* SV2_NOISE_H */
```

### `main/tasks/create_jobs_task.c` `@@ -68,19 +131,59 @@ void create_jobs_task(void *pvParameters)`

```diff
 
             extranonce_2 = 0;
 
-            if (!current_mining_notification->clean_jobs) {
+            // Check clean_jobs flag
+            bool clean;
+            if (current_work_protocol == STRATUM_V2) {
+                if (stratum_v2_is_extended_channel(GLOBAL_STATE)) {
    …
+            // (V1 and SV2 extended are fine — extranonce_2 gives unique work each time.)
+            if (active_protocol == STRATUM_V2 && !stratum_v2_is_extended_channel(GLOBAL_STATE)) {
+                timeout_ms = ASIC_get_asic_job_frequency_ms(GLOBAL_STATE);
+                continue;
+            }
         }
 
-        // Generate and send job (either new work or incremented extranonce_2)
-        generate_work(GLOBAL_STATE, current_mining_notification, extranonce_2, difficulty);
-        extranonce_2++;
+        // Final protocol check before generating work — protocol may have switched
+        // during a timeout dequeue while we still hold stale current_work
+        active_protocol = GLOBAL_STATE->stratum_protocol;
+        if (active_protocol != current_work_protocol) {
+            free_work_item(GLOBAL_STATE, current_work, current_work_protocol);
+            current_work = NULL;
+            current_work_protocol = active_protocol;
+            timeout_ms = ASIC_get_asic_job_frequency_ms(GLOBAL_STATE);
+            continue;
+        }
+
+        // Generate and send job
+        if (active_protocol == STRATUM_V2) {
+            if (stratum_v2_is_extended_channel(GLOBAL_STATE)) {
+                generate_work_sv2_ext(GLOBAL_STATE, (sv2_ext_job_t *)current_work, difficulty, extranonce_2);
+                extranonce_2++;
+            } else {
+                generate_work_sv2(GLOBAL_STATE, (sv2_job_t *)current_work, difficulty);
[… hunk truncated: showing head + densest window of 64 diff lines]
```
