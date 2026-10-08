# 256foundation/asic-rs pull request #231: feat: re-export core and firmware crates via asic-rs features

> Source: https://github.com/256foundation/asic-rs/pull/231
> Collected: 2026-10-07
> Published: 2026-04-10

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 231
- State: closed
- Author: cfilipescu
- Opened: 2026-04-10
- Closed: 2026-04-10
- Labels: none

## Description

## Summary
- add a new `core` feature in `asic-rs` and re-export `asic_rs_core` as `asic_rs::core`
- re-export each firmware crate from `asic-rs` under the existing feature flags (for example `asic_rs::antminer`)
- keep users on a single dependency (`asic-rs`) while selecting firmware support with features
