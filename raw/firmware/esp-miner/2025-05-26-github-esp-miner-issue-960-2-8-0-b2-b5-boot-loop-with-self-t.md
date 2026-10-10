# bitaxeorg/ESP-Miner issue #960: 2.8.0.b2-b5 boot loop with self test

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/960
> Collected: 2026-10-07
> Published: 2025-05-26

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 960
- State: closed
- Author: xr1140
- Opened: 2025-05-26
- Closed: 2025-05-27
- Labels: none

## Description


Erery release after v2.8.0b1 will result in crash loop. Below logs from b2 and b3 firmware, if needed I can provide for the rest b2-b5


**v2.8.0b2**

`Rebooting...
ESP-ROM:esp32s3-20210327
Build:Mar 27 2021
rst:0xc (RTC_SW_CPU_RST),boot:0x28 (SPI_FAST_FLASH_BOOT)
Saved PC:0x40375f19
SPIWP:0xee
mode:DIO, clock div:1
load:0x3fce2810,len:0x15a0
load:0x403c8700,len:0x4
load:0x403c8704,len:0xd20
load:0x403cb700,len:0x2f00
entry 0x403c8928
I (26) boot: ESP-IDF v5.4.1 2nd stage bootloader
I (26) boot: compile time May 21 2025 20:09:40
I (26) boot: Multicore bootloader
I (27) boot: chip revision: v0.2
I (29) boot: efuse block revision: v1.3
I (33) boot.esp32s3: Boot SPI Speed : 80MHz
I (37) boot.esp32s3: SPI Mode       : DIO
I (40) boot.esp32s3: SPI Flash Size : 16MB
I (44) boot: Enabling RNG early entropy source...
I (49) boot: Partition Table:
I (51) boot: ## Label            Usage          Type ST Offset   Length
I (58) boot:  0 nvs              WiFi data        01 02 00009000 00006000
I (64) boot:  1 phy_init         RF data          01 01 0000f000 00001000
I (71) boot:  2 factory          factory app      00 00 00010000 00400000
I (77) boot:  3 www              Unknown data     01 82 00410000 00300000
I (84) boot:  4 ota_0            OTA app          00 10 00710000 00400000
I (90) boot:  5 ota_1            OTA app          00 11 00b10000 00400000
I (97) boot:  6 otadata          OTA data         01 00 00f10000 00002000
I (103) boot:  7 coredump         Unknown data     01 03 00f12000 00010000
I (110) boot: End of partition table
I (113) boot: Defaulting to factory image
I (117) esp_image: segment 0: paddr=00010020 vaddr=3c0e0020 size=31c48h (203848) map
I (160) esp_image: segment 1: paddr=00041c70 vaddr=3fc9d000 size=05820h ( 22560) load
I (166) esp_image: segment 2: paddr=00047498 vaddr=40374000 size=08b80h ( 35712) load
I (174) esp_image: segment 3: paddr=00050020 vaddr=42000020 size=d6fa0h (880544) map
I (330) esp_image: segment 4: paddr=00126fc8 vaddr=4037cb80 size=1042ch ( 66604) load
I (345) esp_image: segment 5: paddr=001373fc vaddr=600fe100 size=0001ch (    28) load
I (356) boot: Loaded app from partition at offset 0x10000
I (356) boot: Disabling RNG early entropy source...
[0;32mI (366) octal_psram: vendor id    : 0x0d (AP)[0m
[0;32mI (366) octal_psram: dev id       : 0x02 (generation 3)[0m
[0;32mI (367) octal_psram: density      : 0x03 (64 Mbit)[0m
[0;32mI (371) octal_psram: good-die     : 0x01 (Pass)[0m
[0;32mI (377) octal_psram: Latency      : 0x01 (Fixed)[0m
[0;32mI (382) octal_psram: VCC          : 0x01 (3V)[0m
[0;32mI (387) octal_psram: SRF          : 0x01 (Fast Refresh)[0m
[0;32mI (393) octal_psram: BurstType    : 0x01 (Hybrid Wrap)[0m
[0;32mI (399) octal_psram: BurstLen     : 0x01 (32 Byte)[0m
[0;32mI (404) octal_psram: Readlatency  : 0x02 (10 cycles@Fixed)[0m
[0;32mI (410) octal_psram: DriveStrength: 0x00 (1/1)[0m
[0;32mI (416) MSPI Timing: PSRAM timing tuning index: 5[0m
[0;32mI (421) esp_psram: Found 8MB PSRAM device[0m
[0;32mI (425) esp_psram: Speed: 80MHz[0m
[0;32mI (429) cpu_start: Multicore app[0m
[0;32mI (866) esp_psram: SPI SRAM memory test OK[0m
[0;32mI (875) cpu_start: Pro cpu start user code[0m
[0;32mI (875) cpu_start: cpu freq: 240000000 Hz[0m
[0;32mI (875) app_init: Application information:[0m
[0;32mI (878) app_init: Project name:     esp-miner[0m
[0;32mI (883) app_init: App version:      v2.8.0b2[0m
[0;32mI (888) app_init: Compile time:     May 21 2025 20:09:34[0m
[0;32mI (894) app_init: ELF file SHA256:  b1ed447ee...[0m
[0;32mI (899) app_init: ESP-IDF:          v5.4.1[0m
[0;32mI (904) efuse_init: Min chip rev:     v0.0[0m
[0;32mI (909) efuse_init: Max chip rev:     v0.99 [0m
[0;32mI (914) efuse_init: Chip rev:         v0.2[0m
[0;32mI (918) heap_init: Initializing. RAM available for dynamic allocation:[0m
[0;32mI (926) heap_init: At 3FCB8870 len 00030EA0 (195 KiB): RAM[0m
[0;32mI (932) heap_init: At 3FCE9710 len 00005724 (21 KiB): RAM[0m
[0;32mI (938) heap_init: At 3FCF0000 len 00008000 (32 KiB): DRAM[0m
[0;32mI (944) heap_init: At 600FE11C len 00001ECC (7 KiB): RTCRAM[0m
[0;32mI (950) esp_psram: Adding pool of 8192K of PSRAM memory to heap allocator[0m
[0;32mI (958) spi_flash: detected chip: gd[0m
[0;32mI (962) spi_flash: flash io: dio[0m
[0;32mI (966) sleep_gpio: Configure to isolate all GPIO pins in sleep state[0m
[0;32mI (973) sleep_gpio: Enable automatic switching of GPIO sleep configuration[0m
[0;32mI (981) main_task: Started on CPU0[0m
[0;32mI (991) esp_psram: Reserving pool of 32K of internal memory for DMA/internal allocations[0m
[0;32mI (991) main_task: Calling app_main()[0m
[0;32mI (1001) bitaxe: Welcome to the bitaxe - FOSS || GTFO![0m
[0;32mI (1001) bitaxe: I2C initialized successfully[0m
[0;32mI (1111) ADC: calibration scheme version is Curve Fitting[0m
[0;32mI (1111) ADC: Calibration Success[0m
[0;32mI (1111) device_config: Device Model: Gamma[0m
[0;32mI (1111) device_config: Board Version: 601[0m
[0;32mI (1111) device_config: ASIC: 1x BM1370 (128 cores)[0m
[0;32mI (1121) self_test: Running Self Tests[0m
[0;32mI (1121) input: Install button driver[0m
[0;32mI (1131) gpio: GPIO[0]| InputEn: 1| OutputEn: 0| OpenDrain: 0| Pullup: 1| Pulldown: 0| Intr:3 [0m
Guru Meditation Error: Core  0 panic'ed (LoadProhibited). Exception was unhandled.

Core  0 register dump:
PC      : 0x42036758  PS      : 0x00060130  A0      : 0x820367d6  A1      : 0x3fcbbae0  
A2      : 0x00000000  A3      : 0x3fcbbb00  A4      : 0x3fcbbb04  A5      : 0x00060323  
A6      : 0x3c0f0d17  A7      : 0x00000000  A8      : 0x00000010  A9      : 0x3fcbbac0  
A10     : 0x00000003  A11     : 0x3fcbbb00  A12     : 0x3fcbbb04  A13     : 0x00060323  
A14     : 0x00000000  A15     : 0x0000cdcd  SAR     : 0x0000001f  EXCCAUSE: 0x0000001c  
EXCVADDR: 0x00000014  LBEG    : 0x400556d5  LEND    : 0x400556e5  LCOUNT  : 0xfffffffe  


Backtrace: 0x42036755:0x3fcbbae0 0x420367d3:0x3fcbbb00 0x420368fd:0x3fcbbb30 0x42034e0a:0x3fcbbb50 0x42036a3d:0x3fcbbb70 0x42033b19:0x3fcbbb90 0x420243c2:0x3fcbbbb0 0x420181b0:0x3fcbbbd0 0x42012532:0x3fcbbc20 0x420128bb:0x3fcbbc40 0x4200f1c7:0x3fcbbfa0 0x420d5fd7:0x3fcbbfd0 0x4037fd3d:0x3fcbc000




ELF file SHA256: b1ed447ee
`


