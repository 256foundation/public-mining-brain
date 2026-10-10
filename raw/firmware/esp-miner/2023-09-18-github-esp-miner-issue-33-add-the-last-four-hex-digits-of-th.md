# bitaxeorg/ESP-Miner issue #33: add the last four hex digits of the MAC address to the WiFi name

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/33
> Collected: 2026-10-07
> Published: 2023-09-18

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 33
- State: closed
- Author: skot
- Opened: 2023-09-18
- Closed: 2023-09-20
- Labels: enhancement

## Description

We need a unique name for the AP SSID incase there are multiple bitaxe running nearby.

I have seen this done by appending the last 2 bytes of the Wi-Fi MAC address to the default SSID.

## Comments

### benjamin-wilson on 2023-09-20

https://github.com/skot/ESP-Miner/commit/a30a7ef05fd2661172ae6e171246c8a080f5fb8e
