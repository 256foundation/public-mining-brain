# 256foundation/mujina pull request #70: feat(board): BZM2 board driver with calibration and runtime tuning

> Source: https://github.com/256foundation/mujina/pull/70
> Collected: 2026-10-07
> Published: 2026-06-11

- Repository: 256foundation/mujina
- Type: pull request
- Number: 70
- State: closed
- Author: recklessnode
- Opened: 2026-06-11
- Closed: 2026-09-28
- Labels: none

## Description

Part 3 of the BZM2 series (stacked on parts 1–2 — review the `feat(board)` + `refactor(bzm2)` commits). The board layer that makes BZM2 hardware mine: registered as virtual board `"bzm2"`, configured via `MUJINA_BZM2_*` env vars, targeting the Satoshi Starter (1 ASIC), bitaxeBIRDS (4), and the larger BZM2 board family.

## Structure

`board/bzm2/` is a directory module split for review (the carve commits are pure code motion):

- **`mod.rs`** — factory + inventory registration, `Bzm2Board` lifecycle, `Bzm2ManagedThread` (decorator publishing thread status into board telemetry).
- **`config.rs`** — env-driven configuration (serial paths/baud, per-bus ASIC counts, voltage domains, calibration class/mode, sensors).
- **`bringup.rs`** — rail/reset sequencing over part 1's `VoltageStackBringupPlan`, voltage/frequency application.
- **`calibration.rs`** — bus-layout resolution (configured or live chain enumeration with fallback), saved operating-point replay with validation, live calibration via the planner, profile persistence.
- **`monitor.rs`** — the runtime loop: sensor snapshots, per-thread metrics, tuning-state evaluation each poll, persistence-gated retune triggers (thermal 85 °C, voltage imbalance 150 mV), safety trip → ordered thread shutdown.
- **`commands.rs`** — the board's command loop answering the eight BZM2 diagnostics added to `api::commands` (HTTP producers land in part 4).
- **`telemetry.rs`** — sysfs/hwmon sensor specs and `BoardTelemetry` publishing/merging.

`tuning/blockscale.rs` is the standalone calibration planner (N voltage domains × M ASICs × 2 PLL stacks): operating-class voltage/frequency tables, saved-point reuse/retune decisions, sweep search-space construction. No crate-internal dependencies.

## Review notes (deliberate divergences + known follow-ups)

- **Telemetry uses `send_modify` merge-in-place** rather than bitaxe's full-snapshot `send` (which 94c8850 tried and 3487b15 reverted): this board merges three telemetry sources (rails, sysfs sensors, thread DTS/VS readings) arriving at different cadences, so merge-in-place is load-bearing here.
- The factory runs bring-up + calibration before returning. For an env-configured board attached at daemon startup this is acceptable; making calibration lazy (bitaxe-style quick factory) is a named follow-up.
- Internal shutdown uses two watch channels; converting to the `CancellationToken` + monitor-owned-state idiom bitaxe established is queued as a follow-up refactor rather than mixed into this series.
- The planner models voltage at stack level today. Boards with multiple series voltage domains need a per-ASIC × series-position model before rail-connected calibration is trusted at 4+ ASICs — flagged in the tuning module and planned before multi-ASIC hardware ships.

Tests: PTY chain emulations (bring-up/shutdown sequencing, enumeration fallback, safety trip closing the scheduler event stream), calibration profile persistence/replay, tuning evaluation — gated unix where PTY-bound.

Gates: `cargo build` (0 warnings), `cargo test` (385 passed / 0 failed), `cargo fmt` clean — held at every carve commit.

