# pool.256foundation.org operator state

> Source: https://pool.256foundation.org/api/v1/query and https://pool.256foundation.org/
> Collected: 2026-10-07
> Published: 2026-10-07

Prometheus query time: 2026-10-07T21:22:40Z. No authentication. The metric `worker_shares_valid_total` is difficulty-weighted; `rate(...[5m])` reads as H/s.

Queries and results:

- `sum(rate(worker_shares_valid_total[5m]))` = 76135574160912.16 H/s, which is 76.14 TH/s
- `count(sum by(btcaddress)(rate(worker_shares_valid_total[5m])))` = 18 addresses with hashrate
- `count(rate(worker_shares_valid_total[5m]))` = 45 workers with hashrate

Homepage HTML fetched the same evening was 184805 bytes. The word "stratum" appears 38 times. The phrase "one-click" appears 0 times.

This page is the operator record. It is not the Foundation homepage and it is not https://hydrapool.org/. Those other pages are the ones that still say one-click. Do not copy their wording onto this file.

`dash.256f.org` was not queried. It is a human dashboard, not this API.
