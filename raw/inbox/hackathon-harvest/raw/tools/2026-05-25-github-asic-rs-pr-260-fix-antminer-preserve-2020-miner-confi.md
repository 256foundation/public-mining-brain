# 256foundation/asic-rs pull request #260: fix(antminer): preserve 2020 miner config updates

> Source: https://github.com/256foundation/asic-rs/pull/260
> Collected: 2026-10-07
> Published: 2026-05-25

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 260
- State: closed
- Author: DanNicolau
- Opened: 2026-05-25
- Closed: 2026-05-25
- Labels: none

## Description

I found the discrepancy between bitmain-miner-mode and work-mode. Even when the payload is accepted with status 200 OK, the sleep mode would not update. With this change it will now update on old stock firmware. v2023 is left untouched.

Validated on:
- Firmware Version Mon Dec 26 17:10:01 CST 2022

## Comments

### b-rowan on 2026-05-25

@DanNicolau Approved, see comment and lints need fixing though.

### DanNicolau on 2026-05-25

changes made

### b-rowan on 2026-05-25

@DanNicolau not sure what changed, but looks fine.  Couple merge conflicts now from #259, if you can fix I'll merge.
