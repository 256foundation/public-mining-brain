# 256foundation/emberone00-pcb issue #40: Temperature / Power readings fail sometimes

> Source: https://github.com/256foundation/emberone00-pcb/issues/40
> Collected: 2026-10-07
> Published: 2025-05-01

- Repository: 256foundation/emberone00-pcb
- Type: issue
- Number: 40
- State: open
- Author: skot
- Opened: 2025-05-01
- Closed: n/a
- Labels: bug

## Description

I _think_ this is a software issue, but I'd like to be sure. failed temp / power readings cause overtemp/current shutdown and interrupt mining.

I have been able to reproduce this by reading temp/power at 0.1s intervals. every so often the INA260 current comes back as 0xFFFF

```
Voltage: 0.00 V
ctrl rx: [02 00 BB 00 00]
Current: 0.00 A
ctrl rx: [02 00 DD 00 00]
Power: 0.00 W
ctrl rx: [02 00 AA 1A 20]
ctrl rx: [02 00 BB 19 B0]
Temp: 26ºC, 25ºC
LED Color: Magenta
ctrl rx: [02 00 CC 00 01]

Voltage: 0.00 V
ctrl rx: [02 00 BB 00 00]
Current: 0.00 A
ctrl rx: [02 00 DD 00 00]
Power: 0.00 W
ctrl rx: [02 00 AA 1A 20]
ctrl rx: [02 00 BB 19 B0]
Temp: 26ºC, 25ºC
LED Color: Green
ctrl rx: [02 00 CC 00 01]

Voltage: 0.00 V
ctrl rx: [02 00 BB FF FF] <-- oops
Current: 81.92 A          <-- oops
ctrl rx: [02 00 DD 00 00]
Power: 0.00 W
ctrl rx: [02 00 AA 1A 20]
ctrl rx: [02 00 BB 19 B0]
Temp: 26ºC, 25ºC
LED Color: Magenta
ctrl rx: [02 00 CC 00 02]
```

## Comments

### skot on 2025-05-01

This doesn't seem to be a emberone-usbserial-fw issue.. the ID field is still coming back correct. I bet the INA260 just isn't ready.
