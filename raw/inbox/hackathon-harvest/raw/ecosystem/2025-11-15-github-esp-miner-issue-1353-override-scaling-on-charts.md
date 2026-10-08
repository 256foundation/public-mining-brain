# bitaxeorg/ESP-Miner issue #1353: Override scaling on charts

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1353
> Collected: 2026-10-07
> Published: 2025-11-15

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1353
- State: open
- Author: mutatrum
- Opened: 2025-11-15
- Closed: n/a
- Labels: none

## Description

For some values, it makes sense to set the scaling to a minimum resolution. Current behaviour blows every scale up until the graph fills almost the complete y-axis, but in most cases that just shows noise. F.e. hashrate graph is ok to be flat if the fluctuation is 0.01 Th/s.

This can be achieved by setting `suggestedMin` and `suggestedMax` on the min and max of the current dataset, but expanding those if they are too close together. So for example for hashrate, the difference between min and max should be around 10 Gh/s, so with 10 ticks each tick will be 1 Gh/s, which is fine. Closer up makes no sense.

Rinse and repeat for all metrics.

## Comments

### DarkCanuck12 on 2026-02-21

I agee - seeing a mountain range of hashrates between 2.01 and 2.08 generally isn't meaningful. It would be great to have the option to set the vertical resolution of the graph.
