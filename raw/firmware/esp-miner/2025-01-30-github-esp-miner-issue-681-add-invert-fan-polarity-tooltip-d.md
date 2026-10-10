# bitaxeorg/ESP-Miner issue #681: add "invert fan polarity" tooltip/definition

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/681
> Collected: 2026-10-07
> Published: 2025-01-30

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 681
- State: closed
- Author: alltheseas
- Opened: 2025-01-30
- Closed: 2025-02-15
- Labels: none

## Description

![Image](https://github.com/user-attachments/assets/a0ecf66b-6fc2-453a-894f-2caf75d8c1f4)

I'm not a bitaxe/mining professional, and I do not know what this means.

Consider adding a tooltip that communicates what "invert fan polarity" this means (e.g. not sure if this is true - "This changes the direction in which the fan, and air flows")

example tooltip ui

![Image](https://github.com/user-attachments/assets/02ed83ed-8f0d-47cb-bc3e-141920f1212f)

## Comments

### MyOwn2C on 2025-01-30

It inverts the PWM fan signal. 
Some fans work at full RPM when PWM is 0%. 
This inverts the signal.
