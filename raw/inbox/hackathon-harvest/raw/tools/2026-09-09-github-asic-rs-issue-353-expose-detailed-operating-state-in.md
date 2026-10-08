# 256foundation/asic-rs issue #353: Expose detailed operating state in MinerData

> Source: https://github.com/256foundation/asic-rs/issues/353
> Collected: 2026-10-07
> Published: 2026-09-09

- Repository: 256foundation/asic-rs
- Type: issue
- Number: 353
- State: closed
- Author: cfilipescu
- Opened: 2026-09-09
- Closed: 2026-09-10
- Labels: none

## Description

Expose an optional firmware-reported operating-state value in `MinerData` so consumers can display states such as `Mining`, `Idling`, and `AdjustingClockVoltage`, and group miners by those states.

### Existing source and gap

Checked at `560e72f12e300200db2c5b63762e3fb917200cf6`; current `master` `6ef32df811437a87b07594db19d118c8bf0940fe` has the same relevant behavior.

- [MinerData](https://github.com/256foundation/asic-rs/blob/560e72f12e300200db2c5b63762e3fb917200cf6/asic-rs-core/src/data/miner.rs#L139) exposes messages and `is_mining: bool`, but no detailed state.
- The [EPIC/UMC collector](https://github.com/256foundation/asic-rs/blob/560e72f12e300200db2c5b63762e3fb917200cf6/asic-rs-firmwares/epic/src/backends/v1/mod.rs#L527) already extracts `/Status/Operating State` into `DataField::IsMining`.
- [Boolean parsing](https://github.com/256foundation/asic-rs/blob/560e72f12e300200db2c5b63762e3fb917200cf6/asic-rs-firmwares/epic/src/backends/v1/mod.rs#L1231) reduces that string to `state != "Idling"` and defaults to true when absent. Detailed states are lost during normalization.

### Acceptance

- Add optional typed operating-state telemetry (suggested representation: `operating_state: Option<String>`) to the ordinary `MinerData` snapshot.
- Preserve UMC's actual reported state, including adjustment/startup/error states and unfamiliar future values.
- Missing/null/invalid state data produces `None`; it must not become an invented `Mining` or `Idling` state.
- A string representation or extensible typed representation must retain unknown firmware labels.
- Support additional backends when they provide explicit state information; keep detailed state unavailable when only a coarse boolean can be obtained.
- Preserve the existing `is_mining` API and document how the detailed state differs from that boolean.
- Consume the existing summary response; avoid duplicate requests.
- This issue covers operating state only. Existing last-error messages already have a separate representation; last command and error-parser enhancements are outside scope.

### Implementation and verification

Integrate with the existing collection and parsing path, reusing already-required responses. Preserve unsupported/missing values as `None`. Update the Rust model, serialization, Python models/stubs, generated TypeScript types where applicable, and documentation together.

Add fixture-based parser/serialization coverage in the existing CI-run tests. No live miner or device configuration changes should be needed.

Cover Mining, Idling, adjustment and unknown states, absent/null/invalid values, boolean-only firmware, and preservation through typed serialization/bindings.



## Comments

### b-rowan on 2026-09-09

`operating_state: Option<...>` is fine, but I would like to make it an enum, with states representative of a union of states from different firmwares, EG `Stable`, `Tuning`, `Paused`, `Ramping Frequency/Voltage` etc.
