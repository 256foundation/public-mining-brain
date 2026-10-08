# 256foundation/asic-rs pull request #360: feat(firmware): add non-mutating preflight API

> Source: https://github.com/256foundation/asic-rs/pull/360
> Collected: 2026-10-07
> Published: 2026-09-10

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 360
- State: closed
- Author: cfilipescu
- Opened: 2026-09-10
- Closed: 2026-09-10
- Labels: none

## Description

## Summary

- add public prepare_firmware and supports_prepare_firmware APIs for Rust and Python consumers
- expose the prepared FirmwareImage filename and payload so callers can inspect the selected image without uploading it
- implement preflight for both stock Antminer backends using the existing read-only miner type lookup and BMU resolver
- route real Antminer upgrades through the same preparation path so validation and upload cannot diverge
- reject magic-bearing truncated BMU headers and cover malformed headers, CRC failures, payload truncation, excessive nesting, and incompatible model/subtype bundles

## Safety

Antminer preparation only reads miner_type.cgi with GET. The firmware upload endpoint is called only by upgrade_firmware.

## Testing

- cargo test --all --locked --exclude asic-rs-pydantic --exclude asic-rs-pydantic-macros
- cargo test -p asic-rs --features python --lib
- cargo clippy -p asic-rs-core -p asic-rs-firmwares-antminer -p asic-rs --all-targets --all-features -- -D warnings
- cargo fmt --all -- --check
- python3 -m py_compile python/pyasic_rs/asic_rs.pyi

Closes #347
