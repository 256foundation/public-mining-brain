# bitaxeorg/ESP-Miner issue #680: "-1 oC" asic temperature value

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/680
> Collected: 2026-10-07
> Published: 2025-01-30

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 680
- State: closed
- Author: alltheseas
- Opened: 2025-01-30
- Closed: 2025-02-12
- Labels: none

## Description

This is displayed while I am troubleshooting the unhappy path of overheat mode. 

I am guessing this is an incorrect measurement (I am not in the North Pole, or the Canadian tundra), or some failsafe. 

Consider displaying the actual temperature value, or a high temperature/overheat warning instead. 

![Image](https://github.com/user-attachments/assets/26d271e4-4bd7-4bb0-997a-2e5f217ad906)

## Comments

### MyOwn2C on 2025-01-30

-1C is what it will show before it’s initialized 

### alltheseas on 2025-01-30

> -1C is what it will show before it’s initialized

does "initialized" mean "starting to hash"?

### MyOwn2C on 2025-01-30

> > -1C is what it will show before it’s initialized
> 
> does "initialized" mean "starting to hash"?

From power up. 
After a few seconds it will read normal temperature. 

### skot on 2025-02-02

I agree showing a real (albeit cold AF) temperature is confusing. Maybe we can show "--" instead.
