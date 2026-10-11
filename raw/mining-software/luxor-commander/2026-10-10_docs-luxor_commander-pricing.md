# Commander Pricing (Commander Lite vs Commander Pro)

> Registry ID: luxor-commander
> Source: https://docs.luxor.tech/platform/commander/pricing (captured from https://docs.luxor.tech/llms-full.txt)
> Collected: 2026-10-10
> Published: n/d
> Posture: verbatim
> As-Of: 2026-10-10

Capture notes: direct per-page .md URL returns Cloudflare 403 to curl; captured verbatim from llms-full.txt.

## Plans [#plans]

Commander is available in two tiers, both supporting LuxOS, Bitmain, MicroBT and Canaan firmware.

### Commander Lite (Free) [#commander-lite-free]

Commander Lite provides core fleet visibility and basic firmware management at no cost. It includes:

* **Dashboard** with fleet-wide KPIs, performance charts, and health/error distributions
* **Reports summary** - period-average Hashrate, Power, Efficiency and Temperature KPIs on the Reports page
* **Miners table** with search, filtering, sorting, and CSV export
* **LuxOS firmware management** - install, update and uninstall LuxOS across your fleet, and remove third-party firmware such as Braiins OS or Vnish
* **Bulk actions** - Change Pool Settings, Change Power Settings, Change Temperature Control (including ATM), Fault Recovery, Run LuxOS Command, Sleep, Wake Up, and Reboot across your fleet
* **Agent deployment** and automatic miner discovery

Commander Lite is a good fit for operators who want to deploy and configure LuxOS, including those who use another fleet management tool day to day, or who want to evaluate Commander before committing to a paid plan.

### Commander Pro [#commander-pro]

Commander Pro unlocks the full platform - automation, optimization, and asset management tools designed for operators who want to reduce manual intervention and maximize fleet profitability. It includes everything in Lite, plus:

* **Reports** - historical trend charts, a bucket-by-bucket breakdown table and a CSV builder that slices your fleet's history by site, model, firmware, subaccount, client or individual miner
* **Automation Rules** - Trigger Rules that respond to real-time conditions (overheating, hashrate drops, error events) and Schedule Rules that execute at set times (daily curtailment, weekly reboots)
* **Sitemap** - visual facility layout with temperature, hashrate, and power heatmaps for identifying spatial issues that tabular data can't surface
* **Inventory** - track the lifecycle of every physical miner from procurement through retirement, with stable Asset IDs that persist across board swaps and site moves
* **Intelligent Miner** - continuous fleet optimization that adjusts every miner's power profile based on real-time hashprice and electricity costs, keeping efficient machines hashing and idling those that would mine at a loss
* **Hashrate Routing** - a site-level proxy that aggregates miners into a few pool connections, reducing upstream bandwidth, improving share efficiency and splitting hashrate across pools with automatic failover
* **Ancillary services participation** - coordinate with energy programs through integrated power response capabilities
* **VIP customer support**

## Payment Options [#payment-options]

Commander Pro offers two payment methods - choose whichever fits your billing preferences:

| Option                    | How it works                                                                                          |
| ------------------------- | ----------------------------------------------------------------------------------------------------- |
| **\$100 / MW / Month**    | Flat monthly rate based on your site's power capacity, paid via Stripe                                |
| **+0.25% Hashrate Adder** | Added to your Luxor mining pool rate - no separate invoice, deducted automatically from pool earnings |

You can switch between payment methods at any time from **Settings > Commander Plan and Billing Mode**.

## Free Trial [#free-trial]

New Commander Pro subscriptions include a free trial period. You can view your trial status and remaining days from the Settings page. If you choose not to continue after the trial, your account automatically downgrades to Commander Lite with no interruption to monitoring.

## Managing Your Plan [#managing-your-plan]

To view or change your plan, navigate to **Settings** (wrench icon in the Commander navigation bar) and scroll to the **Commander Plan and Billing Mode** section. From there you can upgrade, change payment method, or cancel your Pro subscription.
