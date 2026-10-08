# 256foundation/asic-rs pull request #277: fix(vnish): recognize spelled-out hydro model + per-board water temps + fluid temperature

> Source: https://github.com/256foundation/asic-rs/pull/277
> Collected: 2026-10-07
> Published: 2026-06-17

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 277
- State: closed
- Author: pos-ei-don
- Opened: 2026-06-17
- Closed: 2026-06-17
- Labels: none

## Description

## Problem

VNish-flashed hydro miners (e.g. Antminer S19 Pro Hydro, VNish 1.3.3) come back with **zero hashboards** and **no temperatures**.

**Root cause — model detection.** These miners report the model spelled out as `ANTMINER S19 PRO HYDRO`, but the only `S19ProHydro` serde alias is Bitmain's abbreviated `ANTMINER S19 PRO HYD.`. So the model parses to `Unknown`, whose default hardware profile has no board layout → `board_count()` is `None` → `parse_hashboards` builds zero boards (and `expected_hashboards` / chip counts come back `None`). The full `S19ProHydro` profile (`4×180`) already exists in `hardware.rs` — it just never gets selected. (`S19Hydro` already uses the spelled-out `ANTMINER S19 HYDRO`; the Pro/Plus and S21 hydro variants still use the abbreviated `HYD.` form and likely need the same for VNish — only the S19 Pro Hydro is verified here.)

**Secondary (hydro temperatures).** Per-board `intake_temperature`/`outlet_temperature` were both taken from `chip_temp/max`, ignoring the `inlet_water_temp`/`outlet_water_temp` the API reports per chain, and `GetFluidTemperature` was unimplemented.

## Fix

1. Add the spelled-out `ANTMINER S19 PRO HYDRO` alias so the existing `S19ProHydro` hardware profile is selected (boards + chip counts populate).
2. Map `inlet_water_temp` → `intake_temperature`, `outlet_water_temp` → `outlet_temperature`, falling back to `chip_temp/max` for air-cooled models.
3. Implement `GetFluidTemperature` as the warmest per-board `outlet_water_temp` (sourced from `/summary`, since `cooling` is empty in immersion/hydro mode).

## Validation

Verified against a live **Antminer S19 Pro Hydro (VNish 1.3.3)**: `/summary` returns 4 chains with `pcb_temp` / `chip_temp` / `inlet_water_temp` / `outlet_water_temp`. Before the change the model parsed to `Unknown` with 0 boards and `fluid_temperature = None`. I don't have a local Rust toolchain here, so I leaned on the existing patterns — happy to add a unit test or adjust on review.


## Comments

### pos-ei-don on 2026-06-17

Validated end-to-end against a live **Antminer S19 Pro Hydro (VNish 1.3.3)**: built a wheel from this branch and ran `MinerFactory().get_miner()` + `get_data()` against the miner.

- **Before:** 0 hashboards, `expected_hashboards = None`, `fluid_temperature = None` (model parsed to `Unknown`).
- **After:** model resolves to `S19ProHydro` (`expected_hashboards = 4`), **4 hashboards** populated with per-board water temps — `intake_temperature = inlet_water_temp`, `outlet_temperature = outlet_water_temp` (≈31–32 °C in / 44–46 °C out) — and `fluid_temperature = 46 °C` (warmest outlet). Per-board hashrates ≈35–37 TH/s.

All three changes confirmed working on real hardware.


### b-rowan on 2026-06-17

Perfect.  Can you fix the other issues from the comments and then should be good to merge.

### pos-ei-don on 2026-06-17

Thanks for the quick review! Addressed all of it:

1. **Board count from hardware vs API parsing** — agreed; the chain-id fallback is already removed in the current revision. The real fix is the model alias (below), so the existing `S19ProHydro` hardware profile (4×180) gets selected — no API-derived board count anymore.

2. **Why the profile wasn't picked up** — it's purely the model string. VNish reports `ANTMINER S19 PRO HYDRO` (spelled out), but the only `S19ProHydro` alias was Bitmain's abbreviated `ANTMINER S19 PRO HYD.`, so it parsed to `Unknown` → default profile → 0 boards. The profile itself was correct, it just wasn't being matched. Adding the spelled-out alias selects it.

3. **Other hydro types** — done. Added the spelled-out `… HYDRO` alias to S19 Pro+, S21, S21+ and S21E XP hydros as well (S19 Hydro already had it). Heads-up: only the S19 Pro Hydro is verified on real hardware here; the others follow the same `HYD.` → `HYDRO` pattern, so worth a sanity check if anyone has those on VNish.

4. **fluid_temperature** — switched to `inlet_water_temp` per your note (incoming / environment temperature).

I don't have a local Rust toolchain on this box, so I'm relying on CI for the build — happy to tweak anything else.


### pos-ei-don on 2026-06-17

Thanks for the fast review and merge! 🙏

I'll rebuild against `0.6.1` once it's tagged and re-confirm on the S19 Pro Hydro to make sure nothing regressed. The other hydro aliases (S19 Pro+/S21/S21+/S21E XP) are still unverified on real hardware on my side — if anyone shows up with one of those on VNish, happy to help sanity-check the `… HYDRO` aliases against an actual device.

Separately: VNish power/preset writes are still a stub in the VNish backend (`set_power_limit`). I've got a working REST-based path downstream and would be glad to open a PR to wire native VNish power-limit/preset writes into asic-rs if that's something you'd want — just say the word and I'll file an issue to scope it.
