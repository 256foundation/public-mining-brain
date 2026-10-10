# 256foundation/mujina issue #6: Dependency Inflation

> Source: https://github.com/256foundation/mujina/issues/6
> Collected: 2026-10-07
> Published: 2025-11-17

- Repository: 256foundation/mujina
- Type: issue
- Number: 6
- State: closed
- Author: TheBlueMatt
- Opened: 2025-11-17
- Closed: 2025-11-21
- Labels: none

## Description

For something that might eventually move towards being a backend to a trillion dollar asset, a large number of (transitive) dependencies (especially ones that are predominately maintained by a single person) is a critical security issue for the entire network. It'd be nice to go ahead and reduce (non-dev) dependencies early to avoid overly depending on them and finding them hard to remove later.
