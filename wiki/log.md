# Wiki Log

Append-only operation log. Newest entries at the bottom.

## [2026-10-08] init | repository skeleton
- Disposition: New
- Created: SKILL.md, references/, scripts/lint_wiki.py, automation/AGENT-PLAYBOOK.md, sources/registry.md (draft v0.1), wiki/index.md, topic directories
- Note: taxonomy + source registry pending gate review before bulk ingest

## [2026-10-08] lint | 0 issues found, 0 auto-fixed
- Initial lint on empty wiki; detection and auto-fix paths of lint_wiki.py functionally verified

## [2026-10-08] init | registry v0.2 — Tyler seed list integrated
- Disposition: New
- Added: 256F ecosystem (site/newsroom/substack/nostr/hashdash/telehash, Discourse forum, Telegram, X), Hashrate Heatpunks (site, forum, Telegram, X), OSMU (wiki, forum*, Discord), 16 OSS project repos (Mujina stack, asic-rs, RHAP, Ember One PCBs, Libre Board, HashScope, ESP-Miner, Bitaxe), silicon datasheet collections, POD256
- New source classes: chat / social / datasheet / code; Capture Layer added to AGENT-PLAYBOOK.md
- Community-source rule: gated chats default to `extract` posture (PII hygiene); forums/X `verbatim`

## [2026-10-08] ingest | hackathon harvest from 256foundation/public-brain
- Disposition: New (staged to inbox, compile pending gate)
- Raw: raw/inbox/hackathon-harvest/ (~500 sourced captures: ESP-Miner issues, asic-rs PR history #1-#409, OSMU Lab chip pages, POD256 transcripts e067-e127, BIP texts, 256F site/newsletter); raw/inbox/hackathon-wiki/ (~70 candidate drafts incl. wiki-new-sources branch)
- Note: provenance + verification rules in raw/inbox/HARVEST.md — all material UNVERIFIED until re-compiled through our grounding invariant

## [2026-10-08] ingest | 256F Telegram history — signal digest staged
- Disposition: New (staged to inbox, compile in progress)
- Raw: raw/inbox/2026-10-08-256f-telegram-signal.md
- Note: 4,485 messages (2024-02-24 → 2026-10-07, 117 authors) filtered to 2,166 substantive via scripts/process_telegram_export.py (extract posture, PII redacted, bots/service dropped). Knowledge extraction + compile next.

## [2026-10-08] compile | 256F Telegram knowledge → first 12 wiki articles
- Disposition: Compiled (Draft)
- Raw: raw/history/2026-10-08-256f-telegram-signal.md (moved from inbox to topic dir at compile)
- Wiki: hardware/asic-thermals-and-heat-reuse; hardware/ember-one-bzm2; firmware/mujina; mining-software/asic-rs; pools/hydrapool; pools/pool-payout-schemes; protocols/decentralized-pool-designs; economics/open-mining-economics; hashrate-market/on-demand-hashrate; history/256f-community-timeline; industry/repair-supply-and-vendors; getting-started/community-workshop-wisdom
- Note: 870 anchored claims extracted via .agent/telegram-extraction-256f.md (subagent full read); every claim cites [#msgid · date · author] anchors greppable in the digest; disputes rendered as Disputed blocks; lint --strict must pass before push

## [2026-10-09] ingest | Hashrate Heatpunks Telegram history — signal digest staged
- Disposition: New (staged to inbox, compile in progress)
- Raw: raw/inbox/2026-10-09-heatpunks-telegram-signal.md
- Note: 9,590 messages (2024-08-02 → 2026-10-08, 129 authors) filtered to 3,271 via scripts/process_telegram_export.py --strict (new signal-only mode: heat-reuse vocabulary, unit-bearing numbers, bare links kept only for resource domains, welcome-bot dropped); processor now reads multi-file exports (messages*.html) and takes title/source/registry flags; PII redaction wired in (was defined but never called — 256F digest re-checked: only public org addresses present, no phones)

## [2026-10-09] compile | Heatpunks Telegram knowledge → 11 wiki articles
- Disposition: New; Update (cross-links)
- Raw: raw/economics/2026-10-09-heatpunks-telegram-signal.md (moved from inbox to topic dir at compile)
- Wiki: hardware/air-cooled-hashrate-heating; hardware/heater-electrical-and-120v-builds; hardware/hydronic-heat-reuse; hardware/whatsminer-m64-hydro-heaters; hardware/immersion-heat-reuse; firmware/heater-firmware-and-power-control; mining-software/home-assistant-heater-control; pools/pool-choice-for-heat-miners; economics/hashrate-heating-economics; industry/hashrate-heating-products-and-installs; history/heatpunks-community-timeline
- Updated: See Also cross-links added to ASIC Thermals and Heat Reuse, Open Mining Economics, Pool Payout Schemes, Decentralized Pool Designs, asic-rs, Mujina, 256F Community Timeline, Repair Supply & Vendors, Community Workshop Wisdom, On-Demand Hashrate
- Note: 1,154 anchored claims extracted via .agent/heatpunks-extraction-part1..6.md (6 parallel full reads, signal-only); 2,437 [#msgid · date · author] anchors in compiled articles, all mechanically resolved against the digest; disputes rendered as Disputed blocks (TIDES vs FPPS for intermittent hashrate, heat pumps vs miners, J/TH relevance for resistive replacement, electricity-cost-irrelevance, and others)
