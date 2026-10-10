# bitaxeorg/ESP-Miner issue #588: TPS546-based Bitaxe; 0 GH/s hash rate, pulling only 5 W of power. Restart does not always fix.

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/588
> Collected: 2026-10-07
> Published: 2024-12-18

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 588
- State: closed
- Author: ParkaMark
- Opened: 2024-12-18
- Closed: 2025-04-11
- Labels: bug, accepted, critical

## Description

**Describe the bug**
Compared to BM1366 and BM1368 miners, I am encountering a weird behaviour where BM1370 miners are falling into a state showing a 0 GH/s hash rate, pulling only 5 W of power. I have noticed this does happen from time to time (for reasons I do not fully know) but I have been able to fix the problem by calling the `/api/system/restart` API end point which sends the device for a reboot.

If this happens with my BM1366 or BM1368 miners, they normally come back and begin mining again after being restarted. However, with my BM1370 miners, this does not fix the problem and they continue to not mine. The only way to resolve this issue is a total power cycle of the miner.

I'm speculating that there is some fundamental hardware difference and thus behaviour with the BM1370 which the existing code is not accounting for so it would be great to get some feedback and traction on this bug.

**Expected behavior**
I expect a POST to `/api/system/restart` to restart the miner and restore mining on BM1370 devices, but mining does not restart after the device has restarted. The same behaviour is observed when using a browser and clicking on the restart button within the miner's website.

**Screenshots & Photos**
Here is a dump of the output of my management BASH script showing 3 miners that are currently not mining, and 2 that are.

```
http://bm1370-0  	25 °C	 5 W	 50 %	   0 GH/s	 601 @ v2.4.2	BM1370 @ 550 MHz	1.00 cV @ 0.00 aV	ota_1
http://bm1370-1  	56 °C	16 W	 50 %	 810 GH/s	 601 @ v2.4.2	BM1370 @ 550 MHz	1.00 cV @ 0.99 aV	ota_1
http://bm1370-2  	65 °C	17 W	 50 %	 782 GH/s	 601 @ v2.4.2	BM1370 @ 550 MHz	1.00 cV @ 0.97 aV	ota_1
http://bm1370-3  	28 °C	 5 W	 50 %	   0 GH/s	 601 @ v2.4.2	BM1370 @ 550 MHz	1.00 cV @ 0.00 aV	ota_1
http://bm1370-4  	26 °C	 5 W	 50 %	   0 GH/s	 601 @ v2.4.2	BM1370 @ 550 MHz	1.00 cV @ 0.00 aV	ota_1
```

**Hardware (please complete the following information):**
See above.

## Comments

### MyOwn2C on 2024-12-18

I reported the same issue #544 

A warm restart doesn’t get it to work again. 
I had to power off completely, then power on again to make it work. 

### skot on 2024-12-18

how often is your script polling the bitaxe API? do you see any change if you stop it?


### skot on 2024-12-18

If you could collect the USB logs from boot when this happens, that would be great. I haven't been able to reproduce this on my bitaxeGamma

### ParkaMark on 2024-12-18

> how often is your script polling the bitaxe API? do you see any change if you stop it?

Hourly at most. I'd have to check and get back to you about stopping the polling but I don't see how hourly polling would be a problem.

Will try and grab USB logs but not something I've done before. I have managed to do a comparison just now on the logs in the UI and this is what that looks like, with filtering for `jobs` lines.

```
₿ (14251) create_jobs_task: Set chip version rolls 65535		  |	₿ (14286) create_jobs_task: Set chip version rolls 65535
₿ (14271) create_jobs_task: New Work Dequeued 0001047c			  |	₿ (14306) create_jobs_task: New Work Dequeued 000104aa
₿ (14281) create_jobs_task: Job processed and queued: 0001047c		  |	₿ (14316) create_jobs_task: Job processed and queued: 000104aa
									  >	₿ (21736) create_jobs_task: New Work Dequeued 000104ab
									  >	₿ (21736) create_jobs_task: Job processed and queued: 000104ab
									  >	₿ (29836) create_jobs_task: New Work Dequeued 000104ac
									  >	₿ (29836) create_jobs_task: Job processed and queued: 000104ac
									  >	₿ (31746) create_jobs_task: New Work Dequeued 000104ad
									  >	₿ (31746) create_jobs_task: Job processed and queued: 000104ad
									  >	₿ (41746) create_jobs_task: New Work Dequeued 000104ae
									  >	₿ (41746) create_jobs_task: Job processed and queued: 000104ae
```
So on a warm restart (left), it does a single job processed and queued and then there is nothing further. After power cycling (right), it does that and then continues, and it's mining again. Also, I did see traffic going to and from the mining pool while it was not mining, so not sure what that signifies (if anything).

Let me know if there's anything else I can help with investigating/troubleshooting. Thanks!

EDIT: My bad, the above is misleading. It is still generating create_jobs_task lines, I just hadn't captured the same number of lines for the diff comparison, so please ignore this.

UPDATE:

Now I have a miner at 5 W with a stuck hash rate:

```
http://bm1370-4  	31 °C	 5 W	 50 %	 831 GH/s	 601 @ v2.4.2	BM1370 @ 550 MHz	1.00 cV @ 0.00 aV	ota_1
```

Note it is only `mining.notify` responses coming from the pool and no `mining.submit` messages originating from the miner during this state.

### MyOwn2C on 2024-12-18

I suspect there is a bad state kept in TPS546D24ARVFR (U2), as in the bad state it only draws 5W but everything else works - just not mining. 
It perhaps cleared during a power cycle and it works again. 

### skot on 2024-12-18

> I suspect there is a bad state kept in TPS546D24ARVFR (U2), as in the bad state it only draws 5W but everything else works - just not mining. It perhaps cleared during a power cycle and it works again.

that's an interesting idea. Hopefully OP can get USB logs from boot in both situations where it working and not.

### asheiner on 2025-01-09

I'm having the same issue with my BM1370.

However, it never starts/started mining. Regardless of soft or cold booting my bitaxe.
And I'm never getting any message about a processed job.
Only repeating 
"stratum_task: rx:" and "create_jobs_task: New Work Dequeued "

### jeroenubbink on 2025-01-09

> I'm having the same issue with my BM1370.
> 
> However, it never starts/started mining. Regardless of soft or cold booting my bitaxe. And I'm never getting any message about a processed job. Only repeating "stratum_task: rx:" and "create_jobs_task: New Work Dequeued "

Yes same issue with my BM1370. I've had it powered down for more than an hour.

Issue seemed to occur out of the blue (not sure since when) but updating firmware from 2.4.1 to 2.4.4 and now 2.4.5 makes no difference.


### skot on 2025-01-09

Yes, I think we have an issue here. My guess is still some setting cached in the voltage regulator.

It would be very helpful if someone could get USB logs FROM BOOT of the bitaxe starting in this bad state.

### jeroenubbink on 2025-01-09

I'm sure i could manage but unfortunately my psu seems broken now as well
so i'll have to get that replaced first.

On Thu, Jan 9, 2025, 20:24 Skot ***@***.***> wrote:

> Yes, I think we have an issue here. My guess is still some setting cached
> in the voltage regulator.
>
> It would be very helpful if someone could get USB logs FROM BOOT of the
> bitaxe starting in this bad state.
>
> —
> Reply to this email directly, view it on GitHub
> <https://github.com/skot/ESP-Miner/issues/588#issuecomment-2581085570>,
> or unsubscribe
> <https://github.com/notifications/unsubscribe-auth/AAOPGEL5QCID7C7J4EPDGF32J3EHTAVCNFSM6AAAAABT3GRFH6VHI2DSMVQWIX3LMV43OSLTON2WKQ3PNVWWK3TUHMZDKOBRGA4DKNJXGA>
> .
> You are receiving this because you commented.Message ID:
> ***@***.***>
>


### matlen67 on 2025-01-09

I currently have a Gamma here from a user in the Bitcoin forum for verification/repair. His Gamma stopped working after a fan upgrade and he asked me if I could take a look at it because I posted in the forum that I occasionally do something with electronics as a hobby. The Gamma has a consumption of 5 watts and does not start with the Minig. When measuring, I noticed that pin 5 of U6 (MPT1824T-0802E) has 1.2V instead of 0.8V. I cannot judge whether this is the cause. I have ordered new MPTs and will try to replace them. Enclosed is the log of the system start, it may help.

Systemlog:

