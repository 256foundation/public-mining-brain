# 256foundation/asic-rs pull request #401: feat(epic): add perpetual tune scaling reset

> Source: https://github.com/256foundation/asic-rs/pull/401
> Collected: 2026-10-07
> Published: 2026-09-30

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 401
- State: closed
- Author: cfilipescu
- Opened: 2026-09-30
- Closed: 2026-09-30
- Labels: none

## Description

## Summary
- Add `reset_scaling` and `supports_reset_scaling` to `SupportsScalingConfig`, with unsupported defaults for other backends.
- Implement the reset for EPic PowerPlay by reading the active perpetual tune algorithm and POSTing it to `/perpetualtune/reset`.
- Return an error when perpetual tuning is not running, so no reset request is sent without an active algorithm.

## Verification
- `cargo fmt --all -- --check`
- `cargo test -p asic-rs-firmwares-epic --locked`
- `cargo test --all --locked --exclude asic-rs-pydantic --exclude asic-rs-pydantic-macros --exclude pyasic-rs --exclude asic-rs-ffi`

The endpoint restarts perpetual tuning progression. Behavior on a live miner has not been verified here.
