# 256foundation/mujina pull request #32: refactor(deps): remove unused dependencies

> Source: https://github.com/256foundation/mujina/pull/32
> Collected: 2026-10-07
> Published: 2026-03-03

- Repository: 256foundation/mujina
- Type: pull request
- Number: 32
- State: closed
- Author: Nickamoto
- Opened: 2026-03-03
- Closed: 2026-03-11
- Labels: none

## Description

Remove dependencies confirmed unused by cargo-machete analysis, as identified in the dependency audit (discussion #8, issue #29).

mujina-miner:
  - sha2: bitcoin crate provides SHA-256 via bitcoin_hashes
  - hyper (direct): still available transitively via axum/reqwest
  - modular-bitfield: no usage in source

mujina-dissect:
  - hex: no usage in source
  - thiserror: no usage in source
  - tracing: no usage in source (tracing-subscriber retained)

Also removes sha2, hyper, and modular-bitfield from workspace dependencies as they are no longer referenced by any member.

Fix unused import warnings in tracing.rs by gating linux-only imports (env, tracing_journald, prelude) behind cfg(target_os).

Eliminates ~15 exclusive transitive crates.

Refs: #29

## Comments

### jayrmotta on 2026-03-04

tACK e8718fc

### average-gary on 2026-03-05

Independently arrived at the same changes via a dependency audit posted in [Discussion #8](https://github.com/256foundation/mujina/discussions/8#discussioncomment-15915744). Confirmed the same 6 unused deps using both `cargo-machete` (source-code heuristic) and `cargo +nightly udeps` (compiler-level analysis):

```
$ cargo machete
mujina-dissect -- ./tools/mujina-dissect/Cargo.toml:
	hex
	thiserror
	tracing
mujina-miner -- ./mujina-miner/Cargo.toml:
	hyper
	modular-bitfield
	sha2

$ cargo +nightly udeps --workspace
unused dependencies:
`mujina-miner v0.1.0`
└─── dependencies
     └─── "modular-bitfield"
```

Nice that this PR also fixes the `tracing.rs` cfg gating — we noted those as pre-existing clippy failures on macOS but didn't include the fix. LGTM.

Closed my duplicate PR #35 in favor of this one.

### rkuester on 2026-03-11

Thanks for your first contribution, Nick, and welcome to the project!

I restructured the commits slightly. The original first commit mixed dep removal with cfg-gating fixes in tracing.rs. I moved the cfg-gating changes into the second commit alongside the tracing-journald platform gating.

Also changed the type from `refactor` to `build` since these are build configuration changes rather than code restructuring with no change in behavior.
