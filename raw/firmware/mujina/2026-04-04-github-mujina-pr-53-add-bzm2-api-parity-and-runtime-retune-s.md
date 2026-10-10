# 256foundation/mujina pull request #53: Add BZM2 API parity and runtime retune safety

> Source: https://github.com/256foundation/mujina/pull/53
> Collected: 2026-10-07
> Published: 2026-04-04

- Repository: 256foundation/mujina
- Type: pull request
- Number: 53
- State: closed
- Author: recklessnode
- Opened: 2026-04-04
- Closed: 2026-06-11
- Labels: none

## Description

## Summary
This follow-up restores the remaining BZM2 parity work that was intentionally kept out of the core upstream integration PR.

It adds:
- BZM2 chain summary API
- BZM2 clock-report API
- full runtime tuning / retune state exposure
- saved operating-point validation / status reporting
- missing BZM2 protocol regression tests
- a runtime retune safety fix so the saved operating point is retained until a replacement retune is actually applied

## Why this is separate
The core BZM2 integration PR was kept focused on:
- board/ASIC integration
- mining UART/TDM path
- telemetry
- startup calibration flow
- generic documentation
- upstream-scope cleanup

This branch carries the later parity work that exists in the internal repository but was intentionally not folded into the core PR.

## What this adds
- `GET /api/v0/boards/{name}/bzm2/chain-summary`
- `POST /api/v0/boards/{name}/bzm2/clock-report`
- associated board commands and API DTOs
- runtime tuning state fields for:
  - saved operating-point reuse
  - retune requirement / pending state
  - desired voltage / clock / accept ratio targets
  - saved operating-point validation status and reasons
  - planner notes
- protocol coverage for legacy wire-format invariants and parser resynchronization

## Retune safety fix
This branch also fixes an operational safety issue in the richer runtime tuning layer:

- runtime retune no longer invalidates and deletes the saved operating point before any replacement plan is actually applied
- instead, the saved operating point is marked `Pending` with reasons and retained as the last known-good profile
- the live tuning state still reports that the saved operating point should not be reused for the current run

That keeps the persisted calibration artifact available until a real retune executor exists.

## Branch base
This branch is built on top of the already-rebased core BZM2 PR branch and therefore also sits on current upstream `main` (`ece3334`).

## Validation
- `cargo test -p mujina-miner --message-format=human`

Result:
- `384 passed, 0 failed, 5 ignored`
- doctests: `3 passed, 0 failed, 2 ignored`

## Scope note
This branch already includes the same upstream-scope cleanup as the core PR:
- no private-source doc references
- no `bzm2-debug` binary
- no synthetic `virtual_device` transport layer
- tuning and board power logic moved out of `asic/bzm2`

## Comments

### recklessnode on 2026-06-11

Superseding this PR with a rebuilt series on current main: #68 (infra) → #69 (asic core) → #70 (board + tuning) → #71 (diagnostics + docs).

This branch's API-parity and runtime-retune work is carried by #70 (tuning/retune triggers, saved-operating-point reconciliation) and #71 (the diagnostics endpoints), re-expressed against upstream's current `BackplaneConnector` architecture and Telemetry naming. Closing in favor of the series.
