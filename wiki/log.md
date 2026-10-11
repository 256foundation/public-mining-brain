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

## [2026-10-09] compile | Hackathon harvest phase 1 → 16 new articles, 8 updated
- Disposition: New; Update; Disputed
- Raw: raw/firmware/esp-miner/, raw/hardware/bitaxe-osmu/, raw/hardware/256f-hardware/, raw/firmware/mujina/, raw/pools/hydrapool/, raw/protocols/harvest/, raw/mining-software/256f-tools/, raw/history/256f-org/, raw/history/256f-newsletter/, raw/history/256f-research/, raw/history/pod256/ (episode pages) — triaged out of raw/inbox/hackathon-harvest/
- Wiki (new): hardware/bitaxe-models; hardware/bitaxe-board-design-and-errata; hardware/bitmain-asic-reference; hardware/libre-board-and-control-boards; firmware/esp-miner-axeos; getting-started/bitaxe-troubleshooting; mining-software/hashscope; pools/public-pool; pools/pool-centralization-and-fpps; protocols/stratum-in-practice; protocols/rhap; history/256-foundation-organization; history/open-source-solo-blocks; history/pod256-podcast; industry/mining-firmware-security; industry/network-state-2022-2026
- Updated: Mujina; Ember One & the BZM2 Hardware Stack; Hydrapool; asic-rs; Decentralized Pool Designs; 256F Community Timeline; Repair, Supply & Vendors; ASIC Thermals and Heat Reuse
- Note: 2,457 claims extracted by 12 parallel readers (.agent/harvest-*.md), every [src:] path validated; articles cite exact captures via inline raw links (lint now counts these as evidence). hackathon-wiki drafts used as leads only, never cited. Website-styling PRs (84) and code-churn PRs judged no material. Raw backlog 2,185 → 1,038 unreferenced files. POD256 full transcripts (50) pending phase 2.

## [2026-10-10] compile | POD256 transcripts (phase 2) — PARTIAL, interrupted by usage limit
- Disposition: Update; New
- Raw: raw/history/pod256/transcripts/2026-10-07/transcripts/ (50 episode transcripts, e067–e127)
- Wiki (new): protocols/mining-nodes-and-templates
- Updated (transcript material merged, citations preserved): Mujina; Bitaxe Models; Mining Firmware Security; Network State 2022–2026; Hydrapool; Pool Centralization & FPPS; Stratum V1 & V2 in Practice
- Note: 1,458 claims extracted to .agent/harvest-pod-tx-1..6.md (all [src:] paths valid). NOT YET MERGED: POD256 Podcast, The 256 Foundation, Ember One & BZM2, Libre Board & Control Boards, Decentralized Pool Designs, Open Mining Economics, Hashrate Heating Economics; new article industry/mining-policy-and-legal not yet written. The updated articles above may also be incomplete relative to the notes.

## [2026-10-10] compile | POD256 transcripts (phase 2) — COMPLETE
- Disposition: Update; Disputed
- Raw: raw/history/pod256/transcripts/2026-10-07/transcripts/ (50 episode transcripts, e067–e127)
- Updated (all prior citations preserved, zero removed links, verified vs HEAD): pod256-podcast; 256-foundation-organization; ember-one-bzm2; libre-board-and-control-boards; decentralized-pool-designs; open-mining-economics; hashrate-heating-economics; mujina; bitaxe-models; mining-firmware-security; network-state-2022-2026; hydrapool; pool-centralization-and-fpps; stratum-in-practice; mining-nodes-and-templates; asic-rs
- Wiki (new this phase): industry/mining-policy-and-legal (e080–e127 + newsletter e108 breakdown); hardware/osmu-open-miners (NerdMiner line, PiAxe/QAxe, BitForge, firmware forks — 15 captures incl. 5 previously unreferenced)
- Note: all 1,458 harvest claims dispositioned; citation lines grew 14→44, 1→28, 1→26 on the three pools/economics articles; Disputed blocks for Telehash #2 peak (245 Ph/s record vs ~400 Ph/s recall), M74 unit economics, district-heating taxonomy, peak-energy thesis, Ocean-vs-FPPS, BIP 110. lint --strict: 0 errors, 0 warnings.

