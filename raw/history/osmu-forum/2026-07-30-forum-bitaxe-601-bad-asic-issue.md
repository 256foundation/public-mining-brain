# Bitaxe 601 bad asic issue

> Source: https://osmu.xyz/t/bitaxe-601-bad-asic-issue/72
> Collected: 2026-10-10
> Published: 2026-07-30
> Registry ID: osmu-forum

Unknown_aadhi | 2026-07-30 21:45:10 UTC | #1

I dunno if this asic is bad or if there is a bug or not , the hashrate of this bitaxe 601 is at 400ths

![image0](https://osmu.xyz/uploads/default/original/1X/f4f8dddcd1ef66f61a3946871bea614b65ecc5af.jpeg)

-------------------------

Lidamao | 2026-07-31 01:46:52 UTC | #2

Me too,and I try many seting cann’t solve this BUG

-------------------------

Unknown_aadhi | 2026-07-31 02:49:50 UTC | #3

Turns out it was bad asic for my case , if you can share your log file everyone can review it and find the issue .

-------------------------

Lidamao | 2026-07-31 06:10:02 UTC | #4

Are you sure it’s the core that’s broken?this my logs

e[0;32mI (1051) bitaxe: Welcome to the bitaxe - FOSS || GTFO!e[0m

e[0;32mI (1054) bitaxe: I2C initialized successfullye[0m

e[0;32mI (1058) bitaxe: RST pin initialized to lowe[0m

e[0;32mI (1163) adc: calibration scheme version is Curve Fittinge[0m

e[0;32mI (1163) adc: Calibration Successe[0m

e[0;32mI (1194) nvs_config: Used entries: 276e[0m

e[0;32mI (1194) nvs_config: Free entries: 480e[0m

e[0;32mI (1194) nvs_config: Available entries: 354e[0m

e[0;32mI (1197) nvs_config: Total entries: 756e[0m

e[0;32mI (1217) device_config: Device Model: Gammae[0m

e[0;32mI (1217) device_config: Board Version: 601e[0m

e[0;32mI (1217) device_config: ASIC: 1x BM1370 (128 cores)e[0m

e[0;32mI (1221) system: Initial overheat_mode value: 0e[0m

e[0;32mI (1229) pp: pp rom version: e7ae62fe[0m

e[0;32mI (1231) net80211: net80211 rom version: e7ae62fe[0m

I (1237) wifi:wifi driver task: 3fcbe7ec, prio:23, stack:6656, core=0

I (1251) wifi:wifi firmware version: 4df78f2

I (1252) wifi:wifi certification version: v7.0

I (1252) wifi:config NVS flash: enabled

I (1253) wifi:config nano formatting: disabled

I (1258) wifi:Init data frame dynamic rx buffer num: 32

I (1263) wifi:Init static rx mgmt buffer num: 5

I (1267) wifi:Init management short buffer num: 32

I (1272) wifi:Init static tx buffer num: 16

I (1276) wifi:Init tx cache buffer num: 32

I (1279) wifi:Init static tx FG buffer num: 2

I (1283) wifi:Init static rx buffer size: 1600

I (1287) wifi:Init static rx buffer num: 16

I (1291) wifi:Init dynamic rx buffer num: 32

e[0;32mI (1296) wifi_init: rx ba win: 16e[0m

e[0;32mI (1299) wifi_init: accept mbox: 6e[0m

e[0;32mI (1303) wifi_init: tcpip mbox: 32e[0m

e[0;32mI (1307) wifi_init: udp mbox: 6e[0m

e[0;32mI (1311) wifi_init: tcp mbox: 6e[0m

e[0;32mI (1315) wifi_init: tcp tx win: 5760e[0m

e[0;32mI (1319) wifi_init: tcp rx win: 5760e[0m

e[0;32mI (1324) wifi_init: tcp mss: 1440e[0m

e[0;32mI (1327) wifi_init: WiFi/LWIP prefer SPIRAMe[0m

e[0;32mI (1332) wifi_init: WiFi IRAM OP enablede[0m

e[0;32mI (1337) wifi_init: WiFi RX IRAM OP enablede[0m

e[0;32mI (1347) connect: ESP_WIFI_MODE_STAe[0m

e[0;32mI (1348) connect: Wi-Fi Password provided, using WPA2e[0m

e[0;32mI (1352) connect: wifi_init_sta finished.e[0m

I (1356) wifi:Set ps type: 0, coexist: 0

e[0;32mI (1360) connect: ESP_WIFI setting hostname to: bitaxee[0m

e[0;32mI (1366) phy_init: phy_version 711,97bcf0a2,Aug 25 2025,19:04:10e[0m

I (1409) wifi:mode : sta (a4:cb:8f:e2:5a:70) + softAP (a4:cb:8f:e2:5a:71)

I (1410) wifi:enable tsf

I (1411) wifi:Total power save buffer number: 8

I (1412) wifi:Init max length of beacon: 752/752

I (1416) wifi:Init max length of beacon: 752/752

e[0;32mI (1420) connect: Connecting…e[0m

e[0;32mI (1425) connect: wifi_init_sta finished.e[0m

e[0;32mI (1426) connect: Configuration Access Point enablede[0m

e[0;32mI (1435) esp_netif_lwip: DHCP server started on interface WIFI_AP_DEF with IP: 192.168.4.1e[0m

e[0;32mI (1435) display: SSD1306 (128x32)e[0m

e[0;32mI (1447) display: Install panel IOe[0m

e[0;32mI (1451) display: Install panel drivere[0m

e[0;32mI (1457) display: Initialize LVGLe[0m

e[0;32mI (1461) LVGL: Starting LVGL taske[0m

e[0;32mI (1480) display: Rotation: 0e[0m

e[0;32mI (1581) display: Display init success!e[0m

e[0;32mI (1581) input: Install button drivere[0m

e[0;32mI (1659) system: Existing overheat_mode value: 0e[0m

e[0;32mI (1788) filesystem: Partition size: total: 2884241, used: 756012e[0m

e[0;32mI (1789) TPS546: Initializing the core voltage regulatore[0m

e[0;32mI (1805) TPS546: Device ID: 54 49 54 6d 24 41e[0m

e[0;32mI (1805) TPS546: Power config-OPERATION: 00e[0m

e[0;32mI (1806) TPS546: Power config-ON_OFF_CONFIG: 1Fe[0m

e[0;32mI (1810) TPS546: Reading MFR infoe[0m

e[0;32mI (1814) TPS546: MFR_ID: 00 00 00e[0m

e[0;32mI (1817) TPS546: MFR_MODEL: 00 00 00e[0m

e[0;32mI (1822) TPS546: MFR_REVISION: 00 00 00e[0m

e[0;32mI (1826) TPS546: Writing new config valuese[0m

e[0;32mI (1833) TPS546: VOUT_MODE: 97e[0m

e[0;32mI (1835) TPS546: —Writing new config values to TPS546—e[0m

e[0;32mI (1841) TPS546: Setting ON_OFF_CONFIG: 1Be[0m

e[0;32mI (1846) TPS546: Setting STACK_CONFIG: 0000e[0m

e[0;32mI (1851) TPS546: Setting SYNC_CONFIG: 10e[0m

e[0;32mI (1855) TPS546: Setting PHASE: 00e[0m

e[0;32mI (1859) TPS546: Setting FREQUENCY: 650MHze[0m

e[0;32mI (1864) TPS546: Setting VIN_ON: 4.80Ve[0m

e[0;32mI (1869) TPS546: Setting VIN_OFF: 4.50Ve[0m

e[0;32mI (1873) TPS546: Setting VIN_OV_FAULT_LIMIT: 6.50Ve[0m

e[0;32mI (1879) TPS546: Setting VIN_OV_FAULT_RESPONSE: B7e[0m

e[0;32mI (1884) TPS546: Setting VOUT SCALE: 0.25e[0m

e[0;32mI (1889) TPS546: Setting VOUT_COMMAND: 1.20Ve[0m

e[0;32mI (1894) TPS546: Setting VOUT_MAX: 2.00Ve[0m

e[0;32mI (1899) TPS546: Setting VOUT_MIN: 1.00Ve[0m

e[0;32mI (1903) TPS546: Setting VOUT_OV_FAULT_LIMIT: 1.25e[0m

e[0;32mI (1909) TPS546: Setting VOUT_OV_WARN_LIMIT: 1.16e[0m

e[0;32mI (1914) TPS546: Setting VOUT_MARGIN_HIGH: 1.10e[0m

e[0;32mI (1919) TPS546: Setting VOUT_MARGIN_LOW: 0.90e[0m

e[0;32mI (1925) TPS546: Setting VOUT_UV_WARN_LIMIT: 0.90e[0m

e[0;32mI (1930) TPS546: Setting VOUT_UV_FAULT_LIMIT: 0.75e[0m

e[0;32mI (1936) TPS546: ----- IOUTe[0m

e[0;32mI (1938) TPS546: Setting IOUT_OC_WARN_LIMIT: 25.00Ae[0m

e[0;32mI (1944) TPS546: Setting IOUT_OC_FAULT_LIMIT: 30.00Ae[0m

e[0;32mI (1950) TPS546: Setting IOUT_OC_FAULT_RESPONSE: c0e[0m

e[0;32mI (1955) TPS546: ----- TEMPERATUREe[0m

e[0;32mI (1959) TPS546: Setting OT_WARN_LIMIT: 105Ce[0m

e[0;32mI (1964) TPS546: Setting OT_FAULT_LIMIT: 145Ce[0m

e[0;32mI (1969) TPS546: Setting OT_FAULT_RESPONSE: ffe[0m

e[0;32mI (1974) TPS546: ----- TIMINGe[0m

e[0;32mI (1978) TPS546: Setting TON_DELAY: 0mse[0m

e[0;32mI (1982) TPS546: Setting TON_RISE: 3mse[0m

e[0;32mI (1987) TPS546: Setting TON_MAX_FAULT_LIMIT: 0mse[0m

e[0;32mI (1992) TPS546: Setting TON_MAX_FAULT_RESPONSE: 3be[0m

e[0;32mI (1998) TPS546: Setting TOFF_DELAY: 0mse[0m

e[0;32mI (2002) TPS546: Setting TOFF_FALL: 0mse[0m

e[0;32mI (2007) TPS546: Setting PIN_DETECT_OVERRIDEe[0m

e[0;32mI (2012) TPS546: -----------VOLTAGE---------------------e[0m

e[0;32mI (2018) TPS546: read VIN_ON: 4.80Ve[0m

e[0;32mI (2022) TPS546: read VIN_OFF: 4.50Ve[0m

e[0;32mI (2026) TPS546: read VIN_OV_FAULT_LIMIT: 6.50Ve[0m

e[0;32mI (2032) TPS546: read VIN_UV_WARN_LIMIT: 2.50Ve[0m

e[0;32mI (2037) TPS546: read VIN_OV_FAULT_RESPONSE: B7e[0m

e[0;32mI (2042) TPS546: read VOUT_MAX: 2.00Ve[0m

e[0;32mI (2047) TPS546: read VOUT_OV_FAULT_LIMIT: 1.50Ve[0m

e[0;32mI (2052) TPS546: read VOUT_OV_WARN_LIMIT: 1.39Ve[0m

e[0;32mI (2057) TPS546: read VOUT_MARGIN_HIGH: 1.32Ve[0m

e[0;32mI (2062) TPS546: read VOUT_COMMAND: 1.20Ve[0m

e[0;32mI (2067) TPS546: read VOUT_MARGIN_LOW: 1.08Ve[0m

e[0;32mI (2072) TPS546: read VOUT_UV_WARN_LIMIT: 1.08Ve[0m

e[0;32mI (2077) TPS546: read VOUT_UV_FAULT_LIMIT: 0.90Ve[0m

e[0;32mI (2082) TPS546: read VOUT_MIN: 1.00 Ve[0m

e[0;32mI (2086) TPS546: read STATUS_WORD: 0840e[0m

e[0;32mI (2091) TPS546: -----------VOLTAGE/CURRENT---------------------e[0m

e[0;32mI (2098) TPS546: read READ_VIN: 5.21Ve[0m

e[0;32mI (2102) TPS546: read READ_IOUT: -0.19Ae[0m

e[0;32mI (2106) TPS546: read READ_VOUT: 0.02Ve[0m

e[0;32mI (2110) TPS546: -----------TIMING---------------------e[0m

e[0;32mI (2117) TPS546: read TON_DELAY: 0mse[0m

e[0;32mI (2121) TPS546: read TON_RISE: 3mse[0m

e[0;32mI (2125) TPS546: read TON_MAX_FAULT_LIMIT: 0mse[0m

e[0;32mI (2130) TPS546: read TON_MAX_FAULT_RESPONSE: 3be[0m

e[0;32mI (2135) TPS546: read TOFF_DELAY: 0mse[0m

e[0;32mI (2140) TPS546: read TOFF_FALL: 0mse[0m

e[0;32mI (2144) TPS546: ---------CONFIG--------------------e[0m

e[0;32mI (2150) TPS546: read PHASE: 00e[0m

e[0;32mI (2170) TPS546: read STACK_CONFIG: 0000e[0m

e[0;32mI (2171) TPS546: read SYNC_CONFIG: 10e[0m

e[0;32mI (2171) TPS546: read INTERLEAVE: 0020e[0m

e[0;32mI (2173) TPS546: read CAPABILITY: d0e[0m

e[0;32mI (2177) TPS546: ---------OPERATION------------------e[0m

e[0;32mI (2183) TPS546: read OPERATION: 00e[0m

e[0;32mI (2187) TPS546: read ON_OFF_CONFIG: 1be[0m

e[0;32mI (2203) TPS546: read COMPENSATION CONFIGe[0m

e[0;32mI (2204) TPS546: 13 11 08 19 04e[0m

e[0;32mI (2204) TPS546: Clearing faultse[0m

e[0;32mI (2217) TPS546: read STATUS_WORD: 0840e[0m

e[0;32mI (2217) EMC2101: Initializing EMC2101 (Temperature offset: 0° C)e[0m

e[0;32mI (2218) thermal: EMC2101 configuration: Ideality Factor: 24, Beta Compensation: 00e[0m

e[0;32mI (2233) power_management: Startinge[0m

e[0;32mI (2234) power_management: ASIC Frequency: 525 MHz, Expected hashrate: 1.07GH/se[0m

e[0;32mI (2238) fan_controller: Startinge[0m

e[0;32mI (2239) http_server: Starting HTTP Servere[0m

e[0;32mI (2242) fan_controller: Set to Manual mode, fan speed: 100.0%e[0m

e[0;32mI (2252) dns_server: Socket createde[0m

e[0;32mI (2251) websocket_log: websocket_log_task startinge[0m

e[0;32mI (2258) dns_server: Socket bound, port 53e[0m

e[0;32mI (2251) websocket_api: websocket_api_task startinge[0m

e[0;32mI (2268) dns_server: Waiting for datae[0m

e[0;32mI (2253) system: Firmware Version: v2.14.2e[0m

e[0;32mI (2282) system: AxeOS Version: v2.14.2e[0m

e[0;32mI (2287) BAP: Initializing BAP systeme[0m

e[0;32mI (2293) BAP: BAP system initialized successfullye[0m

e[0;32mI (2740) power_management: setting new vcore voltage to 1200mVe[0m

e[0;32mI (2740) vcore: Set ASIC voltage = 1.200Ve[0m

e[0;32mI (2741) TPS546: Vout changed to 1.20 Ve[0m

I (4263) wifi:ap channel adjust o:1,1 n:13,2

I (4263) wifi:new:<13,0>, old:<1,1>, ap:<13,2>, sta:<13,0>, prof:1, snd_ch_cfg:0x0

I (4264) wifi:state: init → auth (0xb0)

I (4273) wifi:state: auth → assoc (0x0)

I (4282) wifi:state: assoc → run (0x10)

I (4287) wifi:idx:0 (ifx:0, ee:b9:70:81:7a:f0), tid:5, ssn:0, winSize:64

e[0;31mE (4378) TPS546: Status: 0x0840e[0m

e[0;31mE (4378) TPS546: The voltage regulator is turned offe[0m

I (4388) wifi:idx:1 (ifx:0, ee:b9:70:81:7a:f0), tid:0, ssn:2, winSize:64

I (4389) wifi:connected with YYGLGG, aid = 29, channel 13, BW20, bssid = ee:b9:70:81:7a:f0

I (4392) wifi:security: WPA2-PSK, phy: bgn, rssi: -44

I (4399) wifi:pm start, type: 0

I (4400) wifi:dp: 1, bi: 102400, li: 3, scale listen interval from 307200 us to 307200 us

I (4408) wifi:set rx beacon pti, rx_bcn_pti: 0, bcn_timeout: 25000, mt_pti: 0, mt_time: 10000

E (4416) wifi:sta is connecting, cannot set config

I (4421) wifi:AP’s beacon interval = 102400 us, DTIM period = 1

e[0;32mI (4428) connect: Acquiring IP…e[0m

e[0;32mI (5945) connect: IPv4 Address: 192.168.1.180e[0m

e[0;32mI (5945) connect: Connected to SSID: YYGLGGe[0m

I (5946) wifi:mode : sta (a4:cb:8f:e2:5a:70)

e[0;32mI (5949) esp_netif_handlers: sta ip: 192.168.1.180, mask: 255.255.255.0, gw: 192.168.1.1e[0m

e[0;32mI (5957) connect: Configuration Access Point disablede[0m

e[0;32mI (6030) asic_init: Starting ASIC initialization (cold boot mode)e[0m

e[0;32mI (6230) asic_init: Performing full UART initializatione[0m

e[0;32mI (6230) serial: Initializing seriale[0m

e[0;32mI (6231) asic_init: Detecting ASIC chips…e[0m

e[0;32mI (6234) asic: Initializing 1x BM1370e[0m

e[0;32mI (6244) common: Chip 0 detected: CORE_NUM: 0x00 ADDR: 0x00e[0m

e[0;32mI (7228) connect: IPv6 Address: FE80::A6CB:8FFF:FEE2:5A70e[0m

e[0;32mI (7244) frequency_transition: Ramping up frequency from 50 MHz to 525 MHze[0m

e[0;32mI (7246) pll: Frequency: 56.25 MHz (fb_divider: 189, refdiv: 2, postdiv1: 7, postdiv2: 6)e[0m

e[0;32mI (7252) bm1370: Setting Frequency to 56.25 MHz (56.25)e[0m

e[0;32mI (7357) pll: Frequency: 62.5 MHz (fb_divider: 175, refdiv: 2, postdiv1: 7, postdiv2: 5)e[0m

e[0;32mI (7358) bm1370: Setting Frequency to 62.5 MHz (62.5)e[0m

e[0;32mI (7461) pll: Frequency: 68.75 MHz (fb_divider: 165, refdiv: 2, postdiv1: 6, postdiv2: 5)e[0m

e[0;32mI (7462) bm1370: Setting Frequency to 68.75 MHz (68.75)e[0m

e[0;32mI (7565) pll: Frequency: 75 MHz (fb_divider: 168, refdiv: 2, postdiv1: 7, postdiv2: 4)e[0m

e[0;32mI (7566) bm1370: Setting Frequency to 75 MHz (75)e[0m

e[0;32mI (7668) pll: Frequency: 81.25 MHz (fb_divider: 182, refdiv: 2, postdiv1: 7, postdiv2: 4)e[0m

e[0;32mI (7678) bm1370: Setting Frequency to 81.25 MHz (81.25)e[0m

e[0;32mI (7729) websocket: Added WebSocket api client, fd: 44, slot: 0e[0m

e[0;32mI (7779) pll: Frequency: 87.5 MHz (fb_divider: 168, refdiv: 2, postdiv1: 6, postdiv2: 4)e[0m

e[0;32mI (7780) bm1370: Setting Frequency to 87.5 MHz (87.5)e[0m

e[0;32mI (7883) pll: Frequency: 93.75 MHz (fb_divider: 180, refdiv: 2, postdiv1: 6, postdiv2: 4)e[0m

e[0;32mI (7884) bm1370: Setting Frequency to 93.75 MHz (93.75)e[0m

e[0;32mI (7988) pll: Frequency: 100 MHz (fb_divider: 160, refdiv: 2, postdiv1: 5, postdiv2: 4)e[0m

e[0;32mI (7989) bm1370: Setting Frequency to 100 MHz (100)e[0m

e[0;32mI (8093) pll: Frequency: 106.25 MHz (fb_divider: 170, refdiv: 2, postdiv1: 5, postdiv2: 4)e[0m

e[0;32mI (8094) bm1370: Setting Frequency to 106.25 MHz (106.25)e[0m

e[0;32mI (8197) pll: Frequency: 112.5 MHz (fb_divider: 162, refdiv: 2, postdiv1: 6, postdiv2: 3)e[0m

e[0;32mI (8198) bm1370: Setting Frequency to 112.5 MHz (112.5)e[0m

e[0;32mI (8301) pll: Frequency: 118.75 MHz (fb_divider: 171, refdiv: 2, postdiv1: 6, postdiv2: 3)e[0m

e[0;32mI (8302) bm1370: Setting Frequency to 118.75 MHz (118.75)e[0m

e[0;32mI (8405) pll: Frequency: 125 MHz (fb_divider: 180, refdiv: 2, postdiv1: 6, postdiv2: 3)e[0m

e[0;32mI (8406) bm1370: Setting Frequency to 125 MHz (125)e[0m

e[0;32mI (8508) pll: Frequency: 131.25 MHz (fb_divider: 189, refdiv: 2, postdiv1: 6, postdiv2: 3)e[0m

e[0;32mI (8509) bm1370: Setting Frequency to 131.25 MHz (131.25)e[0m

e[0;32mI (8612) pll: Frequency: 137.5 MHz (fb_divider: 165, refdiv: 2, postdiv1: 5, postdiv2: 3)e[0m

e[0;32mI (8613) bm1370: Setting Frequency to 137.5 MHz (137.5)e[0m

e[0;32mI (8716) pll: Frequency: 143.75 MHz (fb_divider: 161, refdiv: 2, postdiv1: 7, postdiv2: 2)e[0m

e[0;32mI (8717) bm1370: Setting Frequency to 143.75 MHz (143.75)e[0m

e[0;32mI (8820) pll: Frequency: 150 MHz (fb_divider: 168, refdiv: 2, postdiv1: 7, postdiv2: 2)e[0m

e[0;32mI (8821) bm1370: Setting Frequency to 150 MHz (150)e[0m

e[0;32mI (8923) pll: Frequency: 156.25 MHz (fb_divider: 175, refdiv: 2, postdiv1: 7, postdiv2: 2)e[0m

e[0;32mI (8924) bm1370: Setting Frequency to 156.25 MHz (156.25)e[0m

e[0;32mI (9027) pll: Frequency: 162.5 MHz (fb_divider: 182, refdiv: 2, postdiv1: 7, postdiv2: 2)e[0m

e[0;32mI (9028) bm1370: Setting Frequency to 162.5 MHz (162.5)e[0m

e[0;32mI (9131) pll: Frequency: 168.75 MHz (fb_divider: 162, refdiv: 2, postdiv1: 6, postdiv2: 2)e[0m

e[0;32mI (9132) bm1370: Setting Frequency to 168.75 MHz (168.75)e[0m

e[0;32mI (9235) pll: Frequency: 175 MHz (fb_divider: 168, refdiv: 2, postdiv1: 6, postdiv2: 2)e[0m

e[0;32mI (9236) bm1370: Setting Frequency to 175 MHz (175)e[0m

e[0;32mI (9341) http_server: File sending completee[0m

e[0;32mI (9341) pll: Frequency: 181.25 MHz (fb_divider: 174, refdiv: 2, postdiv1: 6, postdiv2: 2)e[0m

e[0;32mI (9344) bm1370: Setting Frequency to 181.25 MHz (181.25)e[0m

e[0;32mI (9382) websocket: Removed WebSocket api client, fd: 44, slot: 0e[0m

e[0;32mI (9431) websocket: Added WebSocket api client, fd: 44, slot: 0e[0m

e[0;32mI (9450) pll: Frequency: 187.5 MHz (fb_divider: 180, refdiv: 2, postdiv1: 6, postdiv2: 2)e[0m

e[0;32mI (9451) bm1370: Setting Frequency to 187.5 MHz (187.5)e[0m

e[0;32mI (9554) pll: Frequency: 193.75 MHz (fb_divider: 186, refdiv: 2, postdiv1: 6, postdiv2: 2)e[0m

e[0;32mI (9555) bm1370: Setting Frequency to 193.75 MHz (193.75)e[0m

e[0;32mI (9658) pll: Frequency: 200 MHz (fb_divider: 160, refdiv: 2, postdiv1: 5, postdiv2: 2)e[0m

e[0;32mI (9659) bm1370: Setting Frequency to 200 MHz (200)e[0m

e[0;32mI (9761) pll: Frequency: 206.25 MHz (fb_divider: 165, refdiv: 2, postdiv1: 5, postdiv2: 2)e[0m

e[0;32mI (9762) bm1370: Setting Frequency to 206.25 MHz (206.25)e[0m

e[0;32mI (9865) pll: Frequency: 212.5 MHz (fb_divider: 170, refdiv: 2, postdiv1: 5, postdiv2: 2)e[0m

e[0;32mI (9866) bm1370: Setting Frequency to 212.5 MHz (212.5)e[0m

e[0;32mI (9969) pll: Frequency: 218.75 MHz (fb_divider: 175, refdiv: 2, postdiv1: 5, postdiv2: 2)e[0m

e[0;32mI (9970) bm1370: Setting Frequency to 218.75 MHz (218.75)e[0m

e[0;32mI (10073) pll: Frequency: 225 MHz (fb_divider: 180, refdiv: 2, postdiv1: 5, postdiv2: 2)e[0m

e[0;32mI (10074) bm1370: Setting Frequency to 225 MHz (225)e[0m

e[0;32mI (10177) pll: Frequency: 231.25 MHz (fb_divider: 185, refdiv: 2, postdiv1: 5, postdiv2: 2)e[0m

e[0;32mI (10178) bm1370: Setting Frequency to 231.25 MHz (231.25)e[0m

e[0;32mI (10282) pll: Frequency: 237.5 MHz (fb_divider: 190, refdiv: 2, postdiv1: 5, postdiv2: 2)e[0m

e[0;32mI (10283) bm1370: Setting Frequency to 237.5 MHz (237.5)e[0m

e[0;32mI (10386) pll: Frequency: 243.75 MHz (fb_divider: 195, refdiv: 2, postdiv1: 5, postdiv2: 2)e[0m

e[0;32mI (10387) bm1370: Setting Frequency to 243.75 MHz (243.75)e[0m

e[0;32mI (10490) pll: Frequency: 250 MHz (fb_divider: 160, refdiv: 2, postdiv1: 4, postdiv2: 2)e[0m

e[0;32mI (10491) bm1370: Setting Frequency to 250 MHz (250)e[0m

e[0;32mI (10594) pll: Frequency: 256.25 MHz (fb_divider: 164, refdiv: 2, postdiv1: 4, postdiv2: 2)e[0m

e[0;32mI (10595) bm1370: Setting Frequency to 256.25 MHz (256.25)e[0m

e[0;32mI (10698) pll: Frequency: 262.5 MHz (fb_divider: 168, refdiv: 2, postdiv1: 4, postdiv2: 2)e[0m

e[0;32mI (10699) bm1370: Setting Frequency to 262.5 MHz (262.5)e[0m

e[0;32mI (10802) pll: Frequency: 268.75 MHz (fb_divider: 172, refdiv: 2, postdiv1: 4, postdiv2: 2)e[0m

e[0;32mI (10803) bm1370: Setting Frequency to 268.75 MHz (268.75)e[0m

e[0;32mI (10906) pll: Frequency: 275 MHz (fb_divider: 176, refdiv: 2, postdiv1: 4, postdiv2: 2)e[0m

e[0;32mI (10907) bm1370: Setting Frequency to 275 MHz (275)e[0m

e[0;32mI (11010) pll: Frequency: 281.25 MHz (fb_divider: 180, refdiv: 2, postdiv1: 4, postdiv2: 2)e[0m

e[0;32mI (11011) bm1370: Setting Frequency to 281.25 MHz (281.25)e[0m

e[0;32mI (11114) pll: Frequency: 287.5 MHz (fb_divider: 161, refdiv: 2, postdiv1: 7, postdiv2: 1)e[0m

e[0;32mI (11115) bm1370: Setting Frequency to 287.5 MHz (287.5)e[0m

e[0;32mI (11221) pll: Frequency: 293.75 MHz (fb_divider: 188, refdiv: 2, postdiv1: 4, postdiv2: 2)e[0m

e[0;32mI (11224) bm1370: Setting Frequency to 293.75 MHz (293.75)e[0m

e[0;32mI (11327) pll: Frequency: 300 MHz (fb_divider: 168, refdiv: 2, postdiv1: 7, postdiv2: 1)e[0m

e[0;32mI (11328) bm1370: Setting Frequency to 300 MHz (300)e[0m

e[0;32mI (11431) pll: Frequency: 306.25 MHz (fb_divider: 196, refdiv: 2, postdiv1: 4, postdiv2: 2)e[0m

e[0;32mI (11432) bm1370: Setting Frequency to 306.25 MHz (306.25)e[0m

e[0;32mI (11536) pll: Frequency: 312.5 MHz (fb_divider: 175, refdiv: 2, postdiv1: 7, postdiv2: 1)e[0m

e[0;32mI (11537) bm1370: Setting Frequency to 312.5 MHz (312.5)e[0m

e[0;32mI (11641) pll: Frequency: 318.75 MHz (fb_divider: 204, refdiv: 2, postdiv1: 4, postdiv2: 2)e[0m

e[0;32mI (11642) bm1370: Setting Frequency to 318.75 MHz (318.75)e[0m

e[0;32mI (11745) pll: Frequency: 325 MHz (fb_divider: 182, refdiv: 2, postdiv1: 7, postdiv2: 1)e[0m

e[0;32mI (11746) bm1370: Setting Frequency to 325 MHz (325)e[0m

e[0;32mI (11849) pll: Frequency: 331.25 MHz (fb_divider: 212, refdiv: 2, postdiv1: 4, postdiv2: 2)e[0m

e[0;32mI (11850) bm1370: Setting Frequency to 331.25 MHz (331.25)e[0m

e[0;32mI (11953) pll: Frequency: 337.5 MHz (fb_divider: 162, refdiv: 2, postdiv1: 6, postdiv2: 1)e[0m

e[0;32mI (11954) bm1370: Setting Frequency to 337.5 MHz (337.5)e[0m

e[0;32mI (12057) pll: Frequency: 343.75 MHz (fb_divider: 165, refdiv: 2, postdiv1: 6, postdiv2: 1)e[0m

e[0;32mI (12058) bm1370: Setting Frequency to 343.75 MHz (343.75)e[0m

e[0;32mI (12161) pll: Frequency: 350 MHz (fb_divider: 168, refdiv: 2, postdiv1: 6, postdiv2: 1)e[0m

e[0;32mI (12162) bm1370: Setting Frequency to 350 MHz (350)e[0m

e[0;32mI (12265) pll: Frequency: 356.25 MHz (fb_divider: 171, refdiv: 2, postdiv1: 6, postdiv2: 1)e[0m

e[0;32mI (12266) bm1370: Setting Frequency to 356.25 MHz (356.25)e[0m

e[0;32mI (12369) pll: Frequency: 362.5 MHz (fb_divider: 174, refdiv: 2, postdiv1: 6, postdiv2: 1)e[0m

e[0;32mI (12370) bm1370: Setting Frequency to 362.5 MHz (362.5)e[0m

e[0;32mI (12474) pll: Frequency: 368.75 MHz (fb_divider: 177, refdiv: 2, postdiv1: 6, postdiv2: 1)e[0m

e[0;32mI (12475) bm1370: Setting Frequency to 368.75 MHz (368.75)e[0m

e[0;32mI (12578) pll: Frequency: 375 MHz (fb_divider: 180, refdiv: 2, postdiv1: 6, postdiv2: 1)e[0m

e[0;32mI (12579) bm1370: Setting Frequency to 375 MHz (375)e[0m

e[0;32mI (12682) pll: Frequency: 381.25 MHz (fb_divider: 183, refdiv: 2, postdiv1: 6, postdiv2: 1)e[0m

e[0;32mI (12683) bm1370: Setting Frequency to 381.25 MHz (381.25)e[0m

e[0;32mI (12786) pll: Frequency: 387.5 MHz (fb_divider: 186, refdiv: 2, postdiv1: 6, postdiv2: 1)e[0m

e[0;32mI (12787) bm1370: Setting Frequency to 387.5 MHz (387.5)e[0m

e[0;32mI (12890) pll: Frequency: 393.75 MHz (fb_divider: 189, refdiv: 2, postdiv1: 6, postdiv2: 1)e[0m

e[0;32mI (12891) bm1370: Setting Frequency to 393.75 MHz (393.75)e[0m

e[0;32mI (12994) pll: Frequency: 400 MHz (fb_divider: 160, refdiv: 2, postdiv1: 5, postdiv2: 1)e[0m

e[0;32mI (12995) bm1370: Setting Frequency to 400 MHz (400)e[0m

e[0;32mI (13098) pll: Frequency: 406.25 MHz (fb_divider: 195, refdiv: 2, postdiv1: 6, postdiv2: 1)e[0m

e[0;32mI (13099) bm1370: Setting Frequency to 406.25 MHz (406.25)e[0m

e[0;32mI (13202) pll: Frequency: 412.5 MHz (fb_divider: 165, refdiv: 2, postdiv1: 5, postdiv2: 1)e[0m

e[0;32mI (13203) bm1370: Setting Frequency to 412.5 MHz (412.5)e[0m

e[0;32mI (13306) pll: Frequency: 418.75 MHz (fb_divider: 201, refdiv: 2, postdiv1: 6, postdiv2: 1)e[0m

e[0;32mI (13307) bm1370: Setting Frequency to 418.75 MHz (418.75)e[0m

e[0;32mI (13410) pll: Frequency: 425 MHz (fb_divider: 170, refdiv: 2, postdiv1: 5, postdiv2: 1)e[0m

e[0;32mI (13411) bm1370: Setting Frequency to 425 MHz (425)e[0m

e[0;32mI (13514) pll: Frequency: 431.25 MHz (fb_divider: 207, refdiv: 2, postdiv1: 6, postdiv2: 1)e[0m

e[0;32mI (13515) bm1370: Setting Frequency to 431.25 MHz (431.25)e[0m

e[0;32mI (13618) pll: Frequency: 437.5 MHz (fb_divider: 175, refdiv: 2, postdiv1: 5, postdiv2: 1)e[0m

e[0;32mI (13619) bm1370: Setting Frequency to 437.5 MHz (437.5)e[0m

e[0;32mI (13722) pll: Frequency: 443.75 MHz (fb_divider: 213, refdiv: 2, postdiv1: 6, postdiv2: 1)e[0m

e[0;32mI (13723) bm1370: Setting Frequency to 443.75 MHz (443.75)e[0m

e[0;32mI (13826) pll: Frequency: 450 MHz (fb_divider: 180, refdiv: 2, postdiv1: 5, postdiv2: 1)e[0m

e[0;32mI (13827) bm1370: Setting Frequency to 450 MHz (450)e[0m

e[0;32mI (13930) pll: Frequency: 456.25 MHz (fb_divider: 219, refdiv: 2, postdiv1: 6, postdiv2: 1)e[0m

e[0;32mI (13931) bm1370: Setting Frequency to 456.25 MHz (456.25)e[0m

e[0;32mI (14035) pll: Frequency: 462.5 MHz (fb_divider: 185, refdiv: 2, postdiv1: 5, postdiv2: 1)e[0m

e[0;32mI (14036) bm1370: Setting Frequency to 462.5 MHz (462.5)e[0m

e[0;32mI (14139) pll: Frequency: 468.75 MHz (fb_divider: 225, refdiv: 2, postdiv1: 6, postdiv2: 1)e[0m

e[0;32mI (14140) bm1370: Setting Frequency to 468.75 MHz (468.75)e[0m

e[0;32mI (14243) pll: Frequency: 475 MHz (fb_divider: 190, refdiv: 2, postdiv1: 5, postdiv2: 1)e[0m

e[0;32mI (14244) bm1370: Setting Frequency to 475 MHz (475)e[0m

e[0;32mI (14347) pll: Frequency: 481.25 MHz (fb_divider: 231, refdiv: 2, postdiv1: 6, postdiv2: 1)e[0m

e[0;32mI (14348) bm1370: Setting Frequency to 481.25 MHz (481.25)e[0m

e[0;32mI (14452) pll: Frequency: 487.5 MHz (fb_divider: 195, refdiv: 2, postdiv1: 5, postdiv2: 1)e[0m

e[0;32mI (14453) bm1370: Setting Frequency to 487.5 MHz (487.5)e[0m

e[0;32mI (14562) pll: Frequency: 493.75 MHz (fb_divider: 237, refdiv: 2, postdiv1: 6, postdiv2: 1)e[0m

e[0;32mI (14563) bm1370: Setting Frequency to 493.75 MHz (493.75)e[0m

e[0;32mI (14667) pll: Frequency: 500 MHz (fb_divider: 160, refdiv: 2, postdiv1: 4, postdiv2: 1)e[0m

e[0;32mI (14668) bm1370: Setting Frequency to 500 MHz (500)e[0m

e[0;32mI (14771) pll: Frequency: 506.25 MHz (fb_divider: 162, refdiv: 2, postdiv1: 4, postdiv2: 1)e[0m

e[0;32mI (14772) bm1370: Setting Frequency to 506.25 MHz (506.25)e[0m

e[0;32mI (14883) pll: Frequency: 512.5 MHz (fb_divider: 164, refdiv: 2, postdiv1: 4, postdiv2: 1)e[0m

e[0;32mI (14885) bm1370: Setting Frequency to 512.5 MHz (512.5)e[0m

e[0;32mI (14991) pll: Frequency: 518.75 MHz (fb_divider: 166, refdiv: 2, postdiv1: 4, postdiv2: 1)e[0m

e[0;32mI (14992) bm1370: Setting Frequency to 518.75 MHz (518.75)e[0m

e[0;32mI (15097) pll: Frequency: 525 MHz (fb_divider: 168, refdiv: 2, postdiv1: 4, postdiv2: 1)e[0m

e[0;32mI (15098) bm1370: Setting Frequency to 525 MHz (525)e[0m

e[0;32mI (15203) frequency_transition: Successfully transitioned to 525 MHze[0m

e[0;32mI (15204) asic_init: Setting max baud rate and clearing bufferse[0m

e[0;32mI (15207) bm1370: Setting max baud of 1000000 ⁠​‌‌​​​‌​​‌‌​‌​​‌​‌‌‌​‌​​​‌‌​​​​‌​‌‌‌‌​​​​‌‌​​‌​‌⁠e[0m

e[0;32mI (15225) serial: Changing UART baud to 1000000e[0m

e[0;32mI (15235) asic_init: ASIC initialized successfully with 1 chip(s) (cold boot mode)e[0m

e[0;32mI (15238) create_jobs_task: ASIC Job Interval: 500 mse[0m

e[0;32mI (15244) create_jobs_task: ASIC Ready!e[0m

e[0;32mI (15249) statistics_task: Startinge[0m

e[0;32mI (15252) protocol_coordinator: Protocol coordinator started (primary: SV1, fallback: SV1, state: 1)e[0m

e[0;32mI (15253) stratum_v1_task: Opening connection to pool: public-pool.io:3333e[0m

e[0;32mI (15260) main_task: Returned from app_main()e[0m

e[0;32mI (15289) stratum_socket: Resolved [public-pool.io:3333](http://public-pool.io:3333) → 38.51.144.232e[0m

e[0;32mI (15289) stratum_v1_task: Connecting to: stratum+tcp://public-pool.io:3333 (38.51.144.232)e[0m

e[0;32mI (15295) stratum_api: TLS disabled, Using TCP transporte[0m

e[0;32mI (15301) stratum_v1_task: Transport initialized, connecting to [public-pool.io:3333](http://public-pool.io:3333) (38.51.144.232)e[0m

e[0;32mI (16651) stratum_v1_task: Resetting stratum uide[0m

e[0;32mI (16651) system: Clean Jobs: clearing queuee[0m

e[0;32mI (16652) stratum_api: tx: {“id”:1,“method”:“mining.configure”,“params”:[[“version-rolling”],{“version-rolling.mask”:“ffffffff”}]}e[0m

e[0;32mI (16664) stratum_api: tx: {“id”:2,“method”:“mining.subscribe”,“params”:[“bitaxe/BM1370/v2.14.2”]}e[0m

e[0;32mI (16674) stratum_api: tx: {“id”:3,“method”:“mining.authorize”,“params”:[“bc1qnp980s5fpp8l94p5cvttmtdqy8rvrq74qly2yrfmzkdsntqzlc5qkc4rkq.bitaxe”,“x”]}e[0m

e[0;32mI (16979) stratum_api: rx: {“id”:1,“error”:null,“result”:{“version-rolling”:true,“version-rolling.mask”:“1fffe000”}}e[0m

e[0;32mI (16979) stratum_v1_task: Set version mask: 1fffe000e[0m

e[0;32mI (16988) stratum_api: rx: {“id”:2,“error”:null,“result”:[[[“mining.notify”,“cea75609”]],“cea75609”,8]}e[0m

e[0;32mI (16995) stratum_v1_task: Set extranonce: cea75609, extranonce_2_len: 8e[0m

e[0;32mI (17004) stratum_api: rx: {“id”:3,“error”:null,“result”:true}e[0m

e[0;32mI (17009) stratum_v1_task: setup message acceptede[0m

e[0;32mI (17014) stratum_api: tx: {“id”:4,“method”:“mining.suggest_difficulty”,“params”:[1000]}e[0m

e[0;32mI (17024) stratum_api: rx: {“id”:null,“method”:“mining.set_difficulty”,“params”:[100000]}e[0m

e[0;32mI (17032) stratum_v1_task: Set pool difficulty: 100000.00e[0m

e[0;32mI (17040) stratum_api: rx: {“id”:null,“method”:“mining.notify”,“params”:[“e5ba98”,“4640685c685dc562cb0fc405dbaca0b7c9b91b6c00010c7f0000000000000000”,“02000000010000000000000000000000000000000000000000000000000000000000000000ffffffff1b0348a70e5075626c69632d506f6f6c”,“ffffffff028542d31200000000220020984a77c289084ff2d434c316bdada021c6c183d507c8a20d3b159b09ac02fe280000000000000000266a24aa21a9ed067dad2cba0dd42d710b6b0406985139d0cbead9b2f4c74773e74df53ea7051600000000”,[“5611a88413712b14a53c1c22a909abdb6d0c4ed83ce1c0f214459255a994fb5f”,“88286925c2d34411fb6847d9dec407bb1a5dc3b23e57ce934dbe5e2c0024a970”,“e867ed2fc8e05a0f524e0cdf8029104e486d502eb6e3500c8a5ffb45c7a4594e”,“5d24c8b318a730f60f69ec8cb394b3f39e9cc902d0b2f106d94c40514cc4f0b1”,“135abb85b48711c4785a381a80e76ce9cf1e645edd627c6fb7a9898681a2c999”,“a5eea1b0e428893ec5c8d153aa36a887c9a5ad69a1a7ddcc3cfd5b68254bcd3c”,“1dd5736e261de37237ebab6eb64edac51789dc3d4abfa74b6efc57c8da7699de”,“ad1056a9c2c20210f8abde7887e4cc04d9c4740d0b6a2ba0bae26942b7ff6abf”,“1a19b3dc93033447e81a694bd755031a1bb264e69e2c16dfa70c082c3768badd”,“f60c100b35449b1413531fc186d836a435f946131e2c69b86c04ef7ca2f9a531”,“65694b87361c309d751ce4d76cfa0f1c2935d84f6571207b773246026d802067”,“15bc20c516e597b89fc69b192359a26b1086a8ff55341823cbabe974065284b7”],“20000000”,“17023ad4”,“6a6beefe”,false]}e[0m

e[0;32mI (17154) system: Syncing clocke[0m

e[0;32mI (17158) stratum_v1_task: Block height 960328e[0m

e[0;32mI (17162) stratum_v1_task: Scriptsig: Public-Poole[0m

e[0;32mI (17167) stratum_v1_task: Coinbase outputs: 2, total value: 315835013 satse[0m

e[0;32mI (17175) stratum_v1_task:   Output 0: bc1qnp980s5fpp8l94p5cvttmtdqy8rvrq74qly2yrfmzkdsntqzlc5qkc4rkq (315835013 sat) (Your payout address)e[0m

e[0;32mI (17188) stratum_v1_task:   Output 1: OP_RETURN: .!..}.,…-q.k…Q9…Gs.M.>…e[0m

e[0;32mI (17249) create_jobs_task: New Work Dequeued e5ba98e[0m

e[0;32mI (17249) create_jobs_task: New pool difficulty 100000.00e[0m

e[0;32mI (17250) create_jobs_task: Set chip version rolls 65535e[0m

e[0;32mI (17356) stratum_api: rx: {“id”:null,“method”:“mining.set_difficulty”,“params”:[1000]}e[0m

e[0;32mI (17357) stratum_v1_task: Set pool difficulty: 1000.00e[0m

e[0;32mI (18722) stratum_api: rx: {“id”:null,“method”:“mining.notify”,“params”:[“e5c67d”,“4640685c685dc562cb0fc405dbaca0b7c9b91b6c00010c7f0000000000000000”,“02000000010000000000000000000000000000000000000000000000000000000000000000ffffffff1b0348a70e5075626c69632d506f6f6c”,“ffffffff02b71cd41200000000220020984a77c289084ff2d434c316bdada021c6c183d507c8a20d3b159b09ac02fe280000000000000000266a24aa21a9ed99d65e1b0d1c014a48601bf58bb9722f42cdd35c8f46287d59758677a9ffcb3700000000”,[“5611a88413712b14a53c1c22a909abdb6d0c4ed83ce1c0f214459255a994fb5f”,“88286925c2d34411fb6847d9dec407bb1a5dc3b23e57ce934dbe5e2c0024a970”,“e867ed2fc8e05a0f524e0cdf8029104e486d502eb6e3500c8a5ffb45c7a4594e”,“5d24c8b318a730f60f69ec8cb394b3f39e9cc902d0b2f106d94c40514cc4f0b1”,“135abb85b48711c4785a381a80e76ce9cf1e645edd627c6fb7a9898681a2c999”,“724dd9d4fba25d73df65f5562fff8d7180f1ee7d7ca3e0a8fc003471ae02c30a”,“8752c9b3d659e43f928fef698c74e97cbe9a5185b9113c9f04678b7ef446791d”,“cae5b33fcbe573aba636835d0f69bfbee62a1b7302541feaded3a53b95c8c8b4”,“012979c0696d5c7740c3368e381c2439358ba9cfa71a640b08cba9f7f28aae2b”,“c2506969995f6898e81878347aecbe8e3242a40e728191a727d8d9ffa8a33bfb”,“3e91f821a9b4ef4dbbd7edb98dbf9b0eb5f535721ad8362130e49c1a72124454”,“49931c04fbd128347c4be77f901d7ccdbfa0773ae5e3814af37e56a8b48011d3”],“20000000”,“17023ad4”,“6a6bef36”,false]}e[0m

e[0;32mI (18828) create_jobs_task: New Work Dequeued e5c67de[0m

e[0;32mI (18829) stratum_v1_task: Coinbase outputs: 2, total value: 315890871 satse[0m

e[0;32mI (18833) create_jobs_task: New pool difficulty 1000.00e[0m

e[0;32mI (18841) stratum_v1_task:   Output 0: bc1qnp980s5fpp8l94p5cvttmtdqy8rvrq74qly2yrfmzkdsntqzlc5qkc4rkq (315890871 sat) (Your payout address)e[0m

e[0;32mI (18859) stratum_v1_task:   Output 1: OP_RETURN: .!..^…JH`…r/B…F(}Yu.w…7e[0m

e[0;32mI (20116) http_server: File sending completee[0m

e[0;32mI (20136) websocket: Removed WebSocket api client, fd: 44, slot: 0e[0m

e[0;32mI (20215) websocket: Added WebSocket api client, fd: 44, slot: 0e[0m

-------------------------

luckyminer0 | 2026-09-07 03:35:57 UTC | #5

Man, that really sucks. That crazy 400 TH/s bug is usually a physical hardware failure (either a bad solder joint on the BM1370 chip from the factory or a voltage regulator issue). Sometimes completely wiping and re-flashing the firmware to the absolute latest version helps, but if that doesn’t fix it, it’s definitely a bad ASIC.

If you guys do get it fixed or get a replacement board, I highly recommend testing it out on the **Tarcoin (TAR)** pool first instead of standard Bitcoin pools.

Standard BTC difficulty is so high right now that it takes a long time to know if a Bitaxe is actually finding shares or if it’s glitching out again. On Tarcoin, the difficulty is super low, so your Bitaxe will find shares instantly. It’s the absolute best way to stress-test your miner and verify the ASIC chip is working correctly.

Good luck getting the boards fixed!
