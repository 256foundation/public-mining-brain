# Using Components After Adding Workers (Braiins Academy, verbatim markdown)

> Registry ID: braiins-manager
> Source: https://academy.braiins.com/braiins-manager/using-components.md
> Collected: 2026-10-10
> Published: n/d
> Posture: verbatim
> As-Of: 2026-10-10

HTTP 200, text/markdown, 1,399 bytes. Served via Rspress .md route. Content below is the file as served, verbatim. (Related, same route: /braiins-manager/dashboard.md — "displaying critical **KPIs** ... Data is refreshed **every 5 minutes**".)

---

# Using Components After Adding Workers

## Overview

Once your miners are added to the [Workers list](/braiins-manager/workers/workers-list.md), Braiins Manager offers powerful tools to efficiently manage and monitor your mining operations. These tools enable real-time performance tracking, batch management, issue tracking, and automation for tasks like curtailment, providing comprehensive control over your infrastructure.

## Features

### 1. Monitoring

Access real-time performance data in the [Dashboard](/braiins-manager/dashboard.md):
- **Hashrate**: View near real-time and historical data.
- **Power Consumption**: Monitor real-time/historical power usage.
- **Temperature**: Track miner temperature.
- **Uptime & Notifications**: Check miner uptime/alerts.
- **Workers & Statuses**: See distribution of miner models.

**Key Actions**: Zoom the time series graph for specific ranges.

### 2. Batch Management

Manage multiple miners on the [Workers page](/braiins-manager/workers/workers-list.md), allowing actions like restarting or changing pool settings.

**Key Actions**:
- Use the **Actions** dropdown for fleet configurations.
- Click miner IP for individual details.

### 3. Automation

Use [Controlflow](/braiins-manager/controlflow.md) to automate routine tasks.

**Key Actions**: Configure automation for miner groups or your hosting customers.

### 4. Profitability Maximization

Use [Price Adapt](/braiins-manager/price-adapt.md) to automatically keep miners running at the most profitable power target based on energy prices.

**Key Actions**: Set up Price Adapt to optimize miner power targets, or curtail mining when it becomes unprofitable.

### 5. Issue Tracking

[Track and manage](/braiins-manager/issue-tracker.md) miner performance, connectivity, and health issues.

**Key Actions**: Review open issues and resolve them.

### 6. Curtailment

Automate miner shutdowns during peak demand when the [energy price is high](/braiins-manager/strike-price.md), integrate with CSPs, or schedule your [curtailment](/braiins-manager/curtailment.md) times using a calendar.

**Key Actions**: Configure curtailment automation based on your CSP, or set a strike price per miner model to avoid energy price peaks.

### 7. Energy Reports

Track [energy consumption](/braiins-manager/energy-reports.md) and compare with historical data.

**Key Actions**: Set up custom energy reports for customers or locations.

### 8. Sitemap

[Map the layout](/braiins-manager/sitemap.md) of your farm for an overview of miner positions.

**Key Actions**: Define **Groups** and **Racks**, assigning miners for a real-time datacenter layout representation.

### 9. Integrations

Connect Braiins Manager to external systems from **Settings**:
- **Demand response**: link Curtailment Service Providers (CSPs) that dispatch [curtailment](/braiins-manager/curtailment.md) signals automatically.
- **Notifications**: deliver Telegram alerts for [automation](/braiins-manager/controlflow.md) and [curtailment](/braiins-manager/curtailment.md#notifications) events.

**Key Actions**: Set up demand-response and notification in **Settings**.

---

Was this helpful?

Yes, thanks! Sort of, thanks! Not really

Talk to us!
