# 256foundation/asic-rs pull request #324: fix(antminer): read chain rate and board temps on newer stock firmware

> Source: https://github.com/256foundation/asic-rs/pull/324
> Collected: 2026-10-07
> Published: 2026-08-12

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 324
- State: closed
- Author: cryptographicturk
- Opened: 2026-08-12
- Closed: 2026-08-13
- Labels: none

## Description

Two parsing gaps on AntMiner stock firmware `86.48-2.0.0`, both of which leave per-board fields `None`. Neither is model-specific — they affect the already-supported L9 exactly as they affect an L11.

## The gaps

**1. `chain_rate{idx}` is read as a string, but this generation emits a JSON number.**

```rust
.get(&format!("chain_rate{idx}"))
.and_then(|v| v.as_str())          // firmware sends 6.790325248, not "6.790325248"
```

so `board.hashrate` is always `None`. The values are present in the RPC stats payload:

```json
"chain_rate1": 6.790325248,
"chain_rate2": 6.791386112,
"chain_rate3": 6.754780672
```

**2. `temp_pcb{idx}` does not exist on this generation.**

The firmware splits the reading into inlet/outlet pairs instead:

```json
"temp_in_pcb_1": "47",  "temp_out_pcb_1": "57",
"temp_in_pcb_2": "47",  "temp_out_pcb_2": "56",
"temp_in_pcb_3": "44",  "temp_out_pcb_3": "54"
```

so `board.board_temperature` is always `None`. This also leaves `average_temperature` empty, since it is derived from the per-board readings.

## The change

- A small `parse_f64_field` helper that accepts either a JSON number or a quoted string, used for `chain_rate{idx}`.
- `board_temperature` falls back to `temp_out_pcb_{idx}` when the combined `temp_pcb{idx}` key is absent. The outlet reading is the meaningful one for thermal purposes.

Applied to both `v2020` and `v2023_07`, which share this parser.

## Measured

Against live hardware, per board:

```
before:  temp=None      hashrate=None
after:   temp=53C       hashrate=6.80 GH/s
```

`average_temperature` populates as a consequence. Verified on both an L9 and an L11 running this firmware.

## Verification

- `cargo fmt --all -- --check` — clean
- `cargo check --workspace` — clean
- Live check against multiple L9 and L11 units on a production farm

## Note

Board temperature could reasonably map to the 4-field temperature model added in 0.7.0 rather than collapsing to the outlet reading — `temp_in_pcb_*` / `temp_out_pcb_*` and `temp_in_chip_*` / `temp_out_chip_*` are all present on this firmware. I kept this change minimal and behaviour-compatible; happy to extend it if you would prefer the fuller mapping.
