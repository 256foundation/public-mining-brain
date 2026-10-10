# bitaxeorg/ultraHex issue #10: core voltage is too high for ESP32 ADC measurement

> Source: https://github.com/bitaxeorg/ultraHex/issues/10
> Collected: 2026-10-07
> Published: 2023-11-25

- Repository: bitaxeorg/ultraHex
- Type: issue
- Number: 10
- State: closed
- Author: skot
- Opened: 2023-11-25
- Closed: 2024-03-14
- Labels: bug

## Description

The ESP32 measures the ASIC core voltage (TPS40305 output) via an ADC pin. 4.5V is too high to measure directly. put a voltage divider in there.

## Comments

### macphyter on 2023-12-17

I changed this input to a voltage divider, and I used two 10K resistors as placeholders until I could go figure out the real values.  Looks like I forgot to set the new values.  Keeping this issue open until I do that.

### skot on 2023-12-18

How about 100k and 226k for a 0.7 voltage divider? this makes VDD_SAMPLE = 2.5V for VDD = 3.6V and VDD_SAMPLE = 3.12V for VDD = 4.5V

### macphyter on 2023-12-19

I chose 69.8K and 182K just because we are already using those values and we wouldn't have to add any unique parts to the BOM.  This gives us VDD_SAMPLE = 2.6V for VDD = 3.6V, and VDD_SAMPLE = 3.25V for VDD = 4.5V.
In any case, its a simple resistor swap to change this.
