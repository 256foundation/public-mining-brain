# Bitaxe selected ESP Miner firmware release records

> Source: https://api.github.com/repos/bitaxeorg/ESP-Miner/releases?per_page=100
> Collected: 2026-10-07
> Published: Unknown

Method: selected releases from the public GitHub API. Calendar dates are the UTC date component of published_at. Release notes and prerelease flags are preserved.

## v1.0

- URL: https://github.com/bitaxeorg/ESP-Miner/releases/tag/v1.0
- Published UTC: 2023-07-01T20:10:34Z
- Calendar date UTC: 2023-07-01
- Prerelease: false

### Release notes

Firmware for the Bitaxe v2.2

* Supports Stratum v1
* 300-350 GH/s
* Wifi connectivity
* Mining statistics visible on OLED display
* Power management for solar applications

Instructions:
1. Copy `config.cvs.example` to `config.cvs` and modify myssid/mypass with your home Wifi credentials (Only supports 2.4ghz connection) and stratumurl/stratumport/stratumuser/stratumpass with the stratum server and login that you would like to use.

2. Install bitaxetool from pip. pip is included with Python 3.4 but if you need to install it check https://pip.pypa.io/en/stable/installation/
```
pip install --upgrade bitaxetool
```

3.  Flash the firmware and config.cvs onto your Bitaxe
```
bitaxetool --config ./config.cvs --firmware ./esp-miner.bin
```

Note: esp-miner-475.bin uses bm1397 hashing frequency of 475 and esp-miner-425.bin is set to 425

## v2.0.0

- URL: https://github.com/bitaxeorg/ESP-Miner/releases/tag/v2.0.0
- Published UTC: 2023-10-04T23:31:14Z
- Calendar date UTC: 2023-10-04
- Prerelease: false

### Release notes

