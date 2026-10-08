# CleanPool payouts, filters, and Prometheus

> Source: https://cleanpool.cosatoshi.net/payouts , https://cleanpool.cosatoshi.net/filters , and https://cleanprom.cosatoshi.net/api/v1/query
> Collected: 2026-10-07
> Published: payouts and filters HTML last-modified 2026-08-09; Prometheus observed 2026-10-07

Companion to `raw/hydrapool/2026-10-07-cleanpool-caylon.md`, which covers the dashboard HTML and the 2026-07-26 announcement. This file is the extra public pages plus a live Prometheus read. Dashboard counters in the homepage HTML were still "—" because they are filled by client-side script.

## /payouts

HTTP 200. Title: "Payout · CleanPool". HTML last-modified `Sun, 09 Aug 2026 16:58:52 GMT`. 6686 bytes.

Visible claims on the page:

- Badge text: "PPLNS -1BTC"
- "This is a self-hosted pool running open-source software, pointed at a sovereign full node"
- PPLNS: rolling window of the most recent N shares; reward split by shares in the window when a block is found
- "-1BTC Rule": "This pool has no funding behind it". "The first 1 BTC comes from the first block mined (and the remaining BTC is split via PPLNS). That 1 BTC raised goes straight back into funding, building, and expanding this pool"
- "Pool fee: zero for now. After that first block hits, it moves to a simple flat percentage fee"
- "256 Foundation: 2.1% of each block goes to the 256 Foundation, the folks building the open-source software this pool runs on."
- "No minimum payout. You're paid on every block the pool finds, directly"

These are operator-page claims. They were not checked against a block explorer in this pull.

## /filters

HTTP 200. Title in visible text: "CleanPool — Node Filters". HTML last-modified `Sun, 09 Aug 2026 16:58:52 GMT`. 9788 bytes.

The page says CleanPool builds templates from a Bitcoin Knots node and that the listed items are policy, not consensus. Settings printed on the page:

- `datacarrier=1`
- `datacarriersize=83`
- `permitbaremultisig=0`
- `rejectparasites=1`
- `rejecttokens=1`
- `dustrelayfee=0.00003000`
- `minrelaytxfee=0.00000001`

The page calls `datacarriersize=83` "the single most important setting on this page" and says Core v30 raised the default to 100,000. It says `rejecttokens=1` is Knots-only and off by default, so an explicit choice here. It says the low relay floor is deliberate so cheap monetary transactions still confirm, and that payouts are unaffected by the filters.

## Prometheus at cleanprom.cosatoshi.net

`GET https://cleanprom.cosatoshi.net/` returned 403 (nginx/1.31.3). `GET https://cleanprom.cosatoshi.net/metrics` also 403.

`GET https://cleanprom.cosatoshi.net/api/v1/query` accepted PromQL with no auth, same shape as the Foundation pool API. Query time 2026-10-07T21:33:30Z:

- `sum(rate(worker_shares_valid_total[5m]))` = 55755924201270.79 H/s, which is 55.76 TH/s
- `count(sum by(btcaddress)(rate(worker_shares_valid_total[5m]) > 0))` = 8 addresses with hashrate
- `count(rate(worker_shares_valid_total[5m]) > 0)` = 12 workers with hashrate
- `up` = 1 with labels `{instance="host.docker.internal:46884", job="Hydrapool"}`

A query a few seconds earlier the same minute returned 55467424247712.82 H/s (55.47 TH/s) and 12 workers.
