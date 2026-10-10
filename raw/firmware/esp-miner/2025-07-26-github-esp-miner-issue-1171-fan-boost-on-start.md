# bitaxeorg/ESP-Miner issue #1171: Fan boost on start

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1171
> Collected: 2026-10-07
> Published: 2025-07-26

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1171
- State: closed
- Author: riktam
- Opened: 2025-07-26
- Closed: 2025-07-27
- Labels: none

## Description

If you have a setup with a low fan speed some fans don't start rotating due to lack of power to overcome the initial inertia. If you push them manually they will move and then operate normally.

Can you start then fans at 100% and then lower the speed to the set point instead of starting at 0?

Thanks.

## Comments

### skot on 2025-07-26

I'm pretty sure this is going to be a custom EMC2101 configuration. Can you tell us how to get a fan with this issue?

### riktam on 2025-07-26

I'm using  a noctua V splitter to put a fan in the back of the bitaxe gamma.I've a 60x60x15 PWM and a 40x40x20 non-PWM noctua fans.

### skot on 2025-07-27

Check two things please:

1. Confirm both fans are actually 5V fans.

2. Confirm that the same thing happens with just one fan connected.

### riktam on 2025-07-27

The new fan was actually 12v, switching to a 5v one made all issues go away.
Thanks for all the help.