```
I (138837) http_server: Restarting System because of API Request
I (139837) wifi:state: run -> init (0x0)
I (139847) wifi:pm stop, total sleep time: 0 us / 127240756 us

I (139847) wifi:<ba-del>idx:1, tid:0
I (139847) wifi:<ba-del>idx:0, tid:6
I (139847) wifi:new:<11,0>, old:<11,0>, ap:<255,255>, sta:<11,0>, prof:1, snd_ch_cfg:0x0
I (139857) wifi_station: Could not connect to 'MBTC' [rssi -49]: reason 8
I (139907) wifi:flush txq
I (139907) wifi:stop sw txq
I (139907) wifi:lmac stop hw txq
ESP-ROM:esp32s3-20210327
Build:Mar 27 2021
rst:0xc (RTC_SW_CPU_RST),boot:0x28 (SPI_FAST_FLASH_BOOT)
Saved PC:0x40375eb5
SPIWP:0xee
mode:DIO, clock div:1
load:0x3fce2810,len:0x15a0
load:0x403c8700,len:0x4
load:0x403c8704,len:0xd20
load:0x403cb700,len:0x2ee4
entry 0x403c8928
I (26) boot: ESP-IDF v5.4 2nd stage bootloader
I (26) boot: compile time Jan  7 2025 15:36:30
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
I (117) esp_image: segment 0: paddr=00010020 vaddr=3c0e0020 size=2d0e4h (184548) map
I (157) esp_image: segment 1: paddr=0003d10c vaddr=3fc9c800 size=02f0ch ( 12044) load
I (160) esp_image: segment 2: paddr=00040020 vaddr=42000020 size=d2d9ch (863644) map
I (313) esp_image: segment 3: paddr=00112dc4 vaddr=3fc9f70c size=02730h ( 10032) load
I (315) esp_image: segment 4: paddr=001154fc vaddr=40374000 size=18764h (100196) load
I (338) esp_image: segment 5: paddr=0012dc68 vaddr=600fe100 size=0001ch (    28) load
I (348) boot: Loaded app from partition at offset 0x10000
I (349) boot: Disabling RNG early entropy source...
I (359) octal_psram: vendor id    : 0x0d (AP)
I (359) octal_psram: dev id       : 0x02 (generation 3)
I (360) octal_psram: density      : 0x03 (64 Mbit)
I (364) octal_psram: good-die     : 0x01 (Pass)
I (369) octal_psram: Latency      : 0x01 (Fixed)
I (375) octal_psram: VCC          : 0x01 (3V)
I (380) octal_psram: SRF          : 0x01 (Fast Refresh)
I (386) octal_psram: BurstType    : 0x01 (Hybrid Wrap)
I (391) octal_psram: BurstLen     : 0x01 (32 Byte)
I (397) octal_psram: Readlatency  : 0x02 (10 cycles@Fixed)
I (403) octal_psram: DriveStrength: 0x00 (1/1)
I (409) MSPI Timing: PSRAM timing tuning index: 5
I (414) esp_psram: Found 8MB PSRAM device
I (418) esp_psram: Speed: 80MHz
I (422) cpu_start: Multicore app
I (859) esp_psram: SPI SRAM memory test OK
I (868) cpu_start: Pro cpu start user code
I (868) cpu_start: cpu freq: 240000000 Hz
I (868) app_init: Application information:
I (871) app_init: Project name:     esp-miner
I (876) app_init: App version:      v2.4.5
I (880) app_init: Compile time:     Jan  7 2025 15:36:24
I (886) app_init: ELF file SHA256:  f459f48ef...
I (892) app_init: ESP-IDF:          v5.4
I (896) efuse_init: Min chip rev:     v0.0
I (901) efuse_init: Max chip rev:     v0.99 
I (906) efuse_init: Chip rev:         v0.2
I (911) heap_init: Initializing. RAM available for dynamic allocation:
I (918) heap_init: At 3FCB7528 len 000321E8 (200 KiB): RAM
I (924) heap_init: At 3FCE9710 len 00005724 (21 KiB): RAM
I (930) heap_init: At 3FCF0000 len 00008000 (32 KiB): DRAM
I (936) heap_init: At 600FE11C len 00001ECC (7 KiB): RTCRAM
I (943) esp_psram: Adding pool of 8192K of PSRAM memory to heap allocator
I (951) spi_flash: detected chip: gd
I (954) spi_flash: flash io: dio
I (959) sleep_gpio: Configure to isolate all GPIO pins in sleep state
I (966) sleep_gpio: Enable automatic switching of GPIO sleep configuration
I (973) main_task: Started on CPU0
I (983) esp_psram: Reserving pool of 32K of internal memory for DMA/internal allocations
I (983) main_task: Calling app_main()
I (993) bitaxe: Welcome to the bitaxe - hack the planet!
I (993) bitaxe: I2C initialized successfully
I (1103) ADC: calibration scheme version is Curve Fitting
I (1103) ADC: Calibration Success
I (1123) nvs_device: NVS_CONFIG_ASIC_FREQ 525.000000
I (1123) nvs_device: DEVICE: Gamma
I (1123) nvs_device: Found Device Model: gamma
I (1123) nvs_device: Found Board Version: 601
I (1133) nvs_device: ASIC: 1x BM1370 (128 cores)
I (1133) SystemModule: Initial overheat_mode value: 0
I (1143) pp: pp rom version: e7ae62f
I (1143) net80211: net80211 rom version: e7ae62f
I (1163) wifi:wifi driver task: 3fcc9428, prio:23, stack:6656, core=0
I (1173) wifi:wifi firmware version: 48ea317a7
I (1173) wifi:wifi certification version: v7.0
I (1173) wifi:config NVS flash: enabled
I (1173) wifi:config nano formatting: disabled
I (1173) wifi:Init data frame dynamic rx buffer num: 32
I (1183) wifi:Init static rx mgmt buffer num: 5
I (1183) wifi:Init management short buffer num: 32
I (1183) wifi:Init dynamic tx buffer num: 32
I (1193) wifi:Init static tx FG buffer num: 2
I (1193) wifi:Init static rx buffer size: 1600
I (1203) wifi:Init static rx buffer num: 10
I (1203) wifi:Init dynamic rx buffer num: 32
I (1213) wifi_init: rx ba win: 6
I (1213) wifi_init: accept mbox: 6
I (1213) wifi_init: tcpip mbox: 32
I (1223) wifi_init: udp mbox: 6
I (1223) wifi_init: tcp mbox: 6
I (1223) wifi_init: tcp tx win: 5760
I (1233) wifi_init: tcp rx win: 5760
I (1233) wifi_init: tcp mss: 1440
I (1243) wifi_init: WiFi IRAM OP enabled
I (1243) wifi_init: WiFi RX IRAM OP enabled
I (1253) wifi_station: ESP_WIFI Access Point On
I (1263) wifi_station: ESP_WIFI Access Point On
I (1263) wifi_station: ESP_WIFI_MODE_STA
I (1263) wifi_station: WiFi Password provided, using WPA2
I (1273) wifi_station: wifi_init_sta finished.
I (1273) phy_init: phy_version 680,a6008b2,Jun  4 2024,16:41:10
I (1323) wifi:mode : sta (74:4d:bd:97:eb:80) + softAP (74:4d:bd:97:eb:81)
I (1323) wifi:enable tsf
I (1323) wifi:Total power save buffer number: 16
I (1323) wifi:Init max length of beacon: 752/752
I (1323) wifi:Init max length of beacon: 752/752
I (1333) wifi:Set ps type: 0, coexist: 0

I (1333) esp_netif_lwip: DHCP server started on interface WIFI_AP_DEF with IP: 192.168.4.1
I (1343) wifi_station: ESP_WIFI setting hostname to: bitaxe
I (1353) wifi_station: wifi_init_sta finished.
I (1353) TPS546: Initializing the core voltage regulator
I (1363) TPS546: Device ID: 54 49 54 6d 24 41
I (1363) TPS546: Power config-ON_OFF_CONFIG: 18
I (1373) TPS546: Reading MFR info
I (1373) TPS546: MFR_ID: 
I (1373) TPS546: MFR_MODEL: 
I (1383) TPS546: MFR_REVISION: 000 
I (1383) TPS546: Writing new config values
I (1393) TPS546: VOUT_MODE: 97
I (1393) TPS546: ---Writing new config values to TPS546---
I (1403) TPS546: Setting ON_OFF_CONFIG
I (1403) TPS546: Setting FREQUENCY
I (1413) TPS546: Setting VIN_ON: 4.80
I (1413) TPS546: Setting VIN_OFF: 4.50
I (1413) TPS546: Setting VIN_UV_WARN_LIMIT: 5.80
I (1423) TPS546: Setting VIN_OV_FAULT_LIMIT: 6.00
I (1433) TPS546: Setting VIN_OV_FAULT_RESPONSE: B7
I (1433) TPS546: Setting VOUT SCALE: 0.25
I (1443) TPS546: VOUT_COMMAND: 1.20
I (1443) TPS546: VOUT_MAX: 3
I (1443) TPS546: VOUT_OV_FAULT_LIMIT: 1.25
I (1453) TPS546: VOUT_OV_WARN_LIMIT: 1.10
I (1453) TPS546: VOUT_MARGIN_HIGH: 1.10
I (1463) TPS546: VOUT_MARGIN_LOW: 0.90
I (1463) TPS546: VOUT_UV_WARN_LIMIT: 0.90
I (1473) TPS546: VOUT_UV_FAULT_LIMIT: 0.75
I (1473) TPS546: VOUT_MIN: 1
I (1483) TPS546: Setting IOUT
I (1483) TPS546: Setting TEMPERATURE
I (1483) TPS546: OT_WARN_LIMIT: 105
I (1493) TPS546: OT_FAULT_LIMIT: 145
I (1493) TPS546: OT_FAULT_RESPONSE: ff
I (1503) TPS546: Setting TIMING
I (1503) TPS546: TON_DELAY: 0
I (1503) TPS546: TON_RISE: 3
I (1513) TPS546: TON_MAX_FAULT_LIMIT: 0
I (1513) TPS546: TON_MAX_FAULT_RESPONSE: 3b
I (1523) TPS546: TOFF_DELAY: 0
I (1523) TPS546: TOFF_FALL: 0
I (1523) TPS546: Setting PIN_DETECT_OVERRIDE
I (1533) TPS546: Writing MFR ID
I (1533) TPS546: Writing MFR MODEL
I (1543) TPS546: Writing MFR REVISION
I (1543) TPS546: -----------VOLTAGE---------------------
I (1553) TPS546: VIN ON set to: 4.80
I (1553) TPS546: VIN OFF set to: 4.50
I (1563) TPS546: Vout Max set to: 3.00 V
I (1563) TPS546: Vout OV Fault Limit: 1.25 V
I (1573) TPS546: Vout OV Warn Limit: 1.10 V
I (1573) TPS546: Vout Margin HIGH: 1.10 V
I (1573) TPS546: Vout set to: 1.20 V
I (1583) TPS546: Vout Margin LOW: 0.90 V
I (1583) TPS546: Vout UV Warn Limit: 0.90 V
I (1593) TPS546: Vout UV Fault Limit: 0.75 V
I (1593) TPS546: Vout Min set to: 1.00 V
I (1603) TPS546: -----------TIMING---------------------
I (1603) TPS546: TON_DELAY: 0
I (1613) TPS546: TON_RISE: 3
I (1613) TPS546: TON_MAX_FAULT_LIMIT: 0
I (1613) TPS546: TON_MAX_FAULT_RESPONSE: 3b
I (1623) TPS546: TOFF_DELAY: 0
I (1623) TPS546: TOFF_FALL: 0
I (1633) TPS546: --------------------------------------
I (1633) TPS546: COMPENSATION CONFIG
I (1643) TPS546: 13 11 08 19 04
I (1643) vcore.c: Set ASIC voltage = 1.150V
I (1653) TPS546: Vout changed to 1.15 V
I (2153) SystemModule: Existing overheat_mode value: 0
I (2153) display: Install panel IO
I (2153) display: Install SSD1306 panel driver
I (2153) display: Initialize LVGL
I (2153) LVGL: Starting LVGL task
I (2313) SystemModule: OLED init success!
I (2313) input: Install button driver
I (2313) gpio: GPIO[0]| InputEn: 1| OutputEn: 0| OpenDrain: 0| Pullup: 1| Pulldown: 0| Intr:3 
I (2343) power_management: Starting
I (2463) http_server: Partition size: total: 2884241, used: 821774
I (2463) http_server: Starting HTTP Server
I (2473) example_dns_redirect_server: Socket created
I (2473) example_dns_redirect_server: Socket bound, port 53
I (2473) example_dns_redirect_server: Waiting for data
I (2843) power_management: setting new vcore voltage to 1150mV
I (2843) vcore.c: Set ASIC voltage = 1.150V
I (2893) TPS546: Vout changed to 1.15 V
I (4163) wifi:ap channel adjust o:1,1 n:11,2
I (4163) wifi:new:<11,0>, old:<1,1>, ap:<11,2>, sta:<11,0>, prof:1, snd_ch_cfg:0x0
I (4163) wifi:state: init -> auth (0xb0)
I (4183) wifi:state: auth -> assoc (0x0)
I (4193) wifi:state: assoc -> run (0x10)
I (4203) wifi:connected with MBTC, aid = 20, channel 11, BW20, bssid = f6:e2:c6:1e:a3:71
I (4203) wifi:security: WPA2-PSK, phy: bgn, rssi: -52
I (4213) wifi:pm start, type: 0

I (4213) wifi:dp: 1, bi: 102400, li: 3, scale listen interval from 307200 us to 307200 us
I (4213) wifi:set rx beacon pti, rx_bcn_pti: 0, bcn_timeout: 25000, mt_pti: 0, mt_time: 10000
I (4243) wifi:<ba-add>idx:0 (ifx:0, f6:e2:c6:1e:a3:71), tid:6, ssn:2, winSize:64
I (4243) wifi:<ba-add>idx:1 (ifx:0, f6:e2:c6:1e:a3:71), tid:0, ssn:0, winSize:64
I (4273) wifi:AP's beacon interval = 102400 us, DTIM period = 1
I (5243) wifi_station: Bitaxe ip: 192.168.178.249
I (5243) esp_netif_handlers: sta ip: 192.168.178.249, mask: 255.255.255.0, gw: 192.168.178.1
I (5243) bitaxe: Connected to SSID: MBTC
I (5243) wifi_station: ESP_WIFI Access Point Off
I (5253) wifi:mode : sta (74:4d:bd:97:eb:80)
I (5263) serial: Initializing serial
I (5263) bm1370Module: Initializing BM1370
tx: [55 AA 51 09 00 A4 90 00 FF FF 1C]
tx: [55 AA 51 09 00 A4 90 00 FF FF 1C]
tx: [55 AA 51 09 00 A4 90 00 FF FF 1C]
tx: [55 AA 52 05 00 00 0A]
I (6463) bm1370Module: 1 chip(s) detected on the chain, expected 1
tx: [55 AA 51 09 00 A4 90 00 FF FF 1C]
tx: [55 AA 51 09 00 A8 00 07 00 00 03]
tx: [55 AA 51 09 00 18 F0 00 C1 00 04]
tx: [55 AA 53 05 00 00 03]
tx: [55 AA 40 05 00 00 1C]
tx: [55 AA 51 09 00 3C 80 00 8B 00 12]
tx: [55 AA 51 09 00 3C 80 00 80 0C 11]
I (6473) bm1370Module: Setting ASIC difficulty mask to 255
tx: [55 AA 51 09 00 14 00 00 00 FF 08]
tx: [55 AA 51 09 00 58 00 01 11 11 0D]
tx: [55 AA 41 09 00 A8 00 07 01 F0 15]
tx: [55 AA 41 09 00 18 F0 00 C1 00 0C]
tx: [55 AA 41 09 00 3C 80 00 8B 00 1A]
tx: [55 AA 41 09 00 3C 80 00 80 0C 19]
tx: [55 AA 41 09 00 3C 80 00 82 AA 05]
tx: [55 AA 51 09 00 B9 00 00 44 80 0D]
tx: [55 AA 51 09 00 54 00 00 00 02 18]
tx: [55 AA 51 09 00 B9 00 00 44 80 0D]
tx: [55 AA 51 09 00 3C 80 00 8D EE 1B]
I (6523) bm1370Module: Ramping up frequency from 56.25 MHz to 525.00 MHz with step 6.25 MHz
tx: [55 AA 51 09 00 08 40 A2 02 55 0F]
I (6533) bm1370Module: Setting Frequency to 56.25MHz (56.25)
tx: [55 AA 51 09 00 08 40 AF 02 64 08]
I (6543) bm1370Module: Setting Frequency to 62.50MHz (62.50)
tx: [55 AA 51 09 00 08 40 A5 02 54 08]
I (6653) bm1370Module: Setting Frequency to 68.75MHz (68.75)
tx: [55 AA 51 09 00 08 40 A8 02 63 11]
I (6753) bm1370Module: Setting Frequency to 75.00MHz (75.00)
tx: [55 AA 51 09 00 08 40 B6 02 63 0C]
I (6853) bm1370Module: Setting Frequency to 81.25MHz (81.25)
tx: [55 AA 51 09 00 08 40 A8 02 53 1A]
I (6953) bm1370Module: Setting Frequency to 87.50MHz (87.50)
tx: [55 AA 51 09 00 08 40 B4 02 53 12]
I (7053) bm1370Module: Setting Frequency to 93.75MHz (93.75)
tx: [55 AA 51 09 00 08 40 A8 02 62 14]
I (7153) bm1370Module: Setting Frequency to 100.00MHz (100.00)
tx: [55 AA 51 09 00 08 40 AA 02 43 15]
I (7253) bm1370Module: Setting Frequency to 106.25MHz (106.25)
tx: [55 AA 51 09 00 08 40 A2 02 52 14]
I (7353) bm1370Module: Setting Frequency to 112.50MHz (112.50)
tx: [55 AA 51 09 00 08 40 AB 02 52 12]
I (7453) bm1370Module: Setting Frequency to 118.75MHz (118.75)
tx: [55 AA 51 09 00 08 40 B4 02 52 17]
I (7553) bm1370Module: Setting Frequency to 125.00MHz (125.00)
tx: [55 AA 51 09 00 08 40 BD 02 52 11]
I (7653) bm1370Module: Setting Frequency to 131.25MHz (131.25)
tx: [55 AA 51 09 00 08 40 A5 02 42 0C]
I (7753) bm1370Module: Setting Frequency to 137.50MHz (137.50)
tx: [55 AA 51 09 00 08 40 A1 02 61 1D]
I (7853) bm1370Module: Setting Frequency to 143.75MHz (143.75)
tx: [55 AA 51 09 00 08 40 A8 02 61 1B]
I (7953) bm1370Module: Setting Frequency to 150.00MHz (150.00)
tx: [55 AA 51 09 00 08 40 AF 02 61 19]
I (8053) bm1370Module: Setting Frequency to 156.25MHz (156.25)
tx: [55 AA 51 09 00 08 40 B6 02 61 06]
I (8153) bm1370Module: Setting Frequency to 162.50MHz (162.50)
tx: [55 AA 51 09 00 08 40 A2 02 51 1B]
I (8253) bm1370Module: Setting Frequency to 168.75MHz (168.75)
tx: [55 AA 51 09 00 08 40 A8 02 51 10]
I (8353) bm1370Module: Setting Frequency to 175.00MHz (175.00)
tx: [55 AA 51 09 00 08 40 AE 02 51 0A]
I (8453) bm1370Module: Setting Frequency to 181.25MHz (181.25)
tx: [55 AA 51 09 00 08 40 B4 02 51 18]
I (8553) bm1370Module: Setting Frequency to 187.50MHz (187.50)
tx: [55 AA 51 09 00 08 40 BA 02 51 1C]
I (8653) bm1370Module: Setting Frequency to 193.75MHz (193.75)
tx: [55 AA 51 09 00 08 40 A0 02 41 14]
I (8753) bm1370Module: Setting Frequency to 200.00MHz (200.00)
tx: [55 AA 51 09 00 08 40 A5 02 41 03]
I (8853) bm1370Module: Setting Frequency to 206.25MHz (206.25)
tx: [55 AA 51 09 00 08 40 AA 02 41 1F]
I (8953) bm1370Module: Setting Frequency to 212.50MHz (212.50)
tx: [55 AA 51 09 00 08 40 AF 02 41 08]
I (9053) bm1370Module: Setting Frequency to 218.75MHz (218.75)
tx: [55 AA 51 09 00 08 40 B4 02 41 02]
I (9153) bm1370Module: Setting Frequency to 225.00MHz (225.00)
tx: [55 AA 51 09 00 08 40 B9 02 41 0B]
I (9253) bm1370Module: Setting Frequency to 231.25MHz (231.25)
tx: [55 AA 51 09 00 08 40 BE 02 41 09]
I (9353) bm1370Module: Setting Frequency to 237.50MHz (237.50)
tx: [55 AA 51 09 00 08 50 C3 02 41 01]
I (9453) bm1370Module: Setting Frequency to 243.75MHz (243.75)
tx: [55 AA 51 09 00 08 40 A0 02 31 18]
I (9553) bm1370Module: Setting Frequency to 250.00MHz (250.00)
tx: [55 AA 51 09 00 08 40 A4 02 31 17]
I (9653) bm1370Module: Setting Frequency to 256.25MHz (256.25)
tx: [55 AA 51 09 00 08 40 A8 02 31 06]
I (9753) bm1370Module: Setting Frequency to 262.50MHz (262.50)
tx: [55 AA 51 09 00 08 40 AC 02 31 09]
I (9853) bm1370Module: Setting Frequency to 268.75MHz (268.75)
tx: [55 AA 51 09 00 08 40 B0 02 31 01]
I (9953) bm1370Module: Setting Frequency to 275.00MHz (275.00)
tx: [55 AA 51 09 00 08 40 B4 02 31 0E]
I (10053) bm1370Module: Setting Frequency to 281.25MHz (281.25)
tx: [55 AA 51 09 00 08 40 A1 02 60 18]
I (10153) bm1370Module: Setting Frequency to 287.50MHz (287.50)
tx: [55 AA 51 09 00 08 40 BC 02 31 10]
I (10253) bm1370Module: Setting Frequency to 293.75MHz (293.75)
tx: [55 AA 51 09 00 08 40 A8 02 60 1E]
I (10353) bm1370Module: Setting Frequency to 300.00MHz (300.00)
tx: [55 AA 51 09 00 08 50 C4 02 31 0F]
I (10453) bm1370Module: Setting Frequency to 306.25MHz (306.25)
tx: [55 AA 51 09 00 08 40 AF 02 60 1C]
I (10553) bm1370Module: Setting Frequency to 312.50MHz (312.50)
tx: [55 AA 51 09 00 08 50 CC 02 31 11]
I (10653) bm1370Module: Setting Frequency to 318.75MHz (318.75)
tx: [55 AA 51 09 00 08 40 B6 02 60 03]
I (10753) bm1370Module: Setting Frequency to 325.00MHz (325.00)
tx: [55 AA 51 09 00 08 50 D4 02 31 16]
I (10853) bm1370Module: Setting Frequency to 331.25MHz (331.25)
tx: [55 AA 51 09 00 08 40 A2 02 50 1E]
I (10953) bm1370Module: Setting Frequency to 337.50MHz (337.50)
tx: [55 AA 51 09 00 08 40 A5 02 50 1C]
I (11053) bm1370Module: Setting Frequency to 343.75MHz (343.75)
tx: [55 AA 51 09 00 08 40 A8 02 50 15]
I (11153) bm1370Module: Setting Frequency to 350.00MHz (350.00)
tx: [55 AA 51 09 00 08 40 AB 02 50 18]
I (11253) bm1370Module: Setting Frequency to 356.25MHz (356.25)
tx: [55 AA 51 09 00 08 40 AE 02 50 0F]
I (11353) bm1370Module: Setting Frequency to 362.50MHz (362.50)
tx: [55 AA 51 09 00 08 40 B1 02 50 0A]
I (11453) bm1370Module: Setting Frequency to 368.75MHz (368.75)
tx: [55 AA 51 09 00 08 40 B4 02 50 1D]
I (11553) bm1370Module: Setting Frequency to 375.00MHz (375.00)
tx: [55 AA 51 09 00 08 40 B7 02 50 10]
I (11653) bm1370Module: Setting Frequency to 381.25MHz (381.25)
tx: [55 AA 51 09 00 08 40 BA 02 50 19]
I (11753) bm1370Module: Setting Frequency to 387.50MHz (387.50)
tx: [55 AA 51 09 00 08 40 BD 02 50 1B]
I (11853) bm1370Module: Setting Frequency to 393.75MHz (393.75)
tx: [55 AA 51 09 00 08 40 A0 02 40 11]
I (11953) bm1370Module: Setting Frequency to 400.00MHz (400.00)
tx: [55 AA 51 09 00 08 50 C3 02 50 1E]
I (12053) bm1370Module: Setting Frequency to 406.25MHz (406.25)
tx: [55 AA 51 09 00 08 40 A5 02 40 06]
I (12153) bm1370Module: Setting Frequency to 412.50MHz (412.50)
tx: [55 AA 51 09 00 08 50 C9 02 50 15]
I (12253) bm1370Module: Setting Frequency to 418.75MHz (418.75)
tx: [55 AA 51 09 00 08 40 AA 02 40 1A]
I (12353) bm1370Module: Setting Frequency to 425.00MHz (425.00)
tx: [55 AA 51 09 00 08 50 CF 02 50 0F]
I (12453) bm1370Module: Setting Frequency to 431.25MHz (431.25)
tx: [55 AA 51 09 00 08 40 AF 02 40 0D]
I (12553) bm1370Module: Setting Frequency to 437.50MHz (437.50)
tx: [55 AA 51 09 00 08 50 D5 02 50 1D]
I (12653) bm1370Module: Setting Frequency to 443.75MHz (443.75)
tx: [55 AA 51 09 00 08 40 B4 02 40 07]
I (12753) bm1370Module: Setting Frequency to 450.00MHz (450.00)
tx: [55 AA 51 09 00 08 50 DB 02 50 19]
I (12853) bm1370Module: Setting Frequency to 456.25MHz (456.25)
tx: [55 AA 51 09 00 08 40 B9 02 40 0E]
I (12953) bm1370Module: Setting Frequency to 462.50MHz (462.50)
tx: [55 AA 51 09 00 08 50 E1 02 50 1C]
I (13053) bm1370Module: Setting Frequency to 468.75MHz (468.75)
tx: [55 AA 51 09 00 08 40 BE 02 40 0C]
I (13153) bm1370Module: Setting Frequency to 475.00MHz (475.00)
tx: [55 AA 51 09 00 08 50 E7 02 50 06]
I (13253) bm1370Module: Setting Frequency to 481.25MHz (481.25)
tx: [55 AA 51 09 00 08 50 C3 02 40 04]
I (13353) bm1370Module: Setting Frequency to 487.50MHz (487.50)
tx: [55 AA 51 09 00 08 50 ED 02 50 0D]
I (13453) bm1370Module: Setting Frequency to 493.75MHz (493.75)
tx: [55 AA 51 09 00 08 40 A0 02 30 1D]
I (13553) bm1370Module: Setting Frequency to 500.00MHz (500.00)
tx: [55 AA 51 09 00 08 40 A2 02 30 08]
I (13653) bm1370Module: Setting Frequency to 506.25MHz (506.25)
tx: [55 AA 51 09 00 08 40 A4 02 30 12]
I (13753) bm1370Module: Setting Frequency to 512.50MHz (512.50)
tx: [55 AA 51 09 00 08 40 A6 02 30 07]
I (13853) bm1370Module: Setting Frequency to 518.75MHz (518.75)
tx: [55 AA 51 09 00 08 40 A8 02 30 03]
I (13953) bm1370Module: Setting Frequency to 525.00MHz (525.00)
tx: [55 AA 51 09 00 10 00 00 1E B5 0F]
I (14053) bm1370Module: Setting max baud of 1000000 
tx: [55 AA 51 09 00 28 11 30 02 00 03]
I (14053) serial: Changing UART baud to 1000000
I (14053) stratum_task: Trying to get IP for URL: eusolo.ckpool.org
I (14053) stratum_task: Starting heartbeat thread for primary endpoint: eusolo.ckpool.org
I (14063) ASIC_task: ASIC Job Interval: 500.00 ms
I (14063) main_task: Returned from app_main()
I (14073) ASIC_task: ASIC Ready!
I (14083) stratum_task: Connecting to: stratum+tcp://eusolo.ckpool.org:3333 (88.99.11.212)
I (14093) stratum_task: Socket created, connecting to 88.99.11.212:3333
I (14123) stratum_api: Resetting stratum uid
I (14123) stratum_task: Clean Jobs: clearing queue
I (14123) stratum_api: tx: {"id": 1, "method": "mining.configure", "params": [["version-rolling"], {"version-rolling.mask": "ffffffff"}]}
I (14143) stratum_api: tx: {"id": 2, "method": "mining.subscribe", "params": ["bitaxe/BM1370/v2.4.5"]}
I (14153) stratum_api: tx: {"id": 3, "method": "mining.authorize", "params": ["bc1q4hrn7up6w9mwagjpwssgsqafuykgvjqzyhhpje", "x"]}
I (14163) stratum_api: tx: {"id": 4, "method": "mining.suggest_difficulty", "params": [1000]}
I (14173) stratum_task: rx: {"result":{"version-rolling":true,"version-rolling.mask":"1fffe000"},"id":1,"error":null}
I (14183) stratum_api: Set version mask: 1fffe000
I (14183) stratum_task: Set version mask: 1fffe000
I (14193) stratum_task: rx: {"result":[[["mining.notify","67ac3648"]],"6b86a967",8],"id":2,"error":null}
I (14203) stratum_api: extranonce_str: 6b86a967
I (14213) stratum_api: extranonce_2_len: 8
I (14213) stratum_task: rx: {"params":[10000],"id":null,"method":"mining.set_difficulty"}
I (14223) stratum_task: Set stratum difficulty: 10000
I (14233) stratum_task: rx: {"params":["67484e7d0001ec67","e55e85d8085e010006d7b65b6ac7f7984c5593c50001db360000000000000000","01000000010000000000000000000000000000000000000000000000000000000000000000ffffffff3503c2670d0004652e8067040f8b281e0c","0a636b706f6f6c112f736f6c6f2e636b706f6f6c2e6f72672fffffffff033b48621200000000160014adc73f703a7176eea24174208803a9e12c864802ec0b60000000000016001451ed61d2f6aa260cc72cdf743e4e436a82c010270000000000000000266a24aa21a9ed67b3f3c5faebdb43b53d9349a16a31ab5723d01ebe6286975b41e233766be5d100000000",["0900db8029439d21ff5e0a0181734e3a66bf14850b44fd30e860b90009a2b744","86865c7717919310dcbcaa43176746d1e28b14cfcdc9af0fdbdecb214358bb4a","0a8e8957aeda5e917cc675ee0a668cee1241a2718c4a54323fe4dec775bcb994","f53b25f82c856061217e325c0ec9e10d673a115df40823234f0c31275a38cc6a","2579b7f3691c81d28490a56828a96cf2346dde381fa324e6e50dfb1fba7924e4","b456c5de7eed7f32c1d1466eae7289fc1dfffd00c8c0a559f50bc6db9da8808c","92cd001fb03f9f0eafa90162ec50ec1af2632c292f882aef5876f81d685b9d84","c5b5670c50ffa58311fd2a7e5e6f0162b2aa65276d5bd829cd808b7862150b54","6e24b17fe29bf4bafba71b44b4a7470c59362b41fccfb66846a8dc9037fb8274","ee02df73de0f7f8a515d055dbc3b9fead48f58a1a01bb0df2b31c2ac090cee3e","a8c669690a7dcbab95cd2a775b0e35f610efbd21329f28540c8f57e3773db6bd","2931564b00d0599094a56a329fce40b943e15ba33ddf7781c53c1fa5fb9aca11"],"20000000","1702905c","67802e65",true],"id":null,"method":"mining.notify"}
I (14353) SystemModule: Syncing clock
I (14353) create_jobs_task: New Work Dequeued 67484e7d0001ec67
I (14353) stratum_task: rx: {"params":[10000],"id":null,"method":"mining.set_difficulty"}
I (14363) create_jobs_task: Set chip version rolls 65535
I (14373) stratum_task: rx: {"result":true,"error":null,"id":3}
tx: [55 AA 51 09 00 A4 90 00 FF FF 1C]
I (14393) ASIC_task: New pool difficulty 10000
I (14393) stratum_task: setup message accepted
I (15723) stratum_task: rx: {"params":["67484e7d0001ec68","e55e85d8085e010006d7b65b6ac7f7984c5593c50001db360000000000000000","01000000010000000000000000000000000000000000000000000000000000000000000000ffffffff3503c2670d0004832e80670434c592060c","0a636b706f6f6c112f736f6c6f2e636b706f6f6c2e6f72672fffffffff038396641200000000160014adc73f703a7176eea24174208803a9e12c864802f81760000000000016001451ed61d2f6aa260cc72cdf743e4e436a82c010270000000000000000266a24aa21a9ed4b33061fc78dfc164594b41478bed269fb33ce942aae457d0b2dbc0e242062fa00000000",["0900db8029439d21ff5e0a0181734e3a66bf14850b44fd30e860b90009a2b744","49e384716d8a63872dc2f1c0d70eb3167fe729353e7acb133576c2ccfaa0380d","16dea8c3b004f6190e52d3f1865fe39078569ca9b42dbb0f0a23529dbf8de39b","20dd984a54ca465ae09f0cf910006598c2dbcc608dae1275c6cc44c39aa13ec4","72befb78b6a13c503f727e672e6d4f60dd334df648622c1b567baa86d99350ca","135aa406143269c48cb5d786468dcc778fbd456b0e7ee1ab9ba8aced1237817c","fdae05e533ce594533bd99d23a695a401cd8c157b36e6dc51c81b6e21d3a73ca","bd4e24e6a5b9b477da1b169ef28fe4e3cb0533d13e4005a0c439dcbe623af941","389368ecba7061c19cac1246f36c834016974e36d4df1fc0b81a051819e0aa15","87f8116028ae41e4afbf533207f01ef9fe791dddc8b1faf15895b8e73fb03f11","3f33101db40b77ca8a17a92026ab58eb054e5ee8fdda03a61a89002a75d3b80a","166b5d8108d83efb71ead66e508795387bbc5e0be565e695c1b53db5af13a680"],"20000000","1702905c","67802e83",false],"id":null,"method":"mining.notify"}
I (15903) create_jobs_task: New Work Dequeued 67484e7d0001ec68
```



