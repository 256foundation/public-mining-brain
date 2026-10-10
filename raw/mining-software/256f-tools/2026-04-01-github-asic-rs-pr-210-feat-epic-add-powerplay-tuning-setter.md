# 256foundation/asic-rs pull request #210: feat(epic): add PowerPlay tuning setter with scaling input

> Source: https://github.com/256foundation/asic-rs/pull/210
> Collected: 2026-10-07
> Published: 2026-04-01

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 210
- State: closed
- Author: cfilipescu
- Opened: 2026-04-01
- Closed: 2026-04-01
- Labels: none

## Description

## Summary
- implement `set_tuning_config` for ePIC PowerPlay V1 by calling `POST /perpetualtune/algo` with normalized algorithm + validated target values
- require an explicit `ScalingConfig` for ePIC tuning writes and include `min_throttle`/`throttle_step` from it in the request payload
- update `SupportsTuningConfig::set_tuning_config` to accept `Option<ScalingConfig>` and adapt WhatsMiner V2/V3 implementations to the new signature

## Validation
- `cargo check`
- `cargo test -p asic-rs-firmwares-epic`
