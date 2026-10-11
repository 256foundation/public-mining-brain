# F2Pool — Help Center: Mining pools info, payout schemes and thresholds

> Source: https://f2pool.zendesk.com/hc/en-us/articles/360058887912-Mining-pools-info-payout-schemes-and-thresholds-at-f2pool
> Collected: 2026-10-10
> Published: 2026-10-09 (article "Updated" timestamp)
> Registry ID: f2pool

---

# Mining pools info, payout schemes and thresholds at f2pool

(F2Pool Help Center > FAQ > Payouts; author "support"; updated October 09, 2026)

| Coin | Pool URL | Payout scheme | Pool fee | Default payout threshold |
|---|---|---|---|---|
| BTC | stratum+tcp://btc.f2pool.com:3333 (failover 25, 1314, 3333); regional: btc-asia / btc-euro / btc-na / btc-africa / btc-latin.f2pool.com:1314; SSL stratum+ssl://btcssl.f2pool.com:1300 (failover 1301) | FPPS, PPLNS | **FPPS 4%, PPLNS 2%**. "Mine BTC, get HTR, ELA, FB, NAT, and NMC for free" (merged mining) | 0.005 BTC. Changing threshold available |
| BCH | stratum+tcp://b4c.f2pool.com:1228 | PPS | 3% | 0.01 BCH |
| LTC | stratum+tcp://ltc.f2pool.com:8888 (failover 5200, 3335); regional + SSL ltcssl.f2pool.com:5201 | PPS | 4%. "Mine LTC, get DOGE, LKY, PEP, BELLS, DINGO for free" (merged mining) | 0.02 LTC. Changing threshold available |
| ETHW | stratum+tcp://ethw.f2pool.com:6688; SSL :6698 | PPS | 1% | 0.1 ETHW |
| DASH | stratum+tcp://dash.f2pool.com:5588 | PPS | 2% | 0.1 DASH |
| ETC | stratum+tcp://etc.f2pool.com:8008 (failover 8118); SSL etcssl.f2pool.com:8180 | PPS | 1% | 0.1 ETC. Changing threshold available |
| ZEC | stratum+tcp://zec.f2pool.com:3357 | PPS+ | 3% | 0.1 ZEC |
| SC | stratum+tcp://sc.f2pool.com:7788 | PPS | 3% | 100 SC |
| CKB | stratum+tcp://ckb.f2pool.com:4300 (failover 4333) | PPS | 1% | 100 CKB |
| KAS | stratum+tcp://kas.f2pool.com:1430; SSL kasssl.f2pool.com:1430 | PPLNS | 1% | 100 KAS. Changing threshold available |
| CFX | stratum+tcp://cfx.f2pool.com:6800; SSL cfxssl.f2pool.com:6820 | PPLNS | 1% | 10 CFX |
| ALEO | stratum+tcp://aleo.f2pool.com:4430 (Goldshell) / :4400 (IceRiver); SSL :4420 | PPLNS | 1% | No payout threshold; balance above staking requirement withdrawable |
| ALPH | stratum+tcp://alph-asia.f2pool.com:5600 / :5630 (ASICs) | PPLNS | 1% | 1 ALPH |
| PRL | stratum+tcp://pearl.f2pool.com:5500 | PPS | 1% | 1 PRL |

Related help articles in the Payouts section: "How can I withdraw my balance if it does not reach the minimum threshold?", "What is the threshold for manual withdrawals?", "Merged mining manual withdrawal", "When does the mining pool pay the rewards?", "Payout schemes: PPS, PPLNS, FPPS, PPS+".

---

## Supplemental help-center facts (same section, cross-referenced during capture)

- **Payout schemes** (https://f2pool.zendesk.com/hc/en-us/articles/360061042332): PPS pays per share; PPLNS pays only after a block is found, tallying the last N shares; FPPS = PPS + transaction fees (fee share computed as percentage of total network mining fees vs total coinbase rewards of the past day); PPS+ = fixed block reward via PPS + transaction fees distributed via PPLNS.
- **Payout time** (BTC mining guide / "When does the mining pool pay the rewards?"): "Payouts are made daily between 00:00 and 12:00 UTC." Revenue paid out daily if unpaid balance reaches threshold by 00:00 UTC.
- **BTC payout thresholds**: 0.005 / 0.01 / 0.05 / 1 / 5 BTC (user-selectable, BTC only).
- **Payout transaction fees**: "f2pool does not charge any transaction fees for paying out mining revenues if the balance exceeds the minimum payout threshold" and "f2pool covers all blockchain network fees" (https://f2pool.zendesk.com/hc/en-us/articles/360058368652).
- **BTC scheme switching**: FPPS is default; PPLNS selectable per subaccount in app/web; changes take effect at 00:00 UTC the following day, once per day.

---

*Capture notes (2026-10-10):*
- *Fee %: fully disclosed per coin (BTC FPPS 4% / PPLNS 2%) — the most transparent of the large pools captured today.*
- *Payout schemes: PPS, PPLNS, FPPS, PPS+ documented; BTC is FPPS (default) or PPLNS.*
- *Payout threshold/cadence: 0.005 BTC default (selectable up to 5 BTC); daily payouts 00:00–12:00 UTC.*
- *Custody: custodial pool payouts to user wallet; no pool-level payout fees; KYC not mentioned in captured payout articles.*
- *Merged mining: BTC → HTR, ELA, FB, NAT, NMC free; LTC → DOGE, LKY, PEP, BELLS, DINGO free.*
- *No Stratum V2 / DATUM mention in captured articles. f2pool.zendesk.com 403s plain curl (exit 56); captured via alternate fetcher.*
