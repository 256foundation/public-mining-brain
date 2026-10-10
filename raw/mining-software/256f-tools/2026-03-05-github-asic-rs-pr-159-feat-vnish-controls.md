# 256foundation/asic-rs pull request #159: Feat vnish controls

> Source: https://github.com/256foundation/asic-rs/pull/159
> Collected: 2026-10-07
> Published: 2026-03-05

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 159
- State: closed
- Author: glitchpixelz
- Opened: 2026-03-05
- Closed: 2026-03-08
- Labels: none

## Description

Adds VNish backend support for pause, resume, restart, set_pools, and authenticated backend initialization via VnishBackend::with_auth(ip, model, password).

Each feature has been tested and verified to pass.

## Comments

### glitchpixelz on 2026-03-08

Closed this branch. I was copying an old python vnish file that I made from the wrong direction and added too much. Refactoring all of it was getting messy. Started fresh and opened a new PR here that is ready for review, https://github.com/256foundation/asic-rs/pull/160
