# 256foundation/asic-rs pull request #142: feature: `SetPools` trait, related fixes, and bindings

> Source: https://github.com/256foundation/asic-rs/pull/142
> Collected: 2026-10-07
> Published: 2026-02-20

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 142
- State: closed
- Author: b-rowan
- Opened: 2026-02-20
- Closed: 2026-02-23
- Labels: none

## Description

Adds a new `SetPools` trait, which takes in `Vec<PoolGroup>` and is used to set the pools on a miner.

There are several related fixes included here:
- Swapping to using `PoolGroupData` in miner data [BREAKING]
- Adding the relevant python bindings for `SetPools`
- Fixing some issues with the python bindings related to incorrect typing
- Adding a conversion between `PoolGroupData` and the new config `PoolGroup`
