# 256foundation/asic-rs pull request #381: feat(braiins): restore stock OS

> Source: https://github.com/256foundation/asic-rs/pull/381
> Collected: 2026-10-07
> Published: 2026-09-16

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 381
- State: closed
- Author: cfilipescu
- Opened: 2026-09-16
- Closed: 2026-09-16
- Labels: none

## Description

Closes #374

## Summary
- add Braiins OS 26.04 restore-to-stock support through POST /api/v1/upgrade/restore-stock
- accept empty and 204 success responses while continuing to decode non-empty JSON responses
- preserve HTTP status and response body for restore conflicts and unsupported installations
- keep factory_reset as the separate restore-to-stock-settings operation

## Tests
- cover restore-stock 204 acceptance and request routing
- cover factory-reset 204 acceptance
- cover actionable 409 and 501 restore errors
- cover non-empty success JSON decoding

## Validation
- cargo fmt --all -- --check
- cargo clippy -p asic-rs-firmwares-braiins --all-targets -- -D warnings
- cargo check --workspace --all-targets
- cargo test --workspace

## Comments

### chatgpt-codex-connector[bot] on 2026-09-16

<!-- codex-pull-request-review-summary -->

## Codex Review Summary

This comment shows the latest Codex review activity on this pull request.

| Review | Status | Commit | Review trigger |
| --- | --- | --- | --- |
| 📝 **Code Review** | ✅ **Completed** <relative-time datetime="2026-09-16T05:11:26.960863Z">2026-09-16T05:11:26.960863Z</relative-time> | `8777ef4` | PR opened |



<details> <summary>ℹ️ About Codex in GitHub</summary>
<br/>

[Your team has set up Codex to review pull requests in this repo](https://chatgpt.com/codex/cloud/settings/general). Reviews are triggered when you
- Open a pull request for review
- Mark a draft as ready
- Comment "@codex review" or "@codex security review".

Codex reacts with 👀 while any review is running, comments if it has suggestions, and reacts with 👍 once all reviews finish with no findings.

</details>
