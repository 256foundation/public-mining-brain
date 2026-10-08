# 256foundation/mujina pull request #35: chore(deps): remove unused dependencies

> Source: https://github.com/256foundation/mujina/pull/35
> Collected: 2026-10-07
> Published: 2026-03-04

- Repository: 256foundation/mujina
- Type: pull request
- Number: 35
- State: closed
- Author: average-gary
- Opened: 2026-03-04
- Closed: 2026-03-05
- Labels: none

## Description

## Summary

Remove 6 dependencies confirmed unused by two independent tools and manual source audit.

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

Searches source files for `use <crate>` patterns. Finds zero matches for all 6 deps:

```
$ cargo machete
Analyzing dependencies of crates in this directory...
cargo-machete found the following unused dependencies in this directory:
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

Uses unstable compiler flags to determine which crates are actually linked:

```
$ cargo +nightly udeps --workspace
unused dependencies:
`mujina-miner v0.1.0`
└─── dependencies
     └─── "modular-bitfield"
```

`cargo-udeps` only flags `modular-bitfield` because `sha2` and `hyper` are still *compiled* as transitive dependencies of other crates (axum, utoipa-swagger-ui). They are linked into the binary even though no source code imports them. Removing them as *direct* dependencies is still correct — they remain available transitively for the crates that actually need them.

### Why both tools?

| Tool | What it detects | Limitation |
|------|----------------|------------|
| `cargo-udeps` | Deps not linked by the compiler at all | Misses deps that are linked transitively but never imported by *your* code |
| `cargo-machete` | Deps with no `use` or `extern crate` in source | Heuristic; can have false positives for crates used via macros or re-exports |

Together they provide high confidence: `modular-bitfield` is confirmed by both tools. `sha2`, `hyper`, `hex`, `thiserror`, and `tracing` are confirmed by machete's source scan and corroborated by manual grep showing zero imports.

## Impact

Eliminates 15 exclusive transitive dependencies from the build. Zero code changes — only Cargo.toml deletions.

## Verification

- `cargo check --workspace` — pass
- `cargo test --workspace --features skip-pty-tests` — 283 passed, 0 failed
- `cargo machete` — clean (no unused deps detected after removal)
- `cargo fmt --check` — pass

Closes #34
See: https://github.com/256foundation/mujina/discussions/8

## Comments

### average-gary on 2026-03-05

Closing in favor of #32 which covers the same dependency removals and additionally fixes the pre-existing `tracing.rs` clippy warnings. Our audit in [Discussion #8](https://github.com/256foundation/mujina/discussions/8#discussioncomment-15915744) corroborates the findings.
