# 256foundation/asic-rs pull request #405: fix(vnish): allow anonymous access to known read endpoints

> Source: https://github.com/256foundation/asic-rs/pull/405
> Collected: 2026-10-07
> Published: 2026-10-01

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 405
- State: closed
- Author: cfilipescu
- Opened: 2026-10-01
- Closed: 2026-10-06
- Labels: none

## Description

## Summary

- Try anonymous GET requests only for the VNish routes confirmed to be public: `/info`, `/status`, `/summary`, `/metrics`, `/chains`, `/chains/factory-info`, `/settings`, and `/autotune/presets`.
- Share that allowlist between the 1.2.x and 1.3.x clients.
- Authenticate before privileged and unknown requests; authenticate and retry if a public read returns 401.

This allows data reads from VNish miners that expose these routes without a password.

## Validation

- Unauthenticated GET requests returned HTTP 200 for every route in the allowlist on a live VNish miner.
- The ignored `parse_data_live_test_auto_detect` test passed against that miner and returned a non-null MAC.
- `cargo check -p asic-rs-firmwares-vnish` and `cargo fmt --all -- --check` passed.
