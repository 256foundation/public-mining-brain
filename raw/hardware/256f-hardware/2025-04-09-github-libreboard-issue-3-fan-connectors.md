# 256foundation/libreboard issue #3: Fan Connectors

> Source: https://github.com/256foundation/libreboard/issues/3
> Collected: 2026-10-07
> Published: 2025-04-09

- Repository: 256foundation/libreboard
- Type: issue
- Number: 3
- State: closed
- Author: Schnitzel
- Opened: 2025-04-09
- Closed: 2025-09-24
- Labels: none

## Description

Raspberry Pi Compute Module 5 IO board has a single JST-SH PWM fan connector - which we want to keep to cool any RaspberryPi
We need 4 fan connectors of the same type as regular fans but only 1 PWM signal for them

## Comments

### Schnitzel on 2025-05-30

after talking to skot we can actually use an EMC2305 which is a 5 port PWM I2C fan conrtroller, the bitaxe uses an EMC2101 and works great. this way we don't have to sacrifice an PWM pin of the RaspiHAT