### jeroenubbink on 2025-01-10

> I currently have a Gamma here from a user in the Bitcoin forum for verification/repair. His Gamma stopped working after a fan upgrade and he asked me if I could take a look at it because I posted in the forum that I occasionally do something with electronics as a hobby. The Gamma has a consumption of 5 watts and does not start with the Minig. When measuring, I noticed that pin 5 of U6 (MPT1824T-0802E) has 1.2V instead of 0.8V. I cannot judge whether this is the cause. I have ordered new MPTs and will try to replace them. Enclosed is the log of the system start, it may help.

Do you think this could maybe also brick your PSU in some way?

### matlen67 on 2025-01-10

> > I currently have a Gamma here from a user in the Bitcoin forum for verification/repair. His Gamma stopped working after a fan upgrade and he asked me if I could take a look at it because I posted in the forum that I occasionally do something with electronics as a hobby. The Gamma has a consumption of 5 watts and does not start with the Minig. When measuring, I noticed that pin 5 of U6 (MPT1824T-0802E) has 1.2V instead of 0.8V. I cannot judge whether this is the cause. I have ordered new MPTs and will try to replace them. Enclosed is the log of the system start, it may help.
> 
> Do you think this could maybe also brick your PSU in some way?

My power supplies are ok, my Gamma works perfectly with them.

### skot on 2025-01-11

