# bitaxeorg/bitaxeGamma issue #52: Bitaxe gamma 601 errors

> Source: https://github.com/bitaxeorg/bitaxeGamma/issues/52
> Collected: 2026-10-07
> Published: 2025-11-25

- Repository: bitaxeorg/bitaxeGamma
- Type: issue
- Number: 52
- State: closed
- Author: AngelSerra
- Opened: 2025-11-25
- Closed: 2025-11-25
- Labels: none

## Description

It was working perfectly, then one day it suddenly lost its IP address and started giving errors. It was updated from the official AXE website. Is there any way to recover it, or is something broken?

[bitaxe-logs-2025-11-25T10-21-26-761Z.txt](https://github.com/user-attachments/files/23744635/bitaxe-logs-2025-11-25T10-21-26-761Z.txt)

Serial logging started...

I (333) esp_image: segment 4: paddr=00139148 vaddr=403750b4 size[0;32mI (12158) dns_server: IP address: 1.4.168.192
[0m
[0;32mI (12159) dns_server: Received 51 bytes from 192.168.4.2 | DNS reply with len: 67[0m
[0;32mI (12162) dns_server: Waiting for data[0m
[0;32mI (12166) dns_server: IP address: 1.4.168.192
[0m
[0;32mI (12171) dns_server: Received 74 bytes from 192.168.4.2 | DNS reply with len: 90[0m
[0;32mI (12180) dns_server: Waiting for data[0m
[0;32mI (12184) dns_server: IP address: 1.4.168.192
[0m
[0;32mI (12188) dns_server: Received 51 bytes from 192.168.4.2 | DNS reply with len: 67[0m
[0;32mI (12198) dns_server: Waiting for data[0m
[0;32mI (12202) dns_server: IP address: 1.4.168.192
[0m
[0;32mI (12206) dns_server: Received 34 bytes from 192.168.4.2 | DNS reply with len: 50[0m
[0;32mI (12215) dns_server: Waiting for data[0m
[0;32mI (12227) dns_server: Received 28 bytes from 192.168.4.2 | DNS reply with len: 44[0m
[0;32mI (12228) dns_server: Waiting for data[0m
[0;32mI (12234) dns_server: Received 28 bytes from 192.168.4.2 | DNS reply with len: 44[0m
[0;32mI (12241) dns_server: Waiting for data[0m
[0;32mI (12244) dns_server: Received 28 bytes from 192.168.4.2 | DNS reply with len: 44[0m
[0;32mI (12253) dns_server: Waiting for data[0m
[0;32mI (12257) dns_server: Received 28 bytes from 192.168.4.2 | DNS reply with len: 44[0m
[0;32mI (12266) dns_server: Waiting for data[0m
[0;32mI (12270) dns_server: Received 43 bytes from 192.168.4.2 | DNS reply with len: 59[0m
[0;32mI (12278) dns_server: Waiting for data[0m
[0;32mI (12282) dns_server: IP address: 1.4.168.192
[0m
[0;32mI (12287) dns_server: Received 51 bytes from 192.168.4.2 | DNS reply with len: 67[0m
[0;32mI (12296) dns_server: Waiting for data[0m
[0;32mI (12300) dns_server: Received 28 bytes from 192.168.4.2 | DNS reply with len: 44[0m
[0;32mI (12309) dns_server: Waiting for data[0m
[0;32mI (12664) BAP_UART: Sent: $BAP,CMD,mode,ap_mode*7B
[0m
[0;32mI (13334) dns_server: IP address: 1.4.168.192
[0m
[0;32mI (13334) dns_server: Received 42 bytes from 192.168.4.2 | DNS reply with len: 58[0m
[0;32mI (13337) dns_server: Waiting for data[0m
[0;33mW (13891) power_management: AP mode with invalid temperature reading: -1.0 °C - Setting fan to 70%[0m
[0;32mI (14902) dns_server: IP address: 1.4.168.192
[0m
[0;32mI (14903) dns_server: Received 40 bytes from 192.168.4.2 | DNS reply with len: 56[0m
[0;32mI (14905) dns_server: Waiting for data[0m
[0;32mI (14997) dns_server: Received 28 bytes from 192.168.4.2 | DNS reply with len: 0[0m
[0;31mE (14997) dns_server: Failed to prepare a DNS reply[0m
[0;32mI (15000) dns_server: Waiting for data[0m
[0;32mI (15004) dns_server: Received 36 bytes from 192.168.4.2 | DNS reply with len: 36[0m
[0;32mI (15013) dns_server: Waiting for data[0m
[0;32mI (15017) dns_server: IP address: 1.4.168.192
[0m
[0;32mI (15022) dns_server: Received 29 bytes from 192.168.4.2 | DNS reply with len: 45[0m
[0;32mI (15031) dns_server: Waiting for data[0m
[0;33mW (15696) power_management: AP mode with invalid temperature reading: -1.0 °C - Setting fan to 70%[0m
[0;32mI (16961) dns_server: IP address: 1.4.168.192
[0m
[0;32mI (16962) dns_server: Received 32 bytes from 192.168.4.2 | DNS reply with len: 48[0m
[0;32mI (16965) dns_server: Waiting for data[0m
[0;33mW (17500) power_management: AP mode with invalid temperature reading: -1.0 °C - Setting fan to 70%[0m
[0;32mI (17664) BAP_UART: Sent: $BAP,CMD,mode,ap_mode*7B
[0m
[0;33mW (19313) power_management: AP mode with invalid temperature reading: -1.0 °C - Setting fan to 70%[0m
[0;32mI (19945) dns_server: IP address: 1.4.168.192
[0m
[0;32mI (19945) dns_server: Received 37 bytes from 192.168.4.2 | DNS reply with len: 53[0m
[0;32mI (19949) dns_server: Waiting for data[0m
[0;32mI (20471) dns_server: IP address: 1.4.168.192
[0m
[0;32mI (20471) dns_server: Received 40 bytes from 192.168.4.2 | DNS reply with len: 56[0m
[0;32mI (20475) dns_server: Waiting for data[0m
[0;32mI (20899) dns_server: IP address: 1.4.168.192
[0m
[0;32mI (20899) dns_server: Received 39 bytes from 192.168.4.2 | DNS reply with len: 55[0m
[0;32mI (20902) dns_server: Waiting for data[0m
[0;33mW (21122) power_management: AP mode with invalid temperature reading: -1.0 °C - Setting fan to 70%[0m
[0;32mI (22664) BAP_UART: Sent: $BAP,CMD,mode,ap_mode*7B
[0m
[0;33mW (22928) power_management: AP mode with invalid temperature reading: -1.0 °C - Setting fan to 70%[0m
[0;33mW (24733) power_management: AP mode with invalid temperature reading: -1.0 °C - Setting fan to 70%[0m
[0;33mW (26539) power_management: AP mode with invalid temperature reading: -1.0 °C - Setting fan to 70%[0m
[0;32mI (27664) BAP_UART: Sent: $BAP,CMD,mode,ap_mode*7B
[0m
[0;33mW (28351) power_management: AP mode with invalid temperature reading: -1.0 °C - Setting fan to 70%[0m
[0;33mW (30155) power_management: AP mode with invalid temperature reading: -1.0 °C - Setting fan to 70%[0m
[0;33mW (31960) power_management: AP mode with invalid temperature reading: -1.0 °C - Setting fan to 70%[0m
[0;32mI (32665) BAP_UART: Sent: $BAP,CMD,mode,ap_mode*7B
[0m
[0;33mW (33765) power_management: AP mode with invalid temperature reading: -1.0 °C - Setting fan to 70%[0m
[0;32mI (34256) connect: Timeout waiting for IP address. Disconnecting...[0m
I (34256) wifi:state: run -> init (0x0)
I (34258) wifi:pm stop, total sleep time: 0 us / 30027358 us

I (34261) wifi:<ba-del>idx:0, tid:0
I (34264) wifi:new:<6,0>, old:<6,0>, ap:<6,2>, sta:<6,0>, prof:1, snd_ch_cfg:0x0
[0;32mI (34272) connect: Could not connect to 'MOVISTAR_FF45' [rssi -59]: reason 8[0m
[0;32mI (34279) connect: Client(s) connected to AP, not retrying...[0m
[0;33mW (35569) power_management: AP mode with invalid temperature reading: -1.0 °C - Setting fan to 70%[0m
[0;33mW (37381) power_management: AP mode with invalid temperature reading: -1.0 °C - Setting fan to 70%[0m
[0;32mI (37666) BAP_UART: Sent: $BAP,CMD,mode,ap_mode*7B
[0m
[0;32mI (39029) dns_server: IP address: 1.4.168.192
[0m
[0;32mI (39029) dns_server: Received 39 bytes from 192.168.4.2 | DNS reply with len: 55[0m
[0;32mI (39032) dns_server: Waiting for data[0m
[0;33mW (39185) power_management: AP mode with invalid temperature reading: -1.0 °C - Setting fan to 70%[0m
[0;33mW (40989) power_management: AP mode with invalid temperature reading: -1.0 °C - Setting fan to 70%[0m
[0;32mI (42666) BAP_UART: Sent: $BAP,CMD,mode,ap_mode*7B
[0m
[0;33mW (42793) power_management: AP mode with invalid temperature reading: -1.0 °C - Setting fan to 70%[0m
[0;33mW (44597) power_management: AP mode with invalid temperature reading: -1.0 °C - Setting fan to 70%[0m
[0;33mW (46412) power_management: AP mode with invalid temperature reading: -1.0 °C - Setting fan to 70%[0m
[0;32mI (47667) BAP_UART: Sent: $BAP,CMD,mode,ap_mode*7B
[0m
[0;33mW (48216) power_management: AP mode with invalid temperature reading: -1.0 °C - Setting fan to 70%[0m
[0;33mW (50032) power_management: AP mode with invalid temperature reading: -1.0 °C - Setting fan to 70%[0m
[0;33mW (51836) power_management: AP mode with invalid temperature reading: -1.0 °C - Setting fan to 70%[0m
[0;32mI (52667) BAP_UART: Sent: $BAP,CMD,mode,ap_mode*7B
[0m
[0;33mW (53641) power_management: AP mode with invalid temperature reading: -1.0 °C - Setting fan to 70%[0m
[0;33mW (55445) power_management: AP mode with invalid temperature reading: -1.0 °C - Setting fan to 70%[0m
[0;32mI (55818) dns_server: IP address: 1.4.168.192
[0m
[0;32mI (55819) dns_server: Received 45 bytes from 192.168.4.2 | DNS reply with len: 61[0m
[0;32mI (55822) dns_server: Waiting for data[0m
[0;33mW (57259) power_management: AP mode with invalid temperature reading: -1.0 °C - Setting fan to 70%[0m
[0;32mI (57667) BAP_UART: Sent: $BAP,CMD,mode,ap_mode*7B
[0m
[0;33mW (59065) power_management: AP mode with invalid temperature reading: -1.0 °C - Setting fan to 70%[0m
[0;33mW (60869) power_management: AP mode with invalid temperature reading: -1.0 °C - Setting fan to 70%[0m
[0;32mI (62667) BAP_UART: Sent: $BAP,CMD,mode,ap_mode*7B
[0m
[0;33mW (62673) power_management: AP mode with invalid temperature reading: -1.0 °C - Setting fan to 70%[0m
[0;33mW (64477) power_management: AP mode with invalid temperature reading: -1.0 °C - Setting fan to 70%[0m
[0;33mW (66291) power_management: AP mode with invalid temperature reading: -1.0 °C - Setting fan to 70%[0m
[0;32mI (67668) BAP_UART: Sent: $BAP,CMD,mode,ap_mode*7B
[0m
[0;33mW (68095) power_management: AP mode with invalid temperature reading: -1.0 °C - Setting fan to 70%[0m
[0;33mW (69912) power_management: AP mode with invalid temperature reading: -1.0 °C - Setting fan to 70%[0m
[0;33mW (71716) power_management: AP mode with invalid temperature reading: -1.0 °C - Setting fan to 70%[0m
[0;32mI (72669) BAP_UART: Sent: $BAP,CMD,mode,ap_mode*7B
[0m
[0;33mW (73521) power_management: AP mode with invalid temperature reading: -1.0 °C - Setting fan to 70%[0m
[0;33mW (75325) power_management: AP mode with invalid temperature reading: -1.0 °C - Setting fan to 70%[0m
[0;33mW (77128) power_management: AP mode with invalid temperature reading: -1.0 °C - Setting fan to 70%[0m
[0;32mI (77669) BAP_UART: Sent: $BAP,CMD,mode,ap_mode*7B
[0m
[0;33mW (78945) power_management: AP mode with invalid temperature reading: -1.0 °C - Setting fan to 70%[0m
[0;33mW (80749) power_management: AP mode with invalid temperature reading: -1.0 °C - Setting fan to 70%[0m
[0;33mW (82564) power_management: AP mode with invalid temperature reading: -1.0 °C - Setting fan to 70%[0m
[0;32mI (82669) BAP_UART: Sent: $BAP,CMD,mode,ap_mode*7B
[0m
[0;33mW (84370) power_management: AP mode with invalid temperature reading: -1.0 °C - Setting fan to 70%[0m
[0;33mW (86174) power_management: AP mode with invalid temperature reading: -1.0 °C - Setting fan to 70%[0m
[0;32mI (87669) BAP_UART: Sent: $BAP,CMD,mode,ap_mode*7B
[0m
[0;33mW (87977) power_management: AP mode with invalid temperature reading: -1.0 °C - Setting fan to 70%[0m
[0;33mW (89793) power_management: AP mode with invalid temperature reading: -1.0 °C - Setting fan to 70%[0m
[0;33mW (91597) power_management: AP mode with invalid temperature reading: -1.0 °C - Setting fan to 70%[0m
[0;32mI (92669) BAP_UART: Sent: $BAP,CMD,mode,ap_mode*7B
[0m
[0;33mW (93401) power_management: AP mode with invalid temperature reading: -1.0 °C - Setting fan to 70%[0m
[0;33mW (95205) power_management: AP mode with invalid temperature reading: -1.0 °C - Setting fan to 70%[0m
[0;33mW (97020) power_management: AP mode with invalid temperature reading: -1.0 °C - Setting fan to 70%[0m
[0;32mI (97669) BAP_UART: Sent: $BAP,CMD,mode,ap_mode*7B
[0m
[0;33mW (98825) power_management: AP mode with invalid temperature reading: -1.0 °C - Setting fan to 70%[0m
[0;33mW (100629) power_management: AP mode with invalid temperature reading: -1.0 °C - Setting fan to 70%[0m
[0;33mW (102432) power_management: AP mode with invalid temperature reading: -1.0 °C - Setting fan to 70%[0m
[0;32mI (102670) BAP_UART: Sent: $BAP,CMD,mode,ap_mode*7B
[0m
[0;33mW (104250) power_management: AP mode with invalid temperature reading: -1.0 °C - Setting fan to 70%[0m
[0;33mW (106053) power_management: AP mode with invalid temperature reading: -1.0 °C - Setting fan to 70%[0m
[0;32mI (107671) BAP_UART: Sent: $BAP,CMD,mode,ap_mode*7B
[0m
[0;33mW (107857) power_management: AP mode with invalid temperature reading: -1.0 °C - Setting fan to 70%[0m
[0;33mW (109661) power_management: AP mode with invalid temperature reading: -1.0 °C - Setting fan to 70%[0m
[0;33mW (111476) power_management: AP mode with invalid temperature reading: -1.0 °C - Setting fan to 70%[0m
[0;32mI (112671) BAP_UART: Sent: $BAP,CMD,mode,ap_mode*7B
[0m
[0;33mW (113280) power_management: AP mode with invalid temperature reading: -1.0 °C - Setting fan to 70%[0m
[0;33mW (115085) power_management: AP mode with invalid temperature reading: -1.0 °C - Setting fan to 70%[0m
[0;33mW (116900) power_management: AP mode with invalid temperature reading: -1.0 °C - Setting fan to 70%[0m
[0;32mI (117671) BAP_UART: Sent: $BAP,CMD,mode,ap_mode*7B
[0m
[0;33mW (118704) power_management: AP mode with invalid temperature reading: -1.0 °C - Setting fan to 70%[0m
[0;33mW (120508) power_management: AP mode with invalid temperature reading: -1.0 °C - Setting fan to 70%[0m
[0;33mW (122311) power_management: AP mode with invalid temperature reading: -1.0 °C - Setting fan to 70%[0m
[0;32mI (122671) BAP_UART: Sent: $BAP,CMD,mode,ap_mode*7B
[0m
[0;33mW (124128) power_management: AP mode with invalid temperature reading: -1.0 °C - Setting fan to 70%[0m
[0;33mW (125932) power_management: AP mode with invalid temperature reading: -1.0 °C - Setting fan to 70%[0m
[0;32mI (127671) BAP_UART: Sent: $BAP,CMD,mode,ap_mode*7B
[0m
[0;33mW (127747) power_management: AP mode with invalid temperature reading: -1.0 °C - Setting fan to 70%[0m
[0;33mW (129553) power_management: AP mode with invalid temperature reading: -1.0 °C - Setting fan to 70%[0m
[0;33mW (131357) power_management: AP mode with invalid temperature reading: -1.0 °C - Setting fan to 70%[0m
[0;32mI (132671) BAP_UART: Sent: $BAP,CMD,mode,ap_mode*7B
[0m
[0;33mW (133161) power_management: AP mode with invalid temperature reading: -1.0 °C - Setting fan to 70%[0m
[0;33mW (134978) power_management: AP mode with invalid temperature reading: -1.0 °C - Setting fan to 70%[0m
[0;33mW (136782) power_management: AP mode with invalid temperature reading: -1.0 °C - Setting fan to 70%[0m
[0;32mI (137671) BAP_UART: Sent: $BAP,CMD,mode,ap_mode*7B
[0m
[0;33mW (138586) power_management: AP mode with invalid temperature reading: -1.0 °C - Setting fan to 70%[0m
[0;33mW (140390) power_management: AP mode with invalid temperature reading: -1.0 °C - Setting fan to 70%[0m
[0;33mW (142205) power_management: AP mode with invalid temperature reading: -1.0 °C - Setting fan to 70%[0m
[0;32mI (142672) BAP_UART: Sent: $BAP,CMD,mode,ap_mode*7B
[0m
[0;33mW (144011) power_management: AP mode with invalid temperature reading: -1.0 °C - Setting fan to 70%[0m
[0;33mW (145815) power_management: AP mode with invalid temperature reading: -1.0 °C - Setting fan to 70%[0m
[0;33mW (147629) power_management: AP mode with invalid temperature reading: -1.0 °C - Setting fan to 70%[0m
[0;32mI (147673) BAP_UART: Sent: $BAP,CMD,mode,ap_mode*7B
[0m
[0;33mW (149435) power_management: AP mode with invalid temperature reading: -1.0 °C - Setting fan to 70%[0m
[0;33mW (151239) power_management: AP mode with invalid temperature reading: -1.0 °C - Setting fan to 70%[0m
[0;32mI (152674) BAP_UART: Sent: $BAP,CMD,mode,ap_mode*7B
[0m
[0;33mW (153042) power_management: AP mode with invalid temperature reading: -1.0 °C - Setting fan to 70%[0m
[0;33mW (154859) power_management: AP mode with invalid temperature reading: -1.0 °C - Setting fan to 70%[0m
[0;33mW (156663) power_management: AP mode with invalid temperature reading: -1.0 °C - Setting fan to 70%[0m
[0;32mI (157674) BAP_UART: Sent: $BAP,CMD,mode,ap_mode*7B
[0m
[0;33mW (158467) power_management: AP mode with invalid temperature reading: -1.0 °C - Setting fan to 70%[0m
[0;33mW (160284) power_management: AP mode with invalid temperature reading: -1.0 °C - Setting fan to 70%[0m
[0;33mW (162088) power_management: AP mode with invalid temperature reading: -1.0 °C - Setting fan to 70%[0m
[0;32mI (162675) BAP_UART: Sent: $BAP,CMD,mode,ap_mode*7B
[0m
[0;33mW (163892) power_management: AP mode with invalid temperature reading: -1.0 °C - Setting fan to 70%[0m
[0;33mW (165696) power_management: AP mode with invalid temperature reading: -1.0 °C - Setting fan to 70%[0m
[0;33mW (167511) power_management: AP mode with invalid temperature reading: -1.0 °C - Setting fan to 70%[0m
[0;32mI (167675) BAP_UART: Sent: $BAP,CMD,mode,ap_mode*7B
[0m
[0;33mW (169315) power_management: AP mode with invalid temperature reading: -1.0 °C - Setting fan to 70%[0m
[0;33mW (171119) power_management: AP mode with invalid temperature reading: -1.0 °C - Setting fan to 70%[0m
[0;32mI (172675) BAP_UART: Sent: $BAP,CMD,mode,ap_mode*7B
[0m
[0;33mW (172922) power_management: AP mode with invalid temperature reading: -1.0 °C - Setting fan to 70%[0m
[0;33mW (174739) power_management: AP mode with invalid temperature reading: -1.0 °C - Setting fan to 70%[0m
[0;33mW (176543) power_management: AP mode with invalid temperature reading: -1.0 °C - Setting fan to 70%[0m
[0;32mI (177676) BAP_UART: Sent: $BAP,CMD,mode,ap_mode*7B
[0m
[0;33mW (178347) power_management: AP mode with invalid temperature reading: -1.0 °C - Setting fan to 70%[0m
[0;33mW (180151) power_management: AP mode with invalid temperature reading: -1.0 °C - Setting fan to 70%[0m
[0;33mW (181966) power_management: AP mode with invalid temperature reading: -1.0 °C - Setting fan to 70%[0m
[0;32mI (182677) BAP_UART: Sent: $BAP,CMD,mode,ap_mode*7B
[0m
[0;33mW (183770) power_management: AP mode with invalid temperature reading: -1.0 °C - Setting fan to 70%[0m
[0;33mW (185574) power_management: AP mode with invalid temperature reading: -1.0 °C - Setting fan to 70%[0m
[0;33mW (187377) power_management: AP mode with invalid temperature reading: -1.0 °C - Setting fan to 70%[0m
[0;32mI (187678) BAP_UART: Sent: $BAP,CMD,mode,ap_mode*7B
[0m
[0;33mW (189194) power_management: AP mode with invalid temperature reading: -1.0 °C - Setting fan to 70%[0m
[0;33mW (190998) power_management: AP mode with invalid temperature reading: -1.0 °C - Setting fan to 70%[0m
[0;32mI (192678) BAP_UART: Sent: $BAP,CMD,mode,ap_mode*7B
[0m
[0;33mW (192802) power_management: AP mode with invalid temperature reading: -1.0 °C - Setting fan to 70%[0m
[0;33mW (194606) power_management: AP mode with invalid temperature reading: -1.0 °C - Setting fan to 70%[0m
[0;33mW (196421) power_management: AP mode with invalid temperature reading: -1.0 °C - Setting fan to 70%[0m
[0;32mI (197678) BAP_UART: Sent: $BAP,CMD,mode,ap_mode*7B
[0m
[0;33mW (198225) power_management: AP mode with invalid temperature reading: -1.0 °C - Setting fan to 70%[0m
[0;33mW (200029) power_management: AP mode with invalid temperature reading: -1.0 °C - Setting fan to 70%[0m
[0;33mW (201845) power_management: AP mode with invalid temperature reading: -1.0 °C - Setting fan to 70%[0m
[0;32mI (202678) BAP_UART: Sent: $BAP,CMD,mode,ap_mode*7B
[0m
[0;33mW (203650) power_management: AP mode with invalid temperature reading: -1.0 °C - Setting fan to 70%[0m
[0;33mW (205454) power_management: AP mode with invalid temperature reading: -1.0 °C - Setting fan to 70%[0m
[0;33mW (207258) power_management: AP mode with invalid temperature reading: -1.0 °C - Setting fan to 70%[0m
[0;32mI (207678) BAP_UART: Sent: $BAP,CMD,mode,ap_mode*7B
[0m
[0;33mW (209074) power_management: AP mode with invalid temperature reading: -1.0 °C - Setting fan to 70%[0m
[0;33mW (210878) power_management: AP mode with invalid temperature reading: -1.0 °C - Setting fan to 70%[0m
[0;32mI (212680) BAP_UART: Sent: $BAP,CMD,mode,ap_mode*7B
[0m
[0;33mW (212694) power_management: AP mode with invalid temperature reading: -1.0 °C - Setting fan to 70%[0m
[0;33mW (214498) power_management: AP mode with invalid temperature reading: -1.0 °C - Setting fan to 70%[0m
[0;33mW (216303) power_management: AP mode with invalid temperature reading: -1.0 °C - Setting fan to 70%[0m
[0;32mI (217680) BAP_UART: Sent: $BAP,CMD,mode,ap_mode*7B
[0m
[0;33mW (218106) power_management: AP mode with invalid temperature reading: -1.0 °C - Setting fan to 70%[0m
[0;33mW (219910) power_management: AP mode with invalid temperature reading: -1.0 °C - Setting fan to 70%[0m


## Comments

### skot on 2025-11-25

It seems like it's just not joining your wifi. What does the screen say?

This issues section is for Bitaxe hardware, so I'm going to close this. If you're still having trouble, you can reach out to the seller for support, or try the OSMU Discord; https://discord.gg/osmu
