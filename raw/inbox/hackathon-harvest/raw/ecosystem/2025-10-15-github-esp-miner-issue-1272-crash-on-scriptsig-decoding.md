# bitaxeorg/ESP-Miner issue #1272: Crash on scriptsig decoding

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1272
> Collected: 2026-10-07
> Published: 2025-10-15

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1272
- State: closed
- Author: mutatrum
- Opened: 2025-10-15
- Closed: 2025-10-15
- Labels: none

## Description

The following `mining.notify` crashes esp-miner:
```
{
   "params":[
      "68e96556000035c4",
      "37148ec9f5312f63f773c0370b0bcacbd9c3aa9e00f22a240000000000000000",
      "01000000010000000000000000000000000000000000000000000000000000000000000000ffffffff2303020c0e6269746e6f64652e6363202f2f204d696e65204243482c2042757920425443ffffffff020000000000000000166a14",
      "16de6b5880fb0753b47ca212000000001976a914dea7c4b093df2051bb64ff4295afbfdd5905cfd188ac00000000",
      [
         "d494efad62614220d3d44b4c28bb23e1d71cf641b737650dc9ea73de78725501",
         "58e5d19b865dffbac6f45c4b57b3b4cca25b091e69a297f4e3d247c69270e3b9",
         "df16900135d6e72b63acff6a341fb83c118d962d41674cce4c1b7d285e5b55c3",
         "f95dea7f297563ac981636f25a58d41e3c6372ff8f0276ac5d88d1f06d4d4f9b",
         "962d8b3b77164efe23dfdc737937188646a728ffe7cbbbd2507d5da1bd9746d6",
         "55f0b578a9a2ce8355d1e15b13e74dddbcf22f2cb8e038b9efcb1c1920b045ef"
      ],
      "20000000",
      "18018d09",
      "68ef6f5a",
      true
   ],
   "id":null,
   "method":"mining.notify"
}
```
