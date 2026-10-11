# ESP-Miner PR #1897: Instant pool switching

> Source: https://github.com/bitaxeorg/ESP-Miner/pull/1897
> Collected: 2026-10-10
> Published: 2026-08-18
> Registry ID: esp-miner

State: closed | Merged: 2026-09-09 | Author: mutatrum | +4256/-3807 | Labels: enhancement

## Body

This PR separates Stratum V1 and V2 protocols from the mining path. By generalising the whole job preparation, coinbase decoding, asic job creation and nonce return handling it greatly simplifies the code. SV1/2 protocol differences are handled by separate clients, instead of having it in separate task implementations.

Current jobs are stored in a ringbuffer, so ownership transfer and task handover is also no longer a problem, making it much easier to prevent memory leaks or use-after-free bugs. All parsing from SV1 and SV2 go directly into this ring buffer, so no intermediate allocations and/or memory ownership handovers.

It also moves a lot of pool specific fields from `GlobalState` into a connection object, so the whole mining state machine is way more modular now. It also codified ASIC capabilities and adds software version rolling into the generic mining path. This enables BM1397 devices to do header only mining (Stratum V2 Standard Channel).

Needs #1896. The live pool switching uncovered some stability bugs where the TLS handshake starved the fan_controller, killing the i2c bus.

This PR also incorporates the findings and unit tests of the following PRs:
* closes #1880 by Schnitzel
* closes #1881 by Schnitzel
* closes #1849 by Distortions81
* closes #1854 by Distortions81
* closes #1866 by Schnitzel
* closes #1855 by Distortions81
* closes #1909 by cbyam
* closes #1918 by seby1302

Furthermore, adds the following stratum protocol safety improvements as well:
 * Zero-Target & `hash_to_pdiff()` Division-by-Zero Safety
 * SV1 BIP-320 Version Rolling Mask Validation
 * SV1 Extranonce1 Parity & Length Validation
 * SV2 Channel ID Verification
 * `coinbase_decode_varint` Bounds-Checking
 * SV2 accepted_count Bounded by Pending Shares
 * Bitmask Safety & Assertion
 * `calculate_coinbase_tx_hash_bin` Allocation Safety
 * Stratum V1 `version`, `nbits`, and `ntime` Length Validation
 * `CLIENT_RECONNECT` Minimum Delay

## Files changed

