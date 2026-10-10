# 256foundation/asic-rs pull request #327: fix(epic): report the miner serial rather than the control board CPU serial

> Source: https://github.com/256foundation/asic-rs/pull/327
> Collected: 2026-10-07
> Published: 2026-08-13

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 327
- State: closed
- Author: cryptographicturk
- Opened: 2026-08-13
- Closed: 2026-08-17
- Labels: none

## Description

`DataField::SerialNumber` on ePIC PowerPlay is sourced only from
`/capabilities` → `Control Board Version` → `cpuSerial`, so every miner reports
its control board CPU serial. The manufacturer serial that the same endpoint
exposes as `Miner Serial Number` is never read, which breaks any inventory
keyed on the serial printed on the unit.

## The change

Prefer `Miner Serial Number`, falling back to `cpuSerial` so the field stays
populated on units that don't report one.

## Why tagged extractors rather than ordered fallback

The ordered-fallback idiom used elsewhere in the codebase (two untagged
locations, as the AntMiner backend does for `serial_no` / `serinum`) cannot
express this correctly.

`get_by_pointer` is `Value::pointer`, which returns `Some(Value::Null)` for a
key that is present but null — it is `None` only when the path is absent. And
`extract_field` merges scalars last-wins. `Miner Serial Number` is almost
always present-but-null in the field, so:

- ordering `cpuSerial` last → the nulls clobber it, and the field resolves to
  `None`
- ordering `cpuSerial` first → it wins everywhere, and nothing is fixed

Tagging lands the two values under distinct keys so `parse_serial_number` can
choose. This is the same pattern `parse_control_board_version` already uses in
this backend, for this same endpoint.

## Field data

Surveyed 438 ePIC units:

```
Miner Serial Number   present  67    null 371    absent 0
cpuSerial             present 438
```

So the key is essentially always present and usually null — the exact shape
that defeats ordering. `Miner Serial Number` was only ever populated on AMLogic
control boards; BeagleBoneBlack and Xilinx units were null throughout, and all
of them fall back cleanly.

Where present, the values are 17-character Bitmain serials (matching the format
stock AntMiner firmware reports) and were unique across all 67.

## Tests

Three new cases covering the shapes seen in the field and in the fixtures:
serial present, key absent, key present-but-null.

- `cargo fmt --all -- --check` — clean
- `cargo clippy -p asic-rs-firmwares-epic --all-targets` — clean
- `cargo test -p asic-rs-firmwares-epic` — 9 passed
- `cargo test --workspace` — no failures
- Verified against live hardware: 142 units, every one matching the value read
  directly from `/capabilities` (67 reporting a manufacturer serial, the rest
  falling back to the control board serial)
