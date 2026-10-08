# bitaxeorg/ESP-Miner issue #1466: websocket connect generates

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1466
> Collected: 2026-10-07
> Published: 2025-12-19

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1466
- State: closed
- Author: frickl
- Opened: 2025-12-19
- Closed: 2025-12-23
- Labels: wontfix

## Description

**Describe the bug**
A clear and concise description of what the bug is.

Bitaxe Gamma 601 - v2.12.0
Free Heap Memory | 8.16 MB
• Internal | 103 kB
• Spiram | 8.09 MB
Firmware Version | v2.12.0
AxeOS Version | v2.12.0
ESP-IDF Version | v5.5.1


* connecting from remote to the api for getting the logfiles results in
  a) error "Too many open websockets" and
 b) leads to memory corruption and spontaneous reboot

**To Reproduce**
Steps to reproduce the behavior:
1. Go to '...'

open a browser, point to:
*  http://<ip>/api/ws

* open a second tab:
http://<ip>/#/logs

-> logfile is not shown anymore, but a max connection reached.

Browser shows:
u[0;33mW (3697655) httpd_txrx: httpd_resp_send_custom_err: 429 Too Many Requests - Max WebSocket clients reached[0m
I[0;32mI (3697666) websocket: Closing fd: 54 for rejected connection[0m


A websocket-script:

    while True:
    try:
        ws = create_connection("ws://<ip>/api/ws")
        print("Connected. Logging data…")

leads to:

₿ (67949) websocket: Max WebSocket clients reached, rejecting new connection
₿ (67949) httpd_txrx: httpd_resp_send_custom_err: 429 Too Many Requests - Max WebSocket clients reached

after about a minute the system reboots, showing:

Device Model | Gamma
-- | --
Board Version | 601
ASIC Type | BM1370
Uptime | 2 minutes, 37 seconds
Reset Reason | Software reset due to exception/panic



**Expected behavior**
A clear and concise description of what you expected to happen.

Logfile should be shown as result in the api-call

**Screenshots & Photos**
If applicable, add AxeOS screenshots and/or photos of your Bitaxe to help explain your problem.

**Hardware (please complete the following information):**
 - Bitaxe HW version: Gamma 601
 - Bitaxe HW vendor:
 - ESP-Miner FW version:  v5.5.1
 - Hash Frequency: 625
 - Voltage: 1150

**Additional context**
Add any other context about the problem here.


## Comments

### mutatrum on 2025-12-20

Its possible to open 10  websocket connections, are you sure the script works as intended? 

And please elaborate on memory corruption and reboots. 

### mutatrum on 2025-12-23

I reproduced the issue. One can indeed crash the device by hammering the websocket, but probably also when hammering the other endpoints. I tried increasing the stack size, but that didn't help. 

As the device is not meant to be reachable from the open internet, this is not a viable attack vector. If you wish to crash your own device, that's fine.

[crash.log](https://github.com/user-attachments/files/24310553/crash.log)
