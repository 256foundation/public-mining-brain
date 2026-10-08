# 256foundation/asic-rs pull request #365: feat(data): expose pool last share time

> Source: https://github.com/256foundation/asic-rs/pull/365
> Collected: 2026-10-07
> Published: 2026-09-15

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 365
- State: closed
- Author: cfilipescu
- Opened: 2026-09-15
- Closed: 2026-09-15
- Labels: none

## Description

## Summary

- add optional PoolData.last_share_time as a Unix timestamp in seconds
- normalize both epoch values and firmware-provided HH:MM:SS or DD:HH:MM:SS share ages
- populate the field in supporting firmware backends while leaving unavailable or ambiguous values as None
- expose the new field in the Python type stub and add fixture coverage

## Testing

- cargo test --workspace
- cargo clippy --workspace --all-targets -- -D warnings
- cargo check --features python

## Comments

### chatgpt-codex-connector[bot] on 2026-09-15

<!-- codex-pull-request-review-summary -->

## Codex Review Summary

This comment shows the latest Codex review activity on this pull request.

| Review | Status | Commit | Review trigger |
| --- | --- | --- | --- |
| 📝 **Code Review** | ✅ **Completed** <relative-time datetime="2026-09-15T14:04:30.381417Z">2026-09-15T14:04:30.381417Z</relative-time> | `28c6e28` | New commits |



<details> <summary>ℹ️ About Codex in GitHub</summary>
<br/>

[Your team has set up Codex to review pull requests in this repo](https://chatgpt.com/codex/cloud/settings/general). Reviews are triggered when you
- Open a pull request for review
- Mark a draft as ready
- Comment "@codex review" or "@codex security review".

Codex reacts with 👀 while any review is running, comments if it has suggestions, and reacts with 👍 once all reviews finish with no findings.

</details>
