# bitaxeorg/ESP-Miner issue #310: Phase out support for bitaxeMax in future firmware updates

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/310
> Collected: 2026-10-07
> Published: 2024-08-28

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 310
- State: open
- Author: skot
- Opened: 2024-08-28
- Closed: n/a
- Labels: enhancement

## Description

we can do this with a json file in the releases that specifies the minimum HW revision required to run the update. Then AxeOS needs a change to implement this.

This is paired with the esp-miner firmware migration the bitaxeorg GitHub org

## Comments

### jddebug on 2024-08-29

Why phase out support? I have a lot of these. They have only recently become stable.

### benjamin-wilson on 2024-08-29

> Why phase out support? I have a lot of these. They have only recently become stable.

The Max was one of the earliest working bitaxes and did not have a large number of sales when compared to the Ultra and Supra. We believe it has reached a state of stability and now is a good time to sunset any more development. Support for older ASICs adds complexity, bloat and maintenance costs that burdens development of new Bitaxe versions. 

### skot on 2024-08-30

We may want to phase out new update support for some of the earlier Ultras too.. So this JSON should allow for hardware revision number based filtering

### Kubaaaaaaaaaa on 2024-11-05

> > Why phase out support? I have a lot of these. They have only recently become stable.
> 
> 
> 
> The Max was one of the earliest working bitaxes and did not have a large number of sales when compared to the Ultra and Supra. We believe it has reached a state of stability and now is a good time to sunset any more development. Support for older ASICs adds complexity, bloat and maintenance costs that burdens development of new Bitaxe versions. 

But there could be some UI enhancements in the future that even owners of old MAXs could benefits from.