**v2.8.0b3**

`Rebooting...
ESP-ROM:esp32s3-20210327
Build:Mar 27 2021
rst:0xc (RTC_SW_CPU_RST),boot:0x28 (SPI_FAST_FLASH_BOOT)
Saved PC:0x40375f19
SPIWP:0xee
mode:DIO, clock div:1
load:0x3fce2810,len:0x15a0
load:0x403c8700,len:0x4
load:0x403c8704,len:0xd20
load:0x403cb700,len:0x2f00
entry 0x403c8928
I (26) boot: ESP-IDF v5.4.1 2nd stage bootloader
I (26) boot: compile time May 25 2025 13:13:02
I (26) boot: Multicore bootloader
I (27) boot: chip revision: v0.2
I (29) boot: efuse block revision: v1.3
I (33) boot.esp32s3: Boot SPI Speed : 80MHz
I (37) boot.esp32s3: SPI Mode       : DIO
I (40) boot.esp32s3: SPI Flash Size : 16MB
I (44) boot: Enabling RNG early entropy source...
I (49) boot: Partition Table:
I (51) boot: ## Label            Usage          Type ST Offset   Length
I (58) boot:  0 nvs              WiFi data        01 02 00009000 00006000
I (64) boot:  1 phy_init         RF data          01 01 0000f000 00001000
I (71) boot:  2 factory          factory app      00 00 00010000 00400000
I (77) boot:  3 www              Unknown data     01 82 00410000 00300000
I (84) boot:  4 ota_0            OTA app          00 10 00710000 00400000
I (90) boot:  5 ota_1            OTA app          00 11 00b10000 00400000
I (97) boot:  6 otadata          OTA data         01 00 00f10000 00002000
I (103) boot:  7 coredump         Unknown data     01 03 00f12000 00010000
I (110) boot: End of partition table
I (113) boot: Defaulting to factory image
I (117) esp_image: segment 0: paddr=00010020 vaddr=3c0e0020 size=31f78h (204664) map
I (161) esp_image: segment 1: paddr=00041fa0 vaddr=3fc9d000 size=05420h ( 21536) load
I (166) esp_image: segment 2: paddr=000473c8 vaddr=40374000 size=08c50h ( 35920) load
I (174) esp_image: segment 3: paddr=00050020 vaddr=42000020 size=d7134h (880948) map
I (330) esp_image: segment 4: paddr=0012715c vaddr=4037cc50 size=1035ch ( 66396) load
I (345) esp_image: segment 5: paddr=001374c0 vaddr=600fe100 size=0001ch (    28) load
I (356) boot: Loaded app from partition at offset 0x10000
I (356) boot: Disabling RNG early entropy source...
[0;32mI (366) octal_psram: vendor id    : 0x0d (AP)[0m
[0;32mI (366) octal_psram: dev id       : 0x02 (generation 3)[0m
[0;32mI (367) octal_psram: density      : 0x03 (64 Mbit)[0m
[0;32mI (371) octal_psram: good-die     : 0x01 (Pass)[0m
[0;32mI (376) octal_psram: Latency      : 0x01 (Fixed)[0m
[0;32mI (382) octal_psram: VCC          : 0x01 (3V)[0m
[0;32mI (387) octal_psram: SRF          : 0x01 (Fast Refresh)[0m
[0;32mI (393) octal_psram: BurstType    : 0x01 (Hybrid Wrap)[0m
[0;32mI (399) octal_psram: BurstLen     : 0x01 (32 Byte)[0m
[0;32mI (404) octal_psram: Readlatency  : 0x02 (10 cycles@Fixed)[0m
[0;32mI (410) octal_psram: DriveStrength: 0x00 (1/1)[0m
[0;32mI (416) MSPI Timing: PSRAM timing tuning index: 5[0m
[0;32mI (421) esp_psram: Found 8MB PSRAM device[0m
[0;32mI (425) esp_psram: Speed: 80MHz[0m
[0;32mI (429) cpu_start: Multicore app[0m
[0;32mI (866) esp_psram: SPI SRAM memory test OK[0m
[0;32mI (875) cpu_start: Pro cpu start user code[0m
[0;32mI (875) cpu_start: cpu freq: 240000000 Hz[0m
[0;32mI (875) app_init: Application information:[0m
[0;32mI (878) app_init: Project name:     esp-miner[0m
[0;32mI (883) app_init: App version:      v2.8.0b3[0m
[0;32mI (888) app_init: Compile time:     May 25 2025 13:12:56[0m
[0;32mI (894) app_init: ELF file SHA256:  db99fc128...[0m
[0;32mI (899) app_init: ESP-IDF:          v5.4.1[0m
[0;32mI (904) efuse_init: Min chip rev:     v0.0[0m
[0;32mI (909) efuse_init: Max chip rev:     v0.99 [0m
[0;32mI (913) efuse_init: Chip rev:         v0.2[0m
[0;32mI (918) heap_init: Initializing. RAM available for dynamic allocation:[0m
[0;32mI (926) heap_init: At 3FCB8478 len 00031298 (196 KiB): RAM[0m
[0;32mI (932) heap_init: At 3FCE9710 len 00005724 (21 KiB): RAM[0m
[0;32mI (938) heap_init: At 3FCF0000 len 00008000 (32 KiB): DRAM[0m
[0;32mI (944) heap_init: At 600FE11C len 00001ECC (7 KiB): RTCRAM[0m
[0;32mI (950) esp_psram: Adding pool of 8192K of PSRAM memory to heap allocator[0m
[0;32mI (958) spi_flash: detected chip: gd[0m
[0;32mI (962) spi_flash: flash io: dio[0m
[0;32mI (966) sleep_gpio: Configure to isolate all GPIO pins in sleep state[0m
[0;32mI (973) sleep_gpio: Enable automatic switching of GPIO sleep configuration[0m
[0;32mI (981) main_task: Started on CPU0[0m
[0;32mI (991) esp_psram: Reserving pool of 32K of internal memory for DMA/internal allocations[0m
[0;32mI (991) main_task: Calling app_main()[0m
[0;32mI (1001) bitaxe: Welcome to the bitaxe - FOSS || GTFO![0m
[0;32mI (1001) bitaxe: I2C initialized successfully[0m
[0;32mI (1111) ADC: calibration scheme version is Curve Fitting[0m
[0;32mI (1111) ADC: Calibration Success[0m
[0;32mI (1111) device_config: Device Model: Gamma[0m
[0;32mI (1111) device_config: Board Version: 601[0m
[0;32mI (1111) device_config: ASIC: 1x BM1370 (128 cores)[0m
[0;32mI (1121) self_test: Running Self Tests[0m
[0;32mI (1121) input: Install button driver[0m
[0;32mI (1131) gpio: GPIO[0]| InputEn: 1| OutputEn: 0| OpenDrain: 0| Pullup: 1| Pulldown: 0| Intr:3 [0m
Guru Meditation Error: Core  0 panic'ed (LoadProhibited). Exception was unhandled.

Core  0 register dump:
PC      : 0x4203689c  PS      : 0x00060130  A0      : 0x8203691a  A1      : 0x3fcbb6f0  
A2      : 0x00000000  A3      : 0x3fcbb710  A4      : 0x3fcbb714  A5      : 0x00060323  
A6      : 0x3c0f0e4f  A7      : 0x00000000  A8      : 0x00000010  A9      : 0x3fcbb6d0  
A10     : 0x00000003  A11     : 0x3fcbb710  A12     : 0x3fcbb714  A13     : 0x00060323  
A14     : 0x00000000  A15     : 0x0000cdcd  SAR     : 0x0000001f  EXCCAUSE: 0x0000001c  
EXCVADDR: 0x00000014  LBEG    : 0x400556d5  LEND    : 0x400556e5  LCOUNT  : 0xfffffffe  


Backtrace: 0x42036899:0x3fcbb6f0 0x42036917:0x3fcbb710 0x42036a41:0x3fcbb740 0x42034f4e:0x3fcbb760 0x42036b81:0x3fcbb780 0x42033c5d:0x3fcbb7a0 0x42024506:0x3fcbb7c0 0x420183a8:0x3fcbb7e0 0x4201256e:0x3fcbb830 0x420128f7:0x3fcbb850 0x4200f1f7:0x3fcbbbb0 0x420d616b:0x3fcbbbe0 0x4037fd3d:0x3fcbbc10




ELF file SHA256: db99fc128
`

**Hardware (please complete the following information):**
 - Bitaxe HW version: Gamma 601
 - Bitaxe HW vendor: purchased from miningwholesale.eu
 - ESP-Miner FW version: v2.8.0b2+
 - Hash Frequency: default
 - Voltage: default

## Comments

### mutatrum on 2025-05-27

From [r3mko on Discord](https://discord.com/channels/1091348375301013615/1094385611718270977/1376684902367367169):
 > I have had the same problem with my "custom" firmware (up-to-date with dev-latest) when doing a self-test after writing the factory image. I could get it to work by removing the if statements at https://github.com/bitaxeorg/ESP-Miner/blob/8a7a302c5f269cacb0a342583a1ce09090b6bdae/main/self_test/self_test.c#L131 and https://github.com/bitaxeorg/ESP-Miner/blob/8a7a302c5f269cacb0a342583a1ce09090b6bdae/main/self_test/self_test.c#L161
