# 256foundation/emberone00-pcb issue #56: PGOOD reads "good" when VIN is absent

> Source: https://github.com/256foundation/emberone00-pcb/issues/56
> Collected: 2026-10-07
> Published: 2026-03-16

- Repository: 256foundation/emberone00-pcb
- Type: issue
- Number: 56
- State: open
- Author: rkuester
- Opened: 2026-03-16
- Closed: n/a
- Labels: none

## Description

PGOOD is pulled up to 3.3V, so it reads high even when VIN is missing. Consider replacing the pull-up with a resistor divider from the regulator's 5V output. This serves double duty: it provides the open-drain pull-up and naturally falls to zero when VIN is absent.

Hardware version: v5 (9f75f0c)

## Comments

### skot on 2026-03-20

I think when VIN is absent PGOOD is just going to float, which might not be ideal.

The TPS546D24 will be unresponsive over SMBUS when VIN is absent.. but that's an I2C transaction to find out. Are you looking for an interrupt?

### skot on 2026-03-20

oh, wait the lower half of the voltage divider will pull it down. hmm maybe this can work.  Just gotta find a voltage divider value that works with the RP2040 GPIO voltages across the entire VIN range (with some buffer)

### skot on 2026-03-21

added in v6.1

### rkuester on 2026-03-21

I think that works, although I'm surprised to see it pulled up to VIN_REV. Is there a reason not to use VDD5 from pin 28? 

---

Here's an idea that might kill two birds with one stone: What if the USB 5V bus powered TPS546D24 AVIN instead? See section 7.3.3 and 8.5 of the [TPS546D24S datasheet](https://www.ti.com/lit/ds/symlink/tps546d24s.pdf) on split input supplies.

1. That would put the TPS546D24 in the same domain as the RP2040, ensuring the TPS546D42 is always in control of PGOOD. You could restore the pull-up to 3V3, and axe the new divider off VIN_REV.
2. It gives a reset of the TPS546D24 along with the rest of the board when USB 5V is cycled, something we've wanted anyway.
