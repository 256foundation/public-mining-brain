# 256foundation/asic-rs pull request #2: refactor: change to factory pattern, and add luxos discovery

> Source: https://github.com/256foundation/asic-rs/pull/2
> Collected: 2026-10-07
> Published: 2025-03-30

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 2
- State: closed
- Author: b-rowan
- Opened: 2025-03-30
- Closed: 2025-03-31
- Labels: none

## Description

Updated to use a factory pattern, while leaving the simple `get_miner` call at `asic_rs::get_miner`.  Also added luxos model discovery support.

Noticed a minor issue with this way of handling models, for firmware based identification we don't yet have a good way to discriminate between makes based on firmware.  EG BraiinsOS on Antminers vs BraiinsOS on Braiins Mini Miner isn't really covered by this handler. 

## Comments

### jpcomps on 2025-03-31

looks good, lgtm
