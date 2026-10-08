# 256foundation/asic-rs pull request #379: feat(luxos): restore stock OS

> Source: https://github.com/256foundation/asic-rs/pull/379
> Collected: 2026-10-07
> Published: 2026-09-16

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 379
- State: closed
- Author: cfilipescu
- Opened: 2026-09-16
- Closed: 2026-09-16
- Labels: none

## Description

Closes #372

## Summary

- add the authenticated LuxOS `uninstallluxos` RPC wrapper
- implement `RestoreStockOs` for `LuxMinerV1` and advertise the capability
- map a successful immediate response to `RestoreStockOsResult::accepted(None)`
- propagate LuxOS error statuses instead of treating them as accepted
- cover accepted and rejected responses with local TCP protocol tests

The request contract follows the [LuxOS uninstall API documentation](https://docs.luxor.tech/firmware/api/luxminer/uninstallluxos): TCP port 4028, `command: uninstallluxos`, and a valid session ID in `parameter`.

## Validation

- `cargo fmt --all -- --check`
- `cargo clippy -p asic-rs-firmwares-luxminer --all-targets -- -D warnings`
- `cargo check --workspace --all-targets`
- `cargo test --workspace`
- `git diff --check`

## Comments

### chatgpt-codex-connector[bot] on 2026-09-16

<!-- codex-pull-request-review-summary -->

## Codex Review Summary

This comment shows the latest Codex review activity on this pull request.

| Review | Status | Commit | Review trigger |
| --- | --- | --- | --- |
| 📝 **Code Review** | ✅ **Completed** <relative-time datetime="2026-09-16T04:42:01.561568Z">2026-09-16T04:42:01.561568Z</relative-time> | `3d2eae9` | PR opened |



<details> <summary>ℹ️ About Codex in GitHub</summary>
<br/>

[Your team has set up Codex to review pull requests in this repo](https://chatgpt.com/codex/cloud/settings/general). Reviews are triggered when you
- Open a pull request for review
- Mark a draft as ready
- Comment "@codex review" or "@codex security review".

Codex reacts with 👀 while any review is running, comments if it has suggestions, and reacts with 👍 once all reviews finish with no findings.

</details>
