# bitaxeorg/ESP-Miner issue #651: Difference between `esp-miner.bin` and `esp-miner-factory-[...].bin`?

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/651
> Collected: 2026-10-07
> Published: 2025-01-12

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 651
- State: closed
- Author: etkaar
- Opened: 2025-01-12
- Closed: 2025-01-14
- Labels: none

## Description

What is the difference between `esp-miner.bin` and the `esp-miner-factory-[...].bin` firmwares?

## Comments

### MyOwn2C on 2025-01-12

Factory has self test. 
Others don’t. 

### skot on 2025-01-14

"factory" firmware bin files contain both the esp-miner.bin (esp-miner firmware) and www.bin (AxeOS firmware) and a NVS config with selftest=1. This will reset your bitaxe back to it's factory state and run the selftest on first boot.
