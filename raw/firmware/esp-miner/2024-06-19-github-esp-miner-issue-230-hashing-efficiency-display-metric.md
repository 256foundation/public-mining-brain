# bitaxeorg/ESP-Miner issue #230: Hashing Efficiency Display Metric

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/230
> Collected: 2026-10-07
> Published: 2024-06-19

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 230
- State: closed
- Author: dadofsambonzuki
- Opened: 2024-06-19
- Closed: 2024-06-19
- Labels: none

## Description

**Describe the bug**

The units used to hashing efficiency on AxeOS are W/Th, which is dimensionally confusing - `J/s/TH`.

Often TH is used as shorthand to actually mean TH/s and in this case W/Th actually equals `W/Th/s = J/s/Th/s = J/Th`.

Here is a [Twitter Discussion](https://x.com/skot9000/status/1803277729636257816) on the topic with some Physicists.

**To Reproduce**
Steps to reproduce the behavior:
1. Go to the dashboard page
2. Scroll down to Efficiency section
3. Observe unit of efficiency metric and smell brain melting

![image](https://github.com/skot/ESP-Miner/assets/87125117/628996a1-6e88-4ec1-a9c3-ace223c5ffe0)


**Expected behavior**

Either use:

1. `W/Th/s`
2. `J/Th`

2 would be my recommendation as much simpler. Maybe a tool tip with the W/Th/s.
