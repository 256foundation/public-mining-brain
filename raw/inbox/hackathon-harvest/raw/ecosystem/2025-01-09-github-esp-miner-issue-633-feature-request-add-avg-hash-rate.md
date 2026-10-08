# bitaxeorg/ESP-Miner issue #633: [FEATURE REQUEST] Add "avg hash rate" and "avg Efficiency"

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/633
> Collected: 2026-10-07
> Published: 2025-01-09

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 633
- State: closed
- Author: ovik88
- Opened: 2025-01-09
- Closed: 2025-02-16
- Labels: none

## Description

Hey, would it be possible to add Avg values for hash rate and efficiency?
<img width="308" alt="image" src="https://github.com/user-attachments/assets/d778feec-6530-4e76-8ed7-a5b0e4df8138" />


## Comments

### skot on 2025-01-09

We could do this now with just a running average over the current session (ie how long the browser window has been open)

There are future plans to store some historical performance data onboard, which would make this much more useful.

### mrv777 on 2025-01-10

If we add avg hash to the card, I'm wondering if it should be removed from the chart to clean the chart up.  Maybe people like seeing the history of the avg hash there, but not sure if its needed

### skot on 2025-01-11

> If we add avg hash to the card, I'm wondering if it should be removed from the chart to clean the chart up. Maybe people like seeing the history of the avg hash there, but not sure if its needed

I think that makes sense.. I find myself wanting to know the average hashrate, and sometimes it's tough to read off the chart.
