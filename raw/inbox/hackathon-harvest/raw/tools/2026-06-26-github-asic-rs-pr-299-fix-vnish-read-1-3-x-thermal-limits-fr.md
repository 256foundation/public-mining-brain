# 256foundation/asic-rs pull request #299: fix(vnish): read 1.3.x thermal limits from /settings, not /summary

> Source: https://github.com/256foundation/asic-rs/pull/299
> Collected: 2026-10-07
> Published: 2026-06-26

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 299
- State: closed
- Author: pos-ei-don
- Opened: 2026-06-26
- Closed: 2026-06-26
- Labels: none

## Description

## What

The VNish `v1_3_0` backend read its `TemperatureConfig` (`ConfigField::Temperature`) from `/summary`, pointing at `/miner`. On VNish 1.3.x the public `/summary` was slimmed down — `miner.misc` (which holds `restart_temp`) is gone, and `miner.cooling` no longer carries `min_startup_water_temp`. As a result both `danger` (self-protection restart temperature) and `minimum` (min startup water temp) come back `None` on 1.3.x firmware.

This PR reads the thermal config from the authenticated `/settings` endpoint — the canonical config source, where both values still live — and keeps `/summary` as a fallback. The misleading doc comment on `parse_temperature_config` is corrected.

## Why this slipped through

Apologies — this one is on me. The thermal-limits feature was originally written to read from `/settings` (correct), but somewhere in the churn of porting it across the 0.6.x → 0.7.0 → preset/throttle/v1.3.0-split branches, the source got "simplified" back to `/summary` and the supporting comment followed. Maintenance across all those parallel branches clearly slipped here. I caught it while testing the current `0.7.1` against a live miner whose firmware had since moved to 1.3.4.

## Scope / blast radius

I went through every `/summary`-sourced field in the `v1_3_0` backend against a live 1.3.4 `/summary`:

| Field | Source pointer | 1.3.4 `/summary` | Status |
|---|---|---|---|
| Temperature (restart/min-startup) | `/miner/misc`, `/miner/cooling/min_startup_water_temp` | **gone** | **fixed here** |
| Hashrate, ExpectedHashrate, Wattage, Fans, Hashboards, Pools, Fluid/OutletFluid temps, Messages, TuningPercent | various | still present | OK |

`miner.overclock` was also dropped from 1.3.x `/summary`, but the backend already sources preset / power-limit data from the authenticated endpoints (`/settings`, `/autotune/presets`), so nothing else is affected. The thermal config is the only casualty.

## Verification

- Live VNish 1.3.4 (S19 Pro Hydro): `GET /api/v1/summary` has no `miner.misc`; authenticated `GET /api/v1/settings` returns `miner.misc.restart_temp = 78` and `miner.cooling.min_startup_water_temp = 17`.
- `v1_3_0` only serves firmware `>= 1.3.0` (per the backend version routing), so `/settings` is always the right source for this backend; the `/summary` fallback is purely defensive.
- CI: tests green on the branch.

Routing note: `/settings` is already used by `set_power_limit` in this backend, so the authenticated path is exercised and unchanged.

## Comments

### pos-ei-don on 2026-06-26

Closing — opened against the wrong repo by mistake. Handling this on our fork for now.
