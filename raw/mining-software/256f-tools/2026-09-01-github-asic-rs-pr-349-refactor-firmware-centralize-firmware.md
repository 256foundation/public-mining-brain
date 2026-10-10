# 256foundation/asic-rs pull request #349: refactor(firmware): centralize firmware display names

> Source: https://github.com/256foundation/asic-rs/pull/349
> Collected: 2026-10-07
> Published: 2026-09-01

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 349
- State: closed
- Author: Erisli
- Opened: 2026-09-01
- Closed: 2026-09-15
- Labels: none

## Description

## Summary
- Add a shared FirmwareType enum for firmware display names.
- Update firmware Display impls to use enum variants instead of raw string literals.
- Reuse FirmwareType in tuning-config unsupported-target messages for AntMiner and WhatsMiner.

## Validation
- cargo fmt
- cargo check *(blocked by existing lifetime-bound compiler limitation in asic-rs-core/src/traits/miner.rs:427)*

## Comments

### b-rowan on 2026-09-01

Sadly I don't think we can do this, the project started like this, but I want to allow people to extend with their own firmware types externally if needed, and centralizing on an enum for firmwares makes it impossible to extend...

Unless someone has a better idea?

My only thought is maybe it makes sense to have these names as constants inside the top level firmware crates?
