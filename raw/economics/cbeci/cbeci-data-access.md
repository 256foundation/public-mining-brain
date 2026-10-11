# CBECI data access pointers — API, dataset download, hardware list, change log

> Registry ID: cbeci
> Source: https://ccaf.io/cbnsi/cbeci (+ endpoints discovered from SSR/JS)
> Collected: 2026-10-10
> Published: n/a
> Posture: extract (pointers only — full dataset NOT downloaded per no-massive-data rule)
> As-Of: 2026-10-10

This file records WHERE the CBECI data lives and how to get it. No bulk dataset is stored in this repo.

## Dataset download endpoint (historical daily series, CSV)

- Pointer URL (linked on the methodology page, on the word "initial"): https://demo.cbeci.org/api/v1.0.5/download/data
  - `HEAD` → HTTP 302 → Location: https://demo.ccaf.io/cbeci/api/v1.0.5/download/data
  - Redirect target `GET` (range 0–1200 only, to validate) → HTTP 200, content served as CSV (content-type reported as text/html; body is CSV).
  - CSV first line (verbatim): `Average electricity cost assumption: 0.05 USD/kWh,,,,`
  - CSV column header (verbatim): `Timestamp,Date and Time,MAX,MIN,GUESS`
  - Data begins `1404777600,2014-07-08T00:00:00,...` — daily rows with MAX/MIN/GUESS power-demand columns (GW).
  - NOTE: this is the v1.0.5-era model dataset (starts 2014-07-08), i.e. the endpoint linked from the methodology's "initial iteration" sentence. The CURRENT (v1.4.0) full dataset location was not exposed as a direct download on the SSR pages; the landing page presents "Live estimates — Available on request — Request access".
- Full CSV deliberately NOT downloaded or committed (no-massive-data rule). Only a 1,200-byte range was fetched to validate the pointer.

## Live/stats JSON API (production)

- Base (frontend JS default): `baseURL||n.baseUrl||"https://ccaf.io/cbeci/api"` (from /cbnsi/_nuxt/*.js)
- `GET https://ccaf.io/cbeci/api/data/stats/live` → HTTP 200, `application/json`, 26 bytes:
  `{"digiconomist":"204.44"}` (matches Table 2 "Digiconomist — Live estimate — 204.44" on the methodology page)
- `GET https://ccaf.io/cbeci/api/data/live` → HTTP 400, body: `Bad Request — Invalid recaptcha response` (bare curl without reCAPTCHA token). This is the endpoint the landing page's headline numbers depend on; it requires the invisible reCAPTCHA (site key 6LcxxtUpAAAAAGGCa99eoB7bpeI2fKdHyg-1NZQ_, recaptcha.net, "invisible") executed by the site's JS.
- `GET https://ccaf.io/cbeci/api/data/stats/total|live_total|consumption|bitcoin|btc|cbeci` → HTTP 500 (server-side error, wrong arg); `GET .../charts/total_electricity_consumption/daily|latest` → HTTP 404. (Probing record only; correct current chart paths were not enumerated.)
- Other API paths found in the frontend JS (untested, pointer material only): `/charts/mining_map_countries`, `/data/<price>`, `/data/stats/<price>`, `/charts/total_bitcoin_greenhouse_gas_emissions`, `/charts/total_yearly_bitcoin_greenhouse_gas_emissions`, plus `/eth/pos/...` and `/eth/pow/...` CBNSI sibling endpoints.
- Separate CBNSI projects API: `https://api.ccaf.io/v1/projects` (used by the CBNSI project switcher; the JS filters `e.projects.find(... "CBN...")`).

## Historical API host referenced in methodology text

- `https://demo.ccaf.io/cbeci/api/data/stats/live` → HTTP 200, `application/json`, `{"digiconomist":"204.44"}` (same payload as production; CORS `access-control-allow-origin: *`).
- This URL appears in the methodology page's Table 2 context (Digiconomist live-estimate row), not as the CBECI's own data feed.

## Mining hardware list (model input)

- http://sha256.cbeci.org → HTTP 200 (follows to HTTPS) → title "Mining equipment list - Google Sheets". This is the public, commentable list of 100+ SHA-256 ASICs referenced in the methodology ("The complete list is available at http://sha256.cbeci.org").

## Change log

- Methodology text links to: https://ccaf.io/cbnsi/change_log
- 2026-10-10 status: https://ccaf.io/cbnsi/change_log → HTTP 404 (SPA 404 page "The page you requested could not be found."); https://ccaf.io/cbnsi/cbeci/change_log → HTTP 200 but renders the same "404 Page Not Found" content (soft-404). Change log route appears retired/moved — parked for follow-up.

## Licensing

- Site footer: "This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License" (CC BY-NC-SA 4.0).

## What was NOT captured (by design)

- The full daily/annualised CSV time series (per no-massive-data rule). Pointer above suffices for future programmatic pulls.
- The reCAPTCHA-gated `data/live` payload beyond what the rendered page displayed (see cbeci-landing.md for the observed values).
