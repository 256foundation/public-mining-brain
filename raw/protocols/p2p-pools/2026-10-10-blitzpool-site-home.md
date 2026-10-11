# Blitz Pool — site home (blitzpool.yourdevice.ch)

> Source: https://blitzpool.yourdevice.ch/
> Collected: 2026-10-10
> Published: Unknown
> Registry ID: blitz-pool

Capture method: server-rendered Angular (SSR/prerender) HTML fetched with curl; HTML stripped to text (headings/lists preserved, nav/footer/svg/icons dropped). The marketing and how-to text below is fully present in the server HTML (verbatim). Live pool stats render as "—" placeholders in static HTML (JS-gated), so they were pulled from the site's own JSON API instead — see "Live pool stats" section.

The site footer (dropped as nav) names the server repo: github.com/warioishere/blitzpool-server-rust ("Build Blitzpool — Server").

## Page metadata

- <title>: "Blitzpool — Stratum V1 + V2 Bitcoin Mining Pool (Solo, PPLNS, Team Mining)"
- meta description: "Open-source non-custodial Bitcoin mining pool with Stratum V1 + V2 (Job Declaration), solo mining, PPLNS, and team mining payout modes. Multi-output on-chain coinbase, low-fee, self-hostable. Compatible with Bitaxe, NerdQAxe, Braiins OS and SRI proxy."
- Operator: yourdevice.ch ("Built in Switzerland")

## Site text (verbatim)

---

Pool hashrate —
Network difficulty —
Last block found —

Non-custodial · Stratum V1 + V2

# Blitzpool Bitcoin Mining Pool

Solo · PPLNS · Team Mining · Blockparty · by yourdevice.ch

Welcome to Blitz Pool — a modern multi-mode Bitcoin mining pool built on the latest protocols (Stratum V1 + V2 with Job Declaration) and running against our own Bitcoin node. Pick solo for the full reward on a block hit, PPLNS for smooth payouts, or team up with friends in Team Mining — every mode paid out on-chain via multi-output coinbase, no custodial ledger in between. Built in Switzerland by Bitcoiners, for Bitcoiners — for every miner whose heart beats a little faster every ~10 minutes.
Open my dashboard

## How to start

### Pick a mode

Solo, PPLNS, Team Mining or Blockparty. One mode per address, and you can compare them side by side.

### Point your miner at the pool

Use your own Bitcoin address as the worker name. There is nothing to register.

### Watch your workers

Enter that same address here and your dashboard opens. Set a password later if you want to rent or get paid out.

### Quick config

Ports per payout mode. The worker name is always your own Bitcoin address.
Host: `blitzpool.yourdevice.ch`Miner username`<your BTC address>.<worker name>`The worker name is optional and only labels the rig — the address alone works.
- Solo`3333 · 3339 HighDiff · 6666 TLS`
- PPLNS Pool`3340 · 3349 HighDiff · 6640 TLS`
- Team Mining`3333 · 3339 HighDiff · 6666 TLS`
- Blockparty`3339 HighDiff`

 Stratum V2 is auto-negotiated on the same port — no separate endpoint.
Pool Authority Public Key — verifies that you are connecting to the correct pool:`9bCoFxTszKCuffyywH5uS5o6WcU4vsjTH2axxc7wE86y2HhvULU`

## Mining modes

Four ways to mine on Blitzpool — choose what fits your hashrate and your temperament.

#### Solo

Mine alone against the network. Find a block, keep the entire reward.

-  100 % of subsidy + fees on a block hit
-  High variance — long dry spells between blocks
-  Free — no pool fee
Connection details 

#### PPLNS Pool

Mine with everyone else. Payouts share every block proportionally to your work.

-  Smooth, predictable payouts
-  Anti-hop sliding window protects committed miners
Connection details 

#### Team Mining

Team up and mine together — private teams or open to the public, every block split on-chain.

-  Private or public — email-verified membership, no silent adds
-  Multi-output coinbase — shares split on-chain
Connection details 

#### Blockparty

Rent hashpower together with a few friends, share the bill, and split every block on-chain by a fixed percentage you agree up front — straight into each member's address. The easiest blockparty organisation ever.

