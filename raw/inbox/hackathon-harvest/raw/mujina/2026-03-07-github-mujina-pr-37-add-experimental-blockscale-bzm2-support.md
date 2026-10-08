# 256foundation/mujina pull request #37: Add experimental Blockscale BZM2 support and diagnostics

> Source: https://github.com/256foundation/mujina/pull/37
> Collected: 2026-10-07
> Published: 2026-03-07

- Repository: 256foundation/mujina
- Type: pull request
- Number: 37
- State: closed
- Author: recklessnode
- Opened: 2026-03-07
- Closed: 2026-03-07
- Labels: none

## Description

## Summary
This PR adds experimental BZM2 support to `mujina-miner`, including the runtime mining path, board bring-up, telemetry, tuning, diagnostics, and generic reference documentation.

## What this adds
- a dedicated `asic/bzm2` stack for UART/TDM protocol handling, work dispatch, share reconstruction, PLL/DLL control, DTS/VS telemetry, and silicon-validation tooling
- a dedicated `board/bzm2` integration for startup enumeration, bring-up/shutdown sequencing, rail control, domain-voltage application, saved operating-point replay, and runtime engine discovery
- board/API support for BZM2-specific diagnostics, on-demand DTS/VS queries, chain summary, engine discovery, and clock reports
- generic Blockscale reference docs under `docs/bzm2`

## Scope boundaries
- this targets the Blockscale/BZM2 Gen2 path; Gen1-specific runtime support is intentionally not included
- board-specific reference-platform glue is kept out of the core path in favor of generic bring-up abstractions
- local process notes are not part of this branch; only upstream-relevant code and documentation are included

## Suggested review order
1. `feat(bzm2): add initial BZM2 board integration`
2. `feat(bzm2): add telemetry, control, and protocol coverage`
3. `feat(bzm2): add UART clock diagnostics`
4. `feat(bzm2): add debug CLI and DLL diagnostics`
5. `feat(bzm2): add tuning planner and startup calibration`
6. `feat(bzm2): expose DTS/VS telemetry through the API`
7. `feat(bzm2): add chain enumeration and roadmap`
8. `feat(bzm2): add startup auto-enumeration`
9. `feat(bzm2): wire board bring-up into the lifecycle`
10. `feat(bzm2): apply domain voltages and rail telemetry`
11. `feat(bzm2): add engine discovery and runtime layouts`
12. `feat(bzm2): make runtime tuning engine-capacity aware`
13. `feat(bzm2): add runtime measurements and retune state`
14. `feat(bzm2): add live board diagnostics and API parity`
15. `docs(bzm2): organize reference docs under docs/bzm2`
16. `fix(bzm2): resolve upstream port drift`

## Validation
- `cargo test -p mujina-miner --message-format=human`
- result: `344 passed, 0 failed, 5 ignored`
- BZM2 debug binary tests: `3 passed, 0 failed`
- doctests: `8 passed, 0 failed, 2 ignored`

## Comments

### recklessnode on 2026-03-07

Superseded by #38. This earlier branch contained non-buildable intermediate commits; the replacement PR was rebuilt from `upstream/main` with a full `cargo test -p mujina-miner --message-format=human` gate after each commit.
