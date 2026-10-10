# bitaxeorg/ESP-Miner issue #1518: Only generated api sources if openapi.yaml has changed

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1518
> Collected: 2026-10-07
> Published: 2026-01-20

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1518
- State: closed
- Author: mutatrum
- Opened: 2026-01-20
- Closed: 2026-01-27
- Labels: none

## Description

To reduce build times, the `generate:api` step should only run if `openapi.yaml` or any other dependent files actually changed.
