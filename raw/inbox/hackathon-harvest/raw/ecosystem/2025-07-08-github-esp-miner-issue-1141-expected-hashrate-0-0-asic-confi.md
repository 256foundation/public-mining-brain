# bitaxeorg/ESP-Miner issue #1141: Expected Hashrate 0.0, ASIC Configuration 0 total cores

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1141
> Collected: 2026-10-07
> Published: 2025-07-08

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1141
- State: closed
- Author: vlacho2103
- Opened: 2025-07-08
- Closed: 2025-08-29
- Labels: none

## Description

I hope this is the right place to ask. I am talking about the bitaxe hashrate benchmark tool.
First of all thanks for this great tool!

When I run it on my Bitaxe Gamma 601, FW 2.9.0 it shows ASIC Configuration 0 total cores.

As a result Expected Hashrate is always 0.0 and it never adjusts the voltage. 

Any ideas?

## Comments

### coinonaut on 2025-07-14

same here with 2.9.0. expected hashrate values are missing in axeOS dashboard after the update. in consequence of this benchmark scripts using the expected hashrate value are more or less out of function at this stage. i can't find this change in the changelog, so this seems to be buggy in 2.9.0...

### vlacho2103 on 2025-07-14

Here is the solution brother:

https://github.com/WhiteyCookie/Bitaxe-Hashrate-Benchmark/issues/2#issuecomment-3053886690
