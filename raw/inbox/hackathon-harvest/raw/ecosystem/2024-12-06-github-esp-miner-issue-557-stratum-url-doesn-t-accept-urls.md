# bitaxeorg/ESP-Miner issue #557: "Stratum URL" doesn't accept URLs

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/557
> Collected: 2026-10-07
> Published: 2024-12-06

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 557
- State: closed
- Author: luke-jr
- Opened: 2024-12-06
- Closed: 2024-12-07
- Labels: design

## Description

A URL has a schema, host, and optional port. ESP-Miner explicitly doesn't accept schema or port. So it doesn't accept a URL.

Either it should accept a URL, or it should be renamed to "Stratum host" or something
