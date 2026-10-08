# 256foundation/asic-rs pull request #287: feat(vnish): surface miner_state as messages (self-managed alarm passthrough)

> Source: https://github.com/256foundation/asic-rs/pull/287
> Collected: 2026-10-07
> Published: 2026-06-19

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 287
- State: closed
- Author: pos-ei-don
- Opened: 2026-06-19
- Closed: 2026-06-22
- Labels: none

## Description

Surfaces the VNish miner's own state verdict as a `MinerMessage`, so consumers get the firmware's self-assessment instead of recomputing thresholds.

VNish self-manages its protection (it won't start mining below the configured `min_startup_water_temp`, and protects itself above `restart_temp`), so `parse_messages` reports any non-operating `miner_state` as a message: `Error` for `failure`/`stopped`-type states, `Warning` for transitional ones, and nothing for the normal operating states (`mining`, `tuning`/`auto-tuning` — tuning is deliberately not flagged so a ramping hashrate doesn't look like a fault).

Standalone and independent of the temperature work — verified live on an S19 Pro Hydro (VNish): `stopped` / `initializing` / `mining` come through correctly. I'm using it on the integration side to drive a clear safety-reason text.
