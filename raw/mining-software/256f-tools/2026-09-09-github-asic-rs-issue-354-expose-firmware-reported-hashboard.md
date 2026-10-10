# 256foundation/asic-rs issue #354: Expose firmware-reported hashboard performance percentage in BoardData

> Source: https://github.com/256foundation/asic-rs/issues/354
> Collected: 2026-10-07
> Published: 2026-09-09

- Repository: 256foundation/asic-rs
- Type: issue
- Number: 354
- State: closed
- Author: cfilipescu
- Opened: 2026-09-09
- Closed: 2026-09-09
- Labels: none

## Description

Expose each hashboard's firmware-reported performance percentage as optional typed telemetry (suggested field: `BoardData.performance_percent: Option<f64>`). Consumers need the original percentage to show board performance and calculate the legacy miner-wide arithmetic mean without decoding firmware JSON.

### Existing source and gap

Checked at `560e72f12e300200db2c5b63762e3fb917200cf6`; current `master` `6ef32df811437a87b07594db19d118c8bf0940fe` has the same relevant behavior.

- [BoardData](https://github.com/256foundation/asic-rs/blob/560e72f12e300200db2c5b63762e3fb917200cf6/asic-rs-core/src/data/board.rs#L48) includes current/expected hashrate, clock, activity and tuning state, but no reported performance percentage.
- The [EPIC/UMC board parser](https://github.com/256foundation/asic-rs/blob/560e72f12e300200db2c5b63762e3fb917200cf6/asic-rs-firmwares/epic/src/backends/v1/mod.rs#L806) already receives `/Summary/HBs`. It consumes `Hashrate[0]` for current hashrate and leaves `Hashrate[1]` unexposed.
- The [existing UMC fixture](https://github.com/256foundation/asic-rs/blob/560e72f12e300200db2c5b63762e3fb917200cf6/asic-rs-firmwares/epic/src/test/json/v1/summary.json) reports board performance values `103.1` and `104.1`; their arithmetic mean is `103.6%`.
- Normalized expected board hashrate is calculated from chip count, performance-estimator metadata and clock. Current/factory hashrate ratios are not the original reported percentage.

### Acceptance

- Map UMC `HBs[].Hashrate[1]` into the matching board's optional performance percentage using the board index.
- Preserve percentage units: `103.1` means `103.1%`, not a fraction of `1.031`.
- Preserve valid zero values and values above 100%; keep missing/short arrays, invalid types, and placeholder boards without reported values as `None`.
- Prevent non-finite values from entering the normalized/serialized metric.
- Keep the field as firmware-reported performance. Do not silently substitute a ratio derived from factory hashrate.
- Include it in `MinerData.hashboards` and board getters both with and without chip-level collection.
- Other firmware may populate it only when an equivalent reported metric exists. Document backend semantics and leave unsupported values unknown.
- Keep fleet/miner averaging in the consumer; no separate collection mode or new aggregate endpoint is required.

### Implementation and verification

Integrate with the existing collection and parsing path, reusing already-required responses. Preserve unsupported/missing values as `None`. Update the Rust model, serialization, Python models/stubs, generated TypeScript types where applicable, and documentation together.

Add fixture-based parser/serialization coverage in the existing CI-run tests. No live miner or device configuration changes should be needed.

Cover the existing fixture values, index alignment, disabled/placeholder boards, missing/short arrays, invalid values, zero, above-100% values, and board collection with and without chip data.



## Comments

### cfilipescu on 2026-09-09

not worth it

### b-rowan on 2026-09-09

Already easy to compute from expected vs real hashrate, user should be able to figure this one out.
