# bitaxeorg/ESP-Miner issue #177: Make self-test opt-in via nvm config

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/177
> Collected: 2026-10-07
> Published: 2024-05-21

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 177
- State: closed
- Author: skot
- Opened: 2024-05-21
- Closed: 2024-05-24
- Labels: enhancement

## Description

I'd like to make the self-test opt-in by making `NVS_CONFIG_SELF_TEST` default value zero. This way factories can run the self test explicitly setting the config to do so. Others won't be affected.

## Comments

### benjamin-wilson on 2024-05-24

Fixed 19e6369ac272986246b1b83dd8bc616d91b5cff3
