# CoinShares Research & Data — Index + Mining-Relevant Listing

> Registry ID: coinshares-research
> Source: https://www.coinshares.com/research (301 → https://coinshares.com/insights/research-data/)
> Collected: 2026-10-10
> Published: n/d (index)
> Posture: extract
> As-Of: 2026-10-10

## Fetch record

- https://www.coinshares.com/research → HTTP 200, 233,727 B, final URL https://coinshares.com/insights/research-data/ (redirect). Title: "Research & Data | CoinShares".
- Tag-filtered probe `?tags=mining` → HTTP 200 (taxonomy contains an explicit "Mining" tag: `{"id":8773882,"name":"Mining","value":"mining"}`).
- `?page=2` pagination exists (`/insights/research-data/?page=2`, `?page=57`).

## Most recent index entries (verbatim slugs, front page as-of 2026-10-10)

- /insights/research-data/equities-update-09-10-2026/ ("Equities update - Week 41 - October 09 2026")
- /insights/research-data/bitcoin-13f-q2-2026-report/ ("Bitcoin 13F Q2 2026: Professionals hold firm in sell-off")
- /insights/research-data/market-update-08-10-2026/
- /insights/research-data/coinshares-survey-2026-what-wealthy-investors-actually-do-with-digital-assets/
- /insights/research-data/equities-update-02-10-2026/ · market-update-02-10-2026/ · digital-asset-bi-weekly-digest-29-09-2026/ · equities-update-28-09-2026/ · market-update-25-09-2026/
- Weekly node: /insights/the-node/

## Mining-relevant products on the index

- ETF products (nav JSON, verbatim): "CoinShares Bitcoin Mining UCITS ETF", ticker "MINE", ISIN "IE0008EKJPN4"; "CoinShares Bitcoin Mining and Digital Power ETF", ticker "WGMI", ISIN "US91917A2078"; disclaimer names "CoinShares Bitcoin Mining ETF (“WGMI”)".
- No standalone "hashprice"/miner-economics report surfaced in the current front-page index (grep for hashrate/hashprice in SSR HTML: 0 hits). Mining economics exposure is carried by the weekly "Equities update" (covers miners pursuing AI expansion) and the Bitcoin 13F series — both extracted in the companion capture file.

Note: CoinShares' classic miner-economics mining reports did not surface on the current research-data index front page; deeper pages (?page=2+) were not crawled within this pass.
