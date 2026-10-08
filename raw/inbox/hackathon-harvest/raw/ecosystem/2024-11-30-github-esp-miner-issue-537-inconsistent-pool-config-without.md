# bitaxeorg/ESP-Miner issue #537: Inconsistent pool config without restart

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/537
> Collected: 2026-10-07
> Published: 2024-11-30

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 537
- State: closed
- Author: terratec
- Opened: 2024-11-30
- Closed: 2025-01-26
- Labels: good first issue

## Description

Url/Port from global state remain old after saving but user/pass are updated from nvs config.

The config should either work without reboot or the old data should be retained?
