# bitaxeorg/ESP-Miner issue #1510: Firmware version 2.12.2 doesn't work on Bitaxe Gamma 601

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1510
> Collected: 2026-10-07
> Published: 2026-01-15

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1510
- State: closed
- Author: Thorgrlm
- Opened: 2026-01-15
- Closed: 2026-01-16
- Labels: none

## Description

Hi, I have a Bitaxe Gamma 601 and firmware version 2.12.2 isn't working. The last firmware version that works for me is 2.4.2. Is there any way to update my device to the latest firmware or a more recent one?

## Comments

### ghost on 2026-01-15

Post a clean photo here of the ESP32 chip that is on this Gamma so we can read what is on it.

v2.12.2  works on the correct ESP32 chip, both files need to be flashed to the device (`www.bin` & `esp-miner.bin`).



### mutatrum on 2026-01-15

The important part is at the bottom:

<img width="600" alt="Image" src="https://github.com/user-attachments/assets/ccb5add2-d22b-4e51-993d-cdff07511694" />

In this case `MCN16R8`.

### Thorgrlm on 2026-01-15

esptool.py --port /dev/ttyACM0 chip_id
esptool.py v4.10.0
Serial port /dev/ttyACM0
Connecting...
Detecting chip type... ESP32-S3
Chip is ESP32-S3 (QFN56) (revision v0.1)
Features: WiFi, BLE
Crystal is 40MHz
USB mode: USB-Serial/JTAG
MAC: f4:12:fa:46:16:44
Uploading stub...
Running stub...
Stub running...
Warning: ESP32-S3 has no Chip ID. Reading MAC instead.
MAC: f4:12:fa:46:16:44


idf.py -p /dev/ttyACM0 monitor
ELF file SHA256: 

Rebooting...
ESP-ROM:esp32s3-20210327
Build:Mar 27 2021
rst:0xc (RTC_SW_CPU_RST),boot:0x28 (SPI_FAST_FLASH_BOOT)
Saved PC:0x4037e418
SPIWP:0xee
mode:DIO, clock div:1
load:0x3fce2810,len:0x1870
load:0x403c8700,len:0x4
load:0x403c8704,len:0xce8
load:0x403cb700,len:0x2ed8
entry 0x403c8918
I (26) boot: ESP-IDF v5.3.2 2nd stage bootloader
I (26) boot: compile time Dec 16 2024 18:26:29
I (26) boot: Multicore bootloader
I (29) boot: chip revision: v0.1
I (33) boot: efuse block revision: v1.2
I (38) boot.esp32s3: Boot SPI Speed : 80MHz
I (42) boot.esp32s3: SPI Mode       : DIO
I (47) boot.esp32s3: SPI Flash Size : 16MB
I (52) boot: Enabling RNG early entropy source...
I (57) boot: Partition Table:
I (61) boot: ## Label            Usage          Type ST Offset   Length
I (68) boot:  0 nvs              WiFi data        01 02 00009000 00006000
I (76) boot:  1 phy_init         RF data          01 01 0000f000 00001000
I (83) boot:  2 factory          factory app      00 00 00010000 00400000
I (91) boot:  3 www              Unknown data     01 82 00410000 00300000
I (98) boot:  4 ota_0            OTA app          00 10 00710000 00400000
I (106) boot:  5 ota_1            OTA app          00 11 00b10000 00400000
I (113) boot:  6 otadata          OTA data         01 00 00f10000 00002000
I (121) boot:  7 coredump         Unknown data     01 03 00f12000 00010000
I (128) boot: End of partition table
I (133) esp_image: segment 0: paddr=00710020 vaddr=3c110020 size=4e380h (320384) map
I (197) esp_image: segment 1: paddr=0075e3a8 vaddr=3fc9cc00 size=01c70h (  7280) load
I (199) esp_image: segment 2: paddr=00760020 vaddr=42000020 size=104d14h (1068308) map
I (392) esp_image: segment 3: paddr=00864d3c vaddr=3fc9e870 size=040e4h ( 16612) load
I (395) esp_image: segment 4: paddr=00868e28 vaddr=40374000 size=18b40h (101184) load
I (419) esp_image: segment 5: paddr=00881970 vaddr=50000000 size=00020h (    32) load
I (430) boot: Loaded app from partition at offset 0x710000
I (430) boot: Disabling RNG early entropy source...
E (442) octal_psram: PSRAM chip is not connected, or wrong PSRAM line mode
E cpu_start: Failed to init external RAM!

abort() was called at PC 0x420044ab on core 0


Backtrace: 0x4037e259:0x3fceb240 0x4037e225:0x3fceb260 0x403866da:0x3fceb280 0x420044ab:0x3fceb2f0 0x403758cd:0x3fceb310 0x403cca24:0x3fceb340 0x403cce45:0x3fceb380 0x403c8981:0x3fceb4b0 0x40045c01:0x3fceb570 0x40043ab6:0x3fceb6f0 0x40034c45:0x3fceb710


![Image](https://github.com/user-attachments/assets/33671f5d-e0b5-4fad-a286-16f1c47a82e6)

### ghost on 2026-01-16

This has the wrong ESP32 chip on it (`MON16` vs `MCN16R8`). 

Your going to be limited to v2.8.0 or v2.9.0 of the firmware you can use on it due to this.

Reach out to the seller to see if they can resolve this. 

### Thorgrlm on 2026-01-16

Hi, are you telling me there's no solution, that the chip is incompatible with the new firmware version?

### mutatrum on 2026-01-16

No, contact the seller. There have been cases the manufacturer mounted the wrong module and have fixed those in the past. Please report back what they say.

### Thorgrlm on 2026-01-20

I think the seller has ignored me, but is it really that important to upgrade the equipment? Here are my performance data,

<img width="997" height="822" alt="Image" src="https://github.com/user-attachments/assets/7ced28f4-64bc-4b38-9d32-9b8e8eb98744" />

 can the performance be improved?

### mutatrum on 2026-01-20

No, performance looks good. There have been substantial changes to the firmware and lots of new features to the dashboard, but in general the hashing performance is not changed. AFAIK v2.9.0 is the last version that will run without PSRAM, however you have to disable the statistics on the settings page, otherwise it will run out of memory. But then again, if you're happy with how it's running, it is totally fine to keep the firmware as is.

### Thorgrlm on 2026-01-20

What I'm interested in is that it participates in the Bitcoin lottery with the best possible performance. If you tell me that the performance doesn't change and that the newer firmwares only add aesthetics and some configuration, then as I have it, it's fine with me. I'm not looking at the website all day; what I want is for it to close a block and collect the reward xaxaxaxa. 
Thanks for the clarification.
