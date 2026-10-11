# OCEAN — homepage (ocean.xyz)

> Source: https://ocean.xyz/
> Collected: 2026-10-10
> Published: Unknown (live stats page; © 2023–2026)
> Registry ID: ocean-pool

---

*Live stats banner at capture time: **HASHRATE: 21.74 Eh/s • LAST BLOCK: 970835 (4H AGO)***

# Take control of your bitcoin mining and make more money

## THE INDUSTRY'S LOWEST FEES & MOST TRANSPARENT PAYOUTS

Start mining — Point your miners to **mine.ocean.xyz:3334**

Press coverage logos: Forbes, PR Newswire, Bitcoin Magazine, Yahoo Finance, CoinDesk.

**OCEAN Earns SOC 1 and SOC 2 Type 2 Attestations**, Bringing Independent Assurance to Permissionless Bitcoin Mining ([Press Release](https://www.prnewswire.com/news-releases/ocean-earns-soc-1-and-soc-2-type-2-attestations-bringing-independent-assurance-to-permissionless-bitcoin-mining-302878472.html))

## Miner quotes (homepage)

- @denverbitcoin (Upstream Data): "I ran this test and ocean won…even with unlucky variance. FPPS pools are shorting their customers while (many) also are not actually taking variance risk. Ripe for disruption, to say the least."
- @TimoThisis (Co-Founder Munich International Mining): "I mined with them since day 1 - I can confirm I earned more than FPPS. You can look at the data on the ocean website. Each miner's data is 100% transparent to look at."
- @Meditation_Man (Creator of Timechain Calendar): "I mine with @ocean_mining because: Earn more sats than if I mined at other pools, despite filtering! Get paid out direct from coinbase tx. Transparency in pool payouts. **No KYC, only payout address.** Only downside is variance. Check your incentives & time preference."

## There's more with OCEAN (feature blocks)

- **DECENTRALIZED & ENCRYPTED** — Add your name to the blockchain, forever. Powered by DATUM.
- **FAST & FRICTIONLESS** — Instant Bitcoin: No account needed. Seriously, all you need is a bitcoin address. It's that easy.
- **COMPLETE CONTROL** — Decentralized alternative templates for universal mining (DATUM). [GET STARTED](https://ocean.xyz/docs/datum-setup)
- **NON CUSTODIAL** — Get newly generated bitcoins directly from the network.
- **SECURITY** — SOC 1 and SOC 2 attestations for enterprise-grade security and reliability (Type 1 + Type 2 checks shown for both SOC 1 and SOC 2).
- **INSTANT CASHFLOW** — Get paid on Lightning with BOLT12. ([docs/lightning](https://ocean.xyz/docs/lightning))

## Get started — The OCEAN difference

Fast, easy setup that gives you more control of your bitcoin mining.

**2% fee — 1% fee for miners who make their own blocks using DATUM**

Setup takes 2 minutes, no account required, just point your miners to mine.ocean.xyz:3334.

## Frequently Asked Questions (homepage FAQ, abridged)

- **How Do I Mine With OCEAN?** Point pool URL at mine.ocean.xyz:3334; use a Bitcoin address as worker/username (address.workername optional).
- **How Does OCEAN Differ From Other Pools?** (1) Non-custodial: miners are paid directly by the Bitcoin network (example 2026 block with 57 coinbase outputs); (2) DATUM self-built templates; (3) TIDES reward system — "Unlike PPLNS or FPPS, TIDES does not merely approximate reward distributions, so miners are paid the full and exact pro rata portion of their contributed hashrate."
- **What Is DATUM?** "Decentralized Alternative Templates for Universal Mining" — DATUM users enjoy a **50% discount on pool fees**.
- **How Does OCEAN Avoid Taking Custody?** "OCEAN constructs blocks so that miners are paid in the generation transaction whenever possible."
- **What Is The Payout Threshold?** "Currently, the threshold is **0.01048576 BTC or 1,048,576 sats**." Discretionary payouts for balances above **0.00065536 BTC** if you stop mining / change address, "should it be practical to do so."
- **What Happens To Rewards Below This Threshold?** They accumulate until the threshold is exceeded, then payout is automatic. Payouts can be made before reaching the threshold via [Lightning](https://ocean.xyz/docs/lightning).
- **What Reward System Do You Use/What Is TIDES?** Transparent Index of Distinct Extended Shares — proof window chosen so each proof is paid on average 8 times; block reward divided by percent so transaction fees are included; every payout fully auditable. "TIDES is the most accurate payout scheme available in Bitcoin today and unlike other schemes like FPPS it does not require the pool to serve as a custodial intermediary for payment processing."

## About Us / Footer

Team: Mark Artymko (President), Ian Northon (Chief Legal Officer), Nacho Pauls (CCO), Nick Watkins (CFO), Jason Hughes (CTO), Vincenzo Palazzo (Lead Lightning Developer), Christopher Sabella (Head of Operations), Kyle Small (Head of DevOps), Léo Haf (Software Support), Adriana Álvarez (Inside Sales), Wing Li (DevOps), Jonathan Davis (VP Marketing), Yo Wang (APAC BD Director).

OCEAN is operated by **Bitcoin Ocean, LLC, a subsidiary of Mummolin, Inc., a Wyoming corporation**. © 2023–2026.

Links: Get Started, Pool Stats (/dashboard), Documentation (/docs), Announcements, Press, Terms of Service (/docs/terms), Portal (portal.ocean.xyz).

---

*Capture notes (2026-10-10):*
- *Fee %: 2% standard, 1% for DATUM (self-template) miners — stated on homepage.*
- *Payout scheme: TIDES (own pro-rata scheme, ~8× proof window, includes tx fees); not FPPS/PPLNS/PPS+; BOLT12 Lightning payouts below threshold.*
- *Payout threshold: 0.01048576 BTC (1,048,576 sats); discretionary ≥0.00065536 BTC.*
- *Custody: non-custodial — miners paid directly in the coinbase/generation transaction; no account, no KYC ("No KYC, only payout address").*
- *Compliance posture: SOC 1 + SOC 2 Type 2 attestations; US (Wyoming) entity.*
- *SV2/DATUM: DATUM is OCEAN's own decentralized-template protocol (alternative to Stratum V2 template distribution — see existing docs captures in this directory).*
- *ocean.xyz kills plain-curl body transfers (HTTP 200, 0 bytes, curl exit 56); captured via alternate fetcher.*
