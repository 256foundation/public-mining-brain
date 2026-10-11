# F2Pool

> Sources: f2pool.com homepage with live per-coin fee/payout banners (alternate-fetcher capture, 2026-10-10); f2pool.zendesk.com help center, "Mining pools info, payout schemes and thresholds at f2pool" (article updated 2026-10-09) plus cross-referenced payout articles (captured 2026-10-10); mempool.space mining-pool share API, 1w window (2026-10-10); capture-loop A6 pool-landscape report (2026-10-10)
> Raw: [f2pool.com homepage](../../raw/pools/f2pool/2026-10-10-f2pool-home.md); [Zendesk: payout schemes and thresholds](../../raw/pools/f2pool/2026-10-10-f2pool-help-payout-schemes-thresholds.md); [mempool.space pool share, 1w](../../raw/pools/mempool/2026-10-10-mempool-pool-share-1w.md); [capture report](../../raw/pools/foundry/_REPORT.md)
> Updated: 2026-10-10
> As-Of: 2026-10-10
> Status: Draft

## Overview

F2Pool is a large multi-coin pool operating since 2013 (site footer: "© 2013–2026 F2Pool"), with a BTC panel that self-reports a pool hashrate of 164.48 EH/s against a 1-day network average of 954.64 EH/s (As-Of 2026-10-10) ([homepage](../../raw/pools/f2pool/2026-10-10-f2pool-home.md)). On mempool.space's trailing-week ranking F2Pool is third with 183 of 1072 blocks and a 98.7% average block match rate, behind Foundry USA (288) and AntPool (213) (As-Of 2026-10-10) ([mempool.space 1w](../../raw/pools/mempool/2026-10-10-mempool-pool-share-1w.md)).

Its distinguishing trait among the large pools captured in this loop is fee transparency: the BTC fee is disclosed live on the homepage banner — "Payout: FPPS 4.0% | PPLNS 2.0%" — and the help center carries a full per-coin fee/scheme/threshold table whose article is stamped "updated October 09, 2026", the day before capture. The capture note calls it "the most transparent of the large pools captured today" ([homepage](../../raw/pools/f2pool/2026-10-10-f2pool-home.md); [Zendesk](../../raw/pools/f2pool/2026-10-10-f2pool-help-payout-schemes-thresholds.md)).

The site carries an anti-scam modal worth noting for newcomers: f2pool "solely provides mining pool services that are only accessible through our official website: www.f2pool.com" and "We do not offer any investment opportunities, financial services, or cloud mining products." ([homepage](../../raw/pools/f2pool/2026-10-10-f2pool-home.md))

## Fees and payout