- `main/tasks/stratum_v2_task.c` (+0/-1082) — Stratum V2 protocol task
- `main/tasks/stratum_v2_client.c` (+976/-0) — firmware task module
- `main/tasks/protocol_coordinator.c` (+0/-561) — V1/V2 protocol coordinator task
- `main/tasks/stratum_v1_task.c` (+0/-519) — Stratum V1 protocol task
- `main/tasks/stratum_v1_client.c` (+508/-0) — firmware task module
- `components/stratum/test/test_stratum_json.c` (+426/-41) — stratum protocol component
- `components/stratum/stratum_api.c` (+309/-142) — stratum protocol component
- `main/tasks/create_jobs_task.c` (+103/-346) — firmware task module
- `components/stratum/coinbase_decoder.c` (+156/-127) — stratum protocol component
- `main/tasks/stratum_task.c` (+283/-0) — firmware task module
- `components/stratum_v2/test/test_sv2.c` (+201/-0) — SV2 component (frames/Noise/protocol)
- `components/stratum/test/test_coinbase_decoder.c` (+158/-40) — stratum protocol component
- `main/system.c` (+147/-47) — main app
- `components/stratum_v2/sv2_protocol.c` (+96/-88) — SV2 component (frames/Noise/protocol)
- `components/stratum/mining.c` (+75/-87) — stratum protocol component
- `components/stratum/test/test_mining.c` (+65/-79) — stratum protocol component
- `main/work_queue.c` (+0/-109) — ASIC work queue
- `components/stratum_v2/include/sv2_protocol.h` (+40/-55) — SV2 component (frames/Noise/protocol)
- `main/tasks/asic_result_task.c` (+12/-71) — firmware task module
- `components/stratum/test/test_utils.c` (+80/-1) — stratum protocol component
- `main/self_test/self_test.c` (+40/-27) — factory self-test module
- `components/stratum/include/miner_job.h` (+63/-0) — stratum protocol component
- `components/stratum/include/stratum_api.h` (+33/-21) — stratum protocol component
- `main/http_server/axe-os/src/app/components/home/home.component.ts` (+37/-17) — AxeOS Angular UI
- `components/stratum/utils.c` (+36/-16) — stratum protocol component
- `components/stratum/test/test_miner_job.c` (+51/-0) — stratum protocol component
- `main/http_server/http_server.c` (+40/-9) — HTTP server + REST API handlers
- `components/stratum/miner_job.c` (+42/-0) — stratum protocol component
- `main/global_state.h` (+6/-33) — shared global state structs/flags
- `main/http_server/axe-os/src/app/components/home/home.component.html` (+20/-18) — AxeOS Angular UI
- `main/tasks/protocol_coordinator.h` (+0/-34) — V1/V2 protocol coordinator task
- `main/tasks/stratum_task.h` (+32/-0) — firmware task module
- `main/http_server/axe-os/src/app/components/pool/pool.component.ts` (+1/-28) — AxeOS Angular UI
- `main/work_queue.h` (+0/-26) — ASIC work queue
- `components/asic/bm1397.c` (+9/-16) — C source
- `components/stratum/include/utils.h` (+24/-1) — stratum protocol component
- `components/stratum/include/coinbase_decoder.h` (+9/-14) — stratum protocol component
- `main/http_server/system_api_json.c` (+10/-13) — HTTP server + REST API handlers
- `main/system.h` (+9/-13) — main app
- `main/tasks/stratum_v1_client.h` (+22/-0) — firmware task module
- `components/asic/bm1373.c` (+13/-8) — C source
- `main/tasks/stratum_v2_client.h` (+21/-0) — firmware task module
- `components/stratum/include/mining.h` (+8/-12) — stratum protocol component
- `main/main.c` (+6/-14) — main app
- `AGENTS.md` (+15/-3) — documentation
- `components/asic/bm1368.c` (+9/-9) — C source
- `components/asic/bm1370.c` (+9/-9) — C source
- `main/http_server/axe-os/src/app/components/pool/pool.component.html` (+5/-13) — AxeOS Angular UI
- `main/tasks/stratum_v2_task.h` (+0/-18) — Stratum V2 protocol task
- `components/asic/bm1366.c` (+8/-8) — C source

… 14 more changed files (mostly components/asic, components/asic/include, components/stratum, components/stratum_v2, components/stratum_v2/test, main):
`main/device_config.h`, `components/stratum_v2/sv2_noise.c`, `main/tasks/stratum_v1_task.h`, `components/asic/include/bm1397.h`, `main/CMakeLists.txt`, `main/screen.c`, `main/http_server/openapi.yaml`, `main/nvs_config.c`, `components/stratum_v2/test/CMakeLists.txt`, `main/http_server/axe-os/src/app/components/home/home.component.spec.ts`, `components/asic/asic.c`, `test/CMakeLists.txt`, `components/stratum/CMakeLists.txt`, `main/http_server/axe-os/src/app/services/system.service.ts`

## Key excerpts

### `main/tasks/create_jobs_task.c` `@@ -48,365 +100,70 @@ void create_jobs_task(void *pvParameters)`

```diff
     // active_jobs / valid_jobs are allocated and zeroed by SYSTEM_init_system(),
     // before any task that touches them can run.
 
-    double difficulty = GLOBAL_STATE->pool_difficulty;
-    void *current_work = NULL;
-    stratum_protocol_t current_work_protocol = GLOBAL_STATE->stratum_protocol;
+    uint32_t current_version_mask = 0;
+    miner_job_t *current_work = NULL;
    …
-                ESP_LOGI(TAG, "New pool difficulty %.2f", GLOBAL_STATE->pool_difficulty);
-                difficulty = GLOBAL_STATE->pool_difficulty;
-                GLOBAL_STATE->new_set_mining_difficulty_msg = false;
-            }
-
-            if (GLOBAL_STATE->new_stratum_version_rolling_msg && GLOBAL_STATE->ASIC_initalized) {
-                ESP_LOGI(TAG, "Set chip version rolls %i", (int)(GLOBAL_STATE->version_mask >> 13));
-                ASIC_set_version_mask(GLOBAL_STATE, GLOBAL_STATE->version_mask);
-                GLOBAL_STATE->new_stratum_version_rolling_msg = false;
+            GLOBAL_STATE->active_job_slot_idx = (uint8_t)(slot_notify % MINER_JOB_POOL_SIZE);
+            current_work_sent = false;
+            current_version = new_work->version;
+
+            if (new_work->version_mask != current_version_mask && GLOBAL_STATE->ASIC_initalized) {
+                ESP_LOGI(TAG, "Set chip version rolls %i", (int)(new_work->version_mask >> 13));
+                ASIC_set_version_mask(GLOBAL_STATE, new_work->version_mask);
+                current_version_mask = new_work->version_mask;
             }
 
             extranonce_2 = 0;
[… hunk truncated: showing head + densest window of 398 diff lines]
```