> I currently have a Gamma here from a user in the Bitcoin forum for verification/repair. His Gamma stopped working after a fan upgrade and he asked me if I could take a look at it because I posted in the forum that I occasionally do something with electronics as a hobby. The Gamma has a consumption of 5 watts and does not start with the Minig. When measuring, I noticed that pin 5 of U6 (MPT1824T-0802E) has 1.2V instead of 0.8V. I cannot judge whether this is the cause. I have ordered new MPTs and will try to replace them. Enclosed is the log of the system start, it may help.

Thank you for the detailed log. This is really strange about the output voltage of the 0.8V LDO.. please let us know what your find out.

### skot on 2025-01-11

Another one. https://x.com/StackAddict90/status/1878163312354922757

### skot on 2025-01-12

I compared the log from @matlen67 with one from a working Gamma here. No differences that I can tell. Still digging.

### MyOwn2C on 2025-01-29

One more case 
https://x.com/anonameus0/status/1884334945885462961

### MyOwn2C on 2025-01-31

Another case:
https://x.com/dockcapital/status/1885207797593260499

### gustavobrossi on 2025-02-08

I've got same issue for a couple of weeks now, if I recall, it all started when I bumped to v2.5.1. For a couple of days, reconnecting the PSU would bring it back up but now has gone completely dead. Not even flashing older firmware versions works. With 2.5.1 I've got no useful logs but factory resetting with 2.4.5 brings interesting results from the self test.

It is unclear to me if there is still a fix for the TPS546 as flashing other versions doesn't bring it back to life.