## [2026-10-10] audit | hackathon harvest — per-source provenance ledger + dispositions
- Disposition: Audit complete; No material; Backlog
- Tooling: scripts/ingest_ledger.py committed (ledger output is local-only at .agent/ingest-ledger.md, gitignored); 68 upstream sources identified under what the log previously called one "hackathon harvest"
- Coverage verified live against upstream (GitHub API, 2026-10-10): ESP-Miner 729/730 issues (PRs uncaptured), web-flasher 30/31, osmu.wiki 39/39 repo pages, ultraHex/Gamma/GT/Bonanza/Max/Supra/Ultra/GammaHex/bitaxe-raw/bitaxeBIRDS 100%, asic-rs 409/415, mujina 74/79 (rest deleted upstream), website repo #1–46/47, newsletter 23/23, hydrapool 44/44
- No material: btc-toolkit repo article (1-2 sentences added to asic-rs instead — reference GUI consumer, quiet since early 2026); Block-Watcher-website (paused-2025 grant site, config PR only); bitaxe.org residue; web-flasher/osmu residue (~480 unref files across cluster judged genuine churn — kept, not deleted)
- Backlog for Tyler: asic-rs #410–415 recapture; ESP-Miner PR backfill (1,204) + issue #2026; legitlist vendor-application PRs; emberone-usbserial-fw 1/12 gap; gamma-603 tag/README diff (resolves errata 603 question); website PR #47; 18 auth-only forum topics; Treasury PDF capture; "Community channels & X presence" article (5 sprint drafts, no new captures needed); docs-mirror dedupe (hashscope 8 + asic-rs 6 + mujina-website 8); ESP-Miner keeper issues (#65/#138/#1789/#1777/#385) + web-flasher #29/#1 + mujina PR #30 + hydrapool PR #33 companion-cites
- Registry: +legitlist, +naja-duo, +bitaxebirds, +block-watcher-site (all proposed, already captured); substack span corrected to 2025-05 → 2026-05 (dormant since #27)
- Note: sprint drafts' leads-only verdict re-verified against all compiled articles; 64/87 drafts link pre-triage raw paths (re-resolve via HARVEST.md triage map before any future compile)

## [2026-10-10] ingest | keeper-capture pass — audit backlog mined, community-channels article compiled
- Disposition: Update; New article
- Ran an ingestion pass over the compile-ready items the harvest audit left in backlog (all from captures already on disk — no new sources touched):
- New: getting-started/community-channels-and-x — Telegram supergroups, Discourse forums, Nostr, OSMU Discord, and X accounts (@osmu_global/@heatpunks/@Public_Pool_BTC), measured sizes + activity patterns from 12 raw captures (5 sprint drafts used as leads only; drafts' unsupported claims dropped, X-archive incompleteness self-declarations carried into body). Inbound link from 256-foundation-organization.
- Enriched: firmware/mujina (+PR #30 voltage-API companion cite, 181→182); firmware/esp-miner-axeos (+keepers #1789 OLED minimalism, #1777 TLS-default proposal, #385 AP-mode policy; 121→124); getting-started/bitaxe-troubleshooting (+dead-subscription "hashing for nothing" chain #65/#138→#272, web-flasher #29 flashingFailed; 134→137). Zero removed citations on all four files, verified vs HEAD.
- Rejected as unverifiable: #363 (no capture — referenced by #65's close comment only), #385/#272 implementation claims (thin captures), web-flasher #29 fix specifics (single "has been fixed" response).
- Remaining backlog items needing NEW captures stay with Tyler per the audit entry (asic-rs #410–415, ESP-Miner PR backfill, gamma-603 diff, website PR #47, Treasury PDF, etc.). lint --strict: 0 errors, 0 warnings.

## [2026-10-10] registry | capture-loop v1 — verify queue rows, cadence sweep, new sources
- Disposition: Registry pass (A0 of capture loop, per .agent/HANDOFF-capture-loop.md) — no captures
- Row edits (rows never deleted): osmu-forum URL https://osmu.xyz →active; heatpunks-x handle @HashHeatpunks →active (@heatpunks discrepancy parked B3); mining-pod source corrected to Blockspace Media →dormant/static (~486 eps, paused 2026-01, moved to Blockspace Podcast); brainstorm-pod → Braiins feed (no "Brainstorm" show) →active monthly; betterhash attribution fixed to Matt Corallo's draft BIP (TheBlueMatt/bips) →active; desiwe-miner →dormant (Bitdeer acquisition 2024-06); giga-energy →active (URL verified); hashworks →dead (phantom); heatpunk-summit-2025 →active (14 talks verified); hashdash posture extract→link-only (dashboard, do not scrape); bitcoinbook posture verbatim→extract (book rule); 256f-substack →dormant/monthly; btc-toolkit →dormant; bitaxebirds →dormant
- New rows: blockspace-podcast, elektronics-dev (link-only), exergy-docs, exergy-calculators, exergy-forum, tyler-stevens-site, learnmeabitcoin, stratum-work; queue section converted to promotion notes (4 IDs promoted, preserved)
- Notes added: Book-source rule + No-massive-data rule (Tyler, 2026-10-10)
- automation/AGENT-PLAYBOOK.md: Tyler method contracts encoded verbatim (OSMU Discourse JSON, 256F forum RSS, pool Prometheus PromQL contract, X/Nostr, SEC EDGAR UA + rate limit, dash-not-a-source)

## [2026-10-10] ingest | capture-loop A1 — public community surfaces (osmu-forum, heatpunks-forum, 256f-forum)
- Disposition: New (first OSMU forum captures); Update (6 articles); No material (20 heatpunks chatter topics skipped at capture, 6 OSMU topics skipped)
- Raw: raw/history/osmu-forum/ (census 2026-10-10 + 26 topics, 152 posts; upstream 32 public topics, 6 skipped as welcome/greetings/meta/one-post intros); raw/history/heatpunks-forum/ (census + 81 topic captures / 520 posts of 101 publicly listed of 119 site-wide; 20 chatter topics skipped with reasons); raw/history/256f-org/2026-10-10-forum-256f-recensus.md (35 visible topics, newest activity 2026-09-29 — zero new since the 2026-10-07 audit cutoff; 18 auth-only topics → B4)
- Wiki (updated, all citations preserved vs HEAD f9b139b, verified): hardware/osmu-open-miners (35→53: WarpAxe fork registry + TPS546/BM1373 findings, NerdNOS API, TDX33029, new "Pools and tools from the OSMU forum" section — dvb-WarpPool incl. 2026-07-09 GitHub suspension + WarpTune A/B, Pogolo, BTC PoW Lab, Bitaxe Monitor); hardware/bitaxe-models (251→276: BM1370 primer, Gamma Duo 2.4 TH/s, GT XT30PW-M power input + waterblock-mod guidance, Gamma 601 "400 THs" register explanation, Naja 10.74 j/th field efficiency, S23 dump-init confirmation); getting-started/bitaxe-troubleshooting (238→249: 2.14.0→2.15.0 upgrade failure, v2.14.0 error-rate regression, Wi-Fi reconnect backoff request, Gamma Turbo power, fan-PID retune, USB-recovery heat); firmware/esp-miner-axeos (327→344: OLED brightness declined (#567/#1746), Wi-Fi gap, fan-PID retune, WarpAxe/BTCMinerControl reimplementations, Bitaxe Monitor, BM1398 boundary); getting-started/community-channels-and-x (12→15: heatpunks forum 2026-10-10 census 119/682/138/624, 101 publicly listed, live since 2025-03-31); history/heatpunks-community-timeline (1→49: forum-launch era, The Space radiant demo threads, TIDES-vs-FPPS sat-tally arc 1678/792 → 13919/14376, HPS 2026 program, 2027 waitlist, Ofgem numbers; 2 new Disputed blocks — forum-creation date vs Telegram recall, 19kw vs 20kW solar)
- Note: 112 captures this phase (cap 120); forum topics verbatim posture; machine-style chat skipped per signal-only. ESP-Miner PR index correction: ESP-Miner PRs share the issue number space (#6–#2028; captured separately in A2). lint --strict: 0 errors, 0 warnings.
