# bitaxeorg/ESP-Miner issue #1937: Bug: v2.15.1 - HW Error (%) is not available as a separate chart item and is incorrectly grouped with Fan Speed (%)

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1937
> Collected: 2026-10-07
> Published: 2026-08-31

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1937
- State: open
- Author: CrisisNeverEnds
- Opened: 2026-08-31
- Closed: n/a
- Labels: none

## Description

**Describe the bug**

In AxeOS v2.15.1, the HW Error Rate (%) is not available as a separate selectable chart item.
Fan Speed (%) is already available as a separate item, but HW Error (%) is only available as part of the combined Percentage (%) chart.
This causes the HW Error Rate to share the same Y-axis scaling with the fan speed.
This makes the HW Error Rate almost impossible to monitor when the actual error rate is low.

For example, on my Bitaxe Gamma 601:
•	HW Error Rate: around 0.14%
•	Fan Speed: around 40%
•	Chart Y-axis: 0–100%

As a result, the HW Error Rate curve is compressed almost completely against the bottom of the chart.

**To Reproduce**

Steps to reproduce the behavior:
1.	Run a Bitaxe with ESP-Miner/AxeOS v2.15.1 Unified.
2.	Open the AxeOS live dashboard.
3.	Open the chart/metric selection.
4.	Notice that Fan Speed (%) is available as an individual selectable item.
5.	Notice that there is no individual HW Error (%) item.
6.	The only way to display HW Error Rate is by selecting Percentage (%).
7.	Percentage (%) includes both Fan Speed (%) and HW Error (%).
8.	Run the miner with a typical fan speed, for example around 40%.
9.	Observe a low HW Error Rate, for example around 0.14%.
10.	The chart uses a 0–100% Y-axis because Fan Speed (%) is included in the same chart.
11.	Click Fan Speed in the chart legend to hide the fan speed dataset.
12.	The Fan Speed curve disappears, but the Y-axis remains scaled to 0–100%.

**Expected behavior**

HW Error (%) should be available as an individual selectable chart item, just like Fan Speed (%).

For example, the selectable items should include:
•	Fan Speed (%)
•	HW Error (%)

When HW Error (%) is selected on its own, the chart should dynamically scale its Y-axis according to the actual HW error rate.
For example, if the HW Error Rate is around 0.14%, the chart should use a useful scale appropriate to the actual error rate instead of 0–100%.
In AxeOS v2.14.2, the HW Error Rate visualization dynamically adapted to the actual error values, making small changes clearly visible.

**Screenshots & Photos**

This screenshot shows the behavior in AxeOS v2.15.1.

<img width="1635" height="478" alt="Image" src="https://github.com/user-attachments/assets/ff2e2254-0a50-4a4b-b3f5-6424509e9f63" />

The v2.15.1 screenshot shows:
•	Fan Speed around 40%, but hidden
•	HW Error Rate around 0.14%
•	Y-axis scaled from 0–100%
•	HW Error Rate therefore almost invisible

Hardware:
•	Bitaxe HW version: Gamma 601
•	Bitaxe HW vendor: Minertrend
•	ESP-Miner FW version: 2.15.1
•	Hash Frequency: 750 Mhz
•	Voltage: 1230 mV

## Comments

### bonifacio123 on 2026-09-02

I was wondering what happened to this metric. I tried looking quickly and just thought it was removed. Hope it get adjusted as you say.