```
Script started on Fri Feb  7 23:10:14 2025
command: screen /dev/tty.usbmodem14101 115200
I (158) esp_image: segment 1: paddr=0003d10c vaddr=3fc9c800 size

(2485) bm1370Module: 1 chip(s) detected on the chain, expected 1
tx: [55 AA 51 09 00 A4 90 00 FF FF 1C]
tx: [55 AA 51 09 00 A8 00 07 00 00 03]
tx: [55 AA 51 09 00 18 F0 00 C1 00 04]
tx: [55 AA 53 05 00 00 03]
tx: [55 AA 40 05 00 00 1C]
tx: [55 AA 51 09 00 3C 80 00 8B 00 12]
tx: [55 AA 51 09 00 3C 80 00 80 0C 11]
(2495) bm1370Module: Setting ASIC difficulty mask to 255
tx: [55 AA 51 09 00 14 00 00 00 FF 08]
tx: [55 AA 51 09 00 58 00 01 11 11 0D]
tx: [55 AA 41 09 00 A8 00 07 01 F0 15]
tx: [55 AA 41 09 00 18 F0 00 C1 00 0C]
tx: [55 AA 41 09 00 3C 80 00 8B 00 1A]
tx: [55 AA 41 09 00 3C 80 00 80 0C 19]
tx: [55 AA 41 09 00 3C 80 00 82 AA 05]
tx: [55 AA 51 09 00 B9 00 00 44 80 0D]
tx: [55 AA 51 09 00 54 00 00 00 02 18]
tx: [55 AA 51 09 00 B9 00 00 44 80 0D]
tx: [55 AA 51 09 00 3C 80 00 8D EE 1B]
(2555) bm1370Module: Ramping up frequency from 56.25 MHz to 525.00 MHz with step 6.25 MHz
tx: [55 AA 51 09 00 08 40 A2 02 55 0F]
(2565) bm1370Module: Setting Frequency to 56.25MHz (56.25)
tx: [55 AA 51 09 00 08 40 AF 02 64 08]
(2575) bm1370Module: Setting Frequency to 62.50MHz (62.50)
tx: [55 AA 51 09 00 08 40 A5 02 54 08]
(2675) bm1370Module: Setting Frequency to 68.75MHz (68.75)
tx: [55 AA 51 09 00 08 40 A8 02 63 11]
(2775) bm1370Module: Setting Frequency to 75.00MHz (75.00)
tx: [55 AA 51 09 00 08 40 B6 02 63 0C]
(2875) bm1370Module: Setting Frequency to 81.25MHz (81.25)
tx: [55 AA 51 09 00 08 40 A8 02 53 1A]
(2975) bm1370Module: Setting Frequency to 87.50MHz (87.50)
tx: [55 AA 51 09 00 08 40 B4 02 53 12]
(3075) bm1370Module: Setting Frequency to 93.75MHz (93.75)
tx: [55 AA 51 09 00 08 40 A8 02 62 14]
(3175) bm1370Module: Setting Frequency to 100.00MHz (100.00)
tx: [55 AA 51 09 00 08 40 AA 02 43 15]
(3275) bm1370Module: Setting Frequency to 106.25MHz (106.25)
tx: [55 AA 51 09 00 08 40 A2 02 52 14]
(3375) bm1370Module: Setting Frequency to 112.50MHz (112.50)
tx: [55 AA 51 09 00 08 40 AB 02 52 12]
(3475) bm1370Module: Setting Frequency to 118.75MHz (118.75)
tx: [55 AA 51 09 00 08 40 B4 02 52 17]
(3575) bm1370Module: Setting Frequency to 125.00MHz (125.00)
tx: [55 AA 51 09 00 08 40 BD 02 52 11]
(3675) bm1370Module: Setting Frequency to 131.25MHz (131.25)
tx: [55 AA 51 09 00 08 40 A5 02 42 0C]
(3775) bm1370Module: Setting Frequency to 137.50MHz (137.50)
tx: [55 AA 51 09 00 08 40 A1 02 61 1D]
(3875) bm1370Module: Setting Frequency to 143.75MHz (143.75)
tx: [55 AA 51 09 00 08 40 A8 02 61 1B]
(3975) bm1370Module: Setting Frequency to 150.00MHz (150.00)
tx: [55 AA 51 09 00 08 40 AF 02 61 19]
(4075) bm1370Module: Setting Frequency to 156.25MHz (156.25)
tx: [55 AA 51 09 00 08 40 B6 02 61 06]
(4175) bm1370Module: Setting Frequency to 162.50MHz (162.50)
tx: [55 AA 51 09 00 08 40 A2 02 51 1B]
(4275) bm1370Module: Setting Frequency to 168.75MHz (168.75)
tx: [55 AA 51 09 00 08 40 A8 02 51 10]
(4375) bm1370Module: Setting Frequency to 175.00MHz (175.00)
tx: [55 AA 51 09 00 08 40 AE 02 51 0A]
(4475) bm1370Module: Setting Frequency to 181.25MHz (181.25)
tx: [55 AA 51 09 00 08 40 B4 02 51 18]
(4575) bm1370Module: Setting Frequency to 187.50MHz (187.50)
tx: [55 AA 51 09 00 08 40 BA 02 51 1C]
(4675) bm1370Module: Setting Frequency to 193.75MHz (193.75)
tx: [55 AA 51 09 00 08 40 A0 02 41 14]
(4775) bm1370Module: Setting Frequency to 200.00MHz (200.00)
tx: [55 AA 51 09 00 08 40 A5 02 41 03]
(4875) bm1370Module: Setting Frequency to 206.25MHz (206.25)
tx: [55 AA 51 09 00 08 40 AA 02 41 1F]
(4975) bm1370Module: Setting Frequency to 212.50MHz (212.50)
tx: [55 AA 51 09 00 08 40 AF 02 41 08]
(5075) bm1370Module: Setting Frequency to 218.75MHz (218.75)
tx: [55 AA 51 09 00 08 40 B4 02 41 02]
(5175) bm1370Module: Setting Frequency to 225.00MHz (225.00)
tx: [55 AA 51 09 00 08 40 B9 02 41 0B]
(5275) bm1370Module: Setting Frequency to 231.25MHz (231.25)
tx: [55 AA 51 09 00 08 40 BE 02 41 09]
(5375) bm1370Module: Setting Frequency to 237.50MHz (237.50)
tx: [55 AA 51 09 00 08 50 C3 02 41 01]
(5475) bm1370Module: Setting Frequency to 243.75MHz (243.75)
tx: [55 AA 51 09 00 08 40 A0 02 31 18]
(5575) bm1370Module: Setting Frequency to 250.00MHz (250.00)
tx: [55 AA 51 09 00 08 40 A4 02 31 17]
(5675) bm1370Module: Setting Frequency to 256.25MHz (256.25)
tx: [55 AA 51 09 00 08 40 A8 02 31 06]
(5775) bm1370Module: Setting Frequency to 262.50MHz (262.50)
tx: [55 AA 51 09 00 08 40 AC 02 31 09]
(5875) bm1370Module: Setting Frequency to 268.75MHz (268.75)
tx: [55 AA 51 09 00 08 40 B0 02 31 01]
(5975) bm1370Module: Setting Frequency to 275.00MHz (275.00)
tx: [55 AA 51 09 00 08 40 B4 02 31 0E]
(6075) bm1370Module: Setting Frequency to 281.25MHz (281.25)
tx: [55 AA 51 09 00 08 40 A1 02 60 18]
(6175) bm1370Module: Setting Frequency to 287.50MHz (287.50)
tx: [55 AA 51 09 00 08 40 BC 02 31 10]
(6275) bm1370Module: Setting Frequency to 293.75MHz (293.75)
tx: [55 AA 51 09 00 08 40 A8 02 60 1E]
(6375) bm1370Module: Setting Frequency to 300.00MHz (300.00)
tx: [55 AA 51 09 00 08 50 C4 02 31 0F]
(6475) bm1370Module: Setting Frequency to 306.25MHz (306.25)
tx: [55 AA 51 09 00 08 40 AF 02 60 1C]
(6575) bm1370Module: Setting Frequency to 312.50MHz (312.50)
tx: [55 AA 51 09 00 08 50 CC 02 31 11]
(6675) bm1370Module: Setting Frequency to 318.75MHz (318.75)
tx: [55 AA 51 09 00 08 40 B6 02 60 03]
(6775) bm1370Module: Setting Frequency to 325.00MHz (325.00)
tx: [55 AA 51 09 00 08 50 D4 02 31 16]
(6875) bm1370Module: Setting Frequency to 331.25MHz (331.25)
tx: [55 AA 51 09 00 08 40 A2 02 50 1E]
(6975) bm1370Module: Setting Frequency to 337.50MHz (337.50)
tx: [55 AA 51 09 00 08 40 A5 02 50 1C]
(7075) bm1370Module: Setting Frequency to 343.75MHz (343.75)
tx: [55 AA 51 09 00 08 40 A8 02 50 15]
(7175) bm1370Module: Setting Frequency to 350.00MHz (350.00)
tx: [55 AA 51 09 00 08 40 AB 02 50 18]
(7275) bm1370Module: Setting Frequency to 356.25MHz (356.25)
tx: [55 AA 51 09 00 08 40 AE 02 50 0F]
(7375) bm1370Module: Setting Frequency to 362.50MHz (362.50)
tx: [55 AA 51 09 00 08 40 B1 02 50 0A]
(7475) bm1370Module: Setting Frequency to 368.75MHz (368.75)
tx: [55 AA 51 09 00 08 40 B4 02 50 1D]
(7575) bm1370Module: Setting Frequency to 375.00MHz (375.00)
tx: [55 AA 51 09 00 08 40 B7 02 50 10]
(7675) bm1370Module: Setting Frequency to 381.25MHz (381.25)
tx: [55 AA 51 09 00 08 40 BA 02 50 19]
(7775) bm1370Module: Setting Frequency to 387.50MHz (387.50)
tx: [55 AA 51 09 00 08 40 BD 02 50 1B]
(7875) bm1370Module: Setting Frequency to 393.75MHz (393.75)
tx: [55 AA 51 09 00 08 40 A0 02 40 11]
(7975) bm1370Module: Setting Frequency to 400.00MHz (400.00)
tx: [55 AA 51 09 00 08 50 C3 02 50 1E]
(8075) bm1370Module: Setting Frequency to 406.25MHz (406.25)
tx: [55 AA 51 09 00 08 40 A5 02 40 06]
(8175) bm1370Module: Setting Frequency to 412.50MHz (412.50)
tx: [55 AA 51 09 00 08 50 C9 02 50 15]
(8275) bm1370Module: Setting Frequency to 418.75MHz (418.75)
tx: [55 AA 51 09 00 08 40 AA 02 40 1A]
(8375) bm1370Module: Setting Frequency to 425.00MHz (425.00)
tx: [55 AA 51 09 00 08 50 CF 02 50 0F]
(8475) bm1370Module: Setting Frequency to 431.25MHz (431.25)
tx: [55 AA 51 09 00 08 40 AF 02 40 0D]
(8575) bm1370Module: Setting Frequency to 437.50MHz (437.50)
tx: [55 AA 51 09 00 08 50 D5 02 50 1D]
(8675) bm1370Module: Setting Frequency to 443.75MHz (443.75)
tx: [55 AA 51 09 00 08 40 B4 02 40 07]
(8775) bm1370Module: Setting Frequency to 450.00MHz (450.00)
tx: [55 AA 51 09 00 08 50 DB 02 50 19]
(8875) bm1370Module: Setting Frequency to 456.25MHz (456.25)
tx: [55 AA 51 09 00 08 40 B9 02 40 0E]
(8975) bm1370Module: Setting Frequency to 462.50MHz (462.50)
tx: [55 AA 51 09 00 08 50 E1 02 50 1C]
(9075) bm1370Module: Setting Frequency to 468.75MHz (468.75)
tx: [55 AA 51 09 00 08 40 BE 02 40 0C]
(9175) bm1370Module: Setting Frequency to 475.00MHz (475.00)
tx: [55 AA 51 09 00 08 50 E7 02 50 06]
(9275) bm1370Module: Setting Frequency to 481.25MHz (481.25)
tx: [55 AA 51 09 00 08 50 C3 02 40 04]
(9375) bm1370Module: Setting Frequency to 487.50MHz (487.50)
tx: [55 AA 51 09 00 08 50 ED 02 50 0D]
(9475) bm1370Module: Setting Frequency to 493.75MHz (493.75)
tx: [55 AA 51 09 00 08 40 A0 02 30 1D]
(9575) bm1370Module: Setting Frequency to 500.00MHz (500.00)
tx: [55 AA 51 09 00 08 40 A2 02 30 08]
(9675) bm1370Module: Setting Frequency to 506.25MHz (506.25)
tx: [55 AA 51 09 00 08 40 A4 02 30 12]
(9775) bm1370Module: Setting Frequency to 512.50MHz (512.50)
tx: [55 AA 51 09 00 08 40 A6 02 30 07]
(9875) bm1370Module: Setting Frequency to 518.75MHz (518.75)
tx: [55 AA 51 09 00 08 40 A8 02 30 03]
(9975) bm1370Module: Setting Frequency to 525.00MHz (525.00)
tx: [55 AA 51 09 00 10 00 00 1E B5 0F]
(10075) self_test: 1 chips detected, 1 expected
(10075) bm1370Module: Setting max baud of 1000000 
tx: [55 AA 51 09 00 28 11 30 02 00 03]
(10085) serial: Changing UART baud to 1000000
(11085) bm1370Module: Setting ASIC difficulty mask to 7
tx: [55 AA 51 09 00 14 00 00 00 E0 04]
(11095) self_test: Sending work
(11105) bm1370Module: Job ID: 18, Core: 69/2, Ver: 001A4000
(11105) self_test: Nonce 3095331466 Nonce difficulty 46.90853208344006475272180978208780.
(11105) self_test: 2825.171713 Gh/s  , duration 0.012162
(11125) bm1370Module: Job ID: 18, Core: 105/10, Ver: 005B4000
(11125) self_test: Nonce 3579380690 Nonce difficulty 9.08560889412638772455466096289456.
(11125) self_test: 2106.796147 Gh/s  , duration 0.032618
(11145) bm1370Module: Job ID: 18, Core: 114/9, Ver: 00A12000
(11145) self_test: Nonce 688522724 Nonce difficulty 56.78132543498190898390021175146103.
(11155) self_test: 1840.996144 Gh/s  , duration 0.055991
(11155) bm1370Module: Job ID: 18, Core: 21/13, Ver: 00BFA000
(11165) self_test: Nonce 132973098 Nonce difficulty 10.30026946249585861892228422220796.
(11175) self_test: 1889.636801 Gh/s  , duration 0.072733
(11175) bm1370Module: Job ID: 18, Core: 71/6, Ver: 00EEC000
(11185) self_test: Nonce 3877437838 Nonce difficulty 12.50166165390199246587599191116169.
(11195) self_test: 1817.321724 Gh/s  , duration 0.094534
(11215) bm1370Module: Job ID: 18, Core: 72/7, Ver: 017AE000
(11215) self_test: Nonce 421201296 Nonce difficulty 205.16276698851780224686081055551767.
(11225) self_test: 1648.014950 Gh/s  , duration 0.125095
(11285) bm1370Module: Job ID: 18, Core: 53/12, Ver: 024D8000
(11285) self_test: Nonce 471793770 Nonce difficulty 18.15580714993782152077983482740819.
(11285) self_test: 1252.627030 Gh/s  , duration 0.192011
(11305) bm1370Module: Job ID: 18, Core: 37/5, Ver: 02A4A000
(11315) self_test: Nonce 3737059914 Nonce difficulty 29.06699928417114620060601737350225.
(11315) self_test: 1247.256663 Gh/s  , duration 0.220386
(11345) bm1370Module: Job ID: 18, Core: 57/3, Ver: 031E6000
(11355) self_test: Nonce 2322138226 Nonce difficulty 13.96450421696506261071135668316856.
(11355) self_test: 1190.488207 Gh/s  , duration 0.259757
(11395) bm1370Module: Job ID: 18, Core: 65/6, Ver: 03A6C000
(11395) self_test: Nonce 2619670914 Nonce difficulty 10.85713927935993083906396350357682.
(11395) self_test: 1135.213643 Gh/s  , duration 0.302672
(11405) bm1370Module: Job ID: 18, Core: 48/0, Ver: 03B20000
(11415) self_test: Nonce 2845966688 Nonce difficulty 16.64329129234445048268753453157842.
(11415) self_test: 1183.571918 Gh/s  , duration 0.319336
(11425) bm1370Module: Job ID: 18, Core: 73/6, Ver: 03EAC000
(11435) self_test: Nonce 2365194642 Nonce difficulty 8.79606344137725493226298567606136.
(11445) self_test: 1208.619335 Gh/s  , duration 0.341147
(11465) bm1370Module: Job ID: 18, Core: 21/2, Ver: 04884000
(11465) self_test: Nonce 882049834 Nonce difficulty 28.09970398970457949872070457786322.
(11475) self_test: 1190.001542 Gh/s  , duration 0.375358
(11535) bm1370Module: Job ID: 18, Core: 74/5, Ver: 0568A000
(11535) self_test: Nonce 1432879508 Nonce difficulty 29.46805603652905602984901634044945.
(11545) self_test: 1077.057141 Gh/s  , duration 0.446621
(11545) bm1370Module: Job ID: 18, Core: 24/7, Ver: 0580E000
(11555) self_test: Nonce 849085232 Nonce difficulty 108.19933716494756481552030891180038.
(11565) self_test: 1112.306414 Gh/s  , duration 0.463358
(11565) bm1370Module: Job ID: 18, Core: 27/4, Ver: 05908000
(11585) self_test: Nonce 1856045622 Nonce difficulty 9.49693255673613201395255600800738.
(11585) self_test: 1110.494418 Gh/s  , duration 0.495055
(11625) bm1370Module: Job ID: 18, Core: 108/3, Ver: 06786000
(11625) self_test: Nonce 3767206616 Nonce difficulty 34.15865782662408633996165008284152.
(11625) self_test: 1094.296084 Gh/s  , duration 0.533782
(11635) bm1370Module: Job ID: 18, Core: 121/1, Ver: 06842000
(11645) self_test: Nonce 1967457010 Nonce difficulty 36.67304660876931876600792747922242.
(11655) self_test: 1122.539146 Gh/s  , duration 0.550961
(11745) bm1370Module: Job ID: 18, Core: 81/10, Ver: 07F54000
(11745) self_test: Nonce 3839885474 Nonce difficulty 10.92721501319460664092275692382827.
(11755) self_test: 996.425438 Gh/s  , duration 0.655177
(11755) bm1370Module: Job ID: 18, Core: 103/15, Ver: 07FBE000
(11765) self_test: Nonce 2408972494 Nonce difficulty 28.97807918342899569097426137886941.
(11775) self_test: 1022.185350 Gh/s  , duration 0.672280
(11775) bm1370Module: Job ID: 18, Core: 118/11, Ver: 08396000
(11785) self_test: Nonce 3334472940 Nonce difficulty 8.46953636115654617810832860413939.
(11795) self_test: 1039.897194 Gh/s  , duration 0.693871
(11825) bm1370Module: Job ID: 18, Core: 7/0, Ver: 08FE0000
(11835) self_test: Nonce 3088646158 Nonce difficulty 8.08774303638509906022591167129576.
(11835) self_test: 1021.330453 Gh/s  , duration 0.740127
(11845) bm1370Module: Job ID: 18, Core: 90/4, Ver: 092E8000
(11845) self_test: Nonce 3809346228 Nonce difficulty 8.07534525686779680597737751668319.
(11855) self_test: 1044.322024 Gh/s  , duration 0.756734
(11865) bm1370Module: Job ID: 18, Core: 41/5, Ver: 0960A000
(11865) self_test: Nonce 1918304594 Nonce difficulty 12.14843288383768182825406256597489.
(11875) self_test: 1059.856054 Gh/s  , duration 0.778062
(11965) bm1370Module: Job ID: 18, Core: 26/10, Ver: 0AA74000
(11965) self_test: Nonce 3724411956 Nonce difficulty 13.19233331656962526778897881740704.
(11975) self_test: 980.350006 Gh/s  , duration 0.876211
(11975) bm1370Module: Job ID: 18, Core: 52/5, Ver: 0ABAA000
(11985) self_test: Nonce 325517416 Nonce difficulty 9.52136147125195719809198635630310.
(11995) self_test: 1000.607293 Gh/s  , duration 0.892811
(12025) bm1370Module: Job ID: 18, Core: 96/14, Ver: 0B69C000
(12025) self_test: Nonce 602603968 Nonce difficulty 9.92622756898761515742535266326740.
(12035) self_test: 989.113122 Gh/s  , duration 0.937924
(12035) bm1370Module: Job ID: 18, Core: 9/15, Ver: 0B83E000
(12045) self_test: Nonce 1690632978 Nonce difficulty 14.66191062783922482992693403502926.
(12055) self_test: 1007.771061 Gh/s  , duration 0.954654
(12065) bm1370Module: Job ID: 18, Core: 73/6, Ver: 0BACC000
(12065) self_test: Nonce 4130800786 Nonce difficulty 9.99058349453726535216446791309863.
(12075) self_test: 1020.969370 Gh/s  , duration 0.975967
(12095) bm1370Module: Job ID: 18, Core: 40/6, Ver: 0C38C000
(12095) self_test: Nonce 3349021776 Nonce difficulty 10.59150056774604742315659677842632.
(12105) self_test: 1023.175632 Gh/s  , duration 1.007444
(12105) bm1370Module: Job ID: 18, Core: 25/8, Ver: 0C470000
(12115) self_test: Nonce 157089842 Nonce difficulty 8.09629639893213948198535945266485.
(12125) self_test: 1040.234121 Gh/s  , duration 1.023954
(12155) bm1370Module: Job ID: 18, Core: 24/3, Ver: 0CFA6000
(12155) self_test: Nonce 791740464 Nonce difficulty 17.53348988352425763537212333176285.
(12165) self_test: 1030.750277 Gh/s  , duration 1.066710
(12205) bm1370Module: Job ID: 18, Core: 115/7, Ver: 0D9CE000
(12205) self_test: Nonce 734659302 Nonce difficulty 19.98953685805851776535746466834098.
(12215) self_test: 1013.730151 Gh/s  , duration 1.118514
(12245) bm1370Module: Job ID: 18, Core: 72/9, Ver: 0E0F2000
(12245) self_test: Nonce 54985872 Nonce difficulty 20.87479688190073545683844713494182.
(12245) self_test: 1011.189353 Gh/s  , duration 1.155304
(12305) bm1370Module: Job ID: 18, Core: 22/15, Ver: 0ED5E000
(12305) self_test: Nonce 3894018348 Nonce difficulty 41.82666908132255656482811900787055.
(12315) self_test: 987.198049 Gh/s  , duration 1.218186
(12315) bm1370Module: Job ID: 18, Core: 103/0, Ver: 0EEA0000
(12325) self_test: Nonce 330629326 Nonce difficulty 8.67974557966062754132963164011016.
(12335) self_test: 1001.633758 Gh/s  , duration 1.234933
(12395) bm1370Module: Job ID: 18, Core: 53/5, Ver: 0FEAA000
(12395) self_test: Nonce 4244898154 Nonce difficulty 13.99110670806324741022308444371447.
(12405) self_test: 972.734369 Gh/s  , duration 1.306945
(12405) bm1370Module: Job ID: 18, Core: 34/10, Ver: 0FED4000
(12415) self_test: Nonce 3802006340 Nonce difficulty 10.14457210188510671855510736349970.
(12425) self_test: 986.364230 Gh/s  , duration 1.323720
(12425) bm1370Module: Job ID: 18, Core: 113/9, Ver: 10012000
(12435) self_test: Nonce 3743285474 Nonce difficulty 11.33085197312985670237139856908470.
(12445) self_test: 996.044747 Gh/s  , duration 1.345351
(12455) bm1370Module: Job ID: 18, Core: 117/3, Ver: 10466000
(12455) self_test: Nonce 2809528810 Nonce difficulty 51.32804769175664461045016651041806.
(12465) self_test: 1005.520407 Gh/s  , duration 1.366844
(12545) bm1370Module: Job ID: 18, Core: 117/1, Ver: 11B42000
(12545) self_test: Nonce 1066468330 Nonce difficulty 13.33855352277797656768143497174606.
(12545) self_test: 968.959090 Gh/s  , duration 1.453879
(12575) bm1370Module: Job ID: 18, Core: 80/6, Ver: 1208C000
(12575) self_test: Nonce 3127575712 Nonce difficulty 88.92579162781308355079090688377619.
(12575) self_test: 974.731842 Gh/s  , duration 1.480519
(12615) bm1370Module: Job ID: 18, Core: 90/12, Ver: 128B8000
(12615) self_test: Nonce 413532852 Nonce difficulty 19.02012317518970974106196081265807.
(12615) self_test: 970.359090 Gh/s  , duration 1.522600
(12665) bm1370Module: Job ID: 18, Core: 51/12, Ver: 13318000
(12665) self_test: Nonce 1542324582 Nonce difficulty 17.04307353855813289555953815579414.
(12675) self_test: 959.615100 Gh/s  , duration 1.575453
(12725) bm1370Module: Job ID: 18, Core: 38/15, Ver: 13F3E000
(12725) self_test: Nonce 3726378060 Nonce difficulty 12.43764547174390955319722706917673.
(12735) self_test: 944.354733 Gh/s  , duration 1.637296
(12775) bm1370Module: Job ID: 18, Core: 8/10, Ver: 14934000
(12775) self_test: Nonce 3393716752 Nonce difficulty 13.99499356654293613644313154509291.
(12785) self_test: 936.154465 Gh/s  , duration 1.688341
(12795) bm1370Module: Job ID: 18, Core: 101/1, Ver: 14D02000
(12795) self_test: Nonce 1507656650 Nonce difficulty 26.55879355888631465631988248787820.
(12805) self_test: 945.686780 Gh/s  , duration 1.707656
(12825) bm1370Module: Job ID: 18, Core: 66/14, Ver: 1521C000
(12825) self_test: Nonce 3553231492 Nonce difficulty 147.71275905622917434811824932694435.
(12825) self_test: 951.163699 Gh/s  , duration 1.733947
(12855) bm1370Module: Job ID: 18, Core: 71/15, Ver: 158DE000
(12855) self_test: Nonce 806224782 Nonce difficulty 27.44885512213531342240457888692617.
(12865) self_test: 952.075339 Gh/s  , duration 1.768376
(12865) bm1370Module: Job ID: 18, Core: 37/9, Ver: 15912000
(12875) self_test: Nonce 1852375114 Nonce difficulty 36.18711909344741428640190861187875.
(12885) self_test: 962.567126 Gh/s  , duration 1.784797
(12935) bm1370Module: Job ID: 18, Core: 87/4, Ver: 16708000
(12935) self_test: Nonce 2064646830 Nonce difficulty 13.43223325990645200533890601946041.
(12935) self_test: 951.757120 Gh/s  , duration 1.841170
(12975) bm1370Module: Job ID: 18, Core: 82/15, Ver: 1703E000
(12975) self_test: Nonce 3812098980 Nonce difficulty 174.85157893099056991559336893260479.
(12985) self_test: 946.348726 Gh/s  , duration 1.888000
(12985) bm1370Module: Job ID: 18, Core: 52/6, Ver: 1702C000
(12995) self_test: Nonce 1926366056 Nonce difficulty 9.42245171243517809500644943909720.
(13005) self_test: 956.117398 Gh/s  , duration 1.904647
(13015) bm1370Module: Job ID: 18, Core: 112/3, Ver: 17646000
(13015) self_test: Nonce 1774453728 Nonce difficulty 13.11853428587771652757965057389811.
(13025) self_test: 963.134619 Gh/s  , duration 1.926445
(13035) bm1370Module: Job ID: 18, Core: 37/14, Ver: 179FC000
(13035) self_test: Nonce 4054974794 Nonce difficulty 27640.04290963592939078807830810546875.
(13045) self_test: 970.184048 Gh/s  , duration 1.947863
(13135) bm1370Module: Job ID: 18, Core: 7/3, Ver: 18FE6000
(13145) self_test: Nonce 4053926414 Nonce difficulty 87.79714350600656302958668675273657.
(13145) self_test: 938.026826 Gh/s  , duration 2.051269
(13165) bm1370Module: Job ID: 18, Core: 16/5, Ver: 1944A000
(13165) self_test: Nonce 840827424 Nonce difficulty 10.07415947583436199863626825390384.
(13165) self_test: 944.778520 Gh/s  , duration 2.072978
(13285) bm1370Module: Job ID: 18, Core: 8/14, Ver: 1AC9C000
(13285) self_test: Nonce 748094480 Nonce difficulty 57.13968810720911051248549483716488.
(13295) self_test: 907.037929 Gh/s  , duration 2.197113
(13385) bm1370Module: Job ID: 18, Core: 38/15, Ver: 1C09E000
(13395) self_test: Nonce 4172219212 Nonce difficulty 8.24113661135610087171698978636414.
(13395) self_test: 881.528848 Gh/s  , duration 2.299669
(13405) bm1370Module: Job ID: 18, Core: 21/0, Ver: 1C260000
(13405) self_test: Nonce 4068279082 Nonce difficulty 215.07439622134953083332220558077097.
(13415) self_test: 890.242453 Gh/s  , duration 2.315756
(13425) bm1370Module: Job ID: 18, Core: 26/10, Ver: 1C874000
(13435) self_test: Nonce 2920547124 Nonce difficulty 16.99467922029148780893592629581690.
(13435) self_test: 895.747752 Gh/s  , duration 2.339882
(13455) bm1370Module: Job ID: 18, Core: 87/5, Ver: 1CDEA000
(13455) self_test: Nonce 3767665326 Nonce difficulty 8.19106512513363149707856791792437.
(13465) self_test: 899.927078 Gh/s  , duration 2.367196
(13495) bm1370Module: Job ID: 18, Core: 71/11, Ver: 1D636000
(13505) self_test: Nonce 2823815566 Nonce difficulty 8.91211664562331762340363638941199.
(13505) self_test: 898.327737 Gh/s  , duration 2.409659
(13525) bm1370Module: Job ID: 18, Core: 37/11, Ver: 1DAD6000
(13525) self_test: Nonce 2887648586 Nonce difficulty 62.65069554753830516347079537808895.
(13525) self_test: 903.635154 Gh/s  , duration 2.433530
(13565) bm1370Module: Job ID: 18, Core: 115/8, Ver: 1E390000
(13565) self_test: Nonce 2318401766 Nonce difficulty 19.59783545693336037629705970175564.
(13575) self_test: 901.283410 Gh/s  , duration 2.478003
(13605) bm1370Module: Job ID: 18, Core: 84/15, Ver: 1E8FE000
(13605) self_test: Nonce 338232232 Nonce difficulty 9.03940792114704727566731889965013.
(13615) self_test: 900.856321 Gh/s  , duration 2.517319
(13655) bm1370Module: Job ID: 18, Core: 16/8, Ver: 1F4B0000
(13655) self_test: Nonce 2813526560 Nonce difficulty 26.81900219861185519221180584281683.
(13665) self_test: 897.101878 Gh/s  , duration 2.566155
(13675) bm1370Module: Job ID: 18, Core: 39/1, Ver: 1F822000
(13675) self_test: Nonce 2701066318 Nonce difficulty 17.12594843599275051815311599057168.
(13685) self_test: 904.399991 Gh/s  , duration 2.583439
(13725) bm1370Module: Job ID: 18, Core: 69/2, Ver: 001A4000
(13725) self_test: Nonce 3095331466 Nonce difficulty 46.90853208344006475272180978208780.
(13725) self_test: 900.671717 Gh/s  , duration 2.632282
(13745) bm1370Module: Job ID: 18, Core: 105/10, Ver: 005B4000
(13745) self_test: Nonce 3579380690 Nonce difficulty 9.08560889412638772455466096289456.
(13745) self_test: 906.662537 Gh/s  , duration 2.652786
(13765) bm1370Module: Job ID: 18, Core: 114/9, Ver: 00A12000
(13765) self_test: Nonce 688522724 Nonce difficulty 56.78132543498190898390021175146103.
(13775) self_test: 911.844820 Gh/s  , duration 2.675391
(13775) bm1370Module: Job ID: 18, Core: 21/13, Ver: 00BFA000
(13785) self_test: Nonce 132973098 Nonce difficulty 10.30026946249585861892228422220796.
(13795) self_test: 918.892487 Gh/s  , duration 2.692264
(13795) bm1370Module: Job ID: 18, Core: 71/6, Ver: 00EEC000
(13805) self_test: Nonce 3877437838 Nonce difficulty 12.50166165390199246587599191116169.
(13815) self_test: 924.248574 Gh/s  , duration 2.713838
(13905) bm1370Module: Job ID: 18, Core: 53/12, Ver: 024D8000
(13905) self_test: Nonce 471793770 Nonce difficulty 18.15580714993782152077983482740819.
(13905) self_test: 904.222935 Gh/s  , duration 2.811940
(13925) bm1370Module: Job ID: 18, Core: 37/5, Ver: 02A4A000
(13935) self_test: Nonce 3737059914 Nonce difficulty 29.06699928417114620060601737350225.
(13935) self_test: 907.228053 Gh/s  , duration 2.840499
(13965) bm1370Module: Job ID: 18, Core: 57/3, Ver: 031E6000
(13975) self_test: Nonce 2322138226 Nonce difficulty 13.96450421696506261071135668316856.
(13975) self_test: 906.773251 Gh/s  , duration 2.879816
(14015) bm1370Module: Job ID: 18, Core: 65/6, Ver: 03A6C000
(14015) self_test: Nonce 2619670914 Nonce difficulty 10.85713927935993083906396350357682.
(14015) self_test: 905.228598 Gh/s  , duration 2.922687
(14025) bm1370Module: Job ID: 18, Core: 48/0, Ver: 03B20000
(14035) self_test: Nonce 2845966688 Nonce difficulty 16.64329129234445048268753453157842.
(14035) self_test: 911.596058 Gh/s  , duration 2.939964
(14045) bm1370Module: Job ID: 18, Core: 73/6, Ver: 03EAC000
(14055) self_test: Nonce 2365194642 Nonce difficulty 8.79606344137725493226298567606136.
(14065) self_test: 916.746455 Gh/s  , duration 2.960927
(14085) bm1370Module: Job ID: 18, Core: 21/2, Ver: 04884000
(14085) self_test: Nonce 882049834 Nonce difficulty 28.09970398970457949872070457786322.
(14085) self_test: 917.737553 Gh/s  , duration 2.995169
(14155) bm1370Module: Job ID: 18, Core: 74/5, Ver: 0568A000
(14155) self_test: Nonce 1432879508 Nonce difficulty 29.46805603652905602984901634044945.
(14165) self_test: 907.331843 Gh/s  , duration 3.067388
(14165) self_test: Hashrate: 907.331843
(14175) self_test: Voltage: 1117
(14175) self_test: Power: 18.105835, Voltage: 1.148438, Current 15.765625
E (14185) self_test: TPS546 Power Draw Failed, target 11.00
(14195) self_test: SELF TESTS FAIL -- Press RESET to continue

Script done on Fri Feb  7 23:10:43 2025
```

