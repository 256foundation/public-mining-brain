# 256foundation/libreboard issue #12: Feature request: route serial console pins to thru-holes for .100 header

> Source: https://github.com/256foundation/libreboard/issues/12
> Collected: 2026-10-07
> Published: 2025-05-13

- Repository: 256foundation/libreboard
- Type: issue
- Number: 12
- State: closed
- Author: rkuester
- Opened: 2025-05-13
- Closed: 2025-09-24
- Labels: enhancement

## Description

Pins 6, 8, and 10 on the Raspberry Pi 40-pin header are often used for a Linux serial console—The Way to get a command shell without needing monitors, keyboards, a configured network, etc., and often used for development and debugging when nothing else is working. It would ideal to preserve semi-easy access to the serial console even when a hat is in use on the 40-pin header.

Could we please route those signals to thru-holes for a 3-pin, .100"-centers header, even if we don't populate it with a header or connector? Ideally it'd be on a board edge so that a right-angle connector is an option.

As a helpful byproduct, the obvious use of those signals on the PCB might deter hat developers from using those pins for other purposes. We might mention that in our documentation.

## Comments

### Schnitzel on 2025-05-30

great! I'll add that
