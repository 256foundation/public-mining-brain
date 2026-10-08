# 256foundation/asic-rs pull request #223: fix(avalonminer): serialize ascset parameters as comma-separated string

> Source: https://github.com/256foundation/asic-rs/pull/223
> Collected: 2026-10-07
> Published: 2026-04-07

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 223
- State: closed
- Author: ankitgoswami
- Opened: 2026-04-07
- Closed: 2026-04-08
- Labels: none

## Description

## Summary

- The CGMiner RPC protocol expects the `parameter` field as a comma-separated string (e.g. `"0,led,1-1"`), not a JSON array (`["0","led","1-1"]`)
- All `ascset` commands were broken: LED control, soft-off/on, and power limit all failed with `"Missing device id parameter"`
- Fixed pause/resume response handling: `softoff` returns `STATUS:"S"` + `"ASC 0 set OK"` (not `"I"` + `"success softoff"`); `softon` closes the connection without responding and is now treated as success
- Consolidated the identical `rpc.rs` implementations from `avalon_a` and `avalon_q` into a single shared `backends/rpc.rs`

Verified against a live AvalonMiner 1466.

![fix](https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExbXRiNnYyc3NqMzNtdHJiN2RzdjgxeHhtNm11aWtvYXpxeWxiaTVjbyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3o7abKhOpu0NwenH3O/giphy.gif)

## Test plan

- [ ] Verify `ascset` LED command succeeds on a live AvalonMiner (`"ASC 0 set OK"`)
- [ ] Verify soft-off/on commands succeed
- [ ] Run unit tests: `cargo test -p asic-rs-firmwares-avalonminer`

🤖 Generated with [Claude Code](https://claude.com/claude-code)

## Comments

### ankitgoswami on 2026-04-07

testing setting pools etc

### ankitgoswami on 2026-04-07

added another fix for pause/resume. Everything else worked.
