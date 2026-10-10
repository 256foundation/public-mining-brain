# 256foundation/mujina pull request #88: feat(config): introduce config tree with souces

> Source: https://github.com/256foundation/mujina/pull/88
> Collected: 2026-10-07
> Published: 2026-08-05

- Repository: 256foundation/mujina
- Type: pull request
- Number: 88
- State: open
- Author: jayrmotta
- Opened: 2026-08-05
- Closed: n/a
- Labels: none

## Description

## Summary

Implements the first two phases of the incremental plan agreed on in [mujina-mips#1](https://github.com/256foundation/mujina-mips/pull/1) for [MIP-0001](https://github.com/256foundation/mujina-mips/blob/mip-configuration-and-api/mip-0001-configuration-and-api.md) (configuration & API), using pool configuration as the pilot feature per Ryan's suggestion on [#83](https://github.com/256foundation/mujina/issues/83):

1. Replace the unimplemented `Config` stub with a real tree, populated from env vars.
2. Serve that tree read-only over the existing `/api/v0` HTTP API.

Closes #83.

## Scope

Read-only, in-memory, no persistence, no write path for now.

[MIP-0001 DR-1:](https://github.com/rkuester/mujina-mips/blob/mip-configuration-and-api/mip-0001-configuration-and-api.md#dr1-the-configuration-tree-is-one-object)
> There is no separate "API shape" and "internal shape" of configuration that the daemon has to keep in sync, and no conversion code between them.

Structs serialize directly and do include the plaintext pool password. The trust model remains the same, as the API has no authentication or authorization yet.

## What changed

- `Config` is now populated by `Config::from_env()`, and `daemon.rs` builds its job source directly from the tree instead of reading `MUJINA_POOL_*` env vars itself.
- The config tree reuses `stratum_v1::StratumV1PoolConfig` (renamed from `PoolConfig`) rather than defining a second, near-identical type for the API. That's the DR-1 point above applied literally: `daemon.rs` no longer hand-converts one pool-config shape into another before constructing a `StratumV1Source` — the value extracted from the tree already is the type the wire client needs.
- `StratumV1PoolConfig.password` is now `Option<String>`, so an unset password stays distinguishable from an explicitly empty one; the wire-level `"x"` default moved from the daemon into `StratumV1Client::authorize()`, the one place it's actually needed.
- `GET /api/v0/config` returns the full configuration tree; `GET /api/v0/sources` and `GET /api/v0/sources/{name}` return the configured job sources, replacing the old telemetry-backed `/sources`.
- Sources are typed as a `kind`-tagged enum (`SourceKind`) rather than assuming every source is a pool. `"stratum_v1"` is the only kind today; the tag lets a future consumer respond additively as new kinds are added — the dummy source used when none is configured, and, over time, other protocols — instead of needing a breaking shape change later. "Source" is also the vocabulary the rest of the codebase already uses for this concept (the `job_source` module, `SourceRegistration`, `SourceEvent`), so the config tree's naming now matches it.

## Comments

- The spec mentions `256fdn` as a possible name for a source, but since we don't have an env var to name a source, nor a more advanced config file system yet, we only assign an incrementing character like a, b, c, and so on. We could introduce a name property with its own env var, or simply skip it for now and wait for config files to land.
