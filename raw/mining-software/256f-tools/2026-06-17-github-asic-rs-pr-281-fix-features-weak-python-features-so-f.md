# 256foundation/asic-rs pull request #281: fix(features): weak `?` python features so firmwares actually gate (#278)

> Source: https://github.com/256foundation/asic-rs/pull/281
> Collected: 2026-10-07
> Published: 2026-06-17

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 281
- State: closed
- Author: pos-ei-don
- Opened: 2026-06-17
- Closed: 2026-06-17
- Labels: none

## Description

Follow-up to #278.

### Problem
The `python` feature lists each firmware as `asic-rs-firmwares-X/python`. Without the `?` prefix, `"optional-dep/feature"` **implicitly enables the optional dependency**. So any build with `--features python` (i.e. every Python wheel) pulls in *all* firmware crates, regardless of which firmware features are selected — the per-family gating from #278 has no effect for the Python package.

### Fix
Switch the firmware entries in the `python` feature to the weak form `asic-rs-firmwares-X?/python`, so a firmware's `python` feature is only turned on when that firmware is already enabled. No behavior change on default features (all firmwares on). Makes are left untouched (still non-optional — see note below).

### Verified
Built the `pyasic_rs` cp314 musllinux wheel with `--no-default-features --features python,core,proto,antminer,vnish,braiins` (sccache on, same runner), before vs after this change:

| | compile requests | Rust compilation units |
|---|---|---|
| before (all firmwares pulled in) | 621 | 210 |
| after (firmwares gated) | 601 | 190 |

→ 20 fewer Rust crates compiled, wheel builds and loads fine. On a cold CI build that's 20 firmware crates skipped.

### Note on makes
The makes (`asic-rs-makes-*`) are still non-optional workspace deps, so they all compile regardless — that's the other half of #278. I probed gating one (made `asic-rs-makes-auradine` optional + weak its python feature): it builds cleanly (the root crate doesn't reference makes directly) and drops exactly 1 unit. Every unused make is ~1 unit (they all depend only on shared crates: core/serde/strum/serde_json/pyo3), so gating all of them would save ~8 units on top — small, and it needs an explicit firmware→make mapping, which is your call. Left out of this PR deliberately to keep it minimal and uncontroversial.
