# 256foundation/asic-rs pull request #292: feat(power): expose factory default / min / max power target

> Source: https://github.com/256foundation/asic-rs/pull/292
> Collected: 2026-10-07
> Published: 2026-06-23

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 292
- State: closed
- Author: pos-ei-don
- Opened: 2026-06-23
- Closed: 2026-06-23
- Labels: none

## Description

Surfaces the power target a miner ships with — plus the accepted min/max bounds. On BraiinsOS this is the value the **tuner starts from**: when you kick off a fresh tune, the autotuner anchors on this default power target and works out from there. Exposing it lets a UI offer the factory point as the natural starting step for a fresh (re-)tune, and present a realistic range around it instead of guessing.

- Adds `DefaultPowerTarget` / `MinPowerTarget` / `MaxPowerTarget` data fields and matching `Option<Power>` fields on `MinerData`, wired in through the usual `Get*` traits (default to `None`) so every backend keeps compiling unchanged.
- Braiins 26.04: reads `bosminer.metadata.autotuning.powerTarget.{default,min,max}` over the GraphQL client that's already there (unauth metadata, no extra auth path). On an S19k Pro this gives 2760 / 771 / 6435 W.
- All other backends get trivial `None` impls. I only wired Braiins 26.04 because that's the firmware I can test against live; the other BOS backends expose the same GraphQL field, so mirroring it later is straightforward.

Happy to reshape this — e.g. group the three into a small struct, or fold it into the tuning/config model if that fits your direction better. Verified live against a BraiinsOS S19k Pro.


## Comments

### b-rowan on 2026-06-23

Did some talking, and I think we want to wire this up under a "new" trait subsection, `MinerCapabilities`.  I believe the correct naming for this is `TuningCapabilities`, and I want to structure it as so - 

```rust
struct PowerTuningCapabilites {
    default: Option<TuningTarget>, 
    minimum: Option<TuningTarget>, 
    maximum: Option<TuningTarget>
}

struct HashRateTuningCapabilites {
    default: Option<TuningTarget>, 
    minimum: Option<TuningTarget>, 
    maximum: Option<TuningTarget>
}

struct PresetTuningCapabilites {
    default: Option<TuningTarget>, 
    presets: Vec<TuningTarget>
}

struct TuningCapabilities {
    power: Option<PowerTuningCapabilites>,
    hashrate: Option<HashRateTuningCapabilites>,
    presets: Option<PresetTuningCapabilities>,
}
```

### pos-ei-don on 2026-06-23

Done — reworked it into `TuningCapabilities` as you sketched, grouped by tuning domain and reusing the existing `TuningTarget`:

```rust
TuningCapabilities {
    power:    Option<PowerTuningCapabilities>,    // default / minimum / maximum
    hashrate: Option<HashRateTuningCapabilities>, // default / minimum / maximum
    presets:  Option<PresetTuningCapabilities>,   // default / presets
}
```

A couple of decisions where the sketch left room — happy to change either:
- **Value type:** reused `TuningTarget` for the fields (matches your snippet), so a power envelope is `TuningTarget::Power(..)` etc.
- **Where it lives:** I kept it on `MinerData` via a single `DataField::TuningCapabilities` + a `GetTuningCapabilities` trait, mirroring how `tuning_target` already works. If you'd rather have it as a standalone `capabilities()` call off the telemetry path, that's an easy move — just say the word.
- **Coverage:** `BraiinsV2604` fills `power.{default,minimum,maximum}` from the autotuning `powerTarget` metadata; `hashrate`/`presets` stay `None` until a backend exposes them (the `presets` arm lines up with the VNish work in #289).

CI is green. The three flat `*_power_target` fields/traits are gone, replaced by the single structured field.

### b-rowan on 2026-06-23

FYI you can use the files in `meta/` from the root as documentation for some of the APIs, if you feed them into your agent it should be able to implement this for most of the meta documented types.

### pos-ei-don on 2026-06-23

Done — implemented across all BOS backends, CI green:

- Dropped the `== default` guard.
- Two shared helpers in `backends/util.rs` (instead of literal copy-paste): `power_target_capabilities()` for the GraphQL `bosminer/metadata/autotuning/powerTarget` path (21.09 / 25.03 / 25.05), and `tuner_constraints_capabilities()` for the BOS+ REST `GET /configuration/constraints` → `tuner_constraints` (25.07 / 26.04), mapping `PowerConstraints` (watts) and `HashrateConstraints` (TH/s) onto the power + hashrate envelopes.
- 26.04 now uses the REST constraints endpoint instead of the GraphQL metadata query, and reports the hashrate envelope as well.

And it's verified on real hardware, not just CI/schema: tested against my S19k Pro on BraiinsOS. I actually had to fire the miner up on battery to do it (not enough solar at the time 🙂), but `/configuration/constraints` matches exactly — `power_target` = { default 2760 W, min 771 W, max 6435 W } and `hashrate_target` = { default 120 TH/s, min 11.36, max 268.46 }, which is what the helper maps onto the power/hashrate envelopes.

Thanks for the `meta/` schemas and the `constraints.proto` link — made the REST shapes unambiguous.
