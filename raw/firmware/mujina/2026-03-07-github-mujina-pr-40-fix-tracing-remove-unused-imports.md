# 256foundation/mujina pull request #40: fix(tracing): remove unused imports

> Source: https://github.com/256foundation/mujina/pull/40
> Collected: 2026-10-07
> Published: 2026-03-07

- Repository: 256foundation/mujina
- Type: pull request
- Number: 40
- State: closed
- Author: skot
- Opened: 2026-03-07
- Closed: 2026-03-12
- Labels: none

## Description

## Summary
- make Linux-only tracing imports conditional
- remove the unused local tracing prelude import
- keep the journald fallback log message via a fully qualified macro

## Validation
- cargo test --no-run


## Comments

### skot on 2026-03-07

this PR is to support building mujina on macos without warnings.

### skot on 2026-03-10

there is some overlap here with #32 

### rkuester on 2026-03-12

Thanks for filing. I took the issues raised here, along with the overlap in #32, as a hint that conditional compilation of the journald features required a bit of a refactoring to consolidate the `#[cfg]`s multiplying throughout the file. See 3176b56.
