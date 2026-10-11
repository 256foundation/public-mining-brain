# Capture report — Undermine 2025 (Heatpunk Summit) transcripts

- Playlist: https://www.youtube.com/watch?v=videoseries?list=PLgYVdSZznAdN3scDRRbUktk6quW3RtMgA
- Channel: The Space (all 14 videos)
- Collected: 2026-10-10 with yt-dlp 2026.08.19 (json3 caption tracks, converted to timestamped markdown)
- Caption type for all 14: **auto** (YouTube ASR; `en` track with `acAsrConf` segment markers; no manual "Available subtitles" tracks published on any of the 14)
- Method: json3 `events` rebuilt into a caption line stream, consecutive duplicate rolling-caption lines collapsed, chunked into paragraphs of ~30-45 s prefixed `[HH:MM:SS]`. Text kept verbatim (including `>>` speaker-change markers, `[applause]`/`[laughter]`/`[music]` ASR tags, and spoken-number spellouts). No speaker names inferred.
- Failures: none. All 14 fetched and converted on first attempt.
- Parked (no captions at all): none.

| # | Video ID | Title | Duration | Caption type | Words | File written |
|---|----------|-------|----------|--------------|-------|--------------|
| 1 | xarEPPMGdxU | What are the challenges ahead for hashrate heading? | 52:16 | auto | 10,175 | 20251111-undermine-2025-what-are-the-challenges-ahead-for-hashrate-heading.md |
| 2 | E6FjPhL5xWo | The bitcoin ASIC frontier | 45:54 | auto | 7,955 | 20251111-undermine-2025-the-bitcoin-asic-frontier.md |
| 3 | T5soho5GL2w | Datum Setup Tutorial with Bitcoin Mechanic | 52:54 | auto | 9,675 | 20251111-undermine-2025-datum-setup-tutorial-with-bitcoin-mechanic.md |
| 4 | jocM1WBbbTA | Bitcoin mining firmware discussion | 41:36 | auto | 8,380 | 20251111-undermine-2025-bitcoin-mining-firmware-discussion.md |
| 5 | 5kMTeJmEe7Q | Debate on bitcoin mining heat delivery systems | 46:51 | auto | 9,559 | 20251111-undermine-2025-debate-on-bitcoin-mining-heat-delivery-systems.md |
| 6 | 1SLPMWANvoU | Controlling Hashrate Heaters | 44:23 | auto | 9,789 | 20251111-undermine-2025-controlling-hashrate-heaters.md |
| 7 | otYQgWMFlJ8 | The Heatpunk's Manifesto | 51:15 | auto | 9,875 | 20251111-undermine-2025-the-heatpunks-manifesto.md |
| 8 | G3zLz-8cB_I | Exploring the bitcoin mining adoption landscape | 42:13 | auto | 6,781 | 20251111-undermine-2025-exploring-the-bitcoin-mining-adoption-landscape.md |
| 9 | 5TwnzMPvjP0 | Small-scale bitcoin mining panel | 35:44 | auto | 7,248 | 20251111-undermine-2025-small-scale-bitcoin-mining-panel.md |
| 10 | 91Db7ckw3XQ | Bitcoin Mining Heat Reuse book release with Tyler Stevens | 11:45 | auto | 2,136 | 20251111-undermine-2025-bitcoin-mining-heat-reuse-book-release-with-tyler-stevens.md |
| 11 | aeEIgNOcPB0 | Bitcoin mining business models roundtable | 44:39 | auto | 8,575 | 20251111-undermine-2025-bitcoin-mining-business-models-roundtable.md |
| 12 | f3e96xtfFg4 | Exploring the heat reuse potential of bitcoin mining | 45:18 | auto | 7,873 | 20251111-undermine-2025-exploring-the-heat-reuse-potential-of-bitcoin-mining.md |
| 13 | tR0tAfxsuSs | Overview of bitcoin mining for novices | 31:52 | auto | 5,479 | 20251111-undermine-2025-overview-of-bitcoin-mining-for-novices.md |
| 14 | UgL4H89O73c | UnderMine 2025 Opening Remarks with Cody Harris and Tyler Stevens | 7:32 | auto | 1,510 | 20251111-undermine-2025-undermine-2025-opening-remarks-with-cody-harris-and-tyler-stevens.md |

Total: 14/14 captured, 105,988 words of machine-caption transcript.

Verification notes:
- Last caption timestamp of every file falls within ~40 s of the video end (final cue; no truncation).
- Intervals between paragraph timestamps are ≤ 63 s everywhere; the two largest (51 s in #6 at 42:26, 63 s in #8 at 32:34) were checked against the raw json3 and correspond to genuine caption silence (demo/no-speech segments), not dropped text.
- Video 1 note: YouTube's own title reads "hashrate heading?" (sic) — preserved as published; the filename keeps yt-dlp's full-width `？` sanitization in the intermediate only.
- Intermediate `.en.json3` caption files were removed after conversion; each markdown file is the complete talk.
