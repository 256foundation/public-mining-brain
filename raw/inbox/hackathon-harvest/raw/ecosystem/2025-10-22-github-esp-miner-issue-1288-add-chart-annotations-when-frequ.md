# bitaxeorg/ESP-Miner issue #1288: Add chart annotations when frequency or voltage changed

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1288
> Collected: 2026-10-07
> Published: 2025-10-22

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1288
- State: open
- Author: mutatrum
- Opened: 2025-10-22
- Closed: n/a
- Labels: design

## Description

With hashrate registers, you get a really visible change in hashrate when you change the frequency. In this graph, I changed the frequency from 625 to 600:

<img width="1913" height="973" alt="Image" src="https://github.com/user-attachments/assets/ecf5430c-d510-4861-b2f3-98a2679b8b5c" />

It would be nice to have this event annotated in the graph, which should be possible by using something like https://www.chartjs.org/chartjs-plugin-annotation/latest/
