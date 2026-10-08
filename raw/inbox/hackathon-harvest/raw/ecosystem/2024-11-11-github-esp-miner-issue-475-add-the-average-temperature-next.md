# bitaxeorg/ESP-Miner issue #475: Add the average temperature next to the current temperature for the Gamma

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/475
> Collected: 2026-10-07
> Published: 2024-11-11

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 475
- State: closed
- Author: uKnowMister
- Opened: 2024-11-11
- Closed: 2024-11-16
- Labels: enhancement, good first issue

## Description

Because the temperature fluctuates so drastically with the Gamma, reading the actual temperature is difficult. It's almost impossible to tell whether the improved cooling is making a difference or if it’s ineffective. 

Wouldn't it be beneficial to have a second reading showing the average temperature of the last 2-3 minutes next to the current temperature?

The exact time frame would need to be tested and evaluated, but it would make life easier for many users.

## Comments

### MyOwn2C on 2024-11-11

I think temp should be a moving average instead of instantaneous due to the huge variations. 
I often get overheat warnings from my undercoated and underclocked Gamma, but by touch it is running even cooler than OC Supra with same 52pi cooler. 
I have zero confidence about the accuracy of temperature reading from the Gamma. 

### skot on 2024-11-12

We're trying to figure out the reason for the incorrect temp readings on some chips. I don't think we should average clearly bad readings.

### uKnowMister on 2024-11-16

closed because almost resolved
