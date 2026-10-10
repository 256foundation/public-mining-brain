# 256foundation/asic-rs pull request #194: feat(whatsminer): implement SupportsTuningConfig with V2 fallback for mining modes

> Source: https://github.com/256foundation/asic-rs/pull/194
> Collected: 2026-10-07
> Published: 2026-03-19

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 194
- State: closed
- Author: ankitgoswami
- Opened: 2026-03-19
- Closed: 2026-03-20
- Labels: none

## Description

## Summary

Implements `SupportsTuningConfig` for both WhatsMiner V2 and V3 backends — adding discrete power mode support (Low / Normal / High) alongside continuous power limit targets. On V3 miners where `set.miner.mode` returns "invalid command", the backend automatically falls back to the V2 API on port 4028.

![Plan B](https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExZG1rOXQwbjRhYXdxeHZxb3BqcW1hdWt3b2d1M2o2cnQyMDIwbTU5dSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/xUNd9I9MbPzsWADjCU/giphy.gif)

### Why

WhatsMiner firmware exposes power modes as discrete operating profiles separate from continuous wattage limits. The existing `TuningConfig` system only handled numerical power targets. Some V3 miners (confirmed on M60S_VK40, firmware 20251209.16.Rel2) don't support `set.miner.mode` via the V3 RPC API but still accept the V2 per-mode commands (`set_low_power` / `set_normal_power` / `set_high_power`) on port 4028.

### What changed

- **Core**: new `MiningMode` enum (Low/Normal/High) and `TuningTarget::MiningMode` variant, with Python bindings
- **V2 backend**: full `SupportsTuningConfig` impl — `set_tuning_config` (per-mode commands + `adjust_power_limit`), `parse_tuning_config` (reads `Power Mode` / `Power Limit` from summary), `get_configs_locations`
- **V3 backend**: full `SupportsTuningConfig` impl — tries V3 `set.miner.mode` first, falls back to V2 RPC only when the miner responds with an error (not on connection/deserialization failures). Parses `power-mode` / `power-limit` from status summary
- **V3 struct**: gains a `v2_rpc` field (V2 RPC client on port 4028) for the fallback path
- **V2 `tuning_config_to_rpc`**: made `pub(crate)` so V3 reuses it for the fallback instead of duplicating the mode→command mapping

### Fallback flow

```
set_tuning_config(MiningMode::Normal)
  → V3: set.miner.mode "normal" (port 4433)
    → Success? Ok(true)
    → RPCError? Fall back to V2: set_normal_power (port 4028)
    → Connection/other error? Propagate Err
```

## Test plan

- [x] `cargo check` / `cargo clippy` — clean
- [x] `cargo test` — 21 tests pass, covering: mode→command mappings (V2+V3), power limit, hashrate rejection, parse with mode present, parse with empty mode falling back to limit
- [x] Live V2 miner: `get_tuning_config()` returns `MiningMode(Low)` ✓

## Known limitation

The V2 RPC client's `read_to_end()` blocks on privileged commands because the miner doesn't close TCP connections after responding. This is a pre-existing issue affecting all V2 write commands, not introduced here.

Closes #190

🤖 Generated with [Claude Code](https://claude.com/claude-code)

## Comments

### b-rowan on 2026-03-19

Concept is great, and seems well implemented, but of course the manufacturer has to throw a wrench in there somewhere.  Ill see what I can get for real results to test against.

### b-rowan on 2026-03-20

I am very sorry to say you have picked an absolute doozy here.  Distinguishing power mode from power limit on V3 is painful, but possible, but for the V2 API I have absolutely 0 clue how we are going to tell them apart.  Definitely need some input from the rest of the team on this one.

### b-rowan on 2026-03-20

Approved, but want to confirm how we should be using the V2/V3 API combination prior to merging.
