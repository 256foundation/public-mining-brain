# bitaxeorg/ESP-Miner issue #76: detect barrel jack insertion

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/76
> Collected: 2026-10-07
> Published: 2024-01-08

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 76
- State: closed
- Author: skot
- Opened: 2024-01-08
- Closed: 2024-01-13
- Labels: enhancement

## Description

Since Bitaxe version 204 we have the ability to detect if the 5V barrel jack is inserted or not. This signal is called `PLUG_SENSE` and it's connected to the ESP32 GPIO12. `PLUG_SENSE` should go high when the barrel jack is inserted.

We should use this to disable the Core voltage regulator (see #75) when the barrel jack is disconnected (meaning we are powered by USB). 

## Comments

### benjamin-wilson on 2024-01-13

https://github.com/skot/ESP-Miner/commit/ef344f236dda1e7a1dd91cd7556308c456466620
