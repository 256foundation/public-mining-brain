# 256foundation/asic-rs pull request #269: feat: parse control boards from data values

> Source: https://github.com/256foundation/asic-rs/pull/269
> Collected: 2026-10-07
> Published: 2026-06-05

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 269
- State: closed
- Author: cfilipescu
- Opened: 2026-06-05
- Closed: 2026-06-08
- Labels: none

## Description

## Summary
- implement FromValue for make control board hardware enums
- allow ePIC PowerPlay control board parsing from platform data with existing CPU fallback
- add Marathon serde_json dependency needed for FromValue signature

## Tests
- cargo check
- cargo test -p asic-rs-makes-antminer -p asic-rs-makes-epic -p asic-rs-makes-sealminer -p asic-rs-makes-auradine -p asic-rs-makes-bitaxe -p asic-rs-makes-braiins -p asic-rs-makes-nerdaxe -p asic-rs-makes-avalon -p asic-rs-makes-marathon -p asic-rs-makes-whatsminer
