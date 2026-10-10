# 256foundation/libreboard issue #9: Feature request: S9 board plug and play

> Source: https://github.com/256foundation/libreboard/issues/9
> Collected: 2026-10-07
> Published: 2025-05-06

- Repository: 256foundation/libreboard
- Type: issue
- Number: 9
- State: closed
- Author: TimothyShimmin
- Opened: 2025-05-06
- Closed: 2025-09-24
- Labels: none

## Description

Hey I just heard about this [project](https://x.com/Schnitzel/status/1919446976577540429), that one of the goals is modularity. 

Is there any intention of supporting boards straight out of corpo miners? I don't know what the limitations would be for that but it'd be nice to rip one out of an otherwise busted miner and slot it into this board.

## Comments

### econoalchemist on 2025-05-28

There's a few different approaches: One would be to flash [Mujina](https://mujina.org/) onto an existing S9 board, though this probably won't be viable until sometime after the first release. Two would be to use Libre Board as the controller running Mujina and then connect it to the S9 hashboards with the [Adit Board](https://github.com/skot/aditBoard) adapter. A third option would be to fork Libre Board and modify it to be a direct replacement.
