# 256foundation/libreboard issue #14: Feature request: an 4-pin connector compatible with the Adafruit STEMMA and Sparkfun Qwicc standard

> Source: https://github.com/256foundation/libreboard/issues/14
> Collected: 2026-10-07
> Published: 2025-05-13

- Repository: 256foundation/libreboard
- Type: issue
- Number: 14
- State: closed
- Author: rkuester
- Opened: 2025-05-13
- Closed: 2025-06-09
- Labels: enhancement

## Description

It might be a nice touch if we put a 4-pin JST SH connector on the board for the expansion I2C bus, compatible with the [Adafruit STEMMA](https://learn.adafruit.com/introducing-adafruit-stemma-qt/technical-specs) and [Sparkfun Qwicc](https://www.sparkfun.com/qwiic) standard. This would open plug-and-play access to the many sensor, actuator, indicator, etc. modules hobbyists use via those standards.

I realize this could be done with a hat; however, we could do this with just a connector, or the footprint for a connector, and instantly have a lot of fun out-of-the-box.

## Comments

### Schnitzel on 2025-05-30

nice, yea I thought about this before as well, will add to the feature list.

### Schnitzel on 2025-06-09

this has been implemented in the newest version - see the Qwicc Connector above the M2 Slot

![Image](https://github.com/256-Foundation/Libre-Board/blob/main/assets/renders/face_top.png?raw=true)
