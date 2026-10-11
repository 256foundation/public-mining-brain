# ESP-Miner PR #1916: Bitaxe Color: Naja Duo and Gamma Hex support with ST7789 display

> Source: https://github.com/bitaxeorg/ESP-Miner/pull/1916
> Collected: 2026-10-10
> Published: 2026-08-26
> Registry ID: esp-miner

State: closed | Merged: 2026-08-29 | Author: mutatrum | +12652/-393 | Labels: -

## Body

Adds support for Naja Duo 1201 and Gamma Hex 1300

## Files changed

- `main/images/generated/bitaxe_background.c` (+6817/-0) — main app
- `main/images/generated/bitaxe_logo_large.c` (+1236/-0) — main app
- `main/images/fonts/ui_font_DigitalNumbers28.c` (+914/-0) — main app
- `main/images/fonts/ui_font_DigitalNumbers16.c` (+579/-0) — main app
- `main/images/fonts/ui_font_OpenSansBold14.c` (+527/-0) — main app
- `main/images/fonts/ui_font_OpenSansBold13.c` (+508/-0) — main app
- `main/power/TPS546.c` (+282/-29) — main app
- `main/screen.c` (+276/-13) — display screen rendering
- `tools/lvgl_image.py` (+204/-0) — changed file
- `main/display.c` (+182/-0) — OLED/display rendering
- `main/images/fonts/ui_font_AngelWish40.c` (+172/-0) — main app
- `main/power/vcore.c` (+88/-80) — main app
- `components/asic/bm1370.c` (+74/-44) — C source
- `main/device_pins.c` (+115/-0) — main app
- `main/device_config.h` (+62/-34) — main app
- `main/self_test/self_test.c` (+52/-23) — factory self-test module
- `main/power/asic_init.c` (+44/-8) — main app
- `main/device_pins.h` (+49/-0) — main app
- `components/asic/bm1366.c` (+25/-17) — C source
- `components/asic/bm1397.c` (+24/-17) — C source
- `components/asic/asic.c` (+35/-4) — C source
- `components/asic/bm1373.c` (+17/-19) — C source
- `main/power/TPS546.h` (+22/-11) — main app
- `components/asic/bm1368.c` (+19/-13) — C source
- `main/Kconfig.projbuild` (+20/-12) — main app
- `main/images/README.md` (+32/-0) — main app
- `config-1300.cvs` (+31/-0) — changed file
- `config-1201.cvs` (+29/-0) — changed file
- `main/thermal/EMC2103.c` (+24/-3) — thermal/fan control
- `main/main.c` (+18/-8) — main app
- `main/thermal/thermal.c` (+24/-1) — thermal/fan control
- `main/http_server/axe-os/src/app/components/edit/edit.component.html` (+13/-7) — AxeOS Angular UI
- `main/bap/bap_uart.c` (+5/-9) — BAP (Bitaxe Auxiliary Peripheral) bus
- `main/system.c` (+13/-1) — main app
- `main/http_server/axe-os/src/app/components/edit/edit.component.spec.ts` (+13/-0) — AxeOS Angular UI
- `main/filesystem.c` (+11/-1) — main app
- `main/i2c_bitaxe.c` (+5/-6) — main app
- `components/asic/include/asic_common.h` (+9/-0) — C header
- `main/CMakeLists.txt` (+9/-0) — main app
- `main/tasks/create_jobs_task.c` (+2/-7) — firmware task module
- `main/thermal/EMC2103.h` (+8/-1) — thermal/fan control
- `main/bap/bap.c` (+7/-1) — BAP (Bitaxe Auxiliary Peripheral) bus
- `main/bap/bap_readme.md` (+5/-3) — BAP (Bitaxe Auxiliary Peripheral) bus
- `components/asic/include/asic.h` (+7/-0) — C header
- `main/http_server/axe-os/src/app/components/edit/edit.component.ts` (+6/-1) — AxeOS Angular UI
- `main/input.c` (+6/-1) — main app
- `main/power/asic_reset.c` (+4/-3) — main app
- `main/global_state.h` (+5/-0) — shared global state structs/flags
- `main/http_server/system_api_json.c` (+4/-1) — HTTP server + REST API handlers
- `main/power/asic_reset.h` (+4/-1) — main app

… 17 more changed files (mostly .github/workflows, components/asic/include, main, main/http_server, main/images, main/images/fonts_originals):
`components/asic/include/bm1366.h`, `components/asic/include/bm1368.h`, `components/asic/include/bm1370.h`, `components/asic/include/bm1397.h`, `.github/workflows/release-factory-beta.yml`, `.github/workflows/release-factory.yml`, `main/device_config.c`, `main/display.h`, `main/http_server/openapi.yaml`, `main/i2c_bitaxe.h`, `main/power/vcore.h`, `components/asic/include/bm1373.h`, `main/lv_conf.h`, `tools/requirements-image.txt`, `main/images/BitaxeBackground.jpg`, `main/images/BitaxeLogoLarge.png`, `main/images/fonts_originals/AngelWish.ttf`

## Key excerpts

### `main/display.c` `@@ -62,6 +88,144 @@ static esp_err_t read_display_config(GlobalState * GLOBAL_STATE)`

