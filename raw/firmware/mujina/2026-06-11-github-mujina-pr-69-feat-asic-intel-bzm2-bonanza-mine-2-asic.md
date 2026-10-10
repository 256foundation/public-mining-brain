# 256foundation/mujina pull request #69: feat(asic): Intel BZM2 (Bonanza Mine 2) ASIC family support

> Source: https://github.com/256foundation/mujina/pull/69
> Collected: 2026-10-07
> Published: 2026-06-11

- Repository: 256foundation/mujina
- Type: pull request
- Number: 69
- State: closed
- Author: recklessnode
- Opened: 2026-06-11
- Closed: 2026-09-28
- Labels: none

## Description

﻿Part 2 of the BZM2 series (stacked on part 1 — review the `feat(asic)` commit). Adds the ASIC-family layer for the **Intel BZM2 (Bonanza Mine 2)**, the chip the 256 Foundation received as a 54,000-unit grant and that the Satoshi Starter / bitaxeBIRDS board family is built around.

The layout mirrors the in-tree `bm13xx` structure (pure codec → controller → `HashThread`):

- **`protocol.rs`** — opcodes, frame encoders (`write_job`, `write_register`, `noop`, `loopback`, `read_result`), TDM frame/result parsers, the 20×12 logical engine grid (236 active engines by default), target→leading-zeros conversion. Depends on `bitcoin` + std only.
- **`uart.rs`** — `Bzm2UartController` for the chip's 9-bit multidrop UART: register R/W (unicast/multicast/local), NOOP `"BZ2"` verification, chain enumeration (ID-assignment walk from the `0xFA` power-on default), TDM enable and synchronized reads, engine-map discovery, loopback, and DTS/VS (on-die temperature/voltage sensor) configure + query.
- **`clock.rs`** — `Bzm2ClockController`: PLL/DLL program/enable/lock-wait, per-ASIC and broadcast, plus clock debug reports.
- **`thread.rs`** — `Bzm2Thread` implementing `HashThread`: direct UART work dispatch, TDM result handling with per-ASIC/per-PLL hashrate estimation, DTS/VS telemetry emitted via `HashThreadEvent::TelemetryUpdate` (from part 1), thermal-trip frame handling, and a diagnostics handle used by the board layer in part 3.

Unlike the BM13xx family, the BZM2 is publicly documented — the protocol reference and integration guide land with part 4 (CC-BY-SA), so this driver can be reviewed against the chip's actual documentation rather than reverse engineering.

Tests are PTY-based chain emulations (multi-ASIC enumeration, TDM result paths, DTS/VS frames), gated `#[cfg(all(test, unix))]` so non-Unix hosts build the crate cleanly.

Gates: `cargo build` (0 warnings), `cargo test` (362 passed / 0 failed), `cargo fmt` clean.

🤖 Generated with [Claude Code](https://claude.com/claude-code)



---

## Serial-robustness hardening (added 2026-07-22)

An internal adversarial audit of this PR's serial parser/actor against hostile and malformed
multidrop-UART input surfaced five defects **in the code this PR introduces**. They are fixed here
as discrete, individually-tested `fix(bzm2):` commits on top of the `feat(asic)` commit, so the ASIC
layer is robust on a noisy real-world bus from the first commit rather than being hardened in a later
PR. Each is independently reviewable and CI-green per commit.

- **Parser hang + unbounded buffer on line noise** (`protocol.rs`): a `READREG`-looking prefix with
  no pending read wedged framing at cursor 0 and grew the buffer on every read. Now resyncs one byte
  forward (matching the unknown-opcode arm), keeping strictly-forward progress and a bounded buffer.
- **Silent drop of fault frames for out-of-range ASIC ids** (`protocol.rs`): the `asic >= 100` resync
  heuristic dropped DTS/VS trip/fault frames too — reachable via `MUJINA_BZM2_ENUM_START_ID`, which
  silently disabled over-temp protection for the bus. DTS/VS frames are now exempt from the heuristic.
- **Unbounded diagnostic + enumeration reads** (`thread.rs`, `uart.rs`): bare `read_exact` in the
  diagnostic handlers and in `enumerate_chain`'s post-assign verify let a silent chip freeze the
  single-task actor (including `Shutdown`) or wedge board init. Both are now time-bounded.
- **DTS/VS trip acted on without validation** (`thread.rs`): a single frame with a fault bit set
  killed the thread permanently — DoS-by-noise. Fault decisions are now gated on the matching
  sensor-enable bit; a genuine over-temp still stops immediately (no debounce). Residual risk noted
  in a code comment (the protocol carries no checksum).

Two lower-severity findings (generation-mismatch mis-framing; 1-bit nonce-replay double-count) are
deferred with rationale — both would need invasive changes that risk dropping valid frames/shares,
and the safety-relevant consequence of the first is already mitigated by the DTS/VS enable-gate.
A scheduler thread-respawn observation is upstream's own code and out of scope for this series.


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


### recklessnode on 2026-09-28

Superseded by #117, which carries this work rebuilt on current main and exercised on real hardware (three hashboards, 300 BZM2 ASICs, mining to a public pool).
