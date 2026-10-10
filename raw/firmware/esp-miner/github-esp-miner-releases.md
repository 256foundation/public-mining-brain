# bitaxeorg/ESP-Miner release notes (59 releases)

> Source: https://github.com/bitaxeorg/ESP-Miner/releases
> Collected: 2026-10-07
> Published: Unknown

## checksum-test-0 (checksum-test-0)

- Published: 2026-09-26
- Link: https://github.com/bitaxeorg/ESP-Miner/releases/tag/checksum-test-0
- Prerelease: True

! Checksum test

**Full Changelog**: https://github.com/bitaxeorg/ESP-Miner/compare/v2.15.0...checksum-test-0

## v2.15.3 (v2.15.3)

- Published: 2026-09-20
- Link: https://github.com/bitaxeorg/ESP-Miner/releases/tag/v2.15.3
- Prerelease: False

## What's Changed
* fix(axe-os): derive low-frequency warnings from device presets by @vortexopenclaw in #1961

## New Contributors
* @vortexopenclaw made their first contribution in #1961

**Full Changelog**: https://github.com/bitaxeorg/ESP-Miner/compare/v2.15.2...v2.15.3

## v2.15.2 (v2.15.2)

- Published: 2026-09-18
- Link: https://github.com/bitaxeorg/ESP-Miner/releases/tag/v2.15.2
- Prerelease: True

## What's Changed
* fix: prevent reconnect storms from slow clients by @r3mko in https://github.com/bitaxeorg/ESP-Miner/pull/1913
* Add BM1372/BM1373 ASIC driver support by @benjamin-wilson in https://github.com/bitaxeorg/ESP-Miner/pull/1890
* Bitaxe Color: Naja Duo and Gamma Hex support with ST7789 display by @benjamin-wilson, @WantClue and @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1916

## New Contributors
* @r3mko made their first contribution in https://github.com/bitaxeorg/ESP-Miner/pull/1913

**Full Changelog**: https://github.com/bitaxeorg/ESP-Miner/compare/v2.15.1...v2.15.2

## v2.15.1 (v2.15.1)

- Published: 2026-08-29
- Link: https://github.com/bitaxeorg/ESP-Miner/releases/tag/v2.15.1
- Prerelease: False

## What's Changed

### Bug Fixes

- Adapt download assets message in update page by @tassoneroberto in #1907 
- Fix swarm ips by @WantClue in #1905
- Disable RSNO client support to fix WPA 2/3 Compatibility mode by @mutatrum in #1912

## New Contributors
- @tassoneroberto made their first contribution in #1907

**Full Changelog**: https://github.com/bitaxeorg/ESP-Miner/compare/v2.15.0...v2.15.1

## v2.15.0 (v2.15.0)

- Published: 2026-08-21
- Link: https://github.com/bitaxeorg/ESP-Miner/releases/tag/v2.15.0
- Prerelease: False

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

## v2.14.2 (v2.14.2)

- Published: 2026-07-08
- Link: https://github.com/bitaxeorg/ESP-Miner/releases/tag/v2.14.2
- Prerelease: False

# What's Changed:

- #1797 [Fix use after free race condition](https://github.com/bitaxeorg/ESP-Miner/commit/036d234e5b455c1b886c5c6c8ee0a9a3d5fe21f9)
- #1805  [fix: adjust freq to also fallback to default on self test](https://github.com/bitaxeorg/ESP-Miner/commit/64680f8a4da0b9a3b532051f0aa18429fcf04e82)


**Full Changelog**: https://github.com/bitaxeorg/ESP-Miner/compare/v2.14.1...v2.14.2

## v2.14.1 (v2.14.1)

- Published: 2026-06-19
- Link: https://github.com/bitaxeorg/ESP-Miner/releases/tag/v2.14.1
- Prerelease: False

## What's Changed
* Add board version 603 support by @WantClue in https://github.com/bitaxeorg/ESP-Miner/pull/1760
* Configurable self test warmup temp by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1764
* Fix swarm device edit by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1767
* Buffer overflow in rejected-share stats. by @Zayno in https://github.com/bitaxeorg/ESP-Miner/pull/1754

## New Contributors
* @Zayno made their first contribution in https://github.com/bitaxeorg/ESP-Miner/pull/1754

**Full Changelog**: https://github.com/bitaxeorg/ESP-Miner/compare/v2.14.0...v2.14.1

## v2.14.0 (v2.14.0)

- Published: 2026-06-04
- Link: https://github.com/bitaxeorg/ESP-Miner/releases/tag/v2.14.0
- Prerelease: False

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

## v2.14.0b4 (v2.14.0b4)

- Published: 2026-05-29
- Link: https://github.com/bitaxeorg/ESP-Miner/releases/tag/v2.14.0b4
- Prerelease: True

## What's Changed
* Websocket api by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1623
* Fix error counter in the websocket api by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1700
* Pool disconnect by @WantClue in https://github.com/bitaxeorg/ESP-Miner/pull/1689
* Set TCP_NODELAY on pool sockets to fix SV2 submit latency by @warioishere in https://github.com/bitaxeorg/ESP-Miner/pull/1722
* Add blitzpool rejection reasons by @warioishere in https://github.com/bitaxeorg/ESP-Miner/pull/1695
* Change hostname without reboot by @WantClue in https://github.com/bitaxeorg/ESP-Miner/pull/1726
* Measure SV2 share response time per-share by @warioishere in https://github.com/bitaxeorg/ESP-Miner/pull/1720
* Improve dashboard performance by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1725
* Add miningcore reject reason parsing by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1701
* Use format specifiers for printf statements by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1698
* Consolidate shared stratum socket, wifi and clean-queue helpers by @warioishere in https://github.com/bitaxeorg/ESP-Miner/pull/1724


**Full Changelog**: https://github.com/bitaxeorg/ESP-Miner/compare/v2.14.0b3...v2.14.0b4

## v2.14.0b3 (v2.14.0b3)

- Published: 2026-05-19
- Link: https://github.com/bitaxeorg/ESP-Miner/releases/tag/v2.14.0b3
- Prerelease: True

## What's Changed
* Add Stratum V2 (SV2) protocol support by @warioishere in https://github.com/bitaxeorg/ESP-Miner/pull/1553


**Full Changelog**: https://github.com/bitaxeorg/ESP-Miner/compare/v2.14.0b2...v2.14.0b3

## v2.14.0b2 (v2.14.0b2)

- Published: 2026-05-06
- Link: https://github.com/bitaxeorg/ESP-Miner/releases/tag/v2.14.0b2
- Prerelease: True

## What's Changed
* resize for mobile view by @WantClue in https://github.com/bitaxeorg/ESP-Miner/pull/1659
* Fix pool diff logging by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1661
* Code review fixes by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1641
* Fix cpu usage measurement spikes by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1654
* Add wide screen toggle by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1663
* Run frontend test in CI by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1653
* Fix frontend test failures by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1667
* Add dynamic ticks on horizontal chart axis by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1660
* Add testnet/regtest network detection to coinbase decoder by @warioishere in https://github.com/bitaxeorg/ESP-Miner/pull/1578
* Fix small memory leaks in stratum handling by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1666
* Fix hashrate spikes by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1673
* Add AGENTS.md by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1656
* Show actual resolved frequency by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1674
* Fix power reading race condition and improve error handling by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1669
* Fix url decoding of the statistics endpoint path parameters by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1677
* functions to control nonce space and timeouts for all chip topologies by @adammwest in https://github.com/bitaxeorg/ESP-Miner/pull/420

## New Contributors
* @warioishere made their first contribution in https://github.com/bitaxeorg/ESP-Miner/pull/1578

**Full Changelog**: https://github.com/bitaxeorg/ESP-Miner/compare/v2.14.0b1...v2.14.0b2

## v2.14.0b1 (v2.14.0b1)

- Published: 2026-04-12
- Link: https://github.com/bitaxeorg/ESP-Miner/releases/tag/v2.14.0b1
- Prerelease: True

## What's Changed

### AxeOS
* Customizable dashboard by @WantClue in https://github.com/bitaxeorg/ESP-Miner/pull/1622
* Add scoreboard :trophy:  by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1236
* Show BIP-110 signal in Block Header by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1588
* Show BIP-54 signal in Block Header by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1609
* Add m45core pool quick link by @Distortions81 in https://github.com/bitaxeorg/ESP-Miner/pull/1575
* Show actual frequency on dashboard by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1629
* Add log download button with log preservation over soft reboots by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1646
* Modal firmware update progress by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1650
* Add cpu usage task and asic share processing time by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1621
### Hashing and Hardware
* Pause/resume mining by @b-rowan in https://github.com/bitaxeorg/ESP-Miner/pull/1608
* Fan controller tuning by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1640
* Flip GT temperature sensors by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1616
### Stratum
* Add parsing of new ckpool share rejection reason by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1586
* Change public-pool stratum port to 3333 by @WantClue in https://github.com/bitaxeorg/ESP-Miner/pull/1611
* Only count shares from mining.submit responses by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1591
* Handle `client.show_message` stratum message by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1565
* Add support for fractional difficulty in mining.set_difficulty by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1594
### Code Cleanup and Refactoring
* Fix double handler registration for restart API endpoint by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1614
* Add support for indexed strings in NVS config by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1504
* Remove unused npm dependencies by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1627
* Migrate openapitools to ng-openapi-gen by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1597
### Bug Fixes
* Fix hashrate counter overflow on reconnect by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1564
* fix: reboots bitaxe if only ssid changed by @WantClue in https://github.com/bitaxeorg/ESP-Miner/pull/1598
* cutting the blocking time, http server responsive by @WantClue in https://github.com/bitaxeorg/ESP-Miner/pull/1635
* Fix dashboard at startup and heatmap colors by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1634
### Self-test
* Self-test: auto-restart 10s after pass for Bitaxe Touch setups by @SoloSatoshi in https://github.com/bitaxeorg/ESP-Miner/pull/1602
* Add missing self-test failure logs by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1613
* Self test adjustments by @WantClue in https://github.com/bitaxeorg/ESP-Miner/pull/1610
* Refactor self-test by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1615
* Self test refactor 2 by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1632
* Increase self_test ASIC start temperature by @benjamin-wilson in https://github.com/bitaxeorg/ESP-Miner/pull/1642
### Build system
* Update Checkout and Python Actions to latest by @eandersson in https://github.com/bitaxeorg/ESP-Miner/pull/1583
* Update to latest node and node actions by @eandersson in https://github.com/bitaxeorg/ESP-Miner/pull/1582
* Update to ESP IDF 5.5.3 by @eandersson in https://github.com/bitaxeorg/ESP-Miner/pull/1581

