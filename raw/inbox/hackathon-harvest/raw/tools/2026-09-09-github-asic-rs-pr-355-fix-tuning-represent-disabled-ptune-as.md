# 256foundation/asic-rs pull request #355: fix(tuning): represent disabled ptune as manual target

> Source: https://github.com/256foundation/asic-rs/pull/355
> Collected: 2026-10-07
> Published: 2026-09-09

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 355
- State: closed
- Author: cfilipescu
- Opened: 2026-09-09
- Closed: 2026-09-10
- Labels: none

## Description

## Summary

- add a board-indexed `Manual` variant to `TuningTarget`, with all other variants implying perpetual tuning is enabled
- represent each board setpoint as optional frequency and voltage values so an explicit disabled state is retained when telemetry is incomplete
- serialize available manual frequencies and voltages as scalar MHz and volts, matching `BoardData`, with scalar round-trip deserialization
- return the manual target from ePIC telemetry and config parsing whenever `PerpetualTune.Running` is explicitly false
- preserve missing or malformed running status as `None` and expose the board-level representation through Python, Pydantic, TypeScript, and type stubs
- reject unsupported manual configuration in other firmware backends

## Testing

- `cargo test --workspace --all-features`
- `cargo clippy --workspace --all-targets --all-features -- -D warnings`
- `pytest -q python/tests` (98 passed)

Closes #352
