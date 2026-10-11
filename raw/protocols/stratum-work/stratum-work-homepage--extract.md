# Stratum Work — homepage/landing (static text extract)

> Registry ID: stratum-work
> Source: https://stratum.work/
> Collected: 2026-10-10
> Published: n/d (live web app; repo bboerst/stratum-work created 2024-05-28)
> Posture: extract
> As-Of: 2026-10-10

## SSR / JS-shell assessment

HTTP 200, ~26,725 bytes HTML. Server: Next.js (`x-powered-by: Next.js`, `x-nextjs-prerender: 1`, `x-nextjs-cache: HIT`) — the page is **statically prerendered, not a pure JS shell**: real UI chrome (nav, table headers, timing legend, status strings) is present in the HTML. However, **live job data is NOT in the HTML** — the SSR'd table body is empty (`<tbody></tbody>`) with placeholder text "Waiting for new stratum messages...", and the connection badge renders its initial state "Disconnected". Live `mining.notify` rows arrive client-side over a websocket/SSE stream. Per mission, the live visualizer stream was **parked**; only the static marketing/about text is captured here. The site is a real-time tool with essentially no long-form marketing copy — the "about" text lives in the meta description and the GitHub README (captured separately, verbatim).

## Static text found in the prerendered HTML

### `<title>` and meta description (verbatim)

> Stratum Work

> Web app that streams realtime mining pool stratum v1 messages to a table.

(Repo GitHub description, identical in meaning: "Web app that streams realtime mining pool stratum messages to a table." — from GitHub API repo metadata.)

### Navigation (labels + title attributes, verbatim)

| Label | href | title attribute |
|---|---|---|
| Table | `/` | "Main view with table and timing chart" |
| Timing | `/timing` | "Full screen pool timing visualization" |
| Sankey | `/sankey` | "Sankey diagram visualization" |
| Infra | `/infra` | "Realtime Stratum infrastructure metrics" |
| Pools (button) | — | "Filter mining pools" |
| GitHub icon | https://github.com/bboerst/stratum-work | "GitHub Repository" |

Initial stream-status indicator (verbatim): "Disconnected" with tooltip title "Disconnected from data stream".

### Main table columns (verbatim, left to right)

Pool Name · Height · Coinbase Script (ASCII) · First Tx · First Tx Fee Rate · BIP-110 · Time Received · Ntime · Merk. 0 … Merk. 12 (thirteen merkle-branch columns) · Coinbase Outputs · Coinbase Output Value (default sort, descending arrow)

Note: a dedicated **BIP-110** column exists in the table UI.

### Timing-panel legend (verbatim strings)

"Core Fields": `A` - AuxPOW hash · `M` - Merkle branches · `C` - Clean jobs · `P` - Prev hash · `H` - Height · `V` - Version · `N` - nBits · `E` - Extranonce2 length

"Transaction Fields": `X` - TX version · `L` - TX locktime · `I` - Input sequence · `W` - Witness nonce · `U` - Output structure · `K` - AuxPOW merkle size · `J` - AuxPOW nonce

"OP_RETURN Protocols": `R̶` - RSK Block · `C̶` - CoreDAO · `S̶` - Syscoin · `H̶` - Hathor Network · `E̶` - ExSat · `O̶` - Omni · `U̶` - Runestone · `W̶` - WitnessCommitment · `T̶` - Stacks Block · `B̶` - BIP47 Payment · `Ø̶` - Empty OP_RETURN · `Ω̶` - Other OP_RETURN · (gray dot) - First/duplicate

### Other static UI strings (verbatim)

"Timing" (panel heading) · "Options" · "Legend" · "Findings" · "No findings" · "Waiting for new stratum messages..." · "Waiting for updates..." (block-height ribbon placeholder)

## How it connects to pools (from the repo README, captured separately verbatim)

Collector instances connect to mining pools over Stratum (`stratum+tcp://…`, e.g. `--pool-name "NewPool" --url "stratum+tcp://newpool.com:3333" --userpass …`), capture `mining.notify` messages, store them in MongoDB and publish to RabbitMQ; a backend processes blocks from a Bitcoin node and identifies the mining pool by coinbase analysis; the web app consumes the stream and — per README — **all decoding/formatting/visualization happens client-side** ("trustless data processing"). A raw Server-Sent Events endpoint `GET /api/stream` exposes the same data.

## Parks

- Live `mining.notify` job stream / websocket capture: parked (JS/websocket-delivered, explicitly out of scope per mission).
- `/timing`, `/sankey`, `/infra` subpages: not captured (same app shell; live-data views).
- Historical data API endpoints: not probed (out of mission scope).
