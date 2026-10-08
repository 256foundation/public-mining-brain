# 256foundation/asic-rs pull request #380: feat(epic): restore stock OS

> Source: https://github.com/256foundation/asic-rs/pull/380
> Collected: 2026-10-07
> Published: 2026-09-16

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 380
- State: closed
- Author: cfilipescu
- Opened: 2026-09-16
- Closed: 2026-09-16
- Labels: none

## Description

Closes #375

## Summary

- probe `GET :4028/openapi.json` during UMC OS miner construction and cache whether `paths./uninstall.post` exists
- keep builds without the route, including PowerPlay/ePIC-controller OpenAPI documents, explicitly unsupported
- send authenticated `POST :4028/uninstall` with `{"param": null, "password": "..."}`
- map `result: true` to an accepted background restore request
- surface legacy `UninstallError` payloads, including missing-script and script-execution failures
- refuse direct restore calls when the endpoint was not advertised

Success means the UMC OS uninstall task was queued; it does not mean that restoration or reboot has completed.

## Tests

Mock HTTP tests cover:

- OpenAPI route presence and absence
- exact method, path, password, and null parameter
- accepted requests
- missing uninstall script errors
- uninstall script execution errors
- refusal on unsupported builds

## Validation

- `cargo fmt --all -- --check`
- `cargo clippy -p asic-rs-firmwares-epic --all-targets -- -D warnings`
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
| 📝 **Code Review** | ✅ **Completed** <relative-time datetime="2026-09-16T18:54:56.521698Z">2026-09-16T18:54:56.521698Z</relative-time> | `ffdf483` | New commits |



<details> <summary>ℹ️ About Codex in GitHub</summary>
<br/>

[Your team has set up Codex to review pull requests in this repo](https://chatgpt.com/codex/cloud/settings/general). Reviews are triggered when you
- Open a pull request for review
- Mark a draft as ready
- Comment "@codex review" or "@codex security review".

Codex reacts with 👀 while any review is running, comments if it has suggestions, and reacts with 👍 once all reviews finish with no findings.

</details>
