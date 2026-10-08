# 256foundation/asic-rs pull request #179: fix(python): silence type_complexity warnings in factory streams

> Source: https://github.com/256foundation/asic-rs/pull/179
> Collected: 2026-10-07
> Published: 2026-03-16

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 179
- State: closed
- Author: cfilipescu
- Opened: 2026-03-16
- Closed: 2026-03-16
- Labels: none

## Description

## Summary
- add targeted `#[allow(clippy::type_complexity)]` annotations for Python stream wrapper fields and constructors in `src/python/factory.rs`
- keep existing stream type signatures unchanged while making clippy output clean for `--all-targets --all-features --workspace`
- avoid broader/global lint suppressions by scoping allows to the specific complex stream declarations
