# 256foundation/asic-rs pull request #284: feat(vnish): implement SetPowerLimit (preset-based)

> Source: https://github.com/256foundation/asic-rs/pull/284
> Collected: 2026-10-07
> Published: 2026-06-18

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 284
- State: closed
- Author: pos-ei-don
- Opened: 2026-06-18
- Closed: 2026-06-19
- Labels: none

## Description

Closes #280.

VNish has no arbitrary-wattage power control — it exposes named, tuned autotune presets (each ~ a wattage) plus a throttle. So `set_power_limit(limit)` maps the requested watts to the **highest tuned preset whose power is `<= limit`** (same approach pyasic uses), sets `overclock.preset` to it and verifies the change. `supports_set_power_limit()` returns `true`.

- Adds two web helpers: `settings()` (GET) and `autotune_presets()` (GET).
- Preset power is parsed from the preset's `pretty` field (`"3495 watt ~ 132 TH"`); only `status == "tuned"` presets are considered. If no tuned preset fits under the limit, returns `Ok(false)` (no change).
- The existing `web.set_settings()` + verify path is reused.

**Throttle** (percent-of-full-power) is intentionally left out of `set_power_limit` — it's a separate axis; happy to propose it separately as a VNish-specific capability if there's interest.

### Tested
Live on an Antminer S19 Pro Hydro (VNish 1.3.3) via Home Assistant:
- `set_power_limit(3700 W)` → preset `3635` (highest tuned ≤ 3700)
- `set_power_limit(3500 W)` → preset `3495`

both applied and verified against the miner. (I don't have a local Rust toolchain, so I'm relying on CI for the build — happy to adjust anything.)

Context: we needed this for our own deployment but aren't asic-rs architects — please review/change/reject the approach as you see fit.

## Comments

### pos-ei-don on 2026-06-18

Good point. On VNish: **tuned** presets switch over more or less instantly; an **un-tuned** preset triggers a tuning cycle, i.e. effectively a restart before it settles. Right now the PR only picks the highest *tuned* preset ≤ target watts. I'll broaden it to consider **all** presets (tuned + un-tuned), picking the best ≤ watts and accepting the restart for un-tuned ones — same idea as Whatsminer always rebooting on a power-limit change.

On the integration side I'll also surface the miner's tuning state in its status text, so it's clear why the hashrate ramps after an un-tuned preset rather than looking like a fault. The miner's powered down at the moment, so I'll verify the un-tuned→restart behaviour on the S19 Pro Hydro and push the update shortly.


### b-rowan on 2026-06-18

> On the integration side I'll also surface the miner's tuning state in its status text, so it's clear why the hashrate ramps after an un-tuned preset rather than looking like a fault. The miner's powered down at the moment, so I'll verify the un-tuned→restart behaviour on the S19 Pro Hydro and push the update shortly.

Not 100% sure how to track this, I think we can use the `tuned` flag on the hashboards data structure to represent it.  Generally I think for most users this is expected behavior, but will get better in repeated setups using the same duplicated power limit over and over.  Fully "dynamic", rebootless tuning is a relatively new concept, so most people likely expect a reboot anyway, but I understand given the specifics of your setup why you would want to avoid reboots.

### pos-ei-don on 2026-06-19

Pushed the update so `set_power_limit` considers all presets, not just the tuned ones, and reads the wattage from the preset `name` instead of parsing `pretty`.

Verified it against my live S19 Pro Hydro (VNish 1.3.4) — the full `/autotune/presets` list:

- Every real preset has `name` = the bare watt integer, for both **tuned** (3495–5560) and **un-tuned** (5725–7700). Only `"disabled"` is non-numeric, and the `name.parse::<i64>().ok()` in the `filter_map` skips it.
- With the old `status == "tuned"` filter a target of e.g. 6000 W would silently cap at 5560 (the highest tuned preset); now it correctly selects 6000, which just kicks off a tuning cycle before it settles.

CI is recompiling now.
