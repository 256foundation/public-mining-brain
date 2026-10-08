# bitaxeorg/ESP-Miner issue #75: shutdown core voltage regulator

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/75
> Collected: 2026-10-07
> Published: 2024-01-08

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 75
- State: closed
- Author: skot
- Opened: 2024-01-08
- Closed: 2024-01-13
- Labels: enhancement

## Description

Recent BitaxeUltra versions (since 202, I believe) have the ability to turn off the TPS40305 ASIC core voltage regulator. 

it's called `PWR_EN` and it's attached to ESP32 GPIO10

We should shutdown the ASIC power when;
- temperature is too high
- the barrel jack is not inserted

## Comments

### benjamin-wilson on 2024-01-13

https://github.com/skot/ESP-Miner/commit/ef344f236dda1e7a1dd91cd7556308c456466620
