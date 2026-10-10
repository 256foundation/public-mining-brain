# 256foundation/asic-rs pull request #388: test: validate stock OS restoration contracts

> Source: https://github.com/256foundation/asic-rs/pull/388
> Collected: 2026-10-07
> Published: 2026-09-17

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 388
- State: closed
- Author: cfilipescu
- Opened: 2026-09-17
- Closed: 2026-09-18
- Labels: none

## Description

## Summary

Closes #377

- add mocked restore-stock-OS contract coverage across LuxOS, VNish, Braiins OS, and ePIC
- verify unsupported/version-specific backends remain unsupported
- assert factory reset settings capability remains independent from stock-OS restoration
- keep live support probes non-destructive, while preserving the original restore integration tests as explicitly ignored destructive tests
- regenerate the supported-devices matrix with separate `Factory Reset Settings` and `Restore Stock OS` columns

## Validation

- `cargo fmt --all -- --check`
- `cargo test --workspace`
- `cargo clippy --workspace --all-targets -- -D warnings`
- `cargo test -p asic-rs-firmwares-luxminer -p asic-rs-firmwares-vnish -p asic-rs-firmwares-braiins -p asic-rs-firmwares-epic`
- `python3 scripts/docs/gen_supported_devices.py --check`

The local environment does not include Go or uv/pytest; the Go and Python CI checks pass.
