# bitaxeorg/ESP-Miner issue #229: Change work immeadiately on clean_jobs=true

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/229
> Collected: 2026-10-07
> Published: 2024-06-18

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 229
- State: closed
- Author: skot
- Opened: 2024-06-18
- Closed: 2025-06-11
- Labels: enhancement

## Description

Stratum `mining.notify` has a parameter called `clean_jobs`. We should make sure we change out current the ASIC job as fast as possible when `clean_jobs=true`

Pools need to be able to change the miners work ASAP when there is a new block.

## Comments

### mutatrum on 2025-06-11

Fixed with 40cb7fa
