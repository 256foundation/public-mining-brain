# 256foundation/asic-rs pull request #166: feat: implement ePIC pool and hashrate split updates

> Source: https://github.com/256foundation/asic-rs/pull/166
> Collected: 2026-10-07
> Published: 2026-03-11

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 166
- State: closed
- Author: cfilipescu
- Opened: 2026-03-11
- Closed: 2026-03-11
- Labels: none

## Description

## Summary
- implement `SetPools` support for ePIC PowerPlay v1 and enable `supports_set_pools()`
- apply single pool-group configs via `coin`, set worker ID variant to `MacAddress`, and disable hashrate split
- apply multi-group configs via `hashratesplit` with quota-based ratios and enable hashrate split
