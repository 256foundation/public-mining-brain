# 256foundation/asic-rs pull request #357: feat(data): expose detailed firmware operating state

> Source: https://github.com/256foundation/asic-rs/pull/357
> Collected: 2026-10-07
> Published: 2026-09-10

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 357
- State: closed
- Author: cfilipescu
- Opened: 2026-09-10
- Closed: 2026-09-10
- Labels: none

## Description

Fixes #353.

## Summary

- Add optional `MinerData.operating_state` and `get_operating_state()` with a shared enum covering mining/stable operation, startup, tuning, frequency/voltage adjustment, pause/stop, degraded mining, and errors.
- Parse explicit state telemetry from ePIC/UMC, VNish, Braiins REST, MARA, and Proto. Preserve unfamiliar values as `Unknown { raw }`; missing, invalid, or boolean-only telemetry remains `None`.
- Reuse existing collector requests without changing legacy `is_mining` behavior or existing `DataField` numeric values.
- Update Python/Pydantic bindings and stubs, TypeScript types, documentation, and regression coverage. Backends without detailed state telemetry use the default unavailable result.

## Validation

- `cargo test --all --locked --exclude asic-rs-pydantic --exclude asic-rs-pydantic-macros`
- `cargo test --workspace --all-features --locked --exclude asic-rs-pydantic --exclude asic-rs-pydantic-macros`
- `cargo clippy --workspace --all-features --locked`
- `cargo fmt --all -- --check`
- Rebuilt the Python extension with Maturin; `python -m pytest -q python/tests`: **114 passed** on Python 3.13.
- `git diff --check`

Regression tests cover firmware-to-snapshot mappings, unknown/raw and missing states, Rust/Pydantic serialization, TypeScript shape, boolean-only firmware, and single-request ePIC summary collection.

Live-miner tests were not run.
