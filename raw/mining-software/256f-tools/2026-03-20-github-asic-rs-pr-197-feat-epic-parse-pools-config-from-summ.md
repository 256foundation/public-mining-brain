# 256foundation/asic-rs pull request #197: feat(epic): parse pools config from summary and hashrate split

> Source: https://github.com/256foundation/asic-rs/pull/197
> Collected: 2026-10-07
> Published: 2026-03-20

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 197
- State: closed
- Author: cfilipescu
- Opened: 2026-03-20
- Closed: 2026-03-21
- Labels: none

## Description

## Summary
- Parse ePIC pool config from combined config payload by reading summary `StratumConfigs` when hashrate split is disabled.
- Parse `hashratesplit.hashrate_splits` when enabled and map each split to a `PoolGroupConfig` using API `ratio` as quota.
- Add tests covering summary fallback, split parsing, and a 33/33/34 split case.

## Validation
- cargo test -p asic-rs-firmwares-epic parse_pools_config_
