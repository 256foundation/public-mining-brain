# LuxOS Docs — Power Targeting

> Registry ID: luxos-docs
> Source: https://docs.luxor.tech/firmware/features/powertargeting
> Collected: 2026-10-10
> Published: n/d
> Posture: verbatim
> As-Of: 2026-10-10


With power targeting, you tell the miner exactly how much power to consume. LuxOS continuously adjusts frequency and voltage to hold the miner at your chosen wattage. Preset profiles ask you to pick a frequency and voltage, and the resulting wattage follows from that choice. Power targeting flips the relationship: you pick the wattage, and the AutoTuner picks the frequency and voltage that land on it.

## Supported Models [#supported-models]

Power targeting is available on select models. See the [compatibility page](../compatibility) for the current list of supported models.

On models that don't support power targeting, LuxOS continues to tune using [preset profiles](./presetprofiles) — same profiles, same workflows, no change in behavior. On supported models, preset profiles still work the way you expect at the surface (+1, -2, Default, etc.), but under the hood LuxOS interprets each profile as a predefined power target rather than a frequency preset.

## Benefits of Power Targeting [#benefits-of-power-targeting]

* **Stable & predictable power consumption:** By setting a power target, LuxOS will optimize the miner's voltage and frequency to reach and maintain that target, continuously fine-tuning to hold consumption at the value you set.
* **Protection against PSU shutdowns:** A fixed watt ceiling keeps the miner clear of over-power protection thresholds.
* **Mixed-fleet coordination:** A watt-based target normalizes consumption across models so any supported miner can be assigned the exact draw needed to hit a site-level load plan.
* **Curtailment without cold starts:** Idle machines at low wattages during curtailment windows, preserving internal heat and skipping cold-start penalties.
* **Power market participation:** Precise wattage control is the foundation for demand response, interval energy trading, and other energy load based Mining workflows.
* **Heat recycling and BTU planning:** BTU output is proportional to watt input — sites recycling hashrate heat can budget thermal output precisely.

## Using Power Targeting [#using-power-targeting]

* How to Use Power Targeting Video (4 minutes): [Watch Video](https://youtu.be/pM-WwF_d4ck?si=Cvlbg4q2H_3WUVK7)

### Setting a power target [#setting-a-power-target]

Power targeting can be configured from the web UI, [Commander](https://luxor.tech/commander), or the [API](../api/luxminer/powertargetset).

#### LuxOS UI [#luxos-ui]

Open the miner's IP address in a browser, navigate to the `Preset Profiles` tab, and enter your desired wattage in the `Power Target` field. Save to apply.

#### Commander [#commander]

Launch Commander, select the miner(s) you want to configure, and open the `Configure Miners` panel. In the `Power` tab, enter a value in the `Power Target` field and click `Review` to apply.

#### API [#api]

Use the [powertargetset](../api/luxminer/powertargetset) command:

```sh
$ echo '{"command":"powertargetset","parameter":"<session_id>,<watts>"}' | nc $MINER_IP 4028 | jq
```

### Updating a power target [#updating-a-power-target]

If you decide you want to run at a different wattage, you can update the power target at any time. Send a new target from Commander, the web UI, or the API, and the miner will smoothly ramp from its current draw to the new value — no restart or profile reset required. You can adjust the target as often as you like; each new value replaces the last one.

### Power target, power limit, and power minimum [#power-target-power-limit-and-power-minimum]

Three terms worth knowing:

* **Power target** — the wattage the AutoTuner actively maintains on the miner.
* **Power limit** — the ceiling the AutoTuner will not exceed.
* **Power minimum** — the floor the ATM will not underclock below. Useful when you want to keep a baseline of power consumption even under thermal pressure, at the cost of allowing the miner to reach an early shutdown if the temperatures keep climbing.

All three can be inspected or changed via [powertargetget](../api/luxminer/powertargetget) and [powertargetset](../api/luxminer/powertargetset).

## How Power Targeting Works with ATM [#how-power-targeting-works-with-atm]

When ATM is enabled, power targeting and ATM run alongside each other. ATM continues to monitor temperature just as it does during preset-profile operation. If thermal conditions rise and push the miner past [ATM's](./atmsettings) configured [temperature settings](./tempsandfans), the miner begins underclocking to cool down. Once temperatures stabilize, a new power target is set at the current power consumption, and this becomes the active target. The original power limit stays intact throughout — so if conditions improve, the miner can ramp back up as high as the original limit.

If the ATM reaches the configured power minimum while temperatures are still rising, the firmware emits a [`POWER_MINIMUM_REACHED`](../kb/eventstroubleshooting#power-minimum-reached) event and stops underclocking further. If the heat keeps climbing past the early-shutdown threshold while sitting at the minimum, the firmware arms a staggered shutdown timer ([`EARLY_SHUTDOWN_PENDING`](../kb/eventstroubleshooting#early-shutdown-pending)) and, if conditions don't improve, eventually shuts the miner down ([`EARLY_SHUTDOWN_TRIGGERED`](../kb/eventstroubleshooting#early-shutdown-triggered)).

## Important Interactions [#important-interactions]

* Targets outside your model's supported range are rejected.
* Setting a new power target overwrites the current power limit.
* Changing your ATM max profile also overwrites the power limit, but only while ATM is enabled. If ATM is off, max profile changes have no effect on the limit. Whichever change — a new power target or a max profile update with ATM on — happened most recently is what the limit reflects.
* Setting a new profile via [profileset](../api/luxminer/profileset) with `update_atm` enabled (the default) clears the power minimum, in addition to updating the power limit.

<Callout type="warn">
  While power targeting is active, manual frequency and voltage changes are rejected. The `frequencyset` and
  `voltageset` API commands return a `PowerBasedRampEnabled` error. To return to preset-profile control, disable power
  targeting first.
</Callout>
