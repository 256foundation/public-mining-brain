# 256foundation/libreboard issue #1: 12-24V Input Voltage

> Source: https://github.com/256foundation/libreboard/issues/1
> Collected: 2026-10-07
> Published: 2025-04-09

- Repository: 256foundation/libreboard
- Type: issue
- Number: 1
- State: closed
- Author: Schnitzel
- Opened: 2025-04-09
- Closed: 2025-09-24
- Labels: none

## Description

The Raspberry Pi Compute Module 5 IO board supports only 5V input (either via USB-C or vai external connection).
We need to change this to 12-24V like the Ember Board has

## Comments

### econoalchemist on 2025-04-16

A couple options worth considering might could be:

1) A companion expansion board that matches the same 128mm x 128mm profile, this expansion board could have 1 upstream USB data port, 10 downstream USB ports for adding more hashboards, multiple (4?) fan ports, a dedicated fan controller IC, a copy of the Ember One voltage regulator, and the RP2040 USB controller. Essentially, just taking the ASICs off the Ember One board and adding a USB hub and implements for the fans. This way users who want only one Ember One hashboard in their system don't have to pay for the extra components needed to run multiple boards and the control board can just have the bare essentials. 
2) Copy/paste the Ember One voltage regulator onto the control board and modify it to output 12v for the fans and 5v for the compute module.

### Schnitzel on 2025-04-30

realized that the Fans on the raspi board are 5V, while we need 12V, so yea I need to find a way to also output 12V beside the 5V
