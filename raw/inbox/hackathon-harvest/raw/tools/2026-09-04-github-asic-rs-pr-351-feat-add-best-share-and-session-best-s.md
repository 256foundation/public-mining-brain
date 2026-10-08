# 256foundation/asic-rs pull request #351: feat: add best_share and session_best_share to MinerData

> Source: https://github.com/256foundation/asic-rs/pull/351
> Collected: 2026-10-07
> Published: 2026-09-04

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 351
- State: closed
- Author: adamdecaf
- Opened: 2026-09-04
- Closed: 2026-09-09
- Labels: none

## Description

Adds optional miner-level best-share difficulty to `MinerData`.

| Field | Meaning |
| --- | --- |
| `best_share: Option<f64>` | All-time when the firmware distinguishes it; otherwise the single reported value |
| `session_best_share: Option<f64>` | Since last boot / hashing start, only when reported separately |

Also: `DataField::BestShare` / `DataField::SessionBestShare`, getters, Python bindings. `None` if the firmware does not report it. Parse is inline and accepts JSON numbers and suffix strings (`"483k"`, `"1.2M"`).

Only backends we can test are wired:

| Firmware | `best_share` | `session_best_share` |
| --- | --- | --- |
| Bitaxe / NerdAxe / NerdQAxe (AxeOS `system/info`) | `bestDiff` | `bestSessionDiff` |

Unmapped backends leave both fields `None`.

Closes #350

## Comments

### adamdecaf on 2026-09-09

Addressed the unused-parse review: emptied every `GetBestShare` / `GetSessionBestShare` impl that had no data source we can actually test.

The only wired mappings are Bitaxe and NerdAxe (AxeOS / NerdQAxe) `system/info` `bestDiff` / `bestSessionDiff`, covered by the Bitaxe fixture test. Everything else returns `None`. Squashed to one commit.

### adamdecaf on 2026-09-09

Sorry for the extra round of review on this.

I over-implemented parse functions on backends we could not actually test, which left a bunch of unused code for you to mark. That was on me — should have kept the mappings to Bitaxe / NerdAxe / AxeOS from the start and left everything else `None`.

Should be ready for another look. Thanks for catching it.

### b-rowan on 2026-09-09

> Sorry for the extra round of review on this.
> 
> I over-implemented parse functions on backends we could not actually test, which left a bunch of unused code for you to mark. That was on me — should have kept the mappings to Bitaxe / NerdAxe / AxeOS from the start and left everything else `None`.
> 
> Should be ready for another look. Thanks for catching it.

No worries, just want to get it in here for you ASAP.

Unrelated question, but seeing hasherdash, do you have any opposition to porting the GO bindings directly into this library?  We already have python and typescript, and GO is another one that would make sense.

### adamdecaf on 2026-09-09

> Unrelated question, but seeing hasherdash, do you have any opposition to porting the GO bindings directly into this library? We already have python and typescript, and GO is another one that would make sense.

For sure I'd be able to contribute those into asic-rs. I'll admit that all of that is generated/tested via Grok, so I'll lean on that for contributing to asic-rs. I setup the asic-rs-go library to get hasherdash off the ground. 

### b-rowan on 2026-09-09

> For sure I'd be able to contribute those into asic-rs. I'll admit that all of that is generated/tested via Grok, so I'll lean on that for contributing to asic-rs. I setup the asic-rs-go library to get hasherdash off the ground.

No worries, most everything is at this point, hence why I try to review these things more carefully now.  I know a lot less about the interop side of things, but am slowly learning, so getting something basic in place is a really good start.
