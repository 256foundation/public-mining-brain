# 256foundation/asic-rs pull request #270: fix(epic): calculate v1 expected hashrate

> Source: https://github.com/256foundation/asic-rs/pull/270
> Collected: 2026-10-07
> Published: 2026-06-05

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 270
- State: closed
- Author: cfilipescu
- Opened: 2026-06-05
- Closed: 2026-06-08
- Labels: none

## Description

## Summary
- calculate ePIC v1 expected hashboard hashrate from chip count, hashes-per-clock capability, and average core frequency
- stop deriving expected hashrate from the reported actual/ratio array

## Tests
- cargo check -p asic-rs-firmwares-epic
