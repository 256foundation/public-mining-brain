# 256foundation/asic-rs pull request #204: feat(auth): add per-miner auth credentials

> Source: https://github.com/256foundation/asic-rs/pull/204
> Collected: 2026-10-07
> Published: 2026-03-24

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 204
- State: closed
- Author: ankitgoswami
- Opened: 2026-03-24
- Closed: 2026-03-31
- Labels: none

## Description

## Summary

Closes #195

- Adds `MinerAuth` type with `secrecy::SecretString` for passwords (redacted in Debug, zeroized on drop)
- Adds `HasAuth` trait to `Miner` supertrait with `default_auth()` and `set_auth(&mut self)`
- All authenticated backends wired up: AntMiner, WhatsMiner V2/V3, Braiins V21.09/V25.07, VNish, ePIC, Marathon
- `FirmwareEntry::build_miner` accepts optional auth for discovery (AntMiner digest auth) and applies it to the miner for runtime
- Cached bearer tokens and sessions cleared on credential change
- WhatsMiner RPC: replaced panicking `unwrap()` with proper error handling on auth failure
- Python bindings: `miner.set_auth(username, password)`

## Test plan

Tested against real hardware (AntMiner S19, WhatsMiner M50S, VNish S21 Pro) with three scenarios per backend:

- **Default auth**: verify discovery, auth-gated reads (`get_hostname`, `get_pools_config`), and auth-gated writes (`set_fault_light`) all succeed with built-in default credentials
- **Custom auth**: call `set_auth` with non-default credentials, verify auth-gated operations reflect the new credentials (return None/fail when creds are wrong for the target)
- **Wrong auth**: call `set_auth` with invalid credentials, verify auth-gated reads return None and auth-gated writes fail — confirming custom credentials are actually being used, not defaults

Additional verification:
- `cargo test --workspace` with all features enabled — all existing tests pass
- `cargo check --no-default-features` — compiles without features
- WhatsMiner no longer panics on wrong credentials (returns error instead)

🤖 Generated with [Claude Code](https://claude.com/claude-code)

## Comments

### ankitgoswami on 2026-03-31

@b-rowan any estimate on when this can be merged?

### b-rowan on 2026-03-31

> @b-rowan any estimate on when this can be merged?

Will review shortly

### ankitgoswami on 2026-03-31

fyi - the only change since your last review is a merge conflict resolution from master in Cargo.toml
