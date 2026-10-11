# ESP-Miner PR #1986: Add BZM ASIC and Bonanza board support

> Source: https://github.com/bitaxeorg/ESP-Miner/pull/1986
> Collected: 2026-10-10
> Published: 2026-09-19
> Registry ID: esp-miner

State: open | Merged: no | Author: johnny9 | +19020/-948 | Labels: enhancement

## Body

Adds BZM ASIC and Bonanza 1002 support for mining, power, cooling, and live frequency control. Depends on #1972.

## Files changed

- `main/power/bonanza_tps546.c` (+1444/-0) — main app
- `main/power/bzm_board_power.c` (+1311/-0) — main app
- `components/asic/test/test_bzm_bringup.c` (+1244/-0) — C source
- `components/asic/bzm_driver.c` (+1068/-0) — C source
- `components/asic/bzm_bringup.c` (+947/-0) — C source
- `components/asic/test/test_bzm.c` (+914/-0) — C source
- `components/asic/test/test_bzm_frame_parser.c` (+804/-0) — C source
- `components/asic/bzm_transport.c` (+616/-0) — C source
- `components/asic/bzm_bridge.c` (+602/-0) — C source
- `components/asic/bzm_telemetry.c` (+378/-0) — C source
- `components/asic/test/test_bzm_runtime_health.c` (+373/-0) — C source
- `components/asic/test/test_bzm_bridge.c` (+366/-0) — C source
- `components/asic/test/test_bzm_board_power.c` (+363/-0) — C source
- `main/power/bonanza_power_task.c` (+346/-0) — main app
- `components/asic/bzm_reactor.c` (+309/-0) — C source
- `components/asic/test/test_bzm_driver.c` (+283/-0) — C source
- `components/asic/test/test_bzm_balanced_ramp.c` (+280/-0) — C source
- `components/asic/test/test_bonanza_power_policy.c` (+258/-0) — C source
- `components/asic/bzm_runtime_health.c` (+256/-0) — C source
- `doc/bzm-bonanza-pr1972-port.md` (+247/-0) — documentation
- `components/asic/test/test_bzm_power.c` (+237/-0) — C source
- `components/asic/test/test_bzm_topology.c` (+206/-0) — C source
- `components/asic/test/test_bonanza_tps546.c` (+197/-0) — C source
- `components/asic/bzm_balanced_ramp.c` (+185/-0) — C source
- `main/power/bonanza_power_policy.c` (+176/-0) — main app
- `main/power/bonanza_vcore.c` (+171/-0) — main app
- `components/asic/test/test_bitmain_job_packets.c` (+120/-46) — C source
- `components/asic/bzm_serial.c` (+163/-0) — C source
- `components/stratum/utils.c` (+0/-162) — stratum protocol component
- `components/asic/test/test_mining_pipeline.c` (+95/-62) — C source
- `components/asic/bzm_frame_parser.c` (+151/-0) — C source
- `components/asic/bzm_topology.c` (+150/-0) — C source
- `components/asic/test/test_asic_result_job.c` (+150/-0) — C source
- `components/asic/test/test_bzm_lease_guard.c` (+144/-0) — C source
- `components/asic/bzm_job_store.c` (+143/-0) — C source
- `components/asic/bzm_work.c` (+143/-0) — C source
- `components/asic/bzm_power.c` (+134/-0) — C source
- `components/asic/include/bzm/runtime_health.h` (+128/-0) — C header
- `components/asic/private_include/bzm/transport.h` (+124/-0) — C header
- `components/stratum/test/test_utils.c` (+104/-15) — stratum protocol component
- `main/power/bonanza_tps546.h` (+116/-0) — main app
- `components/asic/include/bzm/bridge.h` (+114/-0) — C header
- `components/stratum/test/test_common_jobs.c` (+110/-0) — stratum protocol component
- `components/asic/include/bzm/telemetry.h` (+108/-0) — C header
- `components/asic/bm_job_midstate.c` (+101/-0) — C source
- `components/asic/include/bzm/board.h` (+100/-0) — C header
- `components/stratum/mining.c` (+7/-93) — stratum protocol component
- `components/asic/test/test_bzm_result_dedup.c` (+99/-0) — C source
- `components/asic/test/test_asic_result_task.c` (+32/-65) — C source
- `components/asic/private_include/bzm/reactor.h` (+96/-0) — C header