## New Contributors
* @SoloSatoshi made their first contribution in https://github.com/bitaxeorg/ESP-Miner/pull/1602
* @Distortions81 made their first contribution in https://github.com/bitaxeorg/ESP-Miner/pull/1575

**Full Changelog**: https://github.com/bitaxeorg/ESP-Miner/compare/v2.13.2...v2.14.0b1

## early-access-2026-03 (early-access-2026-03)

- Published: 2026-03-13
- Link: https://github.com/bitaxeorg/ESP-Miner/releases/tag/early-access-2026-03
- Prerelease: True

ESP-Miner Early Access release March 2026.

Please treat this as a preview / test build only.

Just because a pull request is merged into this canary branch does not mean it is approved for or guaranteed to reach a production release. We appreciate your help testing.

## What's Changed

 * functions to control nonce space and timeouts for all chip topologies by @adammwest in #420
 * console log easter egg by @mrv777 in #470
 * Add scoreboard 🏆 by @mutatrum in #1236
 * Add mDNS support for network discovery and dynamic hostname updates by @camalolo in #1240
 * Add solo chance page by @mutatrum in #1368
 * Ethernet-over-USB by @mutatrum in #1437
 * Add Stratum V2 (SV2) protocol support by @warioishere in #1553
 * Add total uptime and hashes by @mutatrum in #1555
 * Fix hashrate counter overflow on reconnect by @mutatrum in #1564
 * Handle `client.show_message` stratum message by @mutatrum in #1565
 * Add m45core pool quick link by @Distortions81 in #1575
 * Add pool.kryptex.com dashboard link for Kryptex Pool users by @maxmalysh in #1577
 * Add testnet/regtest network detection to coinbase decoder by @warioishere in #1578
 * Add parsing of new ckpool share rejection reason by @mutatrum in #1586
 * Show BIP-110 signal in Block Header by @mutatrum in #1588
 * Use mDNS also with Ethernet-over-USB

**Full Changelog**: https://github.com/bitaxeorg/ESP-Miner/compare/v2.13.0...early-access-2026-03

## v2.13.2 (v2.13.2)

- Published: 2026-03-05
- Link: https://github.com/bitaxeorg/ESP-Miner/releases/tag/v2.13.2
- Prerelease: True

## What's Changed
* **self_test domain monitoring by @benjamin-wilson in https://github.com/bitaxeorg/ESP-Miner/pull/1596**

* r2 dont create bucket by @WantClue in https://github.com/bitaxeorg/ESP-Miner/pull/1569
* Change coinbase reward to mining reward in banners by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1566
* Fixes self test after #1559 by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1580
* fix: linking for common by @WantClue in https://github.com/bitaxeorg/ESP-Miner/pull/1576



**Full Changelog**: https://github.com/bitaxeorg/ESP-Miner/compare/v2.13.0...v2.13.2

## v2.13.1 (v2.13.1)

- Published: 2026-03-03
- Link: https://github.com/bitaxeorg/ESP-Miner/releases/tag/v2.13.1
- Prerelease: False

## Bug Fix for Production

This release is for Manufacturers who rely on the self test.

## What's Changed
* Fixes self test after #1559 by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1580

**Full Changelog**: https://github.com/bitaxeorg/ESP-Miner/compare/v2.13.0...v2.13.1

## v2.13.0 (v2.13.0)

- Published: 2026-02-20
- Link: https://github.com/bitaxeorg/ESP-Miner/releases/tag/v2.13.0
- Prerelease: False

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

## v2.12.2 (v2.12.2)

- Published: 2026-01-06
- Link: https://github.com/bitaxeorg/ESP-Miner/releases/tag/v2.12.2
- Prerelease: False

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

## v2.12.0 (v2.12.0)

- Published: 2025-12-04
- Link: https://github.com/bitaxeorg/ESP-Miner/releases/tag/v2.12.0
- Prerelease: False

## What's Changed

## AxeOS New Features
* Identify Device by @duckaxe in https://github.com/bitaxeorg/ESP-Miner/pull/1369
* Fix: Decrease z-index of loading overlay by @duckaxe in https://github.com/bitaxeorg/ESP-Miner/pull/1398
* Add Reset Reason to System page by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1401
* Add difficulty tooltip to show full number by @duckaxe in https://github.com/bitaxeorg/ESP-Miner/pull/1399
* Allow empty Wi-Fi password by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1387
* Add 1m, 10m and 1h hashrate graph by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1348
* Add chance indicator on dashboard by @WantClue in https://github.com/bitaxeorg/ESP-Miner/pull/1407

## Swarm Improvements
* Add "This device" label to swarm by @duckaxe in https://github.com/bitaxeorg/ESP-Miner/pull/1344

## Hashing and Stratum Improvements
* Fix hashrate register for multi-chip devices by @WantClue in https://github.com/bitaxeorg/ESP-Miner/pull/1363
* Set suggested max for error percentage by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1377
* Add frequency ramp for BM1397 by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1069

## New Devices added / brought back
* Bitaxe SupraHex 701/702 by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1395

## Code Cleanup and Refactoring
* Optimize construct_bm_job by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1321
* Standardize hashrate values to Gh/s by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1371
* workflow 303 integration by @WantClue in https://github.com/bitaxeorg/ESP-Miner/pull/1367
* Track web_ui_dist files to skip build step when unchanged by @WantClue in https://github.com/bitaxeorg/ESP-Miner/pull/1338
* Pin esp_lvgl_port and esp_lcd_sh1107 versions by @WantClue in https://github.com/bitaxeorg/ESP-Miner/pull/1372
* Identify Device moved to screen overlay by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1403
* vscode stop annoying me by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1414

## Bug Fixes
* Don't write unchanged values to NVS by @WantClue in https://github.com/bitaxeorg/ESP-Miner/pull/1410
* Fix BM1397 asic_nr and heatmap for hashrate registers by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1397
* Fix statistics logging period by @terratec in https://github.com/bitaxeorg/ESP-Miner/pull/1351
* Add timeout to GET requests by @duckaxe in https://github.com/bitaxeorg/ESP-Miner/pull/1396
* Don't fail SYSTEM_init_peripherals on invalid VCORE value by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1389
* Prevent precision artifacts with floats in REST API by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1364
* Self-test should pass when power is below target by @WantClue in https://github.com/bitaxeorg/ESP-Miner/pull/1415

**Full Changelog**: https://github.com/bitaxeorg/ESP-Miner/compare/v2.11.0...v2.12.0

## v2.11.0 (v2.11.0)

- Published: 2025-11-15
- Link: https://github.com/bitaxeorg/ESP-Miner/releases/tag/v2.11.0
- Prerelease: False

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

## v2.10.1 (v2.10.1)

- Published: 2025-10-28
- Link: https://github.com/bitaxeorg/ESP-Miner/releases/tag/v2.10.1
- Prerelease: False

## What's Changed

* Self test check external temp by @benjamin-wilson in https://github.com/bitaxeorg/ESP-Miner/pull/1300
* Fix ic2 errors when using tps546d24s instead of tps546d24a by @benjamin-wilson in https://github.com/bitaxeorg/ESP-Miner/pull/1293
* fix self test fail for non-factory test by @benjamin-wilson

**Full Changelog**: https://github.com/bitaxeorg/ESP-Miner/compare/v2.10.0...v2.10.1

## v2.10.0 (v2.10.0)

- Published: 2025-09-04
- Link: https://github.com/bitaxeorg/ESP-Miner/releases/tag/v2.10.0
- Prerelease: False

## What's Changed

## AxeOS New Features
* Add Pool Difficulty to Dashboard by @duckaxe in https://github.com/bitaxeorg/ESP-Miner/pull/1170
* Configure min fan speed percentage by @0xf0xx0 in https://github.com/bitaxeorg/ESP-Miner/pull/1059
* Add Privacy Warning to Release Check by @duckaxe in https://github.com/bitaxeorg/ESP-Miner/pull/1042
* Show/Hide pool advanced options by @duckaxe in https://github.com/bitaxeorg/ESP-Miner/pull/1149
* Introduction wifi-icon component by @duckaxe in https://github.com/bitaxeorg/ESP-Miner/pull/1092
* Handle multiple websocket connections by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1110
* Improved formatting of release notes by @duckaxe in https://github.com/bitaxeorg/ESP-Miner/pull/1114
* Increased contrast ratio for purple by @duckaxe in https://github.com/bitaxeorg/ESP-Miner/pull/1072
* Improve PLL calculation for BM1366/BM1368/BM1370 (floating point frequency) by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1051

## Stratum Improvements
* Extranonce 2 variable length by @skot in https://github.com/bitaxeorg/ESP-Miner/pull/1168
* Fix last parsed request id not being updated by @eandersson in https://github.com/bitaxeorg/ESP-Miner/pull/1125
* Extranonce cleanup by @WantClue in https://github.com/bitaxeorg/ESP-Miner/pull/1192

## Hardware and Display Enhancements
* Bitaxe accessory port by @WantClue in https://github.com/bitaxeorg/ESP-Miner/pull/1178
* feat: test both temps gt by @WantClue in https://github.com/bitaxeorg/ESP-Miner/pull/1172
* Add shares accepted, rejected and work received notification to screen by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1209

## Documentation
* Add tooltips for suggest difficulty and extranonce subscribe pool fields by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1134
* Update Readme API section by @duckaxe in https://github.com/bitaxeorg/ESP-Miner/pull/1147

## Bug Fixes
* FUP #1103: Fix sorting for undefined poolDifficulty by @duckaxe in https://github.com/bitaxeorg/ESP-Miner/pull/1107
* Fix strncpy buffer overflow warning in WiFi configuration by @ahmedalalousi in https://github.com/bitaxeorg/ESP-Miner/pull/1106
* Quicklink service: Fix JS error when using local pool by @duckaxe in https://github.com/bitaxeorg/ESP-Miner/pull/1193
* Fix JS error when opening/closing the menu by @duckaxe in https://github.com/bitaxeorg/ESP-Miner/pull/1190
* Bap fix by @WantClue in https://github.com/bitaxeorg/ESP-Miner/pull/1211
* Block found screen sometimes doesn't show by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1213
* Fix Header fields are too long error by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1216

