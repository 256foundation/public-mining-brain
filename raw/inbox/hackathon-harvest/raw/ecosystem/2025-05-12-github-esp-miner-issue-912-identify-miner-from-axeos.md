# bitaxeorg/ESP-Miner issue #912: Identify miner from AxeOS

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/912
> Collected: 2026-10-07
> Published: 2025-05-12

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 912
- State: closed
- Author: mutatrum
- Opened: 2025-05-12
- Closed: 2025-11-26
- Labels: none

## Description

For people with lots of Bitaxes, it would be nice to be able to trigger a big visible marker on the display from AxeOS and the swarm page. Similar to "Identify monitors" in Windows or what some smart thermostats can do:

![Image](https://github.com/user-attachments/assets/a0847130-c83c-40c5-a429-bbe6ad2e3d96)

![Image](https://github.com/user-attachments/assets/737730ef-1ae9-4ca2-a97b-e50fa5540376)

Basically just flash something on screen for 5 or 10 seconds or so.

## Comments

### ghost on 2025-05-12

5 or 10 seconds might not be enough, all depends on where they are located (takes 30 seconds to walk to the first device and then another 30 seconds plus to check all the others).

If your using your cell phone for this it should work fine, just increase the time for the message that gets shown on the OLED. 




### skot on 2025-05-12

We could have the screen invert until the boot button is pushed?

Then we just have to make sure people who inadvertently got in this mode know how to get out...

### ghost on 2025-05-12

Could set it as invert for 30 seconds and then it switches back automatically. 

If using a message that gets displayed .... like ...

"Hey !  I'm the device your looking for !"

### mutatrum on 2025-05-12

Where's the `<blink>` tag?

I do like the oversized Hi! graphic.

### NilByte on 2025-05-12

https://github.com/bitaxeorg/ESP-Miner/issues/615
