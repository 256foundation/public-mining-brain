# 256foundation/asic-rs issue #213: Zynq board shows as unknown

> Source: https://github.com/256foundation/asic-rs/issues/213
> Collected: 2026-10-07
> Published: 2026-04-02

- Repository: 256foundation/asic-rs
- Type: issue
- Number: 213
- State: closed
- Author: DanNicolau
- Opened: 2026-04-02
- Closed: 2026-04-06
- Labels: none

## Description

I have a control board (0 HBs) with a Zynq processor running Antminer on it showing as an "Unknown" control board.

Is this something worth including in the api?

## Comments

### b-rowan on 2026-04-03

Sure, I have no problem with this.  Might as well try to be accurate with what CB we return, even in weird cases.

### jpcomps on 2026-04-06

https://github.com/256foundation/asic-rs/pull/216
