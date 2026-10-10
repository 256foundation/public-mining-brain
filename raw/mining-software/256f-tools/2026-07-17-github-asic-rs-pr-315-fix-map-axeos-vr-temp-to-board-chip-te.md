# 256foundation/asic-rs pull request #315: fix: map AxeOS VR temp to board, chip temp to chain

> Source: https://github.com/256foundation/asic-rs/pull/315
> Collected: 2026-10-07
> Published: 2026-07-17

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 315
- State: closed
- Author: adamdecaf
- Opened: 2026-07-17
- Closed: 2026-07-29
- Labels: none

## Description

AxeOS exposes distinct sensors on `/api/system/info`: `temp` (ASIC chip) and `vrTemp` (voltage regulator / board). Bitaxe and Nerdaxe backends copied `vrTemp` into inlet/outlet chip temperatures and often left `chips[].temperature` empty by reading `temp` from the config-only `/api/system/asic` payload.

This change is limited to the Bitaxe/Nerdaxe firmware backends:

- Map `vrTemp` → `board_temperature`
- Map `temp` → `inlet_chip_temperature` / `outlet_chip_temperature` and `chips[0].temperature` (preferring live system/info)
- Keep chip rows gated on `DataField::Chips`

No core data structure changes.

## Comments

### adamdecaf on 2026-07-17

That's my bad. Changing core types wasn't my intention - was going a bit too fast with Grok. 

### b-rowan on 2026-07-17

Still a couple core changes, just revert them fully.  Making average be chip OR board is even more confusing...

### adamdecaf on 2026-07-29

Addressed the remaining feedback:

- Restored the `DataField::Chips` guard so chip rows are only emitted when chips are requested
- Reverted the related test expectations (`chips` stays empty when excluded)
- Rebased onto latest `master` as a single commit; no core changes
