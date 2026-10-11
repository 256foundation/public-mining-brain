# LuxOS Docs — Introduction to Firmware

> Registry ID: luxos-docs
> Source: https://docs.luxor.tech/firmware/introduction-to-firmware
> Collected: 2026-10-10
> Published: n/d
> Posture: verbatim
> As-Of: 2026-10-10


# Introduction to Firmware [#introduction-to-firmware]

<Callout type="info" title="Deploy LuxOS with Commander">
  LuxOS is deployed across your fleet with Luxor Commander, available for free with the Commander Lite plan. See
  [Getting Started with LuxOS](/firmware/getting-started) to install it on your miners.
</Callout>

Firmware stands as a pivotal tool in the arsenal of any Bitcoin miner, serving as the essential software required to achieve operational excellence. While OEM built-in firmware fulfills basic operational needs, such as powering the miner on/off, selecting power modes (low, normal, high), and establishing connections with mining pools, its capabilities often fall short of maximizing the full potential of the hardware. The OEM Hardware is well built, and so we are excited to build custom firmware to work with this hardware. LuxOS, is an innovative firmware solution, offering unparalleled adaptability, resilience, and improved profit margins for miners that want to take their operations to the next level.

LuxOS is the first and only Bitcoin ASIC firmware developed, owned, and maintained by a US-based company and the first-ever firmware to achieve SOC 2 Type 2 certification. We work with big 4 Auditors, and a number of other stakeholders to ensure smooth audits of the firmware and helping educate them on firmware with the direction of our clients.

## Curtailment [#curtailment]

One of the standout features of LuxOS is its customizable curtailment capabilities, that facilitates seamless integration with demand response programs across various grids like ERCOT, MISO, NYSO, among others.

LuxOS enables miners to participate in any sort of grid program by allowing them to tailor curtailment parameters to meet the specific requirements of each grid. Through demand & response programs miners are able to help with grid reliability but also maximize their earnings potential by optimizing curtailment strategies based on market conditions and energy demand.

LuxOS [curtailment](./api/luxminer/curtail) enables miners to:

* Drop power consumption to \~25W in under 5 seconds.
* Restore power consumption to normal levels in under 10 seconds.
* Customizable wakeup steps that allow the user to control power-up sequence of the miner to reduce strain on the hardware and manage thermal stress.
* Underclock a percentage of the fleet rather than turning off a subset of machines, improving overall efficiency.

## Dynamic Load Control [#dynamic-load-control]

Miners operating within the Oil and Gas (O\&G) and other energy sectors, face the unique challenge of managing fluctuating energy availability. O\&G mining operations often experience variable generation due to factors like pressure fluctuations, changes in gas output, and temperature variations, which mandates users to modulate their load to align with available energy. This challenge is also experienced by miners running on other energy sources.

Traditionally, miners approached this problem by curtailing individual mining units to manage load control, this method is rudimentary and overlooks potential efficiency gains achievable through a more nuanced strategy.

A more sophisticated approach involves the strategic underclocking of the entire mining fleet, rather than simply powering off select units. By uniformly reducing the clock speeds across all equipment, miners can achieve a proportional decrease in power consumption while minimizing the impact on hashrate loss. For instance, implementing a 10% underclocking across the fleet results in a corresponding 10% reduction in power consumption, yet the decrease in hashrate is significantly less pronounced. This approach optimizes energy utilization, enabling miners to efficiently adapt to fluctuating energy conditions while maintaining operational continuity and maximizing efficiency.

Furthermore, LuxOS allows miners to fine-tune their energy consumption with precision to single-digit percentage accuracy. Software that leverages real-time IoT data fro sources from the infrastructure can provide all the information needed to customize each individual machine. This granular level of control ensures that miners can maximize profitability while minimizing energy waste, ultimately enhancing their competitiveness and sustainability in the Bitcoin mining landscape.

## Temperature Management [#temperature-management]

Temperature management is paramount for Bitcoin miners, as excessive heat can degrade hardware performance and shorten its lifespan. LuxOS addresses this challenge with its robust temperature control mechanism, [Advanced Thermal Management (ATM)](./features/atmsettings), which enable miners to monitor and regulate the temperature of their mining hardware effectively. By maintaining optimal operating temperatures, LuxOS helps prevent overheating preventing equipment failures and operating safely in high-temperature environments.

In high-heat environments, infrastructure cooling and the built-in fans are not enough to cool down the machine and miners end up curtailing their machines or their equipment simply powers off due to reaching the shutdown temperature losing their entire hashrate production. When deployed correctly ATM leads to much higher uptime of machines.

