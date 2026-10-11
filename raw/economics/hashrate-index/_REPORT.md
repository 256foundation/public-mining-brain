# Capture Report — Phase A8 Economics (hashrate-index + hashprice-docs)

> Collected: 2026-10-10 by fetch agent
> Scope: registry `hashrate-index` (https://hashrateindex.com, posture extract) and registry `hashprice-docs` (https://docs.luxor.tech/hashrateindex/hashprice, posture verbatim)

## Files captured

| # | File | URL | Posture |
|---|---|---|---|
| 1 | `raw/economics/hashprice-docs/2026-10-10-hashprice-methodology.md` | https://docs.luxor.tech/hashrateindex/hashprice (via https://docs.luxor.tech/llms-full.txt) | verbatim |
| 2 | `raw/economics/hashrate-index/2026-10-10-homepage-snapshot.md` | https://hashrateindex.com | extract |
| 3 | `raw/economics/hashrate-index/2026-10-10-lookback-september-2026.md` | https://hashrateindex.com/blog/luxor-hashrate-lookback-series-september-2026/ | extract |
| 4 | `raw/economics/hashrate-index/2026-10-10-heatmap-q4-2026.md` | https://hashrateindex.com/blog/global-hashrate-heatmap-update-q4-2026-c/ | extract |
| 5 | `raw/economics/hashrate-index/_REPORT.md` | — (this report) | — |

All captures carry the provenance header (Registry ID / Source / Collected 2026-10-10 / Published / Posture / As-Of 2026-10-10).

## Fetch route notes

- `https://docs.luxor.tech/llms.txt` → **HTTP 200** (13.3 KB). Mintlify-style agent index; confirms every docs page has a `.md` twin.
- `https://docs.luxor.tech/hashrateindex/hashprice.md` and `.mdx` → **HTTP 403**, Cloudflare "Attention Required!" block page (2.1 KB HTML) for plain curl with browser UA + --compressed. Workaround that worked: `https://docs.luxor.tech/llms-full.txt` (HTTP 200, 316 KB) contains the full Hashprice page verbatim at its section `# Hashprice (https://docs.luxor.tech/hashrateindex/hashprice)`. Methodology captured from there.
- `https://hashrateindex.com` → **HTTP 200**, 87 KB compressed SSR Next.js HTML. KPI values are server-rendered.
- `https://hashrateindex.com/hashprice` → **HTTP 404** (page does not exist; live hashprice lives on data.hashrateindex.com).
- `https://hashrateindex.com/blog` → HTTP 200, redirects to `https://hashrateindex.com/blog/` (Ghost blog proxied under the main domain; canonical RSS at `https://hashrate-index.ghost.io/blog/rss`, HTTP 200, 82 KB, 15 items).

## Key numbers/facts for the wiki hashprice article (with exact literals + home file)

### Hashprice definition & methodology (file 1 — verbatim)

1. Definition: "Hashprice – a term coined by Luxor in 2019 – quantifies how much a bitcoin miner can expect to earn from a specific quantity of hashrate." (file 1)
2. Index unit: "Luxor's Bitcoin Hashprice Index quantifies the expected value of 1 PetaHash per second (PH/s) of hashrate per day on the Bitcoin Network." (file 1)
3. Denomination inputs: "BTC hashprice is a function of three inputs: block subsidy, transaction fees, and network difficulty." / "USD hashprice is a function of four inputs: block subsidy, transaction fees, network difficulty, and bitcoin price." (file 1)
4. Formula/construction: "Luxor's Bitcoin Hashprice Index uses a 144-block lagging simple moving average to account for transaction fees, and a simple average of the spot price for bitcoin on three US-based cryptocurrency exchanges to account for USD conversion." (file 1)
5. Authority note: "The BTC hashprice formula is used by a majority of mining pools to pay miners for their hashrate." (file 1)
6. Cadence: "Bitcoin's hashprice changes with every new block added to the blockchain (i.e., block height)." (file 1) — live tracking at https://data.hashrateindex.com/network-data/btc; API `GET /hashprice/current` updates "frequently" with rate limit 20-burst/1-per-15s (docs API section, file 1 route note).
7. Difficulty cadence: "Network difficulty is adjusted every 2,016 blocks (approximately every two weeks) to a level that targets an average block time of ten minutes." (file 1)
8. Subsidy status (as written in docs): "The block subsidy is currently 3.125 BTC and the next 'halving' is projected for April 2028." (file 1)
9. Correlation rule: "USD-denominated hashprice is positively correlated with changes to Bitcoin's spot price, block subsidy and transaction fees and negatively correlated with changes to Bitcoin's network difficulty." (file 1)

### Current market snapshot As-Of 2026-10-10 (file 2 — homepage SSR literals)

10. "Hashprice $/PH/DAY $39.44" (file 2, homepage KPI strip)
11. "Projected Difficulty 132.72 T" (file 2)
12. "BTC Price $82,982" (file 2)
13. "Network Hashrate 1002.42 EH/s" (file 2)
14. "Block Time 9m 38s" (file 2)

### September 2026 monthly economics (file 3 — Lookback, published 9 Oct 2026)

15. "The month opened at $39.21 per PH/s/day, closed at $39.92 (+1.8%) and averaged $39.33, the highest monthly average since January." (file 3)
16. "Difficulty averaged 129.24T (+2.0%), and finished the month at 132.76T. Two adjustments occurred and both were upward: +1.31% on September 5 and +4.16% on September 19, the largest single retarget since June 27." (file 3)
17. "the 7-day network hashrate average rose from 926 to 975 EH/s across the month" and "the 7-day hashrate average currently stands at 999 EH/s" (Oct 8) (file 3)
18. "Monthly average BTC hashprice fell 2.0% to 0.00048965 BTC per PH/s/day." (file 3)
19. "Average fee collection fell 10.1% to 0.0199 BTC per block, the lowest since May. Fees were 0.63% of total block rewards, a fifteenth consecutive month below 1%." (file 3)
20. Energy hashprice tiers: "~$137/MWh for under 14 J/TH · ~$99/MWh for 14–19 J/TH · ~$74/MWh for 19–25 J/TH · ~$51/MWh for 25–38 J/TH" vs "average industrial bitcoin mining power cost of $48/MWh" (file 3)
21. Forward market: "Sellers of the September USD contract locked in between $30.10 and $34.72 per PH/s/day against a $39.33 spot settlement." (file 3)
22. "Luxor's Hashrate Forward Market is pricing an average hashprice of $36.65 or 0.00044 BTC per PH/s/day over the October 2026 – March 2027 window." (file 3)
23. "implied network hashrate now crosses 1 ZH/s in January 2027 at 1,029 EH... the strip runs from 953 EH in October to 1,029 EH in January 2027 and 1,053 EH in February" (file 3)

### Geographic hashrate (file 4 — Heatmap, published 5 Oct 2026)

24. "Network hashrate held at ~941 EH/s, +0.1% QoQ... It remains -8.7% year-over-year and ~15% below the ~1,110 EH/s peak set in November 2025." (file 4)
25. Top 3: "United States — 35.6% (~335 EH/s) · Russia — 18.1% (~170 EH/s) · China — 11.7% (~110 EH/s)"; "top three countries commanding roughly two-thirds of global hashrate" (65.4%, down from 66.2%) (file 4)

## Notes / parks

- `https://hashrateindex.com/hashprice` → HTTP 404. Not an error: the route does not exist on the marketing site; live index at data.hashrateindex.com (linked from homepage KPIs).
- Direct `docs.luxor.tech/.../hashprice.md` route blocked (403 Cloudflare) — content recovered verbatim via `llms-full.txt` instead; no invention needed.
- API endpoints for live data (for future capture or queries): `https://api.hashrateindex.com/v1/hashrateindex/docs#/operations/get-hashprice` (public docs; endpoints `/hashprice`, `/hashprice/current`, `/hashprice/volatility`, `/network/difficulty`, `/network/hashrate` — API keys required per Hashrate Index Premium tiers).
- Doc-page caveat for wiki: the methodology page's "block subsidy is currently 3.125 BTC" line predates the April 2024 halving semantics (3.125 BTC is the current epoch subsidy as of 2026-10-10, next halving April 2028) — consistent, no correction needed.
