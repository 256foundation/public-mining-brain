# 256foundation/asic-rs pull request #125: fix: handle optional working chips in total chips calculation

> Source: https://github.com/256foundation/asic-rs/pull/125
> Collected: 2026-10-07
> Published: 2026-01-09

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 125
- State: closed
- Author: glitchpixelz
- Opened: 2026-01-09
- Closed: 2026-01-09
- Labels: none

## Description

Before

- total_chips was computed by summing BoardData.working_chips as an Option<u16>.
- Because Rust’s sum() over Option returns None if any element is None, one inactive/non-reporting board (0/1/2) caused total_chips to become None even if the other boards reported valid chip counts.
- Result: total_chips frequently disappeared during partial board failures, reducing observability.

After

- total_chips is now computed by filtering out missing chip counts (working_chips = None) and summing only the reported values.
- The code returns:
  - Some(total) if at least one board reports a chip count
  - None only if no boards report chip counts at all
- Result: total_chips remains populated and useful even when one or more boards are down.