ATM differentiates from Bitmain's Lower Power Mode as it provides a progressive underclock/overclock of the machine as needed throughout the day. For example, ATM might underclock a miner by 3% between 10 AM and 11 AM, then 5% until 12 PM, then 10% until 4 PM then 5% until 8 PM and overclock afterwards when temperatures cool down. In that situation the OEM Firmware LPM will result in a 25% underclock from start to end without the dynamic and smart scaling based on temperatures. Additionally, Bitmain's LPM might not be enough to prevent miners from overheating in certain scenarios and LuxOS ATM can underclock as much as needed to keep a miner hashing in high ambient temperatures. ATM does not require integrations, triggers, or human intervention to operate.

## Tuning & Optimization [#tuning--optimization]

LuxOS offers two autotuning approaches: Power Targeting and [Preset Profiles](./features/presetprofiles). Which one an operator chooses may depend on their hardware model and operational goals. Both operate through the LuxOS AutoTuner and work alongside Advanced Thermal Management (ATM) to maintain stable, efficient operation.

### Power Targeting [#power-targeting]

Power Targeting is a watt-anchored control loop built into the LuxOS AutoTuner. Rather than setting a frequency and allowing power consumption to follow, operators set a power target (in watts) and LuxOS continuously adjusts frequency and voltage to hold the miner at that target — regardless of temperature swings or environmental changes.
On Power Targeting-supported models, Preset Profiles are interpreted as predefined power targets rather than frequency presets. Operators can still select overclock and underclock profiles (+1, -2, etc.), but under the hood LuxOS is managing wattage directly. Operators can also set an explicit power target via the LuxOS UI, [Commander](/platform/commander/automation/bulk-actions), or the [powertargetset](/firmware/api/luxminer/powertargetset) API command.

Power Targeting comes with a new and improved [Advanced Thermal Management (ATM)](./features/atmsettings) system — the tuner continues to enforce thermal limits, stability thresholds, and safety rules while maintaining precise control over the miner's power consumption. Power Targeting is currently available on select models. See [Compatible Miners](./compatibility) for the full list of supported hardware.

### Preset Profiles [#preset-profiles]

For all LuxOS-compatible models not supported by power targeting, LuxOS offers profile based tuning. The operator selects a Preset Profile — each of which defines a preset voltage and frequency combination — and the LuxOS AutoTuner optimizes from there, finding the minimum voltage required to run the miner at that profile's frequency. This reduces power consumption without sacrificing hashrate.

For example, if an S19j Pro 104T runs from factory at 545 MHz with 13.4V, the AutoTuner will find the minimum voltage required to run stably at 545 MHz. Higher voltage than necessary is typically applied from the factory to ensure stability across all conditions — the AutoTuner reclaims that margin.

On Antminer Equihash ASIC miners, such as the Antminer Z15 Pro, the PSU voltage is fixed and Preset Profiles set the frequency, with each hashboard's voltage following from it. AutoTuner support for these miners is Coming Soon<sup>™</sup>.

Every time a new profile is applied, the AutoTuner recalibrates for the new frequency target. It runs continuously, adjusting operating parameters as environmental conditions change to ensure stable operation. The AutoTuner also adjusts frequency per chain of chips to avoid imbalances in the system, and applies new settings at a minimum rate of every 3 minutes to give the miner enough time to stabilize.

### Optimizing For Profitability [#optimizing-for-profitability]

Miners are profit-driven above all else. Their focus should be on continually optimizing margins after factoring in power costs. In periods of declining Hashprice, miners can strategically adjust to more efficient operations, enhancing overall fleet profitability. Similarly, when Hashprice rises, miners can capitalize on this trend by foregoing efficiency and overclocking to maximize hashrate production. Whether using Power Targeting or Preset Profiles, operators have the flexibility to adjust in real-time to changes in Hashprice and maximize returns.

![S19j Pro 104T Margins @ \$60/MWh Opex](/images/s19jpro_margins.png)

The above chart illustrates the potential profit margins of a S19j Pro 104T miner at a \$60/MWh Opex. The chart demonstrates the potential for miners to optimize their operations by adjusting their hashrate to maximize profitability at different Hashprice levels.

## Data and Security [#data-and-security]

We have expanded on the OEM data security and compliance. We have achieved our SOC2 audit highlighting our dedication to data security, availability, processing integrity, confidentiality, and privacy. We have taken steps to become the most institutional firmware that stakeholders can get comfortable with.

## Fees [#fees]

LuxOS firmware operates on a 2.8% fee structure. However, when using our mining pool, users benefit from free pool usage. Enjoy 0% pool fees when mining on Luxor Bitcoin Pool—plus exclusive volume discounts for large-scale miners; contact our team today to learn more.