### MaSe-Time on 2025-03-02

I'm having the same problem here with a bitaxe gamma 601, trying multiple different clocks/voltages but after a random amount of time it just stops mining and only a full power off and on again will clear it. Is this something that could be fixed with a firmware update? 

### skot on 2025-03-02

> I'm having the same problem here with a bitaxe gamma 601, trying multiple different clocks/voltages but after a random amount of time it just stops mining and only a full power off and on again will clear it. Is this something that could be fixed with a firmware update?

Yes, I think this can be fixed with a firmware update. I'm going to try and get this into the next release, v2.6.0

### skot on 2025-03-02

> I've got same issue for a couple of weeks now, if I recall, it all started when I bumped to v2.5.1. For a couple of days, reconnecting the PSU would bring it back up but now has gone completely dead. Not even flashing older firmware versions works. With 2.5.1 I've got no useful logs but factory resetting with 2.4.5 brings interesting results from the self test.
> 
> It is unclear to me if there is still a fix for the TPS546 as flashing other versions doesn't bring it back to life.
> 
> ```
> Script started on Fri Feb  7 23:10:14 2025
> command: screen /dev/tty.usbmodem14101 115200
> I (158) esp_image: segment 1: paddr=0003d10c vaddr=3fc9c800 size
> 
> (2485) bm1370Module: 1 chip(s) detected on the chain, expected 1
> ~snip
> (14175) self_test: Voltage: 1117
> (14175) self_test: Power: 18.105835, Voltage: 1.148438, Current 15.765625
> E (14185) self_test: TPS546 Power Draw Failed, target 11.00
> (14195) self_test: SELF TESTS FAIL -- Press RESET to continue
> 
> Script done on Fri Feb  7 23:10:43 2025
> ```

This seems to be a different issue. leave you bitaxe unplugged for a few minutes and then try the selftest again.


### MaSe-Time on 2025-03-02

> > I'm having the same problem here with a bitaxe gamma 601, trying multiple different clocks/voltages but after a random amount of time it just stops mining and only a full power off and on again will clear it. Is this something that could be fixed with a firmware update?
> 
> Yes, I think this can be fixed with a firmware update. I'm going to try and get this into the next release, v2.6.0

Brilliant, it's my first miner and was thinking of sending it back 👀

Any idea when v2.6.0 maybe released? 🙈

### MaSe-Time on 2025-03-03

> > I'm having the same problem here with a bitaxe gamma 601, trying multiple different clocks/voltages but after a random amount of time it just stops mining and only a full power off and on again will clear it. Is this something that could be fixed with a firmware update?
> 
> Yes, I think this can be fixed with a firmware update. I'm going to try and get this into the next release, v2.6.0

Another suggestion. I find hashing is higher when the ASIC temp is around the 60c mark. If I set the fan to auto (I have a Argon Thrml installed) it doesn't spin the fan down slow enough so I end up with a very cold ASIC. Is there a way to add in to the GUI under settings a "target temp" that the fan will auto adjust to try and meet? It would need to be able to use the full range of 0% RPM to 100% RPM though as when mine stops hashing with the issue above, the slowest the fan spins is 35% even when the ASIC shows -1 degrees.

Anyway, just a suggestion.

### MyOwn2C on 2025-03-05

> > I'm having the same problem here with a bitaxe gamma 601, trying multiple different clocks/voltages but after a random amount of time it just stops mining and only a full power off and on again will clear it. Is this something that could be fixed with a firmware update?
> 
> Yes, I think this can be fixed with a firmware update. I'm going to try and get this into the next release, v2.6.0

I am seeing this issue reported almost every day now, by users from different sources: TG, X, FB, etc
Only fix that seems to work is power down and power back up again.

### skot on 2025-03-05

> I am seeing this issue reported almost every day now, by users from different sources: TG, X, FB, etc Only fix that seems to work is power down and power back up again.

I have a fix that I _think_ should fix this, but it's tough to know for sure since I can't reproduce the bug myself. If you or anyone you hear about can reliably reproduce this, and can also handle flashing beta firmware, please lmk on OSMU



### MaSe-Time on 2025-03-05

> > I am seeing this issue reported almost every day now, by users from different sources: TG, X, FB, etc Only fix that seems to work is power down and power back up again.
> 
> I have a fix that I _think_ should fix this, but it's tough to know for sure since I can't reproduce the bug myself. If you or anyone you hear about can reliably reproduce this, and can also handle flashing beta firmware, please lmk on OSMU

I'm happy to try, just bought a second one to try as it is so annoying constantly stopping.


### skot on 2025-03-05

> I'm happy to try, just bought a second one to try as it is so annoying constantly stopping.

If my theory is correct, this is caused by a power supply fault. So the question then is; why are you having so many power supply faults? Can you give me more details about your setup?

- How often does this happen?
- What Bitaxe hardware version do you have?
- Where did you get it?
- What power supply do you have?
- Anything else special about your setup?

### MaSe-Time on 2025-03-05

I have this gamma from Amazon
https://amzn.eu/d/a5t9QLl

Bought this 100w psu as well
https://amzn.eu/d/4xAR5fq 

But to be honest despite there being no dips in voltage I had thought a better quality PSU may be in order so am waiting for a 200w meanwell to be delivered. 

I had it running for about 4 or 5 days gradually increasing the clocks no problem but then all of a sudden it would just crash. Bringing it back to stock seems to run OK but it has crashed on a couple of occasions after 6 or 8 hours at close to stock clocks and voltages. 

I've tried the latest beta firmware with no luck and flashing back to 2.5.1 is just the same. 

Is there a possibility of damaging the hardware overclocking? My temps have always been good as you can see my cooling is pretty good, I keep it at 60c on the ascic and the vrm hasn't ever gone above 74

Attached is my setup

