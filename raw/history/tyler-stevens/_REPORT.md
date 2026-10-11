# Capture report — tyler-stevens (capture-loop A3)

- Collected: 2026-10-10
- Scope: 8 YouTube appearances indexed at https://www.tylerstevens.me/content (registry row `tyler-stevens-site`)
- Method: yt-dlp auto-caption capture (`--write-auto-sub --sub-lang en --sub-format json3`), converted to timestamped markdown paragraphs (~30–45s chunks, `[HH:MM:SS]` prefix). Text verbatim as captioned; no per-line speaker attribution (caption-native `>>` change markers preserved). Rolling-caption duplicates deduped. Speaker identifications taken from the source page, header only.
- Note: TFTC (2-txiZKNIRk) required a workaround — the timedtext endpoint returned HTTP 429 to yt-dlp repeatedly; the caption track URL was extracted from video metadata and fetched directly with curl (succeeded, HTTP 200). The `.en` and `.en-orig` tracks were byte-identical for every video.

## Per-video results

| Video ID | Item (per tylerstevens.me/content) | Channel | Upload date | Caption status | Transcript words | File |
|---|---|---|---|---|---|---|
| CUdfjnBd8Jo | Tangents Podcast - Reverse Engineering an Industry (2026-09-02) | Tangents | 2026-09-03 | OK (auto-captions) | 2,118 | `20260903-tangents-reverse-engineering-an-industry.md` |
| 2-txiZKNIRk | TFTC Podcast with Marty Bent - The Home Mining Playbook (2026-07-01) | TFTC | 2026-07-01 | OK (auto-captions; via curl after 429s) | 15,298 | `20260701-tftc-the-home-mining-playbook.md` |
| 7ejGaM-BGRg | Texas Energy & Mining Summit 2026 - Shovels in the Ground (2026-05-20) | Bitcoin Park | 2026-07-24 | OK (auto-captions) | 6,889 | `20260724-texas-energy-mining-summit-shovels-in-the-ground.md` |
| piOpRifhJXc | Bringing Bitcoin Mining Back Home: The Heatpunk Movement Explained (Bitcoin Well webinar, 2026-05-05) | Bitcoin Well | 2026-04-28 | OK (auto-captions) | 16,447 | `20260428-bitcoin-well-deep-dive-heatpunk-movement.md` |
| egF4J7L2iZ4 | Bitcoin Conference Las Vegas 2026 - Decentralizing Bitcoin: The Solo Mining Movement (2026-04-27) | Peter JusticeForTheVictims Ryszkiewicz | 2026-05-01 | OK (auto-captions) | 5,777 | `20260501-bitcoin-2026-decentralizing-bitcoin-solo-mining-movement.md` |
| Xi0M5NLxm20 | Bitcoin Conference Las Vegas 2026 - Open-Sourcing the Bitcoin Mining Ecosystem (2026-04-27) | Bitcoin Magazine | 2026-05-14 | OK (auto-captions) | 5,651 | `20260514-bitcoin-2026-open-sourcing-the-bitcoin-mining-ecosystem.md` |
| tV62kDRUyJw | Bitcoin Conference Las Vegas 2026 - Heating Entrepreneurs: Productizing Waste Heat (2026-04-27) | Bitcoin Magazine | 2026-05-12 | OK (auto-captions) | 7,003 | `20260512-bitcoin-2026-heating-entrepreneurs-productizing-waste-heat.md` |
| svHSq9t0c-I | Bitcoin Rails Podcast - Hashing for Heat with Tyler Stevens (2026-04-14) | Isabel Foxen Duke | 2026-04-14 | OK (auto-captions) | 14,662 | `20260414-bitcoin-rails-hashing-for-heat.md` |

8/8 captured. Word counts are transcript-only (headers and timestamps excluded). Each transcript's final timestamp reaches within ~30s of the video's full duration (verified: no truncation).

## Park list — /content items with no YouTube transcript to capture

Items on https://www.tylerstevens.me/content (page 1) whose embeds link off-YouTube; no machine transcript capturable by this loop:

1. **Freedom Tech Deep Dive | How to Keep Bitcoin Mining Decentralized** (Oslo Freedom Forum 2026 panel, 2026-06-02) — links to an X post (https://x.com/tylerkstevens/status/2062890359282397391), no YouTube embed. Tyler moderated; panelists Matt Corallo (Stratum V2), Skot (Bitaxe / 256 Foundation), Janet Maingi (Gridless Compute).
2. **Bitcoin Audible Chat 168 - Hashing for Heat with Tyler Stevens** (podcast, 2026-05-21) — links via t.co to the audio podcast (Apple Podcasts / Fountain ecosystem; Bitcoin Audible is audio-first), no YouTube version. Guy Swann with Tyler Stevens.

Note for the orchestrator: `/content/2` and deeper contain further items, several also off-YouTube (Heatpunk Summit recordings at heatpunks.org, Imagine IF 2025 keynote on X, TFTC #655 on X, Bitcoin Alaska keynote, Hashrate Up podcast, Book Breakdown videos, Home Mining Podcast). One additional YouTube link exists on page 2 (`ZYk6ve5ibSQ` Nashville Energy & Mining Summit panel, `H4faYFvQYOQ` Home Mining Podcast) — outside the approved A3 list of 8, not captured.
