# 256foundation/emberone00-pcb issue #54: RP2040 may attempt flash read before 3V3 rail is stable

> Source: https://github.com/256foundation/emberone00-pcb/issues/54
> Collected: 2026-10-07
> Published: 2026-03-16

- Repository: 256foundation/emberone00-pcb
- Type: issue
- Number: 54
- State: open
- Author: rkuester
- Opened: 2026-03-16
- Closed: n/a
- Labels: none

## Description

While debugging an EmberOne/00 board that wouldn't boot reliably (which turned out to be a soldering issue on the CC resistors), I started looking at the power-up sequencing and noticed a potential boot race between the RP2040 and its SPI flash.

The RP2040's power-on reset releases at ~1V[^1], at which point the bootrom immediately tries to read from the external SPI flash. But the W25Q16JV flash needs at least 2.7V to operate[^2]. During a slow 3V3 ramp, the RP2040 could come out of reset and attempt a flash read well before the flash is ready, leading to a failed boot or unpredictable behavior.

Consider adding a voltage supervisor to hold the RP2040's RUN pin low until the 3V3 rail has stabilized.

Hardware version: v5 (9f75f0c)

[^1]: [RP2040 datasheet](https://pip-assets.raspberrypi.com/categories/814-rp2040/documents/RP-008371-DS-1-rp2040-datasheet.pdf?disposition=inline), section 2.12.2.1
[^2]: [W25Q16JV datasheet](https://mm.digikey.com/Volume0/opasdata/d220001/medias/docus/6661/W25Q16JV.pdf), section 10.2

## Comments

### skot on 2026-03-16

being as this design is directly from the official RPi Pico, I wonder if any of those have this problem?

### rkuester on 2026-03-16

Survey says... maybe? https://forums.raspberrypi.com/viewtopic.php?t=388599

It sounds like in the scenario I'm hypothesizing, the RP2040 might fall back to its USB firmware-loading mode—which I've not noticed.

### skot on 2026-03-19

ok, i'm in. Voltage supervisor seems like a low cost way to get more resiliency. 

### skot on 2026-03-21

added in v6.1

### rkuester on 2026-03-21

My only nit would be the net name `RUN_N`. The sense of RUN is active high.

Otherwise, LGTM. FWIW, I confirmed the part number matches the desired threshold voltage and package, and verified the pinout.

### korbin on 2026-03-27

I've never had this issue on dozens of RP2xxx boards - maybe add an RC delay at best, use an open drain voltage supervisor, and make either optional?

### rkuester on 2026-03-28

That's good to know. With the same Flash?

This is what's in v6.1 at the moment. It qualifies as optional.

<img width="312" height="145" alt="Image" src="https://github.com/user-attachments/assets/b6a6b7d8-adff-4ac4-b48c-8f0df851ecbe" />

### korbin on 2026-03-28

With Winbond W25Q16JVUXIQ and Zetta ZD25WQ16BUIGR - never any issues with any DC/DC or LDO on any board.

I imagine the POR routine is reasonably slow relative to any 3V3 LDO - if you don't have a massive sea of capacitance (multiple hundreds of µF probably), I don't know that this condition can occur.
