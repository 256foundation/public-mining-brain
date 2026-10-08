# 256foundation/asic-rs pull request #391: fix(braiins): refresh expired bearer token on 401 in v26_04 backend

> Source: https://github.com/256foundation/asic-rs/pull/391
> Collected: 2026-10-07
> Published: 2026-09-24

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 391
- State: closed
- Author: pos-ei-don
- Opened: 2026-09-24
- Closed: 2026-09-24
- Labels: none

## Description

#255 fixed the stuck bearer token for the Braiins `v25_07` backend, but the `v26_04` backend (selected for Braiins OS >= 26.04) was added without that change, so it still has the original problem.

The cached token is never re-validated. Once the miner drops it server-side (e.g. a reboot after a firmware upgrade), every authenticated call returns 401 and the client stays stuck until the process is restarted.

Seen on an Antminer S19k Pro with Braiins OS 26.09: after an upgrade-triggered reboot, `PUT /actions/pause` kept failing with `401 Missing or invalid` until the integration re-created the client.

This mirrors the `v25_07` behaviour from #255: on 401, `send_command` drops the cached token, re-authenticates via `ensure_authenticated()` and retries the request once. A remaining 401 is mapped to `BraiinsError::Unauthorized`.

Not covered here: `read_logs()` calls `execute_request_with_timeout` directly and has the same stale-token behaviour in both backends. I kept this PR to the `send_command` path to match #255; happy to follow up if you want that covered as well.
