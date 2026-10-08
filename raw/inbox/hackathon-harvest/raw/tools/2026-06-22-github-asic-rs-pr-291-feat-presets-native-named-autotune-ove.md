# 256foundation/asic-rs pull request #291: feat(presets): native named autotune/overclock presets (SupportsPresets)

> Source: https://github.com/256foundation/asic-rs/pull/291
> Collected: 2026-10-07
> Published: 2026-06-22

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 291
- State: closed
- Author: pos-ei-don
- Opened: 2026-06-22
- Closed: 2026-08-31
- Labels: none

## Description

Third one — and this is the one with the design question I mentioned, so very much up for discussion.

VNish exposes *named* autotune presets (e.g. `"5560"` → `"5560 watt ~ 175 TH"`, tuned/untuned), and the use case is letting a user pick one by name and see the tuned-hashrate label, rather than only targeting a wattage. `set_power_limit` already picks the closest preset internally, but it never surfaces the *list* / *current name* / *apply-by-name* that a preset picker needs.

This PR adds:
- `SupportsPresets` trait: `get_presets() -> Vec<PresetInfo>`, `get_current_preset() -> Option<String>`, `set_preset(name) -> Result<bool>`, `supports_presets()` (default `false`), in the `Miner` supertrait.
- `PresetInfo { name, pretty: Option<String>, status: Option<String> }` — read-only `pyclass`.
- VNish impl via `/autotune/presets` (list) and `/settings` `miner.overclock.preset` (current + select).
- Python bindings + `.pyi`; trivial default impls for the other backends.

**Design question for you:** I modeled this as named presets because that's VNish's native concept, but I know it sits a bit outside the abstract `TuningTarget` (power/hashrate/mode) model you prefer. If you'd rather express "select preset X" as a `TuningTarget` variant (a `mode`/profile name?) and surface the resulting power via `scaled_tuning_target` — same family as the throttle discussion in #289 — I'm glad to reshape it that way. Tell me which direction fits, and I'll rework it.

CI is green (`cargo test --all` + Python tests).


## Comments

### b-rowan on 2026-06-22

I like the idea, very close in concept to what I think the ideal setup is.

My only change would be to move the setter into `SetTuningConfig`, since technically this is a type of tuning config, and to move `get_current_preset` to be a value coming from `get_tuning_target`, since it fits better there.

Then you can keep `get_presets` and `supports_presets` under `SupportsPresets`, whilst cleanly integrating the presets with existing norms.

With this method, the flow becomes:
1. `miner.supports_presets`?
2. `miner.get_presets`,
3. Select the desired preset,
4. `miner.set_tuning_target`

The one thing we might want to pursue further is integrating more information about what TYPES of tuning target the miner supports, EG `supports_power_tuning_target`, `supports_hashrate_tuning_target`, and `supports_preset_tuning_target`.

### pos-ei-don on 2026-06-22

That's a clean fit — thanks. I'll rework it along those lines:

- keep `get_presets` + `supports_presets` in `SupportsPresets` (the list + capability),
- move the setter to `set_tuning_config` via a new `TuningTarget::Preset(name)` variant,
- and surface the current one through `get_tuning_target`.

So the flow becomes exactly `supports_presets?` → `get_presets` → `set_tuning_target`. The `supports_power/hashrate/preset_tuning_target` capability flags are a good idea too — I'll factor that in. Since this touches `TuningTarget` and overlaps with the throttle discussion in #289 (same model), I'll do it carefully and verify against a live miner before pushing the rework.


### b-rowan on 2026-06-23

Could you implement this for luxos as well, following their docs here

https://docs.luxor.tech/firmware/api/luxminer/profiles
https://docs.luxor.tech/firmware/api/luxminer/profileset

### pos-ei-don on 2026-06-24

On the VNish side I'll do the rework as discussed — move the setter into `SetTuningConfig` via a `TuningTarget::Preset(name)` variant, keep `get_presets`/`supports_presets`, and surface the current preset through `get_tuning_target`.

For luxos, though — I don't have any Luxminer hardware, and everything I've contributed so far I've verified live against my own miners. I'd rather not ship a luxos backend I can't actually run and test. Happy to keep the trait shape clean so someone with a Luxminer can add it as a follow-up, but I don't want to push code blind. Hope that's fair.

### pos-ei-don on 2026-06-24

Pushed the rework (`f1f77d8`, rebased onto v0.7.1):

- selecting a preset now goes through `set_tuning_config` via a new `TuningTarget::Preset(name)` variant
- the active preset is surfaced through `get_tuning_target`
- `SupportsPresets` keeps just `get_presets` + `supports_presets`

Other backends get a `Preset` arm in their tuning matches (unsupported → bail). CI green (Cargo + Python).

(luxos still out of scope for me, as noted above — no Luxminer hardware to verify against.)

### pos-ei-don on 2026-08-30

Rebased onto v0.8.0 — the throttle/thermal/power-target/auth commits this branch carried are in the release now, so they dropped out on rebase; re-integrated the preset trait registration next to the new SupportsScalingConfig, merged the generated stub, and added an empty SupportsPresets impl for the new elphapex backend. cargo check is green.
