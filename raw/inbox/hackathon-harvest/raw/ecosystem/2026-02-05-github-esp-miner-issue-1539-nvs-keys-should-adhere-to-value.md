# bitaxeorg/ESP-Miner issue #1539: NVS keys should adhere to value limits

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1539
> Collected: 2026-10-07
> Published: 2026-02-05

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1539
- State: open
- Author: mutatrum
- Opened: 2026-02-05
- Closed: n/a
- Labels: none

## Description

NVS keys can be stored outside of the specified `min` and `max` range. This should be guarded in `nvs_config.c` itself, both for reads and writes.
