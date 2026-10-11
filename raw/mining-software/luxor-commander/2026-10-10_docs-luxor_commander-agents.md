# Agents (Commander setup)

> Registry ID: luxor-commander
> Source: https://docs.luxor.tech/platform/commander/setup/agents (captured from https://docs.luxor.tech/llms-full.txt)
> Collected: 2026-10-10
> Published: n/d
> Posture: verbatim
> As-Of: 2026-10-10

Capture notes: direct per-page .md URL returns Cloudflare 403 to curl; captured verbatim from llms-full.txt. Gateway hostnames (agent-gateway.commander.luxor.tech, data-collector.commander.luxor.tech, TCP port 9001) quoted verbatim from the system-requirements table.

## Overview [#overview]

Agents are the on-site bridge between your mining hardware and Commander's cloud platform. Each Agent is a lightweight service that runs on a server at your facility, discovers miners on your local network, streams telemetry data (hashrate, temperature, power, health status, errors) to Commander, and executes remote commands sent back from the platform. Without at least one Agent per site, Commander has no visibility into your miners. This page covers system requirements, multi-agent deployments, and ongoing agent management.

## System Requirements [#system-requirements]

| Requirement      | Details                                                                                                                                                               |
| ---------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Operating System | Linux (Ubuntu 20.04+ / Debian 11+ / RHEL 8+ recommended) or Windows Server 2019+ / Windows 10+                                                                        |
| Architecture     | x86\_64 (amd64) or ARM64 (aarch64) on Linux                                                                                                                           |
| Network          | Outbound TCP (port 9001) to `agent-gateway.commander.luxor.tech` and `data-collector.commander.luxor.tech`; the agent machine must be on the same LAN as your miners. |
| Permissions      | Root / Administrator privileges for service installation                                                                                                              |

<Callout type="info" title="macOS Not Supported">
  The Commander Agent is not available for macOS. Linux or Windows are the recommended platforms for production
  deployments.
</Callout>

<Callout type="info" title="Verify connectivity before installing">
  Before installing the Agent, confirm that port 9001 is reachable from the agent machine. From the machine's terminal, run:

  ```bash
  nc -zv agent-gateway.commander.luxor.tech 9001
  nc -zv data-collector.commander.luxor.tech 9001
  ```

  Both should report a successful connection. If either fails, work with your network team to allow outbound TCP on port 9001 to these endpoints before proceeding.
</Callout>

## Managing Agents [#managing-agents]

### Viewing Agents [#viewing-agents]

All configured Agents are listed in the **Settings** menu, accessed from the Commander Dashboard. Each row shows:

| Field        | Description                                                         |
| ------------ | ------------------------------------------------------------------- |
| **Site**     | The Site the Agent is associated with                               |
| **Agent**    | The Agent name and unique identifier (UUID)                         |
| **Version**  | The version of the Agent software currently running (e.g., v0.23.0) |
| **Status**   | Whether the Agent is currently Enabled and connected, or Disabled   |
| **# Miners** | The number of ASIC miners seen by the agent                         |
| **Actions**  | Start, Pause, Restart, Edit, and Delete your agent                  |

### Editing an Agent [#editing-an-agent]

Click the edit icon on an Agent row to modify its settings, including its name, and network scan ranges.

### Pausing an Agent [#pausing-an-agent]

You can pause an Agent without deleting it by toggling its status. A paused Agent will stop scanning and reporting data, but its configuration will be preserved for re-enabling later.

### Deleting an Agent [#deleting-an-agent]

Click the delete icon on an Agent row to permanently remove the Agent. This will stop all data collection from the Agent's network range. Miners previously discovered by the Agent will no longer receive telemetry updates.

### Multiple Agents [#multiple-agents]

For large Sites with multiple network segments, you can deploy multiple Agents, each scanning a different IP range. This is useful when your facility has separate VLANs, subnets, or physically isolated network segments. Each Agent operates independently and reports to the same Commander instance.

### Resetting an Agent Secret [#resetting-an-agent-secret]

If you lose the secret key for an Agent, you can reset it without deleting and recreating the Agent. Click the edit icon on the Agent row in the Settings page, enter a new secret in the **Secret** field, and click **Update**. After updating, you will need to update the agent configuration on your on-site machine to use the new secret and restart the agent service.

### Agent Versioning and Updates [#agent-versioning-and-updates]

The Agent Version column in the Agents table shows the currently running software version. Agents generally update automatically when a new version is available. If an agent appears stuck on an older version, you can re-download and install the agent binary over the existing installation - the new version will replace the old one while preserving your configuration.

<Callout type="info" title="Tip">
  If the agent download is only available during the initial setup flow, you can create a temporary agent to access the
  download link, install the updated binary on your existing agent machine, then delete the temporary agent.
</Callout>

## What Happens When the Agent Goes Offline? [#what-happens-when-the-agent-goes-offline]

If the Commander Agent loses connectivity or stops running, your miners continue to operate normally - mining is not interrupted. However, several Commander capabilities depend on the agent being online:

* **Telemetry stops** - Commander will not receive updated performance data (hashrate, temperature, power, health status) until the agent reconnects. Dashboard KPIs and charts will go stale.
* **Automation Rules will not fire** - Trigger Rules cannot evaluate conditions and Schedule Rules cannot execute their actions while the agent is offline. Scheduled executions that are missed during the outage are not retried or made up after the agent reconnects.
* **Intelligent Miner optimization pauses** - Profile adjustments stop entirely. Miners will continue running at whatever profile was last applied, which may not be optimal if market conditions change during the outage.
* **Bulk Actions cannot be delivered** - Any new bulk actions initiated from the UI will queue but cannot reach miners until the agent is back online.

The agent's status will show as **Disabled** in the Agents table on the Dashboard. If the agent goes offline due to a computer or hardware-related event (power loss, shutdown), the agent will automatically attempt to restart itself, reducing the need for human intervention.
