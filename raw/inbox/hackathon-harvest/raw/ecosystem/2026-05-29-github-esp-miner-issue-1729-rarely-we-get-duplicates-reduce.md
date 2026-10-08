# bitaxeorg/ESP-Miner issue #1729: Rarely we get duplicates, reduce nonce percent for all chips to 95%

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1729
> Collected: 2026-10-07
> Published: 2026-05-29

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1729
- State: open
- Author: adammwest
- Opened: 2026-05-29
- Closed: n/a
- Labels: none

## Description

There have been some reports of duplicates (<1%) some of them are due to #420 
In it I set nonce_percent 100%. I think the cause of the duplicates is some chips have PLL variations which means the calculation is slightly too big.

The nonce search size is modified by frequency so if its a tiny bit wrong we can get Internal duplicates, this only applies to HCN chips Bm62/66/68/70
I discussed internal duplicates here https://github.com/shufps/ESP-Miner-NerdQAxePlus/pull/546#discussion_r3058959737

The nonce percent should be reduced to 95% for version rolling asics
https://github.com/bitaxeorg/ESP-Miner/blob/master/components/asic/bm1366.c#L271
https://github.com/bitaxeorg/ESP-Miner/blob/master/components/asic/bm1368.c#L233
https://github.com/bitaxeorg/ESP-Miner/blob/master/components/asic/bm1370.c#L291

I think @mutatrum  also found small dups on a max these are normal duplicates timeout > wraparound time
for BM1397 which does not have this setting, the timeout percent should be reduced to 95%
https://github.com/bitaxeorg/ESP-Miner/blob/master/components/asic/asic.c#L160

## Comments

### mutatrum on 2026-05-29

We're not going through 100%, it's capped at 500ms / number of cores. If we set the timeout to cover the total search space, then I think you would have a tiny change of duplicates, but I currently have not seen duplicates on the 66/68/70 devices.

As for the Max, the job timeout is only 4.2ms (I think, something tiny), so any fluctuation there in the OS can overshoot it because the ESP is busy with something else, but I think that's not what you mean.

### adammwest on 2026-06-01

>we're not going through 100%, it's capped at 500ms / number of cores. If we set the timeout to cover the total search space, > then I think you would have a tiny change of duplicates, but I currently have not seen duplicates on the 66/68/70 devices.
Internal duplicates come regardless of the timeout used, its because reg 0x10 is too big.

> As for the Max, the job timeout is only 4.2ms (I think, something tiny), so any fluctuation there in the OS can overshoot it 
> because the ESP is busy with something else, but I think that's not what you mean.

I changed the max its default is 20ms, but I use the timeout eqn with 100% time, so its 2^24/freq, for 400Mhz its 42ms

So my proposal is to remedy both these 2 issues
Reduce nonce range for version rolling chips to 95%. and reduce the max timeout percent to 95%




Gitgab posted logs with a bitaxe gamma 601, i was refrenceing that
we are at ~100% nonce and version range approx 300s fullscan time, ao wrap around duplicates can never arrive because we are 500ms timeout.


`34 duplicate-share (0.36 %)`
```
[0;32mI (106213037) asic_result: ID: 21391, ASIC nr: 0, Core: 70/6, ver: 2008C000 Nonce 55B6408D diff 17513.9 of 1601.[0m
[0;32mI (106213108) asic_result: ID: 21391, ASIC nr: 0, Core: 70/6, ver: 2008C000 Nonce 55B6408D diff 17513.9 of 1601.[0m
[0;33mW (106213159) stratum_v2_task: Share rejected: duplicate-share[0m
```

106213108-106213037 = 71ms

another example
```
[0;32mI (5271125) asic_result: ID: 1063, ASIC nr: 0, Core: 75/6, ver: 200AC000 Nonce 497BD597 diff 15394.5 of 970.[0m
[0;32mI (5271141) asic_result: ID: 1063, ASIC nr: 0, Core: 75/6, ver: 200AC000 Nonce 497BD597 diff 15394.5 of 970.[0m
[0;32mI (5271189) stratum_v2_task: Shares accepted: 10 (49.6 ms)[0m
[0;33mW (5271353) stratum_v2_task: Share rejected: duplicate-share[0m
```
5271141-5271125 = 16ms

this is an internal duplicate as duplicate time is `ms`  not `s`, not a wrap around duplicate. I explain below

> update: the duplicates come in bursts, not evenly distributed. Just jumped from 1.87% to 1.93% after a cluster. > Still climbing slowly. Maybe the overlap only triggers under certain timing conditions, not on every nonce wrap.

Thats expected for a HCN that is too big, these are 2 distinct types of duplicates wrap around when the space ends and restarts and (i call them internal dups) maybe overlapping range duplicates is a better name

but essentially the chip encodes info (core,chip) in some part of the nonce range, the HCN can overwrite this
what you end up with is a portion of the nonce range is overlapping, so you get solutions that appear very close together in time.

imagine a fictious scenario of a chip with 2 cores and a total nonce range of 256 
with 128 spacing and we set 130 for the size per core.

| Core   | Start | End  | Range       |
|--------|-------|------|-------------|
| Core 0 | 0     | 130  | 0 -> 130     |
| Core 1 | 128   | 256  | 128 -> 256   |

we cover 100% of the range but both cores are assinged the overlapping range 128->130 so we end up with some dups, that come back at the same time approximately.
