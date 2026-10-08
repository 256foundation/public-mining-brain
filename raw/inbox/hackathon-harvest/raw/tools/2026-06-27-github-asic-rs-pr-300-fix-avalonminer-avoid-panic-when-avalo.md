# 256foundation/asic-rs pull request #300: fix(avalonminer): avoid panic when Avalon Q HBinfo is incomplete

> Source: https://github.com/256foundation/asic-rs/pull/300
> Collected: 2026-10-07
> Published: 2026-06-27

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 300
- State: closed
- Author: gzw13999
- Opened: 2026-06-27
- Closed: 2026-06-28
- Labels: none

## Description

## Summary
- Handle missing or empty Avalon Q `HBinfo` entries without panicking
- Use safe `.get()` access instead of indexing into JSON maps
## Test plan
- [x] `cargo test -p asic-rs-firmwares-avalonminer avalon_q`
- [x] Verified telemetry collection on real Avalon Q miner
