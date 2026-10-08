# 256foundation/asic-rs pull request #289: feat(throttle): native manual throttle (SetThrottle + throttle_percent)

> Source: https://github.com/256foundation/asic-rs/pull/289
> Collected: 2026-10-07
> Published: 2026-06-22

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 289
- State: closed
- Author: pos-ei-don
- Opened: 2026-06-22
- Closed: 2026-06-24
- Labels: none

## Description

First off — thank you for 0.7.0 with native VNish tuning. That's exactly the foundation I was hoping for: it lets me drop my REST shims and source the control from asic-rs the way you laid out in your review.

Forward-porting my 0.6.x additions onto your 0.7 line was already a good chunk of work on my side — but I think it's the more important investment, so that's where I'm putting the effort: contributing what I need back here as proper library code instead of carrying patches. Starting with this one — native throttle. Native named-preset listing and the configured thermal-limit fields come next, and I'm happy to shape them to fit your model (the preset side in particular has a design question I'd value your input on).

On the Home Assistant integration itself, let me be straight: it now does everything I need — I've reached the goals I had for it, so I'm not putting much more into it. Splitting the existing GUI into a clean series of separate upstream PRs would be a lot of work, and since it already does what I need, that's effort I'm not planning to put in — so I'm keeping it as a runnable alpha in my fork rather than opening integration PRs. Anyone who wants it can just install it, and you're very welcome to take any part of it that's useful.

Really appreciate the work you've put into asic-rs.

---

**What this PR adds**
- `SetThrottle` control trait (`set_throttle(percent)` / `supports_set_throttle`, default `false`), wired into `HasMinerControl` next to `SetPowerLimit`.
- `GetThrottle` + `MinerData.throttle_percent` (100 = unthrottled), wired into `GetMinerData`; new `DataField::Throttle`.
- VNish v1.2.0 impl: reads `/summary` `miner_status/throttled`; writes `POST /mining/throttle` (clamped 20..=100).
- Python bindings (`Miner.set_throttle`/`get_throttle`/`supports_set_throttle`, `MinerData.throttle_percent`) + `.pyi`.
- Trivial default impls for the other backends (supertrait bound).

Tested against an S19 Pro Hydro (VNish): read path verified live; CI green (`cargo test --all` + Python tests).


## Comments

### b-rowan on 2026-06-22

Trying to understand what exactly this does...

Seems like it is essentially a scalar on top of the preset tuning target?  Can you help me understand why this is needed?  My preference would be that a use sets a new target power value rather than this, especially since that is already standardized across firmwares...

We already have the concept of a `TuningTarget` and `scaled_tuning_target`, which might be a better place to put the throttled back power, but just trying to understand better what this is and how best to fit it into the ecosystem.

### pos-ei-don on 2026-06-22

Good questions — happy to clarify.

You're right that it's a scalar on top of the active preset. The key point is that on VNish it's a *different operation* from setting a power target: `set_power_limit` selects an overclock preset, which kicks off a tune/reboot cycle (minutes, disruptive). The throttle (`POST /mining/throttle`) is an instant, reversible % de-rate of whatever preset is currently running — no re-tune, no reboot. So it isn't really "set a new target" so much as "run the current target at X% for now". The use case is quick demand-response / evening power reduction without paying a tuning cycle every time you nudge it.

I think you're spot on that the *resulting* (throttled-back) power belongs in `scaled_tuning_target` — I'm happy to populate that from the throttle so it reads consistently with the rest of the ecosystem (and reconsider the standalone `throttle_percent` field if that's cleaner).

The real open question is where the *setter* should live. Options I see:
1. a dedicated `set_throttle(percent)` (what this PR does),
2. fold it into the scaling concept — a `ScalingConfig`/scale-factor write — since it really is a scaling operation,
3. or whatever fits your mental model best.

I don't have a strong attachment to the trait shape; I'd rather fit it to your design. Which direction would you prefer? Happy to rework the PR accordingly.


### b-rowan on 2026-06-22

Tough part for me is that this doesn't fit cleanly into `SetScalingConfig`, since that is used more for automatic scaling (think scaling the miner back when it is overheating, etc), but it fits well with `scaled_tuning_config`.  Whatsminers have a similar concept to this, which I have neglected to implement yet given the complexity...

Curious what the rest of the team thinks, maybe they have better ideas.

### pos-ei-don on 2026-06-22

Agreed — `SetScalingConfig` is the wrong home for this, the automatic-scaling semantics don't match. `scaled_tuning_target` is exactly right: the throttle is a scalar on top of the active preset, so the read-back fits the `scaled_tuning_target` you already have on epic/braiins. I'm happy to wire the VNish read into that rather than carrying it separately.

For the set side I'd rather follow whatever shape you land on for tuning targets (this overlaps with the preset discussion in #291) instead of inventing a parallel path. And since WhatsMiners share the concept, it seems worth settling on one abstraction that covers both — glad to do the VNish part once the team has a direction.

No rush on my end; I can hold this PR open until that's settled.

### cfilipescu on 2026-06-23

@pos-ei-don have you tried the ePIC firmware? It has power tune, and it will guarantee the power within 30sec of changing it. also a lower dev fee

### b-rowan on 2026-06-23

I'll do more talking with the team, but tempted to decline this for now based on a couple things:
1. Power tuning seems like the much more user friendly way to do this, so setting a power limit and having it tune dynamically is a much better option in my opinion, and this adds a lot of complexity on top of that which I would like to abstract away from the user.
2. This feels like a firmware issue, ideally the firmware manufacturers would do a better job of handling this by just tuning dynamically, and AFAIK VNish, Braiins, LuxOS, and ePIC all should do it.
3. Some firmwares may only do this on tuned profiles, but once #291 is merged (a much better fit for asic-rs IMO), you can check `tuned` if needed before setting a profile, which I think is a much better user flow.

### pos-ei-don on 2026-06-23

Totally fair — no objection to declining it here. For context though, since I rely on this **daily**: the throttle isn't a replacement for power-target tuning, it's a fast, linear, *external-signal* power lever, and a couple of things it does that tuning doesn't:

- **It improves efficiency.** Throttling to ~90% actually lowers my W/TH — so it's an efficiency knob, not just a power cut.
- **Speed + linearity.** It adjusts within seconds and proportionally, which opened up a whole new world for me: tracking **PV/solar generation** in real time. Re-tuning to a new power target each time is too slow and restarts the tuner, and the firmware can't do it on its own since it doesn't see the external (solar/battery) signal.

On the "firmware should handle it" point — VNish exposes this as a first-class, promoted firmware feature (the manual throttle endpoint), available in current firmware, so it's stable and not going away.

All that said, I agree it adds complexity and that presets (#291) + power targets cover the common cases well — so I'm happy to keep the manual throttle as a fork-local extra and not push it upstream. I'll keep using it either way. Thanks for taking it to the team.


### pos-ei-don on 2026-06-23

Thanks @cfilipescu — I haven't tried ePIC, and hadn't heard much beyond the name, but a guaranteed power target within 30s (and a lower dev fee) sounds genuinely interesting. Do you run it yourself? I'd love to hear more about how the power-tune behaves in practice — particularly how tightly and quickly it tracks a *changing* target, since fast power-following is exactly what I'm after.


### b-rowan on 2026-06-23

Ok, I think we have a workable solution to this now, I think I want to change this to `tuning_percent` and `SetTuningPercent`, I think it is a better naming scheme across different types, and it needs to be able to stack with scaling and tuning target.

### cfilipescu on 2026-06-23

> Thanks @cfilipescu — I haven't tried ePIC, and hadn't heard much beyond the name, but a guaranteed power target within 30s (and a lower dev fee) sounds genuinely interesting. Do you run it yourself? I'd love to hear more about how the power-tune behaves in practice — particularly how tightly and quickly it tracks a _changing_ target, since fast power-following is exactly what I'm after.

Full disclosure, I work for the company. This was a new feature in the latest firmware release, and it only works on S21 miners because the PSU has a power reading. We confirmed on multiple systems, and the power is within 50W of the set target. If you want more information, I can share my Telegram handle.

### pos-ei-don on 2026-06-24

Two things:

The manual throttle endpoint is now officially documented in the VNish **1.3.4** OpenAPI — I added that schema as `meta/vnish/v1.3.4` in #297. It's `POST /mining/throttle` with `ThrottleSettings { percent: 20–100 }`, so it's a stable, first-class firmware endpoint (promoted feature, not going away).

On the rename: agreed — `tuning_percent` / `SetTuningPercent` is a cleaner cross-firmware name. Happy to rework it that way and make it stack with scaling and the tuning target. I'll push the rename + stacking.

### pos-ei-don on 2026-06-24

Thanks — yes, I'd love your Telegram handle.

This is genuinely interesting to me. The first thing I'd want to figure out is whether I can even try it on my hardware: I run an **S19 Pro Hydro** (water-cooled). I see PowerPlay is open source — `epicblockchain/powerplay-antminer` lists the S19 series, but I don't see the **Hydro** variant called out, so I'm not sure it's supported there.

And did I understand correctly that the new power-target feature is **S21-only for now** because it relies on the PSU exposing a power reading? If the blocker is purely that PSU power telemetry, could it be ported to S19-class hardware where the PSU exposes it? Since the firmware is open source, that might even be something I'd be happy to help contribute.

### pos-ei-don on 2026-06-24

Renamed as requested: `SetThrottle`/`GetThrottle` → `SetTuningPercent`/`GetTuningPercent`, `throttle_percent` → `tuning_percent`, `DataField::Throttle` → `TuningPercent` (core + all backends + python bindings + `.pyi`). CI is green.

On stacking: `tuning_percent` applies *on top of* the active tuning — on VNish the manual throttle is a linear % cap over whatever the tuner/preset is targeting, so it composes with the scaling config and tuning target rather than replacing them. The wire call (`POST /mining/throttle`, now documented in #297) is unchanged. If you had a more specific data-model shape in mind for how it should surface alongside `scaled_tuning_target`, happy to adjust.

### cfilipescu on 2026-06-24

> Thanks — yes, I'd love your Telegram handle.
> 
> This is genuinely interesting to me. The first thing I'd want to figure out is whether I can even try it on my hardware: I run an **S19 Pro Hydro** (water-cooled). I see PowerPlay is open source — `epicblockchain/powerplay-antminer` lists the S19 series, but I don't see the **Hydro** variant called out, so I'm not sure it's supported there.
> 
> And did I understand correctly that the new power-target feature is **S21-only for now** because it relies on the PSU exposing a power reading? If the blocker is purely that PSU power telemetry, could it be ported to S19-class hardware where the PSU exposes it? Since the firmware is open source, that might even be something I'd be happy to help contribute.

Sadly we don't support hydro systems right now, but if I can get remote access to a system, I can add it. Yes that is correct if you put a PSU that supports power it would work. At this time the FW code is not open sourced. my telegram handle is @cfilipescu

### b-rowan on 2026-06-24

> On stacking: `tuning_percent` applies _on top of_ the active tuning — on VNish the manual throttle is a linear % cap over whatever the tuner/preset is targeting, so it composes with the scaling config and tuning target rather than replacing them. The wire call (`POST /mining/throttle`, now documented in #297) is unchanged. If you had a more specific data-model shape in mind for how it should surface alongside `scaled_tuning_target`, happy to adjust.

Having seen #297, and that it doesn't exist in 1.2.x, can you move the implementation for this version to a new `v1_3_0` implementation and do version checks in the new to swap between them, then reset the 1.2.0 implementation to not contain this?  Helps us keep things accurate to what a type actually supports.

### pos-ei-don on 2026-06-24

Done — pushed the split in `8bc856a`:
- new `VnishV130` backend carrying `tuning_percent`
- `VnishV120` reset to trait defaults (`supports_set_tuning_percent() → false`, no `TuningPercent` data location, no `throttle()` endpoint)
- constructor routes on detected fw version (`>= 1.3.0 → V130`, else `V120`), following the braiins pattern

One thing I want to flag before we settle on this, though. `VnishV130` is a ~99% copy of `VnishV120` — the only real delta today is the one `supports_set_tuning_percent()` bool, one data location, and one web endpoint. That's ~1.3k duplicated lines for a single method, and we'd repeat that for every minor firmware bump that adds one capability — with the usual double-maintenance/divergence cost.

What makes me hesitate specifically here: the capability query is instance-level (`fn supports_set_tuning_percent(&self) -> bool`), not type-level. So a single version-aware backend that stores the detected version and gates on it —
```rust
fn supports_set_tuning_percent(&self) -> bool { self.version >= Version::new(1, 3, 0) }
```
— gives every consumer exactly the right answer too, in ~15 lines instead of a full backend copy. That seems to satisfy "accurate to what it supports" without the duplication. The full split clearly wins once a version genuinely diverges (like braiins did across GraphQL schemas), but vnish isn't there yet.

I've pushed the split since that's what you asked for and it's ready to merge — but do you actually want the per-version backend copy here, or would you prefer the instance-level gate while the delta is this small? Happy either way.

Side note: the `1.3.0` cutoff is an assumption (`1.3.4` verified live, `1.2.x` API has no throttle endpoint) — if you have a source for the exact version it landed, I'll pin it.

### b-rowan on 2026-06-24

Looks good, needs merge conflicts fixed, and may need updates for #293 (or in it), but good to go.

### pos-ei-don on 2026-06-24

Rebased onto current master (v0.7.1) and resolved the conflicts. Also did the #293 follow-up you flagged: since `MinerAuth` is now an enum, I regenerated `v1_3_0` from the updated `v1_2_0` so it uses the new auth accessors (no stale struct fields). Squashed to a single commit while I was at it.

CI green (Cargo + Python).
