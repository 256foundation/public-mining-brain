# Hackathon Harvest — Provenance & Status

**Origin:** `256foundation/public-brain` — a 2-hour hackathon MVP built 2026-10-07 by ~8 contributors using the same karpathy-llm-wiki method. Not fully vetted. The old repo (incl. the redundant HTML/SRT/VTT transcript originals) remains at github.com/256foundation/public-brain; its branches are merged here as `main + wiki-new-sources` (the other branches had no unique commits).

## What's in here

| Path | Contents |
|---|---|
| `hackathon-harvest/raw/` | ~500 raw source captures with metadata headers: ESP-Miner/Bitaxe issue archive (2022→2024), asic-rs complete PR/issue history (#1–#409), HashScope + btc-toolkit scrapes, OSMU wiki pages (incl. the ASIC reverse-engineering Lab pages BM1397/BM1362/BM1366/BM1368/BM1370), 256F site captures, 61 POD256 episode transcripts (md), BIP 310/320 texts, newsletter archives |
| `hackathon-harvest/scripts/download_pod256.py` | Their transcript downloader — candidate to adapt for the capture layer's POD256 refresh |
| `hackathon-wiki/` | ~70 compiled candidate drafts (foundation, hardware, mujina, hydrapool, ecosystem, pod256, newsletter, protocols, tools) incl. the `wiki-new-sources` branch additions (POD256 digests 086–092, X archive/timeline articles) |

## Verification status: UNVERIFIED — treat as leads

- Their compiled pages carry Sources/Raw headers and are internally citation-linked, but the chain starts at hackathon captures that Tyler has not vetted.
- **Numbers re-verify at compile time**: when Phase 2 compiles wiki pages from this material, the grounding invariant applies on OUR chain — every load-bearing fact must be located in OUR raw files, and `scripts/lint_wiki.py` greps them mechanically.
- Conflicts between hackathon pages and authoritative sources resolve toward the authoritative source; unresolved conflicts become Disputed blocks (their pages already model this well — e.g., Ember One GPL-vs-CERN-OHL license conflict).
- Anything that looks wrong, promotional, or unsourced gets dropped at triage. Noise is expected; it dies here without ever reaching `wiki/`.

## Next step

Gate approval → triage moves this material from inbox into topic directories → compile begins, this harvest first (it is the largest ready-made corpus, covering the open-source ecosystem pillar).
