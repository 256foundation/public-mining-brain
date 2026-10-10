# 256foundation/mujina pull request #71: feat(api): BZM2 diagnostic endpoints and hardware documentation

> Source: https://github.com/256foundation/mujina/pull/71
> Collected: 2026-10-07
> Published: 2026-06-11

- Repository: 256foundation/mujina
- Type: pull request
- Number: 71
- State: closed
- Author: recklessnode
- Opened: 2026-06-11
- Closed: 2026-09-28
- Labels: none

## Description

Part 4 of the BZM2 series (stacked on parts 1–3 — review the `feat(api)` commit). Completes the series with the HTTP diagnostics surface and the hardware reference documentation.

## Endpoints

Eight endpoints under `/api/v0/boards/{name}/bzm2/`, each forwarding a `BoardCommand` through the board's command channel (part 1's plumbing) with a 5 s reply timeout; boards without a command channel answer 400:

| Endpoint | Purpose |
|---|---|
| `POST dts-vs-query` | trigger an on-die temperature/voltage sensor read; returns refreshed board telemetry |
| `POST noop` | liveness probe; returns the chip's 3-byte `"BZ2"` payload |
| `POST loopback` | echo a hex payload through the ASIC |
| `POST register-read` / `register-write` | raw engine/local register access |
| `POST clock-report` | PLL/DLL status registers, decoded |
| `GET chain-summary` | bus/ASIC layout + startup path + saved-operating-point status |
| `POST discover-engines` | TDM engine-map scan (idle threads only); returns refreshed telemetry with per-ASIC hole maps |

Request/response DTOs carry OpenAPI schemas; integration tests drive every endpoint against a command-capable fake board, including telemetry-refresh round trips.

## Documentation (`docs/bzm2/`)

Port architecture notes, tuning-planner (PnP) notes, opcode grounding, hardware integration guide, UART/TDM protocol reference, and the reference roadmap — the BZM2 is publicly documented, and these are the review companion for parts 2–3. README gains the BZM2 entry under Current Status plus doc links and related projects.

This PR supersedes #66 (the standalone docs PR) — the documents now land with the code they describe.

Gates: `cargo build` (0 warnings), `cargo test` (390 passed / 0 failed), `cargo fmt` clean.

🤖 Generated with [Claude Code](https://claude.com/claude-code)


## Comments

### recklessnode on 2026-06-11

**Series:** #68 (infra) -> #69 (asic core) -> #70 (board + tuning) -> #71 (diagnostics + docs). Each part builds and tests green standalone; later parts are stacked, so their diffs include predecessors - review by commit.

### recklessnode on 2026-07-22

﻿Following up on the 2026-06-15 dev call (discussion #73): the concern about general reference documentation living in-tree applies to part of this PR too, so we have resolved it proactively in `d9ab286`:

- `docs/bzm2/` now carries **only the three documents that describe code in this tree**: the port architecture notes, the tuning-planner (PnP) notes, and the opcode grounding.
- The **hardware reference** (integration guide, UART/TDM protocol reference, reference roadmap) has moved to its canonical home: [bzm2-hwref](https://github.com/Blockscale-Solutions/bzm2-hwref) - the public, CC-BY-SA BZM2 hardware reference Reckless Systems maintains with access to the original collateral. The README now links there instead of carrying copies (-1,326 lines from this PR).

That implements the principle from the call: nothing unmaintained lives in-tree; the tree links to a maintained external home. Same proposal posted to #73 for the tabled where-should-reference-docs-live question; #66 closes in favor of this arrangement.


### recklessnode on 2026-07-22

﻿**Series merge order (updated 2026-07-22)** - four stacked PRs, all MERGEABLE, each green under `just checks` (fmt + `clippy --release -D warnings` + test) on **every commit**. Merge strictly in order:

1. **#68** `bzm2/pr1-infra` - generic infrastructure, zero BZM2 code (per-board command channel wiring upstream's own `SetFanTarget`, `board/power.rs` rail primitives, `HashThread` telemetry types, `attach_configured_board`). Standalone-useful; base of the stack.
2. **#69** `bzm2/pr2-asic-core` - BZM2 protocol/UART/clock/thread layer **+ serial-robustness hardening**. Hard-depends on #68's `HashThread` telemetry types (won't compile without them).
3. **#70** `bzm2/pr3-board-tuning` - board driver + tuning planner. Drives #69's ASIC layer; uses #68's `command_tx`/`power`.
4. **#71** `bzm2/pr4-diagnostics` - HTTP diagnostic endpoints + docs. Forwards `BoardCommand`s that #70's board answers; hardware reference docs link to the maintained [bzm2-hwref](https://github.com/Blockscale-Solutions/bzm2-hwref).

The order is the compile dependency chain (verified at import level - no PR references a symbol from a later one), not a preference. Merging #68 first collapses #69's visible diff to its own commits, and so down the stack. Later commits added today (the runtime-retune invalidation fix on #70, the serial hardening on #69) are folded into the PR whose code they touch, keeping each PR correct-from-first-commit rather than fixed-in-a-later-PR.


### recklessnode on 2026-09-28

Superseded by #117, which carries this work rebuilt on current main and exercised on real hardware (three hashboards, 300 BZM2 ASICs, mining to a public pool).