### `main/tasks/stratum_task.h` `@@ -0,0 +1,32 @@`

```diff
+#ifndef STRATUM_TASK_H_
+#define STRATUM_TASK_H_
+
+#include "global_state.h"
+#include <stdbool.h>
+
+// Manages network connectivity, pool failover/heartbeat, and dispatches to V1/V2 protocol drivers.
+void stratum_task(void *pvParameters);
+
+// Request the active stratum client to reconnect (e.g. on primary pool recovery or pool settings change).
+void stratum_request_reconnect(void);
+
+// Returns true if a reconnect request is pending.
+bool stratum_reconnect_requested(void);
+
+// Probe a pool to check if it is reachable without disrupting active mining.
+bool stratum_probe_pool(GlobalState *gs, uint16_t pool_idx);
+
+// Promptly trigger a heartbeat check of the primary pool (e.g. when primary config changes while on fallback).
+void stratum_trigger_heartbeat_check(void);
+
+// Notify stratum task that a specific pool configuration was modified in NVS.
+void stratum_notify_pool_modified(GlobalState *gs, uint16_t pool_idx);
+
+// Notify stratum task that primary/secondary pool index or fallback toggle was changed.
+void stratum_notify_pool_selection_changed(GlobalState *gs);
+
+// Submit a found share to the active pool (dispatches to SV1 or SV2).
+int stratum_submit_share(GlobalState *GLOBAL_STATE, const bm_job *active_job,
+                         uint32_t nonce, uint32_t rolled_version, uint64_t *sent_time_us);
+
+#endif /* STRATUM_TASK_H_ */
```

### `main/tasks/stratum_v1_client.h` `@@ -0,0 +1,22 @@`

```diff
+#ifndef STRATUM_V1_CLIENT_H_
+#define STRATUM_V1_CLIENT_H_
+
+#include "esp_err.h"
+#include <stdbool.h>
+#include <stdint.h>
+#include "mining.h"
+
+typedef struct GlobalState GlobalState;
+
+// Run the Stratum V1 client loop for pool_idx until disconnect, ASIC pause, or reconnect requested.
+esp_err_t stratum_v1_run(GlobalState *GLOBAL_STATE, uint16_t pool_idx);
+
+void stratum_v1_close_connection(GlobalState *GLOBAL_STATE);
+
+// Submit a solved ASIC share to the active Stratum V1 pool connection
+int stratum_v1_submit_share(GlobalState *GLOBAL_STATE, const bm_job *active_job, uint32_t nonce, uint32_t rolled_version, uint64_t *sent_time_us);
+
+// Probe a Stratum V1 pool to check reachability and credentials
+bool stratum_v1_probe_pool(GlobalState *GLOBAL_STATE, uint16_t pool_idx);
+
+#endif // STRATUM_V1_CLIENT_H_
```

### `main/tasks/stratum_v2_client.h` `@@ -0,0 +1,21 @@`

```diff
+#ifndef STRATUM_V2_CLIENT_H_
+#define STRATUM_V2_CLIENT_H_
+
+#include <stdbool.h>
+#include <stdint.h>
+#include "esp_err.h"
+#include "mining.h"
+
+typedef struct GlobalState GlobalState;
+
+// Run the Stratum V2 client loop for pool_idx until disconnect, ASIC pause, or reconnect requested.
+esp_err_t stratum_v2_run(GlobalState *GLOBAL_STATE, uint16_t pool_idx);
+
+void stratum_v2_close_connection(GlobalState *GLOBAL_STATE);
+int stratum_v2_submit_share(GlobalState *GLOBAL_STATE, const bm_job *active_job,
+                            uint32_t nonce, uint32_t rolled_version, uint64_t *sent_time_us);
+
+// Probe a Stratum V2 pool to check reachability, Noise handshake, and credentials
+bool stratum_v2_probe_pool(GlobalState *GLOBAL_STATE, uint16_t pool_idx);
+
+#endif // STRATUM_V2_CLIENT_H_
```
