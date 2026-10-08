# 256foundation/asic-rs pull request #366: feat(data): expose devfee connection status

> Source: https://github.com/256foundation/asic-rs/pull/366
> Collected: 2026-10-07
> Published: 2026-09-15

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 366
- State: closed
- Author: cfilipescu
- Opened: 2026-09-15
- Closed: 2026-09-15
- Labels: none

## Description

## Summary

- add optional `devfee_connected` telemetry to Rust snapshots and the Python/Pydantic API
- derive ePIC status from `/summary` `Last Devfee Error` presence without using the hidden devfee endpoint
- derive VNish 1.2/1.3 status from typed `DevFee` pools and LuxOS status from `FeeStatus`
- leave the field as `None` for firmware without a usable devfee connection signal
- expose the field through the C FFI and typed Go binding introduced on current `master`
- document the normalized semantics and preserve compatibility with older snapshots

## Status mapping

- `Some(true)`: firmware reports the devfee connection online
- `Some(false)`: firmware reports the devfee connection offline
- `None`: status is absent, unsupported, or indeterminate

## Validation

- `cargo test --workspace`
- `cargo test -p asic-rs-firmwares-epic -p asic-rs-firmwares-vnish -p asic-rs-firmwares-luxminer`
- `cargo test -p asic-rs-ffi --locked -- --test-threads=1`
- `cargo check -p asic-rs --features python`
- `cargo clippy --all-targets --all-features --workspace --fix --allow-dirty`
- `go test ./asic_go/ -count=1` with Go 1.23
- Python/Pydantic suite: 119 passed

## Comments

### chatgpt-codex-connector[bot] on 2026-09-15

<!-- codex-pull-request-review-summary -->

## Codex Review Summary

This comment shows the latest Codex review activity on this pull request.

| Review | Status | Commit | Review trigger |
| --- | --- | --- | --- |
| 📝 **Code Review** | ✅ **Completed** <relative-time datetime="2026-09-15T17:45:43.388260Z">2026-09-15T17:45:43.388260Z</relative-time> | `a65a8c5` | New commits |



<details> <summary>ℹ️ About Codex in GitHub</summary>
<br/>

[Your team has set up Codex to review pull requests in this repo](https://chatgpt.com/codex/cloud/settings/general). Reviews are triggered when you
- Open a pull request for review
- Mark a draft as ready
- Comment "@codex review" or "@codex security review".

Codex reacts with 👀 while any review is running, comments if it has suggestions, and reacts with 👍 once all reviews finish with no findings.

</details>
