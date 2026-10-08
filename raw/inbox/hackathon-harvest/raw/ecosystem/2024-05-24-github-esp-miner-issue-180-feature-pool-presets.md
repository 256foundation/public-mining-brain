# bitaxeorg/ESP-Miner issue #180: [Feature] Pool presets

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/180
> Collected: 2026-10-07
> Published: 2024-05-24

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 180
- State: closed
- Author: he4dhuNTeR
- Opened: 2024-05-24
- Closed: 2025-09-27
- Labels: wontfix

## Description

Hi. 

An option for maybe three pool presets would be nice and the choice to set which one is active after restarting the Bitaxe. So you don't need to type or copy the whole pool settings again and again for switching. 

Maybe there are some more guys here using different pools or coins to mine and switching from time to time. 

Thanks a lot and for all of your time and work with this project.

## Comments

### dustinb on 2025-01-09

I was looking into this to see if it's something that could be done (mostly) in the UI. Started with the ability to swap primary and fallback using the existing API.   The blocker I ran into is the stratum password is not exposed in the system API.  How important is this?  Isn't stratum clear text anyway?  I've never used a stratum password so not sure the use case for it and how sensitive it is.

### dustinb on 2025-01-29

I made a command line "pool manager" for the Bitaxe.  It has a network scanner to get the current settings for any Bitaxe on the network.  Once you have added your pools you can update 1 or all Bitaxe in a single command.  I didn't bother with pool password, have never used that for a pool.

https://github.com/dustinb/axe-pool

### WantClue on 2025-04-16

@dustinb would be nice to have a store function in axeos that would allow to add pools to presets and maybe even share this with others on swarm ?
