# 256foundation/asic-rs pull request #251: fix(antminer-v2020): fix pause/resume on older stock firmware

> Source: https://github.com/256foundation/asic-rs/pull/251
> Collected: 2026-10-07
> Published: 2026-05-13

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 251
- State: closed
- Author: taserz
- Opened: 2026-05-13
- Closed: 2026-05-14
- Labels: none

## Description

## Summary

- Older Antminer stock firmware (e.g. S19j Pro Dec 2022) reports the work mode via `bitmain-work-mode` in `get_miner_conf` but `set_miner_conf` only responds to `miner-mode` — and on some builds that write silently no-ops, requiring a further fallback to `bitmain-work-mode`
- The previous implementation always wrote `bitmain-work-mode`, which did nothing on the affected firmware, leaving the miner stuck in its current mode
- Fix: try `miner-mode` first, verify by re-reading `get_miner_conf`, fall back to `bitmain-work-mode` if the write did not apply; skip the whole sequence if the miner is already in the target mode
- Also extends the `set_miner_conf` timeout floor to 35 s (some firmware takes >20 s to respond)

## Test plan

- [x] 10 new unit tests covering all pause/resume code paths via a minimal mock HTTP server
  - Already in target mode (both key variants) → returns `true` without making a POST
  - No mode key present → returns `false`
  - `miner-mode` write succeeds on first try → returns `true`
  - `miner-mode` write accepted (200) but does not apply; fallback to `bitmain-work-mode` succeeds → returns `true`
  - Mirror set for `resume()`
- [x] `cargo test -p asic-rs-firmwares-antminer pause_resume` — all 10 pass

Closes #245

## Comments

### b-rowan on 2026-05-14

Superseded by #249
