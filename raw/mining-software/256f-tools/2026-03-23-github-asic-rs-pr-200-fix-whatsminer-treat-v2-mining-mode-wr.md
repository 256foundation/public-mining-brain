# 256foundation/asic-rs pull request #200: fix(whatsminer): treat V2 mining mode write timeouts as success

> Source: https://github.com/256foundation/asic-rs/pull/200
> Collected: 2026-10-07
> Published: 2026-03-23

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 200
- State: closed
- Author: ankitgoswami
- Opened: 2026-03-23
- Closed: 2026-03-23
- Labels: none

## Description

## Summary

V2 mining mode commands (`set_low_power`, `set_normal_power`, `set_high_power`) and `power_off` always timeout because the miner applies the change without sending a response. Previously this was masked by the `read_to_end` hang (the call would block forever); with bounded reads, these now surface as timeout errors.

### What changed

- **`set_tuning_config`**: mining mode writes that fail with a timeout, connection reset, or broken pipe are treated as success (the miner applied the change). Power limit writes still propagate errors since not all miners support custom power limits.
- **`pause`** (`power_off`): fire-and-forget — miner may power off before responding.
- **`is_expected_write_error()`**: helper that identifies transient write failures via `std::io::ErrorKind` downcasting (connection reset, broken pipe, connection aborted) and timeout string matching.

### Why only mining modes?

Live testing confirmed:
- `set_low_power` / `set_normal_power` / `set_high_power` → always timeout, but read-back confirms the change was applied
- `adjust_power_limit` → also timeouts on some miners, but some V2 miners don't support custom power limits at all (Power Limit always reads 0). Treating timeout as success would give false positives.

## Test plan

- [x] `cargo check` / `cargo clippy` — clean
- [x] `cargo test` — all unit tests pass
- [x] Live V2 miner: mining mode set returns `Ok(true)` despite timeout, read-back confirms mode changed
- [x] Live V3 miner: mining mode V2 fallback returns `Ok(true)`, full round-trip verified

🤖 Generated with [Claude Code](https://claude.com/claude-code)

## Comments

### ankitgoswami on 2026-03-23

ended up fixing this in https://github.com/256foundation/asic-rs/pull/199
