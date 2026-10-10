# bitaxeorg/ESP-Miner issue #701: TPS546 Power measurements are incorrect

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/701
> Collected: 2026-10-07
> Published: 2025-02-12

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 701
- State: open
- Author: skot
- Opened: 2025-02-12
- Closed: n/a
- Labels: bug

## Description

The TPS546 only measures it's _output_ power so this won't include things like the fan, display and ESP32. But even taking this into account, the power measurement is still off. Especially on the gammaTurbo

## Comments

### skot on 2025-04-23

GT power measurements are much better after #796 

I'll do a reality check and see how close we are on the power measurements now

### WantClue on 2026-05-29

@skot any updates on that? I think the TPS is good atm ?
