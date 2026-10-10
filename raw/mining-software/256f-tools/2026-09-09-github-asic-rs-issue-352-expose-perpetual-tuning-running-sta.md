# 256foundation/asic-rs issue #352: Expose perpetual tuning running status in MinerData

> Source: https://github.com/256foundation/asic-rs/issues/352
> Collected: 2026-10-07
> Published: 2026-09-09

- Repository: 256foundation/asic-rs
- Type: issue
- Number: 352
- State: closed
- Author: cfilipescu
- Opened: 2026-09-09
- Closed: 2026-09-10
- Labels: none

## Description

Consumers can read requested and scaled tuning targets, but cannot distinguish perpetual tuning being disabled from tuning telemetry being unavailable. Expose the firmware-reported running status as an optional typed field in `MinerData` (suggested name: `tuning_running: Option<bool>`).

### Existing source and gap

Checked at `560e72f12e300200db2c5b63762e3fb917200cf6`; current `master` `6ef32df811437a87b07594db19d118c8bf0940fe` has the same relevant behavior.

- [MinerData](https://github.com/256foundation/asic-rs/blob/560e72f12e300200db2c5b63762e3fb917200cf6/asic-rs-core/src/data/miner.rs#L128) exposes `tuning_target` and `scaled_tuning_target`, but no running flag.
- The EPIC/UMC backend already obtains the summary through [DataField::TuningTarget](https://github.com/256foundation/asic-rs/blob/560e72f12e300200db2c5b63762e3fb917200cf6/asic-rs-firmwares/epic/src/backends/v1/mod.rs#L425).
- [Target parsing](https://github.com/256foundation/asic-rs/blob/560e72f12e300200db2c5b63762e3fb917200cf6/asic-rs-firmwares/epic/src/backends/v1/mod.rs#L1164) checks `/PerpetualTune/Running` and returns no target when false or unavailable. Consumers cannot recover a reliable running flag from target presence.
- Optimization completion is separately available through `BoardData.tuned`; it has different semantics.

### Acceptance

- Preserve the explicit UMC running flag: true, false, or unknown.
- False requires an explicit false value; missing/null/malformed data and unsupported backends produce `None`.
- Document that this is firmware-reported perpetual/autotuning running status, independent of whether hashing is running or optimization has completed.
- Use other backends only where an equivalent reported status exists. Do not infer it from `is_mining`, target presence, or board tuning completion.
- Include the value in ordinary `get_data()` snapshots and the existing field/getter machinery as appropriate.
- Existing target/scaled-target telemetry remains available for requested-versus-effective displays such as `70(60) TH/s`; those targets already exist and are outside this field addition.

### Implementation and verification

Integrate with the existing collection and parsing path, reusing already-required responses. Preserve unsupported/missing values as `None`. Update the Rust model, serialization, Python models/stubs, generated TypeScript types where applicable, and documentation together.

Add fixture-based parser/serialization coverage in the existing CI-run tests. No live miner or device configuration changes should be needed.

Cover explicit true/false, absent/null/invalid flag, missing summary, running while optimization is incomplete, and a backend without support.



## Comments

### cfilipescu on 2026-09-09

so if ptune is off return Manual{voltage: Voltage, frequency: Frequency} for `TuningTarget`
