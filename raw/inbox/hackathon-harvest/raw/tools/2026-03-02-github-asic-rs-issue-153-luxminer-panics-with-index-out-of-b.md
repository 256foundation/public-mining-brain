# 256foundation/asic-rs issue #153: LuxMiner panics with index out of bound when trying to get Expected Hash Rate

> Source: https://github.com/256foundation/asic-rs/issues/153
> Collected: 2026-10-07
> Published: 2026-03-02

- Repository: 256foundation/asic-rs
- Type: issue
- Number: 153
- State: closed
- Author: NeroWeNeed
- Opened: 2026-03-02
- Closed: 2026-03-02
- Labels: none

## Description

Panic occurs when trying to call `parse_expected_hashrate` on `LuxMinerV1`, due to an Index Out of Bounds Error at line 755 in `/src/miners/luxminer/v1/mod.rs`
