# LuxOS Docs — Getting Started with LuxOS (deployment & install)

> Registry ID: luxos-docs
> Source: https://docs.luxor.tech/firmware/getting-started
> Collected: 2026-10-10
> Published: n/d
> Posture: verbatim
> As-Of: 2026-10-10


LuxOS is deployed with [Luxor Commander](/platform/commander/getting-started), Luxor's fleet management platform. Commander runs in the [Luxor web app](https://app.luxor.tech/commander) and talks to your miners through a lightweight Agent installed at your site.

You only need the free **Commander Lite** plan to deploy LuxOS. Lite lets you install, update and uninstall LuxOS, and change pools, power, temperature and ATM settings in bulk. If you already run your fleet with another tool, such as Foreman or Braiins Manager, you can keep using it: Commander gets LuxOS onto your miners, and your existing tooling takes it from there.

<Callout type="info" title="Helpful links">
  * Miner optimization video (2 minutes): [Watch video](https://www.youtube.com/watch?v=qlZJG0BZKRY)
  * Supported models: [Compatible Miners](./compatibility)
</Callout>

## Before You Start [#before-you-start]

* **Compatible miners:** check your models, control boards and hashboards against the [Compatible Miners](./compatibility) list. Miners must be running stock Bitmain or MicroBT firmware to install LuxOS.
* **A Luxor account:** [sign up](https://app.luxor.tech) if you don't have one yet.
* **A machine for the Agent:** a Linux or Windows computer, mini PC or VM on the same local network as your miners, with outbound internet access. See the [Agent system requirements](/platform/commander/setup/agents#system-requirements).
* **The EULA:** review the LuxOS [End User License Agreement](https://luxor.tech/firmware/eula) before installing.

## Deploy LuxOS [#deploy-luxos]

<Steps>
  <Step>
    ### Create an Agent [#create-an-agent]

    Open **Commander** from the left sidebar of the Luxor app and select **Start Now** (or **Settings → + Agent** if you already have one).

    ![Commander Onboarding](/images/commander-onboarding.png)

    1. Choose a plan: **Commander Lite**, which is free, or **Commander Pro**, which starts with a 60-day free trial. You can change plans at any time.
    2. Select the **Site** the Agent belongs to, or create a new one directly from this step.
    3. Give the Agent a name and a secret, and under **Network Settings** add the network ranges where your miners live. Each range can be an **IP Range** (`192.168.0.0-192.168.1.255`), an **IP List** (`192.168.14.67`) or a **CIDR** block (`10.20.20.0/24`).
    4. If your miners don't use factory default credentials, or run MicroBT stock firmware, add the miner username and password under **Advanced Settings**.
    5. Click **Create New Agent**.

    <img src="/images/commander-agent-add-form.png" alt="The Add Agent form: agent name, secret and network ranges" style="{ display: &#x22;block&#x22;, width: &#x22;100%&#x22;, maxWidth: &#x22;520px&#x22;, margin: &#x22;0 auto&#x22; }" />
  </Step>

  <Step>
    ### Install the Agent [#install-the-agent]

    After you create the Agent, Commander shows the install options with your Agent ID and secret already filled in:

    * **Linux:** copy the terminal command and run it on your Agent machine.
    * **Windows:** run the PowerShell command as Administrator, or download the GUI installer and enter your Agent ID and secret.

    <img src="/images/commander-agent-install.png" alt="Install Commander Agent dialog with Linux and Windows install options" style="{ display: &#x22;block&#x22;, width: &#x22;100%&#x22;, maxWidth: &#x22;480px&#x22;, margin: &#x22;0 auto&#x22; }" />

    Once the Agent connects, it scans your IP ranges and your miners appear in the **Miners** tab within a few minutes. If they don't, see [Troubleshooting](/platform/commander/troubleshooting).
  </Step>

  <Step>
    ### Remove third-party firmware (if needed) [#remove-third-party-firmware-if-needed]

    If any miners run another custom firmware, such as Braiins OS or Vnish, return them to stock first. Select them in the **Miners** tab, open **Bulk Actions** and run **Uninstall Custom Firmware**. The miners reboot into stock firmware, ready for LuxOS.

    <img src="/images/commander-bulk-uninstall-firmware.png" alt="Uninstall Custom Firmware in the Bulk Actions menu" style="{ display: &#x22;block&#x22;, width: &#x22;100%&#x22;, maxWidth: &#x22;480px&#x22;, margin: &#x22;0 auto&#x22; }" />
  </Step>

  <Step>
    ### Install LuxOS [#install-luxos]

    1. In the **Miners** tab, use the [filters](/platform/commander/features/miners#miners-table) to narrow down by model and firmware, then select the miners to install. We recommend starting with a small batch.
    2. Open **Bulk Actions** and add **Install LuxOS**.
    3. In the preview, check the compatibility column, and set a **Batch Size** and **Delay** to limit how many miners reboot at once.
    4. Run the action and follow the progress in the **Action Log**. Each miner's result is recorded individually, so you can retry only the ones that failed.

    <img src="/images/commander-bulk-install-luxos.png" alt="Install LuxOS in the Bulk Actions menu" style="{ display: &#x22;block&#x22;, width: &#x22;100%&#x22;, maxWidth: &#x22;480px&#x22;, margin: &#x22;0 auto&#x22; }" />

    LuxOS keeps each miner's existing network and pool configuration during install. After a few minutes, the miners boot into LuxOS and start hashing.
  </Step>
</Steps>

## Configure Your Miners [#configure-your-miners]

Once LuxOS is running, use [Bulk Actions](/platform/commander/automation/bulk-actions) to apply settings across your fleet. All of these are included in Commander Lite:

| Action                         | What it does                                                                                                        |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------- |
| **Change Pool Settings**       | Set the stratum URL, worker name and password                                                                       |
| **Change Power Settings**      | Choose a [preset profile](./features/presetprofiles) or a [power target](./features/powertargeting)                 |
| **Change Temperature Control** | Set temperature targets and configure [Advanced Thermal Management](./features/atmsettings)                         |
| **Fault Recovery**             | Control automatic hashboard recovery and its limits                                                                 |
| **Run LuxOS Command**          | Send any [LuxOS API](./api/available_commands) command, for example to enable the [AutoTuner](./features/autotuner) |
| **Sleep / Wake Up**            | Curtail miners and bring them back                                                                                  |
| **Reboot**                     | Restart the selected miners                                                                                         |

For a safe starting point, see [Recommended Settings](./kb/recommended-settings). You can also change settings on a single miner from the LuxOS web interface, or programmatically through the [LuxOS API](./api/available_commands).

## Keep LuxOS Up to Date [#keep-luxos-up-to-date]

To upgrade, select your miners and run the **Update LuxOS** bulk action, choosing the **Stable** or **Preview** release channel. As with installs, upgrading in batches limits the number of miners rebooting at the same time. Release notes are in the [LuxOS Changelog](./changelog).

## Use LuxOS With Your Existing Fleet Manager [#use-luxos-with-your-existing-fleet-manager]

LuxOS exposes a CGMiner-compatible API on port `4028`, so third-party fleet management tools can monitor and control LuxOS miners after installation. See [Foreman](./tools_and_integrations/foreman) for an example integration, and the [LuxOS API reference](./api/available_commands) for the full list of commands.

## Frequently Asked Questions [#frequently-asked-questions]

**Do I need to pay for Commander to use LuxOS?**
No. Commander Lite is free and includes everything needed to install, update and configure LuxOS across your fleet.

**What does Commander Pro add?**
Pro adds automation rules, Intelligent Miner, Sitemap, Inventory, Tickets, Reports and VIP support. See [Pricing](/platform/commander/pricing).

**My miner model or firmware isn't supported by Commander. What now?**
Some control boards and recent stock firmware versions require a remote install by the Luxor team. See [Remote Install](./kb/remoteinstall). For scripted or offline installs, there is also the [LuxOS Installer](./tools_and_integrations/luxosinstaller) command-line tool.

**I'm a partner. How do I get credit for the installs I deploy?**
See the [Partner Referral ID](./features/partnerid) program.

If you have any questions, [submit a ticket](https://luxor.tech/contact) and our team will help.
