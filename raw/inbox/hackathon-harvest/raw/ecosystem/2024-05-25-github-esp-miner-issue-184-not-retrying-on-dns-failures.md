# bitaxeorg/ESP-Miner issue #184: not retrying on DNS failures

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/184
> Collected: 2026-10-07
> Published: 2024-05-25

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 184
- State: closed
- Author: jddebug
- Opened: 2024-05-25
- Closed: 2024-12-01
- Labels: bug

## Description


**Describe the bug**
Router rebooted today. Miners lost connection but seem to have all (5 of them) connected back to wifi after it came back online. However, all 5 did not start mining. 

I can connect to them on the local LAN. This is what I am seeing in the logs:

₿ (899188) stratum_task: Socket unable to connect to public-pool.io:21496 (errno 113)
₿ (904188) stratum_task: Socket created, connecting to 0.0.0.0:21496

One seems to have rebooted on its own after about 18 minutes and it is now mining. The others have not rebooted and are still showing that same information in the logs. Rebooting them gets them mining again.




## Comments

### mac54 on 2024-05-31

I have the same problem with 2.1.6. Wifi reconnect works and webinterface is reachable again. But mining does not start. Only a manually triggered reboot solves the problem.

### alejandroperezlopez on 2024-05-31

I've tested it some minutes ago and it's working on my two Bitaxe 204 (Ultra). When the wifi network was down, both devices were showing both connecting to my ssid and the AP ssid available messages.

When the network was available again, both connected and started showing the mining information.

### mac54 on 2024-06-01

For me it's not working:
₿ (368759) stratum_task: Socket unable to connect to solo.ckpool.org:3333 (errno 113)
₿ (373759) stratum_task: Socket created, connecting to 0.0.0.0:3333
₿ (392259) stratum_task: Socket unable to connect to solo.ckpool.org:3333 (errno 113)
₿ (397259) stratum_task: Socket created, connecting to 0.0.0.0:3333
₿ (415759) stratum_task: Socket unable to connect to solo.ckpool.org:3333 (errno 113)
₿ (420759) stratum_task: Socket created, connecting to 0.0.0.0:3333
₿ (439259) stratum_task: Socket unable to connect to solo.ckpool.org:3333 (errno 113)
₿ (444259) stratum_task: Socket created, connecting to 0.0.0.0:3333
₿ (462759) stratum_task: Socket unable to connect to solo.ckpool.org:3333 (errno 113)
₿ (467759) stratum_task: Socket created, connecting to 0.0.0.0:3333
₿ (486259) stratum_task: Socket unable to connect to solo.ckpool.org:3333 (errno 113)
₿ (491259) stratum_task: Socket created, connecting to 0.0.0.0:3333

### skot on 2024-06-01

0.0.0.0 sounds like a DNS problem somewhere.

### solobito on 2024-06-01

I've seen this too. It's possible that once the connection is lost, it can't resolve the URL to an IP address.

solo.ckpool.org is 2604:2dc0:100:240f::1

Maybe we could try mining directly with the pool's IP address to see if there are any errors.

*Edited
`stratum+tcp://solo.ckpool.org:3333 (51.81.56.15)`

### pixeldoc2000 on 2024-06-05

Same Problem with 2.1.6 and 2.17 and possible older versions. 

```
₿ (18824034) stratum_task: Socket unable to connect to pool.example.org:3333 (errno 113)
₿ (18829034) stratum_task: Socket created, connecting to 0.0.0.0:3333
```

Looking at the source, it seems like stratum_task() does not check if the dns lookup was successful (resolved ip = 0.0.0.0) and does not try to resolve the dns again.

Then stratum_task() does try to connect to the unresolved ip endlessly -> can't connect to pool.

### skot on 2024-06-05

when a pool URL resolves to 0.0.0.0 that likely means there was a DNS failure. We should be recognizing this error and retrying until it works.

### skot on 2024-06-05

Ah, I see what's going on here. The DNS lookup is not in the retry loop. So if for whatever reason DNS fails it sets the IP to 0.0.0.0. The Bitaxe will just keep retrying this bad IP.

