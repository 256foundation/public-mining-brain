# bitaxeorg/ESP-Miner issue #24: Serial Synchronization

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/24
> Collected: 2026-10-07
> Published: 2023-09-03

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 24
- State: open
- Author: SatsForFreedom
- Opened: 2023-09-03
- Closed: n/a
- Labels: none

## Description

Eventually the UART can miss a package and lost the header 0xAA55. Today, I need to manually reset the device to fix that issue.

This is a rare event.

![Screenshot_20230903_155051](https://github.com/skot/ESP-Miner/assets/132848052/6710df77-e2a0-4f60-86cf-51a88b67660b)
