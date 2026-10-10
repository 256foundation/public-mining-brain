# 256foundation/emberone00-pcb issue #19: noise on ASIC serial line with core voltage on

> Source: https://github.com/256foundation/emberone00-pcb/issues/19
> Collected: 2026-10-07
> Published: 2025-02-26

- Repository: 256foundation/emberone00-pcb
- Type: issue
- Number: 19
- State: open
- Author: skot
- Opened: 2025-02-26
- Closed: n/a
- Labels: bug

## Description

When monitoring the ASIC serial port via the RP2040 I saw some erroneous 0xFF bytes come through. This is prolly noise on the serial lines. Not sure of the source yet.

## Comments

### econoalchemist on 2025-03-12

Curious what the noise level is on the S9? Would it be worth checking as a baseline acceptable target to aim for?

### skot on 2025-03-13

The S9 regulator output is 9V. I ran my miner underclocked to 400W to 3 hashboards, so 133W each, or 14.7A and observed about 176mV p-p noise. This noise is 4.88% of the output.

<img width="679" alt="Image" src="https://github.com/user-attachments/assets/6daa160b-3bd8-48ee-86af-548332ae5c3e" />

### skot on 2025-03-13

For comparison, after the tweaks mentioned in #23 #24 #25 and #26 I was able to get the emberOne at 3.6V, 40W to 60mV p-p. This noise is 1.66% of the output. (note the different vertical scale)

<img width="681" alt="Image" src="https://github.com/user-attachments/assets/0d380d0f-a351-4aaa-bea0-50864cae1f38" />
