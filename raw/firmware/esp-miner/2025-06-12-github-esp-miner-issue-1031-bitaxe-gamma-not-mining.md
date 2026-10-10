# bitaxeorg/ESP-Miner issue #1031: Bitaxe Gamma not mining

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1031
> Collected: 2026-10-07
> Published: 2025-06-12

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1031
- State: closed
- Author: vekexasia
- Opened: 2025-06-12
- Closed: 2025-06-12
- Labels: none

## Description

I am using a bitaxe gamma and cant understand the reason why it does not mine.


This is the log

```
I (26) boot: ESP-IDF v5.4.1-dirty 2nd stage bootloader
I (26) boot: compile time May  5 2025 23:04:07
I (26) boot: Multicore bootloader
I (27) boot: chip revision: v0.2
I (30) boot: efuse block revision: v1.3
I (33) boot.esp32s3: Boot SPI Speed : 80MHz
I (37) boot.esp32s3: SPI Mode       : DIO
I (41) boot.esp32s3: SPI Flash Size : 16MB
I (45) boot: Enabling RNG early entropy source...
I (49) boot: Partition Table:
I (52) boot: ## Label            Usage          Type ST Offset   Length
I (58) boot:  0 nvs              WiFi data        01 02 00009000 00006000
I (65) boot:  1 phy_init         RF data          01 01 0000f000 00001000
I (71) boot:  2 factory          factory app      00 00 00010000 00400000
I (78) boot:  3 www              Unknown data     01 82 00410000 00300000
I (84) boot:  4 ota_0            OTA app          00 10 00710000 00400000
I (91) boot:  5 ota_1            OTA app          00 11 00b10000 00400000
I (97) boot:  6 otadata          OTA data         01 00 00f10000 00002000
I (104) boot:  7 coredump         Unknown data     01 03 00f12000 00010000
I (110) boot: End of partition table
I (114) esp_image: segment 0: paddr=00710020 vaddr=3c0e0020 size=30278h (197240) map
I (156) esp_image: segment 1: paddr=007402a0 vaddr=3fc9be00 size=05390h ( 21392) load
I (161) esp_image: segment 2: paddr=00745638 vaddr=40374000 size=0a9e0h ( 43488) load
I (171) esp_image: segment 3: paddr=00750020 vaddr=42000020 size=d1cd4h (859348) map
I (323) esp_image: segment 4: paddr=00821cfc vaddr=4037e9e0 size=0d3f4h ( 54260) load
I (335) esp_image: segment 5: paddr=0082f0f8 vaddr=600fe100 size=0001ch (    28) load
I (344) boot: Loaded app from partition at offset 0x710000
I (345) boot: Disabling RNG early entropy source...
I (355) octal_psram: vendor id    : 0x0d (AP)
I (355) octal_psram: dev id       : 0x02 (generation 3)
I (356) octal_psram: density      : 0x03 (64 Mbit)
I (360) octal_psram: good-die     : 0x01 (Pass)
I (365) octal_psram: Latency      : 0x01 (Fixed)
I (371) octal_psram: VCC          : 0x01 (3V)
I (376) octal_psram: SRF          : 0x01 (Fast Refresh)
I (382) octal_psram: BurstType    : 0x01 (Hybrid Wrap)
I (387) octal_psram: BurstLen     : 0x01 (32 Byte)
I (393) octal_psram: Readlatency  : 0x02 (10 cycles@Fixed)
I (399) octal_psram: DriveStrength: 0x00 (1/1)
I (405) MSPI Timing: PSRAM timing tuning index: 5
I (410) esp_psram: Found 8MB PSRAM device
I (414) esp_psram: Speed: 80MHz
I (418) cpu_start: Multicore app
I (835) esp_psram: SPI SRAM memory test OK
I (844) cpu_start: Pro cpu start user code
I (844) cpu_start: cpu freq: 240000000 Hz
I (844) app_init: Application information:
I (847) app_init: Project name:     esp-miner
I (852) app_init: App version:      4457296
I (857) app_init: Compile time:     Jun  4 2025 10:51:01
I (863) app_init: ELF file SHA256:  3bf993d19...
I (868) app_init: ESP-IDF:          v5.4.1
I (873) efuse_init: Min chip rev:     v0.0
I (878) efuse_init: Max chip rev:     v0.99
I (883) efuse_init: Chip rev:         v0.2
I (888) heap_init: Initializing. RAM available for dynamic allocation:
I (895) heap_init: At 3FCB71E0 len 00032530 (201 KiB): RAM
I (901) heap_init: At 3FCE9710 len 00005724 (21 KiB): RAM
I (907) heap_init: At 3FCF0000 len 00008000 (32 KiB): DRAM
I (913) heap_init: At 600FE11C len 00001ECC (7 KiB): RTCRAM
I (919) esp_psram: Adding pool of 8192K of PSRAM memory to heap allocator
I (928) spi_flash: detected chip: generic
I (931) spi_flash: flash io: dio
I (936) sleep_gpio: Configure to isolate all GPIO pins in sleep state
I (943) sleep_gpio: Enable automatic switching of GPIO sleep configuration
I (951) main_task: Started on CPU0
I (961) esp_psram: Reserving pool of 32K of internal memory for DMA/internal allocations
I (961) main_task: Calling app_main()
I (971) bitaxe: Welcome to the bitaxe - FOSS || GTFO!
I (971) bitaxe: I2C initialized successfully
I (1081) ADC: calibration scheme version is Curve Fitting
I (1081) ADC: Calibration Success
I (1101) device_config: Device Model: Gamma
I (1101) device_config: Board Version: 601
I (1101) device_config: ASIC: 1x BM1370 (128 cores)
I (1101) SystemModule: Initial overheat_mode value: 0
I (1111) pp: pp rom version: e7ae62f
I (1111) net80211: net80211 rom version: e7ae62f
I (1131) wifi:wifi driver task: 3fcc9b64, prio:23, stack:6656, core=0
I (1131) wifi:wifi firmware version: 79fa3f41ba
I (1141) wifi:wifi certification version: v7.0
I (1141) wifi:config NVS flash: enabled
I (1141) wifi:config nano formatting: disabled
I (1141) wifi:Init data frame dynamic rx buffer num: 32
I (1151) wifi:Init static rx mgmt buffer num: 5
I (1151) wifi:Init management short buffer num: 32
I (1151) wifi:Init dynamic tx buffer num: 32
I (1161) wifi:Init static tx FG buffer num: 2
I (1161) wifi:Init static rx buffer size: 1600
I (1171) wifi:Init static rx buffer num: 10
I (1171) wifi:Init dynamic rx buffer num: 32
I (1171) wifi_init: rx ba win: 6
I (1181) wifi_init: accept mbox: 6
I (1181) wifi_init: tcpip mbox: 32
I (1191) wifi_init: udp mbox: 6
I (1191) wifi_init: tcp mbox: 6
I (1191) wifi_init: tcp tx win: 5760
I (1201) wifi_init: tcp rx win: 5760
I (1201) wifi_init: tcp mss: 1440
I (1211) wifi_init: WiFi IRAM OP enabled
I (1211) wifi_init: WiFi RX IRAM OP enabled
I (1231) connect: ESP_WIFI_MODE_STA
I (1231) connect: Wi-Fi Password provided, using WPA2
I (1231) connect: wifi_init_sta finished.
I (1231) phy_init: phy_version 700,8582a7fd,Feb 10 2025,20:13:11
I (1271) wifi:mode : sta (30:ed:a0:1d:95:40) + softAP (30:ed:a0:1d:95:41)
I (1271) wifi:enable tsf
I (1271) wifi:Total power save buffer number: 16
I (1271) wifi:Init max length of beacon: 752/752
I (1281) wifi:Init max length of beacon: 752/752
I (1281) connect: Connecting...
I (1291) wifi:Set ps type: 0, coexist: 0

I (1291) connect: Configuration Access Point enabled
I (1301) esp_netif_lwip: DHCP server started on interface WIFI_AP_DEF with IP: 192.168.4.1
I (1311) connect: ESP_WIFI setting hostname to: bitaxe
I (1311) connect: wifi_init_sta finished.
I (1321) TPS546: Initializing the core voltage regulator
I (1321) TPS546: Device ID: 54 49 54 6d 24 41
I (1331) TPS546: Power config-OPERATION: 00
I (1331) TPS546: Power config-ON_OFF_CONFIG: 1F
I (1341) TPS546: Reading MFR info
I (1341) TPS546: MFR_ID: 00 00 00
I (1341) TPS546: MFR_MODEL: 00 00 00
I (1351) TPS546: MFR_REVISION: 00 00 00
I (1351) TPS546: Writing new config values
I (1361) TPS546: VOUT_MODE: 97
I (1361) TPS546: ---Writing new config values to TPS546---
I (1371) TPS546: Setting PHASE: 00
I (1371) TPS546: Setting FREQUENCY: 650MHz
I (1381) TPS546: Setting VIN_ON: 4.80V
I (1381) TPS546: Setting VIN_OFF: 4.50V
I (1391) TPS546: Setting VIN_OV_FAULT_LIMIT: 6.50V
I (1391) TPS546: Setting VIN_OV_FAULT_RESPONSE: B7
I (1401) TPS546: Setting VOUT SCALE: 0.25
I (1401) TPS546: Setting VOUT_COMMAND: 1.20V
I (1411) TPS546: Setting VOUT_MAX: 2.00V
I (1411) TPS546: Setting VOUT_MIN: 1.00V
I (1421) TPS546: Setting VOUT_OV_FAULT_LIMIT: 1.25
I (1421) TPS546: Setting VOUT_OV_WARN_LIMIT: 1.16
I (1431) TPS546: Setting VOUT_MARGIN_HIGH: 1.10
I (1431) TPS546: Setting VOUT_MARGIN_LOW: 0.90
I (1441) TPS546: Setting VOUT_UV_WARN_LIMIT: 0.90
I (1441) TPS546: Setting VOUT_UV_FAULT_LIMIT: 0.75
I (1451) TPS546: ----- IOUT
I (1451) TPS546: Setting IOUT_OC_WARN_LIMIT: 25.00A
I (1461) TPS546: Setting IOUT_OC_FAULT_LIMIT: 30.00A
I (1461) TPS546: Setting IOUT_OC_FAULT_RESPONSE: c0
I (1471) TPS546: ----- TEMPERATURE
I (1471) TPS546: Setting OT_WARN_LIMIT: 105C
I (1481) TPS546: Setting OT_FAULT_LIMIT: 145C
I (1481) TPS546: Setting OT_FAULT_RESPONSE: ff
I (1491) TPS546: ----- TIMING
I (1491) TPS546: Setting TON_DELAY: 0ms
I (1501) TPS546: Setting TON_RISE: 3ms
I (1501) TPS546: Setting TON_MAX_FAULT_LIMIT: 0ms
I (1511) TPS546: Setting TON_MAX_FAULT_RESPONSE: 3b
I (1511) TPS546: Setting TOFF_DELAY: 0ms
I (1521) TPS546: Setting TOFF_FALL: 0ms
I (1521) TPS546: Setting PIN_DETECT_OVERRIDE
I (1521) TPS546: -----------VOLTAGE---------------------
I (1531) TPS546: read VIN_ON: 4.80V
I (1531) TPS546: read VIN_OFF: 4.50V
I (1541) TPS546: read VIN_OV_FAULT_LIMIT: 6.50V
I (1541) TPS546: read VIN_UV_WARN_LIMIT: 2.50V
I (1551) TPS546: read VIN_OV_FAULT_RESPONSE: B7
I (1551) TPS546: read VOUT_MAX: 2.00V
I (1561) TPS546: read VOUT_OV_FAULT_LIMIT: 1.50V
I (1561) TPS546: read VOUT_OV_WARN_LIMIT: 1.39V
I (1571) TPS546: read VOUT_MARGIN_HIGH: 1.32V
I (1571) TPS546: read VOUT_COMMAND: 1.20V
I (1581) TPS546: read VOUT_MARGIN_LOW: 1.08V
I (1581) TPS546: read VOUT_UV_WARN_LIMIT: 1.08V
I (1591) TPS546: read VOUT_UV_FAULT_LIMIT: 0.90V
I (1601) TPS546: read VOUT_MIN: 1.00 V
I (1601) TPS546: read STATUS_WORD: 0840
I (1601) TPS546: -----------VOLTAGE/CURRENT---------------------
I (1611) TPS546: read READ_VIN: 5.45V
I (1611) TPS546: read READ_IOUT: -0.36A
I (1621) TPS546: read READ_VOUT: 0.02V
I (1621) TPS546: -----------TIMING---------------------
I (1631) TPS546: read TON_DELAY: 0ms
I (1631) TPS546: read TON_RISE: 3ms
I (1641) TPS546: read TON_MAX_FAULT_LIMIT: 0ms
I (1641) TPS546: read TON_MAX_FAULT_RESPONSE: 3b
I (1651) TPS546: read TOFF_DELAY: 0ms
I (1651) TPS546: read TOFF_FALL: 0ms
I (1661) TPS546: ---------CONFIG--------------------
I (1661) TPS546: read PHASE: 00
I (1671) TPS546: read STACK_CONFIG: 0000
I (1671) TPS546: read SYNC_CONFIG: f0
I (1681) TPS546: read INTERLEAVE: 0020
I (1681) TPS546: read CAPABILITY: d0
I (1681) TPS546: ---------OPERATION------------------
I (1691) TPS546: read OPERATION: 00
I (1691) TPS546: read ON_OFF_CONFIG: 1f
I (1701) TPS546: read COMPENSATION CONFIG
I (1701) TPS546: 13 11 08 19 04
I (1711) TPS546: Clearing faults
I (1711) TPS546: read STATUS_WORD: 0840
I (1721) vcore.c: Set ASIC voltage = 1.150V
I (1721) TPS546: Vout changed to 1.15 V
I (1721) thermal: Initializing EMC2101 (Temperature offset: 0C)
I (1731) thermal: EMC2101 configuration: Ideality Factor: 24, Beta Compensation: 00
I (2241) SystemModule: Existing overheat_mode value: 0
I (2241) display: SSD1306 (128x32)
I (2241) display: Install panel IO
I (2241) display: Install panel driver
I (2241) display: Initialize LVGL
I (2251) LVGL: Starting LVGL task
I (2371) display: Display init success!
I (2371) input: Install button driver
I (2371) gpio: GPIO[0]| InputEn: 1| OutputEn: 0| OpenDrain: 0| Pullup: 1| Pulldown: 0| Intr:3
I (2391) bitaxe: NVS_CONFIG_ASIC_FREQ 636.000000
I (2391) power_management: Starting
I (2511) http_server: Partition size: total: 2884241, used: 1088336
I (2511) http_server: Starting HTTP Server
I (2521) example_dns_redirect_server: Socket created
I (2521) example_dns_redirect_server: Socket bound, port 53
I (2531) example_dns_redirect_server: Waiting for data
I (2891) power_management: setting new vcore voltage to 1150mV
I (2891) vcore.c: Set ASIC voltage = 1.150V
I (2891) TPS546: Vout changed to 1.15 V
I (4121) wifi:ap channel adjust o:1,1 n:6,2
I (4121) wifi:new:<6,0>, old:<1,1>, ap:<6,2>, sta:<6,0>, prof:1, snd_ch_cfg:0x0
I (4121) wifi:state: init -> auth (0xb0)
I (5141) wifi:state: auth -> init (0x200)
I (5151) wifi:new:<6,0>, old:<6,0>, ap:<6,2>, sta:<6,0>, prof:1, snd_ch_cfg:0x0
I (5151) wifi:new:<6,2>, old:<6,0>, ap:<6,2>, sta:<6,0>, prof:1, snd_ch_cfg:0x0
I (5151) wifi:state: init -> auth (0xb0)
I (5161) wifi:state: auth -> assoc (0x0)
I (5171) wifi:state: assoc -> run (0x10)
I (5211) wifi:security: WPA2-PSK, phy: bgn, rssi: -77
I (5211) wifi:pm start, type: 0

I (5211) wifi:dp: 1, bi: 102400, li: 3, scale listen interval from 307200 us to 307200 us
I (5221) wifi:set rx beacon pti, rx_bcn_pti: 0, bcn_timeout: 25000, mt_pti: 0, mt_time: 10000
I (5231) connect: Connected!
I (5241) wifi:<ba-add>idx:0 (ifx:0, 72:d7:9a:1a:c8:55), tid:6, ssn:2, winSize:64
I (5271) wifi:AP's beacon interval = 102400 us, DTIM period = 1
I (5491) wifi:<ba-add>idx:1 (ifx:0, 72:d7:9a:1a:c8:55), tid:0, ssn:0, winSize:64

I (6331) connect: Configuration Access Point disabled
I (6341) serial: Initializing serial
I (6341) bm1370Module: Initializing BM1370
I (6541) common: Chip 0 detected: CORE_NUM: 0x00 ADDR: 0x00
I (7541) bm1370Module: Setting ASIC difficulty mask to 255
I (7541) bm1370Module: Ramping up frequency from 56.25 MHz to 636.00 MHz
I (7541) bm1370Module: Setting Frequency to 62.50MHz (62.50)
I (7641) bm1370Module: Setting Frequency to 68.75MHz (68.75)
I (7741) bm1370Module: Setting Frequency to 75.00MHz (75.00)
I (7841) bm1370Module: Setting Frequency to 81.25MHz (81.43)
I (7941) bm1370Module: Setting Frequency to 87.50MHz (87.50)
I (8041) bm1370Module: Setting Frequency to 93.75MHz (93.75)
I (8141) bm1370Module: Setting Frequency to 100.00MHz (100.00)
I (8241) bm1370Module: Setting Frequency to 106.25MHz (106.25)
I (8341) bm1370Module: Setting Frequency to 112.50MHz (112.50)
I (8441) bm1370Module: Setting Frequency to 118.75MHz (119.05)
I (8541) bm1370Module: Setting Frequency to 125.00MHz (125.00)
I (8641) bm1370Module: Setting Frequency to 131.25MHz (131.55)
I (8741) bm1370Module: Setting Frequency to 137.50MHz (137.50)
I (8841) bm1370Module: Setting Frequency to 143.75MHz (143.75)
I (8941) bm1370Module: Setting Frequency to 150.00MHz (150.00)
I (9041) bm1370Module: Setting Frequency to 156.25MHz (156.25)
I (9141) bm1370Module: Setting Frequency to 162.50MHz (162.50)
I (9241) bm1370Module: Setting Frequency to 168.75MHz (168.75)
I (9341) bm1370Module: Setting Frequency to 175.00MHz (175.00)
I (9441) bm1370Module: Setting Frequency to 181.25MHz (181.25)
I (9541) bm1370Module: Setting Frequency to 187.50MHz (187.50)
I (9641) bm1370Module: Setting Frequency to 193.75MHz (193.75)
I (9741) bm1370Module: Setting Frequency to 200.00MHz (200.00)
I (9841) bm1370Module: Setting Frequency to 206.25MHz (206.25)
I (9941) bm1370Module: Setting Frequency to 212.50MHz (212.50)
I (10041) bm1370Module: Setting Frequency to 218.75MHz (218.75)
I (10141) bm1370Module: Setting Frequency to 225.00MHz (225.00)
I (10241) bm1370Module: Setting Frequency to 231.25MHz (231.25)
I (10341) bm1370Module: Setting Frequency to 237.50MHz (237.50)
I (10441) bm1370Module: Setting Frequency to 243.75MHz (243.75)
I (10541) bm1370Module: Setting Frequency to 250.00MHz (250.00)
I (10641) bm1370Module: Setting Frequency to 256.25MHz (256.25)
I (10741) bm1370Module: Setting Frequency to 262.50MHz (262.50)
I (10841) bm1370Module: Setting Frequency to 268.75MHz (268.75)
I (10941) bm1370Module: Setting Frequency to 275.00MHz (275.00)
I (11041) bm1370Module: Setting Frequency to 281.25MHz (281.25)
I (11141) bm1370Module: Setting Frequency to 287.50MHz (287.50)
I (11241) bm1370Module: Setting Frequency to 293.75MHz (294.64)
I (11341) bm1370Module: Setting Frequency to 300.00MHz (300.00)
I (11441) bm1370Module: Setting Frequency to 306.25MHz (307.14)
I (11541) bm1370Module: Setting Frequency to 312.50MHz (312.50)
I (11641) bm1370Module: Setting Frequency to 318.75MHz (319.64)
I (11741) bm1370Module: Setting Frequency to 325.00MHz (325.00)
I (11841) bm1370Module: Setting Frequency to 331.25MHz (332.14)
I (11941) bm1370Module: Setting Frequency to 337.50MHz (337.50)
I (12041) bm1370Module: Setting Frequency to 343.75MHz (344.64)
I (12141) bm1370Module: Setting Frequency to 350.00MHz (350.00)
I (12241) bm1370Module: Setting Frequency to 356.25MHz (357.14)
I (12341) bm1370Module: Setting Frequency to 362.50MHz (362.50)
I (12441) bm1370Module: Setting Frequency to 368.75MHz (369.64)
I (12541) bm1370Module: Setting Frequency to 375.00MHz (375.00)
I (12641) bm1370Module: Setting Frequency to 381.25MHz (382.14)
I (12741) bm1370Module: Setting Frequency to 387.50MHz (387.50)
I (12841) bm1370Module: Setting Frequency to 393.75MHz (394.64)
I (12871) http_server: File sending complete
I (12941) bm1370Module: Setting Frequency to 400.00MHz (400.00)
I (13041) bm1370Module: Setting Frequency to 406.25MHz (407.14)
I (13141) bm1370Module: Setting Frequency to 412.50MHz (412.50)
I (13241) bm1370Module: Setting Frequency to 418.75MHz (419.64)
I (13341) bm1370Module: Setting Frequency to 425.00MHz (425.00)
I (13441) bm1370Module: Setting Frequency to 431.25MHz (431.25)
I (13541) bm1370Module: Setting Frequency to 437.50MHz (437.50)
I (13641) bm1370Module: Setting Frequency to 443.75MHz (443.75)
I (13741) bm1370Module: Setting Frequency to 450.00MHz (450.00)
I (13841) bm1370Module: Setting Frequency to 456.25MHz (456.25)
I (13941) bm1370Module: Setting Frequency to 462.50MHz (462.50)
I (14041) bm1370Module: Setting Frequency to 468.75MHz (468.75)
I (14141) bm1370Module: Setting Frequency to 475.00MHz (475.00)
I (14241) bm1370Module: Setting Frequency to 481.25MHz (481.25)
I (14341) bm1370Module: Setting Frequency to 487.50MHz (487.50)
I (14441) bm1370Module: Setting Frequency to 493.75MHz (493.75)
I (14541) bm1370Module: Setting Frequency to 500.00MHz (500.00)
I (14641) bm1370Module: Setting Frequency to 506.25MHz (506.25)
I (14741) bm1370Module: Setting Frequency to 512.50MHz (512.50)
I (14841) bm1370Module: Setting Frequency to 518.75MHz (518.75)
I (14941) bm1370Module: Setting Frequency to 525.00MHz (525.00)
I (15041) bm1370Module: Setting Frequency to 531.25MHz (531.25)
I (15141) bm1370Module: Setting Frequency to 537.50MHz (537.50)
I (15241) bm1370Module: Setting Frequency to 543.75MHz (543.75)
I (15341) bm1370Module: Setting Frequency to 550.00MHz (550.00)
I (15441) bm1370Module: Setting Frequency to 556.25MHz (556.25)
I (15541) bm1370Module: Setting Frequency to 562.50MHz (562.50)
I (15641) bm1370Module: Setting Frequency to 568.75MHz (568.75)
I (15741) bm1370Module: Setting Frequency to 575.00MHz (575.00)
I (15841) bm1370Module: Setting Frequency to 581.25MHz (581.25)
I (15941) bm1370Module: Setting Frequency to 587.50MHz (587.50)
I (16041) bm1370Module: Setting Frequency to 593.75MHz (593.75)
I (16141) bm1370Module: Setting Frequency to 600.00MHz (600.00)
I (16241) bm1370Module: Setting Frequency to 606.25MHz (606.25)
I (16341) bm1370Module: Setting Frequency to 612.50MHz (612.50)
I (16441) bm1370Module: Setting Frequency to 618.75MHz (618.75)
I (16541) bm1370Module: Setting Frequency to 625.00MHz (625.00)
I (16641) bm1370Module: Setting Frequency to 631.25MHz (631.25)
I (16741) bm1370Module: Setting Frequency to 636.00MHz (635.71)
I (16841) bm1370Module: Setting Frequency to 636.00MHz (635.71)
I (16841) frequency_transition: Successfully transitioned ASIC type 1370 to 636.00 MHz
I (16841) bm1370Module: Setting max baud of 1000000
I (16851) serial: Changing UART baud to 1000000
I (16851) stratum_task: Opening connection to pool: eu.stratum.braiins.com:3333
I (16851) stratum_task: Starting heartbeat thread for primary pool: eu.stratum.braiins.com:3333
I (16861) ASIC_task: ASIC Job Interval: 500.00 ms
I (16871) stratum_task: Connecting to: stratum+tcp://eu.stratum.braiins.com:3333 (164.92.209.20)
I (16871) ASIC_task: ASIC Ready!
I (16891) stratum_task: Socket created, connecting to 164.92.209.20:3333
I (16861) statistics_task: Starting
I (16901) statistics_task: Disabled!
I (16861) main_task: Returned from app_main()
I (16951) stratum_task: Resetting stratum uid
I (16951) stratum_task: Clean Jobs: clearing queue
I (16951) stratum_api: tx: {"id": 1, "method": "mining.configure", "params": [["version-rolling"], {"version-rolling.mask": "ffffffff"}]}?
```

## Comments

### vekexasia on 2025-06-12

I also tried with a bench psu to set exactly 5.0v (because i saw the original PSU had some high voltage).

nothing has changed. bench psu reports ~0.2A of consumption after startup. Briefly after API reset i can see bench psu reporting 4.5 AMP of current being used but that lasts only a split second.

I noticed that within the webinterface the ASIC voltage is being reported to be 0. But i am not sure if that is intended or not.



### skot on 2025-06-12

Hi there, I'm sorry you are having trouble with your Bitaxe. This is not a tech support forum. You can contact the seller where you purchased the Bitaxe for support, or if you built it yourself ask on the OSMU Discord. https://osmu.xyz
