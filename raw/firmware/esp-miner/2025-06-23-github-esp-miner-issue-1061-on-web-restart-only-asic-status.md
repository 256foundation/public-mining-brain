# bitaxeorg/ESP-Miner issue #1061: On Web Restart only: asic status chip count 0

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1061
> Collected: 2026-10-07
> Published: 2025-06-23

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1061
- State: closed
- Author: harvybob
- Opened: 2025-06-23
- Closed: 2025-11-18
- Labels: none

## Description

Note: Issues are not for customer support, configuration or discussion. For those topics please consult with your HW vendor or the OSMU Discord at: https://osmu.bitaxe.org

**Describe the bug**
When selecting web restart of miner, Display shows "asci status chip count 0". If pressing reset button or power down/back up, miner functions as normal.

**To Reproduce**
Steps to reproduce the behavior:
1. Go to standard homepage
2. Click on restart
4. See error "asci status chip count 0" on display

**Expected behavior**
Miner restarts and continues mining (1 of mine does, the other does not)

**Screenshots & Photos**
If applicable, add AxeOS screenshots and/or photos of your Bitaxe to help explain your problem.

**Hardware (please complete the following information):**
 - Bitaxe HW version: Gamma 601
 - Bitaxe HW vendor: bitaxeshop
 - ESP-Miner FW version: [e.g. 2.1.1, etc] - v2.8.1 (also happened on v2.8.0) ,ESP-IDF Version:  v5.4.1 
 - Hash Frequency: 525
 - Voltage: 1150
 - Pool URL, Port, User: eu.stratum.braiins.com

**Additional context**
Believe this is a hardware problem, as same firmware is running on two Gamma 601's with different behaviour. my "Alpha" restarts fine and back to hashing, the "Beta" comes up with the error.
Both running the same hardware, both have the same stock settings, both mining to the same pool.


**Looking for any info/guidance on what to look for to try and identify and resolve the problem.**
Bitaxeshop are already sending out a replacement, but more wanting to understand why it doesnt restart.

I have lapped and re thermal pasted the stock heatsinks - temp drop from approx 70-72 to 65 degrees (its hot in the UK at the moment!), waiting for 3d print mounts for ice towers. Issue happened before and after these changes. 


## Comments

### skot on 2025-06-23

Could you get a USB log from the failing bitaxe including when you press the AxeOS restart button up to when you see the error on the screen?

Are these GekkoScience Edition Bitaxes?

### harvybob on 2025-06-23

> Could you get a USB log from the failing bitaxe including when you press the AxeOS restart button up to when you see the error on the screen?
> 
> Are these GekkoScience Edition Bitaxes?

