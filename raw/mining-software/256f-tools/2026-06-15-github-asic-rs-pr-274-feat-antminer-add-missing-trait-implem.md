# 256foundation/asic-rs pull request #274: feat(antminer): add missing trait implementations for stock AM

> Source: https://github.com/256foundation/asic-rs/pull/274
> Collected: 2026-10-07
> Published: 2026-06-15

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 274
- State: closed
- Author: b-rowan
- Opened: 2026-06-15
- Closed: 2026-06-16
- Labels: none

## Description

Adds all traits that stock antminer firmware can support, basically everything sans scaling.

Includes some generic fixes for python representations of data types I noticed while testing.

## Comments

### b-rowan on 2026-06-15

Ill look at the re-auth idea, its probably not a bad idea to try to deal with those funky edge cases.
