# 256foundation/asic-rs pull request #183: feat: add tuning config support across miner traits and backends

> Source: https://github.com/256foundation/asic-rs/pull/183
> Collected: 2026-10-07
> Published: 2026-03-17

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 183
- State: closed
- Author: cfilipescu
- Opened: 2026-03-17
- Closed: 2026-03-17
- Labels: none

## Description

## Summary
- add a new `TuningConfig` model and `SupportsTuningConfig` trait path in core config/trait interfaces.
- rename collector field usage from `WattageLimit` to `TuningTarget` and update backend data extraction/parsing accordingly.
- implement Epic backend parsing for tuning target/config from summary perpetual tune data and add explicit `SupportsTuningConfig` stubs for other backends.
