# 256foundation/asic-rs issue #304: expand hashrate struct in core to implement default units for display

> Source: https://github.com/256foundation/asic-rs/issues/304
> Collected: 2026-10-07
> Published: 2026-06-29

- Repository: 256foundation/asic-rs
- Type: issue
- Number: 304
- State: closed
- Author: cfilipescu
- Opened: 2026-06-29
- Closed: 2026-09-10
- Labels: none

## Description

Might be worth breaking hashrate out to being a trait, then having a few different hashrate types (ScryptHashRate, SHA256HashRate, etc), which can each implement default_unit and display for example.
