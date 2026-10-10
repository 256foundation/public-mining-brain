# bitaxeorg/ESP-Miner issue #1289: Add frequency to statistics

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1289
> Collected: 2026-10-07
> Published: 2025-10-22

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1289
- State: closed
- Author: jns-codeworks
- Opened: 2025-10-22
- Closed: 2025-11-29
- Labels: design

## Description

Add frequency to the statistics endpoint response.
App developers could use the value to visualize its effect on other values such as asic temp / voltage regulator temp over time. 

## Comments

### KillerInk on 2025-11-02

its added in https://github.com/bitaxeorg/ESP-Miner/pull/1152

### WantClue on 2025-11-29

frequencies + voltages are available on the /asic endpoint

### jns-codeworks on 2025-12-06

I think you are referencing the frequency / voltage OPTIONS from api/system/asic. 
But I'm looking for the current asic frequency value, which is stored as statistic, such as hashrate, asic temperature, etc.
