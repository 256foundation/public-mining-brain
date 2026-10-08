# 256foundation/asic-rs pull request #337: feat(core): name the algorithms this crate's miners actually mine

> Source: https://github.com/256foundation/asic-rs/pull/337
> Collected: 2026-10-07
> Published: 2026-08-24

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 337
- State: closed
- Author: cryptographicturk
- Opened: 2026-08-24
- Closed: 2026-08-25
- Labels: none

## Description

First of three, and the foundation for #335.

## Problem

`HashAlgorithm` has five variants, and **three of them — `X11`, `Blake2S256`, `Kadena` — are never constructed anywhere in the tree.** Only `SHA256` and `Scrypt` are ever produced. Meanwhile the AntMiner make alone ships models on ten different algorithms, so anything outside those two had nowhere to go and silently became SHA-256.

## What's needed

I went through every model in every make. Across ~610 models in 13 makes, six algorithms are missing:

| Algorithm | Models |
|---|---|
| kHeavyHash | KS3, KS5, KS5 Pro *(Kaspa)* |
| Eaglesong | K7 *(Nervos CKB)* |
| EtHash | E9 Pro |
| Equihash | Z15, Z15 Pro *(Zcash)* |
| Handshake | HS3 *(Blake2b then SHA3)* |
| Blake256R14 | DR5 *(Decred)* |

Every other make is single-algorithm and already expressible — Elphapex and VolcMiner are Scrypt, the remaining eleven are SHA-256 throughout. AntMiner is the only mixed-algorithm make: 39 SHA-256, 5 Scrypt, 3 X11, and one each of the rest.

## Also adds `Unknown`

For a miner naming an algorithm this crate doesn't recognise. Exactly one backend learns its algorithm from the device at runtime rather than from the model — ePIC, via `/Mining/Algorithm` — and reporting an unrecognised value as SHA-256 would be a confident wrong answer of precisely the kind this type exists to prevent.

`Unknown` is deliberately **not** a `from_str` catch-all: a typo still fails to parse rather than quietly becoming `Unknown`. It's a value a caller opts into.

It carries no payload, so the original text isn't preserved. Doing that would mean a `String` field, which drops `Copy` (relied on at three call sites), serialises as `{"Unknown": "..."}` instead of a flat string, and is rejected outright by `PyPydanticEnum`, which supports only fieldless variants. That's a change to the pydantic macro crate rather than an enum addition, so it's out of scope here — say the word if the fidelity is worth it.

## Tests

`EnumIter` is derived to support a round-trip test asserting `Display` and `EnumString` agree for every variant. They're derived independently, so a variant whose rendered name didn't parse back would be a silent one-way trip — and the next PR in this stack depends on that holding.

## Notes

- `Kadena` and `Blake2S256` are the same algorithm under two names (Kadena *is* Blake2s-256). I have not touched either, since removing a public variant breaks the Python and TypeScript bindings — but worth a decision at some point.
- Stub regenerated with `maturin generate-stubs`, not hand-edited.

Verified: 182 Rust tests pass, `cargo clippy --all-targets` clean under `warnings = "deny"`, `cargo fmt --check` clean, and `cargo check --features python` builds.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

https://claude.ai/code/session_01ErTo1a4BgYptp5tC8r1oHR
