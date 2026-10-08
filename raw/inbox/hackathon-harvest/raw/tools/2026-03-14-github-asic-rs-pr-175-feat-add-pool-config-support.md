# 256foundation/asic-rs pull request #175: feat: add pool config support

> Source: https://github.com/256foundation/asic-rs/pull/175
> Collected: 2026-10-07
> Published: 2026-03-14

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 175
- State: closed
- Author: cfilipescu
- Opened: 2026-03-14
- Closed: 2026-03-14
- Labels: none

## Description

## Summary
- add dedicated pool config types (`PoolConfig`, `PoolGroupConfig`) and migrate miner config traits to the new pool-config interface
- update firmware backends and Python bindings to use `supports_pools_config` / `set_pools_config`
- introduce shared scaling config trait plumbing required by the miner config migration