```
I (9701) stratum_task: Get IP for URL: publisdfsdfsfc-pool.io

I (9721) stratum_task: Connecting to: stratum+tcp://publisdfsdfsfc-pool.io:21496 (0.0.0.0)

I (9721) stratum_task: Socket created, connecting to 0.0.0.0:21496
I (9731) ASIC_task: ASIC Ready!
I (9731) main_task: Returned from app_main()
E (27971) stratum_task: Socket unable to connect to publisdfsdfsfc-pool.io:21496 (errno 113)
I (32971) stratum_task: Socket created, connecting to 0.0.0.0:21496
E (51471) stratum_task: Socket unable to connect to publisdfsdfsfc-pool.io:21496 (errno 113)
I (56471) stratum_task: Socket created, connecting to 0.0.0.0:21496
E (74971) stratum_task: Socket unable to connect to publisdfsdfsfc-pool.io:21496 (errno 113)
I (79971) stratum_task: Socket created, connecting to 0.0.0.0:21496
E (98471) stratum_task: Socket unable to connect to publisdfsdfsfc-pool.io:21496 (errno 113)
I (103471) stratum_task: Socket created, connecting to 0.0.0.0:21496
E (121971) stratum_task: Socket unable to connect to publisdfsdfsfc-pool.io:21496 (errno 113)
I (126971) stratum_task: Socket created, connecting to 0.0.0.0:21496
```

### skot on 2024-06-05

