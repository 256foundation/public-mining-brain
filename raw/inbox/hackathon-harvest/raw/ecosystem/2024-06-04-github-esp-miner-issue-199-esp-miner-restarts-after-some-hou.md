# bitaxeorg/ESP-Miner issue #199: esp-miner restarts after some hours when AxeOS is left connected

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/199
> Collected: 2026-10-07
> Published: 2024-06-04

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 199
- State: closed
- Author: skot
- Opened: 2024-06-04
- Closed: 2024-10-10
- Labels: bug

## Description

#182 fixed a number of restart errors, but this one still remains. In some cases the restart happens as soon as a websocket connection is made.

## Comments

### benjamin-wilson on 2024-06-04

I've tried for 30min to get an error out of the websocket or http server but was unable. If someone has logs that'd be helpful.

### Shen on 2024-06-05

I got one.
I 'stressed' it a bit. I logged with Putty on COM, I requested info by api and I monitored with the website realtime-logs. Last one killed it.

```
I (1652169) stratum_task: rx: {"result":true,"error":null,"id":441}
I (1652169) stratum_task: message result accepted
I (1652849) bm1368Module: Job ID: 9E
I (1652849) bm1368Module: RX Job ID: 48
I (1652849) asic_result: Nonce difficulty 463.20 of 479.
I (1653319) stratum_task: rx: {"params":["648516380010a383","26c604aac06ee1966425490d8f12d4df01b295e4000142e90000000000000000","01000000010000000000000000000000000000000000000000000000000000000000000000ffffffff350305eb0c0004540e60660442e8f3130c","0a636b706f6f6c112f736f6c6f2e636b706f6f6c2e6f72672fffffffff035262a813000000002200201bc038ee5f8759ad75eb703c00d860de2ac75fdb6c2852424845ee1998927da4a3b366000000000016001451ed61d2f6aa260cc72cdf743e4e436a82c010270000000000000000266a24aa21a9ed60c4d513c43a6c611793399ecde11fc5cc5b0b28c049239d7d6b50e203fbb1bf00000000",["6e2cb12ab468ff1e13ccfd55c290d8a0d5fe7f56a48f0d744a763600de3d3cd6","16af7a609116b0526eb4cba78dc433dbddb0ec479beb8f0b171f53ab9ac429f4","82748581976bdf6e97a6e057b124ec4cf1521888e36aad3dc29ab303e28a5bc1","022521e2e2a54400e6a71ef17560bc2d4a2f6822a6bf17bd39c5a927ac19ec32","5ce64ad7cb44b856f18656ac2e8c21861b9d77fc3274caf6f7aa21e4f275b3b2","f35addc74fb38c79669f154fc3ffaaa4d7ba444564d500d7e9b7a07c583687e4","72705aff85ad8ae889e1181e9878c0ebe4aba8285a9c2c5b3a2f25b124c3a1e1","6fe0f7a36bd6cc5430a3e4a503c06e9d19c22909957ae4b0865231329e998802","52c08aaea04d7cac4d14feda2fa7d1b2065524176372624221f176684d474d03","d6bcd93c59654ff2211b28a55d6094e8ab01bc026bc651cc9ceba5d679026aee","9a5ea3d403a4fb19083df7006a0fd62d36f9a5708afb7ab0137fc239fd248c59","9b27f4e3ec17fea297207ddea63ab5b0b9d3f2155324155c96044042b84cdd2d","35c9d7a14fdefcd2e63b4bc72bfcab85bcaa9d6e4414921579867164aaaa7d25"],"20000000","170355f0","66600e54",false],"id":null,"method":"mining.notify"}
I (1653349) bm1368Module: Job ID: F7
I (1653439) bm1368Module: RX Job ID: 78
I (1653449) asic_result: Nonce difficulty 1962.69 of 479.
I (1653459) create_jobs_task: New Work Dequeued 648516380010a383
W (1653459) httpd_txrx: httpd_sock_err: error in send : 104
W (1653459) httpd_txrx: httpd_sock_err: error in send : 128
W (1653469) httpd_txrx: httpd_sock_err: error in send : 128
W (1653479) httpd_txrx: httpd_sock_err: error in send : 128
W (1653479) httpd_txrx: httpd_sock_err: error in send : 128
W (1653479) httpd_txrx: httpd_sock_err: error in send : 128
W (1653499) httpd_txrx: httpd_sock_err: error in send : 128
W (1653499) httpd_txrx: httpd_sock_err: error in send : 128
W (1653509) httpd_txrx: httpd_sock_err: error in send : 128
W (1653509) httpd_txrx: httpd_sock_err: error in send : 128
W (1653519) httpd_txrx: httpd_sock_err: error in send : 128
W (1653519) httpd_txrx: httpd_sock_err: error in send : 128
W (1653529) httpd_txrx: httpd_sock_err: error in send : 128
W (1653529) httpd_txrx: httpd_sock_err: error in send : 128
W (1653549) httpd_txrx: httpd_sock_err: error in send : 128
W (1653549) httpd_txrx: httpd_sock_err: error in send : 128
W (1653559) httpd_txrx: httpd_sock_err: error in send : 128
W (1653559) httpd_txrx: httpd_sock_err: error in send : 128
W (1653569) httpd_txrx: httpd_sock_err: error in send : 128
W (1653579) httpd_txrx: httpd_sock_err: error in send : 128
W (1653579) httpd_txrx: httpd_sock_err: error in send : 128
W (1653579) httpd_txrx: httpd_sock_err: error in send : 128
W (1653599) httpd_txrx: httpd_sock_err: error in send : 128
W (1653599) httpd_txrx: httpd_sock_err: error in send : 128
W (1653609) httpd_txrx: httpd_sock_err: error in send : 128
W (1653609) httpd_txrx: httpd_sock_err: error in send : 128
W (1653619) httpd_txrx: httpd_sock_err: error in send : 128
W (1653629) httpd_txrx: httpd_sock_err: error in send : 128
W (1653629) httpd_txrx: httpd_sock_err: error in send : 128
W (1653639) httpd_txrx: httpd_sock_err: error in send : 128
W (1653639) httpd_txrx: httpd_sock_err: error in send : 128
W (1653649) httpd_txrx: httpd_sock_err: error in send : 128

***ERROR*** A stack overflow in task asic result has been detected.


Backtrace: 0x40375c42:0x3fccc1b0 0x4037d819:0x3fccc1d0 0x4037e7d2:0x3fccc1f0 0x4037fca7:0x3fccc270 0x4037e898:0x3fccc290 0x4037e88e:0x00000000 |<-CORRUPTED




ELF file SHA256: 4ae5e3ac7675b79f

Rebooting...
ESP-ROM:esp32s3-20210327
Build:Mar 27 2021
rst:0xc (RTC_SW_CPU_RST),boot:0x2a (SPI_FAST_FLASH_BOOT)
Saved PC:0x40375b7c
SPIWP:0xee
mode:DIO, clock div:1
load:0x3fce3818,len:0x16e0
load:0x403c9700,len:0x4
load:0x403c9704,len:0xc00
load:0x403cc700,len:0x2eb0
entry 0x403c9908
I (26) boot: ESP-IDF v5.1 2nd stage bootloader
I (26) boot: compile time Mar  3 2024 19:55:36
I (26) boot: Multicore bootloader
I (29) boot: chip revision: v0.2
I (33) boot.esp32s3: Boot SPI Speed : 80MHz
I (38) boot.esp32s3: SPI Mode       : DIO
I (43) boot.esp32s3: SPI Flash Size : 16MB
I (47) boot: Enabling RNG early entropy source...
I (53) boot: Partition Table:
I (56) boot: ## Label            Usage          Type ST Offset   Length
I (64) boot:  0 nvs              WiFi data        01 02 00009000 00006000
I (71) boot:  1 phy_init         RF data          01 01 0000f000 00001000
I (79) boot:  2 factory          factory app      00 00 00010000 00400000
I (86) boot:  3 www              Unknown data     01 82 00410000 00300000
I (93) boot:  4 ota_0            OTA app          00 10 00710000 00400000
I (101) boot:  5 ota_1            OTA app          00 11 00b10000 00400000
I (109) boot:  6 otadata          OTA data         01 00 00f10000 00002000
I (116) boot:  7 coredump         Unknown data     01 03 00f12000 00010000
I (124) boot: End of partition table
I (128) esp_image: segment 0: paddr=00710020 vaddr=3c0b0020 size=2a81ch (174108) map
I (168) esp_image: segment 1: paddr=0073a844 vaddr=3fc9a800 size=05018h ( 20504) load
I (173) esp_image: segment 2: paddr=0073f864 vaddr=40374000 size=007b4h (  1972) load
I (174) esp_image: segment 3: paddr=00740020 vaddr=42000020 size=ac674h (706164) map
I (309) esp_image: segment 4: paddr=007ec69c vaddr=403747b4 size=15fcch ( 90060) load
I (338) boot: Loaded app from partition at offset 0x710000
I (339) boot: Disabling RNG early entropy source...
I (350) cpu_start: Multicore app
I (360) cpu_start: Pro cpu start user code
I (360) cpu_start: cpu freq: 160000000 Hz
I (361) app_init: Application information:
I (363) app_init: Project name:     esp-miner
I (368) app_init: App version:      v2.1.7
I (373) app_init: Compile time:     Jun  2 2024 09:14:19
I (379) app_init: ELF file SHA256:  4ae5e3ac7675b79f...
I (385) app_init: ESP-IDF:          v5.3-beta1-105-g3f632df143
I (391) efuse_init: Min chip rev:     v0.0
I (396) efuse_init: Max chip rev:     v0.99
I (401) efuse_init: Chip rev:         v0.2
I (406) heap_init: Initializing. RAM available for dynamic allocation:
I (413) heap_init: At 3FCA5200 len 00044510 (273 KiB): RAM
I (419) heap_init: At 3FCE9710 len 00005724 (21 KiB): RAM
I (425) heap_init: At 3FCF0000 len 00008000 (32 KiB): DRAM
I (431) heap_init: At 600FE100 len 00001EE8 (7 KiB): RTCRAM
I (439) spi_flash: detected chip: gd
I (442) spi_flash: flash io: dio
W (446) i2c: This driver is an old driver, please migrate your application code to adapt `driver/i2c_master.h`
W (457) ADC: legacy driver is deprecated, please migrate to `esp_adc/adc_oneshot.h`
I (465) sleep: Configure to isolate all GPIO pins in sleep state
I (472) sleep: Enable automatic switching of GPIO sleep configuration
I (479) main_task: Started on CPU0
I (489) main_task: Calling app_main()
I (519) miner: NVS_CONFIG_ASIC_FREQ 490.000000
I (519) miner: ASIC: BM1368
I (519) SystemModule: I2C initialized successfully
I (519) DS4432U.c: Set ASIC voltage = 1.200V [0xC6]
I (529) DS4432U.c: Writing 0xC6
I (529) miner: Welcome to the bitaxe!
I (539) pp: pp rom version: e7ae62f
I (539) net80211: net80211 rom version: e7ae62f
I (559) wifi:wifi driver task: 3fcb08c8, prio:23, stack:6656, core=0
I (569) wifi:wifi firmware version: f9a71af
I (569) wifi:wifi certification version: v7.0
I (569) wifi:config NVS flash: enabled
I (569) wifi:config nano formating: disabled
I (569) wifi:Init data frame dynamic rx buffer num: 32
I (579) wifi:Init static rx mgmt buffer num: 5
I (579) wifi:Init management short buffer num: 32
I (589) wifi:Init dynamic tx buffer num: 32
I (589) wifi:Init static tx FG buffer num: 2
I (589) wifi:Init static rx buffer size: 1600
I (599) wifi:Init static rx buffer num: 10
I (599) wifi:Init dynamic rx buffer num: 32
I (609) wifi_init: rx ba win: 6
I (609) wifi_init: accept mbox: 6
I (609) wifi_init: tcpip mbox: 32
I (619) wifi_init: udp mbox: 6
I (619) wifi_init: tcp mbox: 6
I (629) wifi_init: tcp tx win: 5744
I (629) wifi_init: tcp rx win: 5744
I (629) wifi_init: tcp mss: 1440
I (639) wifi_init: WiFi IRAM OP enabled
I (639) wifi_init: WiFi RX IRAM OP enabled
I (659) wifi station: ESP_WIFI Access Point On
W (659) wifi:Affected by the ESP-NOW encrypt num, set the max connection num to 10
I (659) wifi station: ESP_WIFI_MODE_STA
I (669) wifi station: wifi_init_sta finished.
I (669) phy_init: phy_version 670,b7bc9b9,Apr 30 2024,10:54:13
I (709) wifi:mode : sta (dc:da:0c:3a:51:ac) + softAP (dc:da:0c:3a:51:ad)
I (709) wifi:enable tsf
I (709) wifi:Total power save buffer number: 16
I (709) wifi:Init max length of beacon: 752/752
I (719) wifi:Init max length of beacon: 752/752
I (719) esp_netif_lwip: DHCP server started on interface WIFI_AP_DEF with IP: 192.168.4.1
I (729) wifi:new:<1,1>, old:<1,1>, ap:<1,1>, sta:<1,0>, prof:1, snd_ch_cfg:0x0
I (739) wifi:state: init -> auth (0xb0)
I (739) wifi station: ESP_WIFI setting hostname to: espressif
I (749) wifi station: wifi_init_sta finished.
I (1179) SystemModule: OLED init success!
I (1259) http_server: Partition size: total: 2884241, used: 664648
I (1259) http_server: Starting HTTP Server
I (1259) example_dns_redirect_server: Socket created
I (1269) example_dns_redirect_server: Socket bound, port 53
I (1269) example_dns_redirect_server: Waiting for data
I (5089) wifi:state: auth -> init (0x200)
I (5099) wifi:new:<1,0>, old:<1,1>, ap:<1,1>, sta:<1,0>, prof:1, snd_ch_cfg:0x0
I (7599) wifi station: Retrying WiFi connection...
I (8359) wifi:ap channel adjust o:1,1 n:6,2
I (8359) wifi:new:<6,0>, old:<1,0>, ap:<6,2>, sta:<6,0>, prof:1, snd_ch_cfg:0x0
I (8359) wifi:state: init -> auth (0xb0)
I (9149) wifi:state: auth -> assoc (0x0)
I (9159) wifi:state: assoc -> run (0x10)
I (9179) wifi:connected with WLAN, aid = 5, channel 6, BW20, bssid = d4:24:dd:12:16:5d
I (9179) wifi:security: WPA3-SAE, phy: bgn, rssi: -45
I (9199) wifi:pm start, type: 1

I (9199) wifi:dp: 1, bi: 102400, li: 3, scale listen interval from 307200 us to 307200 us
I (9199) wifi:set rx beacon pti, rx_bcn_pti: 0, bcn_timeout: 25000, mt_pti: 0, mt_time: 10000
I (9209) wifi:<ba-add>idx:0 (ifx:0, d4:24:dd:12:16:5d), tid:0, ssn:0, winSize:64
I (9229) wifi:AP's beacon interval = 102400 us, DTIM period = 1
I (10209) wifi station: Bitaxe ip:192.168.XXX.XXX
I (10209) esp_netif_handlers: sta ip: 192.168.XXX.XXX, mask: 255.255.255.0, gw: 192.168.0.1
I (10209) miner: Connected to SSID: WLAN
I (10219) gpio: GPIO[12]| InputEn: 1| OutputEn: 0| OpenDrain: 0| Pullup: 0| Pulldown: 0| Intr:0
I (10219) wifi station: ESP_WIFI Access Point Off
I (10229) wifi:mode : sta (dc:da:0c:3a:51:ac)
I (10239) serial: Initializing serial
I (10239) bm1368Module: Initializing BM1368
I (11439) bm1368Module: 1 chip(s) detected on the chain
I (11439) bm1368Module: Setting ASIC difficulty mask to 255
final refdiv: 2, fbdiv: 235, postdiv1: 6, postdiv2: 1, min diff value: 0.416656
I (17939) bm1368Module: Setting Frequency to 490.00MHz (0.01)
I (17939) bm1368Module: Setting max baud of 1000000
I (17939) serial: Changing UART baud to 1000000
I (17949) stratum_task: Get IP for URL: solo.ckpool.org

I (17959) ASIC_task: ASIC Ready!
I (17959) main_task: Returned from app_main()
I (17959) stratum_task: Connecting to: stratum+tcp://solo.ckpool.org:3333 (51.81.56.15)

I (17969) stratum_task: Socket created, connecting to 51.81.56.15:3333
I (18139) stratum_api: tx: {"id": 1, "method": "mining.subscribe", "params": ["bitaxe/BM1368"]}

I (18139) stratum_api: tx: {"id": 2, "method": "mining.configure", "params": [["version-rolling"], {"version-rolling.mask": "ffffffff"}]}

I (18149) stratum_api: tx: {"id": 3, "method": "mining.suggest_difficulty", "params": [1000]}

I (18159) stratum_api: tx: {"id": 4, "method": "mining.authorize", "params": ["BC-ADDRESS", "x"]}

I (18349) stratum_task: rx: {"result":[[["mining.notify","749cca50"]],"458c0371",8],"id":1,"error":null}
I (18349) stratum_api: extranonce_str: 458c0371
I (18349) stratum_api: extranonce_2_len: 8
I (18359) stratum_task: rx: {"params":[10000],"id":null,"method":"mining.set_difficulty"}
I (18369) stratum_task: Set stratum difficulty: 10000
I (18449) stratum_task: rx: {"result":{"version-rolling":true,"version-rolling.mask":"1fffe000"},"id":2,"error":null}
I (18449) stratum_api: Set version mask: 1fffe000
I (18459) stratum_task: rx: {"params":["648516380010a383","26c604aac06ee1966425490d8f12d4df01b295e4000142e90000000000000000","01000000010000000000000000000000000000000000000000000000000000000000000000ffffffff350305eb0c0004540e60660442e8f3130c","0a636b706f6f6c112f736f6c6f2e636b706f6f6c2e6f72672fffffffff035262a813000000002200201bc038ee5f8759ad75eb703c00d860de2ac75fdb6c2852424845ee1998927da4a3b366000000000016001451ed61d2f6aa260cc72cdf743e4e436a82c010270000000000000000266a24aa21a9ed60c4d513c43a6c611793399ecde11fc5cc5b0b28c049239d7d6b50e203fbb1bf00000000",["6e2cb12ab468ff1e13ccfd55c290d8a0d5fe7f56a48f0d744a763600de3d3cd6","16af7a609116b0526eb4cba78dc433dbddb0ec479beb8f0b171f53ab9ac429f4","82748581976bdf6e97a6e057b124ec4cf1521888e36aad3dc29ab303e28a5bc1","022521e2e2a54400e6a71ef17560bc2d4a2f6822a6bf17bd39c5a927ac19ec32","5ce64ad7cb44b856f18656ac2e8c21861b9d77fc3274caf6f7aa21e4f275b3b2","f35addc74fb38c79669f154fc3ffaaa4d7ba444564d500d7e9b7a07c583687e4","72705aff85ad8ae889e1181e9878c0ebe4aba8285a9c2c5b3a2f25b124c3a1e1","6fe0f7a36bd6cc5430a3e4a503c06e9d19c22909957ae4b0865231329e998802","52c08aaea04d7cac4d14feda2fa7d1b2065524176372624221f176684d474d03","d6bcd93c59654ff2211b28a55d6094e8ab01bc026bc651cc9ceba5d679026aee","9a5ea3d403a4fb19083df7006a0fd62d36f9a5708afb7ab0137fc239fd248c59","9b27f4e3ec17fea297207ddea63ab5b0b9d3f2155324155c96044042b84cdd2d","35c9d7a14fdefcd2e63b4bc72bfcab85bcaa9d6e4414921579867164aaaa7d25"],"20000000","170355f0","66600e54",true],"id":null,"method":"mining.notify"}
I (18589) SystemModule: Syncing clock
I (18589) create_jobs_task: New Work Dequeued 648516380010a383
I (18589) stratum_task: rx: {"params":[10000],"id":null,"method":"mining.set_difficulty"}
I (18599) ASIC_task: New pool difficulty 10000
I (18609) stratum_task: rx: {"result":true,"error":null,"id":4}
I (18619) stratum_task: setup message accepted
I (21529) bm1368Module: Job ID: F1
I (21529) bm1368Module: RX Job ID: 78
I (21529) asic_result: Nonce difficulty 546.91 of 10000.
I (21639) bm1368Module: Job ID: 0A
I (21639) bm1368Module: RX Job ID: 00
I (21639) asic_result: Nonce difficulty 445.61 of 10000.
I (22819) bm1368Module: Job ID: 26
I (22819) bm1368Module: RX Job ID: 10
I (22819) asic_result: Nonce difficulty 422.61 of 10000.
I (23479) bm1368Module: Job ID: 83
I (23479) bm1368Module: RX Job ID: 40
I (23479) asic_result: Nonce difficulty 1166.99 of 10000.
I (23489) bm1368Module: Job ID: BF
I (23489) bm1368Module: RX Job ID: 58
I (23489) asic_result: Nonce difficulty 1767.21 of 10000.
I (24329) bm1368Module: Job ID: 75
I (24329) bm1368Module: RX Job ID: 38
I (24329) asic_result: Nonce difficulty 665.04 of 10000.
I (24519) bm1368Module: Job ID: 0D
I (24519) bm1368Module: RX Job ID: 00
I (24519) asic_result: Nonce difficulty 774.87 of 10000.
I (29509) stratum_task: rx: {"params":["648516380010a384","26c604aac06ee1966425490d8f12d4df01b295e4000142e90000000000000000","01000000010000000000000000000000000000000000000000000000000000000000000000ffffffff350305eb0c0004720e6066046b9c780b0c","0a636b706f6f6c112f736f6c6f2e636b706f6f6c2e6f72672fffffffff03cfabaa13000000002200201bc038ee5f8759ad75eb703c00d860de2ac75fdb6c2852424845ee1998927da496bf66000000000016001451ed61d2f6aa260cc72cdf743e4e436a82c010270000000000000000266a24aa21a9edf9fdc988f5d800e2953c2262aeb31c1e748fddf2dccccf579dda07ef2e7ea6d500000000",["6e2cb12ab468ff1e13ccfd55c290d8a0d5fe7f56a48f0d744a763600de3d3cd6","8d00f23b1e3beb9bbfb1efdb9a3357e3b34719f44f799ac49816514519946fcf","94edcd1e89c1d8e47859fdb234847f02568463ceb699293f58cb2b7142884733","be200d929ed76364b0c246b4440ca7e6aebf841034669f5e3fcf7eaa6d09daaf","ce27f5e1d2adf17c36bb9b12112b847c15607f549702119aac15e2173371f03e","abce0ce52924c49b5003d4b624636c53f52cd227043e885288c9efd4ba1bf975","30864bd02765e19ba05cb64ff508c004a9d3368aea007a6abd7ca57aa0aae0bb","4197e9794c996deba513ae1ca7aa67024b3371a98863d79bc1b35471f333cbcc","9b1e33dcd34c26bd7777998be50116f462c8803a2b7b97d0a5950a29a7fbb058","380c4f72bcab87b8b56716d2728b12fc0099992966efedf60d47c4d9f8c80955","e9bde485a6d31daef033f48f3c02c94411df01b96a48482bdf9574bff11644b7","6e0c6daef852de3617d38238e0ce95f9da1448a86c201031961c3486f2d0cf74","8814515d93ce0cb3d50957b739e109a89d1f79a10e37d219c60d1d52f14b3af5"],"20000000","170355f0","66600e72",false],"id":null,"method":"mining.notify"}
I (29639) create_jobs_task: New Work Dequeued 648516380010a384

```

