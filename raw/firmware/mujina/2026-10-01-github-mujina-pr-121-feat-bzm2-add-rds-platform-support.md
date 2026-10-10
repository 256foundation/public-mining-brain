# 256foundation/mujina pull request #121: feat(bzm2): add RDS platform support

> Source: https://github.com/256foundation/mujina/pull/121
> Collected: 2026-10-07
> Published: 2026-10-01

- Repository: 256foundation/mujina
- Type: pull request
- Number: 121
- State: open
- Author: recklessnode
- Opened: 2026-10-01
- Closed: n/a
- Labels: none

## Description

The RDS-specific layer on top of the BZM2 protocol driver (#117) and the general fixes (#120): the
hashboard MCU (identity, fault history, heartbeat), supply-rail sequencing and bring-up, the
power-on self-test, the abort/scram ladder, run-time calibration and efficiency reporting, fan
control, and the platform descriptor the chassis facts live in.

This is deliberately **not** folded into the chip driver. The new `board/bzm2/platform.rs` states
the line this PR draws: if swapping the chassis would change a fact, it belongs here; if swapping
the hashboard would change it, it belongs in the chip driver (#117) instead. Board count, the I²C
adapter numbering, and chain-port naming are chassis facts and live here as a `Bzm2Platform`
constant, not as literals scattered through the board code.

**Depends on #117 and #120. Its first 26 commits are those PRs'; review only
the last 27.**

## Commits (the last 27 are this PR's own)

| # | commit | title |
|---|---|---|
| 1 | `2b7106d` | feat(serial): apply platform control flags with baud verification |
| 2 | `b3043b1` | feat(i2c): add a Linux i2c-dev backend |
| 3 | `04841dc` | feat(types): add an efficiency type with power provenance |
| 4 | `e25018f` | feat(tuning): add a thermal runaway check |
| 5 | `1d6a1b5` | feat(api): report efficiency per power domain |
| 6 | `cd3e36d` | feat(api): record when each temperature was read |
| 7 | `defc820` | feat(scheduler): stagger chain starts |
| 8 | `a97d031` | feat(scheduler): stagger chain stops on pause |
| 9 | `4280e24` | feat(bzm2): add the BZM2 board and attach it from configuration |
| 10 | `a614a1c` | feat(bzm2): sequence supply rails and poll board sensors |
| 11 | `c7e3137` | feat(bzm2): add the hashboard MCU: identity, fault history, heartbeat |
| 12 | `6422f62` | feat(bzm2): judge the machine against its declaration before power-up |
| 13 | `ae448f9` | feat(bzm2): stop and de-energise on abort conditions |
| 14 | `1e7aa75` | feat(bzm2): watch for stalled and lost chains and report limit coverage |
| 15 | `d85aa2e` | feat(bzm2): drive the fans from the hottest die |
| 16 | `c778d22` | feat(bzm2): calibrate the board at start-up with the planner |
| 17 | `ed1aff2` | feat(bzm2): persist and replay a sealed operating-point profile |
| 18 | `46d0026` | feat(bzm2): re-evaluate tuning at run time and report efficiency |
| 19 | `500b6b3` | feat(bzm2): serve board diagnostics over the API |
| 20 | `6c5c7f8` | feat(bzm2): add a computed per-ASIC summary endpoint |
| 21 | `51710a1` | fix(bzm2): require opt-in for raw register access over the API |
| 22 | `e8f3f19` | fix(bzm2): require the per-ASIC nameplate rate instead of guessing it |
| 23 | `66ea25a` | docs(bzm2): document every BZM2 and raw-register environment variable |
| 24 | `3e4a53e` | fix(bzm2): refuse to calibrate with on-die protection unconfirmed |
| 25 | `da10878` | fix(bzm2): stop dispatch and scram on a confirmed rail drop |
| 26 | `009a323` | fix(bzm2): map the wire ASIC id to its index before using it as one |
| 27 | `a927ab0` | fix(fans): hold the command loop only for the fan duty write |

## Open question: a second BZM2 platform

The one `Bzm2Platform` defined here (`rds-2.0`) is a 3-board, 300-ASIC chassis. Whether a future
second BZM2 platform would share this same hashboard-MCU layer, or need its own, is open — raised
here for discussion, not as a request. The `platform.rs` split above is written so that answering
it later is a new constant and a test, not a rewrite.

## Review findings fixed in this PR

Five of the eight findings filed against the earlier single-commit version touch the hashboard-MCU
or board-integration layer, which lives here rather than in the chip driver (#117). All five are
fixed on this branch.

| # | finding | fixed by | one line of the fix | discussion |
|---|---|---|---|---|
| 3 | a fan command holds the board command loop through its settle, past the API's own reply deadline | `a927ab0` | the duty write is awaited inline and replied to immediately; the settle and tach read run in a spawned task | [comment](https://github.com/256foundation/mujina/pull/117#discussion_r4129429597) |
| 4 | dispatch continues after a confirmed supply-rail drop | `da10878` | a confirmed drop now takes the monitor ladder's own scram rung, stopping dispatch first | [comment](https://github.com/256foundation/mujina/pull/117#discussion_r4129429600) |
| 5 | a wire ASIC id is used directly as a bus-local index | `009a323` | both monitor call sites now convert through `global_asic_id_from_wire` before indexing | [comment](https://github.com/256foundation/mujina/pull/117#discussion_r4129429602) |
| 6 | bring-up fails open when on-die protection can't be confirmed | `3e4a53e` | an unconfirmed chain now refuses and scrams the whole board instead of logging and continuing | [comment](https://github.com/256foundation/mujina/pull/117#discussion_r4129481846) |
| 7 | the raw-register API endpoints have no opt-in access control | `51710a1` | both endpoints refuse with 403 unless explicitly enabled, and refuse a non-loopback bind unless remote access is also explicitly enabled | [comment](https://github.com/256foundation/mujina/pull/117#discussion_r4129545760) |

The other three findings (zero-length register reads, invalid register-write frames, reserved
enumeration ids) are protocol-level and fixed in #117 directly.

## Hardware baseline

The series' baseline ran on this platform: run `20261001T085812Z`, 3.5 h on all three boards of the 300-ASIC RDS platform this PR adds, with a replicate run `20261001T014554Z`. The full figures are in #117, their one copy.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

https://claude.ai/code/session_012tKbAMHoFAEgGVb8PenGTV
