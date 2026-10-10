# 256foundation/asic-rs pull request #221: fix(python): fix `into_unit` in the python bindings

> Source: https://github.com/256foundation/asic-rs/pull/221
> Collected: 2026-10-07
> Published: 2026-04-07

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 221
- State: closed
- Author: b-rowan
- Opened: 2026-04-07
- Closed: 2026-04-08
- Labels: none

## Description

The symbols were flipped when using into unit in the python bindings, the value should be multiplied by the old unit then divided by the new unit.
