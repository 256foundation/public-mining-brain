# bitaxeorg/bitaxe-raw issue #7: Image requires efuse blk rev >= v103.31, but chip is v1.3

> Source: https://github.com/bitaxeorg/bitaxe-raw/issues/7
> Collected: 2026-10-07
> Published: 2026-01-12

- Repository: bitaxeorg/bitaxe-raw
- Type: issue
- Number: 7
- State: open
- Author: skot
- Opened: 2026-01-12
- Closed: n/a
- Labels: none

## Description

When flashing with `cargo flash --release --chip esp32s3` my bitaxeGamma restarts and I get this looping in the log

```
ESP-ROM:esp32s3-20210327
Build:Mar 27 2021
rst:0x3 (RTC_SW_SYS_RST),boot:0x28 (SPI_FAST_FLASH_BOOT)
Saved PC:0x403cceb5
SPIWP:0xee
mode:DIO, clock div:2
load:0x3fce2810,len:0x15a0
load:0x403c8700,len:0x4
load:0x403c8704,len:0xd24
load:0x403cb700,len:0x2f04
entry 0x403c8928
I (27) boot: ESP-IDF v5.4.1-426-g3ad36321ea 2nd stage bootloader
I (27) boot: compile time Apr 24 2025 15:55:11
I (27) boot: Multicore bootloader
I (28) boot: chip revision: v0.2
I (31) boot: efuse block revision: v1.3
I (35) boot.esp32s3: Boot SPI Speed : 40MHz
I (39) boot.esp32s3: SPI Mode : DIO
I (42) boot.esp32s3: SPI Flash Size : 16MB
I (46) boot: Enabling RNG early entropy source...
I (51) boot: Partition Table:
I (53) boot: ## Label Usage Type ST Offset Length
I (60) boot: 0 nvs WiFi data 01 02 00009000 00006000
I (66) boot: 1 phy_init RF data 01 01 0000f000 00001000
I (73) boot: 2 factory factory app 00 00 00010000 00fa0000
I (79) boot: End of partition table
I (83) esp_image: segment 0: paddr=00010020 vaddr=3c020020 size=03038h ( 12344) map
E (90) boot_comm: Image requires efuse blk rev >= v103.31, but chip is v1.3
E (97) boot: Factory app partition is not bootable
E (101) boot: No bootable app partitions in the partition table
```
