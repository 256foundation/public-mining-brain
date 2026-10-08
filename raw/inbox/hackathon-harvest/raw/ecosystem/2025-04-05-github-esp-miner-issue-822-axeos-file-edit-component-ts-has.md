# bitaxeorg/ESP-Miner issue #822: AxeOS file edit.component.ts has hardware specific code

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/822
> Collected: 2026-10-07
> Published: 2025-04-05

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 822
- State: closed
- Author: skot
- Opened: 2025-04-05
- Closed: 2025-04-27
- Labels: bug, help wanted

## Description

AxeOS frontend file [edit.component.ts](https://github.com/bitaxeorg/ESP-Miner/blob/master/main/http_server/axe-os/src/app/components/edit/edit.component.ts) has hardware specific code in it. This should all come through the API (prolly from asic.c).

This looks to be how AxeOS gets the suggested ASIC frequency and voltage settings. Maybe the API can provide an array of values for this?

https://github.com/bitaxeorg/ESP-Miner/blob/6de4609f929ab92155b262bbe1422dd63b319f4f/main/http_server/axe-os/src/app/components/edit/edit.component.ts#L32-L120

https://github.com/bitaxeorg/ESP-Miner/blob/6de4609f929ab92155b262bbe1422dd63b319f4f/main/http_server/axe-os/src/app/components/edit/edit.component.ts#L278-L287

https://github.com/bitaxeorg/ESP-Miner/blob/6de4609f929ab92155b262bbe1422dd63b319f4f/main/http_server/axe-os/src/app/components/edit/edit.component.ts#L305-L314


## Comments

### mutatrum on 2025-04-06

Maybe we can add a new api call for this, the `info` endpoint is getting quite overloaded. There is no need to send all this info to the front-end every 5 seconds.

### skot on 2025-04-06

Great idea. Prolly only need to send it once?
