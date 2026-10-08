# 256foundation/mujina pull request #24: fix(stratum_v1): support float difficulty in mining.set_difficulty

> Source: https://github.com/256foundation/mujina/pull/24
> Collected: 2026-10-07
> Published: 2026-01-23

- Repository: 256foundation/mujina
- Type: pull request
- Number: 24
- State: closed
- Author: average-gary
- Opened: 2026-01-23
- Closed: 2026-02-24
- Labels: none

## Description

## Summary

Stratum v1 pools may send difficulty as either integer or float values (e.g., `0.001` for low-difficulty vardiff). The previous implementation used `as_u64()` which rejected float values with the error `difficulty not a number`.

## Problem

When connecting to pools or translators that use variable difficulty with sub-integer values, mujina would fail with:

```
WARN stratum_v1::client: Error handling notification
     error=Invalid message format: difficulty not a number
```

This was encountered when testing with the SRI (Stratum Reference Implementation) translator which sends float difficulties for vardiff.

## Changes

- Change `DifficultyChanged` event payload from `u64` to `f64`
- Update `handle_set_difficulty` to parse with `as_f64()`, falling back to `as_u64()` for compatibility
- Update `ProtocolState.difficulty` field to `Option<f64>`
- Use `Difficulty::from_f64()` instead of `Difficulty::from()` when converting to internal `Difficulty` type
- Add test case for float difficulty parsing

## Testing

- All existing tests pass
- Added new test `test_handle_set_difficulty_float` that verifies float parsing
- Manually tested against SRI translator with vardiff enabled

## Comments

### rkuester on 2026-02-03

This issue was also reported, with a log of the Stratum v1 conversation, in #27.

### rkuester on 2026-02-03

Branch main had some style inconsistencies, see d76cc42 and 49aa16b. I rebased this PR atop the fixes in main to get rid of the formatting noise in the PR.

### rkuester on 2026-02-20

> Would you please take a quick look at my additions, and give this branch one more test, with a pool that actually sends fractional values, before I merge it?

In particular, `cargo run --bin mujina-cli -- api miner` should show the fractional difficulty correctly, once things are up and running.

### average-gary on 2026-02-24

Tests worked locally. LGTM.
