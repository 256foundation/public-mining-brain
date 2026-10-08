# 256foundation/asic-rs pull request #339: refactor(core): make HashRate.algo a HashAlgorithm instead of a String

> Source: https://github.com/256foundation/asic-rs/pull/339
> Collected: 2026-10-07
> Published: 2026-08-24

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 339
- State: closed
- Author: cryptographicturk
- Opened: 2026-08-24
- Closed: 2026-08-25
- Labels: none

## Description

Third of three. **Stacked on #337 and #338** — both appear here until they merge. Review the third commit only.

This is @b-rowan's suggestion from #335: *"if we want to more strictly define the algorithm types into an enum or something, then just implement string conversion."*

## Problem

The algorithm was a free-form `String` on `HashRate` while `DeviceInfo` already carried a proper `HashAlgorithm` — the same fact in two representations, only one of them checkable.

What that cost, concretely: an ePIC test asserted `algo: "SHA-256".to_string()` — hyphenated, unlike the other 128 sites — and nothing caught it, because `HashRate`'s hand-written `PartialEq` compares only `value` after unit conversion and **ignores `algo` entirely**. Typing the field turns that class of typo into a compile error.

## Compatibility

**JSON is unchanged.** `HashAlgorithm` carries `#[serde(rename)]` on every variant, so `"algo": "SHA256"` serialises byte-identically, and `pydantic_data(to_string)` keeps the Python representation a string.

**Python callers are unaffected.** `hashrate.algo == "SHA256"` still works, because #338 taught the enum to compare against its own name. The interop tests now assert *both* forms — `== HashAlgorithm.Scrypt` and `== "Scrypt"` — so the guarantee is pinned by the test rather than described in a commit message.

**TypeScript narrows** from `string` to a union of the variant names. Reading improves; only code assigning an arbitrary string breaks, and the compiler says so.

**Rust is mechanical** — 129 construction sites across 27 files, all compile-time constants, every failure a compile error. There is exactly one meaningful read in the whole tree.

## The one behavioural change

ePIC is the only backend that learns its algorithm from the device at runtime. An unrecognised value there now reports `Unknown` rather than being flattened into SHA-256. An absent field keeps the SHA-256 default that was already applied. Every other site is a compile-time constant, so nothing else can be affected.

Verified: 182 Rust tests, 91 Python tests, clippy clean under `warnings = "deny"`, fmt clean, stub regenerated with `maturin generate-stubs`.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

https://claude.ai/code/session_01ErTo1a4BgYptp5tC8r1oHR

## Comments

### b-rowan on 2026-08-25

Good for now, I have some changes I want to make based on this but will submit a PR later for those.
