# bitaxeorg/ESP-Miner issue #53: Add validation for user settings inputs like url

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/53
> Collected: 2026-10-07
> Published: 2023-10-26

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 53
- State: closed
- Author: benjamin-wilson
- Opened: 2023-10-26
- Closed: 2023-11-15
- Labels: none

## Description

Url should not contain the stratum+tcp:// that some pools include, we should not allow saving this bad data. Other fields as well.

## Comments

### benjamin-wilson on 2023-11-15

Added https://github.com/skot/ESP-Miner/commit/a5bcec5cd4c6a00b0e2d289729ead6b58eb3905b