![Image](https://github.com/user-attachments/assets/226b9e8b-3a55-4b5c-b06b-9f3f62258da8)
![Image](https://github.com/user-attachments/assets/0a06bf7a-6909-4e00-9acd-e2d274e2bfc3)

Thank you for your help



### MaSe-Time on 2025-03-05

> > I'm happy to try, just bought a second one to try as it is so annoying constantly stopping.
> 
> If my theory is correct, this is caused by a power supply fault. So the question then is; why are you having so many power supply faults? Can you give me more details about your setup?
> 
> * How often does this happen?
> * What Bitaxe hardware version do you have?
> * Where did you get it?
> * What power supply do you have?
> * Anything else special about your setup?

FYI my new one just did it, same set up as above had clocks at 925mhz 1380mV. Only thing I can think is it's the power supply. Mean We'll 200w coming in a couple of days

### skot on 2025-03-05

> FYI my new one just did it, same set up as above had clocks at 925mhz 1380mV. Only thing I can think is it's the power supply. Mean We'll 200w coming in a couple of days

Can you try running it for a while on defaults and see if it happens?



### MaSe-Time on 2025-03-05

Sure, I'll run them both overnight at default 

### MaSe-Time on 2025-03-06

Ok, New one stopped over night and dropped to 5w. I restarted this morning and its stopped again, this time it looks like its hashing but it isn't.

![Image](https://github.com/user-attachments/assets/d88b5102-a982-40ac-8521-3477a7287b0d)

### MaSe-Time on 2025-03-06

> > > I'm happy to try, just bought a second one to try as it is so annoying constantly stopping.
> > 
> > 
> > If my theory is correct, this is caused by a power supply fault. So the question then is; why are you having so many power supply faults? Can you give me more details about your setup?
> > 
> > * How often does this happen?
> > * What Bitaxe hardware version do you have?
> > * Where did you get it?
> > * What power supply do you have?
> > * Anything else special about your setup?
> 
> FYI my new one just did it, same set up as above had clocks at 925mhz 1380mV. Only thing I can think is it's the power supply. Mean We'll 200w coming in a couple of days

And again looks like its hashing but isn't 

![Image](https://github.com/user-attachments/assets/2196fe25-d283-48db-8ea6-64412ac6be0b)

### skot on 2025-03-06

This seems like a different issue. You should contact the seller about this.

### MaSe-Time on 2025-03-06

> This seems like a different issue. You should contact the seller about this.

OK, I'll return that one. It still did the original fault though whereby it stopped hashing and dropped to 5w much like my first one does

### MaSe-Time on 2025-03-08

OK, here's a new one. Both stop hashing at exactly the same time 🤷

Running on the new mean well lrs-200-5

![Image](https://github.com/user-attachments/assets/381e6150-e452-4924-a015-ec27d7a45d09)

### MaSe-Time on 2025-03-08

Guessing it may be pool related, swapped to eusolo.ckpool.org

### MaSe-Time on 2025-03-08

> Guessing it may be pool related, swapped to eusolo.ckpool.org

OK, it's not the pool, 10 mins in it did it again. This is a nightmare 🙄

### benjamin-wilson on 2025-03-08

> > Guessing it may be pool related, swapped to eusolo.ckpool.org
> 
> OK, it's not the pool, 10 mins in it did it again. This is a nightmare 🙄

Unstable ASIC, return to defaults

### MaSe-Time on 2025-03-08

> > > Guessing it may be pool related, swapped to eusolo.ckpool.org
> > 
> > 
> > OK, it's not the pool, 10 mins in it did it again. This is a nightmare 🙄
> 
> Unstable ASIC, return to defaults

Both at exactly the same time both clocked differently? 

### skot on 2025-03-08

Are these attached to the same power supply? Same power strip?

### MaSe-Time on 2025-03-08

> Both connected to my new mean well lrs-200-5. Outputting 5.4v. 

The Bitaxe max input voltage is 5.5V. Maybe you are getting a VIN overvoltage fault? Can you try turning this down so that all connected Bitaxe are at or below 5V and see if the problem persists?


### MaSe-Time on 2025-03-09

1 and 2 both dropped to 5w after 1.2 hours and 2.4 hours respectively. They then after an hour or so both stopped hashing but looked like they were hashing so put clocks and voltages to default and warm restarted them. 

They then both stopped hashing over night again but were able to be warm restarted again this morning.

Unit 3 continues to hash at 675 1280mV.

I pinged them all and all were getting 30 to 40ms with the occasional high ping in the low 100ms

Do you have any idea when 2.6.0 maybe released so I can try it before returning at least two of these?

Thanks for listening 

### skot on 2025-03-09

> 1 and 2 both dropped to 5w after 1.2 hours and 2.4 hours respectively. They then after an hour or so both stopped hashing but looked like they were hashing so put clocks and voltages to default and warm restarted them. 
> 
> They then both stopped hashing over night again but were able to be warm restarted again this morning.
> 
> Unit 3 continues to hash at 675 1280mV.
> 
> Do you have any idea when 2.6.0 maybe released so I can try it before returning at least two of these?
> 
> Thanks for listening 

We are targeting the end of March for the v2.6.0 release. I don't think this is going to solve your problem though.

This upcoming release will still stop mining as a result of a power fault like this. It will show a banner in AxeOS and require a manual reset, just like overtemp mode.

I think in your case the Bitaxe voltage regulator (TPS546) is shutting down because of a fault situation occurring on your Bitaxe or from your PSU. There isn't much esp-miner can do about that besides just turn off and let you know something is wrong. 


### MaSe-Time on 2025-03-09

Thanks Skot, I appreciate your insights. 

Looks like I'll be returning two of these. The third one seems stable at the moment and I've just put an Argon THRML on it and copper heatsinks.

Do you think in these instances it could reboot itself as the whole point of these after initially playing around with clocks etc is to leave them going with little to no intervention.

Could be a warning come up once logged in to say something along the lines of "system auto rebooted x times due to x, check psu/clocks etc" 

Could set it so it can auto reboot only 4/5 times in a 24 hour period after which it defaults to an error state until you log in? 

Just for the record this occurred with two separate power supplies, a cheap 100w amazon one and a better quality meanwell. 

Again, thanks for your insights, much appreciated 


### skot on 2025-03-09

The bug we are working on fixing here is this no-hashing mode that a **warm restart _does not_ fix**.  I'd like to stay focused on that here so we can get it resolved.

I created https://github.com/skot/ESP-Miner/issues/752 to track the isssue that a warm restart _does_ fix.

### MaSe-Time on 2025-03-09

> > Both connected to my new mean well lrs-200-5. Outputting 5.4v.
> 
> The Bitaxe max input voltage is 5.5V. Maybe you are getting a VIN overvoltage fault? Can you try turning this down so that all connected Bitaxe are at or below 5V and see if the problem persists?

I missed this skot, I've dialed it down so the two that keep crashing are showing 5v now. The third one is currently on a thinner gauge wire so is 0.2v lower due to droop. Will update 🙈

### MaSe-Time on 2025-03-10

Ok, my last gasp attempt was to move all three units out of my front cupboard and next to an additional router in my rear outbuilding. Tested pings and all sub 5ms.... 12 hours gone by and no drop outs at all no drop to 5w and stop hashing which requires a hard reset and no stop hashing but still pulling the same power and soft reset starts it again.

Moral of the story, if you think you have adequate wifi signal, you haven't! Move them closer to the router!!

Ill post this in the other thread you created as well skoot.

### MavenCH on 2025-03-10

Evening everyone

I have had the same problem since last week.
It worked great until it dropped to 0.
I tried restarting via the website and also disconnecting the miner from the power for a few minutes without success.
Changing the pool didn't change anything and neither did placing the miner next to an access point.

Then I tried to reload the firmware but also without success.
Downgrading to e.g. 2.5.0 has also had no effect, nor has giving it more power or less.

I get the same messages in the log and sometimes the following:
`₿ (314651) stratum_task: rx: {"id":null,"method":"mining.set_difficulty","params":[128]}
₿ (314661) stratum_task: Set stratum difficulty: 128
₿ (314661) stratum_task: rx: {"id":null,"method":"mining.notify","params":["d3ace4","5dd991299afabe1cc5097059607430ed5f242e6c00016d4b0000000000000000","02000000010000000000000000000000000000000000000000000000000000000000000000ffffffff1703a4890d5075626c69632d506f6f6c","ffffffff02102cc8120000000017a914b46e629336cac9252929b9808cb1ea7d4af14f59870000000000000000266a24aa21a9ed9a03889efaed8f47ae98bd6be0d84cb74d478623bb9ca2eae09f654ef250167500000000",["1fd29ed19514cd341321c814064fd244c2e70ed418b6ddb5a23fbc0982081ee6","8df0d6e9ff48ef975b883f2982616af4763f3ec0262675cdc68a0a92024e0f40","f7f0c15e1a6ac265228de4a4aa44a64cf58e8c7bffbcb9ff282149faa8b247ed","e02d42563a304b08529706165c9c5d8647b8b0fa141fff307ee2351a3a8df0a1","7adeb112a0a0654a83d332d9f4fdddbaa634b0356f14938ba6ad6a6015c6191f","fa2867ceca90aab4ca25952d3fa358ecb9efac1342715206653a37c8dfd08a50","1f330e4b1f873be30f86cb7ca95132c4723cafa0713caaf24087d68da569fdd3","14fc939db7093f67f1c1379de4d80568bafbf84c7d9252b47d59e9779063f696","17efc5f1f7eb9d5c45c39c0c340c7fa3260a5ebf218eb3d3c85afd4d9adedf72","1f9610c8953ccd75dd2d72f3179602468976408e403ed92dac232d14c0d97fcf","8e558a524b742659605b6f53409f70d605a98791269b1a4a14ac92557cee650d","e601cdaf9aa004c5a725091e6170e1d8a499d962d5ed7b64713f0fb6f028c2de"],"20000000","17028281","67cf2d5e",true]}
₿ (314771) stratum_task: Clean Jobs: clearing queue
₿ (314831) create_jobs_task: New Work Dequeued d3ace4
₿ (314831) ASIC_task: New pool difficulty 128
₿ (343861) stratum_task: rx: {"id":null,"method":"mining.notify","params":["d3b8a9","5dd991299afabe1cc5097059607430ed5f242e6c00016d4b0000000000000000","02000000010000000000000000000000000000000000000000000000000000000000000000ffffffff1703a4890d5075626c69632d506f6f6c","ffffffff02aa8ecd120000000017a914b46e629336cac9252929b9808cb1ea7d4af14f59870000000000000000266a24aa21a9ed5d0f4f3f14e644ebb8312811580931971db38be0dcb57c7cf537dda23e63ddb100000000",["1fd29ed19514cd341321c814064fd244c2e70ed418b6ddb5a23fbc0982081ee6","8df0d6e9ff48ef975b883f2982616af4763f3ec0262675cdc68a0a92024e0f40","b80435c480acc519edc6084a24b58d3c661d6fad86a34028c8df4b4016c0c534","359512eb308b18df351462332b5b709824f81bd216719abf755b65af8968c805","183bf93d099bb630bc3cbb68986e78bdb865d1e47c5e60827a40315fb1d20287","80efdd9ec78db947762b366f9354f3552a4142e0d8271c6a0d52e93ba27c2534","84042d7b1af047236a387a8b51726a1909bf5f4422302649ce96cac3bc2ec124","ccea336f16ba2192fae06e94ed4844500fd8b947d1ad82042d5f4edaa757ed04","22b3742e18cf255546650772800c29cf3f6ecb1374401ff869277eae1f151972","fd95688cab3c91261528912dcaaf4e80f210ac1f0431820ec0ca18e48068ab37","0e34112582af694334c74d32d5c32b33568a6702e3b934732f71dfaf66fa4a0a","58a6464d0ed6732cacafe03221e690010e2eb5fc7c3ed1a937c28e87ed0a84e0"],"20000000","17028281","67cf2d9a",false]}
₿ (344041) create_jobs_task: New Work Dequeued d3b8a9
₿ (374651) stratum_task: rx: {"id":null,"method":"mining.set_difficulty","params":[16]}
₿ (374651) stratum_task: Set stratum difficulty: 16
₿ (374661) stratum_task: rx: {"id":null,"method":"mining.notify","params":["d3b8fe","5dd991299afabe1cc5097059607430ed5f242e6c00016d4b0000000000000000","02000000010000000000000000000000000000000000000000000000000000000000000000ffffffff1703a4890d5075626c69632d506f6f6c","ffffffff02aa8ecd120000000017a914b46e629336cac9252929b9808cb1ea7d4af14f59870000000000000000266a24aa21a9ed5d0f4f3f14e644ebb8312811580931971db38be0dcb57c7cf537dda23e63ddb100000000",["1fd29ed19514cd341321c814064fd244c2e70ed418b6ddb5a23fbc0982081ee6","8df0d6e9ff48ef975b883f2982616af4763f3ec0262675cdc68a0a92024e0f40","b80435c480acc519edc6084a24b58d3c661d6fad86a34028c8df4b4016c0c534","359512eb308b18df351462332b5b709824f81bd216719abf755b65af8968c805","183bf93d099bb630bc3cbb68986e78bdb865d1e47c5e60827a40315fb1d20287","80efdd9ec78db947762b366f9354f3552a4142e0d8271c6a0d52e93ba27c2534","84042d7b1af047236a387a8b51726a1909bf5f4422302649ce96cac3bc2ec124","ccea336f16ba2192fae06e94ed4844500fd8b947d1ad82042d5f4edaa757ed04","22b3742e18cf255546650772800c29cf3f6ecb1374401ff869277eae1f151972","fd95688cab3c91261528912dcaaf4e80f210ac1f0431820ec0ca18e48068ab37","0e34112582af694334c74d32d5c32b33568a6702e3b934732f71dfaf66fa4a0a","58a6464d0ed6732cacafe03221e690010e2eb5fc7c3ed1a937c28e87ed0a84e0"],"20000000","17028281","67cf2d9a",true]}
₿ (374771) stratum_task: Clean Jobs: clearing queue
₿ (374841) create_jobs_task: New Work Dequeued d3b8fe
₿ (374841) ASIC_task: New pool difficulty 16
₿ (403951) stratum_task: rx: {"id":null,"method":"mining.notify","params":["d3c4c5","5dd991299afabe1cc5097059607430ed5f242e6c00016d4b0000000000000000","02000000010000000000000000000000000000000000000000000000000000000000000000ffffffff1703a4890d5075626c69632d506f6f6c","ffffffff023d3cd1120000000017a914b46e629336cac9252929b9808cb1ea7d4af14f59870000000000000000266a24aa21a9ed54c25fe0480159cb6594ae8cdf0db8c5f56e433c2488a2899b7fa069ee1910fd00000000",["1fd29ed19514cd341321c814064fd244c2e70ed418b6ddb5a23fbc0982081ee6","8df0d6e9ff48ef975b883f2982616af4763f3ec0262675cdc68a0a92024e0f40","b80435c480acc519edc6084a24b58d3c661d6fad86a34028c8df4b4016c0c534","359512eb308b18df351462332b5b709824f81bd216719abf755b65af8968c805","823d0138cd2a00d63b25b712085c90e2aead8a193f1b890443e86636502dba11","37066ae75bd7cf23f2a1ab9968e20800820428252b6cb8c48f31c531ea36900d","088bb377db411fa46001ef6d8e2596d98535c730274f8717b75380ba5401558b","7b902c472ab0723efeb7b6786caa9e0c1b931c4a6c959e170a37e88f54c07b1c","ced22895425492f6a88783fcbe916ea0cebc85e6a48d87d569ec37d81de029b3","5a508151091616b4c816c3ff9b7487a5506e3b6a5cbe4ed329f837cd3d9369e7","b125ef58978b2d31f5407519a63866603121735e89e17b81e7809c73a808f52b","cd4c2f15b6e9fbaada22b0c0efd87ccca02a703745444c0266e5298b4bf67e19"],"20000000","17028281","67cf2dd6",false]}
₿ (404161) create_jobs_task: New Work Dequeued d3c4c5
₿ (415671) http_server: File sending complete
₿ (434651) stratum_task: rx: {"id":null,"method":"mining.set_difficulty","params":[2]}
₿ (434661) stratum_task: Set stratum difficulty: 2
₿ (434661) stratum_task: rx: {"id":null,"method":"mining.notify","params":["d3c517","5dd991299afabe1cc5097059607430ed5f242e6c00016d4b0000000000000000","02000000010000000000000000000000000000000000000000000000000000000000000000ffffffff1703a4890d5075626c69632d506f6f6c","ffffffff023d3cd1120000000017a914b46e629336cac9252929b9808cb1ea7d4af14f59870000000000000000266a24aa21a9ed54c25fe0480159cb6594ae8cdf0db8c5f56e433c2488a2899b7fa069ee1910fd00000000",["1fd29ed19514cd341321c814064fd244c2e70ed418b6ddb5a23fbc0982081ee6","8df0d6e9ff48ef975b883f2982616af4763f3ec0262675cdc68a0a92024e0f40","b80435c480acc519edc6084a24b58d3c661d6fad86a34028c8df4b4016c0c534","359512eb308b18df351462332b5b709824f81bd216719abf755b65af8968c805","823d0138cd2a00d63b25b712085c90e2aead8a193f1b890443e86636502dba11","37066ae75bd7cf23f2a1ab9968e20800820428252b6cb8c48f31c531ea36900d","088bb377db411fa46001ef6d8e2596d98535c730274f8717b75380ba5401558b","7b902c472ab0723efeb7b6786caa9e0c1b931c4a6c959e170a37e88f54c07b1c","ced22895425492f6a88783fcbe916ea0cebc85e6a48d87d569ec37d81de029b3","5a508151091616b4c816c3ff9b7487a5506e3b6a5cbe4ed329f837cd3d9369e7","b125ef58978b2d31f5407519a63866603121735e89e17b81e7809c73a808f52b","cd4c2f15b6e9fbaada22b0c0efd87ccca02a703745444c0266e5298b4bf67e19"],"20000000","17028281","67cf2dd6",true]}
₿ (434771) stratum_task: Clean Jobs: clearing queue
₿ (434861) create_jobs_task: New Work Dequeued d3c517
₿ (434861) ASIC_task: New pool difficulty 2
₿ (464241) stratum_task: rx: {"id":null,"method":"mining.notify","params":["d3d0d4","5dd991299afabe1cc5097059607430ed5f242e6c00016d4b0000000000000000","02000000010000000000000000000000000000000000000000000000000000000000000000ffffffff1703a4890d5075626c69632d506f6f6c","ffffffff027affd4120000000017a914b46e629336cac9252929b9808cb1ea7d4af14f59870000000000000000266a24aa21a9ed3d4cf1b40b5bf6218a44dcda275ee67277938117afa72309ac2e7aa8d746cca100000000",["1fd29ed19514cd341321c814064fd244c2e70ed418b6ddb5a23fbc0982081ee6","8df0d6e9ff48ef975b883f2982616af4763f3ec0262675cdc68a0a92024e0f40","c018a9c20548508b9e70ff28023179e4e804486d7c51a70a4e757df3761b83ac","8bf6a39a0464ee7dde3ee1b47be4e0f3f1dc8402692b321eaf916e98b116e9ee","cdbb14e1d1a67b666709c66a804539f007cd38ccd68d7001a04c066da8b050a6","8325546c04ae655d248945fe550c09ee5073c71187b10b618e9d47e13a29feb8","f4c10af39dfb8ef35ef81169e11dd08497bd0bbe0019cf6c8c8eee5e2de366ee","12d5b0144d2d2f311f4ecdcdf76291ee3b9b3e546a287a3b3804c039b13af343","11ef82dad61734c3a7a49fbb7776ed0c34972aef389942536b1ad2814e444631","d027d1a805f68d0d25a78b798d98f5ff6aeb099926f31f137c16582077dfddcf","9033c674ce177ea9295146bad05defaad66bb01f9437f5c15cbf52f18b46e4d4","66aca04039e97ffd378d2f0dd9f40d6565a255bac944cc1cb63f3b73998065a6"],"20000000","17028281","67cf2e12",false]}
₿ (464381) create_jobs_task: New Work Dequeued d3d0d4`

I hope a solution will be found soon. Because I have only had this miner since 28.2.25

Many thanks
Kind regards from Switzerland


### MaSe-Time on 2025-03-10

> Evening everyone
> 
> I have had the same problem since last week. It worked great until it dropped to 0. I tried restarting via the website and also disconnecting the miner from the power for a few minutes without success. Changing the pool didn't change anything and neither did placing the miner next to an access point.
> 
> Then I tried to reload the firmware but also without success. Downgrading to e.g. 2.5.0 has also had no effect, nor has giving it more power or less.
> 
> I get the same messages in the log and sometimes the following: ...
> 
> I hope a solution will be found soon. Because I have only had this miner since 28.2.25
> 
> Many thanks Kind regards from Switzerland

What pool are you on? eusolo.ckoool.org was the lowest ping for me in the UK 

### MavenCH on 2025-03-10

> > Evening everyone
> > I have had the same problem since last week. It worked great until it dropped to 0. I tried restarting via the website and also disconnecting the miner from the power for a few minutes without success. Changing the pool didn't change anything and neither did placing the miner next to an access point.
> > Then I tried to reload the firmware but also without success. Downgrading to e.g. 2.5.0 has also had no effect, nor has giving it more power or less.
> > I get the same messages in the log and sometimes the following: ...
> > I hope a solution will be found soon. Because I have only had this miner since 28.2.25
> > Many thanks Kind regards from Switzerland
> 
> What pool are you on? eusolo.ckoool.org was the lowest ping for me in the UK

Hello MaSe-Time

I have always been on public-pool.io:21496 and it has worked. 
But I have also tried to use eusolo.ckpool.org:3333, but without success.

The settings are set to default. In other words: 525 1150

I have also just tried to update to v2.6.0b8 but no change here either.

I have just tried to ping both but without success.
Is there a special address that can be pinged?

Greetings


`--- web.public-pool.io ping statistics ---
27 packets transmitted, 27 received, 0% packet loss, time 67ms
rtt min/avg/max/mdev = 14.178/16.162/18.555/1.178 ms
`

### skot on 2025-03-10

> Evening everyone
> 
> I have had the same problem since last week. It worked great until it dropped to 0. I tried restarting via the website and also disconnecting the miner from the power for a few minutes without success. Changing the pool didn't change anything and neither did placing the miner next to an access point.
> 
> Then I tried to reload the firmware but also without success. Downgrading to e.g. 2.5.0 has also had no effect, nor has giving it more power or less.
>
> I hope a solution will be found soon. Because I have only had this miner since 28.2.25

Where did you get this Bitaxe? What Power Supply do you have?

I'd like to collect some info on what power supplies people who see this error have.

Also that is interesting that unplugging power does not fix it. Can you upload a screenshot of your AxeOS dashboard and settings?

### MavenCH on 2025-03-10

> > Evening everyone
> > I have had the same problem since last week. It worked great until it dropped to 0. I tried restarting via the website and also disconnecting the miner from the power for a few minutes without success. Changing the pool didn't change anything and neither did placing the miner next to an access point.
> > Then I tried to reload the firmware but also without success. Downgrading to e.g. 2.5.0 has also had no effect, nor has giving it more power or less.
> > I hope a solution will be found soon. Because I have only had this miner since 28.2.25
> 
> Where did you get this Bitaxe? What Power Supply do you have?
> 
> I'd like to collect some info on what power supplies people who see this error have.


Hello skot

Thank you for your request.
I got it from here: https://miningwholesale.eu/product/bitaxe-gamma/

Also here a picture of the miner with the power supply and the dashboard:
https://photos.app.goo.gl/rsoQ2PonckK8iAxr9

I have just seen from the picture that I have had the miner since 3.3.25 and put it into operation the day after.

I hope this helps.
For further questions I am very happy to answer :)

Greetings

### Erkman84 on 2025-03-16

Same issue: restarting (cold/warm) device and plug power off-on again does not solve the issue. It is a software releated issue... please fix it.

Update: downgrade to v2.0.3 seems to help. (Better as non-working miner)

### skot on 2025-03-16

> Same issue: restarting (cold/warm) device and plug power off-on again does not solve the issue. It is a software releated issue... please fix it.
> 
> Update: downgrade to v2.0.3 seems to help. (Better as non-working miner)

We are going to have better indication that a Power fault has occurred in v2.6.0; to be released at the end of this month. You can load the latest pre-release beta now if you want to test it.

### MavenCH on 2025-03-16

> > Same issue: restarting (cold/warm) device and plug power off-on again does not solve the issue. It is a software releated issue... please fix it.
> > Update: downgrade to v2.0.3 seems to help. (Better as non-working miner)
> 
> We are going to have better indication that a Power fault has occurred in v2.6.0; to be released at the end of this month. You can load the latest pre-release beta now if you want to test it.

I have already tried this, but unfortunately it has not changed anything.
I'll try to supply the miner via USB C tomorrow to rule out the power supply unit.

Since I have tried to downgrade to 2.0.3, I can no longer reach the miner. I hope I haven't made anything worse now...

### MaSe-Time on 2025-03-16

> > > Same issue: restarting (cold/warm) device and plug power off-on again does not solve the issue. It is a software releated issue... please fix it.
> > > Update: downgrade to v2.0.3 seems to help. (Better as non-working miner)
> > 
> > 
> > We are going to have better indication that a Power fault has occurred in v2.6.0; to be released at the end of this month. You can load the latest pre-release beta now if you want to test it.
> 
> I have already tried this, but unfortunately it has not changed anything. I'll try to supply the miner via USB C tomorrow to rule out the power supply unit.
> 
> Since I have tried to downgrade to 2.0.3, I can no longer reach the miner. I hope I haven't made anything worse now...

I have three that were all doing variations of this. Moved closer to my router and not had one drop out since 🤷

### bonifacio123 on 2025-03-18

Running 2.6.0b10 - having no issues until I moved the gamma which was about 15 feet away from the wifi router to about 1 foot away and it manifested the non-mining issue. I just kept rebooting it until it just started working again. Using a 50w power supply. I didn't grab the logs but it was getting work from the pool but not mining.

### cniweb on 2025-03-19

I have the same problem with a Bitaxe 600, no Firmware Version´s work for me.

### skot on 2025-03-24

This should be "fixed" in #780 ... meaning that power faults are now shown in AxeOS, and assuming the fault cause is gone, a warm restart should clear.

This will be included in the v2.6.0 firmware release.

### ParkaMark on 2025-04-02

Just an update from me on this. Have updated to 2.6.1. It's great that it now reports a power fault. I've since swapped the power supplies on my miners around. On one of my bulk orders from BitcoinMerch, they shipped units with some PSUs which are bricks with attachable power cables. All the other ones they've sent me on other orders where bricks where there is no attachable power cable, so the power socket pins are built straight into the unit that you plug in.

Anyway, after swapping them around, and putting the attachable power cable variants on my lowest power draw miners, and using the no attachable power cable variants on the 1370s, things are now looking way more stable.

Thank you for everyone involved and for fixing and addressing this bug. It seems that not all PSUs are equal.

EDIT: They are more stable and I am now able to restart the miners via the API, but they are still failing after a while with a power supply fault. It looks like the PSUs BitcoinMerch have issued for the BM1370 Gamma are problematic. I'm going to email them and see what they say.

### avatardiablo on 2025-04-04

I own 4 bitaxes. 2 ultra 1 supra 1 gamma.
I have the same problem with the gamma. only with it. I have really tried everything. (firmware, reset, etc etc) At first it goes as if nothing had happened it can last even three hours without a hitch but then it always blocks.
It blocks, but does not lose wattage or volts. the hashrate remains constant I noticed when it blocks because in reality it is not mining.
When I read that it happened to someone after changing the fan.... I had a doubt. because all 4 bitaxes were equipped with the noctua 5v pwn. On the Gamma I therefore put the previous original fan back..... and magic it's 24 hours without stopping.
suggestions?

### skot on 2025-04-04

> I own 4 bitaxes. 2 ultra 1 supra 1 gamma.
> I have the same problem with the gamma. only with it. I have really tried everything. (firmware, reset, etc etc) At first it goes as if nothing had happened it can last even three hours without a hitch but then it always blocks.
> It blocks, but does not lose wattage or volts. the hashrate remains constant I noticed when it blocks because in reality it is not mining.
> When I read that it happened to someone after changing the fan.... I had a doubt. because all 4 bitaxes were equipped with the noctua 5v pwn. On the Gamma I therefore put the previous original fan back..... and magic it's 24 hours without stopping.
> suggestions?

Are you running v2.6.2 firmware? Are you getting the voltage regulator fault?

### avatardiablo on 2025-04-04

> > Io possiedo 4 bitax. 2 ultra 1 supra 1 gamma. 
> > Ho lo stesso problema con la gamma. solo con quella. Ho provato davvero di tutto. (firmware, reset, ecc ecc) All'inizio va come se niente fosse può durare anche tre ore senza intoppi ma poi si blocca sempre. 
> > Si blocca, ma non perde wattaggio o volt. l'hashrate rimane costante me ne sono accorto quando si blocca perché in realtà non è mining. 
> > Quando ho letto che è successo a qualcuno dopo aver cambiato la ventola.... mi è venuto un dubbio. perché tutte e 4 le bitax erano equipaggiate con la noctua 5v pwn. Sulla Gamma ho quindi rimesso la ventola originale precedente..... e magia sono 24 ore senza fermarsi. 
> > suggerimenti?
> 
> Stai utilizzando il firmware v2.6.2? Stai riscontrando un errore nel regolatore di tensione?

yes the firmware tested with the noctua 5v pwn fan is 2.6.1 the voltage regulator values ​​are normal I think but I didn't do any measurements. the power supply is a dedicated 5v 40 Ampere that runs all 4 bitaxes and 5.3v under load. After trying everything I put back its original fan which is always a 5v pwn but I don't know what brand it is, and it started working again without blocks.

### procent85 on 2025-04-11

Hi. I have a Bitaxe Gamma 601 since yesterday and I have the same problem. No matter if I am running v2.5.1, v2.6.1 or v2.6.3, I constantly get this error after 10-50 minutes of starting or restarting:

```
₿ (701623) stratum_task: Clean Jobs: clearing queue
₿ (701703) create_jobs_task: New Work Dequeued 3939325
```

Changing the pool (solo.ckpool and public-pool.io), flashing, updating, overclocking or reducing the clock value does not help. Nothing. The device is currently worthless because it usually stops hashing after 10 min. I am attaching a screenshot. This error appears nonstop in the logs - there are no other messages.

![Image](https://github.com/user-attachments/assets/928ad7fb-8752-4c7b-90cf-1776144305b0)


### skot on 2025-04-11

> Hi. I have a Bitaxe Gamma 601 since yesterday and I have the same problem. No matter if I am running v2.5.1, v2.6.1 or v2.6.3, I constantly get this error after 10-50 minutes of starting or restarting:
> 
> ```
> ₿ (701623) stratum_task: Clean Jobs: clearing queue
> ₿ (701703) create_jobs_task: New Work Dequeued 3939325
> ```
> 
> Changing the pool (solo.ckpool and public-pool.io), flashing, updating, overclocking or reducing the clock value does not help. Nothing. The device is currently worthless because it usually stops hashing after 10 min. I am attaching a screenshot. This error appears nonstop in the logs - there are no other messages.
> 
> ![Image](https://github.com/user-attachments/assets/928ad7fb-8752-4c7b-90cf-1776144305b0)
> 

This is a different issue. Please talk to the seller where you purchased your Bitaxe for support.
