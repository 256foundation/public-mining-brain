# A11 Fetch Report — Foreman (foreman-docs, foreman-api) + Luxor Commander (luxor-commander)

> Collected: 2026-10-10
> Captured by: A11 fetch subagent
> Scope: farm-management products. Wrote only under raw/mining-software/foreman/ and raw/mining-software/luxor-commander/. No git commands run. No files outside these two dirs touched.
> Duplication guard: docs.luxor.tech firmware pages (A9) NOT re-captured — only /platform/commander/* and the marketing landing.

## Files written (11)

### Registry foreman-docs (raw/mining-software/foreman/)
| File | Source | HTTP | Posture |
|---|---|---|---|
| 2026-10-10_foreman-docs_obm-io-miners-product-overview.md | https://foreman.mn/ → https://obm.io/miners/ | 301→200 | verbatim (HTML→text) |
| 2026-10-10_foreman-docs_obm-io-features.md | https://obm.io/features/ | 200 | verbatim (HTML→text) |
| 2026-10-10_foreman-docs_obm-io-pricing.md | https://obm.io/pricing/ | 200 | verbatim (HTML→text) |

### Registry foreman-api (raw/mining-software/foreman/)
| File | Source | HTTP | Posture |
|---|---|---|---|
| 2026-10-10_foreman-api_quick-guide-foreman-api.md | https://support.foreman.mn/hc/en-us/articles/48780631909531 (via Zendesk JSON API) | 200 | verbatim |
| 2026-10-10_foreman-api_swaggerhub-openapi-endpoint-surface.md | https://api.swaggerhub.com/apis/foremanmining/foreman-api/2.0.0/swagger.json | 200 | verbatim (OpenAPI excerpt: full path list + selected endpoint JSON + schemas) |
| 2026-10-10_foreman-api_how-to-find-the-client-id.md | https://support.foreman.mn/hc/en-us/articles/31572906125851 (via Zendesk JSON API) | 200 | verbatim |

### Registry luxor-commander (raw/mining-software/luxor-commander/)
| File | Source | HTTP | Posture |
|---|---|---|---|
| 2026-10-10_luxor-tech-commander-landing.md | https://luxor.tech/commander/ | 200 | verbatim (HTML→text) |
| 2026-10-10_docs-luxor_commander-getting-started.md | https://docs.luxor.tech/platform/commander/getting-started (from llms-full.txt) | 200 (llms-full) / 403 (direct .md) | verbatim |
| 2026-10-10_docs-luxor_commander-pricing.md | https://docs.luxor.tech/platform/commander/pricing (from llms-full.txt) | 200 / 403 direct | verbatim |
| 2026-10-10_docs-luxor_commander-agents.md | https://docs.luxor.tech/platform/commander/setup/agents (from llms-full.txt) | 200 / 403 direct | verbatim |

## SSR vs JS shell (per site)

- **obm.io (foreman.mn)**: SSR WordPress (Yoast). Full content server-rendered incl. JSON-LD SoftwareApplication blocks. Not a JS shell. `foreman.mn/llms.txt` returns the HTML page (obm.io/miners/) — no llms.txt exists (obm.io/llms.txt → 404). `foreman.mn` 301 → `https://obm.io/miners/`.
- **support.foreman.mn**: Zendesk Help Center. HTML pages are Cloudflare-challenged: `/hc/en-us` → 302→301→**403 "Just a moment..."** to curl. Workaround: the Zendesk Help Center JSON API is fully open (HTTP 200): `/api/v2/help_center/en-us/articles.json` (206 articles, 3 pages), `/sections.json`, `/articles/{id}.json` (includes body). Not a JS shell once via API.
- **docs.luxor.tech**: `/llms.txt` and `/llms-full.txt` (316 KB, full docs) serve HTTP 200; per-page `.md` URLs (e.g. `/platform/commander/getting-started.md`) return **403 Cloudflare "Attention Required!"** to curl — used llms-full.txt section split instead (as anticipated in brief).
- **luxor.tech/commander**: SSR Next.js, HTTP 200, full hero/features/FAQ questions in HTML; FAQ answers are collapsed accordions (not in DOM).

## Key facts — Foreman (OBM) [foreman-docs]

- Identity/rebrand: site is OBM, Inc. (Baltimore, MD); Foreman formerly "OBM" — page title "Bitcoin Miner Solutions - OBM", canonical obm.io/miners/. Login at dashboard.foreman.mn.
- Positioning (JSON-LD, obm.io/miners/): "Foreman is OBM's flagship Bitcoin mining management software that enables miners to remotely manage their sites from anywhere with automation, operational insights, and precision controls to optimize efficiency and profitability."
- Scale claim (miners page): "Foreman is the industry-leading bitcoin mine management software, trusted by more than 10,000 customers to remotely manage sites of any size."
- JSON-LD featureList (verbatim): ["Remote site and fleet management","Hands-free, automated energy management","Real-time monitoring and performance insights","Automations and controls to reduce manual work","Alerts and notifications for operational issues","Tools to optimize uptime and operational efficiency"]
- Feature pillars (miners page): Simplify Mine Management ("Reboot idle miners... Apply updates across dozens or thousands of miners simultaneously"), Optimize Energy Consumption ("Curtail, slow down, or overclock mines automatically based on real-time pricing"), Boost Profitability, Turn Data Into Decisions (Foreman Intelligence: "portfolio-level visibility into your operation, no data analyst required").
- Features page (obm-io-features.md) — Essentials: Real-Time Monitoring & Insights; Miner Management & Configuration (Site Map, tickets); Issue Detection & Resolution (alerts via "Discord, Telegram, Google Chat, and Slack"; automated "rebooting or changing pools"); Infrastructure Integration & Monitoring ("Smart PDUs & Phase Balancing — Monitor each miner's consumption directly from the PDU port and perform hard reboots through your dashboard", Cooling Towers, External Fans, network switches); Power Controls ("Set customizable rules to respond instantly to events such as time of day, miner temperatures, or profitability").
- Premium add-ons: Advanced Power Management — Price Response Plus with three strategies: "Basic — Delivers reliable on/off control when strike price thresholds are met", "Power Mode — Adds discrete states to underclock or overclock", "Wattage Target — Enables granular, wattage-level precision"; Partner Integrations ("Aggregators such as Voltus, CPower, and GridBeyond"); Adaptive Dispatches ("Set Point Dispatches", "Buffered Dispatches", "Execution Sequences – Mine only your most profitable miners when you curtail part of your load"); Assets & Inventory; Foreman Intelligence; Security & Compliance ("SOC 1 and SOC 2 reports, and maintains ISO 27001 certification", SSO); Managed Network Services.
- Pricing (obm-io-pricing.md): "Essential Pricing $0.60 Per Miner / Month, Billed Monthly, Free 30-day trial"; "Enterprise Pricing — Custom Pricing". Premium modules are add-ons (Advanced Power Management, Assets & Inventory, Foreman Intelligence, Security & Compliance, Managed Network Services).
- Immersion: no immersion/immersion-ready claim found on captured pages. On-prem agent is "Pickaxe" (KB sections); firmware management incl. "How To: Install and Manage LuxOS with Foreman" exists in KB (not captured, out of file budget).

## Key facts — Foreman API [foreman-api]

- API overview (quick-guide-foreman-api.md): "The Foreman API gives developers and operators programmatic access to Foreman's mine management platform."
- Base URL: `https://api.foreman.mn/api/v2/` — "All requests must be made over HTTPS. Plain HTTP is not supported."
- Auth: `Authorization: Token YOUR_API_KEY` — "The API uses API key authentication." Key found in dashboard: Man-with-a-Tie icon → My Account → "API Information" section.
- Interactive reference: SwaggerHub `https://app.swaggerhub.com/apis-docs/foremanmining/foreman-api/2.0.0`.
- Resource groups (verbatim table): Miners ("List, add, update, delete, and reboot miners. Retrieve real-time metrics including hashrate, temperature, fan speed, and power consumption."), Pickaxes (agents), Alerts, Pools ("Add, update, or switch pools for individual miners or groups programmatically"), Farms & groups ("Perform bulk operations — such as rebooting all miners at a site or switching pools for an entire farm"), Power controls ("Retrieve power consumption data and trigger power management actions on supported hardware"), Events & audit logs.
- Pagination: `page` (default 1), `per_page` (default 25, max 100); 429 → "implement exponential backoff".
- OpenAPI spec (swaggerhub-openapi-endpoint-surface.md): "Foreman API" v2.0.0, **92 paths**. Power/fleet control endpoints (verbatim summaries):
  - `POST /actions/reboot/{minerId}` — "Reboots the miner." ("Currently only ASIC support.")
  - `POST /actions/power-mode/{minerId}` — "Change the power mode." ("some modes may only be available to certain miner models and manufacturers")
  - `POST /actions/change-pools/{minerId}` — "Changes mining pools."; `POST /actions/change-pools/bulk/{clientId}` — "Bulk change mining pools for multiple miners."
  - `POST /actions/blink/{minerId}`, `POST /actions/fetch-miner-logs/{minerId}`, `POST /actions/network/{minerId}` (static IP), `POST /actions/change-password/{minerId}`, `POST /actions/vnish-overclock/{minerId}`, `GET /actions/status/{commandId}`.
  - Fleet read: `GET /clients`, `GET /clients/{clientId}/miners`, `.../miners/summary`, `.../miners/group-summary`, `GET /clients/{clientId}/pickaxes`.
  - Power/curtailment: `POST /curtailment/{clientId}/once` — "Creates a single-fire curtailment. This is intended to be the mechanism to connect the system to a utility signal."; `/curtailment/{clientId}/plans`, `/curtailment/plans/{planId}/run`, `/curtailment/runs/{runId}/revert`; `/dispatches/{clientId}` — "This is a paid feature disabled by default."; broker/CSP dispatch endpoints (`/broker/{broker}/dispatches/...`, `/csp/{csp}/dispatches/...`); Voltus/CPower/HiveOS key endpoints.
  - Also: firmware (`/firmware/{clientId}/manufacturers...`), assets/inventory, tickets, site-map, custom-field, tags, reports, `/system/asics`, `/ping` (unauthenticated).
- Credentials article (how-to-find-the-client-id.md): My Account → API Information shows "Your unique API Key" and "Your Client ID"; "required for configuring your Pickaxe installation".
- Note: API key/Client ID article updated 2026-05-18; API guide created 2026-04-06, updated 2026-08-07.

## Key facts — Luxor Commander [luxor-commander]

- Landing (luxor-tech-commander-landing.md): "Luxor Commander brings real-time miner monitoring software, bulk remote commands, and automated profitability optimization together with your pool, firmware, and energy tools — all in one platform."
- Feature blocks: Real-Time Fleet Monitoring ("Monitor hashrate, power consumption, efficiency, and temperature for every miner across all sites... CSV export"); One-Click Bulk Actions ("Change pool settings, adjust ATM tuning profiles, reboot, sleep, or wake thousands of miners in a single operation. Configurable batch sizes and delays"); Visual Sitemap & Heatmaps ("rack-and-stack layout with heatmap overlays for temperature, hashrate, and power"); Inventory & Asset Tracking ("Smart tracking prevents losing track of assets after swapping PCB or hashboards"); Automation Rules.
- Grid-Interactive Mining (with Luxor Energy): Intelligent Miner — "Every five minutes, Intelligent Miner ingests spot hashprice, live power prices, and your energy-contract terms — then sets the most profitable power profile for each machine."; claims "+8–14% more profit than on/off curtailment"; Demand Response — "programs like ERCOT's ECRS", "$40–100K+ grid revenue per MW / yr (varies by year)"; 4CP optimizer — "predicts the coincident peaks", "~$40–67K transmission charges avoided per MW / yr".
- "Coming Soon" roadmap on landing: IoT Devices Integration (PDUs/containers), Ticketing System, AI-Powered Operational Insights.
- Docs getting-started: "Luxor Commander is Luxor's cloud-based Miner Management Software (MMS) for Bitcoin mining operations." Supports "miners running LuxOS, stock Bitmain, and MicroBT firmware"; agent has "protocol handlers for both Bitmain (Antminer), MicroBT (Whatsminer) and Canaan (Avalon) - LuxOS is not required, though some advanced features (such as Intelligent Miner profile optimization and ATM configuration) are LuxOS-specific."
- Architecture: Commander Agent = "a lightweight service that runs at your mining site and serves as the bridge between your local miner network and the Commander cloud platform" — scans LAN, streams telemetry, executes commands.
- Plan tiers (docs pricing): **Commander Lite (Free)** — "dashboard and miners table, installing and updating LuxOS, and bulk actions to change pool, power and temperature settings, sleep, wake up and reboot your miners" (+ Reports summary KPIs, agent deployment/discovery, uninstall third-party firmware "such as Braiins OS or Vnish"). **Commander Pro** — adds full Reports, Automation Rules (Trigger + Schedule), Sitemap, Inventory, Intelligent Miner, Hashrate Routing ("site-level proxy... automatic failover"), "Ancillary services participation", "VIP customer support".
- Commander Pro payment options (verbatim table): "**$100 / MW / Month** — Flat monthly rate based on your site's power capacity, paid via Stripe" OR "**+0.25% Hashrate Adder** — Added to your Luxor mining pool rate - no separate invoice, deducted automatically from pool earnings". Switchable in "Settings > Commander Plan and Billing Mode"; free trial on Pro; downgrade to Lite "with no interruption to monitoring".
- Agents page: OS "Linux (Ubuntu 20.04+ / Debian 11+ / RHEL 8+) or Windows Server 2019+ / Windows 10+"; arch "x86_64 (amd64) or ARM64 (aarch64)"; network "Outbound TCP (port 9001) to `agent-gateway.commander.luxor.tech` and `data-collector.commander.luxor.tech`"; "macOS Not Supported". Offline agent behavior: mining continues; "Automation Rules will not fire"; "Intelligent Miner optimization pauses"; "Bulk Actions cannot be delivered".
- API surface (context from llms.txt, not written as separate files to avoid A9/API overlap): Commander REST under `/v2/commander/*` — actions (create-commander-action incl. "Install Firmware"/"Update Firmware"/"Power Configuration"/"Run LuxOS Command"/"Blink Miner LED"), agents CRUD, automation-rules (trigger/schedule), inventory assets CRUD+bulk, reporting (get-miners, get-miner-details batch ≤500, performance history/summary). Auth per docs.luxor.tech/platform/api/introduction.md (platform API intro page — not captured here).

## Failures / parks

- `foreman.mn/llms.txt` → 200 but serves the WordPress HTML page (alias of obm.io/miners/), not an llms manifest; `obm.io/llms.txt` → 404. No agent-friendly docs route on the marketing site; SSR HTML used instead.
- `https://support.foreman.mn/hc/en-us` (and any /hc HTML) → **403 Cloudflare challenge** to curl (302→301 chain first). Parked HTML; content captured via Zendesk JSON API (200).
- `https://docs.luxor.tech/platform/commander/*.md` → **403 Cloudflare** to curl (as warned in brief). Worked around via `https://docs.luxor.tech/llms-full.txt` (200) section extraction.
- luxor.tech/commander FAQ answers: collapsed accordions, answers not present in server HTML (questions only) — minor gap, answered by docs instead.
- Nothing else failed; no JS-shell parks (all four sites server-render their content by at least one route).
