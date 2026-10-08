# bitaxeorg/ESP-Miner issue #1198: Pool response/ping time bug?

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1198
> Collected: 2026-10-07
> Published: 2025-08-19

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1198
- State: closed
- Author: homecryptominer
- Opened: 2025-08-19
- Closed: 2025-08-21
- Labels: none

## Description

On my fleet of Bitaxes, some of them will randomly show a massive Pool Response Time of something like 26041793.839 ms. On the pool side, everything is working fine and hash rates are registering fine. When I click the restart button on these Bitaxes, within a few seconds it shows the more normal/correct value of around 120ms.

Is this a bug? Or is there something causing the massive number blowout?

Screen shot with massive pool response/ping time:
![Image](https://github.com/user-attachments/assets/d370e249-31a2-422a-a897-492fa00749ed)

Screen shot after a reset showing normal pool response/ping time:
![Image](https://github.com/user-attachments/assets/4ed87e2b-872a-477e-988c-a2ead21f4688)

Thanks!

## Comments

### Dragonfir3 on 2025-08-21

Same here. Sometimes appear 17435586.158ms, but other ~50ms (with shares). Surely the correct one is the second one.

### WantClue on 2025-08-21

It's a nown bug and has already been resolved in the master branch. As soon as 2.10.0 hits this will be resolved.
Thanks for the awareness
