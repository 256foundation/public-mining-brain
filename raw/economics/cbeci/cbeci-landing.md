# CBECI landing page — Cambridge Bitcoin Electricity Consumption Index

> Registry ID: cbeci
> Source: https://ccaf.io/cbnsi/cbeci
> Collected: 2026-10-10
> Published: live page (continuously updated)
> Posture: extract
> As-Of: 2026-10-10

## Page identity

- Page `<title>`: "Cambridge Blockchain Network Sustainability Index: CBECI"
- Meta description (verbatim): "The Cambridge Blockchain Network Sustainability Index (CBNSI) is created and maintained by the Cambridge Digital Assets Programme (CDAP) Team at the Cambridge Centre for Alternative Finance, an independent research institute based at Cambridge Judge Business School, University of Cambridge."
- The CBECI now sits inside the CBNSI umbrella ("Cambridge Blockchain Network Sustainability Index"); the page is branded "Cambridge Bitcoin Electricity Consumption Index" with nav links Home / About CCAF / Contact.
- Footer: "Cambridge Centre for Alternative Finance © 2026"; contact https://www.jbs.cam.ac.uk/ccaf · ccaf@jbs.cam.ac.uk · "10 Trumpington Street Cambridge CB2 1QA, UK".
- License (footer, verbatim): "This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License".

## Current consumption estimate — as rendered on 2026-10-10

The headline numbers are NOT in the SSR HTML (the SSR shows "LOADING" and empty Vuex state, e.g. `powerDemand:[]`); they are fetched client-side from `https://ccaf.io/cbeci/api/data/live`, which is reCAPTCHA-gated (see cbeci-data-access.md). Values below were observed in a rendered browser session on 2026-10-10 (embedded OpenChamber browser panel, after accepting the analytics banner; reCAPTCHA completed).

Section: "Bitcoin network power demand — history updated every 24 hours"

| Estimate | Power (GW) | Annualised (TWh) |
|---|---|---|
| Theoretical lower bound | 9.48 | 83.08 |
| Estimated (best guess) | 18.48 | 162.04 |
| Theoretical upper bound | 35.56 | 311.70 |

Section: "Bitcoin mining hardware efficiency — history updated every 24 hours"

| Estimate | Efficiency |
|---|---|
| Theoretical lower bound | 9.50 J/TH |
| Estimated | 17.01 J/TH |
| Theoretical upper bound | 30.00 J/TH |

Interactive parameter: "Average electricity cost" slider default sits at 5 on a 1¢–20¢ scale (i.e. the documented default assumption of 0.05 USD/kWh; methodology page: "we assume that, on average, miners pay USD 0.05 per kilowatt-hour (USD/kWh)").

## How the estimate is presented (page structure)

Three chart sections, each with unit toggle and range controls:

1. "Bitcoin network power demand" — Estimated GW + Annualised TWh, lower/upper bounds; chart "Historical annualised electricity consumption" with "Annualised consumption / Power demand" series toggle.
   - SSR note (verbatim): "a 7-day moving average is applied to reduce the effect of short-term hashrate volatility. The model begins on July 18th 2010 due to a lack of available price data for the prior period."
2. "Total Bitcoin electricity consumption" — Yearly / Monthly / Custom; "Yearly consumption / Cumulative consumption" toggle.
   - SSR note (verbatim): "monthly consumption figures are the sum of daily consumption figures calculated by assuming constant power usage over 24 hours at the daily best-guess estimate of Bitcoin's network power demand. The cumulative consumption is the sum of monthly totals since the start of the model on July 18th 2010. A separate analysis that ignores profitability considerations suggests that the cumulative consumption for the period between January 2009 and July 2010 has only amounted to 4.74 megawatt-hours (MWh), or 0.00000474 TWh – a mere rounding error. It is therefore safe to assume that the cumulative consumption figure listed above provides a robust estimate of Bitcoin's total consumption since its inception in 2009."
3. "Bitcoin mining hardware efficiency" — lower/estimated/upper J/TH; chart "Energy efficiency of bitcoin mining hardware".
   - SSR note (verbatim): "efficiency refers to the amount of electricity (in Joules) required to perform a given amount of computational work (one terahash) per second. Hence, the higher the value, the lower the efficiency."

Electricity-cost slider copy (verbatim): "The electricity cost parameter plays a crucial role in modelling the economic lifetime of mining hardware. You can adjust the parameter below to explore how the model reacts." / "Click here to restore the default assumption".

Charts are Highcharts (console warning confirms "Highcharts"); observed annualised-consumption chart axis ran Jan '25 – Jul '26 with ticks 40–480 TWh.

## Data-access posture observed on the page

- Before data loads, each chart section showed a "Live estimates — Available on request — Request access" overlay/button group (verbatim labels captured in the body snapshot; the "Request access" buttons are `#blur > div > button`-style overlays that disappear once data renders). I.e. live/raw data access is request-gated, not open download, as presented on the landing page.
- The rendered page initially displayed "LOADING" with blank estimate boxes; numbers only appeared after the analytics-consent "Accept" click + reCAPTCHA round-trip. Console logged `requestStorageAccess: Permission denied.` from `https://www.recaptcha.net/recaptcha/api2/anchor?...&k=6LcxxtUpAAAAAGGCa99eoB7bpeI2fKdHyg-1NZQ_&co=aHR0cHM6Ly9jY2FmLmlvOjQ0Mw..` (site key 6LcxxtUpAAAAAGGCa99eoB7bpeI2fKdHyg-1NZQ_, invisible recaptcha via recaptcha.net).

## Fetch notes

- `curl --compressed` + Chrome/126 UA → HTTP 200, `text/html; charset=utf-8`, 149,837 bytes (server: nginx/1.14.2, via: 1.1 google).
- SSR HTML is a Nuxt app: `window.__NUXT__` payload (118 KB) contains country properties (Mining Map legacy data, e.g. flags on firebasestorage.googleapis.com bucket `ccaf-afea`) but NOT the current CBECI estimates; those arrays are empty server-side.
- Frontend JS (`/cbnsi/_nuxt/*.js`) reveals API base default `baseURL||n.baseUrl||"https://ccaf.io/cbeci/api"` with calls `getStats: n.get("/data/stats/".concat(e))`, `getDataPrice: n.get("/data/".concat(e))`, `getMapCountries: n.get("/charts/mining_map_countries")`, and a separate `https://api.ccaf.io/v1/projects` fetch used for the CBNSI project switcher. Details and statuses in cbeci-data-access.md.
