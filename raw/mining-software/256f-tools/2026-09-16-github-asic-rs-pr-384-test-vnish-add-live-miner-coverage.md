# 256foundation/asic-rs pull request #384: test(vnish): add live miner coverage

> Source: https://github.com/256foundation/asic-rs/pull/384
> Collected: 2026-10-07
> Published: 2026-09-16

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 384
- State: closed
- Author: cfilipescu
- Opened: 2026-09-16
- Closed: 2026-09-16
- Labels: none

## Description

## Summary

- add an ignored Vnish live data smoke test using `MINER_IP`
- add an ignored destructive restore-to-stock-OS live test using `MINER_IP`
- auto-detect the Vnish backend so the tests cover supported 1.2.x and 1.3.x firmware

## Testing

- `cargo fmt --check`
- `rustup run 1.95.0 cargo test -p asic-rs-firmwares-vnish live_test_auto_detect -- --nocapture` (2 ignored as expected without `--ignored`)


## Comments

### chatgpt-codex-connector[bot] on 2026-09-16

<!-- codex-pull-request-review-summary -->

## Codex Review Summary

This comment shows the latest Codex review activity on this pull request.

| Review | Status | Commit | Review trigger |
| --- | --- | --- | --- |
| 📝 **Code Review** | ✅ **Completed** <relative-time datetime="2026-09-16T18:23:08.313112Z">2026-09-16T18:23:08.313112Z</relative-time> | `248cf74` | PR opened |



<details> <summary>ℹ️ About Codex in GitHub</summary>
<br/>

[Your team has set up Codex to review pull requests in this repo](https://chatgpt.com/codex/cloud/settings/general). Reviews are triggered when you
- Open a pull request for review
- Mark a draft as ready
- Comment "@codex review" or "@codex security review".

Codex reacts with 👀 while any review is running, comments if it has suggestions, and reacts with 👍 once all reviews finish with no findings.

</details>
