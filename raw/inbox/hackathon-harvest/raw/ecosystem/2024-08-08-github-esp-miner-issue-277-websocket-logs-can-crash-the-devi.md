# bitaxeorg/ESP-Miner issue #277: Websocket (logs) can crash the device

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/277
> Collected: 2026-10-07
> Published: 2024-08-08

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 277
- State: closed
- Author: eandersson
- Opened: 2024-08-08
- Closed: 2024-09-11
- Labels: bug

## Description

If you open too many connections to get logs you'll eventually crash the device and it won't recover on its own. It's pretty easy to reproduce by just having something like a python script open a few ws connections in rapid succession. This seems to be a pretty known issue with ESP32, but wasn't able to find a solution for ws. I tried adding `Connection: close` to the header and set things like `lru_purge_enable` without success.

```
(19826) httpd_ws: httpd_ws_get_frame_type: Failed to read header byte (socket FD invalid), closing socket now
W (19826) httpd_ws: httpd_ws_get_frame_type: Failed to read header byte (socket FD invalid), closing socket now
W (19836) httpd_txrx: httpd_sock_err: error in send : 104
W (19846) httpd_txrx: httpd_sock_err: error in send : 128
W (19846) httpd_txrx: httpd_sock_err: error in send : 128
W (19856) httpd_txrx: httpd_sock_err: error in send : 128

***ERROR*** A stack overflow in task httpd has been detected.

Backtrace: 0x40375c62:0x3fcbe720 0x4037d859:0x3fcbe740 0x4037e812:0x3fcbe760 0x4037fce7:0x3fcbe7e0 0x4037e8d8:0x3fcbe800 0x4037e8ce:0x00000000 |<-CORRUPTED
0x40375c62: panic_abort at /opt/esp/idf/components/esp_system/panic.c:463
0x4037d859: esp_system_abort at /opt/esp/idf/components/esp_system/port/esp_system_chip.c:92
0x4037e812: vApplicationStackOverflowHook at /opt/esp/idf/components/freertos/FreeRTOS-Kernel/portable/xtensa/port.c:553
0x4037fce7: vTaskSwitchContext at /opt/esp/idf/components/freertos/FreeRTOS-Kernel/tasks.c:3701 (discriminator 7)
0x4037e8d8: _frxt_dispatch at /opt/esp/idf/components/freertos/FreeRTOS-Kernel/portable/xtensa/portasm.S:451
0x4037e8ce: _frxt_int_exit at /opt/esp/idf/components/freertos/FreeRTOS-Kernel/portable/xtensa/portasm.S:246
```

## Comments

### skot on 2024-08-08

Ah, good catch. Do you know if we can set a connection limit?

### eandersson on 2024-08-09

The issue seems to be with any type of broken connection and not necessarily just having a bunch of connections. This is a simple code snippet to quickly trigger the crash. It requires the python `websockets` library.
```
from websockets.sync import client
import multiprocessing
import time

MY_IP = '192.168.0.100'


def main():
    while True:
        with client.connect(f"ws://{MY_IP}/api/ws") as websocket:
            while True:
                websocket.recv(timeout=60)


if __name__ == '__main__':
    processes = []
    for _ in range(5):
        process = multiprocessing.Process(target=main)
        process.start()
        processes.append(process)

    time.sleep(1)

    for process in processes:
        process.kill()
```

### OsO-1973 on 2024-08-23

Hello
was able to reproduce a crash as discussed with skot
1368, 525, 1166, 2.1.10

open on iPhone 15 pro latest firmware logs, hit show logs and put iPhone on standby
innert 5 mins webgui of Bitaxe is not reachable on LAN anymore

network ping - device is responding
webgui not responding
display on device says see pics
device is not recovering and on display showing evthg alright though ckpool says otherwise


log on ckpool (happened yesterday same at 9am (at 10 p.m i changed some settings) and today at about 8 a.m.

![IMG_5877](https://github.com/user-attachments/assets/4a699891-479d-43c1-b972-0b378b9556f4)
![IMG_5876](https://github.com/user-attachments/assets/27397cfc-1be7-4ee2-b2c6-dfb4238bdaa6)
![IMG_5875](https://github.com/user-attachments/assets/20b0c65d-0be2-4c83-b131-28af089de51f)
<img width="2055" alt="Bildschirmfoto 2024-08-23 um 08 48 57" src="https://github.com/user-attachments/assets/054e1d0b-3bcb-4e6e-b1d4-009baa98f842">
