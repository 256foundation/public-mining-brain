# What is Braiins Manager? (Braiins Academy, verbatim markdown)

> Registry ID: braiins-manager
> Source: https://academy.braiins.com/braiins-manager/overview.md
> Collected: 2026-10-10
> Published: n/d
> Posture: verbatim
> As-Of: 2026-10-10

HTTP 200, text/markdown, 2,494 bytes. Served via Rspress llms.txt + per-page .md route (https://academy.braiins.com/llms.txt lists the full /braiins-manager/* docs tree). Content below is the file as served, verbatim.

---

# What is Braiins Manager?

## Overview

Braiins Manager offers an all-in-one solution for managing both small and large mining operations. It provides **real-time monitoring**, **batch management**, **curtailment solutions**, **automation** of routine tasks, and **energy reporting**, simplifying the complexities of data center management.

With an intuitive interface, it supports automated processes, power optimization, and fleet management across various locations, ensuring seamless and efficient mining operations.

![Braiins Manager App](/static/image/manager-overview.d275c851e8.png)

## How Braiins Manager Works

Braiins Manager operates through integration with the [Braiins Manager Agent](/braiins-manager/agent/overview.md), a complementary software installed locally at the mining data center. The Agent collects real-time data from mining hardware and relays it to the Braiins Manager web application. This setup enables users to remotely monitor and manage their mining fleet, ensuring efficient operation and performance. Through the app, users can manage everything from fleet monitoring to power management and routine tasks automation, keeping full control over their infrastructure remotely.

![Braiins Manager App](/static/image/bm-diagram.a957cfb4d8.png)

## Target Users of Braiins Manager

Braiins Manager is a comprehensive platform designed for two key user types:

- Providers
- Hosting Clients

### 1. Providers

Providers are datacenter operators who either:

- **Self-Mine**: Managing their own mining devices.
- **Host Customers**: Offering services for third-party [customers](/braiins-manager/customers.md) who own mining hardware.

#### Benefits for Providers:

- **Centralized Management**: Easily manage thousands of devices with [batch management](/braiins-manager/workers/workers-list.md), [monitoring](/braiins-manager/dashboard.md), [automation](/braiins-manager/controlflow.md), and [issue tracking](/braiins-manager/issue-tracker.md).
- **Scalability**: Manage operations from small farms to enterprise-level datacenters with features like [Sitemap](/braiins-manager/sitemap.md).
- **Energy and Cost Efficiency**: Monitor [energy consumption](/braiins-manager/energy-reports.md), optimize uptime, and reduce costs via [curtailment](/braiins-manager/curtailment.md) integration, which minimizes energy costs during peak demand times by working with Curtailment Service Providers (CSPs). Maximize profitability with [Price Adapt](/braiins-manager/price-adapt.md), which automatically keeps miners running at the most profitable power target based on energy prices.
- **Client Management**: Easily manage [customers](/braiins-manager/customers.md) and their [mining devices](/braiins-manager/workers/workers-list.md) with seamless [account](/braiins-manager/customers.md#how-to-create-a-customer) tools.
- **Team Management**: [Set up accounts](/braiins-manager/user-interface/index.md#3-settings) for team members with specific permissions.

### 2. Hosting Clients

Hosting clients are customers of a **Provider** hosting their mining hardware.

#### Benefits for Hosting Clients:

- **Performance Monitoring**: Access [near real-time data](/braiins-manager/dashboard.md) on the health and performance of hosted devices.
- **Device Management**: [Manage hosted devices](/braiins-manager/workers/workers-list.md) (if permissions are granted), including actions like rebooting and pausing.
- **Energy and Financial Transparency**: View detailed [energy reports](/braiins-manager/energy-reports.md) for operational costs.
- **Pool Reporting**: Verify that pool payouts align with actual performance.
- **Team Management**: [Create accounts](/braiins-manager/sign-up/index.md#creating-hosting-client-accounts) for colleagues to allow them to access Braiins Manager with equal permissions.

## Key Capabilities of Braiins Manager

Braiins Manager includes a wide range of features tailored to both **Providers** and **Hosting Clients**:

| **Capability** | **For Providers** | **For Hosting Clients** |
| --- | --- | --- |
| [Monitoring](/braiins-manager/dashboard.md) | Monitor total/individual performance | Monitor performance of hosted devices |
| [Batch Management](/braiins-manager/workers/workers-list.md) | Bulk manage devices | Manage hosted devices, if allowed |
| [Sitemap](/braiins-manager/sitemap.md) | Visualize device locations across facilities | N/A |
| [Curtailment](/braiins-manager/curtailment.md) | Automate downtime, reduce energy costs | N/A |
| [Price Adapt](/braiins-manager/price-adapt.md) | Mine at the most profitable power target | N/A |
| [Strike Price Curtailment](/braiins-manager/strike-price.md) | Avoid mining when energy prices surge | N/A |
| [Issue Tracking](/braiins-manager/issue-tracker.md) | Track and resolve worker issues | N/A |
| [Triggers](/braiins-manager/triggers.md) | Automate routine tasks | N/A |
| [Controlflow](/braiins-manager/controlflow.md) | Automate routine tasks | N/A |
| [Scanner](/braiins-manager/scanner.md) | Automatically scan and add miners | N/A |
| [Account Management](/braiins-manager/sign-up/index.md#managing-team-accounts) | Manage teams and hosting clients | Create team accounts |
| [Energy Reports](/braiins-manager/energy-reports.md) | Detailed energy usage management | Monitor energy consumption |

## Key Use Cases

Braiins Manager is adaptable to a wide range of mining operations:

1. **Large-Scale Self-Mining Operations**: Providers benefit from tools like [batch management](/braiins-manager/workers/workers-list.md), [Sitemap](/braiins-manager/sitemap.md), and [Curtailment](/braiins-manager/curtailment.md) or [Issue Tracking](/braiins-manager/issue-tracker.md) and more for efficiency.
2. **Large-Scale Self-Mining Operations**: Providers benefit from tools like [batch management](/braiins-manager/workers/workers-list.md), [Sitemap](/braiins-manager/sitemap.md), [Curtailment](/braiins-manager/curtailment.md), [Price Adapt](/braiins-manager/price-adapt.md), and [Controlflow](/braiins-manager/controlflow.md) automation or [Issue Tracking](/braiins-manager/issue-tracker.md) and more for efficiency.
3. **Hosting Providers**: Manage [client](/braiins-manager/overview.md#2-hosting-clients) devices and operations with full real-time control and customer management tools.
4. **Small to Medium-Sized Operations**: Use Braiins Manager [automation](/braiins-manager/triggers.md) and [monitoring features](/braiins-manager/dashboard.md) to improve efficiency without a large team.
5. **Small to Medium-Sized Operations**: Use Braiins Manager [automation](/braiins-manager/controlflow.md) and [monitoring features](/braiins-manager/dashboard.md) to improve efficiency without a large team.
6. **Hosting Clients**: Monitor device performance, operational costs, and energy consumption through Braiins Manager [monitoring](/braiins-manager/dashboard.md) and [energy reports](/braiins-manager/energy-reports.md) features.

Recommended next step

### Want to validate the setup before you move forward?

Talk to sales if you are choosing products for a larger site, comparing rollout options, or deciding how this should fit into the rest of your mining stack.

[Talk to sales](https://braiins.com/contact-sales) [See Braiins OS](https://braiins.com/os-firmware)

---

Was this helpful?

Yes, thanks! Sort of, thanks! Not really

Talk to us!
