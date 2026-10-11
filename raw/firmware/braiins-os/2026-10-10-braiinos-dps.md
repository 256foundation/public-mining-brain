# Dynamic Performance Scaling (DPS) — Braiins OS (Braiins Academy)

> Registry ID: braiins-os
> Source: https://academy.braiins.com/braiins-os/dps (markdown captured via /braiins-os/dps.md llms route)
> Collected: 2026-10-10
> Published: n/d (docs site build 2026-10-02, sitemap lastmod 2026-10-04)
> Posture: verbatim
> As-Of: 2026-10-10

# Dynamic Performance Scaling

## Introduction

Dynamic Performance Scaling (DPS) is designed to keep your miner operational & efficient when overheating. This feature is ideal for clients who prioritize consistent uptime & safe mining.
DPS dynamically adjusts power and hash-rate targets based on real-time conditions, helping miners maintain the ideal balance between performance and stability.

#### Why Is DPS Important?

- **Stable Operation:** Prevents overheating and shutdowns during temperature spikes
- **Maximum Uptime:** Keeps miners running smoothly in fluctuating conditions while keeping the best efficiency possible
- **Hardware Protection:** Reduces hardware stress by scaling performance based on conditions

#### Who Should Use DPS?

DPS is ideal for miners in environments with frequent temperature changes, or for those managing large-scale operations where automated performance scaling is critical.

## Feature Overview

Dynamic Performance Scaling (DPS) helps your miner dynamically adjust performance based on environmental conditions, maximizing both uptime and efficiency. Before configuring DPS settings, **Autotuning must be enabled**. This core feature of Braiins OS optimizes your miner's performance, and we highly recommend keeping it active—disabling it will likely not yield better results.

DPS has several configurable layers and steps designed to suit different operating environments. While we provide a default setup that works well for most users, there are always exceptions based on specific needs. Let's take a closer look at how DPS works and the options available.

In simple terms, DPS adjusts your miner's power or hash-rate targets depending on environmental factors. For example, if the temperature rises during the day, your miner will downscale to reduce heat and allow fans to cool it effectively. When the temperature drops, the miner will upscale back to higher performance targets.

## How DPS Works

When DPS is **enabled**, it is activated in the background all the time waiting for conditions to be met to upscale or downscale. Upscale means going up with the power or hash-rate target by one step. Downscale means going down with the power or hash-rate target by one step.

| **Behaviour**     | **25.11 and Older**                                                | **26.01 and Newer**                                                     |
| ----------------- | ------------------------------------------------------------------ | ----------------------------------------------------------------------- |
| New installations | DPS is OFF by default                                              | DPS is ON by default                                                    |
| Upgraded machines | DPS is OFF by default                                              | DPS settings are migrated from previous versions, On Start Target = 66% |
| On Start Target   | When first enabled, DPS starts tuning on 66% from set Power Target | Newly installed machines start tuning on 100% of set Power Target       |

In 26.01 and newer releases, DPS is on by default but will not be engaged if the miner is not overheated. On Start Target defines the % of Power Target at which DPS will start tuning.
If the chip temperature reaches Hot temperature in the first 5 minutes of miner operations, it will downscale to 66% of the default Power Target to prevent overheating.
If the Hot temperature is reached after the 5 minute interval, DPS will downscale by one step.

All profiles that are tuned by DPS are saved and do not need retuning, unless they were removed. The DPS can cruise from its target to the minimal power target that you can set in settings.

This way miners can tune approximately 6 - 15 targets, depending on what step size you are using. Those targets can be set and quickly ramped up even if you disable the DPS.

## Scaling Conditions

To fully grasp Dynamic Performance Scaling (DPS), it's crucial to understand how it was designed and the rules that govern its operation. Please have a look at them below.

### Downscaling Conditions

Downscaling conditions are simpler and designed to respond quickly to prevent overheating. When the miner hits the **HOT temperature**, it needs to reduce its power or hash-rate to avoid potential damage or shutdown.

