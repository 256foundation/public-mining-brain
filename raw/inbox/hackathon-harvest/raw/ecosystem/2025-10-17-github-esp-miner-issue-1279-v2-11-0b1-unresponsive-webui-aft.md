# bitaxeorg/ESP-Miner issue #1279: v2.11.0b1 - unresponsive webui after few hours

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1279
> Collected: 2026-10-07
> Published: 2025-10-17

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1279
- State: closed
- Author: xr1140
- Opened: 2025-10-17
- Closed: 2025-11-01
- Labels: none

## Description

 - Bitaxe HW version: 601
 - ESP-Miner FW version: 2.11.0b1

After about 3-5 hours the webUI become inaccessible. The miner still works, I can see on the pool side but the webUI is completely unresponsive. A forced power off and on (aka unplug from socket) fix the problem for the next few hours.

The same behavior happens on multiple Gamma units. I'm the only one experiencing this?



## Comments

### duckaxe on 2025-10-18

What happens when you switch back to the v2.10.0? 

### LightBridge16 on 2025-10-19

this is what I got after rebooting the gamma 601 with the latest beta firmware. 


[0;32mI (6335192) websocket: WebSocket client disconnected, fd: 44[0m nothing more then this.

### LightBridge16 on 2025-10-19

oh btw this can change over time that the one that has this error come online in the swarm but the miners display says its mining all the time.

### mutatrum on 2025-10-19

Hopefully fixed by #1280 

### xr1140 on 2025-10-19

> What happens when you switch back to the v2.10.0?

It reverts back to running without a problem.
