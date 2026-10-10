# bitaxeorg/ESP-Miner issue #731: AxeOS “Presettings Button"

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/731
> Collected: 2026-10-07
> Published: 2025-02-21

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 731
- State: closed
- Author: CptGrato
- Opened: 2025-02-21
- Closed: 2025-03-06
- Labels: none

## Description

It would be great to implement 2 buttons where you can
save your settings.
(Preset of Frequency/Core Voltage/Fan Speed)

For example, 1. button could be used as "save-mode" when you leave the house and the miners are unattended. 

The 2nd button could be a high-setting. 

This would make it much easier to switch quickly without having to search for the best data again, especially if you have several in use.

If these two preset buttons
are also in the "swarm" view 
It would be perfect to change all miners quickly switching.

## Comments

### MyOwn2C on 2025-02-22

You can use API calls to write your preset values easily. 
Memory size in ESP32 is very little. 

### WantClue on 2025-03-06

We already feature a scope of settings, adding a preset is currently not planned and might not be applicable to all devices. Some chips behave better, some worse.

### CptGrato on 2025-03-07

You misunderstood me.  They are not supposed to be presets, but I want to save settings that work well and call them up with the buttons.
