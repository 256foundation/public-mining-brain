# 256foundation/asic-rs pull request #255: fix(braiins,vnish): refresh expired bearer tokens on 401

> Source: https://github.com/256foundation/asic-rs/pull/255
> Collected: 2026-10-07
> Published: 2026-05-20

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 255
- State: closed
- Author: aleksander-rudolf
- Opened: 2026-05-20
- Closed: 2026-05-20
- Labels: none

## Description

The cached bearer token is never re-validated, so once the miner expires it server-side (e.g. reboot), every subsequent call returns 401 and the client is stuck until the process restarts. On 401, `send_command` now invalidates the cached token, re-authenticates via the existing `authenticate()`, and retries the request once.
