# 256foundation/asic-rs pull request #340: fix(antminer): declare the algorithms #335 could not name

> Source: https://github.com/256foundation/asic-rs/pull/340
> Collected: 2026-10-07
> Published: 2026-08-24

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 340
- State: closed
- Author: cryptographicturk
- Opened: 2026-08-24
- Closed: 2026-08-25
- Labels: none

## Description

Follow-up to #335. **Stacked on #337** — that commit appears here until it merges. Review the second commit only.

## What #335 left behind

#335 gave the L-series, D-series and KA3 their real algorithms, but nine models were left reporting **SHA-256** — not because they mine it, but because `HashAlgorithm` had no variant for what they actually mine. The doc comment said as much, and deferred it.

#337 adds those variants, so the gap closes:

| Model | Algorithm | Coin |
|---|---|---|
| HS3 | `Handshake` | Handshake *(Blake2b then SHA3)* |
| DR5 | `Blake256R14` | Decred |
| KS3, KS5, KS5 Pro | `KHeavyHash` | Kaspa |
| K7 | `Eaglesong` | Nervos CKB |
| E9 Pro | `EtHash` | — |
| Z15, Z15 Pro | `Equihash` | Zcash |

That's every remaining non-SHA-256 model in the make. All 18 now declare their algorithm on the variant, so the fallback applies only to the S/T-series — which genuinely is SHA-256 — and to models this crate doesn't recognise. The caveat in the doc comment is removed rather than reworded.

## Tests

Two, and the second is the one that matters:

- Each of the ten non-SHA-256 models resolves to its expected algorithm.
- All eighteen declared properties are walked and checked to parse as a `HashAlgorithm` **and** resolve to something other than the fallback. A property naming an algorithm that doesn't exist — a typo in the attribute string — would otherwise fail silently back to SHA-256, which is precisely the failure mode this series exists to remove. The attribute is stringly-typed, so this is the only thing standing between a typo and a wrong answer.

Verified: 8 tests pass in the makes crate, clippy clean under `warnings = "deny"`, fmt clean.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

https://claude.ai/code/session_01ErTo1a4BgYptp5tC8r1oHR
