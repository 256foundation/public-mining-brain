# bitaxeorg/ESP-Miner issue #1429: Add difficulty to graph

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1429
> Collected: 2026-10-07
> Published: 2025-12-05

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1429
- State: open
- Author: mutatrum
- Opened: 2025-12-05
- Closed: n/a
- Labels: none

## Description

Add share difficulty to the graph. 

This would need a log2 axis scale to make sense, but luckily the people from chart.js made this already: https://www.chartjs.org/docs/master/samples/advanced/derived-axis-type.html

And we somehow have to to a max per time period. So best share for every statistics sampling (5 sec), but also a max value to put into the historical data.

This ties in with #1173, where we need some interpolation to get current data into historical data. For most it would be the average, but for some (such as the share diff) it would be the max value.

## Comments

### adammwest on 2025-12-05

even better it can be meaningful rather than a linear factor
hex_zeros = log2(diff)/4+8

also potential bug 
log(0)= undefined
 0 diffs can happen in practise (HW problems/Power issues)