```diff
     return ESP_FAIL;
 }
 
+static esp_err_t init_i80_st7789_display(GlobalState * GLOBAL_STATE, const lvgl_port_cfg_t *lvgl_cfg)
+{
+    const I80Pins *pins = GLOBAL_STATE->DEVICE_CONFIG.pins.i80;
+    ESP_RETURN_ON_FALSE(pins, ESP_ERR_INVALID_ARG, TAG, "No I80 display pin map configured");
+    current_st7789_pins = pins;
    …
+        uint16_t rotation = nvs_config_get_u16(NVS_CONFIG_ROTATION);
+        ESP_LOGI(TAG, "Rotation: %d", rotation);
+        switch(rotation) {
+            case 90:
+                lv_display_set_rotation(disp, LV_DISPLAY_ROTATION_90);
+                break;
+            case 180:
+                lv_display_set_rotation(disp, LV_DISPLAY_ROTATION_180);
+                break;
+            case 270:
+                lv_display_set_rotation(disp, LV_DISPLAY_ROTATION_270);
+                break;
+        }
+
+        lv_style_init(&scr_style);
+        lcd_font_unscii_16 = lv_font_unscii_16;
+        lcd_font_unscii_16.fallback = &lv_font_portfolio_6x8;
+        lv_style_set_text_font(&scr_style, &lcd_font_unscii_16);
+        lv_style_set_bg_opa(&scr_style, LV_OPA_COVER);
+        lv_style_set_bg_color(&scr_style, lv_color_black());
+        lv_style_set_text_color(&scr_style, lv_color_white());
+
+        lv_theme_set_apply_cb(&theme, theme_apply);
+        lv_display_set_theme(disp, &theme);
[… hunk truncated: showing head + densest window of 144 diff lines]
```

### `main/device_config.h` `@@ -58,33 +72,40 @@ typedef struct FamilyConfig {`

```diff
     uint16_t nominal_voltage;
     uint16_t voltage_domains;
     const char * swarm_color;
+    const TPS546_CONFIG * tps546_config;
 } FamilyConfig;
 
 typedef struct DeviceConfig {
     const char * board_version;
    …
     FamilyConfig family;
+    DevicePins pins;
     bool plug_sense;
     bool asic_enable;
+    bool asic_enable_active_high;
     bool EMC2101 : 1;
     bool EMC2103 : 1;
     bool EMC2302 : 1;
+    bool emc_direct_pwm : 1;
     bool emc_internal_temp : 1;
     bool TMP1075 : 1;
     uint8_t emc_ideality_factor;
     uint8_t emc_beta_compensation;
     bool temp_flip;
+    bool display_flip : 1;
     int8_t temp_offset;
     bool DS4432U : 1;
     bool INA260  : 1;
     bool TPS546  : 1;
     // test values
     uint16_t power_consumption_target;
+    uint16_t power_consumption_margin;
+    uint16_t self_test_fan_target_rpm;
 } DeviceConfig;
[… hunk truncated: showing head + densest window of 41 diff lines]
```

### `main/screen.c` `@@ -115,8 +140,117 @@ static screen_t get_current_screen() {`

```diff
     return -1;
 }
 
+static bool is_large_display(void) {
+    return lv_display_get_vertical_resolution(NULL) > 128;
+}
+
+static void apply_screen_padding(lv_obj_t * obj) {
    …
+        return;
+    }
+
+    make_inverted_logo(&bitaxe_logo, &bitaxe_logo_inverted, bitaxe_logo_inverted_map, sizeof(bitaxe_logo_inverted_map));
+    make_inverted_logo(&osmu_logo, &osmu_logo_inverted, osmu_logo_inverted_map, sizeof(osmu_logo_inverted_map));
+    lv_image_cache_drop(&bitaxe_logo);
+    lv_image_cache_drop(&osmu_logo);
+    lv_image_cache_drop(&bitaxe_logo_inverted);
+    lv_image_cache_drop(&osmu_logo_inverted);
+    inverted_logos_ready = true;
+}
+
+static const lv_img_dsc_t * get_bitaxe_logo_src(void) {
+    if (is_large_display()) {
+        init_inverted_logos();
+        return &bitaxe_logo_inverted;
+    }
+
+    return &bitaxe_logo;
+}
+
+static const lv_img_dsc_t * get_osmu_logo_src(void) {
+    if (is_large_display()) {
+        init_inverted_logos();
[… hunk truncated: showing head + densest window of 117 diff lines]
```

### `config-1201.cvs` `@@ -0,0 +1,29 @@`

```diff
+key,type,encoding,value
+main,namespace,,
+hostname,data,string,bitaxe-naja-duo
+wifissid,data,string,myssid
+wifipass,data,string,password
+stratumurl,data,string,public-pool.io
+stratumport,data,u16,21496
+stratumuser,data,string,bc1qnp980s5fpp8l94p5cvttmtdqy8rvrq74qly2yrfmzkdsntqzlc5qkc4rkq.bitaxe
+stratumpass,data,string,x
+stratumdiff,data,u16,1000
+stratumxnsub,data,u16,0
+fbstratumurl,data,string,solo.ckpool.org
+fbstratumport,data,u16,3333
+fbstratumuser,data,string,bc1qnp980s5fpp8l94p5cvttmtdqy8rvrq74qly2yrfmzkdsntqzlc5qkc4rkq.bitaxe
+fbstratumpass,data,string,x
+fbstratumdiff,data,u16,1000
+fbstratumxnsum,data,u16,0
+asicfrequency,data,u16,327
+asicvoltage,data,u16,1000
+asicmodel,data,string,BM1373
+devicemodel,data,string,NajaDuo
+boardversion,data,string,1201
+rotation,data,u16,0
+autofanspeed,data,u16,1
+temptarget,data,u16,50
+fanspeed,data,u16,100
+selftest,data,u16,1
+selftest_warm,data,u16,45
+overheat_mode,data,u16,0
```
