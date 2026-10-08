# bitaxeorg/ESP-Miner issue #1746: Feature: Screen Brightness

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1746
> Collected: 2026-10-07
> Published: 2026-06-01

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1746
- State: closed
- Author: WantClue
- Opened: 2026-06-01
- Closed: 2026-06-02
- Labels: none

## Description

We should add screen brightness.



## Comments

### WantClue on 2026-06-01

there is no backlight to the oled screen but we can control the contrast via 0x81 afaik

### mutatrum on 2026-06-02

Duplicate of #567

It's possible, but it's display dependent. Not all displays listen to the register, and the rate of dimming can also vary wildly.
