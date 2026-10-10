# 256foundation/mujina issue #34: chore: remove unused dependencies identified by cargo-machete and cargo-udeps

> Source: https://github.com/256foundation/mujina/issues/34
> Collected: 2026-10-07
> Published: 2026-03-04

- Repository: 256foundation/mujina
- Type: issue
- Number: 34
- State: closed
- Author: average-gary
- Opened: 2026-03-04
- Closed: 2026-03-05
- Labels: none

## Description

## Context

Per [Discussion #8](https://github.com/256foundation/mujina/discussions/8), a dependency audit identified 6 direct dependencies with zero usage in source code.

## Unused Dependencies

### mujina-miner
- **`sha2`** — the `bitcoin` crate provides SHA-256 via `bitcoin_hashes`; `sha2` is never imported
- **`hyper`** (direct) — only used transitively via axum/reqwest, never imported directly
- **`modular-bitfield`** — never imported anywhere in source code

### mujina-dissect
- **`hex`** — never imported
- **`thiserror`** — never imported
- **`tracing`** — never imported

## Tool Evidence

### `cargo-machete` (source-code heuristic, stable Rust)

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
```

### `cargo +nightly udeps` (compiler-level analysis)

```
$ cargo +nightly udeps --workspace
unused dependencies:
`mujina-miner v0.1.0`
└─── dependencies
     └─── "modular-bitfield"
```

`cargo-udeps` only flags `modular-bitfield` because `sha2` and `hyper` are still compiled as transitive dependencies of other crates. Removing them as direct dependencies is still correct — they remain available transitively for the crates that actually need them.

## Proposed Change

Remove all 6 entries from the respective `Cargo.toml` files. Zero source code changes needed. Eliminates 15 exclusive transitive dependencies from the build.

## Comments

### average-gary on 2026-03-05

Closing as duplicate of #29, which covers the same scope.
