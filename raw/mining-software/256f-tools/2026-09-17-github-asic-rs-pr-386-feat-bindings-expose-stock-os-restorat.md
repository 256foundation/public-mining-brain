# 256foundation/asic-rs pull request #386: feat(bindings): expose stock OS restoration

> Source: https://github.com/256foundation/asic-rs/pull/386
> Collected: 2026-10-07
> Published: 2026-09-17

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 386
- State: closed
- Author: cfilipescu
- Opened: 2026-09-17
- Closed: 2026-09-17
- Labels: none

## Description

Closes #376

## Summary
- expose `supports_restore_stock_os` and `restore_stock_os()` in Python
- add C FFI capability/result endpoint and generated header
- add Go capability/result type and `RestoreStockOS()`
- document that `factory_reset()` restores settings only, while stock OS restoration uninstalls the aftermarket OS

## Validation
- `cargo fmt --all`
- `cargo test --workspace`
- `cargo clippy -p asic-rs-ffi --all-targets -- -D warnings`
- `python3 scripts/docs/gen_supported_devices.py --check`

Go toolchain was not installed in the local environment; the checked-in cgo header was regenerated from cbindgen.
