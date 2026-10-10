# bitaxeorg/ESP-Miner issue #100: Have to press the restart button in AxeOS to start hashing

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/100
> Collected: 2026-10-07
> Published: 2024-01-30

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 100
- State: closed
- Author: thermosats
- Opened: 2024-01-30
- Closed: 2024-05-24
- Labels: bug

## Description

When I plug in the power cable to start the bitaxe, the power consumption stays low and the hashing doesn't start. I have to press the restart button in AxeOS every time.

https://github.com/skot/ESP-Miner/assets/152765961/b3f4b3f3-2bd2-43cc-9c45-5a4a99edb32c



## Comments

### monster4866 on 2024-01-30

try to flash a new firmware,

first download
https://github.com/skot/ESP-Miner/releases

then u can flash it here:
https://espressif.github.io/esptool-js/

### laststrawman on 2024-02-05

I flashed my bitaxe using the above flash tool and now it is not working. I have always had success from the command line bitaxetool etc ... I guess I have to go back to that.

### skot on 2024-02-16

I have seen the case where the bitaxe doesn't hash very well on startup and requires a restart. but never _every_ time.
It's a tough one to debug because it happens so infrequently for me.

@thermosats is this still happening _every_ time for you?