## Code Quality
* Common difficulty mask function by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1102
* Clean up quick links by @duckaxe in https://github.com/bitaxeorg/ESP-Miner/pull/1101
* Refactored network component by @duckaxe in https://github.com/bitaxeorg/ESP-Miner/pull/1083
* Remove unused PrimeNG icons by @duckaxe in https://github.com/bitaxeorg/ESP-Miner/pull/1038
* Uniform notifications design by @duckaxe in https://github.com/bitaxeorg/ESP-Miner/pull/1075
* Refactored edit component by @duckaxe in https://github.com/bitaxeorg/ESP-Miner/pull/1062
* Refactored system component by @duckaxe in https://github.com/bitaxeorg/ESP-Miner/pull/1104
* Refactored quicklink service by @duckaxe in https://github.com/bitaxeorg/ESP-Miner/pull/1143
* Auto refresh current version @ update view by @duckaxe in https://github.com/bitaxeorg/ESP-Miner/pull/1111
* Consistent spelling by @duckaxe in https://github.com/bitaxeorg/ESP-Miner/pull/1151
* Remove GZIP handling for WOFF2 files by @duckaxe in https://github.com/bitaxeorg/ESP-Miner/pull/1161
* Add memory leak protection to home.component by @duckaxe in https://github.com/bitaxeorg/ESP-Miner/pull/1191
* Fix statistics deactivation without restart by @terratec in https://github.com/bitaxeorg/ESP-Miner/pull/1162
* Fix form labels by @duckaxe in https://github.com/bitaxeorg/ESP-Miner/pull/1196

## Build system
* Add workflow for building and publishing our devcontainer by @johnny9 in https://github.com/bitaxeorg/ESP-Miner/pull/1108
* Upgrade from idf 5.4.1 to 5.4.2 by @eandersson in https://github.com/bitaxeorg/ESP-Miner/pull/1116
* Minor NPM package updates by @eandersson in https://github.com/bitaxeorg/ESP-Miner/pull/1117
* Remove fallback code for 7xx board versions by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1126
* Split unittest workflow up it can work with pull requests by @johnny9 in https://github.com/bitaxeorg/ESP-Miner/pull/1113
* Introduce dockerbuild.py by @johnny9 in https://github.com/bitaxeorg/ESP-Miner/pull/1120
* fix: bump up idf 5.5 by @WantClue in https://github.com/bitaxeorg/ESP-Miner/pull/1163
* Generate sdkconfig.defaults by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1004
* Require at least IDF 5.5 by @eandersson in https://github.com/bitaxeorg/ESP-Miner/pull/1201

## New Contributors
* @ahmedalalousi made their first contribution in https://github.com/bitaxeorg/ESP-Miner/pull/1106

**Full Changelog**: https://github.com/bitaxeorg/ESP-Miner/compare/v2.9.0...v2.10.0

## v2.9.0 (v2.9.0)

- Published: 2025-07-01
- Link: https://github.com/bitaxeorg/ESP-Miner/releases/tag/v2.9.0
- Prerelease: False

## AxeOS New Features
* Add clear button and filter for realtime logs by @terratec in https://github.com/bitaxeorg/ESP-Miner/pull/884
* Add sorting to all swarm table columns by @duckAxe in https://github.com/bitaxeorg/ESP-Miner/pull/948
* Add browser tab title by @duckAxe in https://github.com/bitaxeorg/ESP-Miner/pull/996
* Add release notes by @duckAxe in https://github.com/bitaxeorg/ESP-Miner/pull/1005
* Add AxeOS version and mismatched version warning by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1006
* One statistics slider by @terratec in https://github.com/bitaxeorg/ESP-Miner/pull/1016
* Rethinking Navigation by @duckAxe in https://github.com/bitaxeorg/ESP-Miner/pull/1026
* Refresh Logs Page by @duckAxe in https://github.com/bitaxeorg/ESP-Miner/pull/1049
* Hostname & WiFi RSSI at header/menu by @duckAxe in https://github.com/bitaxeorg/ESP-Miner/pull/1056
* Add stratum response time by @WantClue in https://github.com/bitaxeorg/ESP-Miner/pull/1063
* Improved update notifications by @duckAxe in https://github.com/bitaxeorg/ESP-Miner/pull/1060
* Introduction Loading Animation by @duckAxe in https://github.com/bitaxeorg/ESP-Miner/pull/1066
* Pool difficulty column on swarm by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1103

## API Improvements
* Add board family to API by @0xf0xx0 in https://github.com/bitaxeorg/ESP-Miner/pull/966
* API returns a JSON error for unhandled requests by @0xf0xx0 in https://github.com/bitaxeorg/ESP-Miner/pull/972
* Add fallback code for deviceModel and swarmColor by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1097

## Stratum Improvements
* Send mining.suggest_difficulty after authorization by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/913
* Add Parasite pool to Pool Quick Links by @jemekite in https://github.com/bitaxeorg/ESP-Miner/pull/956
* Extranonce subscribe and suggested difficulty pool options by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1064
* Add new config fields for #1064 by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1082

## Hardware and Display Enhancements
* Share submit notification dot on display by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/975
* Custom board config by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1018
* Add signal strength indicator to screen by @WantClue in https://github.com/bitaxeorg/ESP-Miner/pull/1019
* SH1107 (64x128) display support completed by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1022
* Simplify Wi-Fi screen by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1030
* Fixing TPS546D24 phase register default value by @powerminingfarm in https://github.com/bitaxeorg/ESP-Miner/pull/1032
* Improve vcore read timeout handling by @KillerInk in https://github.com/bitaxeorg/ESP-Miner/pull/1035

## Documentation
* Fix duplicated help messages in Kconfig.projbuild by @Nexus9090 in https://github.com/bitaxeorg/ESP-Miner/pull/984
* Update readme.md by @WantClue in https://github.com/bitaxeorg/ESP-Miner/pull/1013
* Update API examples in docs and clean up swarm endpoint by @0xf0xx0 in https://github.com/bitaxeorg/ESP-Miner/pull/1055
* Update readme.md by @WantClue in https://github.com/bitaxeorg/ESP-Miner/pull/1088

## Bug Fixes
* Fix chart tooltip reset on every data change by @KillerInk in https://github.com/bitaxeorg/ESP-Miner/pull/951
* Improve Logs Fullscreen by @duckAxe in https://github.com/bitaxeorg/ESP-Miner/pull/1000
* Fix memory leak in info api by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1009
* LVGL upstream bug by @WantClue in https://github.com/bitaxeorg/ESP-Miner/pull/1020
* Wait after socket creation by @KillerInk in https://github.com/bitaxeorg/ESP-Miner/pull/1023
* Fix Angular build warnings by @duckAxe in https://github.com/bitaxeorg/ESP-Miner/pull/1027
* fix: process dirs recursively by @WantClue in https://github.com/bitaxeorg/ESP-Miner/pull/1046
* Fixed label icon wrap @ pool page by @duckAxe in https://github.com/bitaxeorg/ESP-Miner/pull/1074
* fix: styling and naming of time response by @WantClue in https://github.com/bitaxeorg/ESP-Miner/pull/1077
* Swarm scan shouldn't emit errors by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1080
* Swarm should handle devices without asic endpoint by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1089
* Fix swarm edit and restart by @WantClue in https://github.com/bitaxeorg/ESP-Miner/pull/1095
* Fix settings page by @WantClue in https://github.com/bitaxeorg/ESP-Miner/pull/1096

## AxeOS Code Quality and Refactorings
* Refactoring Power & Heat cards by @duckAxe in https://github.com/bitaxeorg/ESP-Miner/pull/982
* Uniform icon only buttons by @duckAxe in https://github.com/bitaxeorg/ESP-Miner/pull/983
* Introduction Modal Component by @duckAxe in https://github.com/bitaxeorg/ESP-Miner/pull/1014
* FUP #1005: Use Modal Component for Release Notes by @duckAxe in https://github.com/bitaxeorg/ESP-Miner/pull/1041
* Refactored settings component by @duckAxe in https://github.com/bitaxeorg/ESP-Miner/pull/1050
* Header SVG logo by @duckAxe in https://github.com/bitaxeorg/ESP-Miner/pull/1058
* Fix SVG Content-Type by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1065
* Fix selected accent color after page reload by @duckAxe in https://github.com/bitaxeorg/ESP-Miner/pull/1073
* Embed AxeOS logo as inline SVG by @duckAxe in https://github.com/bitaxeorg/ESP-Miner/pull/1084
* Fixed logo outline by @duckAxe in https://github.com/bitaxeorg/ESP-Miner/pull/1091

## Code Quality and Refactoring
* Set FreeRTOS frequency to 1000Hz and enable bootloader compiler optimization by @fromport in https://github.com/bitaxeorg/ESP-Miner/pull/954
* Clean up duplicate ASIC reset code by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/986
* Uniform logging tags by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/977
* Init ASIC frequency in power_management_task by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/978
* Self_test check and Wi-Fi code moved to modules by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/979
* Add Ultra 207 support by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/992
* Remove duplicate fonts on production build by @duckAxe in https://github.com/bitaxeorg/ESP-Miner/pull/1010
* Optimised Fonts by @duckAxe in https://github.com/bitaxeorg/ESP-Miner/pull/1012
* Minor update to NPM packages by @eandersson in https://github.com/bitaxeorg/ESP-Miner/pull/1021
* Remove ASIC specific code from AxeOS by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1029
* Remove Knob Module by @duckAxe in https://github.com/bitaxeorg/ESP-Miner/pull/1033
* Improve status messages on self-test finish by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1086

## API Changes
 - `apy/system/info`:
   - `stratumDiff` renamed to `poolDifficulty`
   - `flipScreen(0/1)` replaced by `rotation(0/90/180/270)`
   - `asicCount` moved to `api/system/asic`
 - `api/system/asic`: 
   - `deviceModel`, `swarmColor` and `asicCount` added

## New Contributors
* @KillerInk made their first contribution in https://github.com/bitaxeorg/ESP-Miner/pull/951
* @jemekite made their first contribution in https://github.com/bitaxeorg/ESP-Miner/pull/956
* @Nexus9090 made their first contribution in https://github.com/bitaxeorg/ESP-Miner/pull/984
* @powerminingfarm made their first contribution in https://github.com/bitaxeorg/ESP-Miner/pull/1032

**Full Changelog**: https://github.com/bitaxeorg/ESP-Miner/compare/v2.8.1...v2.9.0

## v2.8.1 (v2.8.1)

- Published: 2025-06-06
- Link: https://github.com/bitaxeorg/ESP-Miner/releases/tag/v2.8.1
- Prerelease: False

## Bug Fixes
-Fix memory leak in info api #1009 by @mutatrum 

