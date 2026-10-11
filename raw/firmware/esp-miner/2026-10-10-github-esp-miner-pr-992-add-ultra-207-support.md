# ESP-Miner PR #992: Add Ultra 207 support

> Source: https://github.com/bitaxeorg/ESP-Miner/pull/992
> Collected: 2026-10-10
> Published: 2025-05-31
> Registry ID: esp-miner

State: closed | Merged: 2025-06-10 | Author: mutatrum | +26/-2 | Labels: enhancement, critical

## Body

Fixes #989 

## Files changed

- `config-207.cvs` (+23/-0) — changed file
- `.github/workflows/release-factory-beta.yml` (+1/-1) — CI workflow
- `.github/workflows/release-factory.yml` (+1/-1) — CI workflow
- `main/device_config.h` (+1/-0) — main app

## Key excerpts

### `config-207.cvs` `@@ -0,0 +1,23 @@`

```diff
+key,type,encoding,value
+main,namespace,,
+hostname,data,string,bitaxe
+wifissid,data,string,
+wifipass,data,string,
+stratumurl,data,string,public-pool.io
+stratumport,data,u16,21496
+stratumuser,data,string,bc1qnp980s5fpp8l94p5cvttmtdqy8rvrq74qly2yrfmzkdsntqzlc5qkc4rkq.bitaxe
+stratumpass,data,string,x
+fbstratumurl,data,string,solo.ckpool.org
+fbstratumport,data,u16,3333
+fbstratumuser,data,string,bc1qnp980s5fpp8l94p5cvttmtdqy8rvrq74qly2yrfmzkdsntqzlc5qkc4rkq.bitaxe
+fbstratumpass,data,string,x
+asicfrequency,data,u16,485
+asicvoltage,data,u16,1200
+asicmodel,data,string,BM1366
+devicemodel,data,string,ultra
+boardversion,data,string,207
+flipscreen,data,u16,1
+autofanspeed,data,u16,1
+fanspeed,data,u16,100
+selftest,data,u16,1
+overheat_mode,data,u16,0
\ No newline at end of file
```

### `main/device_config.h` `@@ -88,6 +88,7 @@ static const DeviceConfig default_configs[] = {`

```diff
     { .board_version = "203",  .family = FAMILY_ULTRA,       .EMC2101 = true, .emc_internal_temp = true,                                  .emc_temp_offset = 5,   .DS4432U = true, .INA260 = true, .plug_sense = true, .asic_enable = true, .power_consumption_target = 12, },
     { .board_version = "204",  .family = FAMILY_ULTRA,       .EMC2101 = true, .emc_internal_temp = true,                                  .emc_temp_offset = 5,   .DS4432U = true, .INA260 = true, .plug_sense = true,                      .power_consumption_target = 12, },
     { .board_version = "205",  .family = FAMILY_ULTRA,       .EMC2101 = true, .emc_internal_temp = true,                                  .emc_temp_offset = 5,   .DS4432U = true, .INA260 = true, .plug_sense = true, .asic_enable = true, .power_consumption_target = 12, },
+    { .board_version = "207",  .family = FAMILY_ULTRA,       .EMC2101 = true,                                                                                     .TPS546 = true,                                                           .power_consumption_target = 12, },
     { .board_version = "400",  .family = FAMILY_SUPRA,       .EMC2101 = true, .emc_internal_temp = true,                                  .emc_temp_offset = 5,   .DS4432U = true, .INA260 = true, .plug_sense = true, .asic_enable = true, .power_consumption_target = 12, },
     { .board_version = "401",  .family = FAMILY_SUPRA,       .EMC2101 = true, .emc_internal_temp = true,                                  .emc_temp_offset = 5,   .DS4432U = true, .INA260 = true, .plug_sense = true, .asic_enable = true, .power_consumption_target = 12, },
     { .board_version = "402",  .family = FAMILY_SUPRA,       .EMC2101 = true,                                                                                     .TPS546 = true,                                                           .power_consumption_target = 8,  },
```

### `.github/workflows/release-factory-beta.yml` `@@ -16,7 +16,7 @@ jobs:`

```diff
     strategy:
       fail-fast: false
       matrix:
-        build_type: ["102", "202", "204", "205", "401", "402", "403", "601", "602"]
+        build_type: ["102", "202", "204", "205", "207", "401", "402", "403", "601", "602"]
     steps:
       - name: Checkout repo
         uses: actions/checkout@v4
```

### `.github/workflows/release-factory.yml` `@@ -16,7 +16,7 @@ jobs:`

```diff
     strategy:
       fail-fast: false
       matrix:
-        build_type: ["102", "201", "202", "203", "204", "205", "401", "402", "403", "601", "602"]
+        build_type: ["102", "201", "202", "203", "204", "205", "207", "401", "402", "403", "601", "602"]
     steps:
       - name: Checkout repo
         uses: actions/checkout@v4
```