🤖 Generated with [Claude Code](https://claude.com/claude-code)


## Comments

### recklessnode on 2026-06-11

**Series:** #68 (infra) -> #69 (asic core) -> #70 (board + tuning) -> #71 (diagnostics + docs). Each part builds and tests green standalone; later parts are stacked, so their diffs include predecessors - review by commit.

### recklessnode on 2026-07-22

﻿**Reviewer note - a behavior gap our own documentation audit just exposed** (flagging it honestly rather than letting review find it):

The saved-operating-point lifecycle has three states (Pending / Validated / Invalidated), and `Bzm2PersistedCalibrationProfile::is_compatible` rejects only `Invalidated` profiles at startup. However, **nothing in the driver currently writes `Invalidated`** - the runtime retune triggers mark the point `Pending`. Net effect: a profile whose operating point was found bad at runtime is still replayed on the next restart, and correction relies on the runtime retune triggers firing again after replay (which they do - so the system self-corrects, at the cost of one suboptimal startup cycle).

Options, in our order of preference:
1. Write `Invalidated` when a retune trigger fires persistently (the state exists for exactly this; small change in the monitor's reconcile path), or
2. Keep current behavior and treat replay-then-retune as the intended startup strategy - in which case `Invalidated` is dead state and could be dropped.

Happy to push (1) as a commit on this PR if maintainers agree; the accompanying docs (bzm2-pnp.md in #71) have been corrected to describe the actual current behavior either way.


### recklessnode on 2026-07-22

﻿Implemented as option 1 in `c4e714e` ("fix(bzm2): invalidate saved operating point on persistent retune"), now on this PR:

- When runtime retune triggers fire persistently (past the 3-poll tracker), `reconcile_saved_operating_point_status` writes `Invalidated` (persisted through the existing store path) instead of `Pending`. The untouched startup `is_compatible` check then refuses the profile, and the board falls back to live calibration instead of replaying a known-bad operating point.
- New test `persistent_retune_triggers_invalidate_saved_operating_point` proves the persisted profile JSON flips to `invalidated` on the persistence threshold; the existing `reconcile_saved_operating_point_status_invalidates_profile` test now matches its name.
- The lifecycle docs in #71 describe the fixed behavior.

Also note: the whole series was rebased onto current main today (scheduler rework, dynamic expected-hashrate - `Bzm2Thread` now implements `configure()` and emits `ExpectedHashRate` like the in-tree drivers) and every commit passes `just checks` (fmt, clippy -D warnings, test) to match the new per-commit CI. All four PRs show mergeable again.


### recklessnode on 2026-07-22

﻿**Series merge order (updated 2026-07-22)** - four stacked PRs, all MERGEABLE, each green under `just checks` (fmt + `clippy --release -D warnings` + test) on **every commit**. Merge strictly in order:

1. **#68** `bzm2/pr1-infra` - generic infrastructure, zero BZM2 code (per-board command channel wiring upstream's own `SetFanTarget`, `board/power.rs` rail primitives, `HashThread` telemetry types, `attach_configured_board`). Standalone-useful; base of the stack.
2. **#69** `bzm2/pr2-asic-core` - BZM2 protocol/UART/clock/thread layer **+ serial-robustness hardening**. Hard-depends on #68's `HashThread` telemetry types (won't compile without them).
3. **#70** `bzm2/pr3-board-tuning` - board driver + tuning planner. Drives #69's ASIC layer; uses #68's `command_tx`/`power`.
4. **#71** `bzm2/pr4-diagnostics` - HTTP diagnostic endpoints + docs. Forwards `BoardCommand`s that #70's board answers; hardware reference docs link to the maintained [bzm2-hwref](https://github.com/Blockscale-Solutions/bzm2-hwref).

The order is the compile dependency chain (verified at import level - no PR references a symbol from a later one), not a preference. Merging #68 first collapses #69's visible diff to its own commits, and so down the stack. Later commits added today (the runtime-retune invalidation fix on #70, the serial hardening on #69) are folded into the PR whose code they touch, keeping each PR correct-from-first-commit rather than fixed-in-a-later-PR.


### recklessnode on 2026-09-28

Superseded by #117, which carries this work rebuilt on current main and exercised on real hardware (three hashboards, 300 BZM2 ASICs, mining to a public pool).
