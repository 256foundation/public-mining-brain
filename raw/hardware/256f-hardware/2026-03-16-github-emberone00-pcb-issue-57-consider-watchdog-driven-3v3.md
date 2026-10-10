# 256foundation/emberone00-pcb issue #57: Consider watchdog-driven 3V3 bus reset for robust recovery

> Source: https://github.com/256foundation/emberone00-pcb/issues/57
> Collected: 2026-10-07
> Published: 2026-03-16

- Repository: 256foundation/emberone00-pcb
- Type: issue
- Number: 57
- State: open
- Author: rkuester
- Opened: 2026-03-16
- Closed: n/a
- Labels: none

## Description

We recently advised a Bitaxe user to power-cycle his board for a clean state, which got me thinking about the reset story on EmberOne.

The hash chip chain is easy: it lives behind a switched power domain and resets cleanly. The regulator for that domain doesn't hard-reset, though, so firmware must fully tear down and reinitialize its state.

The bigger gap is the 3V3 bus. The RP2040, flash, and temperature sensors all live here, and the only way to hard-reset them today is to pull the USB cable. The RP2040 itself can be warm-reset via the pushbutton or a software command, but the flash and temperature sensors have no reset path at all.

One approach would be to use a 5V-to-3.3V regulator with an enable pin and add a watchdog that can pull enable low to collapse the entire 3V3 bus. Connect the existing reset pushbutton to the watchdog's manual reset input, and give the RP2040 a GPIO to trigger it as well. This would give three reset paths: watchdog timeout, pushbutton, and firmware-initiated.

The LED is the one exception. It sits on the 5V bus, and adding a load switch for a single device seems unreasonable. Firmware should just clear it at boot.

The reset story on future Bitaxes (like Bonanza) deserves a thorough look too.

Hardware version: v5 (9f75f0c)

## Comments

### rkuester on 2026-03-19

A watchdog's interaction with the firmware loading mode would have to be considered.

### skot on 2026-03-19

The main issue here is the regulator getting in a bad state and needing reset, right? Afaik the only way to hard reset the regulator is to switch off VIN. That would have to be the job of the controlboard & PSU.

The TPS546D24 regulator is a complicated beast for sure, but I'd like to think we could soft reset it and reinitialize to a known state from the RP2040

As for the 5V/3V3 rails, I suppose a capable controlboard could switch on and off the 5V USB Power?

### rkuester on 2026-03-19

> The main issue here is the regulator getting in a bad state and needing reset, right? Afaik the only way to hard reset the regulator is to switch off VIN. That would have to be the job of the controlboard & PSU.
> 
> The TPS546D24 regulator is a complicated beast for sure, but I'd like to think we could soft reset it and reinitialize to a known state from the RP2040

Yes, I have long given up on a hard reset of the TPS546D24. As you imply, switching VIN on the board is certainly out of the question. You're right it could be done at more of a system level, but that's probably impractical to manage from Mujina.

I'm pretty happy with the hardware-based safe state of the TPS546D24: at boot and reset of the RP2040, enable turns into an input, gets pulled down, and the regulator output stops. I too am confident in software's ability to reset and re-initialize it from the ground up when it needs to.

> As for the 5V/3V3 rails, I suppose a capable controlboard could switch on and off the 5V USB Power?

This was my main issue: ICs on the always-on 3V3 rail.

You make a good point. Capable USB hubs can switch off the power to a port. Looking at LibreBoard's on-board hub: the IC is capable of this, but it is not wired up to do so. Perhaps we should ask @Schnitzel to change that. The more I think about it, the more this seems like a good solution.

The RP2040's internal peripheral is suitable for regular watchdog functions.  I still think a power supervisor is a good idea (#54).
