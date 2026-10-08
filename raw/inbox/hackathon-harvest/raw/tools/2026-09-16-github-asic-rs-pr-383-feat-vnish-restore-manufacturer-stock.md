# 256foundation/asic-rs pull request #383: feat(vnish): restore manufacturer stock OS

> Source: https://github.com/256foundation/asic-rs/pull/383
> Collected: 2026-10-07
> Published: 2026-09-16

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 383
- State: closed
- Author: cfilipescu
- Opened: 2026-09-16
- Closed: 2026-09-16
- Labels: none

## Description

Closes #373

## Summary
- implement restore-to-stock through POST /api/v1/firmware/remove for VNish 1.2.x and 1.3.x
- send no request body for 1.2.x and {"remove_stock_logs": false} for 1.3.x
- parse the API after field into RestoreStockOsResult.reboot_after_seconds
- report restore-to-stock support from both VNish backends
- keep factory_reset as the separate restore-to-stock-settings operation

## Tests
- verify each generation sends its version-specific authenticated request
- verify reboot-delay parsing for both generations
- verify HTTP 400 model incompatibility is surfaced as an error
- use local HTTP mocks only; no real hardware is contacted

## Validation
- cargo fmt --all -- --check
- cargo clippy -p asic-rs-firmwares-vnish --all-targets -- -D warnings
- cargo check --workspace --all-targets
- cargo test --workspace

## Comments

### chatgpt-codex-connector[bot] on 2026-09-16

<!-- codex-pull-request-review-summary -->

## Codex Review Summary

This comment shows the latest Codex review activity on this pull request.

| Review | Status | Commit | Review trigger |
| --- | --- | --- | --- |
| 📝 **Code Review** | ✅ **Completed** <relative-time datetime="2026-09-16T13:24:07.403075Z">2026-09-16T13:24:07.403075Z</relative-time> | `cbd5083` | PR opened |



<details> <summary>ℹ️ About Codex in GitHub</summary>
<br/>

[Your team has set up Codex to review pull requests in this repo](https://chatgpt.com/codex/cloud/settings/general). Reviews are triggered when you
- Open a pull request for review
- Mark a draft as ready
- Comment "@codex review" or "@codex security review".

Codex reacts with 👀 while any review is running, comments if it has suggestions, and reacts with 👍 once all reviews finish with no findings.

</details>