### solobito on 2024-06-05

The same thing happens to me, `httpd_txrx: httpd_sock_err: error`.

**To reproduce the error,** you need to run the following script in Python and wait. It establishes a WebSocket connection and makes an HTTP request every 5 seconds. I just realized that if I only establish one WebSocket connection, the error does not appear as quickly.

If instead of running this script, you view the data in the browser (AxeOS), the reboots do not occur as often.

```python
# python3 -m venv .venv
# source .venv/bin/activate
# python3 -m pip install websocket-client
# python3 bitaxeLogger.py
```

```python
# bitaxeLogger.py

import websocket # websocket-client
import threading
import urllib.request
import json
import time

# CHANGE ME!!
bitaxe_ip = "192.168.0.7"

def on_message(ws, message):
    print(message)
    
def on_error(ws, error):
    msg = "### Clsed ###"
    print(f"{msg} error={error}")

def on_close(ws, close_status_code, close_msg):
    print(f"close_status_code={close_msg} close_status_code={close_status_code}")
    print (f"Retry 20s")
    time.sleep(20)
    connect_ws() # retry per 20 seconds

def on_open(ws):
    msg = "### Opened ws connection ###"
    print(msg)
    
def get_info():
    while True:
        contents = urllib.request.urlopen("http://" + bitaxe_ip + "/api/system/info", timeout=5).read()
        j = json.loads(contents)
        for key in j.keys():
            print(f"  {key}: {j[key]}")
            
        time.sleep(5) # seconds
    
def connect_ws():
    #websocket.enableTrace(True)
    ws = websocket.WebSocketApp("ws://" + bitaxe_ip + "/api/ws" ,
                              on_open=on_open,
                              on_message=on_message,
                              on_error=on_error,
                              on_close=on_close)
    ws.run_forever(reconnect=10)
    
if __name__ == "__main__":
    
    # INFO
    thread_info = threading.Thread(target=get_info, args=())
    thread_info.start()
    
    # WebSockets
    thread_ws = threading.Thread(target=connect_ws, args=())
    thread_ws.start()
    
    print("WS END!")
```



### Shen on 2024-07-11

Do you have a potential solution for this problem in sight?

### solobito on 2024-10-10

This has already been fixed in version 2.2.2. Maybe due to these changes: "_Fix websocket logs causing device to crash #277 by @eandersson in #318_"