- **BTC fees (both sources agree).** Homepage banner: "Payout: FPPS 4.0% | PPLNS 2.0%". Help-center table: "FPPS 4%, PPLNS 2%" (As-Of 2026-10-10) ([homepage](../../raw/pools/f2pool/2026-10-10-f2pool-home.md); [Zendesk](../../raw/pools/f2pool/2026-10-10-f2pool-help-payout-schemes-thresholds.md)).
- **Scheme selection for BTC.** "FPPS is default; PPLNS selectable per subaccount in app/web; changes take effect at 00:00 UTC the following day, once per day." ([Zendesk](../../raw/pools/f2pool/2026-10-10-f2pool-help-payout-schemes-thresholds.md))
- **Scheme definitions (help center).** PPS pays per share; PPLNS pays only after a block is found, tallying the last N shares; "FPPS = PPS + transaction fees (fee share computed as percentage of total network mining fees vs total coinbase rewards of the past day)"; "PPS+ = fixed block reward via PPS + transaction fees distributed via PPLNS." ([Zendesk](../../raw/pools/f2pool/2026-10-10-f2pool-help-payout-schemes-thresholds.md))
- **No payout fees.** "f2pool does not charge any transaction fees for paying out mining revenues if the balance exceeds the minimum payout threshold" and "f2pool covers all blockchain network fees" ([Zendesk](../../raw/pools/f2pool/2026-10-10-f2pool-help-payout-schemes-thresholds.md))
- **BTC threshold and cadence.** Default minimum payout 0.005 BTC (homepage banner; help table adds "Changing threshold available"), user-selectable at "0.005 / 0.01 / 0.05 / 1 / 5 BTC (user-selectable, BTC only)". "Payouts are made daily between 00:00 and 12:00 UTC.", with revenue paid daily once the unpaid balance reaches the threshold by 00:00 UTC (As-Of 2026-10-10) ([homepage](../../raw/pools/f2pool/2026-10-10-f2pool-home.md); [Zendesk](../../raw/pools/f2pool/2026-10-10-f2pool-help-payout-schemes-thresholds.md)).
- **Other coins (help-center table, updated 2026-10-09).** BCH PPS 3% (0.01 BCH); LTC PPS 4% (0.02 LTC); ETHW PPS 1%; DASH PPS 2%; ETC PPS 1%; ZEC PPS+ 3% (0.1 ZEC); SC PPS 3%; CKB PPS 1%; KAS PPLNS 1%; CFX PPLNS 1%; ALEO PPLNS 1% with "No payout threshold; balance above staking requirement withdrawable"; ALPH PPLNS 1%; PRL PPS 1% — each row with pool URLs and regional/SSL endpoints ([Zendesk](../../raw/pools/f2pool/2026-10-10-f2pool-help-payout-schemes-thresholds.md)).
- **Merged mining, free.** "Mine BTC, get HTR, ELA, FB, NAT, and NMC for free" — with the homepage adding that FB and NAT rewards are paid "based on PPLNS mining scheme". For LTC: "Mine LTC, get DOGE, LKY, PEP, BELLS, DINGO for free" (merged coins on PPLNS per the homepage) ([Zendesk](../../raw/pools/f2pool/2026-10-10-f2pool-help-payout-schemes-thresholds.md); [homepage](../../raw/pools/f2pool/2026-10-10-f2pool-home.md)).
- **Connection.** `stratum+tcp://btc.f2pool.com:1314` (backup ports 25, 3333), SSL `stratum+ssl://btcssl.f2pool.com:1300`, regional endpoints btc-asia / btc-euro / btc-na / btc-africa / btc-latin ([homepage](../../raw/pools/f2pool/2026-10-10-f2pool-home.md); [Zendesk](../../raw/pools/f2pool/2026-10-10-f2pool-help-payout-schemes-thresholds.md)).

## Custody and access

- **Custodial payouts, no account-level fee games.** Mining revenue accumulates in the pool account and is paid daily to the user's wallet once over threshold; the pool covers network fees ([Zendesk](../../raw/pools/f2pool/2026-10-10-f2pool-help-payout-schemes-thresholds.md)).
- **KYC: not mentioned in captured payout articles** (homepage or help center) — the capture note records "KYC not mentioned in captured payout articles"; the site's own modal steers users to the official domain only ([homepage](../../raw/pools/f2pool/2026-10-10-f2pool-home.md); [Zendesk](../../raw/pools/f2pool/2026-10-10-f2pool-help-payout-schemes-thresholds.md)).
- **Tooling.** Tx Accelerator, PoW Rankings, Popular Miners, miner tools and an app are linked from the homepage; the calculator "uses the current network difficulty and default pool fees to estimate PPS mining revenue" ([homepage](../../raw/pools/f2pool/2026-10-10-f2pool-home.md)).

## SV2 / DATUM

Zero Stratum V2 or DATUM mentions on the captured F2Pool pages (As-Of 2026-10-10): the homepage capture note records "No Stratum V2 / DATUM mention on homepage" and the Zendesk note the same for the payout articles ([homepage](../../raw/pools/f2pool/2026-10-10-f2pool-home.md); [Zendesk](../../raw/pools/f2pool/2026-10-10-f2pool-help-payout-schemes-thresholds.md)). F2Pool joined the Stratum V2 Working Group in May 2026 — see [Pool Centralization & FPPS](pool-centralization-and-fpps.md).

## See Also

- [Pool Payout Schemes](pool-payout-schemes.md)
- [Pool Centralization & FPPS](pool-centralization-and-fpps.md)
- [Foundry USA Pool](foundry.md)
- [AntPool](antpool.md)
- [ViaBTC](viabtc.md)
- [OCEAN](ocean.md)
- [Stratum in Practice](../protocols/stratum-in-practice.md)
- [Solo Blocks Found by Open-Source & Home Miners](../history/open-source-solo-blocks.md)