| **Condition**        | **All versions**                                                                         |
| -------------------- | ---------------------------------------------------------------------------------------- |
| Temperature Trigger  | Chip temperature is greater than or equal to the HOT temperature                         |
| Downscale Timeout    | It has been at least 3 minutes since the last downscaling                                |
| Upscale Timeout      | It has been at least 30 seconds since the last upscaling                                 |
| Minimal Target Check | The miner will not downscale below the minimal power or hash-rate target set by the user |

### Upscaling Conditions

Upscaling is a moment where a miner meets all conditions for stepping up to the next **Target Step**. There are several of them, have a look below in the table.

| **Condition**         | **24.12 and Older**                                                      | **25.01 and Newer (Normal mode)**                                        | **25.01 and Newer (Boost mode)**                                         |
| --------------------- | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| Temperature Threshold | Chip temperature is at least 5°C below the HOT temperature               | Chip temperature is less than or equal to the TARGET temperature         | Chip temperature is at least 8°C below the HOT temperature               |
| Cooldown Time         | Last upscale was less than 3 minutes ago                                 | Last upscale was less than 3 minutes ago                                 | Last upscale was less than 3 minutes ago                                 |
| Stable Temperature    | Chip temperature did not fluctuate by more than 1°C in the last minute   | Chip temperature did not fluctuate by more than 1°C in the last minute   | Chip temperature did not fluctuate by more than 1°C in the last minute   |
| Overheating Timeout   | It has been at least 1 hour since the miner reached HOT temperature      | It has been at least 1 hour since the miner reached HOT temperature      | It has been at least 1 hour since the miner reached HOT temperature      |
| Fan Speed             | The fan speed is below 100%                                              | n/a                                                                      | n/a                                                                      |
| DPS Memory            | The target step is not preserved in the DPS Memory (since 24.09 version) | The target step is not preserved in the DPS Memory (since 24.09 version) | The target step is not preserved in the DPS Memory (since 24.09 version) |

## Additional Behavior

### Grid Alignment: Keeping Targets Clean and Consistent

The **Grid Alignment** feature ensures your miner scales power logically by snapping target values to predefined grid steps. This prevents irregular or awkward power targets that can arise during operation.

**Let's walk through an example:**
Suppose your miner has a power target of 3500W, and the power adjustment steps are set to 300W. Normally, the scaling sequence would look like this: 3200W, 2900W, 2600W, 2300W, and so on. However, when Braiins OS restarts with an On Start Target of 66%, the miner initializes at 66% of the set target. In this case, 66% of 3500W equals **2310W**.

Since **2310W** does not align with the grid, Grid Alignment snaps the value to the closest grid step, which is **2300W**. This keeps your power targets in a clean, organized sequence, avoiding scattered or unpredictable values. Keeping the value at 2310 would create another sequence of targets that would need to be tuned when upscaling or downscaling, slowing down the operation and lowering the hash-rate.

![Grid Alignment Visual](/static/image/DPS_grid_snap.82b0df5e41.png)
The grid automatically recalculates whenever you adjust the Power Target, Hash-rate Target, or Target Step Values. This feature helps maintain consistent scaling behavior, improving stability and efficiency.

### DPS Memory: Preventing Unwanted Target Cycling

"DPS Memory" is a feature designed to prevent your miner from constantly cycling between power targets due to temperature fluctuations. Let's break it down with an example:

Imagine your miner operates at 2500W but becomes too cold, while at 3000W it overheats. This can cause the miner to endlessly cycle between these two targets—scaling up and down without finding stability.

You can sometimes mitigate this issue by fine-tuning the **Target Step Values** (the increments used to adjust power). However, certain environmental conditions, like poor airflow, can lead to rapid and unpredictable temperature shifts. These fluctuations can cause a cascading "avalanche effect" where each adjustment triggers the same cycle over and over again.

This is where the **DPS Memory** feature steps in to stabilize things. Here's how it works in practice:

