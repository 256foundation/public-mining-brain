# 256foundation/asic-rs pull request #168: feat: replace wattage_limit with tuning_target enum

> Source: https://github.com/256foundation/asic-rs/pull/168
> Collected: 2026-10-07
> Published: 2026-03-12

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 168
- State: closed
- Author: cfilipescu
- Opened: 2026-03-12
- Closed: 2026-03-12
- Labels: none

## Description

## Summary
- replace `MinerData.wattage_limit` with `MinerData.tuning_target: Option<TuningTarget>`
- add `TuningTarget` enum with `Power(Power)` and `HashRate(HashRate)` variants
- map existing parsed wattage limits to `TuningTarget::Power` and update Python bindings/tests accordingly

## Comments

### cfilipescu on 2026-03-12

also i don't know if you want me to rename the trait from SetPowerLimit to SetPowerTarget
