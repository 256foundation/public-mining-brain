# 256foundation/asic-rs pull request #193: feat(whatsminer): add MiningMode support via SupportsTuningConfig

> Source: https://github.com/256foundation/asic-rs/pull/193
> Collected: 2026-10-07
> Published: 2026-03-19

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 193
- State: closed
- Author: ankitgoswami
- Opened: 2026-03-19
- Closed: 2026-03-19
- Labels: none

## Description

## Summary

Implements discrete power mode support (Low / Normal / High) for WhatsMiner miners, resolving #190.

WhatsMiner firmware exposes power modes as discrete operating profiles separate from continuous wattage limits. The existing `SetPowerLimit` and `TuningConfig` traits handle numerical targets (e.g., "cap at 3000W"), but cannot represent firmware-level mode selection. Per discussion with maintainers, this is implemented within the existing `SupportsTuningConfig` system rather than as a separate trait.

### What this PR adds

**Core types** (`asic-rs-core/src/data/miner.rs`):
- New `MiningMode` enum (`Low`, `Normal`, `High`) with `pyclass` support for Python bindings
- New `TuningTarget::MiningMode(MiningMode)` variant

**WhatsMiner V3 backend** (`whatsminer/src/backends/v3/mod.rs`):
- `set_tuning_config`: sends `set.miner.mode` RPC with `"low"` / `"normal"` / `"high"` param; also handles `Power` target via `set.miner.power_limit`
- `parse_tuning_config`: reads `power-mode` from status summary (falls back to `power-limit` when absent)
- `get_configs_locations`: maps `ConfigField::Tuning` → `get.miner.status` summary
- Pure `tuning_config_to_v3_rpc()` helper extracted for unit testing

**WhatsMiner V2 backend** (`whatsminer/src/backends/v2/mod.rs`):
- `set_tuning_config`: sends per-mode privileged commands (`set_low_power`, `set_normal_power`, `set_high_power`); also handles `Power` target via `adjust_power_limit`
- `parse_tuning_config`: reads `Power Mode` / `Power Limit` from summary response (same RPC command as `DataField::TuningTarget`)
- `get_configs_locations`: maps `ConfigField::Tuning` → `summary` RPC
- Pure `tuning_config_to_rpc()` helper extracted for unit testing

**Python bindings** (`src/python/data.rs`):
- Compile maintenance — adds `MiningMode` variant to Python `TuningTarget` enum and `From` conversion

**Fixture update** (`whatsminer/src/test/json/v2/status.json`):
- Updated with real API response captured from a live V2 miner (now includes `power_mode` and `power_limit_set` fields)

### Design decisions

- **`TuningTarget::MiningMode` variant** (not a separate `SetPowerMode` trait): Per maintainer guidance, power modes belong in the tuning config system. This keeps the trait surface small and reuses existing `get_tuning_config()` / `set_tuning_config()` infrastructure.
- **Explicit `HashRate(_)` match arm** instead of `_` wildcard: Ensures future `TuningTarget` variants produce compile errors rather than silent fallthrough.
- **`parse_tuning_config` reads from `summary`**, not `status`: The V2 `status` response has unreliable `power_mode` (often empty) and no power limit field. The `summary` response has both `Power Mode` and `Power Limit` and is already used for `DataField::TuningTarget`.
- **`supports_tuning_config() -> true`** on both V2 and V3: Both backends now support the full read/write contract.

### How callers use this

```rust
// Set mining mode
let config = TuningConfig::new(TuningTarget::MiningMode(MiningMode::Low));
miner.set_tuning_config(config).await?;

// Read current config
let config = miner.get_tuning_config().await?;
match config.target {
    TuningTarget::MiningMode(mode) => println!("Mode: {mode}"),
    TuningTarget::Power(watts) => println!("Power limit: {watts}"),
    _ => {}
}
```

## Test plan

- [x] `cargo check` — all backends compile with new `TuningTarget` variant
- [x] `cargo check --features python` — Python bindings compile with `MiningMode` pyclass
- [x] `cargo clippy` — no warnings
- [x] `cargo test` — 21 tests pass (unit + integration), covering:
  - V3: all 3 mining modes → correct RPC command/param, power limit passthrough, hashrate rejection, parse with mode, parse fallback to power limit, V2 fallback mapping
  - V2: all 3 mining modes → correct V2 command names, power limit passthrough, hashrate rejection, parse with mode, parse empty mode fallback to limit
- [x] Live V2 miner (172.16.2.244): `get_tuning_config()` returns `MiningMode(Low)` ✓
- [ ] Live V3 miner with `set.miner.mode` support: not yet available for testing

## Known limitations

- **V2 write commands hang**: The V2 RPC client uses `read_to_end()` which blocks forever because the miner doesn't close TCP connections after responding. This is a pre-existing bug affecting all V2 privileged commands (`adjust_power_limit`, `set_led`, `reboot`, etc.), not introduced by this PR. Tracked separately.
- **Some V3 miners lack `set.miner.mode` RPC**: The command returns "invalid command" even though the web UI has power mode controls. These miners expose modes via LuCI CGI, not the RPC API. See stacked PR #2 for a V2 API fallback.

Closes #190
