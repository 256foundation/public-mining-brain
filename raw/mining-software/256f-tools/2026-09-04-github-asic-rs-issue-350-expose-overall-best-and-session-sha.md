# 256foundation/asic-rs issue #350: Expose overall best and session share difficulty on MinerData

> Source: https://github.com/256foundation/asic-rs/issues/350
> Collected: 2026-10-07
> Published: 2026-09-04

- Repository: 256foundation/asic-rs
- Type: issue
- Number: 350
- State: closed
- Author: adamdecaf
- Opened: 2026-09-04
- Closed: 2026-09-09
- Labels: none

## Description

`MinerData` and `DataField` currently have pool accepted/rejected counts, but no best-share difficulty. Several firmwares already report this; it would be nice to extract and expose it through asic-rs instead of leaving clients to scrape vendor APIs.

## What to add

Two optional miner-level fields, both numeric difficulty (not a formatted string):

- **all-time best share** (high-water mark, often NVS-backed)
- **session best share** (since last boot / hashing process start)

Pool-level best share is a nice extra where the firmware has it, but miner-level is the useful one.

## Firmware sources already in-tree

| Firmware | All-time | Session | Notes |
| --- | --- | --- | --- |
| Bitaxe / Nerdaxe (AxeOS `/api/system/info`) | `bestDiff` | `bestSessionDiff` | Older AxeOS sends a suffix string (`"483k"`, `"1.2M"`). [ESP-Miner #1202](https://github.com/bitaxeorg/ESP-Miner/pull/1202) switched the API to a number. Parsers should accept both. |
| Braiins | `best_share` / `best_share_str` | — | Also `last_difficulty` (current pool diff, not best). `best_share` can overflow u64; prefer `best_share_str` on 26.04+. Present on miner stats, pools, and hashboards in the fixtures. |
| Vnish | `best_share` | — | In miner stats API. |

## Suggested shape

- New `DataField` variants, e.g. `BestShare` and `SessionBestShare`
- `Option<f64>` (or a small newtype) on `MinerData`
- Bitaxe/Nerdaxe `get_locations` already fetches `system/info` — map the keys there
- Braiins/Vnish can fill all-time from existing stats JSON; session may stay `None`
