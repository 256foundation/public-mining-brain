# bitaxeorg/ESP-Miner issue #320: Wifi never goes back to connected after WiFi connection failed

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/320
> Collected: 2026-10-07
> Published: 2024-09-05

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 320
- State: closed
- Author: eandersson
- Opened: 2024-09-05
- Closed: 2024-09-06
- Labels: none

## Description

In the UI the status is stuck at something like this after being disconnected from the WiFi and then successfully re-establishing the connection again.
> WiFi Status: Retrying 100

![image](https://github.com/user-attachments/assets/cc0332ee-9add-488c-a7a4-914682e80fe4)

Steps to reproduce
- Connect device to WiFi.
- Restart WiFi Router / AP.
- Reconnect to device. WebUI under Logs should say `Connected!`, but instead says `Retrying: X`.


## Comments

### eandersson on 2024-09-06

This is a duplicate of https://github.com/skot/ESP-Miner/issues/289