I made a 2.1.8b1 build with this fix; can y'all give it a try? 
You can unzip this image and then update via AxeOS. No need to worry about `www.bin` if you're already on 2.1.7
[esp-miner.bin.zip](https://github.com/user-attachments/files/15596411/esp-miner.bin.zip)


### pixeldoc2000 on 2024-06-08

With 2.1.8 i had at least one instance where dns lookup only partialy resolved the pool ip and firmware stopped after that:

# Serial Log
```
I (50241) bm1366Module: RX Job ID: 28
I (50241) asic_result: Nonce difficulty 821.47 of 1000.
I (50471) bm1366Module: RX Job ID: 28
I (50481) asic_result: Nonce difficulty 399.29 of 1000.
I (55331) bm1366Module: RX Job ID: 40
I (55331) asic_result: Nonce difficulty 368.11 of 1000.
I (55811) bm1366Module: RX Job ID: 40
I (55811) asic_result: Nonce difficulty 324.15 of 1000.
E (58941) stratum_api: recv
I (58941) stratum_api: Restarting System because of Error: recv
I (59951) wifi:state: run -> init (0x0)
I (59951) wifi:pm stop, total sleep time: 44789814 us / 58347512 us

I (59951) wifi:<ba-del>idx:0, tid:0
I (59951) wifi:<ba-del>idx:1, tid:4
I (59951) wifi:new:<6,0>, old:<6,0>, ap:<255,255>, sta:<6,0>, prof:1, snd_ch_cfg:0x0
I (60001) wifi:flush txq
I (60001) wifi:stop sw txq
I (60001) wifi:lmac stop hw txq
ESP-ROM:esp32s3-20210327
Build:Mar 27 2021
rst:0xc (RTC_SW_CPU_RST),boot:0x8 (SPI_FAST_FLASH_BOOT)
Saved PC:0x40375b88
SPIWP:0xee
mode:DIO, clock div:1
load:0x3fce3818,len:0x16e0
load:0x403c9700,len:0x4
load:0x403c9704,len:0xc00
load:0x403cc700,len:0x2eb0
entry 0x403c9908
I (31) boot: ESP-IDF v5.1 2nd stage bootloader
I (31) boot: compile time Mar 18 2024 01:01:26
I (31) boot: Multicore bootloader
I (34) boot: chip revision: v0.2
I (38) boot.esp32s3: Boot SPI Speed : 80MHz
I (43) boot.esp32s3: SPI Mode       : DIO
I (48) boot.esp32s3: SPI Flash Size : 16MB
I (52) boot: Enabling RNG early entropy source...
I (58) boot: Partition Table:
I (61) boot: ## Label            Usage          Type ST Offset   Length
I (69) boot:  0 nvs              WiFi data        01 02 00009000 00006000
I (76) boot:  1 phy_init         RF data          01 01 0000f000 00001000
I (84) boot:  2 factory          factory app      00 00 00010000 00400000
I (91) boot:  3 www              Unknown data     01 82 00410000 00300000
I (99) boot:  4 ota_0            OTA app          00 10 00710000 00400000
I (106) boot:  5 ota_1            OTA app          00 11 00b10000 00400000
I (114) boot:  6 otadata          OTA data         01 00 00f10000 00002000
I (121) boot:  7 coredump         Unknown data     01 03 00f12000 00010000
I (129) boot: End of partition table
I (133) esp_image: segment 0: paddr=00710020 vaddr=3c0b0020 size=2d16ch (184684) map
I (175) esp_image: segment 1: paddr=0073d194 vaddr=3fc9a500 size=02e84h ( 11908) load
I (177) esp_image: segment 2: paddr=00740020 vaddr=42000020 size=aceach (708268) map
I (307) esp_image: segment 3: paddr=007eced4 vaddr=3fc9d384 size=02194h (  8596) load
I (310) esp_image: segment 4: paddr=007ef070 vaddr=40374000 size=1649ch ( 91292) load
I (343) boot: Loaded app from partition at offset 0x710000
I (343) boot: Disabling RNG early entropy source...
I (354) cpu_start: Multicore app
I (364) cpu_start: Pro cpu start user code
I (364) cpu_start: cpu freq: 160000000 Hz
I (364) app_init: Application information:
I (367) app_init: Project name:     esp-miner
I (372) app_init: App version:      v2.1.8
I (377) app_init: Compile time:     Jun  8 2024 10:17:32
I (383) app_init: ELF file SHA256:  92453246f...
I (388) app_init: ESP-IDF:          v5.3-beta1
I (393) efuse_init: Min chip rev:     v0.0
I (398) efuse_init: Max chip rev:     v0.99 
I (403) efuse_init: Chip rev:         v0.2
I (408) heap_init: Initializing. RAM available for dynamic allocation:
I (415) heap_init: At 3FCA4F30 len 000447E0 (273 KiB): RAM
I (421) heap_init: At 3FCE9710 len 00005724 (21 KiB): RAM
I (427) heap_init: At 3FCF0000 len 00008000 (32 KiB): DRAM
I (433) heap_init: At 600FE100 len 00001EE8 (7 KiB): RTCRAM
I (441) spi_flash: detected chip: gd
I (444) spi_flash: flash io: dio
W (448) i2c: This driver is an old driver, please migrate your application code to adapt `driver/i2c_master.h`
W (459) ADC: legacy driver is deprecated, please migrate to `esp_adc/adc_oneshot.h`
I (467) sleep: Configure to isolate all GPIO pins in sleep state
I (474) sleep: Enable automatic switching of GPIO sleep configuration
I (481) main_task: Started on CPU0
I (491) main_task: Calling app_main()
I (521) miner: NVS_CONFIG_ASIC_FREQ 525.000000
E (521) miner: Invalid DEVICE model
I (521) miner: ASIC: BM1366
I (521) SystemModule: I2C initialized successfully
I (531) vcore.c: Set ASIC voltage = 1.250V [0xB9]
I (531) gpio: GPIO[12]| InputEn: 1| OutputEn: 0| OpenDrain: 0| Pullup: 0| Pulldown: 0| Intr:0 
I (541) miner: Welcome to the bitaxe!
I (551) pp: pp rom version: e7ae62f
I (551) net80211: net80211 rom version: e7ae62f
I (561) wifi:wifi driver task: 3fcb27e0, prio:23, stack:6656, core=0
I (571) wifi:wifi firmware version: 50adca9
I (571) wifi:wifi certification version: v7.0
I (571) wifi:config NVS flash: enabled
I (571) wifi:config nano formating: disabled
I (581) wifi:Init data frame dynamic rx buffer num: 32
I (581) wifi:Init static rx mgmt buffer num: 5
I (591) wifi:Init management short buffer num: 32
I (591) wifi:Init dynamic tx buffer num: 32
I (591) wifi:Init static tx FG buffer num: 2
I (601) wifi:Init static rx buffer size: 1600
I (601) wifi:Init static rx buffer num: 10
I (611) wifi:Init dynamic rx buffer num: 32
I (611) wifi_init: rx ba win: 6
I (611) wifi_init: accept mbox: 6
I (621) wifi_init: tcpip mbox: 32
I (621) wifi_init: udp mbox: 6
I (631) wifi_init: tcp mbox: 6
I (631) wifi_init: tcp tx win: 5760
I (631) wifi_init: tcp rx win: 5760
I (641) wifi_init: tcp mss: 1440
I (641) wifi_init: WiFi IRAM OP enabled
I (651) wifi_init: WiFi RX IRAM OP enabled
I (661) wifi station: ESP_WIFI Access Point On
W (661) wifi:Affected by the ESP-NOW encrypt num, set the max connection num to 10
I (661) wifi station: ESP_WIFI_MODE_STA
I (671) wifi station: wifi_init_sta finished.
I (671) phy_init: phy_version 670,b7bc9b9,Apr 30 2024,10:54:13
I (711) wifi:mode : sta (xx:xx:xx:xx:xx:d0) + softAP (xx:xx:xx:xx:xx:d1)
I (711) wifi:enable tsf
I (711) wifi:Total power save buffer number: 16
I (711) wifi:Init max length of beacon: 752/752
I (721) wifi:Init max length of beacon: 752/752
I (731) esp_netif_lwip: DHCP server started on interface WIFI_AP_DEF with IP: 192.168.4.1
I (731) wifi:ap channel adjust o:1,1 n:6,2
I (741) wifi:new:<6,0>, old:<1,1>, ap:<6,2>, sta:<6,0>, prof:1, snd_ch_cfg:0x0
I (741) wifi:state: init -> auth (0xb0)
I (751) wifi station: ESP_WIFI setting hostname to: pd-lm01
I (761) wifi station: wifi_init_sta finished.
I (1441) wifi:state: auth -> assoc (0x0)
I (1441) SystemModule: OLED init success!
I (1451) wifi:state: assoc -> run (0x10)
I (1471) wifi:connected with xxxxxxxxx, aid = 24, channel 6, BW20, bssid = xx:xx:xx:3e:18:5e
I (1471) wifi:security: WPA3-SAE, phy: bgn, rssi: -70
I (1471) wifi:pm start, type: 1

I (1471) wifi:dp: 1, bi: 102400, li: 3, scale listen interval from 307200 us to 307200 us
I (1481) wifi:set rx beacon pti, rx_bcn_pti: 0, bcn_timeout: 25000, mt_pti: 0, mt_time: 10000
I (1501) wifi:AP's beacon interval = 102400 us, DTIM period = 1
I (1621) http_server: Partition size: total: 2884241, used: 666154
I (1621) http_server: Starting HTTP Server
I (1621) example_dns_redirect_server: Socket created
I (1621) example_dns_redirect_server: Socket bound, port 53
I (1631) example_dns_redirect_server: Waiting for data
I (1651) SystemModule: SYSTEM_task started
I (2011) wifi:<ba-add>idx:0 (ifx:0, xx:xx:xx:3e:18:5e), tid:0, ssn:1, winSize:64
I (2321) wifi:<ba-del>idx:0, tid:0
I (2331) wifi:<ba-add>idx:0 (ifx:0, xx:xx:xx:3e:18:5e), tid:0, ssn:3, winSize:64
I (3001) wifi station: Bitaxe ip:192.168.0.239
I (3001) esp_netif_handlers: sta ip: 192.168.0.239, mask: 255.255.255.0, gw: 192.168.0.1
I (3001) miner: Connected to SSID: xxxxxxxxxxxx
I (3001) wifi station: ESP_WIFI Access Point Off
I (3011) wifi:mode : sta (xx:xx:xx:xx:xx:d0)
I (3021) serial: Initializing serial
I (3021) bm1366Module: Initializing BM1366
I (4221) bm1366Module: 1 chip(s) detected on the chain
final refdiv: 2, fbdiv: 210, postdiv1: 5, postdiv2: 1, min diff value: 0.000000
I (4251) bm1366Module: Setting Frequency to 525.00MHz (0.01)
I (4251) bm1366Module: Setting max baud of 1000000 
I (4261) serial: Changing UART baud to 1000000
I (4261) stratum_task: Get IP for URL: sha256-eu.unmineable.com
I (4271) ASIC_task: ASIC Ready!
I (4271) main_task: Returned from app_main()
I (4281) stratum_task: Connecting to: stratum+tcp://sha256-eu.unmineable.com:3333 (0.0.0.149)
I (4291) stratum_task: Socket created, connecting to 0.0.0.149:3333
I (5081) wifi:<ba-add>idx:1 (ifx:0, xx:xx:xx:3e:18:5e), tid:4, ssn:1, winSize:64
E (22401) stratum_task: Socket unable to connect to sha256-eu.unmineable.com:3333 (errno 113)
I (27401) stratum_task: Get IP for URL: sha256-eu.unmineable.com
```
Bitaxe did not continue, had to Reboot via Webinterface

Note the resolved IP: 0.0.0.149 Looks like the ip was only partialy "resolved" or converted? The correct ip is 46.101.2.149

```
I (2062371) http_server: File sending complete
I (2062981) http_server: File sending complete
W (2063291) httpd_txrx: httpd_sock_err: error in send : 104
E (2063291) http_server: File sending failed!
W (2063291) httpd_txrx: httpd_sock_err: error in send : 104
W (2063301) httpd_txrx: httpd_resp_send_err: 500 Internal Server Error - Failed to send file
W (2063311) httpd_txrx: httpd_resp_send_err: error calling setsockopt : 22
W (2063321) httpd_txrx: httpd_sock_err: error in send : 128
W (2063321) httpd_uri: httpd_uri: uri handler execution failed
I (2066121) http_server: Handshake done, the new connection was opened
I (2071951) http_server: Restarting System because of API Request
I (2072951) wifi:state: run -> init (0x0)
I (2072951) wifi:pm stop, total sleep time: 1667844366 us / 2071474653 us

I (2072951) wifi:<ba-del>idx:0, tid:0
I (2072951) wifi:<ba-del>idx:1, tid:4
I (2072961) wifi:new:<6,0>, old:<6,0>, ap:<255,255>, sta:<6,0>, prof:1, snd_ch_cfg:0x0
I (2073001) wifi:flush txq
I (2073001) wifi:stop sw txq
I (2073001) wifi:lmac stop hw txq
ESP-ROM:esp32s3-20210327
Build:Mar 27 2021
rst:0xc (RTC_SW_CPU_RST),boot:0x8 (SPI_FAST_FLASH_BOOT)
Saved PC:0x40375b88
SPIWP:0xee
mode:DIO, clock div:1
load:0x3fce3818,len:0x16e0
load:0x403c9700,len:0x4
load:0x403c9704,len:0xc00
load:0x403cc700,len:0x2eb0
entry 0x403c9908
I (31) boot: ESP-IDF v5.1 2nd stage bootloader
I (31) boot: compile time Mar 18 2024 01:01:26
I (31) boot: Multicore bootloader
```
SNIP
```
I (5011) serial: Initializing serial
I (5011) bm1366Module: Initializing BM1366
I (6211) bm1366Module: 1 chip(s) detected on the chain
final refdiv: 2, fbdiv: 210, postdiv1: 5, postdiv2: 1, min diff value: 0.000000
I (6241) bm1366Module: Setting Frequency to 525.00MHz (0.01)
I (6241) bm1366Module: Setting max baud of 1000000 
I (6251) serial: Changing UART baud to 1000000
I (6251) stratum_task: Get IP for URL: sha256-eu.unmineable.com
I (6261) ASIC_task: ASIC Ready!
I (6261) main_task: Returned from app_main()
I (6301) stratum_task: Connecting to: stratum+tcp://sha256-eu.unmineable.com:3333 (46.101.2.149)
I (6301) stratum_task: Socket created, connecting to 46.101.2.149:3333
I (6361) stratum_api: tx: {"id": 1, "method": "mining.subscribe", "params": ["bitaxe/BM1366 (v2.1.8)"]}

I (6361) stratum_api: tx: {"id": 2, "method": "mining.configure", "params": [["version-rolling"], {"version-rolling.mask": "ffffffff"}]}

I (6371) stratum_api: tx: {"id": 3, "method": "mining.suggest_difficulty", "params": [1000]}

I (6381) stratum_api: tx: {"id": 4, "method": "mining.authorize", "params": ["BTC:bc1qxxxxxxxxxxxxxxxxxxxxx", "x"]}

I (6401) wifi:<ba-add>idx:1 (ifx:0, xx:xx:xx:xx:18:5e), tid:2, ssn:1, winSize:64
I (6441) stratum_task: rx: {"id": 1, "result": [[["mining.set_difficulty", "008c1957711582d8"], ["mining.notify", "008c1957711582d8"]], "61e3448e", 8], "error": null}
I (6451) stratum_api: extranonce_str: 61e3448e
I (6451) stratum_api: extranonce_2_len: 8
I (6461) stratum_task: rx: {"id": 2, "result": {"version-rolling": true, "version-rolling.mask": "1fffe000"}, "error": null}
I (6471) stratum_api: Set version mask: 1fffe000
I (6471) stratum_task: rx: {"id": null, "method": "mining.set_version_mask", "params": ["1fffe000"], "error": null}
I (6481) stratum_task: Set version mask: 1fffe000
I (6491) stratum_task: rx: {"id": 3, "error": null, "result": true}
I (6501) stratum_task: setup message accepted
I (6501) stratum_task: rx: {"id": null, "method": "mining.set_difficulty", "params": [1000]}
I (6511) stratum_task: Set stratum difficulty: 1000
I (6521) stratum_task: rx: {"id": 4, "result": true, "error": null}
I (6521) stratum_task: setup message accepted
I (6531) stratum_task: rx: {"id": null, "method": "mining.set_difficulty", "params": [1000]}
I (6541) stratum_task: rx: {"id": null, "method": "mining.notify", "params": ["36c", "471f751e0137a6783c435c60e5d6cfe4946dde280002118e0000000000000000", "01000000010000000000000000000000000000000000000000000000000000000000000000fff}
I (6681) SystemModule: Syncing clock
I (6681) create_jobs_task: New Work Dequeued 36c
I (6691) ASIC_task: New pool difficulty 1000
I (9511) bm1366Module: RX Job ID: 10
I (9511) asic_result: Nonce difficulty 480.09 of 1000.
I (12081) bm1366Module: RX Job ID: 18
I (12091) asic_result: Nonce difficulty 338.58 of 1000.
I (13691) bm1366Module: RX Job ID: 20
I (13691) asic_result: Nonce difficulty 720.64 of 1000.
I (14831) bm1366Module: RX Job ID: 20
I (14831) asic_result: Nonce difficulty 407.24 of 1000.
I (19861) bm1366Module: RX Job ID: 38
```
SNIP
```
I (169921) bm1366Module: RX Job ID: 68
I (169921) asic_result: Nonce difficulty 22157.30 of 1000.
I (169921) stratum_api: tx: {"id": 17, "method": "mining.submit", "params": ["BTC:xxxxxxxxxxxxxxxxxx", "373", "0b00000000000000", "6664d038", "442b00d0", "0c15a000"]}

I (169991) stratum_task: rx: {"id":17,"error":null,"result":true}
I (169991) stratum_task: message result accepted
I (172571) bm1366Module: RX Job ID: 70
I (172581) asic_result: Nonce difficulty 835.70 of 1000.
E (175991) stratum_api: recv
I (175991) stratum_api: Restarting System because of Error: recv
I (176991) wifi:state: run -> init (0x0)
I (176991) wifi:pm stop, total sleep time: 134193861 us / 174514975 us

I (176991) wifi:<ba-del>idx:0, tid:0
I (176991) wifi:<ba-del>idx:1, tid:2
I (176991) wifi:new:<6,0>, old:<6,0>, ap:<255,255>, sta:<6,0>, prof:1, snd_ch_cfg:0x0
I (177041) wifi:flush txq
I (177041) wifi:stop sw txq
I (177041) wifi:lmac stop hw txq
ESP-ROM:esp32s3-20210327
Build:Mar 27 2021
rst:0xc (RTC_SW_CPU_RST),boot:0x8 (SPI_FAST_FLASH_BOOT)
Saved PC:0x40375b88
SPIWP:0xee
mode:DIO, clock div:1
load:0x3fce3818,len:0x16e0
load:0x403c9700,len:0x4
load:0x403c9704,len:0xc00
load:0x403cc700,len:0x2eb0
entry 0x403c9908
I (31) boot: ESP-IDF v5.1 2nd stage bootloader
I (31) boot: compile time Mar 18 2024 01:01:26
I (31) boot: Multicore bootloader
```

### skot on 2024-06-09

How long did you wait before rebooting?

### pixeldoc2000 on 2024-06-09

@skot the first time it sit stuck like 4h+. Got the issue again tonight, Uptime was 7h (i belive it was stuck like 6h) and again for about an hour.

### skot on 2024-06-17

this is still happening in 2.1.8. need to merge in @bitMaker-hub fix from #185 

### WantClue on 2024-12-01

Fixed in #320