… 129 more changed files (mostly components/asic, components/asic/include, components/asic/include/bzm, components/asic/private_include, components/asic/private_include/bzm, components/asic/test):
`components/asic/bzm.c`, `components/asic/test/test_bitmain_job_packet_building.c`, `components/asic/include/bzm/power.h`, `components/asic/private_include/bzm/topology.h`, `components/asic/private_include/bzm/registers.h`, `components/stratum/test/test_mining.c`, `main/tasks/create_jobs_task.c`, `components/stratum/hash_bytes.c`, `components/asic/private_include/bzm/balanced_ramp.h`, `components/asic/bzm_frequency.c`, `components/asic/bzm_lease_guard.c`, `components/asic/private_include/bzm/protocol.h`, `components/asic/private_include/bzm/bringup.h`, `components/asic/private_include/bzm/frame_parser.h`, `components/asic/test/test_bzm_work.c`, `components/asic/test/test_asic_submit.c`, `components/asic/test/test_bzm_frequency.c`, `components/asic/bitmain_job_packet.c`, `main/power/bonanza_power_policy.h`, `components/asic/private_include/bzm/serial.h`, `main/tasks/asic_result_task.c`, `components/asic/private_include/bzm/job_store.h`, `components/stratum/test/test_job_building.c`, `components/asic/private_include/bzm/bridge_protocol.h`, `components/stratum/mining_job.c`, `components/asic/test/test_bzm_result_adapter.c`, `main/http_server/http_server.c`, `components/asic/test/test_bzm_dispatch_gate.c`, `components/asic/test/bzm_board_test_bindings.h`, `components/asic/CMakeLists.txt`, `components/asic/bzm_result_dedup.c`, `components/asic/private_include/bitmain_job_packet.h`, `components/asic/private_include/bzm/result.h`, `components/asic/asic.c`, `components/asic/bm1397.c`, `components/mining_job/include/asic_job.h`, `components/asic/private_include/bzm/telemetry_internal.h`, `components/asic/bm1366.c`, `components/asic/bm1368.c`, `components/asic/bm1370.c`, `components/asic/bm1373.c`, `components/asic/private_include/bzm/lease_guard_internal.h`, `components/stratum/include/mining.h`, `main/power/vcore.c`, `main/self_test/self_test.c`, `configs/config-1002.csv`, `components/asic/include/bzm/frequency.h`, `main/thermal/thermal.c`, `components/asic/private_include/bzm/result_dedup.h`, `components/stratum/test/README.md`, `components/asic/include/bzm/driver.h`, `main/power/bonanza_power_task.h`, `components/asic/test/bitmain_job_allocator_fault_injector.c`, `components/asic/bzm_dispatch_gate.c`, `components/asic/include/bzm/README.md`, `components/asic/test/bzm_test_state.h`, `components/asic/asic_submit.c`, `components/asic/private_include/bzm/work_registers.h`, `components/mining_job/asic_job.c`, `components/asic/include/bzm/lease_guard.h` …

## Key excerpts

### `main/power/bonanza_power_task.c` `@@ -0,0 +1,346 @@`

```diff
+#include "bonanza_power_task.h"
+
+#include <math.h>
+#include <stdatomic.h>
+#include <stdlib.h>
+#include <stdio.h>
+#include "bzm_board_power.h"
+#include "bzm/frequency.h"
    …
+{
+    GlobalState *state = context;
+    if (enabled) {
+        nvs_config_set_bool(NVS_CONFIG_AUTO_FAN_SPEED, false);
+        nvs_config_set_u16(NVS_CONFIG_MANUAL_FAN_SPEED, 100);
+    }
+    nvs_config_set_bool(NVS_CONFIG_OVERHEAT_MODE, enabled);
+    state->SYSTEM_MODULE.overheat_mode = enabled;
+}
+
+static bool save_target(void *context, bonanza_power_target_t target)
+{
+    GlobalState *state = context;
+    if ((state->DEVICE_CONFIG.family.id == BONANZA)) {
+        bzm_frequency_target_t resolved;
+        float voltage;
+        if (!bzm_frequency_resolve_target(target.frequency_mhz, &resolved) ||
+            !bzm_power_resolve_user_voltage(target.voltage_mv, &voltage)) return false;
+        target.frequency_mhz = resolved.actual_mhz;
+    }
+    nvs_config_set_u16(NVS_CONFIG_ASIC_VOLTAGE, target.voltage_mv);
+    nvs_config_set_float(NVS_CONFIG_ASIC_FREQUENCY, target.frequency_mhz);
+    return nvs_config_get_u16(NVS_CONFIG_ASIC_VOLTAGE) == target.voltage_mv &&
+           fabsf(nvs_config_get_float(NVS_CONFIG_ASIC_FREQUENCY) - target.frequency_mhz) < 0.001f;
[… hunk truncated: showing head + densest window of 346 diff lines]
```

### `components/asic/test/CMakeLists.txt` `@@ -1,4 +1,17 @@`

