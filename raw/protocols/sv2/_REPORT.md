# Capture Report — Stratum V2 cluster (capture-loop A4, SV2)

> Collected: 2026-10-10 by SV2 capture subagent
> Directory: `raw/protocols/sv2/` (28 files, ~3,070 lines total)

## What was captured

### 1. stratumprotocol.org — 8 files (Registry ID: stratum-v2)
- `2026-10-10-stratumprotocol-org-home.md` — homepage text verbatim (features, SV1-vs-SV2 stats, adoption lists, working group, community).
- `2026-10-10-stratumprotocol-org-spec-abstract.md` — spec 0. Abstract page + full chapter nav (00–10).
- `2026-10-10-stratumprotocol-org-blog.md` — blog index reconstructed (site blog page is a JS shell; posts live at `/content/blog/<slug>.md`, all 7 slugs enumerated with dates).
- 5 blog posts as raw markdown (site serves them as .md): `new-members` (2026-05-07), `sri-roadmap-2026` (2025-10-24), `hashlabs` (2025-06-12), `sri-roadmap-2025` (2024-11-07), `sri-1.0.0` (2024-03-21).

### 2. stratum-mining/sv2-spec — 5 files (Registry ID: sv2-repo)
- `...-sv2-spec-readme.md` — README verbatim + full repo tree (45 blobs; 11 chapters `00`–`10`, 2 extensions docs, drawio sources, generate-readme script) + repo metadata.
- 3 load-bearing chapters captured VERBATIM (chosen per task preference):
  - `03-Protocol-Overview.md` (397 lines — framing, channels, common messages, TLV extensions)
  - `06-Job-Declaration-Protocol.md` (282 lines)
  - `07-Template-Distribution-Protocol.md` (185 lines)
- `00-Abstract.md` (12 lines) as a bonus anchor chapter.
- Chapters NOT taken: 01-Motivation, 02-Design-Goals, 04-Protocol-Security, 05-Mining-Protocol, 08-Message-Types, 09-Extensions, 10-Discussion, extensions/0x0001 & 0x0002 (noted in tree listing).

### 3. stratum-mining/stratum (SRI) — 12 files (Registry ID: sv2-repo)
- README verbatim + repo metadata.
- Latest 5 releases verbatim: v1.12.0 (2026-09-17), v1.11.1 (2026-07-22), v1.11.0 (2026-07-08), v1.10.0 (2026-06-03), v1.9.0 (2026-05-05).
- 6 key issues (bodies; top ≤4 comments included for the 3 most-discussed):
  - #1843 New Job Declarator Client (closed, 31 comments)
  - #1983 Extensions negotiation + TLV + Worker-Specific Hashrate Tracking (closed)
  - #2393 `SupportedChannelTypes` predates sv2-spec#162 (OPEN — spec/impl divergence, interop-relevant)
  - #868 Custom transactions from JDC removed from mempool during update (closed, 30 comments)
  - #1841 Serialize/encrypt separately in codec encoder API (OPEN, 12 comments)
  - #1791 New Translator Proxy — SV1↔SV2 bridge (closed, 30 comments)

### 4. stratum-mining/sv2-apps — 3 files (Registry ID: sv2-repo)
- README verbatim + repo metadata.
- 2 latest releases verbatim: v0.8.0 (2026-09-17), v0.7.0 (2026-07-24).

## What was skipped / gaps
- stratumprotocol.org: language variants (es/it/zh/ru/ar), hashlab sub-pages, `/#anchor` sections are folded into the home capture. `/specification/` and `/blog/` are JS shells; worked around by fetching their data sources directly (`/content/blog/<slug>.md`, spec nav in abstract page HTML). No sitemap.xml exists.
- Site pages `/what-is-stratum-v2`, `/developers`, `/miners`, `/pools` from the task brief do not exist on this site; the real nav is home-anchors + `/specification/` + `/blog/`.
- sv2-spec: images are `.drawio`/`.png` (paths kept in tree listing, binaries skipped); chapters 01,02,04,05,08,09,10 not captured verbatim (≤3-chapter budget).
- SRI releases: notes kept verbatim (all <130 lines, under truncation threshold). Older releases v1.4.0–v1.8.0 not fetched (tag list is in README capture).
- No files exceeded 3000 lines; no truncation needed anywhere.
- SRI README links into `stratum-core`/workspace docs that live in sibling repos — not captured (out of scope, separate repos).

## Failures
- None blocking. Minor: GitHub release `Published:` header lines initially empty due to a zsh array-indexing slip; fixed in place. One `grep -P` incompatibility (macOS BSD grep) — switched to `sed`.
- `search/issues` API for "interop" returned mostly closed CI-migration issues; open interop signal came from #2393 and #1841 instead.

## Signal (5 lines)
1. **Release cadence**: SRI cuts a minor release ~every 6–8 weeks without a miss (v1.9.0 May 2026 → v1.12.0 Sep 2026); sv2-apps rides the same train (v0.8.0 same day as SRI v1.12.0, synced to `stratum-core` 0.6.0). Latest: SRI v1.12.0, sv2-apps v0.8.0.
2. **Working-group expansion (May 2026)**: ANTPOOL, Block, F2Pool, Foundry, MARA Foundation, SpiderPool, DMND formally joined the SV2 Working Group — the big pools are now at the table, not just Braiins/Spiral.
3. **JD client adoption**: JD clients (JDC/JDS) run in production at DMND (miner-selected templates), Braiins Pool, and SRI Community Pool; pools like CKPool/PublicPool/NexusPool/Blitzpool run SV2 solo in production; firmware support is native in BraiinsOS, Bitaxe, NerdAxe, Auradine (via FluxOS), with Block/Proto and Mujina in progress.
4. **Open interop/spec-gap issues**: #2393 (open) — SRI's `SupportedChannelTypes` predates spec PR sv2-spec#162 and cannot express group-mode+standard/extended channel mixes; #1841 codec API split; plus hardened share validation (`SeenSharesBudgetExhausted`, bounded job storage) landing in v1.12.0.
5. **Security posture**: sv2-apps v0.8.0 is an audit-driven hardening release (findings from the **Loupe audit**), BIP323 version-rolling support across tProxy/SV1 bridge, all config via env vars for containerized deployments — moving from spec-complete toward audited production software.
