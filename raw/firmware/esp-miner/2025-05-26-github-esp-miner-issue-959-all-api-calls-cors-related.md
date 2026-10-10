# bitaxeorg/ESP-Miner issue #959: All API calls - CORS related

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/959
> Collected: 2026-10-07
> Published: 2025-05-26

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 959
- State: closed
- Author: xr1140
- Opened: 2025-05-26
- Closed: 2025-05-26
- Labels: none

## Description

Hello, 
Unable to use the UI after inital network config. All API calls fail with  "Unauthorized". Log below.


`
[0;32mI (5512) connect: IP Address: 8.0.0.106
[0;32mI (5512) esp_netif_handlers: sta ip: 8.0.0.106, mask: 255.255.255.0, gw: 8.0.0.1
[0;32mI (5602) bitaxe: Connected to SSID: XXXXXXXXXX
I (5602) wifi:mode : sta (--:--:--:--:--:--)
[0;32mI (5602) connect: Configuration Access Point disabled

[0;32mI (32452) CORS: Client is NOT in the private ip ranges or same range as server.
[0;33mW (32452) httpd_txrx: httpd_resp_send_err: 401 Unauthorized - Unauthorized

[0;32mI (36532) CORS: Client is NOT in the private ip ranges or same range as server.
[0;33mW (36542) httpd_txrx: httpd_resp_send_err: 401 Unauthorized - Unauthorized
[0;32mI (36612) CORS: Client is NOT in the private ip ranges or same range as server.
[0;33mW (36612) httpd_txrx: httpd_resp_send_err: 401 Unauthorized - Unauthorized
`


**Hardware (please complete the following information):**
 - Bitaxe HW version: 601
 - Bitaxe HW vendor: WholeMining.eu
 - ESP-Miner FW version: 4.7.0 - 4.8.0b3



## Comments

### xr1140 on 2025-05-26

After some reading it seems my network is not using a private ip range. #821
