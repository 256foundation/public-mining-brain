# 256foundation/mujina pull request #68: feat(board): per-board command channel, power-rail primitives, thread telemetry types

> Source: https://github.com/256foundation/mujina/pull/68
> Collected: 2026-10-07
> Published: 2026-06-11

- Repository: 256foundation/mujina
- Type: pull request
- Number: 68
- State: closed
- Author: recklessnode
- Opened: 2026-06-11
- Closed: 2026-09-28
- Labels: none

## Description

Part 1 of a 4-PR series adding Intel BZM2 (Bonanza Mine 2) ASIC support. This first part is **generic infrastructure with zero BZM2 code** — each piece is useful to mujina on its own:

## Per-board command channel, wired end to end

`BoardCommand::SetFanTarget` and the `SetFanTargetRequest` DTO existed but nothing connected them. This PR lands the missing plumbing along architecture.md's "new capabilities = new channels" rule:

- `BackplaneConnector` and `api::registry::BoardRegistration` gain an optional `mpsc::Sender<BoardCommand>`; the backplane forwards it in `start_board`.
- `PATCH /api/v0/boards/{name}/fans/{fan}` now drives `SetFanTarget` with a 5 s reply timeout. Boards opt in by populating `command_tx`; all current boards answer "accepts no commands" (400) until they grow a command loop — wiring bitaxe's EMC2101 into this is a natural follow-up.
- `BoardRegistry` gains `board(name)` / `command_tx(name)` accessors with lazy disconnect pruning; `get_board` now uses the former instead of scanning the full snapshot list.

## Power-rail primitives (`board/power.rs`)

`PowerRail` trait with three implementations — `Tps546PowerRail` (adapts the existing TPS546 driver to the trait and to `VoltageRegulator`), `FilePowerRail`/`FileGpioPin` (sysfs/hwmon file adapters for SBC-style regulator and GPIO files without I2C), and `GpioResetLine` (an `AsicEnable` with `pulse(assert, settle)`). Plus `VoltageStackBringupPlan`: ordered multi-rail power-up with per-step settle delays and reverse-order shutdown. Bitaxe hand-rolls its TPS546 bring-up and EmberOne00 (12 ASICs) has no rail-sequencing primitives yet — this is the shared layer both can converge on. Tested, no new dependencies.

## Typed thread telemetry + shared thread errors

`HashThreadTemperatureReading`/`HashThreadPowerReading`/`HashThreadTelemetryUpdate` and `HashThreadEvent::TelemetryUpdate` give hash threads a typed path to report sensor data (the bitaxe monitor currently publishes `threads: Vec::new() // TODO: populate from hash thread telemetry`). `HashThreadError` gives thread implementations a shared error vocabulary.

## Smaller pieces

- `Backplane::attach_configured_board(device_type, device_id)` — attach an env-configured virtual board without synthesizing a transport event (the CPU miner's daemon-side synthetic `CpuDeviceConnected` injection could migrate to this).
- `BoardTelemetry.asics` (serde-default, hidden when empty) + `AsicState`/`EngineCoordinate`: generic per-ASIC topology/diagnostics state for multi-ASIC boards.
- `Clone` derives on the Arc-backed serial reader/writer/control halves, so a board can keep a stats handle while its thread owns the port.
- `.gitattributes` for LF normalization.

## Series

1. **infra (this PR)** → 2. `asic/bzm2` protocol/thread layer → 3. BZM2 board driver + tuning planner → 4. HTTP diagnostics + hardware docs. Each part builds and tests green standalone. The series replaces #38 and #53 (rebuilt from scratch on current main — see those PRs for history).

Gates: `cargo build` (0 warnings), `cargo test` (330 passed / 0 failed), `cargo fmt` clean.

🤖 Generated with [Claude Code](https://claude.com/claude-code)


## Comments

### recklessnode on 2026-06-11

**Series:** #68 (infra) -> #69 (asic core) -> #70 (board + tuning) -> #71 (diagnostics + docs). Each part builds and tests green standalone; later parts are stacked, so their diffs include predecessors - review by commit.

### recklessnode on 2026-07-22

﻿**Series merge order (updated 2026-07-22)** - four stacked PRs, all MERGEABLE, each green under `just checks` (fmt + `clippy --release -D warnings` + test) on **every commit**. Merge strictly in order:

1. **#68** `bzm2/pr1-infra` - generic infrastructure, zero BZM2 code (per-board command channel wiring upstream's own `SetFanTarget`, `board/power.rs` rail primitives, `HashThread` telemetry types, `attach_configured_board`). Standalone-useful; base of the stack.
2. **#69** `bzm2/pr2-asic-core` - BZM2 protocol/UART/clock/thread layer **+ serial-robustness hardening**. Hard-depends on #68's `HashThread` telemetry types (won't compile without them).
3. **#70** `bzm2/pr3-board-tuning` - board driver + tuning planner. Drives #69's ASIC layer; uses #68's `command_tx`/`power`.
4. **#71** `bzm2/pr4-diagnostics` - HTTP diagnostic endpoints + docs. Forwards `BoardCommand`s that #70's board answers; hardware reference docs link to the maintained [bzm2-hwref](https://github.com/Blockscale-Solutions/bzm2-hwref).

The order is the compile dependency chain (verified at import level - no PR references a symbol from a later one), not a preference. Merging #68 first collapses #69's visible diff to its own commits, and so down the stack. Later commits added today (the runtime-retune invalidation fix on #70, the serial hardening on #69) are folded into the PR whose code they touch, keeping each PR correct-from-first-commit rather than fixed-in-a-later-PR.


### recklessnode on 2026-08-01

Heads-up on a force-push just now across the whole series (#68 → #69 → #70 → #71). Two drivers, no functional change in either:

**1. Rebased onto current `main`.** All four branches were one commit behind and are now up to date and conflict-free.

**2. Applied the new `S.topdown` ordering rule.** `CODE_STYLE.md` gained [S.topdown](https://github.com/256foundation/mujina/commit/e0e582f) on 25 Jul, after this series was opened, so rather than leave it for review I audited the new modules against it and fixed the ordering up front. Most visibly, `Bzm2Thread`, `Bzm2UartController`, `Bzm2ClockController` and `Bzm2CalibrationPlanner` were each declared *last* in their module and now open it; constants that had drifted into the type and function groups are back in the constants group; and public items now precede private ones in the function groups.

Each style commit is **pure reordering** — every touched file is identical as a multiset of lines apart from a couple of blank lines `rustfmt` normalised — so they should be quick to skim. Verified with the justfile's own recipe before pushing: `cargo fmt --check` clean, `cargo clippy --release -- -D warnings` clean, `cargo test` 419 passed / 0 failed.

Two notes for whoever picks this up:

- I deliberately did **not** de-interleave `struct`/`impl` pairs, since that interleaving is the established convention across the existing codebase (`backplane.rs`, `scheduler.rs`, …). Happy to go further if you read S.mod more strictly.
- The series' CI has never actually run — all four PRs sit at `action_required`, the approval gate for workflows on fork PRs. That's why they show as blocked despite being mergeable. Whenever someone has a moment to approve the workflow runs, the checks should go green.


### recklessnode on 2026-09-02

Any progress on getting these PRs merged in?

### recklessnode on 2026-09-28

Superseded by #117, which carries this work rebuilt on current main and exercised on real hardware (three hashboards, 300 BZM2 ASICs, mining to a public pool).
