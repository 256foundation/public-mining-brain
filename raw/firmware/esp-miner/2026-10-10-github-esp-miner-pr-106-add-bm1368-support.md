# ESP-Miner PR #106: Add BM1368 support

> Source: https://github.com/bitaxeorg/ESP-Miner/pull/106
> Collected: 2026-10-10
> Published: 2024-02-10
> Registry ID: esp-miner

State: closed | Merged: 2024-02-10 | Author: johnny9 | +643/-6 | Labels: -

## Body

(no body)

## Files changed

- `components/bm1397/bm1368.c` (+537/-0) — C source
- `components/bm1397/include/bm1368.h` (+44/-0) — C header
- `main/http_server/axe-os/src/app/components/edit/edit.component.html` (+29/-0) — AxeOS Angular UI
- `readme.md` (+13/-1) — documentation
- `main/main.c` (+12/-0) — main app
- `components/bm1397/bm1366.c` (+2/-2) — C source
- `main/http_server/axe-os/src/models/enum/eASICModel.ts` (+2/-1) — AxeOS web UI
- `.vscode/settings.json` (+1/-1) — config
- `main/tasks/power_management_task.c` (+1/-1) — firmware task module
- `components/bm1397/CMakeLists.txt` (+1/-0) — changed file
- `main/global_state.h` (+1/-0) — shared global state structs/flags
- `merge_bin_with_config.sh` (+0/-0) — shell script

## Key excerpts

### `components/bm1397/include/bm1368.h` `@@ -0,0 +1,44 @@`

```diff
+#ifndef BM1368_H_
+#define BM1368_H_
+
+#include "common.h"
+#include "driver/gpio.h"
+#include "mining.h"
+
+#define CRC5_MASK 0x1F
    …
+typedef struct __attribute__((__packed__))
+{
+    uint8_t job_id;
+    uint8_t num_midstates;
+    uint8_t starting_nonce[4];
+    uint8_t nbits[4];
+    uint8_t ntime[4];
+    uint8_t merkle_root[32];
+    uint8_t prev_block_hash[32];
+    uint8_t version[4];
+} BM1368_job;
+
+void BM1368_init(u_int64_t frequency);
+
+void BM1368_send_init(void);
+void BM1368_send_work(void * GLOBAL_STATE, bm_job * next_bm_job);
+void BM1368_set_job_difficulty_mask(int);
+int BM1368_set_max_baud(void);
+int BM1368_set_default_baud(void);
+void BM1368_send_hash_frequency(float frequency);
[… hunk truncated: showing head + densest window of 44 diff lines]
```

### `main/main.c` `@@ -38,6 +38,18 @@ void app_main(void)`

```diff
                                         .send_work_fn = BM1366_send_work};
         GLOBAL_STATE.asic_job_frequency_ms = BM1366_FULLSCAN_MS;
 
+        GLOBAL_STATE.ASIC_functions = ASIC_functions;
+    } else if (strcmp(GLOBAL_STATE.asic_model, "BM1368") == 0) {
+        ESP_LOGI(TAG, "ASIC: BM1368");
+        AsicFunctions ASIC_functions = {.init_fn = BM1368_init,
+                                        .receive_result_fn = BM1368_proccess_work,
+                                        .set_max_baud_fn = BM1368_set_max_baud,
+                                        .set_difficulty_mask_fn = BM1368_set_job_difficulty_mask,
+                                        .send_work_fn = BM1368_send_work};
+
+        uint64_t bm1368_hashrate = GLOBAL_STATE.POWER_MANAGEMENT_MODULE.frequency_value * BM1368_CORE_COUNT * 1000000;
+        GLOBAL_STATE.asic_job_frequency_ms = ((double) NONCE_SPACE / (double) bm1368_hashrate) * 1000;
+
         GLOBAL_STATE.ASIC_functions = ASIC_functions;
     } else if (strcmp(GLOBAL_STATE.asic_model, "BM1397") == 0) {
         ESP_LOGI(TAG, "ASIC: BM1397");
```

### `main/tasks/power_management_task.c` `@@ -141,7 +141,7 @@ void POWER_MANAGEMENT_task(void * pvParameters)`

```diff
                     last_frequency_increase++;
                 }
             }
-        } else if (strcmp(GLOBAL_STATE->asic_model, "BM1366") == 0) {
+        } else if (strcmp(GLOBAL_STATE->asic_model, "BM1366") == 0 || strcmp(GLOBAL_STATE->asic_model, "BM1368") == 0) {
             power_management->chip_temp = EMC2101_get_internal_temp() + 5;
 
             if (power_management->chip_temp > THROTTLE_TEMP &&
```

### `components/bm1397/bm1368.c` `@@ -0,0 +1,537 @@`

```diff
+#include "bm1368.h"
+
+#include "crc.h"
+#include "global_state.h"
+#include "serial.h"
+#include "utils.h"
+
+#include "esp_log.h"
    …
+        freq_cmd[2] = freq_list[i][0];
+        freq_cmd[3] = freq_list[i][1];
+        freq_cmd[4] = freq_list[i][2];
+        freq_cmd[5] = freq_list[i][3];
+        _send_BM1368((TYPE_CMD | GROUP_ALL | CMD_WRITE), freq_cmd, 6, false);
+        vTaskDelay(100 / portTICK_PERIOD_MS);
+    }
+}
+
+static void _send_init(uint64_t frequency) {
+
+    //enable and set version rolling mask to 0xFFFF
+    unsigned char init0[11] = {0x55, 0xAA, 0x51, 0x09, 0x00, 0xA4, 0x90, 0x00, 0xFF, 0xFF, 0x1C};
+    _send_simple(init0, 11);
+
+    //enable and set version rolling mask to 0xFFFF (again)
+    unsigned char init1[11] = {0x55, 0xAA, 0x51, 0x09, 0x00, 0xA4, 0x90, 0x00, 0xFF, 0xFF, 0x1C};
+    _send_simple(init1, 11);
+
+    //enable and set version rolling mask to 0xFFFF (again)
[… hunk truncated: showing head + densest window of 537 diff lines]
```
