# 256foundation/asic-rs pull request #399: fix(braiins): derive board activity from frequency

> Source: https://github.com/256foundation/asic-rs/pull/399
> Collected: 2026-10-07
> Published: 2026-09-29

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 399
- State: closed
- Author: cfilipescu
- Opened: 2026-09-29
- Closed: 2026-09-29
- Labels: none

## Description

## Summary

- Derive Braiins `BoardData.active` from per-board frequency across supported backends: positive frequency is active, zero is inactive, and missing frequency remains unknown.
- Clarify that the shared activity field may be inferred from firmware telemetry.

## Validation

- `cargo fmt --check`
- `cargo check -p asic-rs-firmwares-braiins`
