# 256foundation/asic-rs pull request #330: test(epic): add live perpetual tuning test

> Source: https://github.com/256foundation/asic-rs/pull/330
> Collected: 2026-10-07
> Published: 2026-08-19

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 330
- State: closed
- Author: cfilipescu
- Opened: 2026-08-19
- Closed: 2026-08-19
- Labels: none

## Description

## Summary

- add an ignored ePIC PowerPlay live test that reads and prints the current perpetual tuning and scaling configuration before writing
- support ChipTune and PowerTune selection through `EPIC_TUNE_MODE`
- support optional `EPIC_HASHRATE_TARGET_TH` and `EPIC_POWER_TARGET_W` overrides, defaulting to 103 TH/s and 3000 W
- keep the general live data test read-only by removing its tuning write

## Why

This provides a deliberate, opt-in way to validate perpetual tuning against a live miner while preserving the miner's existing scaling values and keeping ordinary test runs non-destructive.

## Validation

- `cargo +1.95.0 fmt --all -- --check`
- `cargo +1.95.0 test -p asic-rs-firmwares-epic` (9 passed, 3 live tests ignored)
