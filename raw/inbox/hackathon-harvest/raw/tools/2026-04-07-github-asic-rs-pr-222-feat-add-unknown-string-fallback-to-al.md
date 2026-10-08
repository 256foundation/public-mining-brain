# 256foundation/asic-rs pull request #222: feat: add Unknown(String) fallback to all model enums

> Source: https://github.com/256foundation/asic-rs/pull/222
> Collected: 2026-10-07
> Published: 2026-04-07

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 222
- State: closed
- Author: ankitgoswami
- Opened: 2026-04-07
- Closed: 2026-04-08
- Labels: none

## Description

## Summary

- Adds `Unknown(String)` variant to all 7 model enums (antminer, avalon, bitaxe, braiins, epic, nerdaxe, whatsminer)
- `FromStr` now falls back to `Unknown` instead of erroring, so unrecognized models still pair with correct make metadata and all-`None` hardware specs
- Removes `Copy` from all 7 model enums (required since `String` is not `Copy`)
- Removes `#[pyclass]` from all 7 model enums — they are never exported to Python, and pyo3 doesn't support complex enums (mixed unit + tuple variants)
- Removes `ModelSelectionError::UnknownModel` — now unreachable since `FromStr` never errors on unknown strings
- Derives `Default` on `MinerHardware` (all fields are `Option`) to simplify unknown hardware arms
- Adds `Avalon1466` model entry and `MM4v1X3` control board, found on a live device

![No more broken pairing](https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExcHUxcmRtaDcxMnhjNnU1ZnVlMmh0NmJhNDI5dXdlZzFpaWpxbnpwMCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/l0MYt5jPR6QX5pnqM/giphy.gif)

## Test plan

- [x] `cargo test --workspace` passes
- [x] `cargo build --workspace --features python` passes
- [x] Verify a device reporting an unknown model string pairs successfully and returns correct `make_name()`
- [x] Verify known model strings still parse to the correct variant

## Comments

### ankitgoswami on 2026-04-07

Contributors will still need to add accurate MinerHardware metadata for each model, but imo being more permissive here is the right call for usability.

This is especially important when asic-rs is used as a dependency in downstream projects. A new model shouldn't force a full update chain: patch asic-rs, wait for a release, update the downstream crate, cut another release, then push that to customers. That's a lot of churn for something that could just work.
