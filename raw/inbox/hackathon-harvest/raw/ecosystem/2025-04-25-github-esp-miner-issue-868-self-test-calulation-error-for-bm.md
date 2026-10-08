# bitaxeorg/ESP-Miner issue #868: Self test calulation error for BM1368

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/868
> Collected: 2026-10-07
> Published: 2025-04-25

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 868
- State: closed
- Author: adammwest
- Opened: 2025-04-25
- Closed: 2025-05-28
- Labels: none

## Description


**issue**
The bm1368 has 16 midstates here
in the code its 8
```c
 case DEVICE_SUPRA:
            expected_hashrate_mhs *= BM1368_CORE_COUNT * 8; // should be 16
            // lower target due to temp sensitivity
            hashrate_test_percentage_target = 0.8; 
            break;
````
[here](https://github.com/bitaxeorg/ESP-Miner/blob/master/main/self_test/self_test.c#L500)


**solution**
no magic numbers
have midstate constants in asic.c
or an expected hashrate function in asic.c

thanks @mutatrum  for spotting this one

## Comments

### skot on 2025-04-25

> 
> **issue**
> The bm1368 has 16 midstates here
> in the code its 8
> ```c
>  case DEVICE_SUPRA:
>             expected_hashrate_mhs *= BM1368_CORE_COUNT * 8; // should be 16
>             // lower target due to temp sensitivity
>             hashrate_test_percentage_target = 0.8; 
>             break;
> ````
> [here](https://github.com/bitaxeorg/ESP-Miner/blob/master/main/self_test/self_test.c#L500)
> 
> 
> **solution**
> no magic numbers
> have midstate constants in asic.c
> or an expected hashrate function in asic.c
> 
> thanks @mutatrum  for spotting this one

+1 on abstracting these things to asic.c ... we won't be Bitmain only for much longer.

### mutatrum on 2025-05-28

This was fixed in #857
