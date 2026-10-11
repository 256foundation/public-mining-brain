# ESP-Miner PR #292: Gamma support

> Source: https://github.com/bitaxeorg/ESP-Miner/pull/292
> Collected: 2026-10-10
> Published: 2024-08-16
> Registry ID: esp-miner

State: closed | Merged: 2024-09-03 | Author: skot | +785/-70 | Labels: -

## Body

Adding support for gamma hardware

## Files changed

- `components/asic/bm1370.c` (+504/-0) — C source
- `main/tasks/power_management_task.c` (+95/-62) — firmware task module
- `components/asic/include/bm1370.h` (+46/-0) — C header
- `main/http_server/axe-os/src/app/components/edit/edit.component.html` (+33/-1) — AxeOS Angular UI
- `main/http_server/axe-os/src/app/components/edit/edit.component.ts` (+21/-0) — AxeOS Angular UI
- `config-600.cvs` (+19/-0) — changed file
- `main/main.c` (+18/-1) — main app
- `main/vcore.c` (+17/-2) — main app
- `main/system.c` (+13/-0) — main app
- `main/self_test/self_test.c` (+7/-0) — factory self-test module
- `main/EMC2101.c` (+2/-2) — main app
- `main/global_state.h` (+3/-0) — shared global state structs/flags
- `main/http_server/axe-os/src/models/enum/eASICModel.ts` (+2/-1) — AxeOS web UI
- `main/http_server/http_server.c` (+3/-0) — HTTP server + REST API handlers
- `main/CMakeLists.txt` (+1/-1) — main app
- `components/asic/CMakeLists.txt` (+1/-0) — changed file
- `components/asic/bm1366.c` (+0/-0) — C source
- `components/asic/bm1368.c` (+0/-0) — C source
- `components/asic/bm1397.c` (+0/-0) — C source
- `components/asic/crc.c` (+0/-0) — C source
- `components/asic/include/bm1366.h` (+0/-0) — C header
- `components/asic/include/bm1368.h` (+0/-0) — C header
- `components/asic/include/bm1397.h` (+0/-0) — C header
- `components/asic/include/common.h` (+0/-0) — C header
- `components/asic/include/crc.h` (+0/-0) — C header
- `components/asic/include/serial.h` (+0/-0) — C header
- `components/asic/serial.c` (+0/-0) — C source
- `components/asic/test/CMakeLists.txt` (+0/-0) — changed file
- `components/asic/test/test_job_command.c` (+0/-0) — C source

## Key excerpts

### `main/vcore.c` `@@ -22,8 +22,19 @@`

```diff
 static const char *TAG = "vcore.c";
 
 void VCORE_init(GlobalState * global_state) {
-    if (global_state->board_version == 402) {
-        TPS546_init();
+    switch (global_state->device_model) {
+        case DEVICE_MAX:
+        case DEVICE_ULTRA:
+        case DEVICE_SUPRA:
+            if (global_state->board_version == 402) {
+                TPS546_init();
+            }
+            break;
+        case DEVICE_GAMMA:
+            TPS546_init();
+            break;
+        // case DEVICE_HEX:
+        default:
     }
     ADC_init();
 }
```

### `main/main.c` `@@ -46,6 +46,11 @@ void app_main(void)`

```diff
         GLOBAL_STATE.device_model = DEVICE_SUPRA;
         GLOBAL_STATE.asic_count = 1;
         GLOBAL_STATE.voltage_domain = 1;
+        } else if (strcmp(GLOBAL_STATE.device_model_str, "gamma") == 0) {
+        ESP_LOGI(TAG, "DEVICE: Gamma");
+        GLOBAL_STATE.device_model = DEVICE_GAMMA;
+        GLOBAL_STATE.asic_count = 1;
+        GLOBAL_STATE.voltage_domain = 1;
     } else {
         ESP_LOGE(TAG, "Invalid DEVICE model");
         // maybe should return here to now execute anything with a faulty device parameter !
```

### `main/tasks/power_management_task.c` `@@ -125,88 +131,115 @@ void POWER_MANAGEMENT_task(void * pvParameters)`

```diff
                     power_management->current = TPS546_get_iout() * 1000;
                     // calculate regulator power (in milliwatts)
                     power_management->power = (TPS546_get_vout() * power_management->current) / 1000;
+                    // The power reading from the TPS546 is only it's output power. So the rest of the Bitaxe power is not accounted for.
+                    power_management->power += SUPRA_POWER_OFFSET; // Add offset for the rest of the Bitaxe power. TODO: this better.
 				} else if (INA260_installed() == true) {
                     power_management->voltage = INA260_read_voltage();
                     power_management->current = INA260_read_current();
    …
+                    nvs_config_set_u16(NVS_CONFIG_ASIC_VOLTAGE, 1000);
+                    nvs_config_set_u16(NVS_CONFIG_ASIC_FREQ, 50);
+                    nvs_config_set_u16(NVS_CONFIG_FAN_SPEED, 100);
+                    nvs_config_set_u16(NVS_CONFIG_AUTO_FAN_SPEED, 0);
+                    nvs_config_set_u16(NVS_CONFIG_OVERHEAT_MODE, 1);
+                    exit(EXIT_FAILURE);
+                }
 
-                    if ((power_management->vr_temp > TPS546_THROTTLE_TEMP || power_management->chip_temp_avg > THROTTLE_TEMP) &&
-                        (power_management->frequency_value > 50 || power_management->voltage > 1000)) {
-                        ESP_LOGE(TAG, "OVERHEAT  VR: %fC ASIC %fC", power_management->vr_temp, power_management->chip_temp_avg );
-
-                        EMC2101_set_fan_speed(1);
-                        if (GLOBAL_STATE->board_version == 402) {
-                            // Turn off core voltage
-                            VCORE_set_voltage(0.0, GLOBAL_STATE);
-                        } else if (power_management->HAS_POWER_EN) {
-                            gpio_set_level(GPIO_NUM_10, 1);
-                        }
-                        nvs_config_set_u16(NVS_CONFIG_ASIC_VOLTAGE, 1000);
[… hunk truncated: showing head + densest window of 175 diff lines]
```

### `components/asic/include/bm1370.h` `@@ -0,0 +1,46 @@`

```diff
+#ifndef BM1370_H_
+#define BM1370_H_
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
+} BM1370_job;
+
+uint8_t BM1370_init(uint64_t frequency, uint16_t asic_count);
+
+uint8_t BM1370_send_init(void);
+void BM1370_send_work(void * GLOBAL_STATE, bm_job * next_bm_job);
+void BM1370_set_job_difficulty_mask(int);
+int BM1370_set_max_baud(void);
+int BM1370_set_default_baud(void);
+void BM1370_send_hash_frequency(int, float, float);
[… hunk truncated: showing head + densest window of 46 diff lines]
```
