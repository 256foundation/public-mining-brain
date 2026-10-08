# 256foundation/asic-rs pull request #385: test: add Braiins and LuxOS restore live coverage

> Source: https://github.com/256foundation/asic-rs/pull/385
> Collected: 2026-10-07
> Published: 2026-09-16

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 385
- State: closed
- Author: cfilipescu
- Opened: 2026-09-16
- Closed: 2026-09-16
- Labels: none

## Description

## Summary

- add ignored destructive restore-to-stock-OS live tests for Braiins OS and LuxOS
- auto-detect each firmware backend from `MINER_IP`
- verify restore support before invoking the operation and assert that the request is accepted

## Testing

- `cargo fmt --check`
- `rustup run 1.95.0 cargo test -p asic-rs-firmwares-braiins restore_stock_os_live_test_auto_detect -- --nocapture`
- `rustup run 1.95.0 cargo test -p asic-rs-firmwares-luxminer restore_stock_os_live_test_auto_detect -- --nocapture`

Both live tests are ignored as expected unless explicitly run with `--ignored`.


## Comments

### chatgpt-codex-connector[bot] on 2026-09-16

<!-- codex-pull-request-review-summary -->

## Codex Review Summary

This comment shows the latest Codex review activity on this pull request.

| Review | Status | Commit | Review trigger |
| --- | --- | --- | --- |
| 📝 **Code Review** | ✅ **Completed** <relative-time datetime="2026-09-16T18:31:48.564805Z">2026-09-16T18:31:48.564805Z</relative-time> | `ca1c408` | PR opened |



<details> <summary>ℹ️ About Codex in GitHub</summary>
<br/>

[Your team has set up Codex to review pull requests in this repo](https://chatgpt.com/codex/cloud/settings/general). Reviews are triggered when you
- Open a pull request for review
- Mark a draft as ready
- Comment "@codex review" or "@codex security review".

Codex reacts with 👀 while any review is running, comments if it has suggestions, and reacts with 👍 once all reviews finish with no findings.

</details>
