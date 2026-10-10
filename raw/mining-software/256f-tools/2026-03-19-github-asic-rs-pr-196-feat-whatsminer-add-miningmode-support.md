# 256foundation/asic-rs pull request #196: feat(whatsminer): add MiningMode support via SupportsTuningConfig

> Source: https://github.com/256foundation/asic-rs/pull/196
> Collected: 2026-10-07
> Published: 2026-03-19

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 196
- State: closed
- Author: ankitgoswami
- Opened: 2026-03-19
- Closed: 2026-03-19
- Labels: none

## Description

## Summary

- Adds a `MiningMode` enum (`Low`, `Normal`, `High`) to `TuningTarget` in asic-rs-core, enabling discrete power mode control alongside the existing `Power` and `HashRate` targets
- Implements `SupportsTuningConfig` for WhatsMiner V2 and V3 backends, mapping `MiningMode` to the correct RPC commands (`set_low_power`/`set_normal_power`/`set_high_power` on V2, `set.miner.mode` on V3)
- Implements `parse_tuning_config` for both backends, reading the current mode from `power-mode` in the status summary (with fallback to `power-limit` for wattage-based miners)

## Context

Resolves https://github.com/256foundation/asic-rs/issues/190

WhatsMiner miners use discrete power modes (Low/Normal/High) rather than arbitrary wattage targets. Previously, `SupportsTuningConfig` returned `false` for all WhatsMiner backends, and the only power control available was `SetPowerLimit` which sets a wattage cap via `set.miner.power_limit`. This doesn't change the miner's actual power mode — the WhatsMiner web UI's Power Mode radio buttons (Low/Normal/High) remained unchanged.

The pyasic library handles this by sending `set_low_power`/`set_high_power`/`set_normal_power` RPC commands on the V2 API (port 4028). This PR brings equivalent functionality to asic-rs through the existing `SupportsTuningConfig` trait, keeping the API clean — callers just pass `TuningTarget::MiningMode(MiningMode::Low)` and the backend handles the protocol details.

## Test plan

- [x] Unit tests for `tuning_config_to_rpc` mapping (all three modes + power limit + hashrate rejection)
- [x] Unit tests for `parse_tuning_config` (power-mode field, power-limit fallback)
- [ ] Manual test against live WhatsMiner M60SVK40 (firmware 20251209.16.Rel2) — confirmed mode change via web UI

🤖 Generated with [Claude Code](https://claude.com/claude-code)
