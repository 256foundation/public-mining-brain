# 256foundation/asic-rs pull request #290: feat(temp): configured thermal limits (min_startup/restart_temperature)

> Source: https://github.com/256foundation/asic-rs/pull/290
> Collected: 2026-10-07
> Published: 2026-06-22

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 290
- State: closed
- Author: pos-ei-don
- Opened: 2026-06-22
- Closed: 2026-06-23
- Labels: none

## Description

Surfaces the miner's configured thermal limits — modeled as a **config** (mirroring the Braiins OS layout / your `ScalingConfig` pattern), per your review feedback.

- `config::temperature::TemperatureConfig { target, hot, danger, minimum }` — all `Option<f64>`, where `None` means *the firmware does not report this threshold* (not "no limit").
- `SupportsTemperatureConfig` trait (`get_temperature_config` / `set_temperature_config` / `supports_temperature_config`), wired into `SupportsConfigs`.
- VNish: reads `/summary` — `minimum` (`cooling.min_startup_water_temp`) + `danger` (`misc.restart_temp`). `target`/`hot` aren't exposed via `/summary`, so they stay `None`.
- Python bindings (`Miner.get_temperature_config` / `supports_temperature_config`) + `TemperatureConfig` export; `.pyi`. Trivial default impls for the other backends.

CI green (`cargo test --all` + Python tests).


## Comments

### b-rowan on 2026-06-22

This one I have a bit more insight on, I have implemented this concept once already (https://github.com/UpstreamData/pyasic/blob/bb5442a373ecfac5907b295bbf91415042b456e6/pyasic/config/temperature.py#L21-L24), and I think it makes sense to take this in the same direction, as a config, rather than part of the data.

What I would like to see:

```rust
struct TemperatureConfig {
    /// The target chip temperature for the miner
    target: f64,
    /// The temperature at which the fans will run at 100%
    hot: f64,
    /// The temperature at which the miner will reboot or trigger thermal scaling
    danger: f64,
    /// The minimum temperature the miner must preheat to in order to start
    minimum: f64,
}
```

This mirrors the structure from Braiins OS, which I think makes the most sense as it is the most complex, but cleanly laid out.

### pos-ei-don on 2026-06-22

Reworked per your feedback — it's now a `TemperatureConfig` (`target`/`hot`/`danger`/`minimum`) via a `SupportsTemperatureConfig` config trait, mirroring the Braiins/`ScalingConfig` shape, rather than data fields. Two notes:

- Fields are `Option<f64>`: VNish reports `minimum` (`cooling.min_startup_water_temp`) and `danger` (`misc.restart_temp`) via `/summary`, but not `target`/`hot` — so `None` there means "not reported by this firmware", not "no limit". That lets each firmware fill what it has. (VNish's `target` lives in the `/settings` autotune config — happy to wire it in a follow-up.)
- I implemented `get_temperature_config` directly for VNish (via `/summary`) rather than going through the `ConfigField`/collector machinery; glad to move it to the collector pattern like the other configs if you'd prefer.


### b-rowan on 2026-06-22

> * I implemented `get_temperature_config` directly for VNish (via `/summary`) rather than going through the `ConfigField`/collector machinery; glad to move it to the collector pattern like the other configs if you'd prefer.

:laughing: see my comment...

### pos-ei-don on 2026-06-22

Thanks, that makes sense — pushed the rework:

- `SupportsTemperatureConfig` is now a `CollectConfigs` supertrait. `get_temperature_config()` goes through the collector and delegates to a `parse_temperature_config()` hook, mirroring `SupportsScalingConfig`. The VNish backend registers the `/summary → /miner` location in `get_configs_locations` and does the parsing there instead of a direct REST call in the trait impl.
- Added `ConfigField::Temperature` and the matching arm in the epic backend.
- Dropped the manual `FromPyObject` impl. Since `TemperatureConfig` is return-only, I switched it to `pyclass(from_py_object, …)` so the pydantic macro's `extract::<Self>()` resolves via the clone-based derive — no hand-written impl needed.

CI is green. Let me know if you'd rather have the location mapping shaped differently.

### b-rowan on 2026-06-23

Code looks good, tests are failing though.

FYI you can use the files in `meta/` as documentation for other API's, so if you reference them you can probably implement them, let me know if that's inside the scope you want for this PR.

### pos-ei-don on 2026-06-23

Tests are green now — the failure was the `FromPyObject`: with `skip_from_py_object` the auto impl is suppressed, so I added the small manual `impl FromPyObject` in a `python_impls` module like `PoolConfig`/`ScalingConfig`. All your points are in (`target` dropped, `py_pydantic_model(new, name)`, `skip_from_py_object`, epic `_ => vec![]`).

Thanks for the `meta/` pointer — that's really useful. I'd like to keep this PR scoped to the VNish thermal limits and tackle the other firmwares (Braiins/ePIC temperature config from the `meta/` schemas) in a dedicated follow-up, so this one can land as-is. I'll open that next.
