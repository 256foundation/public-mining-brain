# 256foundation/asic-rs pull request #348: feat(epic): support hashrate-split pool status

> Source: https://github.com/256foundation/asic-rs/pull/348
> Collected: 2026-10-07
> Published: 2026-08-31

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 348
- State: closed
- Author: Erisli
- Opened: 2026-08-31
- Closed: 2026-08-31
- Labels: none

## Description

## Summary

Adds ePIC PowerPlay pool parsing for hashrate-split mode while preserving standard pool behavior.

## Changes

- Fetches and tags hashrate-split config/status data for pool collection.
- Parses split pool groups with quota, active pool state, share counts, and connection status.
- Aligns pool config parsing with the tagged hashrate-split config payload.

## Validation

- Reviewed diff against master.
- git diff --check passed.
- cargo test -p asic-rs-firmwares-epic parse_ currently stops in asic-rs-core/src/traits/miner.rs with existing lifetime bound error before backend tests run.
