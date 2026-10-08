# bitaxeorg/ESP-Miner issue #1902: AxeOS reports normal BM1372/BM1373 frequency as low

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1902
> Collected: 2026-10-07
> Published: 2026-08-21

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1902
- State: closed
- Author: skot
- Opened: 2026-08-21
- Closed: 2026-09-18
- Labels: none

## Description

**Describe the bug**

AxeOS shows the warning banner:

> Device frequency is set low - See settings

on a Naja Duo 1201 running at its normal BM1372/BM1373 frequency of 327 MHz. The ASIC frequency is configured correctly and the miner operates normally.

The warning condition is currently hard-coded as `frequency < 400` in both:

- `main/http_server/axe-os/src/app/components/home/home.component.ts`
- `main/http_server/axe-os/src/app/components/swarm/swarm.component.ts`

BM1372/BM1373 uses a default frequency of 327 MHz and currently exposes these supported options: 327, 350, 375, 380, 400, and 410 MHz.

**To reproduce**

1. Run the Naja Duo 1201 firmware from the current Naja PR series.
2. Leave the BM1372/BM1373 frequency at the factory default of 327 MHz.
3. Open the AxeOS dashboard.
4. Observe the low-frequency warning even though the configured frequency is valid and mining is operating normally.

**Expected behavior**

AxeOS should not display a low-frequency warning when the configured frequency is within the supported range for the active ASIC.

**Suggested fix**

Replace the global 400 MHz threshold with an ASIC-aware threshold. AxeOS already obtains the device-specific settings from `/api/system/asic`, including `frequencyOptions` and `defaultFrequency`.

A robust condition would preserve the warning for a missing or zero frequency, but compare nonzero frequencies against the minimum supported value for the active device, for example:

```ts
const minimumFrequency = Math.min(...asicSettings.frequencyOptions);
const frequencyIsLow = !info.frequency || info.frequency < minimumFrequency;
```

Apply the same logic to both the main dashboard and swarm view so their warning behavior remains consistent. If ASIC settings are unavailable, AxeOS can retain a conservative fallback.

**Hardware**

- Device: Naja Duo
- Board version: 1201
- ASIC: 2x BM1372/BM1373
- Tested frequency: 327 MHz
- Voltage: 1000 mV
- Tested firmware: integrated Naja branch at `3d84e44`

Related implementation work: #1890 and #1892.

## Comments

### vortexopenclaw on 2026-09-10

Thanks for the clear report, @skot. We have now confirmed the fix on a physical Naja Duo at 327 MHz: the false low-frequency warning no longer appears.

I opened draft PR #1961. It derives the threshold from each device frequencyOptions in both Home and Swarm, preserves warnings for invalid or zero frequency values, and avoids guessing a device threshold when compatible preset metadata is unavailable. The focused 38-test suite and production AxeOS build pass. The below-327 MHz warning path is covered in tests but was not reproduced on the physical Naja.

### mutatrum on 2026-09-10

When is it actually too low? As with #1961 it gives a warning directly below the lowest default setting. Maybe it needs some leeway for underclocking before a warning shows?

### vortexopenclaw on 2026-09-10

> When is it actually too low? As with [#1961](https://github.com/bitaxeorg/ESP-Miner/pull/1961) it gives a warning directly below the lowest default setting. Maybe it needs some leeway for underclocking before a warning shows?

It currently alerts as too low when the Naja Duo is set to its default freq. of 327 MHz.

<img width="420" alt="Naja Duo showing the incorrect low-frequency warning at 327 MHz" src="https://github.com/user-attachments/assets/d84c2cb0-11e5-4c84-8f33-c6edbe2e9a58" />

With the draft PR [#1961](https://github.com/bitaxeorg/ESP-Miner/pull/1961), it no longer does that.

<img width="420" alt="Naja Duo running at 327 MHz without the low-frequency warning" src="https://github.com/user-attachments/assets/75f23d85-7e0e-4c12-9f2f-abed3dbe9579" />

Thanks to @SuperG7one3 for helping validate this one.
