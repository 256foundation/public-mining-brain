# 256foundation/asic-rs pull request #198: feat(config): add fan config support and ePIC parsing

> Source: https://github.com/256foundation/asic-rs/pull/198
> Collected: 2026-10-07
> Published: 2026-03-21

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 198
- State: closed
- Author: cfilipescu
- Opened: 2026-03-21
- Closed: 2026-03-21
- Labels: none

## Description

## Summary
- Add a new `FanConfig` model in core config types, including `Auto` and `Manual` fan modes, and introduce a new `ConfigField::Fan`.
- Add `SupportsFanConfig` support across miner traits/backends, with no-op unsupported implementations where fan config is not available.
- Implement ePIC PowerPlay v1 fan config collection/parsing from `/summary` (`/Fans/Fan Mode`) and add coverage for fan config parsing.

## Validation
- cargo check
- cargo test -p asic-rs-core
- cargo test -p asic-rs-firmwares-epic --lib

## Comments

### b-rowan on 2026-03-21

CI wants `cargo fmt` run..