-  Every share goes on-chain directly to each member — no pool wallet in between
-  Fixed % per member — agreed up front, signed by everyone, locked in
-  Order the Braiins rental right from the admin dashboard, port 3339 (SV1 + SV2)
Connection details 

## Why Blitzpool

Six things that are true of every payout mode here.

### Never custodial

The pool never holds your coins. There is no balance to withdraw and no account to lock, because payouts go to the address you mine with.

### Paid from the block itself

Every mode pays through a multi-output coinbase, so your share is written into the block that was found. No internal ledger sits in between.
Why it matters →

### No transaction censorship

Blocks are built from the full mempool. You can check the template the pool is working on at any time.
Learn more →

### Native Stratum V2

Encrypted and faster, with Job Declaration, and no proprietary proxy in the path. Stratum V1 keeps working as before.
Learn more →

### Rent hashrate with Lightning

Rent hashpower straight onto your address over Lightning. No account, no KYC, no deposit, and automatic refunds.
Learn more →

### Open source, own node

The server is public and the pool runs against its own Bitcoin node. Built in Switzerland.
Learn more →

Login

## Check your workers

`login for your statistics: <your BTC address>`


## Live pool stats (JS-gated on the page; from the site's own API, 2026-10-10)

GET https://blitzpool.yourdevice.ch/api/pplns/fees (verbatim JSON):
```json
{"feePercent":1,"feeAddress":"bc1q394m293t35ls8fq8gu0h5tjwrmpwkkpm245dex","coinbaseWeightBudget":35000,"groupFeePercent":1.5,"groupFeeAddress":"bc1q394m293t35ls8fq8gu0h5tjwrmpwkkpm245dex","blockpartyFeePercent":1.5,"dustLimitSats":546,"minPayoutSats":5000,"coinbaseBaseWeight":328,"coinbaseOutputWeight":172,"coinbaseWitnessCommitmentWeight":188,"maxMinerOutputs":198,"maxMinerOutputsAdaptive":198,"minDifficulty":500}
```

Fee summary: PPLNS 1% · Team/group mining 1.5% · Blockparty 1.5% · Solo 0% (per home page "Free — no pool fee"). Payouts via multi-output coinbase capped at 198 miner outputs (coinbase weight budget 35,000 WU); min payout 5,000 sats; min difficulty 500.

GET https://blitzpool.yourdevice.ch/api/info (2026-10-10, summarized):
- 769 worker connections total; combined reported hashrate ≈ 2.74 PH/s
- Largest user-agent cohorts: bitaxe 223 workers (~228 TH/s), cgminer 42 (~262 TH/s), bitaxe/sv2 88 (~106 TH/s), NMMiner 117, NerdQAxe++ 39 (~178 TH/s), NerdQAxe++/sv2 30 (~151 TH/s), Braiins 5 (~1.17 PH/s single cohort), Antminer 8 (~164 TH/s)
- Workers flagged `/sv2` (native Stratum V2): ~160 connections across bitaxe/sv2, NerdQAxe++/sv2, NerdOCTAXE-γ/sv2, bp-proxy/sv2, SRI/sv2, jd-client/sv2, Braiins/sv2 etc. — roughly 16% of pool hashrate over native SV2 (incl. one SRI proxy and one jd-client = Job Declaration client)
- Bitcoin Core backing node: v31.0.0 (GET /api/info/core, getnetworkinfo verbatim fields: subversion "/Satoshi:31.0.0/", 17 connections, WITNESS + NETWORK_LIMITED + P2P_V2 services)
- API exposes: /api/info, /api/info/workers, /api/info/chart/mode/, /api/pplns/fees, /api/pplns/groups/public, /api/blockparty, /api/next-block-reward, /api/network

Note on JS-garble gaps: per-mode live hashrate, network difficulty, last-block-found and per-worker stats are fetched client-side (Angular main-BRPBOUBK.js) and are not in the static HTML; figures above come from the JSON API at collection time. Home page does not state PPLNS window length or solo/PPLNS fee split on the static page — fee numbers come from /api/pplns/fees.
