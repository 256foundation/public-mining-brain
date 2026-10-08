# 256foundation/emberone00-pcb issue #36: Add a fan connector?

> Source: https://github.com/256foundation/emberone00-pcb/issues/36
> Collected: 2026-10-07
> Published: 2025-04-24

- Repository: 256foundation/emberone00-pcb
- Type: issue
- Number: 36
- State: open
- Author: skot
- Opened: 2025-04-24
- Closed: n/a
- Labels: enhancement

## Description

The idea is to add some sort of fan connector on the emberOne to better facilitate single device hacking. This is a little tricky since most fans want 12V, and we don't have a fixed 12V available on the EmberOne. (VIN is 12-24V).

- We could just add a fan connector on VIN and say only use it if your fan is compatible with your input voltage.
     - This could lead to some sadness if you have VIN too high and burn out the fan
- We could add a proper fan controller (like say the EMC2101 potentially for #34) and have it connected to MCU I2C. Still have the VIN problem from above.
     - Same problem as above 
- We could add a 12V voltage regulator and do either of the options from above. 
     - Now _everyone_ has to pay for a 12V voltage regulator, even if they are using a separate system fan, or no fans at all (immersion, hydro, etc)
