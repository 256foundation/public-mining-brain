# bitaxeorg/ESP-Miner issue #1250: Feature Request - Stop hashing when Wifi is down - save electricity costs

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1250
> Collected: 2026-10-07
> Published: 2025-09-25

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1250
- State: closed
- Author: Legandalf
- Opened: 2025-09-25
- Closed: 2025-09-26
- Labels: none

## Description

Currently, if the Wifi goes down temporarily or for a long period of time, the hashing will try to continue and the Power Consumption will not go down, especially when the user is not at home to switch off the Bitaxe until the Wifi is back.

If possible, when Wifi is down, or when hashing is impossible, the hashing should stop and be put on standby until the Wifi comes back. This should lower energy consumption.

## Comments

### mutatrum on 2025-09-26

Duplicate of #911
