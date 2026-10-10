# 256foundation/asic-rs pull request #387: fix(epic): detect restore support from capabilities

> Source: https://github.com/256foundation/asic-rs/pull/387
> Collected: 2026-10-07
> Published: 2026-09-17

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 387
- State: closed
- Author: cfilipescu
- Opened: 2026-09-17
- Closed: 2026-09-17
- Labels: none

## Description

## Summary
- detect Epic stock OS restore support from the `/capabilities` `UninstallSupported` boolean
- stop inferring support from `/openapi.json`
- print the detected capability in the non-destructive live data test
- preserve retry behavior after transient capability probe failures

## Validation
- `MINER_IP=10.0.81.33 cargo test parse_data_live_test_auto_detect -p asic-rs-firmwares-epic -- --ignored --nocapture` (reports `supports_restore_stock_os true`)
- `cargo test -p asic-rs-firmwares-epic`
- `cargo clippy -p asic-rs-firmwares-epic --all-targets -- -D warnings`

Related to #376.