```diff
 idf_component_register(SRC_DIRS "."
-                       INCLUDE_DIRS "." "../../stratum/test/stubs"
-                                    "../../../main/tasks" "../../../main/self_test"
+                       INCLUDE_DIRS "." "../../stratum/test" "stubs"
+                                    "../../../main/tasks" "../../../main/thermal" "../../../main/power" "../../../main/self_test" "../../../main"
+                       PRIV_INCLUDE_DIRS "../private_include"
                        REQUIRES cmock stratum stratum_v2 asic)
+
+target_sources(${COMPONENT_LIB} PRIVATE "../../../main/power/bonanza_power_policy.c")
+
+# Compile each public BZM header using only the ASIC component's exported
+# dependencies. These targets must not inherit this test component's private
+# headers or hardware stubs.
+foreach(header board bridge chain driver frequency lease_guard power runtime_health telemetry)
+    add_library(bzm_public_header_${header} OBJECT "public_headers/check.c")
+    target_link_libraries(bzm_public_header_${header} PRIVATE idf::asic)
+    target_compile_definitions(bzm_public_header_${header} PRIVATE
+        BZM_PUBLIC_HEADER="bzm/${header}.h")
+endforeach()
```

### `main/power/bonanza_vcore.c` `@@ -0,0 +1,171 @@`

```diff
+#include "bonanza_vcore.h"
+#include <math.h>
+#include "esp_check.h"
+#include "esp_log.h"
+#include "driver/gpio.h"
+#include "freertos/FreeRTOS.h"
+#include "freertos/task.h"
+#include "bzm/bridge.h"
    …
+#include "bzm/power.h"
+#include "global_state.h"
+#define GPIO_ASIC_ENABLE CONFIG_GPIO_ASIC_ENABLE
+#define GPIO_TPS546_PGOOD 11
+static const char *TAG = "bonanza_vcore";
+esp_err_t BONANZA_VCORE_init(GlobalState *GLOBAL_STATE)
+{
+    gpio_config_t enable = {
+        .pin_bit_mask = 1ULL << GPIO_ASIC_ENABLE,
+        .mode = GPIO_MODE_OUTPUT,
+    };
+    ESP_RETURN_ON_ERROR(gpio_config(&enable), TAG,
+                        "TPS546 enable GPIO config failed");
+    ESP_RETURN_ON_ERROR(gpio_set_level(GPIO_ASIC_ENABLE, 0), TAG,
+                        "TPS546 enable safe-state failed");
+    gpio_config_t pgood = {
+        .pin_bit_mask = 1ULL << GPIO_TPS546_PGOOD,
+        .mode = GPIO_MODE_INPUT,
+        .pull_up_en = GPIO_PULLUP_DISABLE,
+        .pull_down_en = GPIO_PULLDOWN_DISABLE,
+    };
+    ESP_RETURN_ON_ERROR(gpio_config(&pgood), TAG,
+                        "TPS546 PGOOD GPIO config failed");
+    esp_err_t bridge_err = BZM_bridge_init();
[… hunk truncated: showing head + densest window of 171 diff lines]
```

### `main/power/bzm_board_power.c` `@@ -0,0 +1,1311 @@`

```diff
+#include "bzm_board_power.h"
+#include "global_state.h"
+#include "bonanza_power_task.h"
+
+#include <math.h>
+#include <pthread.h>
+#include <stdatomic.h>
+#include <stdio.h>
    …
+#include "nvs_config.h"
+#include "thermal.h"
+#include "bonanza_vcore.h"
+
+#define BZM_MONITOR_PERIOD_MS 100U
+#define BZM_HEALTH_PERIOD_MS 500U
+#define BZM_SAFE_OFF_TIMEOUT_MS 1500U
+#define BZM_SAFE_OFF_SAMPLE_MS 25U
+#define BZM_BOARD_WATCHDOG_MS 300000U
+#define BZM_IO_TASK_PRIORITY 18U
+#define BZM_WORK_REPLACEMENT_TIMEOUT_MS 30000U
+
+/* Board 1002 operating limits. CH2 is an inter-stack differential. */
+#define BZM_FAN_MIN_RPM 1000U
+#define BZM_SAFE_OFF_VCORE_MV 250U
+#define BZM_TEMP_MIN_C (-20)
+#define BZM_TEMP_MAX_C 75
+#define BZM_STACK_MV_MIN 300U
+#define BZM_STACK_MV_MAX 800U
+#define BZM_INTERSTACK_DIFF_ABS_MAX_MV 50U
+#define BZM_STACK_MAX_SPREAD_MV 100U
+/* Confirm noisy CH2/combined-PLL samples; trips and other faults act at once. */
+#define BZM_CH2_CONFIRM_SAMPLES 3U
+#define BZM_PLL_LOCK_CONFIRM_SAMPLES 3U
[… hunk truncated: showing head + densest window of 1311 diff lines]
```
