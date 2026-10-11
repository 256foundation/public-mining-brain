# HPS 2026 Transcript Capture — Report

Agent: capture-loop A3 (subagent). Collected: 2026-10-10.
Pipeline: yt-dlp 2026.08.19 (`--skip-download --write-auto-sub --write-sub --sub-lang en --sub-format json3`) → json3→markdown (word-level rolling-repeat dedupe, ~30–45s paragraphs, `[HH:MM:SS]` prefix, verbatim as captioned, no speaker-name inference).
Playlist: 2026 Heatpunk Summit `PLgYVdSZznAdM7JVqScdZcKJ5i4ILABNC4` (channel: The Space).

## Captured — 13 of 13 priority videos (all had English captions)

| # | Video ID | Title | Published | Words | Last TS / Duration |
|---|----------|-------|-----------|-------|--------------------|
| 1 | 4FEwVYIvvSU | Heatpunk Hydronics: Boiler Walkthrough (Workshop 2) | 20260305 | 7,426 | 00:37:52 / 38:14 |
| 2 | k_x48ErmSh8 | Home Assistant Deep Dive (Workshop 1) | 20260303 | 4,473 | 00:38:44 / 38:52 |
| 3 | EtJaUA2-okg | Intro to Mining SDK with Tether (Workshop 3) | 20260310 | 5,896 | 00:37:51 / 37:59 |
| 4 | evlNZsmOYW8 | Dismantling the Proprietary Mining Empire: This is the 256 Foundation (Talk 15) | 20260305 | 6,510 | 00:36:07 / 36:41 |
| 5 | 8HtS6QTYTUo | Your Heat, Hash & Rules: Pool Payout Sovereignty (Talk 14) | 20260305 | 6,563 | 00:32:52 / 33:21 |
| 6 | eeEZIJ78W-0 | The Asset-Liability Flip: When Buildings Print Money (Talk 12) | 20260305 | 6,561 | 00:36:16 / 36:43 |
| 7 | J7W-ZTTalys | Precision BTU: The Economics of BTC Heater Sizing (Talk 13) | 20260305 | 5,911 | 00:31:18 / 31:29 |
| 8 | geMRKorVKmQ | Cutting Through Regulatory BS (Talk 11) | 20260305 | 6,423 | 00:36:14 / 36:28 |
| 9 | OZ954alVytM | Chips on the Table: Home-Mining Hardware & ASICs (Talk 6) | 20260303 | 6,185 | 00:35:07 / 35:11 |
| 10 | tIJDsZ7fzqw | Set & Forget: Ideal Control for Hashrate Heat (Talk 5) | 20260303 | 6,668 | 00:32:50 / 32:58 |
| 11 | AztBa4qPpiY | Large Scale Heatpunks: Mining or Heating? (Talk 3) | 20260303 | 6,559 | 00:36:52 / 36:58 |
| 12 | 0Z99qdTS4x8 | Welcome Remarks & Defining An Industry Keynote (Talk 1) | 20260302 | 3,265 | 00:15:42 / 16:17 |
| 13 | yua2M13XEjw | Building the Heatpunk Workforce (Talk 10) | 20260310 | 6,280 | 00:32:17 / 32:33 |

Total: 78,154 words across 13 files. Every transcript's final timestamp verified within ~30s of video duration (full talk, no truncation).

## Files

- `20260305-hps-2026-heatpunk-hydronics-boiler-walkthrough-workshop-2.md`
- `20260303-hps-2026-home-assistant-deep-dive-workshop-1.md`
- `20260310-hps-2026-intro-to-mining-sdk-with-tether-workshop-3.md`
- `20260305-hps-2026-dismantling-the-proprietary-mining-empire-this-is-the-256-foundation-talk-15.md`
- `20260305-hps-2026-your-heat-hash-rules-pool-payout-sovereignty-talk-14.md`
- `20260305-hps-2026-the-asset-liability-flip-when-buildings-print-money-talk-12.md`
- `20260305-hps-2026-precision-btu-the-economics-of-btc-heater-sizing-talk-13.md`
- `20260305-hps-2026-cutting-through-regulatory-bs-talk-11.md`
- `20260303-hps-2026-chips-on-the-table-home-mining-hardware-asics-talk-6.md`
- `20260303-hps-2026-set-forget-ideal-control-for-hashrate-heat-talk-5.md`
- `20260303-hps-2026-large-scale-heatpunks-mining-or-heating-talk-3.md`
- `20260302-hps-2026-welcome-remarks-defining-an-industry-keynote-talk-1.md`
- `20260310-hps-2026-building-the-heatpunk-workforce-talk-10.md`

## Parked (remaining 7 playlist videos — deliberately not fetched)

- gqJW1mlPbZ8
- K9lZusJSz5c
- DSwNslNiUN8
- QodHeWZu6-g
- 2ro83M_rUR4
- zdrAf_a3tH4
- dNKZhRVaXbM

## Failures / Notes

- None. All 13 priority videos returned English caption tracks (auto-generated json3).
- Note on priority 1: task ID `4FEwWYIvvSU` was corrected to `4FEwVYIvvSU` per task notes; used the corrected ID.
- Minor yt-dlp warnings (no JS runtime for format extraction; no impersonate target) did not affect caption downloads.
- Machine captions only: no speaker labels inferred; stage directions like `[laughter]`, `[applause]` and `>>` turn markers preserved verbatim as captioned.