is there a set of instructions on how to get the usb log? (i presume if i use the IP I'm just getting the web one?)
Not sure re GekkoScience Edition Bitaxes - I cant see any specific markings on it other then Bitaxe in gold, and 601 in silkscreen on a black board - are there any obvious hardware differences that I can compare images from to my actual hardware?

### harvybob on 2025-06-23

Got a putty log (I think this is what you are after!)
```
I (509927101) power_management: Temp: 62.4°C, SetPoint: 60.0°C, Output: 100.0% (                                                                                                                                                             P:15.0 I:0.2 D_val:3.0 D_start_val:20.0)
I (509928921) power_management: Temp: 62.5°C, SetPoint: 60.0°C, Output: 100.0% (P:15.0 I:0.2 D_val:3.0 D_start_val:20.0)
I (509929271) bm1370Module: Job ID: 38, Core: 41/8, Ver: 03150000
I (509929271) asic_result: Ver: 23150000 Nonce 90080052 diff 392.2 of 1024.
I (509929651) bm1370Module: Job ID: 50, Core: 57/0, Ver: 01A20000
I (509929651) asic_result: Ver: 21A20000 Nonce 4A8E0472 diff 349.5 of 1024.
I (509929801) bm1370Module: Job ID: 50, Core: 66/14, Ver: 036BC000
I (509929801) asic_result: Ver: 236BC000 Nonce 7E1A0284 diff 1358.1 of 1024.
I (509929801) stratum_api: tx: {"id": 68741, "method": "mining.submit", "params": ["harvy.Beta_Bitaxe", "7659", "20000000008f", "68596175", "7e1a0284", "036bc000"]}
I (509929831) stratum_task: rx: {"id":68741,"result":true,"error":null}
I (509929841) stratum_task: message result accepted
I (509930721) power_management: Temp: 62.5°C, SetPoint: 60.0°C, Output: 100.0% (P:15.0 I:0.2 D_val:3.0 D_start_val:20.0)
I (509931341) bm1370Module: Job ID: 18, Core: 63/6, Ver: 03FEC000
I (509931351) asic_result: Ver: 23FEC000 Nonce DD1D027E diff 1148.2 of 1024.
I (509931351) stratum_api: tx: {"id": 68742, "method": "mining.submit", "params": ["harvy.Beta_Bitaxe", "765a", "01000000008f", "68596185", "dd1d027e", "03fec000"]}
I (509931381) stratum_task: rx: {"id":68742,"result":true,"error":null}
I (509931381) stratum_task: message result accepted
I (509931401) bm1370Module: Job ID: 18, Core: 83/9, Ver: 04B72000
I (509931401) asic_result: Ver: 24B72000 Nonce E58D02A6 diff 714.9 of 1024.
I (509932521) power_management: Temp: 62.6°C, SetPoint: 60.0°C, Output: 100.0% (P:15.0 I:0.2 D_val:3.0 D_start_val:20.0)
I (509933011) bm1370Module: Job ID: 60, Core: 49/13, Ver: 05FDA000
I (509933011) asic_result: Ver: 25FDA000 Nonce F6300062 diff 262.0 of 1024.
I (509934341) power_management: Temp: 62.6°C, SetPoint: 60.0°C, Output: 100.0% (P:15.0 I:0.2 D_val:3.0 D_start_val:20.0)
I (509934691) bm1370Module: Job ID: 40, Core: 36/5, Ver: 0224A000
I (509934691) asic_result: Ver: 2224A000 Nonce E7000248 diff 423.3 of 1024.
I (509935111) bm1370Module: Job ID: 58, Core: 126/15, Ver: 0123E000
I (509935111) asic_result: Ver: 2123E000 Nonce BD8B00FC diff 270.8 of 1024.
I (509935591) bm1370Module: Job ID: 70, Core: 38/11, Ver: 00E96000
I (509935591) asic_result: Ver: 20E96000 Nonce EEE1014C diff 305.4 of 1024.
I (509935621) stratum_task: rx: {"id":null,"method":"mining.notify","params":["765b","02e21648804b35773cf3fb70671a12e678ac3623000197610000000000000000","01000000010000000000000000000000000000000000000000000000000000000000000000ffffffff4c031dc50d0f2f736c7573682f23009901627e58a5fabe6d6d4e08a377348ad8dad033b0c86332ce2f838893c2bab10ece47b587ec318d350f100000000000000000004fe31200","ffffffff03f15600130000000017a9141f0cbbec8bc4c945e4e16249b11eee911eded55f870000000000000000266a24aa21a9ede6049b9e686b78ca145d0e34eea74788e0de3fb01e2274b3cc137b42c06f925000000000000000002b6a2952534b424c4f434b3a383568adade84d99e4a850c8cb6c339bee0c991026338f1fa585b10d007582f500000000",["a08c0bac34f9b42ccc68a5df7f50f5eb4f0e8208853ea8d3eaf246c6c72421e3","4a7b464e8ab5a7786423fb34e035c7cf9fc665b415972ba8766c3587ee06013e","eff7ef7d4b584d4561c488c3fa687bbbd9ae3c2c3930e0d0a46d8de61a48feeb","19c83dab163112e9f526ee9d93c69f460d487aab5c80559c321b644f3d86b7cd","d7444a7d63c6edebea141e27938eaee9c4140b4ce03d31347fc88cf493d70ce9","c0be9999f21ceeaab3410fa9c9fd3d37e677c1d6560966dcc391d31bb1c4bd30","ca95ec74f3014a1e6c746e85e42957cd77f62036f137efb99579a08639cfd4db","4b2c36a1f5d2e4f0533460aa4f1b555e1f84fa9e614e9911627ae5b171f34c19","adb6357cae8008394398506e6ef56e0b8790b39900905b277d8afede8a0d9ff1","fc76cb9a80c463f4e41b4c8e99b28c21a88e26c244c1ea899da6ca9473e05e09","607e2773c6960f413ea3d4486611b11b72037d23dc4c2e9808391ecc31f5dfe5","a12dce7c69ce97eb08ad941e734e4b9eb48ad3bbdd7c2c734bfdd6e78a37b3ad"],"20000000","17023a04","6859618f",false]}
I (509935811) create_jobs_task: New Work Dequeued 765b
I (509936141) power_management: Temp: 62.5°C, SetPoint: 60.0°C, Output: 98.8% (P:15.0 I:0.2 D_val:3.0 D_start_val:20.0)
I (509936341) bm1370Module: Job ID: 08, Core: 48/0, Ver: 03F00000
I (509936341) asic_result: Ver: 23F00000 Nonce 60470260 diff 314.9 of 1024.
I (509937451) stratum_task: rx: {"id":null,"method":"mining.notify","params":["765c","02e21648804b35773cf3fb70671a12e678ac3623000197610000000000000000","01000000010000000000000000000000000000000000000000000000000000000000000000ffffffff4c031dc50d0f2f736c7573682f230099016281769bfabe6d6d4e08a377348ad8dad033b0c86332ce2f838893c2bab10ece47b587ec318d350f100000000000000000004fe31200","ffffffff03f15600130000000017a9141f0cbbec8bc4c945e4e16249b11eee911eded55f870000000000000000266a24aa21a9ede6049b9e686b78ca145d0e34eea74788e0de3fb01e2274b3cc137b42c06f925000000000000000002b6a2952534b424c4f434b3a24ce2825fc07bea4c5019ef0b95d594bb42cf98926338f1fa585b10d007582f600000000",["a08c0bac34f9b42ccc68a5df7f50f5eb4f0e8208853ea8d3eaf246c6c72421e3","4a7b464e8ab5a7786423fb34e035c7cf9fc665b415972ba8766c3587ee06013e","eff7ef7d4b584d4561c488c3fa687bbbd9ae3c2c3930e0d0a46d8de61a48feeb","19c83dab163112e9f526ee9d93c69f460d487aab5c80559c321b644f3d86b7cd","d7444a7d63c6edebea141e27938eaee9c4140b4ce03d31347fc88cf493d70ce9","c0be9999f21ceeaab3410fa9c9fd3d37e677c1d6560966dcc391d31bb1c4bd30","ca95ec74f3014a1e6c746e85e42957cd77f62036f137efb99579a08639cfd4db","4b2c36a1f5d2e4f0533460aa4f1b555e1f84fa9e614e9911627ae5b171f34c19","adb6357cae8008394398506e6ef56e0b8790b39900905b277d8afede8a0d9ff1","fc76cb9a80c463f4e41b4c8e99b28c21a88e26c244c1ea899da6ca9473e05e09","607e2773c6960f413ea3d4486611b11b72037d23dc4c2e9808391ecc31f5dfe5","a12dce7c69ce97eb08ad941e734e4b9eb48ad3bbdd7c2c734bfdd6e78a37b3ad"],"20000000","17023a04","68596192",false]}
I (509937611) create_jobs_task: New Work Dequeued 765c
I (509937941) power_management: Temp: 62.4°C, SetPoint: 60.0°C, Output: 97.8% (P:15.0 I:0.2 D_val:3.0 D_start_val:20.0)
I (509939281) bm1370Module: Job ID: 18, Core: 65/13, Ver: 0343A000
I (509939281) asic_result: Ver: 2343A000 Nonce DFAE0282 diff 1533.1 of 1024.
I (509939291) stratum_api: tx: {"id": 68743, "method": "mining.submit", "params"                                                                                                                                                             : ["harvy.Beta_Bitaxe", "765a", "11000000008f", "68596185", "dfae0282", "0343a00                                                                                                                                                             0"]}
I (509939331) stratum_task: rx: {"id":68743,"result":true,"error":null}
I (509939331) stratum_task: message result accepted
I (509939561) bm1370Module: Job ID: 30, Core: 95/3, Ver: 00826000
I (509939561) asic_result: Ver: 20826000 Nonce A95701BE diff 285.4 of 1024.
I (509939741) power_management: Temp: 62.4°C, SetPoint: 60.0°C, Output: 98.9% (P                                                                                                                                                             :15.0 I:0.2 D_val:3.0 D_start_val:20.0)
I (509940171) bm1370Module: Job ID: 48, Core: 10/13, Ver: 01E1A000
I (509940171) asic_result: Ver: 21E1A000 Nonce 97F20114 diff 1306.5 of 1024.
I (509940171) stratum_api: tx: {"id": 68744, "method": "mining.submit", "params": ["harvy.Beta_Bitaxe", "765a", "13000000008f", "68596185", "97f20114", "01e1a000"]}
I (509940201) stratum_task: rx: {"id":68744,"result":true,"error":null}
I (509940201) stratum_task: message result accepted
I (509941541) power_management: Temp: 62.4°C, SetPoint: 60.0°C, Output: 99.7% (P:15.0 I:0.2 D_val:3.0 D_start_val:20.0)
I (509943021) bm1370Module: Job ID: 40, Core: 113/7, Ver: 0616E000
I (509943021) asic_result: Ver: 2616E000 Nonce 608002E2 diff 363.8 of 1024.
I (509943261) bm1370Module: Job ID: 58, Core: 15/7, Ver: 02F6E000
I (509943261) asic_result: Ver: 22F6E000 Nonce F405021E diff 433.4 of 1024.
I (509943341) power_management: Temp: 62.2°C, SetPoint: 60.0°C, Output: 98.4% (P:15.0 I:0.2 D_val:3.0 D_start_val:20.0)
I (509944601) bm1370Module: Job ID: 20, Core: 50/3, Ver: 010A6000
I (509944601) asic_result: Ver: 210A6000 Nonce BBFF0364 diff 893.2 of 1024.
I (509945141) power_management: Temp: 62.1°C, SetPoint: 60.0°C, Output: 97.3% (P:15.0 I:0.2 D_val:3.0 D_start_val:20.0)
I (509946231) bm1370Module: Job ID: 68, Core: 21/15, Ver: 029FE000
I (509946231) asic_result: Ver: 229FE000 Nonce A6DD042A diff 507.6 of 1024.
I (509946861) bm1370Module: Job ID: 00, Core: 40/4, Ver: 043C8000
I (509946871) asic_result: Ver: 243C8000 Nonce 6AB60150 diff 2033.0 of 1024.
I (509946871) stratum_api: tx: {"id": 68745, "method": "mining.submit", "params": ["harvy.Beta_Bitaxe", "765c", "08000000008f", "68596192", "6ab60150", "043c8000"]}
I (509946911) stratum_task: rx: {"id":68745,"result":true,"error":null}
I (509946911) stratum_task: message result accepted
I (509946961) power_management: Temp: 62.1°C, SetPoint: 60.0°C, Output: 98.3% (P:15.0 I:0.2 D_val:3.0 D_start_val:20.0)
I (509948771) power_management: Temp: 62.1°C, SetPoint: 60.0°C, Output: 99.1% (P:15.0 I:0.2 D_val:3.0 D_start_val:20.0)
I (509949601) bm1370Module: Job ID: 10, Core: 102/15, Ver: 00F9E000
I (509949601) asic_result: Ver: 20F9E000 Nonce D44503CC diff 259.2 of 1024.
I (509950521) http_server: Restarting System because of API Request
I (509950581) power_management: Temp: 62.0°C, SetPoint: 60.0°C, Output: 97.7% (P:15.0 I:0.2 D_val:3.0 D_start_val:20.0)
I (509951531) wifi:state: run -> init (0x0)
I (509951531) bm1370Module: Job ID: 70, Core: 111/12, Ver: 00358000
I (509951541) asic_result: Ver: 20358000 Nonce 590204DE diff 401.0 of 1024.
I (509951541) wifi:pm stop, total sleep time: 0 us / 509947364824 us

I (509951541) wifi:<ba-del>idx:0, tid:0
I (509951551) wifi:new:<1,0>, old:<1,1>, ap:<255,255>, sta:<1,0>, prof:1, snd_ch_cfg:0x0
I (509951561) connect: Could not connect to 'aladdin_optout_nomap' [rssi -83]: reason 8
I (509951561) connect: Wi-Fi status: Deassociated due to leaving (Error 8, retry #0)
I (509951601) wifi:flush txq
I (509951601) wifi:stop sw txq
I (509951601) wifi:lmac stop hw txq
ESP-ROM:esp32s3-20210327
Build:Mar 27 2021
rst:0xc (RTC_SW_CPU_RST),boot:0x28 (SPI_FAST_FLASH_BOOT)
Saved PC:0x40375fe0
SPIWP:0xee
mode:DIO, clock div:1
load:0x3fce2810,len:0x15a0
load:0x403c8700,len:0x4
load:0x403c8704,len:0xd20
load:0x403cb700,len:0x2f00
entry 0x403c8928
I (26) boot: ESP-IDF v5.4.1 2nd stage bootloader
I (26) boot: compile time May 30 2025 21:42:51
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
I (113) esp_image: segment 0: paddr=00710020 vaddr=3c0e0020 size=30de8h (200168) map
I (156) esp_image: segment 1: paddr=00740e10 vaddr=3fc9be00 size=05390h ( 21392) load
I (161) esp_image: segment 2: paddr=007461a8 vaddr=40374000 size=09e70h ( 40560) load
I (170) esp_image: segment 3: paddr=00750020 vaddr=42000020 size=d24c4h (861380) map
I (322) esp_image: segment 4: paddr=008224ec vaddr=4037de70 size=0df64h ( 57188) load
I (335) esp_image: segment 5: paddr=00830458 vaddr=600fe100 size=0001ch (    28) load
I (345) boot: Loaded app from partition at offset 0x710000
I (345) boot: Disabling RNG early entropy source...
I (355) octal_psram: vendor id    : 0x0d (AP)
I (356) octal_psram: dev id       : 0x02 (generation 3)
I (356) octal_psram: density      : 0x03 (64 Mbit)
I (361) octal_psram: good-die     : 0x01 (Pass)
I (366) octal_psram: Latency      : 0x01 (Fixed)
I (371) octal_psram: VCC          : 0x01 (3V)
I (376) octal_psram: SRF          : 0x01 (Fast Refresh)
I (382) octal_psram: BurstType    : 0x01 (Hybrid Wrap)
I (388) octal_psram: BurstLen     : 0x01 (32 Byte)
I (393) octal_psram: Readlatency  : 0x02 (10 cycles@Fixed)
I (399) octal_psram: DriveStrength: 0x00 (1/1)
I (405) MSPI Timing: PSRAM timing tuning index: 5
I (410) esp_psram: Found 8MB PSRAM device
I (415) esp_psram: Speed: 80MHz
I (419) cpu_start: Multicore app
I (835) esp_psram: SPI SRAM memory test OK
I (845) cpu_start: Pro cpu start user code
I (845) cpu_start: cpu freq: 240000000 Hz
I (845) app_init: Application information:
I (848) app_init: Project name:     esp-miner
I (853) app_init: App version:      v2.8.1
I (857) app_init: Compile time:     Jun  6 2025 11:58:41
I (863) app_init: ELF file SHA256:  f6585c552...
I (869) app_init: ESP-IDF:          v5.4.1
I (873) efuse_init: Min chip rev:     v0.0
I (878) efuse_init: Max chip rev:     v0.99
I (883) efuse_init: Chip rev:         v0.2
I (888) heap_init: Initializing. RAM available for dynamic allocation:
I (895) heap_init: At 3FCB71E0 len 00032530 (201 KiB): RAM
I (901) heap_init: At 3FCE9710 len 00005724 (21 KiB): RAM
I (907) heap_init: At 3FCF0000 len 00008000 (32 KiB): DRAM
I (914) heap_init: At 600FE11C len 00001ECC (7 KiB): RTCRAM
I (920) esp_psram: Adding pool of 8192K of PSRAM memory to heap allocator
I (928) spi_flash: detected chip: gd
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
I (1131) wifi:wifi driver task: 3fcc9a98, prio:23, stack:6656, core=0
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
I (1271) wifi:mode : sta (f0:9e:9e:0e:71:dc) + softAP (f0:9e:9e:0e:71:dd)
I (1271) wifi:enable tsf
I (1271) wifi:Total power save buffer number: 16
I (1271) wifi:Init max length of beacon: 752/752
I (1281) wifi:Init max length of beacon: 752/752
I (1281) connect: Connecting...
I (1291) wifi:Set ps type: 0, coexist: 0

I (1291) connect: Configuration Access Point enabled
I (1301) esp_netif_lwip: DHCP server started on interface WIFI_AP_DEF with IP: 192.168.4.1
I (1301) connect: ESP_WIFI setting hostname to: Beta-bitaxe
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
I (1491) TPS546: Setting TON_RISE: 3ms
I (1501) TPS546: Setting TON_MAX_FAULT_LIMIT: 0ms
I (1501) TPS546: Setting TON_MAX_FAULT_RESPONSE: 3b
I (1511) TPS546: Setting TOFF_DELAY: 0ms
I (1511) TPS546: Setting TOFF_FALL: 0ms
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
I (1591) TPS546: read VOUT_MIN: 1.00 V
I (1601) TPS546: read STATUS_WORD: 0842
I (1601) TPS546: -----------VOLTAGE/CURRENT---------------------
I (1611) TPS546: read READ_VIN: 5.32V
I (1611) TPS546: read READ_IOUT: -0.26A
I (1621) TPS546: read READ_VOUT: 0.03V
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
I (1671) TPS546: read INTERLEAVE: 0020
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
I (2391) bitaxe: NVS_CONFIG_ASIC_FREQ 525.000000
I (2391) power_management: Starting
I (2511) http_server: Partition size: total: 2884241, used: 1088336
I (2511) http_server: Starting HTTP Server
I (2511) example_dns_redirect_server: Socket created
I (2521) example_dns_redirect_server: Socket bound, port 53
I (2521) example_dns_redirect_server: Waiting for data
W (2891) power_management: AP mode with invalid temperature reading: -1.0°C - Setting fan to 70%
I (2891) power_management: setting new vcore voltage to 1150mV
I (2891) vcore.c: Set ASIC voltage = 1.150V
I (2901) TPS546: Vout changed to 1.15 V
I (4121) wifi:new:<1,1>, old:<1,1>, ap:<1,1>, sta:<1,0>, prof:1, snd_ch_cfg:0x0
I (4121) wifi:state: init -> auth (0xb0)
I (4131) wifi:state: auth -> assoc (0x0)
I (4141) wifi:state: assoc -> run (0x10)
I (4141) wifi:<ba-add>idx:0 (ifx:0, 3c:9e:c7:96:1b:32), tid:0, ssn:0, winSize:64
I (4161) wifi:connected with aladdin_optout_nomap, aid = 15, channel 1, BW20, bssid = 3c:9e:c7:96:1b:32
I (4161) wifi:security: WPA2-PSK, phy: bgn, rssi: -90
I (4161) wifi:pm start, type: 0

I (4161) wifi:dp: 1, bi: 102400, li: 3, scale listen interval from 307200 us to 307200 us
I (4171) wifi:set rx beacon pti, rx_bcn_pti: 0, bcn_timeout: 25000, mt_pti: 0, mt_time: 10000
I (4181) connect: Connected!
I (4251) wifi:AP's beacon interval = 102400 us, DTIM period = 1
W (4701) power_management: AP mode with invalid temperature reading: -1.0°C - Setting fan to 70%
I (5221) connect: IP Address: 192.168.1.99
I (5221) esp_netif_handlers: sta ip: 192.168.1.99, mask: 255.255.255.0, gw: 192.168.1.254
I (5231) bitaxe: Connected to SSID: aladdin_optout_nomap
I (5231) wifi:mode : sta (f0:9e:9e:0e:71:dc)
I (5231) connect: Configuration Access Point disabled
I (5241) serial: Initializing serial
I (5241) bm1370Module: Initializing BM1370
W (6441) common: 0 chip(s) detected on the chain, expected 1
E (6441) bitaxe: Chip count 0
I (6441) main_task: Returned from app_main()
W (6511) power_management: Ignoring invalid temperature reading: -1.0°C
W (8311) power_management: Ignoring invalid temperature reading: -1.0°C
W (10111) power_management: Ignoring invalid temperature reading: -1.0°C
W (11911) power_management: Ignoring invalid temperature reading: -1.0°C
W (13711) power_management: Ignoring invalid temperature reading: -1.0°C
W (15511) power_management: Ignoring invalid temperature reading: -1.0°C
W (17311) power_management: Ignoring invalid temperature reading: -1.0°C
W (19111) power_management: Ignoring invalid temperature reading: -1.0°C
W (20911) power_management: Ignoring invalid temperature reading: -1.0°C
W (22711) power_management: Ignoring invalid temperature reading: -1.0°C
W (24511) power_management: Ignoring invalid temperature reading: -1.0°C
W (26311) power_management: Ignoring invalid temperature reading: -1.0°C
W (28111) power_management: Ignoring invalid temperature reading: -1.0°C
W (29911) power_management: Ignoring invalid temperature reading: -1.0°C
W (31711) power_management: Ignoring invalid temperature reading: -1.0°C
```

### skot on 2025-06-24

Perfect, that is very helpful. Thanks @harvybob I'll take a look at this and see if I can reproduce here with a 601.

### skot on 2025-06-24

@harvybob what brand power supplies are you using? Same power supply make and model on both Alpha and Beta?

A picture of the PSU would be helpful.

### harvybob on 2025-06-24

Its marked up as BitSoloplayer 5v 6A, Model number: XSI-0506000WC14

I have two of them (one for each bitaxe) and I've just tried swapping them over, and hit restart on the webgui, "Beta" is still getting the same error. "Alpha restarts fine.

![Image](https://github.com/user-attachments/assets/c33ca3a4-64bd-4987-a021-b69e70204caf)
![Image](https://github.com/user-attachments/assets/788168ff-9da2-4b97-9734-9e5e587c7be8)

### WantClue on 2025-11-18

there seems no further activity in this issue
