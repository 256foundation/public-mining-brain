# 256foundation/asic-rs pull request #400: fix(release): break publish cycle and retry registry rate limits

> Source: https://github.com/256foundation/asic-rs/pull/400
> Collected: 2026-10-07
> Published: 2026-09-29

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 400
- State: closed
- Author: cfilipescu
- Opened: 2026-09-29
- Closed: 2026-09-29
- Labels: none

## Description

The v0.8.4 release fails while packaging `asic-rs-pydantic-macros`: its versioned dev dependency requires `asic-rs-pydantic 0.8.4` to be published first, but that library depends on the macro crate. Switching from `cargo workspaces publish` to individual `cargo publish --package` calls removed the publisher's automatic dev-dependency cleanup.

Use an unversioned local path for this test dependency so Cargo omits it from the published manifest. Keep explicit package selection and add up to five publish attempts for crates.io HTTP 429 responses, with 60/120/240/480-second backoff. Other errors fail immediately, and exhausted retries preserve the failing exit status.

Validation:
- `cargo publish --dry-run --allow-dirty --locked --package asic-rs-pydantic-macros` passed, including package compilation; nothing was uploaded.
- Inspected the generated crate archive: the circular dev dependency is absent, while `pyo3` and `trybuild` remain.
- Executed the workflow's publish script with stubbed Cargo and sleep commands: immediate success, recovery after rate limits, exhausted retries, permanent failure, and a rate limit followed by a permanent failure all passed.
- `bash -n` and `git diff --check` passed.

Failure evidence: https://github.com/256foundation/asic-rs/actions/runs/35770501034
