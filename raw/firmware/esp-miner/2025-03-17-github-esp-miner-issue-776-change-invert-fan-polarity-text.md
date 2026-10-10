# bitaxeorg/ESP-Miner issue #776: Change "Invert Fan Polarity" text

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/776
> Collected: 2026-10-07
> Published: 2025-03-17

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 776
- State: closed
- Author: skot
- Opened: 2025-03-17
- Closed: 2025-03-20
- Labels: documentation, enhancement, good first issue, design

## Description

Seems like people are confusing this with a fan spin direction setting. Let's change the text to "Invert PWM Duty Cycle"

## Comments

### skot on 2025-03-17

or "Invert Fan Duty Cycle"

### JasonB1833 on 2025-03-17

Hey there, you just need the "invert fan polarity" calls to change for clarity throughout the codebase?? just asking for clarification before I jump into it and blindly change every instance of it to a clearer name.

### skot on 2025-03-17

> Hey there, you just need the "invert fan polarity" calls to change for clarity throughout the codebase?? just asking for clarification before I jump into it and blindly change every instance of it to a clearer name.

The only change needed is the text on the settings tab of AxeOS:

<img width="247" alt="Image" src="https://github.com/user-attachments/assets/09c5c6c2-6580-4afe-8d8f-a1f498bd6267" />

### skot on 2025-03-17

and lets go with "Invert Fan Duty Cycle"

### JasonB1833 on 2025-03-17

> and lets go with "Invert Fan Duty Cycle"

good to go, pr is up
