# bitaxeorg/ESP-Miner issue #272: Create a general status task

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/272
> Collected: 2026-10-07
> Published: 2024-08-07

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 272
- State: open
- Author: skot
- Opened: 2024-08-07
- Closed: n/a
- Labels: enhancement, help wanted

## Description

I'd like to create a general mining status indicator for esp-miner. Currently it's too hard to tell if your Bitaxe is actively mining and working properly. This would probably be a separate rtos task that would always show the current status on the Bitaxe display and on the AxeOS dashboard. Maybe this takes the form of the watchdog task?

things to monitor:
- have we received a nonce from the ASIC in the expected interval?
- have we received work from the pool?
- is the network socket still open?
- is wifi connected?
- has the bitaxe overheated?
- what else?

## Comments

### WantClue on 2024-08-07

something like this status: O.K. or status: mining that is been used by the standard bitmain firmware I assume. 

Sure doable. 

I think for a general status O.K. to pass we need all the above to be true execpt for the overheat_mode.


change:

- have we received work from the pool ? --> when was the last time we have received work < threshold



### skot on 2024-08-07

maybe even a little ✅ or ❌ icon for the display in the corner

### WantClue on 2024-08-07

Or we bring back the status LED like on a control board
