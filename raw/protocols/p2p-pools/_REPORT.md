# Capture report — capture-loop A4 (SV2 cluster): OCEAN DATUM docs + decentralized pool projects

> Collected: 2026-10-10
> Ownership: `raw/pools/ocean/` + `raw/protocols/p2p-pools/` (nothing else written)

## Captured (11 files)

### OCEAN DATUM docs — `raw/pools/ocean/` (Registry ID: ocean-datum, verbatim posture)

| File | Source |
|---|---|
| `2026-10-10-ocean-xyz-docs-index.md` | https://ocean.xyz/docs (index card grid → structured list with dates) |
| `2026-10-10-ocean-xyz-docs-datum.md` | https://ocean.xyz/docs/datum ("The Origins of DATUM", Jason Hughes, 2024-09-29) |
| `2026-10-10-ocean-xyz-docs-datum-setup.md` | https://ocean.xyz/docs/datum-setup ("DATUM Setup Guide", OCEAN Team, 2024-10-18) |
| `2026-10-10-ocean-xyz-docs-alternate-templates.md` | https://ocean.xyz/docs/templateselection (extra: DATUM-adjacent — alternate templates decommissioned 2025-12-21 now that DATUM miners cut their own) |
| `2026-10-10-ocean-xyz-docs-tides.md` | https://ocean.xyz/docs/tides (extra: TIDES payout math that DATUM coinbase splits are accounted by; Jason Hughes, 2024-02-29) |

All pages server-rendered; stripped to readable text, verbatim, nav/footer dropped. No "datum gotchas" or "non-coinbase payout" pages exist on ocean.xyz/docs — the datum page links only to datum-setup and terms; the datum-setup page points downloads at github.com/OCEAN-xyz/datum_gateway (noted in-file).

### Decentralized pool projects — `raw/protocols/p2p-pools/`

| File | Source |
|---|---|
| `2026-10-10-github-braidpool-braidpool-readme.md` | gh api repos/braidpool/braidpool README (verbatim) + repo metadata + release/commit/branch activity snapshot |
| `2026-10-10-github-braidpool-braidpool-docs-overview.md` | gh api repos/braidpool/braidpool/contents/docs/overview.md (verbatim) |
| `2026-10-10-github-braidpool-braidpool-docs-roadmap.md` | gh api repos/braidpool/braidpool/contents/docs/roadmap.md (verbatim) |
| `2026-10-10-github-pool2win-p2pool-v2-readme.md` | gh api repos/pool2win/p2pool-v2 README (verbatim; repo now at p2poolv2/p2poolv2) + metadata + activity |
| `2026-10-10-gist-pool2win-p2pool-v2-adoc-design.md` | gh api gists/41f1c0011bd13dc993165c6128084b5d → p2pool-v2.adoc design doc (verbatim, updated 2024-12-05) |
| `2026-10-10-blitzpool-site-home.md` | https://blitzpool.yourdevice.ch/ (server-rendered text verbatim) + live stats/fees from site's own JSON API |

## Skipped

- **pool-sig** — not a project: it's the pool-signature coinbase-tag idea, already covered in the Telegram digests (see wiki `protocols/decentralized-pool-designs.md`); no capture created per instructions.
- Registry IDs: `sources/registry.md` has no `braidpool` / `p2pool-v2` / `blitz-pool` rows (only `ocean-pool`); used task fallbacks — Braidpool files: `decentralized-pools`; P2Poolv2 + Blitz Pool: `decentralized-pool`.

## Failures

- None. (Minor: Blitzpool home-page live stats are JS-gated — recovered from the site's own `/api/info` + `/api/pplns/fees` endpoints; noted in-file.)

## 5 signal lines

1. **P2Poolv2 is live on a public testnet4 pool — testnet4.p2poolv2.org** ("The chain, the accounting, and the coinbase payouts run on testnet4 today", per p2poolv2/website landing page, pushed 2026-10-05): share chain replicating between private/public nodes, SV1 server with per-miner vardiff, PPLNS accounting + payouts built into the coinbase, share-chain block explorer, published Grafana dashboards; mainnet only "after thorough testing on testnet4 first". Rust node at v0.15.3 (2026-09-21) with prebuilt macOS/Linux binaries; daily commits (last 2026-10-09); README documents a `mode = "hydrapool"` that skips the share chain — the mode behind pool.256foundation.org's Hydrapool deployment.
2. **Braidpool is under daily development but pre-testnet**: `main` branch stale since 2025-06-02; all activity on `dev` (last commit 2026-10-09; Oct-2026 PRs #583–#588 on bead wire-protocol hardening, rpc getworkbybead, DAG dashboard; contributors priyashuu, zaidmstrr, Dhirenderchoudhary, Atishyy27, Mayank Yadav, Bob McElrath). No GitHub releases. Roadmap still at "Version 0.01: CPUNet Mining (in progress)" — public testnet only at v0.2, public launch at v0.5; testing today is local CPUNet (patched bitcoind, `cpunet_node.nix`), i.e. zero production hashrate.
3. **Blitz Pool runs 4 payout modes on one endpoint**: Solo (0% fee, full subsidy+fees on a hit), PPLNS (1%, anti-hop sliding window), Team Mining (1.5%, private/public teams, multi-output coinbase split on-chain), Blockparty (1.5%, fixed %-per-member split signed up front + Braiins hashrate rental ordered from the dashboard) — all paid from the block itself via multi-output coinbase (198 miner outputs max, 35,000 WU coinbase budget, min payout 5,000 sats), no custodial ledger; SV2 auto-negotiated on the same ports with Job Declaration ("no proprietary proxy in the path"), SV1 unchanged.
4. **Production hashrate: only the centralized-mode pools have it.** Blitz Pool: ~2.74 PH/s over 769 workers (mostly Bitaxe/NerdMiner-class hobbyist gear; biggest single cohort Braiins ~1.17 PH/s), with ~160 connections flagged native `/sv2` (~16% of pool hashrate, incl. bp-proxy, SRI, and a jd-client Job Declaration client) against Bitcoin Core 31.0.0. OCEAN (DATUM) at capture: 21.49 Eh/s, last block 970835 (3h old). Braidpool and P2Poolv2: no production hashrate — P2Poolv2 is testnet4-only, Braidpool is pre-testnet prototype.
5. **DATUM posture confirmed verbatim on ocean.xyz**: DATUM gives miners their own block templates + non-custodial instant coinbase payouts with a 50% OCEAN fee discount; OCEAN explicitly rejected Stratum V2 as "not a viable solution in the near term" and built DATUM from scratch ("the first fully decentralized mining protocol since 2017"); OCEAN decommissioned its centralized alternate-template options on 2025-12-21 (templateselection doc) — miners wanting other policies must now run DATUM.
