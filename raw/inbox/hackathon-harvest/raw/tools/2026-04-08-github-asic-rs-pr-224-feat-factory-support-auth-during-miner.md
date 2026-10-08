# 256foundation/asic-rs pull request #224: feat(factory): support auth during miner discovery

> Source: https://github.com/256foundation/asic-rs/pull/224
> Collected: 2026-10-07
> Published: 2026-04-08

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 224
- State: closed
- Author: cfilipescu
- Opened: 2026-04-08
- Closed: 2026-04-08
- Labels: none

## Description

## Summary
- add optional `discovery_auth` to `MinerFactory` so callers can supply credentials during discovery-based miner construction
- pass configured auth to `build_miner` after firmware identification to support stock firmwares requiring non-default digest credentials
- add `with_discovery_auth` builder method and update docs/debug output to reflect configurable discovery auth
