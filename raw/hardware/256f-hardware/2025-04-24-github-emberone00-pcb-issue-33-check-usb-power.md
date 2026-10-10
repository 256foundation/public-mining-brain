# 256foundation/emberone00-pcb issue #33: Check USB power

> Source: https://github.com/256foundation/emberone00-pcb/issues/33
> Collected: 2026-10-07
> Published: 2025-04-24

- Repository: 256foundation/emberone00-pcb
- Type: issue
- Number: 33
- State: closed
- Author: skot
- Opened: 2025-04-24
- Closed: 2025-06-09
- Labels: enhancement

## Description

Unconfigured USB devices should not draw over 100mA. as per [USB Wikipedia](https://en.wikipedia.org/wiki/USB_hardware#Allowable_current_draw). Once configured, "High-power devices" may draw up to 500mA.

500mA should be plenty. Not sure about 100mA. Either way, I should characterize how much power is needed over USB.

## Comments

### skot on 2025-04-25

While mining i'm seeing 50-60mA, depending on how the LED is set.
