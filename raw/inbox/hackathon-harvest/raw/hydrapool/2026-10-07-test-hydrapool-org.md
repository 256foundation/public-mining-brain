# test.hydrapool.org live read

> Source: https://test.hydrapool.org/ fetched 2026-10-07T21:31:44Z (curl, no login)
> Collected: 2026-10-07
> Published: Unknown

This is the live test instance named in the Hydrapool README. It is not https://pool.256foundation.org/ and it is not https://hydrapool.org/. No login was attempted.

## HTTP

`GET https://test.hydrapool.org/` returned `302 Found` to `/login`. Following the redirect returned `200 OK`. Server: `nginx/1.18.0 (Ubuntu)`. Response headers on both hops: `Cache-Control: no-store`, `X-Content-Type-Options: nosniff`, `X-Frame-Options: deny`, `X-Xss-Protection: 1; mode=block`.

The 200 body is a Grafana SPA shell. `<title>Grafana</title>`. HTML size 58853 bytes. `window.grafanaBootData` is present. Selected public fields from that blob:

- `user.isSignedIn`: false
- `settings.appSubUrl`: empty
- `settings.appUrl`: `https://grafana.p2poolv2.org/`
- `settings.disableLoginForm`: false
- `settings.anonymousEnabled`: false
- analytics identifier: `@https://grafana.p2poolv2.org/`

The same HTML also contains Grafana's default fallback heading: "If you're seeing this Grafana has failed to load its application files". That heading is in the preloader fail block of the stock Grafana login page. This pull did not execute JavaScript, so it does not prove the frontend assets failed in a browser.

`GET https://test.hydrapool.org/login` returned the same 200 Grafana shell (58853 bytes).

## Other paths, same evening

| path | result |
|---|---|
| `/api` | 401, 102 bytes |
| `/metrics` | 200, 1622759 bytes, `text/plain; version=0.0.4` |
| `/grafana` | 302 |
| `/dashboard` | 302 |
| `/status` | 302 |
| `/health` | 302 |
| `/public` | 302 |

`/metrics` is Grafana process metrics, not Hydrapool `worker_shares_valid_total`. There is no public Prometheus query API on this host equivalent to `https://pool.256foundation.org/api/v1/query`. Selected Grafana series from that scrape:

- `grafana_build_info{branch="release-13.0.1",edition="oss",goversion="go1.25.9",revision="a100054f",version="13.0.1"}` = 1
- `grafana_stat_total_users` = 1
- `grafana_stat_active_users` = 1
- `grafana_stat_total_orgs` = 1
- `grafana_stat_totals_admins` = 1
- `grafana_stat_totals_dashboard` = 5
- `grafana_stat_totals_public_dashboard` = 4
- `grafana_stat_totals_datasource{plugin_id="prometheus"}` = 1
- `grafana_live_node_num_clients` = 0
- `grafana_live_node_num_users` = 0
- `process_start_time_seconds` = 1784221631.2 (2026-07-16T17:07:11Z)

This file does not contain a pool hashrate, worker count, or stratum greeting from test.hydrapool.org. Those numbers were not in the unauthenticated HTML or in the Grafana `/metrics` scrape.