**Full Changelog**: https://github.com/bitaxeorg/ESP-Miner/compare/v2.8.0...v2.8.1


## v2.8.0 (v2.8.0)

- Published: 2025-05-30
- Link: https://github.com/bitaxeorg/ESP-Miner/releases/tag/v2.8.0
- Prerelease: False

## API Enhancements
- Added expected hashrate to API by @jpcomps in #603
- Dashboard: Get expected hash rate from API by @duckAxe in #943

## UI/UX Improvements
- Move restart warning to Toast by @duckAxe in #926
- Show restart warning only for relevant fields by @duckAxe in #967
- Add amount of active devices to the swarm page by @duckAxe in #930
- Fix swarm sorting by @duckAxe in #928
- Remember menu toggle state by @duckAxe in #929
- Feature: Expand Logs by @duckAxe in #919
- Add Wi-Fi RSSI to the Logs Overview by @duckAxe in #922
- Display Timeout Slider by @duckAxe in #942
- Message update with ref to new firmware release by @STSMiner1 in #910
- Pools Visual Separation by @duckAxe in #923
- Fixed Pool Card Overflow by @duckAxe in #920
- Add Project Favicon by @duckAxe in #924
- Add Braiins Solo Pool to Pool Quick Links by @duckAxe in #946

## Bug Fixes
- Fix stratum parse if there's no error field by @mutatrum in #917
- Fix scientific notation in best session diff by @mutatrum in #906
- Fix broken text scroll animation for self test by @terratec in #931
- Fix: adjust the diff string to .2 by @WantClue in #952
- Fix: match hashrate y-axis tick colors to line by @mrv777 in #887
- Fix self test power consumption target for 402/403 by @mutatrum in #973
- Self test fixes by @mutatrum in #961
- power_consumption_target fix introduced in #346 by @benjamin-wilson 

## Hardware and Display Enhancements
- Add support for multiple displays by @mutatrum in #934
- SH1107 improvements, incomplete by @mutatrum in #938
- Ssd1309 extra screen by @WantClue in #937
- Pid improvements by @WantClue in #947
- emc2101-fix and emc2103 by @WantClue in #875
- Fix: change back display conf to v_res by @WantClue in #958
- Fix: adds the GT offset by @WantClue in #962
- Fix: remove external offset by @WantClue in #965
- EMC temperature offsets should be in device_config.h by @mutatrum in #968

## Performance and Compilation
- feat: add -O2 compiling by @WantClue in #953
- Updated version of CrC calculations by Mecanix by @fromport in #933

## Statistics and Data
- Statistics task for previous chart data by @terratec in #898

## Code Quality and Refactoring
- Device model cleanup by @mutatrum in #857
- Clean up NVS Wi-Fi credentials code by @mutatrum in #859
- Simplify swarm best diff compare by @mutatrum in #907
- .editorconfig: Add indent size for SCSS & HTML files by @duckAxe in #935
- Refactor font embedding by @duckAxe in #918
- Avoid duplicate code @ edit.component.ts by @duckAxe in #964
- Removal of unnecessary code @ edit.component.ts by @duckAxe in #963
- Fix inconsistent function naming @ edit.component.ts by @duckAxe in #969
- FUP #603: Add missing declarations by @duckAxe in #932

## New Contributors
- @jpcomps made their first contribution in #603
- @duckAxe made their first contribution in #923
- @STSMiner1 made their first contribution in #910
- @fromport made their first contribution in #933