- **Memory Note**: If the miner scales up power and then quickly downscales within 30 minutes, DPS takes note of the conditions. It records the power or hash-rate target, as well as key metrics like temperature and fan speed.

- **Upscaling Rules**: The next time the miner attempts to scale up to that same target, it must meet one of these additional conditions to proceed:
  - The current temperature is at least 2°C lower than the temperature from the preserved memory
  - Alternatively, the fan speed is at least 20% slower than the previously recorded state
  - If neither condition is met, DPS blocks the upscaling attempt, assuming that it would only lead to another cycle

- **Memory Reset**: The DPS memory automatically clears itself after 32 hours if no triggering event occurs

By using DPS Memory, your miner avoids getting stuck in an endless loop of scaling, allowing for more stable and efficient operation even in challenging environments. The DPS memory is by default embedded in the DPS itself, so there is no need to enable or disable this behavior!

## Configuring DPS

We always try to give users several options to configure the features we provide in our firmware. Talking about the DPS - all of the configuration can be set either via the [Toolbox](https://braiins.com/toolbox), the [Public API](/braiins-os/papi-about/index.md), or the miner's GUI.

#### Enable: Dynamic Performance Scaling

This feature must be enabled to configure DPS further on. Keep in mind that after saving this setting, Braiins OS will require a restart.

You can manage this through the Toolbox in batches, in the desired way via API or individually in the GUI.


#### Select Your Mode: NORMAL & BOOST

DPS offers two modes: **NORMAL** and **BOOST**, which control the conditions for performance upscaling.

- **NORMAL Mode:** The miner upscales when it is less than or equal to the target temperature.
- **BOOST Mode:** The miner upscales more aggressively, continuing until it reaches 8°C below the HOT temperature threshold. Keep in mind that this mode can increase the stress on the hardware at the cost of more hash-rate, proceed at your own risk!

Each mode is designed to fit different performance strategies, with more details provided in the upscaling conditions section. Changing the mode also requires a Braiins OS restart. It can be set through the Toolbox, the API, or individually in the GUI.



If you are using an older firmware version (before 25.01), these modes are not available. We recommend updating to
the latest firmware version

#### Choose: Step Values

The **Step Value** determines how much the miner scales up or down when conditions are met, whether by hash-rate or power target.

- **Smaller Step Value:** The miner will make smaller, more frequent adjustments, providing finer control but requiring more tuning steps
- **Larger Step Value:** Fewer, larger adjustments will be made, but you may miss opportunities for optimal hash-rate performance

It's important to find a balance here—too large a step may cause missed optimizations, while too small a step may lead to excessive tuning. However, once the entire grid is tuned, the miner will operate efficiently without further adjustments.


#### Decide: Minimal Target

This defines the lowest point your miner can reach when downscaling. Once the miner hits this limit, it will not reduce performance further.


###### Shutdown When Minimal Power Target Is Reached

This option gives you control over what happens if the miner hits the minimal power target.

- **If enabled:** The miner will PAUSE and attempt to resume operations after a defined period
- **If disabled:** The miner will PAUSE and resume automatically when the temperature drops below the HOT threshold

This feature can be particularly useful in environments with extremely high ambient temperatures, helping to prevent overheating while maintaining safe operating conditions.

#### AT LAST: SAVE & APPLY

After configuring everything to your needs, click SAVE & APPLY on the miner. This will restart Braiins OS and apply your new settings!

## Support and contact


Have questions? Our dev and support teams are always available to help.
Join our Telegram group:

[EN group](https://t.me/BraiinsOS)[ES group](https://t.me/BraiinsOS_ES)[RU group](https://t.me/BraiinsOS_RU)[ZH group](https://t.me/BraiinsOS_ZH)

You can also [send a VIP request](https://help.braiins.com/en/support/tickets/new) to our support team.



---

Was this helpful?

Yes, thanks!Sort of, thanks!Not really

Talk to us!
