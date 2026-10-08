# bitaxeorg/ESP-Miner issue #2017: [Feature request] Allow wifi reconnect after router is turned off overnight

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/2017
> Collected: 2026-10-07
> Published: 2026-10-05

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 2017
- State: open
- Author: marcofiocco
- Opened: 2026-10-05
- Closed: n/a
- Labels: none

## Description

I turn off wifi overnight to reduce EMF exposure.
Unfortunately the BitAxe 601 stops retrying to connect after a while and the only way to make it reconnect is to unplug/replug the power cable every morning.
It would be nice that the OS has an option to retry indefinitely or after a set number of hours.

## Comments

### 1837Wine on 2026-10-05

Turning one's Wi-Fi off at night also reduces the chance of finding a block while your asleep if your solo mining ! 

### filteredreality on 2026-10-06

Cable is a better option for you.

### marcofiocco on 2026-10-06

> Cable is a better option for you.

Yes, but the BitAxe 601 does not have an ethernet port.

### 1837Wine on 2026-10-06

Even if cable is used and you turn off the Wi-Fi router (flip the switch / disconnect it from the wall socket) it leaves the miner in the same state at night doing nothing as it can not talk to the outside world, you've put it in no mans land. 


### filteredreality on 2026-10-07

he could just schedule ssid broadcast time. lan can still be up.

oh, it didn't pass early access.
https://github.com/bitaxeorg/ESP-Miner/pull/1437
https://github.com/bitaxeorg/ESP-Miner/releases/tag/early-access-2026-03