### Firmware for the Bitaxe Max (1397) and Bitaxe Ultra (1366)
### New Features
 - Initial support for the BM1366 (S19) ASIC
 - AxeOS Web UI based on Angular. Interface can be accessed on port 80 (http://)
 - HTTP+JSON based API for device configuration
 - Updated and expanded partitioning scheme
 - OTA updates over HTTP
 - SoftAP support for Onboarding without a working WiFi configuration.
 - Captive portal for easier onboarding
 
### Factory Setup

Starting with v2.0.0, the ESP-Miner firmware requires some basic manufacturing data to be flashed in the NVS partition. 

1. Copy `config.cvs.example` to `config.cvs` and modify `asicfrequency`, `asicvoltage`, `asicmodel`, `devicemodel`, and `boardversion`.

- recommended values for the Bitaxe 1366 ultra

```
key,type,encoding,value
main,namespace,,
asicfrequency,data,u16,485
asicvoltage,data,u16,1320
asicmodel,data,string,BM1366
devicemodel,data,string,ultra
boardversion,data,string,0.11
```
- recommended values for the Bitaxe 1397
```
key,type,encoding,value
main,namespace,,
asicfrequency,data,u16,475
asicvoltage,data,u16,1400
asicmodel,data,string,BM1397
devicemodel,data,string,max
boardversion,data,string,2.2
```

3. Install bitaxetool from pip. pip is included with Python 3.4 but if you need to install it check https://pip.pypa.io/en/stable/installation/
```
pip install --upgrade bitaxetool
```

4.  Flash the merged firmware and config.cvs onto your Bitaxe
```
bitaxetool --config ./config.cvs --firmware ./esp-miner-factory-v2.0.0.bin
```

Thank you to @benjamin-wilson, @skot, @Georges760, @developeralgo8888, @SatsForFreedom, and the Open Source Miners United (OSMU) community for their contributions to this release.

## v2.0.4

- URL: https://github.com/bitaxeorg/ESP-Miner/releases/tag/v2.0.4
- Published UTC: 2023-11-27T00:29:30Z
- Calendar date UTC: 2023-11-27
- Prerelease: false

### Release notes

## New Features
* Swarm view in AxeOS. Monitor and administrate all your AxeOS devices from a single view.
## What's Changed
* Fix formula for automatic fan control and adjust minimum fan speed by @ozbibi in https://github.com/skot/ESP-Miner/pull/59
* Hide logs and websocket connection on page startup
* http_server: handle missing key/values in system settings updates
## New Contributors
* @ozbibi made their first contribution in https://github.com/skot/ESP-Miner/pull/59

**Full Changelog**: https://github.com/skot/ESP-Miner/compare/v2.0.3...v2.0.4

## v2.1.0

- URL: https://github.com/bitaxeorg/ESP-Miner/releases/tag/v2.1.0
- Published UTC: 2024-03-04T02:48:39Z
- Calendar date UTC: 2024-03-04
- Prerelease: false

### Release notes

## What's Changed
* AxeOS GUI refactor
* Add BM1368 support by @johnny9 in https://github.com/skot/ESP-Miner/pull/106
* Issue #112 resolved : build instructions added to Readme.md by @Collins-Webdev in https://github.com/skot/ESP-Miner/pull/114
* Revert "Issue #112 resolved : build instructions added to Readme.md" by @skot in https://github.com/skot/ESP-Miner/pull/115

## New Contributors
* @Collins-Webdev made their first contribution in https://github.com/skot/ESP-Miner/pull/114

**Full Changelog**: https://github.com/skot/ESP-Miner/compare/v2.0.7...v2.1.0

## v2.11.0

- URL: https://github.com/bitaxeorg/ESP-Miner/releases/tag/v2.11.0
- Published UTC: 2025-11-15T12:13:24Z
- Calendar date UTC: 2025-11-15
- Prerelease: false

### Release notes

## What's Changed

## AxeOS New Features

* Chart data source selection by @terratec in https://github.com/bitaxeorg/ESP-Miner/pull/955
* Switch pool on dashboard by @duckaxe in https://github.com/bitaxeorg/ESP-Miner/pull/1187
* Introduction Sensitive Data Service by @duckaxe in https://github.com/bitaxeorg/ESP-Miner/pull/1135
* Added blockFound to dashboard and API by @duckaxe in https://github.com/bitaxeorg/ESP-Miner/pull/1235
* Mobile: Moving quick links from the menu to the top bar by @duckaxe in https://github.com/bitaxeorg/ESP-Miner/pull/1307
* Automagical StratumURL cleanup by @duckaxe in https://github.com/bitaxeorg/ESP-Miner/pull/1316

## Swarm improvements

* Swarm Facelift by @duckaxe in https://github.com/bitaxeorg/ESP-Miner/pull/1231
  * Rearrange swarm layout by @terratec in https://github.com/bitaxeorg/ESP-Miner/pull/1223
  * Fix color representation for Nerdaxe devices by @duckaxe in https://github.com/bitaxeorg/ESP-Miner/pull/1232
* Swarm Grid View by @duckaxe in https://github.com/bitaxeorg/ESP-Miner/pull/1247
* Swarm device notifications by @duckaxe in https://github.com/bitaxeorg/ESP-Miner/pull/1290

## Hashing and Stratum Improvements

* Overheat protection by @WantClue in https://github.com/bitaxeorg/ESP-Miner/pull/1304
* Show block header, scriptsig and network difficulty by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1200
* Option to disable suggested difficulty by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1264
* Allow ipv6 stratum and local address by @WantClue in https://github.com/bitaxeorg/ESP-Miner/pull/1254
  * Show ipv4 ipv6 on home component by @WantClue in https://github.com/bitaxeorg/ESP-Miner/pull/1324
* Reduce stratum tcp timeout by @WantClue in https://github.com/bitaxeorg/ESP-Miner/pull/1312

## Hashrate registers

* Hashrate registers by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1249
  * Hashrate registers for BM1366, BM1368 and BM1397 by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1271
  * Hashrate Registers Part 3 by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1301
  * Reverse register error counter and percentage and remove hash rate smoothing by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1340
  * Fix heatmap tooltip and hashrate error percentage on Hex by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1345
* Hashrate Heatmap by @duckaxe in https://github.com/bitaxeorg/ESP-Miner/pull/1274

## Hardware and Display Improvements

* Bitaxe Hex 303 by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1257
* Add SH1107 display offset configuration by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1329
  * Fix SH1107 display offset by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1335
* Add Wi-Fi connect QR code to display by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1323
* GT: Simplify EMC2103 second temperature reading by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1218
* Fix ic2 errors when using tps546d24s instead of tps546d24a by @benjamin-wilson in https://github.com/bitaxeorg/ESP-Miner/pull/1293
  * Extend TPS546 detection code for other startup failures by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1319
* Disconnect Wi-Fi if IP address is not assigned by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1326
* Add degree symbol on display by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1214
* Add space before dBm by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1238
* Remove spacing from suffixString by @duckaxe in https://github.com/bitaxeorg/ESP-Miner/pull/1308

## Memory Improvements

* Misc optimizations to free more internal memory by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1280
  * Static allocation of statistics buffer by @terratec in https://github.com/bitaxeorg/ESP-Miner/pull/1246
  * Isolate NVS usage into task by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1286

## API Changes and Improvements

* Add type checks for API settings by @terratec in https://github.com/bitaxeorg/ESP-Miner/pull/880
* Change best(Session)Diff type from string to number by @duckaxe in https://github.com/bitaxeorg/ESP-Miner/pull/1202
* Set the 404 status for unknown api routes by @0xf0xx0 in https://github.com/bitaxeorg/ESP-Miner/pull/1296
* Convert API networkDifficulty to number by @duckaxe in https://github.com/bitaxeorg/ESP-Miner/pull/1309

## Documentation

* Update notes in readme to mention the usb-c problem of models before 602 by @kakulukia in https://github.com/bitaxeorg/ESP-Miner/pull/1225
* Add note about ESP32 module type by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1243
* Add notes on esptool version requirement and Wi-Fi routers that block Bitaxe traffic by @STSMiner1 in https://github.com/bitaxeorg/ESP-Miner/pull/1252
* Fix stratum submit_share code comments by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1306

## Bugfixes

* Fix form elements hover/focus color by @duckaxe in https://github.com/bitaxeorg/ESP-Miner/pull/1227
* Destroy subscriptions when leaving page by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1237
* Fix watchdog timer on screen init by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1268
* Fix scriptsig decoder crash by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1273
* Init hashrate register statistics data if hashrate registers are not available by @WantClue in https://github.com/bitaxeorg/ESP-Miner/pull/1263
* Fix scriptsig decoder crash part 2 by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1276
* Fix missing IPv6 zone identifier append by @WantClue in https://github.com/bitaxeorg/ESP-Miner/pull/1277
* Fix System Page issues by @duckaxe in https://github.com/bitaxeorg/ESP-Miner/pull/1278
* Fix chart data source key for local storage by @terratec in https://github.com/bitaxeorg/ESP-Miner/pull/1256
* Fix swarm live data with fallback fields by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1265
* Load default theme if none stored in nvs by @WantClue in https://github.com/bitaxeorg/ESP-Miner/pull/1295
* Fix JSON of DEFAULT_COLORS by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1297
* Improving sensitive data masking for text fields by @duckaxe in https://github.com/bitaxeorg/ESP-Miner/pull/1287
* Handle invalid temperature readings by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1285
* Fix theme color preselect by @duckaxe in https://github.com/bitaxeorg/ESP-Miner/pull/1299
* Fix sensitive data visibility on dashboard by @duckaxe in https://github.com/bitaxeorg/ESP-Miner/pull/1305
* Fix heatmap on Max and Hex by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1318
* Fix manual fan speed setting by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1331
* Fix: some swarm issues by @duckaxe in https://github.com/bitaxeorg/ESP-Miner/pull/1330
* QuickLinks: Return only know hosts by @duckaxe in https://github.com/bitaxeorg/ESP-Miner/pull/1327
* Don't try to printf %s a number in nvs_config_init_fallback() by @skot in https://github.com/bitaxeorg/ESP-Miner/pull/1337
* Reduces bap logging by @WantClue in https://github.com/bitaxeorg/ESP-Miner/pull/1339
* Fix shares rejected reasons break by @duckaxe in https://github.com/bitaxeorg/ESP-Miner/pull/1341
* Fix tooltip component (no value -> value) by @duckaxe in https://github.com/bitaxeorg/ESP-Miner/pull/1343
* Shortenend error percentage option by @duckaxe in https://github.com/bitaxeorg/ESP-Miner/pull/1346
* Increase z-index for tooltip backdrop by @duckaxe in https://github.com/bitaxeorg/ESP-Miner/pull/1349

## Code Quality

* Uniform dashboard dropdowns by @duckaxe in https://github.com/bitaxeorg/ESP-Miner/pull/1270
* Replace deprecated HttpClientModule by @duckaxe in https://github.com/bitaxeorg/ESP-Miner/pull/1160
* Remove unused edit.component.scss by @duckaxe in https://github.com/bitaxeorg/ESP-Miner/pull/1197
* Move html calcs to ts by @WantClue in https://github.com/bitaxeorg/ESP-Miner/pull/1275
* Remove INA260_installed method by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1266
* Move dashboard messages from template to component by @duckaxe in https://github.com/bitaxeorg/ESP-Miner/pull/1229
* Refactor hashrate to float and timestamps to ms by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1251
* Check error if SYSTEM_init_peripherals fails by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1320
* Refactor fallback for asic frequency and fan speed NVS config by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1334
* Introduction Tooltip Components by @duckaxe in https://github.com/bitaxeorg/ESP-Miner/pull/1175

## Build System

* Introduce tools/upload2device.py by @johnny9 in https://github.com/bitaxeorg/ESP-Miner/pull/1145
* Switch to latest stable verion of ESP IDF 5.5.1 by @eandersson in https://github.com/bitaxeorg/ESP-Miner/pull/1215
* Update esp_lvgl_port dependency version to 2.6.2 by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1294
* Self test external temp by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1302

## New Contributors
* @kakulukia made their first contribution in https://github.com/bitaxeorg/ESP-Miner/pull/1225

**Full Changelog**: https://github.com/bitaxeorg/ESP-Miner/compare/v2.10.1...v2.11.0

## v2.12.2

- URL: https://github.com/bitaxeorg/ESP-Miner/releases/tag/v2.12.2
- Published UTC: 2026-01-06T21:59:49Z
- Calendar date UTC: 2026-01-06
- Prerelease: false

### Release notes

## v2.12.2 Changelog

## Improvements
- GT Self Test
- TPS Phase register #1490 
- self test improvements #1480 
- Fix tests nonce diff #1461 
- Show units in self test #1432 

## New Hardware
- The Bitaxe GT 801 is finally supported #1479 #1478



**Full Changelog**: https://github.com/bitaxeorg/ESP-Miner/compare/v2.12.0...v2.12.1

## v2.13.0

- URL: https://github.com/bitaxeorg/ESP-Miner/releases/tag/v2.13.0
- Published UTC: 2026-02-20T19:38:58Z
- Calendar date UTC: 2026-02-20
- Prerelease: false

### Release notes

## What's Changed

### New Devices
* add 801 config by @WantClue in #1479
  * 801 Strapless working by @benjamin-wilson in #1478
  * Tps phase registers by @WantClue in #1490
* Add support for 650 by @benjamin-wilson in #1537
  * Update the defaults for 650 duo to 400mhz by @benjamin-wilson and @WantClue in #1557

### AxeOS
* Add AtlasPool.io dashboard link for AtlasPool.io users by @mweinberg in #1416
* Add response time to graph by @mutatrum in #1423
* Show notification on dashboard when device is unreachable by @duckaxe in #1385
* feat: warning if default address is been used by @WantClue in #1449
* Bring back uptime by @mutatrum in #1428
* Add custom icon to <tooltip-text-icon> component by @duckaxe in #1435
* dismiss block found, feat int for blockfound, feat clear screen by @WantClue in #1550

### Hashing and Hardware
* Go Queueless by @mutatrum in #1424
* Coinbase transaction parser by @mutatrum in #1391
  * Handle coinbase tx parser for other chains by @mutatrum in #1540
  * Add option to disable coinbase tx decode by @mutatrum in #1544
  * fix sensitive dots by @WantClue in #1542
* Fan controller task by @mutatrum in #1357
* merge fan rpms into fan 1 speed as tooltip by @0xf0xx0 in #1527

### Stratum
* Add TLS support by @AxisRay, @mutatrum and @duckaxe in #1413
  * Restore socket options after #1413 by @mutatrum in #1447
* Add name resolve for public IPv6 addresses by @mutatrum in #1468
* Add mining.ping support by @mutatrum in #1439

### Display
* Turn on the screen for identify mode by @terratec in #1443
* Wake screen briefly on button press or non-carousel screens by @mutatrum in #1366
* Extend the Portfolio font by @mutatrum in #1502

### BAP
* BAP Protocol improvements by @benjamin-wilson in #1525
  * feat: add share REQ by @WantClue in #1482
  * feat: add found block param to BAP by @WanrClue in #1547

### Swarm
* Clear power fault on swarm by @mutatrum in #1524
  * Fix swarm scan by @mutatrum in #1528

### Code Cleanup and Refactoring
* Add missing keys to openapi.yaml, split responses into schemas by @0xf0xx0 in #1433
* openapi spec updating by @0xf0xx0 in #1467
* Misc. set of improvements and error checking by @mutatrum in #1422
* Single options request handler for API by @mutatrum in #1501

### Bug Fixes
* Update block found condition to >=  by @leandroalbero in #1419
* Fix logs font by @duckaxe in #1448
* Fix: Ensure that isUsingFallbackStratum is a number by @duckaxe in #1332
* Add support for 32 character SSID and show connection screen if Wi-Fi disconnects by @mutatrum in #1376
* valid_jobs_lock wasn't initialised properly by @mutatrum in #1441
* Fix possible out-of-bounds write by @terratec in #1460
* Some small bugs and cleanups by @mutatrum in #1496
* Free SHA256 context in utils.c by @mutatrum in #1508
* Fix crash on restart due to Wi-Fi shutting down by @mutatrum in #1530
* statistics_task: use uint64_t timestamps to prevent 32-bit overflow by @r3mko in #1545
* improve empty string on null init + formatting by @WantClue in #1483
* Spike on hashrate graph by @mutatrum in #1558
  * Fix hashrate spike by @mutatrum in #1559

### Build system and testing
* show units in self test by @WantClue in #1432
* Fix tests nonce diff checking by @terratec in #1461
* Self test was prevously not rolling ntime and the search space was rolling over. Improve logging, misc by @benjamin-wilson in #1480
* fix angular tests by @beati in #1452
* Update to ESP-IDF v5.5.2 by @eandersson in #1486
* increase main task for self test extensive logging by @WantClue in #1492
* Change selftest value from 0 to 1 by @WantClue in #1494
* Generate frontend api services from openapi spec by @0xf0xx0 in #1442
  * Frontend openapi by @WantClue in #1503
  * fix: package lock update and openapi only build if changes detected by @WantClue in #1526

### Documentation
* Add a hint for CHROME_BIN by @beati in #1489
* Add devcontainer documentation to readme.md by @bonifacio123 in #1538

## New Contributors
* @leandroalbero made their first contribution in #1419
* @mweinberg made their first contribution in #1416
* @beati made their first contribution in #1452
* @r3mko made their first contribution in #1545

**Full Changelog**: https://github.com/bitaxeorg/ESP-Miner/compare/v2.12.2...v2.13.0

## v2.14.0

- URL: https://github.com/bitaxeorg/ESP-Miner/releases/tag/v2.14.0
- Published UTC: 2026-06-04T17:52:24Z
- Calendar date UTC: 2026-06-04
- Prerelease: false

### Release notes

## What's Changed

### AxeOS
* Customizable dashboard by @WantClue in https://github.com/bitaxeorg/ESP-Miner/pull/1622
* Add scoreboard :trophy:  by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1236
* Show actual frequency on dashboard by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1629
* Add log download button with log preservation over soft reboots by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1646
* Modal firmware update progress by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1650
* Add cpu usage task and asic share processing time by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1621
* Show actual resolved frequency by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1674
* Add testnet/regtest network detection to coinbase decoder by @warioishere in https://github.com/bitaxeorg/ESP-Miner/pull/1578
* Add dynamic ticks on horizontal chart axis by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1660
* Add wide screen toggle by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1663
* resize for mobile view by @WantClue in https://github.com/bitaxeorg/ESP-Miner/pull/1659
### API
* Websocket api by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1623
* Fix error counter in the websocket api by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1700
### Hashing and Hardware
* Pause/resume mining by @b-rowan in https://github.com/bitaxeorg/ESP-Miner/pull/1608
* Fan controller tuning by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1640
* Flip GT temperature sensors by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1616
* functions to control nonce space and timeouts for all chip topologies by @adammwest in https://github.com/bitaxeorg/ESP-Miner/pull/420
* Pool disconnect by @WantClue in https://github.com/bitaxeorg/ESP-Miner/pull/1689
* Change hostname without reboot by @WantClue in https://github.com/bitaxeorg/ESP-Miner/pull/1726
### Stratum
* Add Stratum V2 (SV2) protocol support by @warioishere in https://github.com/bitaxeorg/ESP-Miner/pull/1553
* Measure SV2 share response time per-share by @warioishere in https://github.com/bitaxeorg/ESP-Miner/pull/1720
* Show BIP-110 signal in Block Header by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1588
* Show BIP-54 signal in Block Header by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1609
* Only count shares from mining.submit responses by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1591
* Handle `client.show_message` stratum message by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1565
* Add support for fractional difficulty in mining.set_difficulty by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1594
* Set TCP_NODELAY on pool sockets to fix SV2 submit latency by @warioishere in https://github.com/bitaxeorg/ESP-Miner/pull/1722
### Pool support
* Change public-pool stratum port to 3333 by @WantClue in https://github.com/bitaxeorg/ESP-Miner/pull/1611
* Add m45core pool quick link by @Distortions81 in https://github.com/bitaxeorg/ESP-Miner/pull/1575
* Add parsing of new ckpool share rejection reason by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1586
* Add blitzpool rejection reasons by @warioishere in https://github.com/bitaxeorg/ESP-Miner/pull/1695
* Add miningcore reject reason parsing by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1701
### Bug Fixes
* Fix hashrate counter overflow on reconnect by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1564
* fix: reboots bitaxe if only ssid changed by @WantClue in https://github.com/bitaxeorg/ESP-Miner/pull/1598
* cutting the blocking time, http server responsive by @WantClue in https://github.com/bitaxeorg/ESP-Miner/pull/1635
* Fix dashboard at startup and heatmap colors by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1634
* Fix url decoding of the statistics endpoint path parameters by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1677
* Fix power reading race condition and improve error handling by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1669
* Fix hashrate spikes by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1673
* Fix small memory leaks in stratum handling by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1666
* Fix cpu usage measurement spikes by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1654
* Code review fixes by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1641
* Fix pool diff logging by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1661
* Improve dashboard performance by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1725
* fix restart button not available after selecting new ssid by @WantClue in https://github.com/bitaxeorg/ESP-Miner/pull/1751
### Self-test
* Self-test: auto-restart 10s after pass for Bitaxe Touch setups by @SoloSatoshi in https://github.com/bitaxeorg/ESP-Miner/pull/1602
* Add missing self-test failure logs by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1613
* Self test adjustments by @WantClue in https://github.com/bitaxeorg/ESP-Miner/pull/1610
* Refactor self-test by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1615
* Self test refactor 2 by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1632
* Increase self_test ASIC start temperature by @benjamin-wilson in https://github.com/bitaxeorg/ESP-Miner/pull/1642
* Improve factory self-test validation and thermal control by @benjamin-wilson  in https://github.com/bitaxeorg/ESP-Miner/pull/1738
### Code Cleanup and Refactoring
* Fix double handler registration for restart API endpoint by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1614
* Add support for indexed strings in NVS config by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1504
* Remove unused npm dependencies by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1627
* Migrate openapitools to ng-openapi-gen by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1597
* Use format specifiers for printf statements by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1698
* Consolidate shared stratum socket, wifi and clean-queue helpers by @warioishere in https://github.com/bitaxeorg/ESP-Miner/pull/1724
* Clean up SV2 NVS configuration by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1743
### Build system and testing
* Update Checkout and Python Actions to latest by @eandersson in https://github.com/bitaxeorg/ESP-Miner/pull/1583
* Update to latest node and node actions by @eandersson in https://github.com/bitaxeorg/ESP-Miner/pull/1582
* Update to ESP IDF 5.5.3 by @eandersson in https://github.com/bitaxeorg/ESP-Miner/pull/1581
* Add AGENTS.md by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1656
* Fix frontend test failures by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1667
* Run frontend test in CI by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1653

## New Contributors
* @SoloSatoshi made their first contribution in https://github.com/bitaxeorg/ESP-Miner/pull/1602
* @Distortions81 made their first contribution in https://github.com/bitaxeorg/ESP-Miner/pull/1575
* @warioishere made their first contribution in https://github.com/bitaxeorg/ESP-Miner/pull/1578

**Full Changelog**: https://github.com/bitaxeorg/ESP-Miner/compare/v2.13.2...v2.14.0

## v2.15.0

- URL: https://github.com/bitaxeorg/ESP-Miner/releases/tag/v2.15.0
- Published UTC: 2026-08-21T08:25:08Z
- Calendar date UTC: 2026-08-21
- Prerelease: false

### Release notes

## What's Changed

### Notables

> [!IMPORTANT]
> The AxeOS web interface is now embedded directly into the main firmware binary (`esp-miner.bin`). This means you no longer need to upload a separate `www.bin` file when updating your miner. Make sure to refresh the dashboard page after the firmware update.

> [!NOTE]
> With this version we also added mDNS support, which means you can now open the AxeOS dashboard with the hostname of the miner, instead of the IP address.

### AxeOS
* Add mDNS support for network discovery and dynamic hostname updates by @camalolo in https://github.com/bitaxeorg/ESP-Miner/pull/1240
* Add multi-line charts by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1736
* Add total uptime and hashes by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1555
* Refactor theme mechanism by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1637
* Prompt before restart in topbar by @0xf0xx0 in https://github.com/bitaxeorg/ESP-Miner/pull/1831
* Show target temp on temp bars by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1691
* Move uptime to misc card by @0xf0xx0 in https://github.com/bitaxeorg/ESP-Miner/pull/1687
* Remove luck from hashrate card by @0xf0xx0 in https://github.com/bitaxeorg/ESP-Miner/pull/1832
* Improve undervoltage detection in UI by @WantClue in https://github.com/bitaxeorg/ESP-Miner/pull/1888
* Show pending SV2 shares on the dashboard by @warioishere in https://github.com/bitaxeorg/ESP-Miner/pull/1735

### Pool support
* More pools by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1795
* Add SoloLuck pool to quicklink service by @sololuckio in https://github.com/bitaxeorg/ESP-Miner/pull/1785
* Set default value of useFallbackStratum to false by @r3mko in https://github.com/bitaxeorg/ESP-Miner/pull/1823
* Add SV2 "require authentication" per-pool option by @cbyam in https://github.com/bitaxeorg/ESP-Miner/pull/1796

### Stratum
* Send SV2 frames in a single write by @warioishere in https://github.com/bitaxeorg/ESP-Miner/pull/1771
* Increase SV2 frame size to 8kb by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1783
* Reduce SV2 minimum extranonce size from 6->2 bytes by @0xf0xx0 in https://github.com/bitaxeorg/ESP-Miner/pull/1799
* Keep fractional SV2 pool difficulty to avoid difficulty-too-low rejects by @warioishere in https://github.com/bitaxeorg/ESP-Miner/pull/1779
* Ignore duplicate stratum jobId by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1731

### Hashing and Hardware
* Add board version 603 support by @WantClue in https://github.com/bitaxeorg/ESP-Miner/pull/1760
* Add TPS546 config to NVS by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1838
* Higher VIN for solar by @WantClue in https://github.com/bitaxeorg/ESP-Miner/pull/1819
* Bluetooth LE by @WantClue in https://github.com/bitaxeorg/ESP-Miner/pull/1827
* Add global PSRAM allocation check by @WantClue in https://github.com/bitaxeorg/ESP-Miner/pull/1772

### Bug Fixes
* HTTP Handler Audit by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1759
* Remove stale WebSocket clients after async send failures by @frickl in https://github.com/bitaxeorg/ESP-Miner/pull/1803
* Fix heap fragmentation crash by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1766
* Fix use after free race condition by @WantClue in https://github.com/bitaxeorg/ESP-Miner/pull/1797
* Buffer overflow in rejected-share stats by @Zayno in https://github.com/bitaxeorg/ESP-Miner/pull/1754
* Fix live WebSocket reconnect loop by @eandersson in https://github.com/bitaxeorg/ESP-Miner/pull/1830
* Fix work received notification with SV2 by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1778
* Parse response.message on swarm page by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1788
* Fix swarm device edit by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1767
* Disable browser autocomplete for pool password fields by @mbmtbtbc in https://github.com/bitaxeorg/ESP-Miner/pull/1733

### Code Cleanup and Refactoring
* Purge PrimeNG and migrate to Tailwind CSS by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1815
* Upgrade AxeOS to Angular 19 by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1651
* Angular Control Flow Migration by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1835
* Free internal memory by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1761
* Cleanup stratum parsing code by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1755
* Clean up unused mining-pool service by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1748
* Decouple header dependencies and improve type safety by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1826

### Documentation
* Add community section to readme by @WantClue in https://github.com/bitaxeorg/ESP-Miner/pull/1773
* Correct hashrate register unit comment by @pRizz in https://github.com/bitaxeorg/ESP-Miner/pull/1885

### Self-test
* Configurable self test warmup temp by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1764
* Make self test fan speed adjustable by @WantClue in https://github.com/bitaxeorg/ESP-Miner/pull/1817
* Adjust freq to also fallback to default on self test by @WantClue in https://github.com/bitaxeorg/ESP-Miner/pull/1805
* Stratum coordinator doesn't need to run on self test by @WantClue in https://github.com/bitaxeorg/ESP-Miner/pull/1882

### Build system and testing
* Unified firmware by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1763
* Upgrade to ESP-IDF 6.0.2 by @eandersson in https://github.com/bitaxeorg/ESP-Miner/pull/1829
* Connect npm dev server to real device by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1699

## New Contributors
* @mbmtbtbc made their first contribution in https://github.com/bitaxeorg/ESP-Miner/pull/1733
* @Zayno made their first contribution in https://github.com/bitaxeorg/ESP-Miner/pull/1754
* @camalolo made their first contribution in https://github.com/bitaxeorg/ESP-Miner/pull/1240
* @sololuckio made their first contribution in https://github.com/bitaxeorg/ESP-Miner/pull/1785
* @frickl made their first contribution in https://github.com/bitaxeorg/ESP-Miner/pull/1803
* @cbyam made their first contribution in https://github.com/bitaxeorg/ESP-Miner/pull/1796

**Full Changelog**: https://github.com/bitaxeorg/ESP-Miner/compare/v2.14.0...v2.15.0rc1

## v2.15.2

- URL: https://github.com/bitaxeorg/ESP-Miner/releases/tag/v2.15.2
- Published UTC: 2026-09-18T06:20:56Z
- Calendar date UTC: 2026-09-18
- Prerelease: true

### Release notes

## What's Changed
* fix: prevent reconnect storms from slow clients by @r3mko in https://github.com/bitaxeorg/ESP-Miner/pull/1913
* Add BM1372/BM1373 ASIC driver support by @benjamin-wilson in https://github.com/bitaxeorg/ESP-Miner/pull/1890
* Bitaxe Color: Naja Duo and Gamma Hex support with ST7789 display by @benjamin-wilson, @WantClue and @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1916

## New Contributors
* @r3mko made their first contribution in https://github.com/bitaxeorg/ESP-Miner/pull/1913

**Full Changelog**: https://github.com/bitaxeorg/ESP-Miner/compare/v2.15.1...v2.15.2
