# bitaxeorg/ESP-Miner issue #369: Lower the default hash frequency and core voltage for Gamma

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/369
> Collected: 2026-10-07
> Published: 2024-09-30

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 369
- State: closed
- Author: skot
- Opened: 2024-09-30
- Closed: 2024-10-10
- Labels: bug, enhancement, help wanted

## Description

The stock heatsink and fan on the Gamma cannot reliably handle more than 525MHz @ 1100mV.

We should change the firmware defaults.

## Comments

### jrkalf on 2024-10-01

@skot I partially agree with you on that one. With the stock yellow cooling brick & springloaded clamps you won't get it more stable than that at regular room temperatures. 
I would suggest that it can handle 595MHz @ 1150mV, but only under the condition that the springloaded clamps are replaced by M3*8 bolts and nuts. 

The springloaded clamps in combination with the thermal paste is not performing well. There's multiple articles out on the web now, I've seen this first hand on my gamma.



### benjamin-wilson on 2024-10-06

525@1150 seems to be the minimum voltage to be stable 

### skot on 2024-10-08

okay, lets go with 525MHz/1150mV as the default. This needs to be adjusted in the cvs file as well as the AxeOS settings drop downs.
