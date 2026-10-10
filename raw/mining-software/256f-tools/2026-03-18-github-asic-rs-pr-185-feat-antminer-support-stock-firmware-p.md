# 256foundation/asic-rs pull request #185: feat(antminer): support stock firmware pool configuration

> Source: https://github.com/256foundation/asic-rs/pull/185
> Collected: 2026-10-07
> Published: 2026-03-18

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 185
- State: closed
- Author: cfilipescu
- Opened: 2026-03-18
- Closed: 2026-03-19
- Labels: none

## Description

## Summary
- add Antminer stock firmware pool configuration support through `SupportsPoolsConfig::set_pools_config`
- improve Antminer pool discovery by collecting pool data from both RPC and miner config sources, with miner config as fallback when RPC pool data is empty
- refactor pool parsing in the Antminer v2020 backend to reduce duplication and keep pool mapping logic consistent

## Validation
- cargo check -q

## Comments

### b-rowan on 2026-03-18

Main issue here is that the parsing for `get_miner_conf.cgi` is being put into the `get_pools` data gathering endpoint, when we actually don't want it there, and it should be moved into `get_pools_config`.  The default implementation for `get_pools_config` is just there to allow using it if the proper way to get the pool config hasn't been defined.
