# ESP-Miner PR #698: GammaTurbo support and HW abstraction

> Source: https://github.com/bitaxeorg/ESP-Miner/pull/698
> Collected: 2026-10-10
> Published: 2025-02-11
> Registry ID: esp-miner

State: closed | Merged: 2025-02-12 | Author: skot | +1394/-593 | Labels: -

## Body

This PR adds some much needed hardware abstraction layers. To support new hardware "all" you need to do is implement the functions in

- Thermal functions like fan and temp sensing in `/main/thermal/thermal.c`
- Power monitoring and voltage regulation in `/main/power/power.c` and `/main/power/vcore.c`
- ASIC support in `/asic/asic.c`
and create an appropriate `config.cvs`

I have used this to add support for the new [bitaxeGammaTurbo](https://github.com/bitaxeorg/bitaxeGT) hardware

## Files changed

- `main/power/TPS546.c` (+283/-94) — main app
- `main/tasks/power_management_task.c` (+44/-188) — firmware task module
- `components/asic/asic.c` (+225/-0) — C source
- `main/thermal/EMC2103.c` (+158/-0) — thermal/fan control
- `main/power/vcore.c` (+146/-0) — main app
- `main/power/power.c` (+122/-0) — main app
- `main/nvs_device.c` (+9/-102) — main app
- `main/vcore.c` (+0/-106) — main app
- `main/thermal/thermal.c` (+83/-0) — thermal/fan control
- `main/power/TPS546.h` (+58/-15) — main app
- `main/thermal/EMC2103.h` (+73/-0) — thermal/fan control
- `main/power/DS4432U.c` (+35/-0) — main app
- `main/system.c` (+3/-28) — main app
- `main/http_server/http_server.c` (+4/-21) — HTTP server + REST API handlers
- `components/asic/include/asic.h` (+24/-0) — C header
- `config-800x.cvs` (+24/-0) — changed file
- `main/global_state.h` (+11/-12) — shared global state structs/flags
- `main/self_test/self_test.c` (+13/-8) — factory self-test module
- `main/thermal/thermal.h` (+17/-0) — thermal/fan control
- `main/CMakeLists.txt` (+11/-5) — main app
- `main/power/power.h` (+14/-0) — main app
- `main/i2c_bitaxe.c` (+12/-0) — main app
- `main/main.c` (+5/-4) — main app
- `main/tasks/create_jobs_task.c` (+6/-3) — firmware task module
- `main/tasks/asic_result_task.c` (+5/-2) — firmware task module
- `main/tasks/asic_task.c` (+4/-1) — firmware task module
- `main/power/vcore.h` (+1/-1) — main app
- `main/screen.c` (+1/-1) — display screen rendering
- `main/tasks/power_management_task.h` (+0/-2) — firmware task module
- `components/asic/CMakeLists.txt` (+1/-0) — changed file
- `main/i2c_bitaxe.h` (+1/-0) — main app
- `main/power/DS4432U.h` (+1/-0) — main app
- `main/power/INA260.c` (+0/-0) — main app
- `main/power/INA260.h` (+0/-0) — main app
- `main/thermal/EMC2101.c` (+0/-0) — thermal/fan control
- `main/thermal/EMC2101.h` (+0/-0) — thermal/fan control
- `main/thermal/TMP1075.c` (+0/-0) — thermal/fan control
- `main/thermal/TMP1075.h` (+0/-0) — thermal/fan control

## Key excerpts

### `main/power/power.c` `@@ -0,0 +1,122 @@`

```diff
+#include "TPS546.h"
+#include "INA260.h"
+#include "DS4432U.h"
+
+#include "power.h"
+#include "vcore.h"
+
+#define GPIO_ASIC_ENABLE CONFIG_GPIO_ASIC_ENABLE
    …
+
+#define SUPRA_POWER_OFFSET 5 //Watts
+#define GAMMA_POWER_OFFSET 5 //Watts
+#define GAMMATURBO_POWER_OFFSET 5 //Watts
+
+esp_err_t Power_disable(GlobalState * GLOBAL_STATE) {
+
+    switch (GLOBAL_STATE->device_model) {
+        case DEVICE_MAX:
+        case DEVICE_ULTRA:
+        case DEVICE_SUPRA:
+            if (GLOBAL_STATE->board_version >= 402 && GLOBAL_STATE->board_version <= 499) {
+                // Turn off core voltage
+                VCORE_set_voltage(0.0, GLOBAL_STATE);
+            } else if (GLOBAL_STATE->board_version == 202 || GLOBAL_STATE->board_version == 203 || GLOBAL_STATE->board_version == 204) {
+                gpio_set_level(GPIO_ASIC_ENABLE, 1);
+            }
+            break;
+        case DEVICE_GAMMA:
+        case DEVICE_GAMMATURBO:
[… hunk truncated: showing head + densest window of 123 diff lines]
```

### `components/asic/asic.c` `@@ -0,0 +1,225 @@`

```diff
+#include <string.h>
+
+#include <esp_log.h>
+
+#include "bm1397.h"
+#include "bm1366.h"
+#include "bm1368.h"
+#include "bm1370.h"
    …
+
+#include "asic.h"
+
+//static const double NONCE_SPACE = 4294967296.0; //  2^32
+
+static const char *TAG = "asic";
+
+// .init_fn = BM1366_init,
+uint8_t ASIC_init(GlobalState * GLOBAL_STATE) {
+    switch (GLOBAL_STATE->device_model) {
+        case DEVICE_MAX:
+            return BM1397_init(GLOBAL_STATE->POWER_MANAGEMENT_MODULE.frequency_value, BITAXE_MAX_ASIC_COUNT);
+        case DEVICE_ULTRA:
+            return BM1366_init(GLOBAL_STATE->POWER_MANAGEMENT_MODULE.frequency_value, BITAXE_ULTRA_ASIC_COUNT);
+        case DEVICE_SUPRA:
+            return BM1368_init(GLOBAL_STATE->POWER_MANAGEMENT_MODULE.frequency_value, BITAXE_SUPRA_ASIC_COUNT);
+        case DEVICE_GAMMA:
+            return BM1370_init(GLOBAL_STATE->POWER_MANAGEMENT_MODULE.frequency_value, BITAXE_GAMMA_ASIC_COUNT);
+        case DEVICE_GAMMATURBO:
+            return BM1370_init(GLOBAL_STATE->POWER_MANAGEMENT_MODULE.frequency_value, BITAXE_GAMMATURBO_ASIC_COUNT);
[… hunk truncated: showing head + densest window of 225 diff lines]
```

### `components/asic/include/asic.h` `@@ -0,0 +1,24 @@`

```diff
+#ifndef ASIC_H
+#define ASIC_H
+
+#include <esp_err.h>
+#include "global_state.h"
+#include "common.h"
+
+#define BITAXE_MAX_ASIC_COUNT 1
+#define BITAXE_ULTRA_ASIC_COUNT 1
+#define BITAXE_SUPRA_ASIC_COUNT 1
+#define BITAXE_GAMMA_ASIC_COUNT 1
+#define BITAXE_GAMMATURBO_ASIC_COUNT 2
+
+uint8_t ASIC_init(GlobalState * GLOBAL_STATE);
+uint8_t ASIC_get_asic_count(GlobalState * GLOBAL_STATE);
+uint16_t ASIC_get_small_core_count(GlobalState * GLOBAL_STATE);
+task_result * ASIC_proccess_work(GlobalState * GLOBAL_STATE);
+int ASIC_set_max_baud(GlobalState * GLOBAL_STATE);
+void ASIC_set_job_difficulty_mask(GlobalState * GLOBAL_STATE, uint8_t mask);
+void ASIC_send_work(GlobalState * GLOBAL_STATE, void * next_job);
+void ASIC_set_version_mask(GlobalState * GLOBAL_STATE, uint32_t mask);
+esp_err_t ASIC_set_device_model(GlobalState * GLOBAL_STATE);
+
+#endif // ASIC_H
\ No newline at end of file
```

### `main/thermal/thermal.c` `@@ -0,0 +1,83 @@`

```diff
+#include "thermal.h"
+
+#define INTERNAL_OFFSET 5 //degrees C
+
+
+esp_err_t Thermal_init(DeviceModel device_model, bool polarity) {
+        //init the EMC2101, if we have one
+    switch (device_model) {
    …
+        case DEVICE_MAX:
+        case DEVICE_ULTRA:
+        case DEVICE_SUPRA:
+            EMC2101_init(polarity);
+            break;
+        case DEVICE_GAMMA:
+            EMC2101_init(polarity);
+            EMC2101_set_ideality_factor(EMC2101_IDEALITY_1_0319);
+            EMC2101_set_beta_compensation(EMC2101_BETA_11);
+            break;
+        case DEVICE_GAMMATURBO:
+            EMC2103_init(polarity);
+            break;
+        default:
+    }
+    return ESP_OK;
+    
+}
+
+//percent is a float between 0.0 and 1.0
[… hunk truncated: showing head + densest window of 84 diff lines]
```
