# bitaxeorg/ESP-Miner issue #403: add ASIC init OLED screen

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/403
> Collected: 2026-10-07
> Published: 2024-10-10

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 403
- State: closed
- Author: skot
- Opened: 2024-10-10
- Closed: 2025-11-29
- Labels: enhancement

## Description

We have the special screen for connecting to the WiFi at boot, it would be nice to have a special screen for the ASIC init sequence since it takes a little while.

It could look like:

```
1x BM1370
525 MHz, 1150mV

Initializing...
```

And if there are any errors with the ASIC init, we could show them on this screen

## Comments

### skot on 2024-10-10

might be cool to show the frequency ramp up on this screen?

### WantClue on 2024-10-17

Aight I'll work on a loading screen 

### WantClue on 2025-11-29

The Bitaxe Logo is taking the same amount of time the asic is initializing, if we wan't to change this in the future we might need to reopen this issue