**Full Changelog**: [v2.7.2...v2.8.0](https://github.com/bitaxeorg/ESP-Miner/compare/v2.7.2...v2.8.0)

## v2.7.2 (v2.7.2)

- Published: 2025-05-28
- Link: https://github.com/bitaxeorg/ESP-Miner/releases/tag/v2.7.2
- Prerelease: False

Hotfix for 402, 403
Fixes self test power consumption failure introduced in https://github.com/bitaxeorg/ESP-Miner/pull/346 by going from 8w target (+-3) to 5w.

**Full Changelog**: https://github.com/bitaxeorg/ESP-Miner/compare/v2.7.1...v2.7.2

## v2.7.1 (v2.7.1)

- Published: 2025-05-05
- Link: https://github.com/bitaxeorg/ESP-Miner/releases/tag/v2.7.1
- Prerelease: False

Hotfix Fan Controller.

This changes the minimum fan speed for the PID to 25% as well as ensure the fan is running in the AP mode at 70% to prevent heat buildup.

## What's Changed
* hotfix fan controller, increase minimum and add ap mode fan speed by @WantClue in https://github.com/bitaxeorg/ESP-Miner/pull/896


**Full Changelog**: https://github.com/bitaxeorg/ESP-Miner/compare/v2.7.0...v2.7.1

## v2.7.0 (v2.7.0)

- Published: 2025-05-02
- Link: https://github.com/bitaxeorg/ESP-Miner/releases/tag/v2.7.0
- Prerelease: False

## What's Changed
* Improve AP mode stability by stopping unnecessary Wi-Fi reconnections by @eandersson in https://github.com/bitaxeorg/ESP-Miner/pull/815
* Fix stratumPort max limit verification by @terratec in https://github.com/bitaxeorg/ESP-Miner/pull/795
* PID Fan Control by @WantClue in https://github.com/bitaxeorg/ESP-Miner/pull/800
* Move to ESP IDF 5.4.1 by @eandersson in https://github.com/bitaxeorg/ESP-Miner/pull/809
* Handle all Wi-Fi error messages by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/819
* Fix Connected! display on screen by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/827
* Self-test display cleanup by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/828
* Add OSMU logo by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/825
* Pid controller fix by @WantClue in https://github.com/bitaxeorg/ESP-Miner/pull/831
* quicklink service init by @WantClue in https://github.com/bitaxeorg/ESP-Miner/pull/830
* Remove under power failure by @benjamin-wilson in https://github.com/bitaxeorg/ESP-Miner/pull/837
* fix: remove polarity bit by @WantClue in https://github.com/bitaxeorg/ESP-Miner/pull/848
* fix: spelling error fix by @WantClue in https://github.com/bitaxeorg/ESP-Miner/pull/849
* Make "Latest Release" into a link for the changelog by @kukovecz in https://github.com/bitaxeorg/ESP-Miner/pull/835
* fix: pid finetune, adjusting the settings by @WantClue in https://github.com/bitaxeorg/ESP-Miner/pull/852
* re-order code in _check_for_best_diff() method in system.c file to prevent missing block found notification by @aaron3481 in https://github.com/bitaxeorg/ESP-Miner/pull/858
* Screensaver timeout by @terratec in https://github.com/bitaxeorg/ESP-Miner/pull/525
* Share reject reasons tooltips by @GIGIG4 in https://github.com/bitaxeorg/ESP-Miner/pull/847
* fix: add stratumUser split by @WantClue in https://github.com/bitaxeorg/ESP-Miner/pull/860
* Simplify share rejection explanations by @GIGIG4 in https://github.com/bitaxeorg/ESP-Miner/pull/861
* Update gitignore, simplify layout, fix refresh button UI, unify headlines/margins, improve modal responsiveness and theme color selection by @ciruz in https://github.com/bitaxeorg/ESP-Miner/pull/834
* Initial page load causes multiple inconsistent GET responses by @AxisRay in https://github.com/bitaxeorg/ESP-Miner/pull/854
* Fix automatic display on by @terratec in https://github.com/bitaxeorg/ESP-Miner/pull/864
* Track rejection reasons to avoid flickering by @GIGIG4 in https://github.com/bitaxeorg/ESP-Miner/pull/863
* GT Fan polarity fix by @skot in https://github.com/bitaxeorg/ESP-Miner/pull/866
* set GAMMATURBO_POWER_OFFSET to 10W by @skot in https://github.com/bitaxeorg/ESP-Miner/pull/867
* Api rework asic by @WantClue in https://github.com/bitaxeorg/ESP-Miner/pull/862
* Fix increased power reported on bitaxeGamma by @skot in https://github.com/bitaxeorg/ESP-Miner/pull/873
* Updating npm libraries by @eandersson in https://github.com/bitaxeorg/ESP-Miner/pull/871
* add default to supra model by @WantClue in https://github.com/bitaxeorg/ESP-Miner/pull/876
* Use latest LTS release of Node by @eandersson in https://github.com/bitaxeorg/ESP-Miner/pull/877
* fix: change default value of max model by @WantClue in https://github.com/bitaxeorg/ESP-Miner/pull/882

## New Contributors
* @kukovecz made their first contribution in https://github.com/bitaxeorg/ESP-Miner/pull/835
* @aaron3481 made their first contribution in https://github.com/bitaxeorg/ESP-Miner/pull/858
* @GIGIG4 made their first contribution in https://github.com/bitaxeorg/ESP-Miner/pull/847
* @ciruz made their first contribution in https://github.com/bitaxeorg/ESP-Miner/pull/834
* @AxisRay made their first contribution in https://github.com/bitaxeorg/ESP-Miner/pull/854

**Full Changelog**: https://github.com/bitaxeorg/ESP-Miner/compare/v2.6.5...v2.7.0

## v2.6.5 (v2.6.5)

- Published: 2025-04-15
- Link: https://github.com/bitaxeorg/ESP-Miner/releases/tag/v2.6.5
- Prerelease: False

**Full Changelog**: https://github.com/bitaxeorg/ESP-Miner/compare/v2.6.4...v2.6.5

Increase power target for gamma self test

## v2.6.4 (v2.6.4)

- Published: 2025-04-15
- Link: https://github.com/bitaxeorg/ESP-Miner/releases/tag/v2.6.4
- Prerelease: False

Remove under limits for power consumption self test

## What's Changed
* chore: update openapi spec by @0xf0xx0 in https://github.com/bitaxeorg/ESP-Miner/pull/806

## New Contributors
* @0xf0xx0 made their first contribution in https://github.com/bitaxeorg/ESP-Miner/pull/806

**Full Changelog**: https://github.com/bitaxeorg/ESP-Miner/compare/v2.6.3...v2.6.4

## v2.6.1 (v2.6.1)

- Published: 2025-03-31
- Link: https://github.com/bitaxeorg/ESP-Miner/releases/tag/v2.6.1
- Prerelease: False

## What's Changed

### Wi-Fi
- **New Features**:  
  - **Grandma knows what Wifi means!** by @b-rowan (#623)
  - **SSID WiFi lookup** by @WantClue (#679)
  - **Expose Wifi RSSI to API endpoint** by @eandersson (#739)
  - **Trim spaces from SSID** by @w3irdrobot (#728)
  - **Init AxeOS AP mode** by @dustinb (#624)
  - **Don't allow 0.0.0.0 in CORS** by @eandersson (#665)
- **Bugfixes**:  
  - **Adjust wifi setup text speed** by @WantClue (#682)
  - **Wifi scan fix** by @WantClue (#690)
  - **Fix Wi-Fi spelling** by @mutatrum (#684)
  - **More Wi-Fi spelling fixes** by @mutatrum (#685)

### User Interface (UI) / Display
- **New Features**:  
  - **Menu rework, adding menu Design** by @WantClue (#675)
  - **Pool rework menu** by @WantClue (#676)
  - **feat: add tooltip for pwm invert and flip screen** by @WantClue (#709)
  - **Show firmware updates on the display** by @mutatrum (#664)
  - **add sorting switch to swarm page for hostname and ip** by @w3irdrobot (#733)
  - **Show share reject reasons** by @mutatrum (#746)
  - **Add asic failure status screen** by @mutatrum (#777)
  - **Max power gauges** by @WantClue (#793)
  - **Swap update www and esp-miner** by @WantClue (#771)
- **Bugfixes**:  
  - **Add mock data and cache to theme service** by @mrv777 (#654)
  - **Color swarm ips by model or count** by @mrv777 (#647)
  - **Show IP of bitaxe you are restarting on swarm** by @mrv777 (#646)
  - **Display placeholder for unavailable ASIC temp** by @steven-s-martins (#692) 
  - **Don't show -1 temperature on screen** by @mutatrum (#703)
  - **Move avg hash to card & add eff avg** by @mrv777 (#643)
  - **Typo in home.component.html** by @diegorodriguezv (#797)

### Mining / Pool / Stratum
- **New Features**:  
  - **Keep old pool config synchronized until reboot** by @terratec (#543)  
  - **Add support for extranonce2_len<4** by @adammwest (#660)  
  - **Improved pool fallback code** by @eandersson (#693)  
  - **Updated confusing connect to pool log message** by @eandersson (#697)  
  - **Refactor Stratum code for Seamless Failover** by @eandersson (#717) *(reverted in #754)*  
- **Bugfixes**:  
  - **Submit shares that are exactly equal to the target when rounded to a "diff"** by @luke-jr (#687)  
  - **Reduce invalid job found log from error to warning** by @eandersson (#480)  

### Hardware / Power / Overclocking
- **New Features**:  
  - **Use url params to unlock overclock** by @mrv777 (#729)  
  - **Unlock OC** by @WantClue (#714)  
  - **Overclock url params** by @WantClue (#770)  
  - **GammaTurbo support and HW abstraction** by @skot (#698)  
  - **Create TPS546 VCORE alerts** by @skot (#780)  
  - **Get combined current (power) for multi-phase TPS546** by @skot (#796)  
  - **Frequency transition** by @WantClue (#747)  
  - **Verify CHIP_ID response** by @mutatrum (#745)  
- **Bugfixes**:  
  - **Don't collect hashrate while in power_fault** by @WantClue (#804)  

### API / Backend
- **New Features**:  
  - **add openapi spec for existing api** by @w3irdrobot (#736)  
- **Bugfixes**:  
  - **fix: current not exposed to api** by @WantClue (#749)  
  - **Improve null handling in API settings PATCH** by @w3irdrobot (#748)  

### Development / Build / Testing
- **New Features**:  
  - **Enable Unit Test CI** by @eandersson (#634)  
  - **Update angular to 18** by @eandersson (#678)  
  - **Added nodejs and npm v22 installation** by @mapio (#763)  
- **Bugfixes**:  
  - **Remove unit test workaround for qemu** by @eandersson (#743)  
  - **Fix stackoverflow when upgrading #674** by @eandersson (#723)  
  - **V2.6.0b11 selftest fixes** by @skot (#783)  
  - **Ensure timeout in self test** by @adammwest (#769)  
  - **Added test_vreg_faults() to selftest** by @skot (#789)  

### Configuration / System
- **New Features**:  
  - **Is SPIRAM Available?** by @eandersson (#626)  
  - **Restore Max support** by @eandersson (#705)  
- **Bugfixes**:  
  - **Disable softap even if we don’t have a valid model** by @eandersson (#706)  

### Documentation / Miscellaneous
- **New Features**:  
  - **Ports over everything to bitaxeorg** by @WantClue (#774)  
  - **Add whitepaper** by @mutatrum (#735)
  - **feat: update readme** by @WantClue (#720)  
- **Bugfixes**:  
  - **Typo in .filter** by @WantClue (#724)  

### Fan Control
- **Bugfixes**:  
  - **Changed 'Invert Fan Polarity' text** by @JasonB1833 (#779)

## New Contributors
* @terratec made their first contribution in https://github.com/bitaxeorg/ESP-Miner/pull/543
* @luke-jr made their first contribution in https://github.com/bitaxeorg/ESP-Miner/pull/687
* @steven-s-martins made their first contribution in https://github.com/bitaxeorg/ESP-Miner/pull/692
* @dustinb made their first contribution in https://github.com/bitaxeorg/ESP-Miner/pull/624
* @w3irdrobot made their first contribution in https://github.com/bitaxeorg/ESP-Miner/pull/728
* @JasonB1833 made their first contribution in https://github.com/bitaxeorg/ESP-Miner/pull/779
* @diegorodriguezv made their first contribution in https://github.com/bitaxeorg/ESP-Miner/pull/797
* @mapio made their first contribution in https://github.com/bitaxeorg/ESP-Miner/pull/763

**Full Changelog**: https://github.com/bitaxeorg/ESP-Miner/compare/v2.5.1...v2.6.1

## v2.5.1 (v2.5.1)

- Published: 2025-01-20
- Link: https://github.com/bitaxeorg/ESP-Miner/releases/tag/v2.5.1
- Prerelease: False

## What's Changed
* Tiny header define cleanup by @mutatrum in https://github.com/skot/ESP-Miner/pull/535
* allow-cors-in-ap-mode by @benjamin-wilson in https://github.com/skot/ESP-Miner/pull/659
* fix: selftest button functionality by @benjamin-wilson in https://github.com/skot/ESP-Miner/pull/653
* Clean up CORS implemention by @eandersson in https://github.com/skot/ESP-Miner/pull/662
* Require at least IDF 5.4.0 by @eandersson in https://github.com/skot/ESP-Miner/pull/666


**Full Changelog**: https://github.com/skot/ESP-Miner/compare/v2.5.0...v2.5.1

## v2.5.0 (v2.5.0)

- Published: 2025-01-15
- Link: https://github.com/bitaxeorg/ESP-Miner/releases/tag/v2.5.0
- Prerelease: False

This update has a critical fix for a CSRF vulnerability. It is reccommended all Bitaxe users update as soon as possible!

Note: You will no longer be able to access AxeOS by hostname, you must use the Bitaxe IP. (ex: `http://192.168.1.21`)

## What's Changed
* typo: small typo fix by @b-rowan in https://github.com/skot/ESP-Miner/pull/629
* check psram on self test by @WantClue in https://github.com/skot/ESP-Miner/pull/628
* test: fix stratum alternative error unit test by @tdb3 in https://github.com/skot/ESP-Miner/pull/608
* fix: Use this.uri for edit restart by @mrv777 in https://github.com/skot/ESP-Miner/pull/642
* Add instructions for development by @pRizz in https://github.com/skot/ESP-Miner/pull/641
* CSRF vulnerability patch by @benjamin-wilson in https://github.com/skot/ESP-Miner/pull/637
  * Huge thanks to @shaunography for discovering and reporting this issue.


**Full Changelog**: https://github.com/skot/ESP-Miner/compare/v2.4.5...v2.5.0

## v2.4.5 (v2.4.5)

- Published: 2025-01-07
- Link: https://github.com/bitaxeorg/ESP-Miner/releases/tag/v2.4.5
- Prerelease: False

## CRITICAL FIX on devices without PSRAM module
## What's Changed
* Allow device to start without SPIRAM by @eandersson in https://github.com/skot/ESP-Miner/pull/625


**Full Changelog**: https://github.com/skot/ESP-Miner/compare/v2.4.4...v2.4.5

## v2.4.4 (v2.4.4)

- Published: 2025-01-05
- Link: https://github.com/bitaxeorg/ESP-Miner/releases/tag/v2.4.4
- Prerelease: False

## What's Changed
(Mostly manufacturer QoL)
* Continue automatically if self tests pass by @benjamin-wilson in https://github.com/skot/ESP-Miner/pull/616
* Press reset then hold boot for self test by @benjamin-wilson in https://github.com/skot/ESP-Miner/pull/617


**Full Changelog**: https://github.com/skot/ESP-Miner/compare/v2.4.3...v2.4.4

## v2.4.3 (v2.4.3)

- Published: 2025-01-05
- Link: https://github.com/bitaxeorg/ESP-Miner/releases/tag/v2.4.3
- Prerelease: False

## What's Changed
* Enable PSRAM by @mutatrum in https://github.com/skot/ESP-Miner/pull/468
* Updated node and npm packages by @eandersson in https://github.com/skot/ESP-Miner/pull/590
* Revert "Enable PSRAM (#468)" by @WantClue in https://github.com/skot/ESP-Miner/pull/594
* Enable SPIRAM and use it for specific tasks by @eandersson in https://github.com/skot/ESP-Miner/pull/597
* UI themes by @WantClue in https://github.com/skot/ESP-Miner/pull/600
* Streamline create_jobs_task by @eandersson in https://github.com/skot/ESP-Miner/pull/478
* Configure GPIO in Kconfig by @mutatrum in https://github.com/skot/ESP-Miner/pull/566
* fix: Show warning if freq is low or not set by @mrv777 in https://github.com/skot/ESP-Miner/pull/576
* Move to ESP-IDF 5.4 by @eandersson in https://github.com/skot/ESP-Miner/pull/609
* Revert "Enable SPIRAM and use it for specific tasks (#597)" by @eandersson in https://github.com/skot/ESP-Miner/pull/610
* Enable PSRAM again by @WantClue in https://github.com/skot/ESP-Miner/pull/611
* test: fix failing unit test for large stratum id by @tdb3 in https://github.com/skot/ESP-Miner/pull/546
* test: add boundary check for implicit response method by @tdb3 in https://github.com/skot/ESP-Miner/pull/548
* Improve i2c error logging by @mutatrum in https://github.com/skot/ESP-Miner/pull/552
* Fix logs not rendering properly in AxeOS by @eandersson in https://github.com/skot/ESP-Miner/pull/612
* Add ESP-IDF version to overview by @eandersson in https://github.com/skot/ESP-Miner/pull/604


**Full Changelog**: https://github.com/skot/ESP-Miner/compare/v2.4.2...v2.4.3

## v2.4.2 (v2.4.2)

- Published: 2024-12-16
- Link: https://github.com/bitaxeorg/ESP-Miner/releases/tag/v2.4.2
- Prerelease: False

## What's Changed
* Add uptime to home screen by @mutatrum in https://github.com/skot/ESP-Miner/pull/425
* doc: add initial unit test guide by @tdb3 in https://github.com/skot/ESP-Miner/pull/549
* Reenable self test, add 201/3, update CI by @WantClue in https://github.com/skot/ESP-Miner/pull/553
* change naming of stratum url to host by @WantClue in https://github.com/skot/ESP-Miner/pull/561
* Change Stratum Fallback URL as well by @WantClue in https://github.com/skot/ESP-Miner/pull/562
* Parse stratum api reject reason by @mutatrum in https://github.com/skot/ESP-Miner/pull/472
* Fix npm package warnings by @eandersson in https://github.com/skot/ESP-Miner/pull/556
* Remove recovery actions by @eandersson in https://github.com/skot/ESP-Miner/pull/554
* fix: Swarm hashRate check, shorter uptime, & pause refresh on scan by @mrv777 in https://github.com/skot/ESP-Miner/pull/560
* Use latest stable esp idf 5.3.2 release by @eandersson in https://github.com/skot/ESP-Miner/pull/555
* LVGL All The Things! by @mutatrum in https://github.com/skot/ESP-Miner/pull/539
* Adds solohash getQuickLink() by @robwoodgate in https://github.com/skot/ESP-Miner/pull/569
* Improve HTTP and System Stability by @eandersson in https://github.com/skot/ESP-Miner/pull/571
* Fix lvgl without display by @mutatrum in https://github.com/skot/ESP-Miner/pull/574
* Change Mining URL to Stratum Host on screen by @mutatrum in https://github.com/skot/ESP-Miner/pull/577
* fix: Show custom values in dropdown if set by @mrv777 in https://github.com/skot/ESP-Miner/pull/578
* Toggle auto_fan_speed without reboot by @mutatrum in https://github.com/skot/ESP-Miner/pull/580

## New Contributors
* @robwoodgate made their first contribution in https://github.com/skot/ESP-Miner/pull/569

**Full Changelog**: https://github.com/skot/ESP-Miner/compare/v2.4.1...v2.4.2

## v2.4.1 (v2.4.1)

- Published: 2024-12-02
- Link: https://github.com/bitaxeorg/ESP-Miner/releases/tag/v2.4.1
- Prerelease: False

## What's Changed
* Don't abandon the first mining.notify by @eandersson in https://github.com/skot/ESP-Miner/pull/492
* add 205 config and remove self test flag  by @WantClue in https://github.com/skot/ESP-Miner/pull/502
* Fix bug when setting baudrate that can prevent the ASIC from working by @eandersson in https://github.com/skot/ESP-Miner/pull/503
* Fix stratum message order by @mutatrum in https://github.com/skot/ESP-Miner/pull/498
* Add link for pool.satoshiradio.nl by @WRKampi in https://github.com/skot/ESP-Miner/pull/501
* fix: Add restart to settings & better disabled state by @mrv777 in https://github.com/skot/ESP-Miner/pull/493
* Swarm styles, refresh on load, more combined stats, more info in table by @mrv777 in https://github.com/skot/ESP-Miner/pull/491
* Add Noderunners pool to quick links by @PMK in https://github.com/skot/ESP-Miner/pull/490
* api: add stratum difficulty by @tdb3 in https://github.com/skot/ESP-Miner/pull/489
* doc: update readme to mention recovery page by @tdb3 in https://github.com/skot/ESP-Miner/pull/474
* fix: update feedback & reset file input by @mrv777 in https://github.com/skot/ESP-Miner/pull/521
* chore: clean up network component by @mrv777 in https://github.com/skot/ESP-Miner/pull/504
* Set proper size in hex2bin call by @mutatrum in https://github.com/skot/ESP-Miner/pull/471
* fix: correct json_rpc_buffer initialization order by @tdb3 in https://github.com/skot/ESP-Miner/pull/473
* Fix setting overheat mode flag on device Max by @mutatrum in https://github.com/skot/ESP-Miner/pull/522
* Rejected Shares Percentage Information added by @WhiteyCookie in https://github.com/skot/ESP-Miner/pull/450
* Add Recovery Image to CI by @eandersson in https://github.com/skot/ESP-Miner/pull/413
* Add 205 to ci by @eandersson in https://github.com/skot/ESP-Miner/pull/529
* Make selftest failing non-fatal by @skot in https://github.com/skot/ESP-Miner/pull/524
* Fix hashing on BM1366 by @skot in https://github.com/skot/ESP-Miner/pull/532
* Add support for eusolo stats for ckpool by @eandersson in https://github.com/skot/ESP-Miner/pull/541
* Fix minor node security warnings by @eandersson in https://github.com/skot/ESP-Miner/pull/540
* Re-order and fix ckpool regex by @eandersson in https://github.com/skot/ESP-Miner/pull/542

## New Contributors
* @WRKampi made their first contribution in https://github.com/skot/ESP-Miner/pull/501
* @PMK made their first contribution in https://github.com/skot/ESP-Miner/pull/490

**Full Changelog**: https://github.com/skot/ESP-Miner/compare/v2.4.0...v2.4.1

## v2.4.0 (v2.4.0)

- Published: 2024-11-17
- Link: https://github.com/bitaxeorg/ESP-Miner/releases/tag/v2.4.0
- Prerelease: False

## What's Changed
* Re-worked how we publish artifacts when releasing new builds by @eandersson in https://github.com/skot/ESP-Miner/pull/411
* Use the same espressif/idf release for github and vscode by @eandersson in https://github.com/skot/ESP-Miner/pull/428
* Add OLED Bitaxe logo screen by @mutatrum in https://github.com/skot/ESP-Miner/pull/416
* add all in one factory file script by @WantClue in https://github.com/skot/ESP-Miner/pull/436
* Chart enhance by @benjamin-wilson in https://github.com/skot/ESP-Miner/pull/433
* Redo swarm by @benjamin-wilson in https://github.com/skot/ESP-Miner/pull/430
* Overhaul Axeos theme by @benjamin-wilson in https://github.com/skot/ESP-Miner/pull/429
* replaced default address with a prompt by @eyelight in https://github.com/skot/ESP-Miner/pull/438
* Add info for check on update by @WantClue in https://github.com/skot/ESP-Miner/pull/445
* fix: Temp suffix & 5v marker by @mrv777 in https://github.com/skot/ESP-Miner/pull/448
* small change to only-gzip.js to remove warning by @skot in https://github.com/skot/ESP-Miner/pull/449
* Fix ESP-NOW warning by limiting ap max_connections by @mutatrum in https://github.com/skot/ESP-Miner/pull/426
* Move back to solostats by @eandersson in https://github.com/skot/ESP-Miner/pull/423
* fix: Move back primary to human readable ckpool by @mrv777 in https://github.com/skot/ESP-Miner/pull/452
* Fix api not handling errors properly by @eandersson in https://github.com/skot/ESP-Miner/pull/424
* Fix CI warnings by @eandersson in https://github.com/skot/ESP-Miner/pull/465
* Do nothing when roaming to a different AP within the same wifi network by @eandersson in https://github.com/skot/ESP-Miner/pull/464
* fix: Change log font and add colors by @mrv777 in https://github.com/skot/ESP-Miner/pull/453
* fix: Better restart feedback & attempt to fix CORS by @mrv777 in https://github.com/skot/ESP-Miner/pull/455
* fix: Sort swarm, dup check, auto add not overwrite, import cleanup by @mrv777 in https://github.com/skot/ESP-Miner/pull/457
* Change artifact name for test builds by @eandersson in https://github.com/skot/ESP-Miner/pull/466
* Swarm restart returns text, not json by @eandersson in https://github.com/skot/ESP-Miner/pull/467
* fix: Better mobile styles for swarm by @mrv777 in https://github.com/skot/ESP-Miner/pull/458
* Minor npm module version bump to fix security warnings by @eandersson in https://github.com/skot/ESP-Miner/pull/460
* adjust bm1370 mhz settings to 6.25 multiplier by @WantClue in https://github.com/skot/ESP-Miner/pull/477
* add hashrate check to self test by @benjamin-wilson in https://github.com/skot/ESP-Miner/pull/486
* temp sensor fixes by @benjamin-wilson in https://github.com/skot/ESP-Miner/pull/484
* additions to dropdown by @benjamin-wilson in https://github.com/skot/ESP-Miner/pull/487

## New Contributors
* @eyelight made their first contribution in https://github.com/skot/ESP-Miner/pull/438

**Full Changelog**: https://github.com/skot/ESP-Miner/compare/v2.3.0...v2.4.0

## v2.3.0 (v2.3.0)

- Published: 2024-10-16
- Link: https://github.com/bitaxeorg/ESP-Miner/releases/tag/v2.3.0
- Prerelease: False

This is the "quick update just to change the overheat mode UI". There are tons of changes and improvements, check it out!

## What's Changed
* Legacy selftest fixes by @skot in https://github.com/skot/ESP-Miner/pull/346
* Allow the password... password by @eandersson in https://github.com/skot/ESP-Miner/pull/347
* Allow connecting to open WiFi networks by @skot in https://github.com/skot/ESP-Miner/pull/348
* WebUI fix for Power/Watts circle visualization by @WhiteyCookie in https://github.com/skot/ESP-Miner/pull/352
* Version mask now based on stratum msg by @adammwest in https://github.com/skot/ESP-Miner/pull/349
* ck solostats no longer works by @eandersson in https://github.com/skot/ESP-Miner/pull/354
* Set default cpu freq to 240mhz by @eandersson in https://github.com/skot/ESP-Miner/pull/338
* Add support for TPS546D24S as a drop in replacement for the TPS546D24A by @adasauce in https://github.com/skot/ESP-Miner/pull/355
* Suggest difficulty after auth to fix ckpool issue by @eandersson in https://github.com/skot/ESP-Miner/pull/353
* fix: Password visibility toggle #357 by @mrv777 in https://github.com/skot/ESP-Miner/pull/358
* fix: Add overheat alert, knob colors & max, chart dots & label #342 by @mrv777 in https://github.com/skot/ESP-Miner/pull/359
* Overheat mode improvements by @skot in https://github.com/skot/ESP-Miner/pull/344
* Protect against negative frequency and voltage values by @eandersson in https://github.com/skot/ESP-Miner/pull/326
* Fix wifi status not updating after disconnected #320 by @eandersson in https://github.com/skot/ESP-Miner/pull/321
* nvs memory fix by @shufps in https://github.com/skot/ESP-Miner/pull/305
* Add MAC address to API. by @b-rowan in https://github.com/skot/ESP-Miner/pull/295
* minor change to ckpool quicklink detector by @onlyblackstars in https://github.com/skot/ESP-Miner/pull/280
* Add a blurb about web based administration to the readme by @pRizz in https://github.com/skot/ESP-Miner/pull/259
* fix: Show mac address on log page #361 by @mrv777 in https://github.com/skot/ESP-Miner/pull/362
* fix: Misc UI Tweaks by @mrv777 in https://github.com/skot/ESP-Miner/pull/368
* Update CI to use esp idf v5.3.1 by @eandersson in https://github.com/skot/ESP-Miner/pull/363
* Increase the max number of log lines stored in browser by @eandersson in https://github.com/skot/ESP-Miner/pull/327
* Add stratum fallback support by @eandersson in https://github.com/skot/ESP-Miner/pull/336
* Fix compiler warnings by @skot in https://github.com/skot/ESP-Miner/pull/381
* changed BM1370 defaults in AxeOS by @skot in https://github.com/skot/ESP-Miner/pull/387
* fix: Power section UI on mobile improvement by @mrv777 in https://github.com/skot/ESP-Miner/pull/383
* Separate Network and regular Settings in UI by @eandersson in https://github.com/skot/ESP-Miner/pull/389
* Fix warnings2 by @skot in https://github.com/skot/ESP-Miner/pull/393
* Fix fallback user by @eandersson in https://github.com/skot/ESP-Miner/pull/375
* fix #374 Issue 1 : Fallback Stratum Password by @jiga in https://github.com/skot/ESP-Miner/pull/379
* Expose fallback state to API by @eandersson in https://github.com/skot/ESP-Miner/pull/391
* fix: Simply display just the active pool by @mrv777 in https://github.com/skot/ESP-Miner/pull/394
* simplify screen and remove old code by @WantClue in https://github.com/skot/ESP-Miner/pull/396
* Update npm dependencies by @eandersson in https://github.com/skot/ESP-Miner/pull/398
* Enable WiFi 802.11k 802.11v by @eandersson in https://github.com/skot/ESP-Miner/pull/365
* Don't allow flashing in AP mode and fix firmware upload error handling by @eandersson in https://github.com/skot/ESP-Miner/pull/390
* add warnings for consecutive timeout responses (no rx) from the chip by @adammwest in https://github.com/skot/ESP-Miner/pull/378
* Add overheat button and change loading service by @mrv777 in https://github.com/skot/ESP-Miner/pull/364
* Fix firmware error handling by @eandersson in https://github.com/skot/ESP-Miner/pull/399
* Fix bad www.bin loads by @skot in https://github.com/skot/ESP-Miner/pull/402
* fix self test functions, update example nvs configs with fallback stratum defaults by @skot in https://github.com/skot/ESP-Miner/pull/405
* fix selftest for bitaxe with INA260 by @skot in https://github.com/skot/ESP-Miner/pull/409
* Enable automatic build and release by @eandersson in https://github.com/skot/ESP-Miner/pull/408
* slight display formatting cleanup. by @skot in https://github.com/skot/ESP-Miner/pull/414

## New Contributors
* @WhiteyCookie made their first contribution in https://github.com/skot/ESP-Miner/pull/352
* @adammwest made their first contribution in https://github.com/skot/ESP-Miner/pull/349
* @adasauce made their first contribution in https://github.com/skot/ESP-Miner/pull/355
* @mrv777 made their first contribution in https://github.com/skot/ESP-Miner/pull/358
* @b-rowan made their first contribution in https://github.com/skot/ESP-Miner/pull/295
* @onlyblackstars made their first contribution in https://github.com/skot/ESP-Miner/pull/280
* @pRizz made their first contribution in https://github.com/skot/ESP-Miner/pull/259
* @jiga made their first contribution in https://github.com/skot/ESP-Miner/pull/379

**Full Changelog**: https://github.com/skot/ESP-Miner/compare/v2.2.2...v2.3.0

## v2.2.2 - Critical gamma bug fix (v2.2.2)

- Published: 2024-09-23
- Link: https://github.com/bitaxeorg/ESP-Miner/releases/tag/v2.2.2
- Prerelease: False

**Critical TPS546 Bug fix**

## Removed Previous Gamma Releases

## What's Changed
* Fixed TPS546 NVS writing that could cause corruption
* 601 defaults
* Misc 601 improvements
* Update readme.md by @WantClue in https://github.com/skot/ESP-Miner/pull/306
* Gamma support by @skot in https://github.com/skot/ESP-Miner/pull/292
* Update workflows to use esp idf 5.3 by @eandersson in https://github.com/skot/ESP-Miner/pull/322
* remove duplication by @WantClue in https://github.com/skot/ESP-Miner/pull/323
* add frequency rampup bm1368 by @WantClue in https://github.com/skot/ESP-Miner/pull/324
* Fix websocket logs causing device to crash #277 by @eandersson in https://github.com/skot/ESP-Miner/pull/318
* add transition to power management by @WantClue in https://github.com/skot/ESP-Miner/pull/325
* Remove invalid IPv4 validation in DNS code #329 by @eandersson in https://github.com/skot/ESP-Miner/pull/330
* Fix overtemp and self tests for gamma by @benjamin-wilson in https://github.com/skot/ESP-Miner/pull/343

## New Contributors
* @eandersson made their first contribution in https://github.com/skot/ESP-Miner/pull/322

**Full Changelog**: https://github.com/skot/ESP-Miner/compare/v2.1.10...v2.2.2

## v2.1.10 (v2.1.10)

- Published: 2024-08-13
- Link: https://github.com/bitaxeorg/ESP-Miner/releases/tag/v2.1.10
- Prerelease: False

## What's Changed
* *Added Overheat_mode by @wantclue in https://github.com/skot/ESP-Miner/pull/267**
- Add Multi-chip support without the need of nvs by @Georges760 in https://github.com/skot/ESP-Miner/pull/206
- Small optimization and code refacotr:  by @Georges760 in https://github.com/skot/ESP-Miner/pull/198
- Add quick link to stats when mining on CKPool by @wantclue
- Code cleanup by @tommywatson in https://github.com/skot/ESP-Miner/pull/220
- Add Supra 402 by @Georges760 in https://github.com/skot/ESP-Miner/pull/221
- Fix Fan speed web update by @skot @tommywatson @Georges760 @dadofsambonzuki @yanir99 @tdb3 in https://github.com/skot/ESP-Miner/pull/222
- Add Recovery Page by @tdb3 in https://github.com/skot/ESP-Miner/pull/223
- Change efficiency metric on display by @mutatrum in https://github.com/skot/ESP-Miner/pull/236
- Fix overheat boot loop by @benjamin-wilson 
- Fix job interval timining by @skot in https://github.com/skot/ESP-Miner/pull/249
- overheat mode protection on startup --> force a nvs value add if none existent

## Changes from 2.1.9 to 2.1.10
- reduce ASIC serial RX buf to 16 bytes and free() afer every nvs_config_get_string() by @skot in https://github.com/skot/ESP-Miner/pull/249
- moved nvs_close in nvs_config_get_u16() by @skot
- moved the whole overheat checking process into a new function and call it only of needed by @WantClue
- modify work queue to reduce startup mining.notify behaviour of not starting to hash (still needs improvement) by @WantClue in https://github.com/skot/ESP-Miner/pull/281
- ignoring Pre-Release from GitHub by @WantClue 
- introduce a mutec protection on http_server.c by @WantClue

## New Contributors
- @yanir99 made their first contribution in https://github.com/skot/ESP-Miner/pull/209
- @dadofsambonzuki made their first contribution in https://github.com/skot/ESP-Miner/pull/231
- @3x3y3z3t made their first contribution in https://github.com/skot/ESP-Miner/pull/247
- @harrr1 made their first contribution in https://github.com/skot/ESP-Miner/pull/254
- @Arabaku made their first contribution in https://github.com/skot/ESP-Miner/pull/256


**Full Changelog**: https://github.com/skot/ESP-Miner/compare/v2.1.8...v2.1.10

## v2.1.8 (v2.1.8)

- Published: 2024-06-08
- Link: https://github.com/bitaxeorg/ESP-Miner/releases/tag/v2.1.8
- Prerelease: False

## What's Changed
* **Fix for possible over heat situation if the WiFi goes down**
* Add software version string to the stratum mining.subscribe by @wizkid057 in https://github.com/skot/ESP-Miner/pull/197
* Small optimization : avoid strcmp by @Georges760 in https://github.com/skot/ESP-Miner/pull/198
* Add quick link to stats when mining on OCEAN by @wizkid057 in https://github.com/skot/ESP-Miner/pull/200
* refactor: deduplicate i2c parameters by @tdb3 in https://github.com/skot/ESP-Miner/pull/188
* moved the DNS lookup inside the stratum connection retry loop by @skot in https://github.com/skot/ESP-Miner/pull/204
* Optimization: i2c factorization by @Georges760 in https://github.com/skot/ESP-Miner/pull/202
* refactor: split vcore out from ds4432 driver, to make it an abstracti… by @Georges760 in https://github.com/skot/ESP-Miner/pull/205
* Pressing the boot button will cycle the info screen @WantClue 

## New Contributors
* @wizkid057 made their first contribution in https://github.com/skot/ESP-Miner/pull/197
* @tdb3 made their first contribution in https://github.com/skot/ESP-Miner/pull/188

**Full Changelog**: https://github.com/skot/ESP-Miner/compare/v2.1.7...v2.1.8

## v2.1.7 (v2.1.7)

- Published: 2024-06-02
- Link: https://github.com/bitaxeorg/ESP-Miner/releases/tag/v2.1.7
- Prerelease: False

Fix OCEAN min diff rejected shares and hashrate updates

This firmware is tested and working on;
- BitaxeUltra 202
- BitaxeUltra 205
- BitaxeSupra 400
- BitaxeSupra 401

It has not been tested on any BitaxeMax (BM1397-based) versions 😬

## To update your Bitaxe: 
0. Download the `esp-miner.bin` in the assets section of this release
1. Navigate to the IP addresses listed on your Bitaxe display via your browser.
2. In the left-hand menu click on "Settings"
3. In the Update Firmware section click "+ Browse" and select the `esp-miner.bin` file you downloaded in step 0
4. AxeOS will show "Working..." on the screen. **wait until this message goes away!** then you can click Restart in the left hand menu
5. Hack the planet!

There are no AxeOS updates in this release, so no `www.bin` file is necessary. It is provided here in case you are updating from an older version.

## What's Changed
* Stratum message ordering fix by @skot in https://github.com/skot/ESP-Miner/pull/192
* Faster hashrate display updates by @skot in https://github.com/skot/ESP-Miner/pull/196


**Full Changelog**: https://github.com/skot/ESP-Miner/compare/v2.1.6...v2.1.7

## v2.1.6 (v2.1.6)

- Published: 2024-05-26
- Link: https://github.com/bitaxeorg/ESP-Miner/releases/tag/v2.1.6
- Prerelease: False

**Full Changelog**: https://github.com/skot/ESP-Miner/compare/v2.1.5...v2.1.6
- Fixed overflow bug with realtime logs
- Fixed restart POST request not returning 

## v2.1.5 (v2.1.5)

- Published: 2024-05-25
- Link: https://github.com/bitaxeorg/ESP-Miner/releases/tag/v2.1.5
- Prerelease: False

## What's Changed
* Wifi will continue to try to re-connect when disconnected
* Fan will no longer go 100% on reboot
* fix stratum parsing not always counting rejected shares by @MoellerDi in https://github.com/skot/ESP-Miner/pull/163
* add option to configure hostname by @MoellerDi in https://github.com/skot/ESP-Miner/pull/174
* Add more Logging before esp_restart by @pixeldoc2000 in https://github.com/skot/ESP-Miner/pull/179
* add best difficulty since system boot by @MoellerDi in https://github.com/skot/ESP-Miner/pull/162
* issue #100 resolved - ASIC not always starting/hashing after boot (due to race condition) by @MoellerDi in https://github.com/skot/ESP-Miner/pull/152


**Full Changelog**: https://github.com/skot/ESP-Miner/compare/v2.1.4...v2.1.5

## v2.1.4 (v2.1.4)

- Published: 2024-05-22
- Link: https://github.com/bitaxeorg/ESP-Miner/releases/tag/v2.1.4
- Prerelease: False

## What's Changed
* uint fix by @WantClue in https://github.com/skot/ESP-Miner/pull/151
* fix Best Difficulty can not be > 4.29G by @MoellerDi in https://github.com/skot/ESP-Miner/pull/155
* API: System Info change similar / duplicate JSON Key fanSpeed and fanspeed by @pixeldoc2000 in https://github.com/skot/ESP-Miner/pull/170
* selftest should only run with "factory" images. You can opt-in by setting selftest in the config.cvs

## New Contributors
* @MoellerDi made their first contribution in https://github.com/skot/ESP-Miner/pull/155
* @pixeldoc2000 made their first contribution in https://github.com/skot/ESP-Miner/pull/170

**Full Changelog**: https://github.com/skot/ESP-Miner/compare/v2.1.3...v2.1.4

## v2.1.3 (v2.1.3)

- Published: 2024-03-18
- Link: https://github.com/bitaxeorg/ESP-Miner/releases/tag/v2.1.3
- Prerelease: False

Improved self test and when to run it, skipping BM1397.

**Full Changelog**: https://github.com/skot/ESP-Miner/compare/v2.1.2...v2.1.3

## v2.1.2 (v2.1.2)

- Published: 2024-03-17
- Link: https://github.com/bitaxeorg/ESP-Miner/releases/tag/v2.1.2
- Prerelease: False

## What's Changed
* Self_test by @benjamin-wilson in https://github.com/skot/ESP-Miner/pull/139
* Add API section to readme.md by @mroxso in https://github.com/skot/ESP-Miner/pull/135

## New Contributors
* @mroxso made their first contribution in https://github.com/skot/ESP-Miner/pull/135

**Full Changelog**: https://github.com/skot/ESP-Miner/compare/v2.1.1...v2.1.2

## v2.1.1 (v2.1.1)

- Published: 2024-03-12
- Link: https://github.com/bitaxeorg/ESP-Miner/releases/tag/v2.1.1
- Prerelease: False

**Full Changelog**: https://github.com/skot/ESP-Miner/compare/v2.1.0...v2.1.1

- Fixed mining for Bitaxe Max (BM1397) models
- Restart button moved and available on mobile
- Logs scroll stop button
- Minor tweaks 

## v2.1.0 (v2.1.0)

- Published: 2024-03-04
- Link: https://github.com/bitaxeorg/ESP-Miner/releases/tag/v2.1.0
- Prerelease: False

## What's Changed
* AxeOS GUI refactor
* Add BM1368 support by @johnny9 in https://github.com/skot/ESP-Miner/pull/106
* Issue #112 resolved : build instructions added to Readme.md by @Collins-Webdev in https://github.com/skot/ESP-Miner/pull/114
* Revert "Issue #112 resolved : build instructions added to Readme.md" by @skot in https://github.com/skot/ESP-Miner/pull/115

## New Contributors
* @Collins-Webdev made their first contribution in https://github.com/skot/ESP-Miner/pull/114

**Full Changelog**: https://github.com/skot/ESP-Miner/compare/v2.0.7...v2.1.0

## v2.0.7 (v2.0.7)

- Published: 2024-01-21
- Link: https://github.com/bitaxeorg/ESP-Miner/releases/tag/v2.0.7
- Prerelease: False

- Power management will now use the board version to distinguish capabilities 
- New Stratum password field
- Version rolling now properly configured by stratum server
**Full Changelog**: https://github.com/skot/ESP-Miner/compare/v2.0.6...v2.0.7

## v2.0.6 (v2.0.6)

- Published: 2024-01-10
- Link: https://github.com/bitaxeorg/ESP-Miner/releases/tag/v2.0.6
- Prerelease: False

## What's Changed
* revert the order of mining.configure and mining.subscribe by @skot in https://github.com/skot/ESP-Miner/pull/81

**Full Changelog**: https://github.com/skot/ESP-Miner/compare/v2.0.5...v2.0.6

## New Factory File

esp-miner-factory-204-v2.0.6.bin is a factory file with a default configuration for the 204 bitaxe merged into it. If you use this file you can use a flasher like https://espressif.github.io/esptool-js/ instead of bitaxetool and flash to address 0x0.

## Known Issues

Some pools complain about the ordering of `mining.configure` and `mining.subscribe` but should still work. We are still investigating this issue in #80 

## v2.0.5 (v2.0.5)

- Published: 2024-01-08
- Link: https://github.com/bitaxeorg/ESP-Miner/releases/tag/v2.0.5
- Prerelease: False

## What's Changed
* update readme to bitaxetool by @WantClue in https://github.com/skot/ESP-Miner/pull/60
* Network resets2 by @skot in https://github.com/skot/ESP-Miner/pull/74
* Fixed display when share found
* Removed password from REST Get
* Added links to latest firmware
* Fix suggest_difficulty
* Lowered voltage danger warning threshold
* Added script to merge config into factory file

**Full Changelog**: https://github.com/skot/ESP-Miner/compare/v2.0.4...v2.0.5

## New Factory File
`esp-miner-factory-204-v2.0.5.bin` is a factory file with a default configuration for the 204 bitaxe merged into it. If you use this file you can use a flasher like https://espressif.github.io/esptool-js/ instead of bitaxetool and flash to address 0x0.

## Known Issues
A regression from 2.0.4, braiins pool mining does not work


## v2.0.4 (v2.0.4)

- Published: 2023-11-27
- Link: https://github.com/bitaxeorg/ESP-Miner/releases/tag/v2.0.4
- Prerelease: False

## New Features
* Swarm view in AxeOS. Monitor and administrate all your AxeOS devices from a single view.
## What's Changed
* Fix formula for automatic fan control and adjust minimum fan speed by @ozbibi in https://github.com/skot/ESP-Miner/pull/59
* Hide logs and websocket connection on page startup
* http_server: handle missing key/values in system settings updates
## New Contributors
* @ozbibi made their first contribution in https://github.com/skot/ESP-Miner/pull/59

**Full Changelog**: https://github.com/skot/ESP-Miner/compare/v2.0.3...v2.0.4

## v2.0.3 (v2.0.3)

- Published: 2023-11-21
- Link: https://github.com/bitaxeorg/ESP-Miner/releases/tag/v2.0.3
- Prerelease: False

Fix bug where the nvs config option for fan polarity was too long

## PWM and Form validation (v2.0.2)

- Published: 2023-11-18
- Link: https://github.com/bitaxeorg/ESP-Miner/releases/tag/v2.0.2
- Prerelease: False

- Added PWM controls and settings to AxeOs
- Manual fan speed
- Automatic fan speed
- Added additional validation in the settings form
- Added quick-link for public-pool users on home screen

## What's Changed
* Save "Best Difficulty" scores into NVS #20 by @tommywatson in https://github.com/skot/ESP-Miner/pull/47
* Fixes mining.configure order #50 by @checksum0 in https://github.com/skot/ESP-Miner/pull/51

## New Contributors
* @tommywatson made their first contribution in https://github.com/skot/ESP-Miner/pull/47
* @checksum0 made their first contribution in https://github.com/skot/ESP-Miner/pull/51

**Full Changelog**: https://github.com/skot/ESP-Miner/compare/v2.0.1...v2.0.2

## v2.0.1 (v2.0.1)

- Published: 2023-10-18
- Link: https://github.com/bitaxeorg/ESP-Miner/releases/tag/v2.0.1
- Prerelease: False

### Temperature protection for the Bitaxe 201 (Ultra , BM1366)
- added 'flipscreen' config option that will rotate the screen 180 degrees for different mounting options.
- released OTA flies

See v2.0.0 for setup details

**Full Changelog**: https://github.com/skot/ESP-Miner/compare/v2.0.0...v2.0.1

## v2.0.0 (ultra) (v2.0.0)

- Published: 2023-10-04
- Link: https://github.com/bitaxeorg/ESP-Miner/releases/tag/v2.0.0
- Prerelease: False

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

## v1.0 (v1.0)

- Published: 2023-07-01
- Link: https://github.com/bitaxeorg/ESP-Miner/releases/tag/v1.0
- Prerelease: False

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
