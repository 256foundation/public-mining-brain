# 256foundation/asic-rs pull request #174: feat(core): add HashRateUnit string parsing

> Source: https://github.com/256foundation/asic-rs/pull/174
> Collected: 2026-10-07
> Published: 2026-03-14

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 174
- State: closed
- Author: cfilipescu
- Opened: 2026-03-14
- Closed: 2026-03-14
- Labels: none

## Description

## Summary
- Adds string parsing support for `HashRateUnit` in the core type layer.
- Keeps unit conversion/parsing logic centralized so future API/config inputs can accept human-readable hashrate unit values safely.
- This is needed groundwork for upcoming integrations where units will be received as strings (for example from config, CLI, or external payloads).
