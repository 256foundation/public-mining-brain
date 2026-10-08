# 256foundation/asic-rs pull request #228: feat(firmware): add upgrade options and ePIC system update upload

> Source: https://github.com/256foundation/asic-rs/pull/228
> Collected: 2026-10-07
> Published: 2026-04-09

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 228
- State: closed
- Author: jpcomps
- Opened: 2026-04-09
- Closed: 2026-04-09
- Labels: none

## Description

## Summary
- add `FirmwareUpgradeOptions` to the core firmware model and update the `UpgradeFirmware` trait signature to accept options
- implement ePIC `/systemupdate` multipart firmware upload with SHA-256 checksum, retain-settings option mapping, API response handling, and improved logging context
- thread upgrade options through Rust and Python bindings (`retain_settings: bool | None`), while keeping Antminer behavior unchanged by accepting and ignoring the new options

## Validation
- cargo test -p asic-rs-firmwares-epic
- cargo test -p asic-rs-firmwares-antminer
- cargo check -p asic-rs --features python
