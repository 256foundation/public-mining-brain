# 256foundation/mujina pull request #117: feat(bzm2): add BZM2 ASIC support

> Source: https://github.com/256foundation/mujina/pull/117
> Collected: 2026-10-07
> Published: 2026-09-28

- Repository: 256foundation/mujina
- Type: pull request
- Number: 117
- State: open
- Author: recklessnode
- Opened: 2026-09-28
- Closed: n/a
- Labels: none

## Description

This restructures the single-commit PR into 22 reviewable commits, in dependency order, each
passing `just ci` alone: the original commit taken apart along the lines discussed in #28 (BZM2
background) and at the 2026-09-28 dev call (#115), one ASIC/UART protocol driver independent of
any one board or chassis, plus the fixes for the review findings below.

What moved out, per that call: the hashboard-MCU and platform-wiring code went to a follow-up PR
(RDS platform support, stacked on this one and on the general fixes below); a handful of
standalone fixes unrelated to BZM2 went to a second follow-up (general fixes). This PR is left
with exactly the ASIC/UART protocol driver: the frame codec, the UART controller, on-die sensor
streaming, engine discovery, clock control, the calibration planner, the thermal interlock, hash
dispatch and share decoding, and the API surface that exposes per-ASIC state.

The previously reviewed single-commit head was `dc5ad91`; it stays in this PR's history for
anyone comparing.

**Depends on:** nothing. **Followed by:** #120 (general fixes) and #121 (RDS platform support), both
stacked on this one.

## Commits (oldest first, 22 total)

| # | commit | title |
|---|---|---|
| 1 | `067f5ad` | feat(serial): add a veto on outbound frames |
| 2 | `1f9ec27` | feat(types): add a budget for records that repeat at wire speed |
| 3 | `cf3743f` | feat(api): add per-ASIC state to board telemetry |
| 4 | `c587291` | feat(hash_thread): let threads publish telemetry updates |
| 5 | `b9ca2f2` | feat(hash_thread): add a HashThreadError type |
| 6 | `1e04400` | feat(hash_thread): coalesce telemetry updates by time |
| 7 | `6d386dd` | feat(bzm2): add the UART frame codec and parser |
| 8 | `5212637` | feat(bzm2): add a UART controller for registers and enumeration |
| 9 | `d69d353` | feat(bzm2): configure and stream the on-die sensors |
| 10 | `2080462` | feat(bzm2): discover the engine map over TDM |
| 11 | `baab0bc` | feat(bzm2): add a read-only frame policy |
| 12 | `7e24184` | feat(bzm2): add PLL and DLL clock control |
| 13 | `16accb8` | feat(tuning): add a BZM2 calibration planner |
| 14 | `7f5376a` | feat(bzm2): add the thermal interlock and fault corroborator |
| 15 | `78776f1` | feat(bzm2): attach a hash thread and stream die telemetry |
| 16 | `bf9223e` | feat(bzm2): dispatch work behind the interlock and engine gate |
| 17 | `8ef952e` | feat(bzm2): decode results into shares |
| 18 | `c4769e6` | feat(bzm2): run UART diagnostics on an idle thread |
| 19 | `11543d9` | feat(bzm2): record chain reads for replay |
| 20 | `6bb0cde` | fix(bzm2): refuse an enumeration layout that reaches a reserved id |
| 21 | `173003a` | fix(bzm2): refuse a zero-length register read before it reaches the wire |
| 22 | `c7f8e03` | fix(bzm2): refuse an invalid register-write frame before it reaches the wire |

## Review findings from the earlier single-commit version

Eight findings were filed against the single-commit head. Three are fixed on this branch; the
other five touch the hashboard-MCU/board-integration layer, which now lives in #121, so their
fixes land there instead.

| # | finding | fixed by | lands in | discussion |
|---|---|---|---|---|
| 1 | a zero-length register read desyncs the serial reader | `173003a` | this PR | [comment](https://github.com/256foundation/mujina/pull/117#discussion_r4129429583) |
| 2 | an empty or 256-byte register write produces an invalid wire frame | `c7f8e03` | this PR | [comment](https://github.com/256foundation/mujina/pull/117#discussion_r4129429592) |
| 3 | a fan command holds the board command loop through its settle, past the API's own reply deadline | `a927ab0` | #121 | [comment](https://github.com/256foundation/mujina/pull/117#discussion_r4129429597) |
| 4 | dispatch continues after a confirmed supply-rail drop | `da10878` | #121 | [comment](https://github.com/256foundation/mujina/pull/117#discussion_r4129429600) |
| 5 | a wire ASIC id is used directly as a bus-local index | `009a323` | #121 | [comment](https://github.com/256foundation/mujina/pull/117#discussion_r4129429602) |
| 6 | bring-up fails open when on-die protection can't be confirmed | `3e4a53e` | #121 | [comment](https://github.com/256foundation/mujina/pull/117#discussion_r4129481846) |
| 7 | the raw-register API endpoints have no opt-in access control | `51710a1` | #121 | [comment](https://github.com/256foundation/mujina/pull/117#discussion_r4129545760) |
| 8 | enumeration can assign a reserved or duplicate ASIC id | `6bb0cde` | this PR | [comment](https://github.com/256foundation/mujina/pull/117#discussion_r4129567964) |

Replies are posted on each thread individually.

## Hardware baseline

The series (this PR plus #120 and #121, the tree that actually runs) has a hardware baseline: the
series' baseline, run `20261001T085812Z`, 3.5 h on all three boards of a 300-ASIC RDS platform.
Every figure is computed from that run's own files; none is typed from prose. This is the one
copy of these figures; #121 links here. A replicate
run, `20261001T014554Z`, backs up every figure (last section).

- Shares: 1207 pool-accepted inside the hold, 0 rejected, run `20261001T085812Z`.
- Hash rate, pool's own figure (Ocean, in-hold poll): range 106.02-111.34 TH/s across its 1 h and 3 h trailing windows, run `20261001T085812Z` (the 3.5 h hold is longer than either trailing window, so neither matches it exactly).
- Hash rate, derived from accepted shares and their assigned difficulty: 107.85 TH/s, 95% exact interval [101.85, 114.11] TH/s, run `20261001T085812Z`.
- Hash rate, the miner's own self-reported rate: mean 107.12 TH/s, readings spanning 97.08-116.30 TH/s, run `20261001T085812Z`.
- Supply power: mean 3674.53 W, readings spanning 3554.0-3706.0 W, run `20261001T085812Z`.
- Wall power: the meter's step for the miner is 3.469 ± 0.172 kW, with 6 unrelated house loads excluded, run `20261001T085812Z`.
- The supply's own input reading is 0.21 kW above that step, outside the meter's uncertainty, run `20261001T085812Z`. Across four runs on this build and its predecessors the gap is 0.44, 0.34, 0.21 and 0.07 kW, so it is not a fixed instrument offset; the likelier cause is the house's base load drifting under the step, which a whole-house meter cannot separate.
- A 2 h run of the build as submitted, in a quiet house: wall step 3.608 ± 0.312 kW against a supply mean of 3673.5 W, 0.07 kW apart and inside the meter's uncertainty, run `20261001T192725Z`; its share-derived rate 107.24 TH/s, 95% interval [99.37, 115.58] TH/s, run `20261001T192725Z`; wall efficiency 33.64 J/TH, interval [31.22, 36.31] J/TH, run `20261001T192725Z`.
- Efficiency, wall step against the share-derived rate: 32.17 J/TH, 28.9-35.7 J/TH with both uncertainties together, run `20261001T085812Z`.
- Efficiency, supply power against the share-derived rate: 34.07 J/TH, interval [32.20, 36.08] J/TH, run `20261001T085812Z`.
- Thermal: hottest die 81.87 °C over 223 in-hold readings, die-temperature slope +0.028 °C/min over the final 9.4 minutes of the hold, run `20261001T085812Z`.
- Operation: bring-up to first accepted share 5 s, stop to dark mean 75 s across the three boards, 0 faults/trips/scrams over the hold, run `20261001T085812Z`.
- One pool reconnect, at 10:27:43 UTC, 72 min into the hold: the stratum client could not parse a message from the pool (`Failed to parse JSON`, the line starting mid-message), disconnected, reconnected within 1 s and had its next share accepted 13 s later; the share being submitted at that moment was lost. The stratum client is upstream's and unchanged by this series, so the fix is outside it, run `20261001T085812Z`.
- Versions: series tip `a927ab0`; stock OpenWrt 18.06.2 with busybox 1.28.4; a 3-board, 300-ASIC RDS platform.
- Replicate, run `20261001T014554Z` (3 h): share-derived rate interval [96.89, 109.85] TH/s and efficiency interval [33.42, 37.89] J/TH both overlap this run's intervals, run `20261001T085812Z`; its self-reported mean 107.38 TH/s is within 0.3 TH/s of this run's 107.12 TH/s, run `20261001T014554Z`.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

https://claude.ai/code/session_012tKbAMHoFAEgGVb8PenGTV


## Comments

### recklessnode on 2026-09-29

This is great @j-kon thank you! I am having claude refactor the PR (per my conversation with Ryan) into a more reasonable PR series of commits. And I am fixing the issues you outlined above. When that is done, a new PR series will be submitted that is way more OSS compatible than this monolithic single commit, and more easily auditable going forward. I also failed to check existing PRs and existing GH Issues, and am working to not clobber other folks' work as well.

### recklessnode on 2026-10-01

Restructured this into 22 commits, in dependency order, each passing `just ci` alone: the same
change taken apart along the lines discussed in #28 and at the
2026-09-28 dev call (#115): one ASIC/UART protocol driver, independent of any one board or
chassis, plus the fixes for your review findings.

What moved out:

- the hashboard-MCU and platform-wiring code, to a follow-up PR (RDS platform support), stacked on
  this one;
- four standalone fixes unrelated to BZM2, to a second follow-up (general fixes), also stacked on
  this one.

Both follow-ups are open as drafts and link back here.

The previous single-commit head was `dc5ad91`; it stays in this PR's history for anyone comparing.

Thanks for the review, @j-kon — replying to each thread individually below.
