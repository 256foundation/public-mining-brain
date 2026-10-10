# 256foundation/asic-rs pull request #267: feat: add scaled tuning target support

> Source: https://github.com/256foundation/asic-rs/pull/267
> Collected: 2026-10-07
> Published: 2026-06-04

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 267
- State: closed
- Author: cfilipescu
- Opened: 2026-06-04
- Closed: 2026-06-05
- Labels: none

## Description

## Summary
- add scaled tuning target to MinerData and miner backend requirements
- implement default empty scaled tuning target support for existing backends
- parse ePIC PowerPlay scaled tuning target from the lower of Throttle Target and Error Throttle Target

## Tests
- cargo test -p asic-rs-firmwares-epic
- cargo check

## Comments

### cfilipescu on 2026-06-04

> Looks good, I'm assuming for scaled target since ePIC has both Error and Temp scaling possibilities you just are just parsing the lowest one

Yes. For now just putting both in there.
