# 256foundation/asic-rs pull request #378: feat(core): add stock OS restore abstraction

> Source: https://github.com/256foundation/asic-rs/pull/378
> Collected: 2026-10-07
> Published: 2026-09-15

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 378
- State: closed
- Author: cfilipescu
- Opened: 2026-09-15
- Closed: 2026-09-15
- Labels: none

## Description

## Summary

- add a dedicated `RestoreStockOs` trait and result model
- keep `factory_reset()` explicitly scoped to restoring settings without changing the OS
- make the new operation available through `dyn Miner`
- add an unsupported-by-default implementation to every backend
- leave vendor endpoint implementations to the focused follow-up issues

## Semantics

`factory_reset()` restores default settings. `restore_stock_os()` uninstalls an aftermarket OS and initiates restoration of the manufacturer OS. A successful result records request acceptance and an optional vendor-reported reboot delay; it does not claim that the restore has completed.

Closes #371.

## Validation

- `cargo fmt --all -- --check`
- `cargo check --workspace --all-targets`
- `cargo test --workspace`
- `cargo clippy --workspace --lib -- -D warnings`
- `git diff --check`

`cargo clippy --workspace --all-targets -- -D warnings` remains blocked by the pre-existing `clippy::items_after_test_module` warning in `asic-rs-core/src/data/pool.rs`; this PR does not modify that file.

## Comments

### chatgpt-codex-connector[bot] on 2026-09-15

<!-- codex-pull-request-review-summary -->

## Codex Review Summary

This comment shows the latest Codex review activity on this pull request.

| Review | Status | Commit | Review trigger |
| --- | --- | --- | --- |
| 📝 **Code Review** | ✅ **Completed** <relative-time datetime="2026-09-15T21:50:01.386687Z">2026-09-15T21:50:01.386687Z</relative-time> | `b0152b1` | PR opened |



<details> <summary>ℹ️ About Codex in GitHub</summary>
<br/>

[Your team has set up Codex to review pull requests in this repo](https://chatgpt.com/codex/cloud/settings/general). Reviews are triggered when you
- Open a pull request for review
- Mark a draft as ready
- Comment "@codex review" or "@codex security review".

Codex reacts with 👀 while any review is running, comments if it has suggestions, and reacts with 👍 once all reviews finish with no findings.

</details>
