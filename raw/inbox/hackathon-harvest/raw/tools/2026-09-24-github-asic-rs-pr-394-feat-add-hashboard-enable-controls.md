# 256foundation/asic-rs pull request #394: feat: add hashboard enable controls

> Source: https://github.com/256foundation/asic-rs/pull/394
> Collected: 2026-10-07
> Published: 2026-09-24

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 394
- State: closed
- Author: cfilipescu
- Opened: 2026-09-24
- Closed: 2026-09-24
- Labels: none

## Description

## Summary

- Add a capability-checked `set_hashboards_enabled` operation to the shared Miner API.
- Implement board control for ePIC UMC and Braiins OS backends, validating selected board positions and mapping firmware-specific identifiers.
- Expose the operation through Python, C, and Go bindings.

Closes #392

## Validation

- `cargo check --workspace` — passed.
- `git diff --check` — passed.
- Tests were not run. The Go wrapper was not build-checked because Go tooling is unavailable in the environment.
