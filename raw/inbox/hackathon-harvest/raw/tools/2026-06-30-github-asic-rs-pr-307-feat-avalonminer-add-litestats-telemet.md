# 256foundation/asic-rs pull request #307: feat(avalonminer): add litestats telemetry and support new Avalon models

> Source: https://github.com/256foundation/asic-rs/pull/307
> Collected: 2026-10-07
> Published: 2026-06-30

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 307
- State: closed
- Author: gzw13999
- Opened: 2026-06-30
- Closed: 2026-07-02
- Labels: none

## Description

## Summary
- Use `litestats` as the primary telemetry source for Avalon Q when `stats` returns empty `MM ID0:Summary` / `HBinfo`
- Add Summary + HBinfo parsing fallback to `AvalonAMiner` for industrial models such as 1566HA
- Register `15PRO`, `1566HA`, and `1566HU` model aliases with hydro-cooled hardware profiles
- Parse summary-format wattage from `WALLPOWER` or `PS` array slots (indices 4 and 5)
- Map `ITemp` / `HBOTemp` to fluid temperature fields for hydro-cooled devices
## Motivation
Several Avalon deployments only reported hashrate and wattage while temperature and fan data were missing. Root causes included:
1. Unknown model strings (`15PRO`, `1566HA`, `1566HU`) resulting in zero expected boards/fans
2. Avalon Q firmware exposing telemetry via `litestats` while `stats` Summary remains empty even while mining
3. 1566HA using Summary + HBinfo stats format instead of classic `MM ID0`
## Changes
- **Avalon Q**: collect summary telemetry from both `stats` and `litestats`; keep `HBinfo` chip data on `stats` only
- **Avalon A**: detect Summary format and reuse shared parsing helpers
- **Models / hardware**: add `15PRO`, `1566HA`, `1566HU`; 1566HA = 4 boards, 1566HU = 3 boards, both hydro (`fans: 0`)
- **Tests**: empty-stats + litestats fixture, summary-format hashboards, wattage-only collection
## Test plan
- [x] `cargo test -p asic-rs-firmwares-avalonminer -p asic-rs-makes-avalon`
- [x] `cargo clippy -p asic-rs-firmwares-avalonminer -p asic-rs-makes-avalon -- -D warnings`
- [x] Verified on live hardware: Avalon Q, 1566HA, 1566HU, 15 Pro
