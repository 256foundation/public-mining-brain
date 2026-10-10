# bitaxeorg/ESP-Miner issue #538: Bug: Front end sometimes loses connection with bitaxe after a reset or reflash.

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/538
> Collected: 2026-10-07
> Published: 2024-12-01

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 538
- State: closed
- Author: mutatrum
- Opened: 2024-12-01
- Closed: 2026-06-02
- Labels: none

## Description

On some restarts of the device, the front-end picks up the connections, but sometimes the front-end loses connection and never updates again until a refresh. Didn't investigate further.

## Comments

### mutatrum on 2024-12-03

Trying to reproduce this by rebooting the device. I didn't succeed yet, but I did notice the api calls take quite a long time:

![image](https://github.com/user-attachments/assets/ce5354df-8897-4d7d-9ef6-483c6b440b29)

This might be related. 100ms+ for returning a json is not good.

### eandersson on 2024-12-03

Are you able to capture logs from your device? This is usually WiFi connectivity issues, but can be anything where the device is too busy to reply, or even connections that aren't closed properly.

### mutatrum on 2024-12-04

It's a front-end error, it doesn't seem to recover from this:

![image](https://github.com/user-attachments/assets/6c4d5ed1-a291-41bc-af45-c83823558fdf)

This was after a sleep and/or network disconnect from my computer.


### mutatrum on 2026-06-02

No longer relevant
