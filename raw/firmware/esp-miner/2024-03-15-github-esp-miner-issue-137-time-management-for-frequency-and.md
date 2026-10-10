# bitaxeorg/ESP-Miner issue #137: Time management for frequency and core voltage

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/137
> Collected: 2026-10-07
> Published: 2024-03-15

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 137
- State: closed
- Author: exobug
- Opened: 2024-03-15
- Closed: 2024-03-16
- Labels: none

## Description

Is it possible to implement a menu for time management, e.g. to use a special frequency and core voltage at night from 11 p.m. to 8 a.m.?

And during the rest of the time for the default settings? Is that possible?

## Comments

### MyOwn2C on 2024-03-15

You can use a keyboard recorder to record the keystrokes that will go to the webpage and change the settings. Then run the macro using a scheduler. 

### exobug on 2024-03-16

> You can use a keyboard recorder to record the keystrokes that will go to the webpage and change the settings. Then run the macro using a scheduler.

but there is a Scheduler in Bitaxe firmware and time can be updated over internet. nor?

### skot on 2024-03-16

The ESP32 has a RTC that could be used for this, so yes technically possible. It's a big task to implement in firmware and the UI.

I think a better way to do it might be a separate program running on another machine to control the miners over the API.

Please use the Discussion area or OSMU Discord to discuss feature requests.

### ghost on 2025-09-17

It would be a great feature.
