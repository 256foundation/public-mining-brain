# LuxOS Docs — Advanced Thermal Management (ATM)

> Registry ID: luxos-docs
> Source: https://docs.luxor.tech/firmware/features/atmsettings
> Collected: 2026-10-10
> Published: n/d
> Posture: verbatim
> As-Of: 2026-10-10


## Advanced Thermal Management Overview [#advanced-thermal-management-overview]

Advanced Thermal Management (ATM) is a system engineered to dynamically adjust a miner's operating parameters, such as frequency and voltage, based on environmental conditions and user-defined settings. This ensures optimal performance while preventing shutdowns due to overheating.

In high-temperature environments, ATM smoothly underclocks the miner as temperatures rise, preventing shutdowns. As the ambient temperature drops, especially during cooler evenings, ATM automatically restores the miner to its default settings, or even overclocks it if configured by the user. This entire process operates without the need for integrations, triggers, or manual intervention.

Additionally, ATM serves as a tool to extend the lifespan of mining equipment. By operating at lower temperatures, the equipment experiences fewer failures, translating to an increased operational lifetime.

### Compared to Bitmain's Lower Power Mode [#compared-to-bitmains-lower-power-mode]

ATM differentiates itself from Bitmain's Lower Power Mode (LPM) by offering progressive underclocking and overclocking throughout the day as needed.

For example, ATM might underclock a miner by 3% between 10 AM and 11 AM, then by 5% until 12 PM, 10% until 4 PM, reduce to 5% until 6 PM, and finally return to stock settings afterward. In contrast, Bitmain's LPM results in a constant 25% underclock from start to finish. Moreover, Bitmain's LPM may not sufficiently prevent overheating in certain scenarios, whereas LuxOS ATM can underclock as much as necessary to keep the miner operational.

## How to Enable ATM [#how-to-enable-atm]

There are three main ways to enable ATM: via the web UI, [Commander](/platform/commander/automation/bulk-actions), or our [API](../api/luxminer/atmset).

### LuxOS UI [#luxos-ui]

For individual miners, you can enable ATM from within the LuxOS web UI. Simply type in your miners' IP address into a web browser, navigate to `Temperature & Fans`, and then scroll down to `Advanced Thermal Management` and toggle that on. Don't forget to hit `Save` to confirm your settings.

![Enable ATM from the web GUI](/images/atmenable.gif)

### Commander [#commander]

If you want to enable ATM on one or more miners at a time, use [Commander](/platform/commander/automation/bulk-actions). Select your miners in the **Miners** tab, open **Bulk Actions** and add **Change Temperature Control**. From there you can turn ATM on and configure its settings. Check out our [Recommended Settings](../kb/recommended-settings) page for a good starting point.

### API [#api]

ATM can also be enabled though the [LuxOS API](../tools/luxos/intro) with the [atmset](../api/luxminer/atmset) command.

```sh
$ echo '{"command": "atmset", "parameter":"tjqw4aNI,enabled=true"}' | nc $MINER_IP 4028 | jq
```

## Temperature sources ATM uses [#temperature-sources-atm-uses]

ATM reads temperature from every sensor available on the miner and factors all of them into its decisions. The specific sources depend on hardware:

* **Hashboard temperature** is the core input on all supported miners. ATM uses the highest hashboard reading to decide whether to underclock or allow more power.

* **Chip temperature** is used alongside hashboard temperature on hardware that reports real on-die chip temps. On these miners, a hot reading from either the hashboard or a chip can trigger ATM to underclock. To ramp up — step up a preset profile or increase the power target — every available reading has to be cold (cold = hot temperature − temperature buffer). Chip temperature thresholds can be configured via the [tempctrlset](../api/luxminer/tempctrlset) API command.

* **Water inlet temperature** is used alongside hashboard (and chip, when available) on hydro-cooled miners. ATM treats the inlet reading as an additional input, not a replacement for the others. Water inlet temperature thresholds can be configured via the [tempctrlset](../api/luxminer/tempctrlset) API command.

<Callout type="info">
  {" "}

  **Water inlet ATM is a system-wide lever.** Configuring water inlet ATM on only a portion of the miners in a shared cooling
  system generally has little effect on system-wide temperatures. The machines that *are* configured will respond to inlet
  temperature changes and end up underclocked more than necessary, while the rest of the fleet continues to run at full power.
  For water inlet ATM to do its job, apply the same configuration across every miner on the cooling system.{" "}
</Callout>

## ATM settings [#atm-settings]

* **Minimum Profile:** The minimum profile sets the minimum boundary profile ATM can decrease to. By default the minimum profile is unbounded, meaning ATM will drop to the lowest profile available if required.

  If a relatively high power consumption (voltage & frequency) profile is configured as the minimum boundary ATM might not be capable of preventing the machine from overheating in high heat scenarios. When the AutoTuner sits at the minimum while temperatures keep climbing, the firmware will eventually [shut the miner down](../kb/eventstroubleshooting#early-shutdown-triggered) to protect the hardware.

  On models that support power targeting, the minimum profile acts as the power minimum (the floor the AutoTuner will not underclock below). Setting it adjusts `power_min`; clearing it unbounds the minimum. You can also set the floor directly in watts via [powertargetset](../api/luxminer/powertargetset).

* **Maximum Profile:** The maximum profile sets the top-end boundary profile ATM can increase to. By default, the EEPROM profile (stock settings) is used. Users can increase this setting but acknowledge that miners will draw more power.

  The maximum profile can not be unbounded. A maximum profile needs to be selected for ATM to operate. ATM will increase up to the maximum boundary if the temperature allows it to.

  On models that support power targeting, the maximum profile also acts as the power limit for the AutoTuner. Raising it gives the AutoTuner more headroom; lowering it brings the limit down, and pulls the current power target down with it if the target sits above the new limit. Setting a new power target replaces the limit — the wattage you enter becomes both the target and the new limit. ATM continues to underclock in response to heat either way.

* **Temperature Buffer:** Degrees below Hot Temperature at which ATM will allow a profile or power target increase.

* **Chip Temperature Buffer:** Degrees below Chip Hot Temperature at which ATM will allow a profile or power target increase.

  For example, if the observed hashboard maximum temperature is 56C, the temperature buffer is 8C and the Hot Temperature is 65C then ATM will increase a profile within its boundaries. However, if the observed maximum temperature is 60C then ATM will not increase a profile as it risks overshooting temperature by reaching the Hot Temperature and having to come back down again. The default and [recommended](../kb/recommended-settings) value is 8C. Click [here](./tempsandfans) to learn more about Temperature and Fan settings.

* **Startup time:** This parameter specifies the duration before ATM becomes active following a miner's startup. We suggest a 1-minute delay, enabling ATM to commence temperature assessments as soon as heat generation starts.

* **Post Ramping time:** This parameter determines how frequently ATM reviews the temperature following any adjustment to the operational profile. To ensure the ATM receives accurate and timely temperature data after a profile change, we recommend setting this period at 1 minute.

![ATM Settings from the UI](/images/atmsettingsui.png)
