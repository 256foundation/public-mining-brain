# ESP-Miner PR #139: Self_test

> Source: https://github.com/bitaxeorg/ESP-Miner/pull/139
> Collected: 2026-10-10
> Published: 2024-03-17
> Registry ID: esp-miner

State: closed | Merged: 2024-03-17 | Author: benjamin-wilson | +290/-12 | Labels: -

## Body

Self test that runs once lifetime (if passing) to test the ASIC, power and fan. TODO is check a returned nonce instead of chip cout. Doesn't work on MAX. 

## Files changed

- `main/self_test/self_test.c` (+246/-0) — factory self-test module
- `components/bm1397/bm1368.c` (+16/-3) — C source
- `components/bm1397/bm1366.c` (+7/-3) — C source
- `main/main.c` (+7/-1) — main app
- `main/self_test/self_text.h` (+6/-0) — factory self-test module
- `components/bm1397/include/bm1368.h` (+2/-2) — C header
- `components/bm1397/include/bm1366.h` (+1/-1) — C header
- `main/DS4432U.c` (+1/-1) — main app
- `main/global_state.h` (+1/-1) — shared global state structs/flags
- `main/CMakeLists.txt` (+1/-0) — main app
- `main/main.h` (+1/-0) — main app
- `main/nvs_config.h` (+1/-0) — NVS settings schema/keys

## Key excerpts

### `main/main.c` `@@ -73,10 +73,15 @@ void app_main(void)`

```diff
         GLOBAL_STATE.ASIC_functions = ASIC_functions;
     }
 
-    ESP_LOGI(TAG, "Welcome to the bitaxe!");
+    uint16_t should_self_test = nvs_config_get_u16(NVS_CONFIG_SELF_TEST, 1);
+    if (should_self_test == 1) {
+        self_test((void *) &GLOBAL_STATE);
+    }
 
     xTaskCreate(SYSTEM_task, "SYSTEM_task", 4096, (void *) &GLOBAL_STATE, 3, NULL);
 
+    ESP_LOGI(TAG, "Welcome to the bitaxe!");
+
     // pull the wifi credentials out of NVS
     char * wifi_ssid = nvs_config_get_string(NVS_CONFIG_WIFI_SSID, WIFI_SSID);
     char * wifi_pass = nvs_config_get_string(NVS_CONFIG_WIFI_PASS, WIFI_PASS);
```

### `main/self_test/self_text.h` `@@ -0,0 +1,6 @@`

```diff
+#ifndef SELF_TEST_H_
+#define SELF_TEST_H_
+
+void self_test(void * pvParameters);
+
+#endif
\ No newline at end of file
```

### `main/self_test/self_test.c` `@@ -0,0 +1,246 @@`

```diff
+#include "DS4432U.h"
+#include "EMC2101.h"
+#include "INA260.h"
+#include "adc.h"
+#include "driver/i2c.h"
+#include "esp_log.h"
+#include "global_state.h"
+#include "nvs_config.h"
    …
+
+    // turn ASIC on
+    gpio_set_direction(GPIO_NUM_10, GPIO_MODE_OUTPUT);
+    gpio_set_level(GPIO_NUM_10, 0);
+
+    // Init I2C
+    ESP_ERROR_CHECK(i2c_master_init());
+    ESP_LOGI(TAG, "I2C initialized successfully");
+
+    ADC_init();
+    DS4432U_set_vcore(nvs_config_get_u16(NVS_CONFIG_ASIC_VOLTAGE, CONFIG_ASIC_VOLTAGE) / 1000.0);
+
+    EMC2101_init(nvs_config_get_u16(NVS_CONFIG_INVERT_FAN_POLARITY, 1));
+    EMC2101_set_fan_speed(1);
+
+    // oled
+    if (!OLED_init()) {
+        ESP_LOGI(TAG, "OLED init failed!");
+    } else {
+        ESP_LOGI(TAG, "OLED init success!");
[… hunk truncated: showing head + densest window of 246 diff lines]
```

### `main/nvs_config.h` `@@ -22,6 +22,7 @@`

```diff
 #define NVS_CONFIG_AUTO_FAN_SPEED "autofanspeed"
 #define NVS_CONFIG_FAN_SPEED "fanspeed"
 #define NVS_CONFIG_BEST_DIFF "bestdiff"
+#define NVS_CONFIG_SELF_TEST "selftest"
 
 #define NVS_CONFIG_SWARM "swarmconfig"
 
```
