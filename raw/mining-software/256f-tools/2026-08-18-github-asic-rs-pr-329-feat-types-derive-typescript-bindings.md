# 256foundation/asic-rs pull request #329: feat(types): derive TypeScript bindings for shared models

> Source: https://github.com/256foundation/asic-rs/pull/329
> Collected: 2026-10-07
> Published: 2026-08-18

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 329
- State: closed
- Author: Erisli
- Opened: 2026-08-18
- Closed: 2026-08-19
- Labels: none

## Description

## Summary
- Add ts-rs as a workspace dependency and configure large integers as TypeScript numbers.
- Derive TS for shared config, telemetry, model, hardware, pool, message, and make-specific enums.
- Override TypeScript shapes for custom-serialized measurement, MAC, power target, and uptime fields.

## Validation
- cargo fmt
- cargo +1.95.0 check --workspace

Note: cargo check --workspace with the local 1.88.0 override hit an existing compiler limitation in asic-rs-core/src/traits/miner.rs:419, so validation used the already-installed 1.95.0 toolchain.

## Comments

### b-rowan on 2026-08-18

Is this dependent on #322 ?
