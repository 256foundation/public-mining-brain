# LuxOS Docs — AutoTuner

> Registry ID: luxos-docs
> Source: https://docs.luxor.tech/firmware/features/autotuner
> Collected: 2026-10-10
> Published: n/d
> Posture: verbatim
> As-Of: 2026-10-10


LuxOS AutoTuner is a smart feature that automatically adjusts your system’s settings to reduce power usage without compromising performance. It works quietly in the background, continuously fine-tuning operating parameters, so that your hardware runs as efficiently as possible, while keeping your equipment healthy. This means you can enjoy lower energy consumption and stable performance effortlessly.

<Callout type="info">
  AutoTuner support for Antminer Equihash ASIC miners, such as the Antminer Z15 Pro, is Coming Soon<sup>™</sup>. Until
  then, those miners run their [Preset Profiles](./presetprofiles) as defined, and turning the AutoTuner on is refused.
</Callout>

## Features [#features]

* Automatic Optimization: Continuously adjusts frequency and voltage to optimize efficiency and maintain stable operation.
* Quick Adjustment: Switching to a new [Preset Profile](./presetprofiles) or [Power Target](./powertargeting) takes effect immediately — the AutoTuner ramps the miner to the new settings without any restart or downtime.
* Performance Maintenance: Ensures chip health and stable hash rates are upheld.
* User-Friendly Controls: Simple enable/disable functionality via [Commander](/platform/commander/automation/bulk-actions) or [API](/firmware/api/luxminer/autotunerset).

## Enabling AutoTuner [#enabling-autotuner]

AutoTuner can be enabled across many miners at once in [Commander](/platform/commander/automation/bulk-actions): select your miners, open **Bulk Actions** and use **Run LuxOS Command** with the `autotunerset` command. It can also be activated programmatically via the [LuxOS API](/firmware/api/luxminer/autotunerset).

The time required for the AutoTuner to complete tuning depends on several factors:

* Temperature: Voltage and frequency calibrations are impacted by temperature. No machine will perform the exact same in different environments.
* Machine and Chip Health: A healthy machine will tune better than an unhealthy machine.
* Machine Model: Different models may have varying tuning durations.
* Estimated Time: Tuning happens while the machine hashes without any hashrate loss. As soon as the AutoTuner is enabled your miner will be optimized, achieving the ideal hashrate and power consumption within \~1 hour.

## Managing Power Targets [#managing-power-targets]

On supported models, if you decide you want to run at a different wattage, you can update the power target at any time. Send a new target from Commander, the web UI, or the API, and the miner will smoothly ramp from its current draw to the new value — no restart or profile reset required. You can adjust the target as often as you like; each new value replaces the last one.

## Managing Tuned Profiles [#managing-tuned-profiles]

If a tuned profile does not perform as expected, you can revert it to its original settings. To restore the profile, click the restore button next to the profile name under preset profiles to reset the voltage and frequency to their original values. You can also reset all profiles to their original state by using the 3 dot menu on the same page.

![Tuned Profile Restore](/images/restoreprofile.png)

## Common Issues & Troubleshooting [#common-issues--troubleshooting]

* AutoTuner does not work on custom profiles. When you create a custom profile, you explicitly state what voltage and frequency combo you want, so AutoTuner will not adjust it.
* If the machine moves, or average temperatures change significantly, you may want to restore and retune your profiles to allow AutoTuner to readjust. Miners using power targeting will adjust automatically.
* Power targeting and profile-based tuning cannot run simultaneously. If your miner supports power targeting, the AutoTuner will use it automatically when enabled. Manual frequency and voltage commands are not available while power targeting is active.
