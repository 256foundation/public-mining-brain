# 256foundation/asic-rs pull request #136: Chore: Update Reqwest & Diqwest

> Source: https://github.com/256foundation/asic-rs/pull/136
> Collected: 2026-10-07
> Published: 2026-02-09

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 136
- State: closed
- Author: NeroWeNeed
- Opened: 2026-02-09
- Closed: 2026-02-09
- Labels: none

## Description

Pushes `reqwest` to `0.13`,  `diqwest` to `3.2`, updates feature flag from `rustls-tls` to `rustls` to reflect changes made in the reqwest library, and moves to use `send_digest_auth` because `send_with_digest_auth` will be deprecated soon.
