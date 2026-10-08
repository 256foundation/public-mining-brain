# bitaxeorg/BitaxeGT issue #11: Can we DNP all the TPS546 strapping resistors?

> Source: https://github.com/bitaxeorg/BitaxeGT/issues/11
> Collected: 2026-10-07
> Published: 2025-09-01

- Repository: bitaxeorg/BitaxeGT
- Type: issue
- Number: 11
- State: open
- Author: skot
- Opened: 2025-09-01
- Closed: n/a
- Labels: enhancement

## Description

My sense is that the strapping resistors are just to set the default configuration of the [TPS546D24x](https://www.ti.com/lit/ds/symlink/tps546d24a.pdf) voltage regulator. Can we just configure the VR over I2C before enabling it? 

## Comments

### skot on 2025-09-01

<img width="1015" height="940" alt="Image" src="https://github.com/user-attachments/assets/d1a00e0c-855f-4bf7-8e25-3ce1b1f18273" />

I think the answer is _yes_. We can leave the pin-stripping resistors (R7, R9, R10, R11, R12 & R13) DNP, as long as we also leave the EN/UVLO pin also floating (DNP R4 & R5, and prolly C17). This will cause the TPS546D24x to startup with the output disabled, waiting for configuration at the default PMBus address (default slave address 0x24 if ADRSEL is floating).

We can still utilize the undervoltage shutdown functionality with a write to (0x5A) VIN_OFF register to set the VIN level below which the regulator shuts down.

We will need to maintain backwards compatibility with any hardware out there that still has these resistors placed. I think we can do this by making sure to disable the TPS546 output right away.

### skot on 2025-09-01

removing pin-stripping resistors (R7, R9, R10, R11, R12 & R13) and EN/UVLO parts (R4, R5, and C17) seems to be good. The only catch is that the firmware needs to be changed to configure the `ON_OFF_CONFIG` register 0x02 to ignore the analog EN/UVLO voltage by clearing the `CP` bit.

Now I need to make sure we are actually completely configuring the TPS546D24x over PMBus, and that the undervoltage shutdown functionality is still working. 

### skot on 2025-09-01

For some reason this isn't working on the bitaxeGamma 601;
```
I (2941) power_management: setting new vcore voltage to 1150mV
I (2942) vcore: Set ASIC voltage = 1.150V
I (2943) TPS546: Vout changed to 1.15 V
E (2947) TPS546: Status: 0x1842
E (2950) TPS546: The voltage regulator is turned off
E (2955) TPS546: A communication, memory, logic fault has occurred
E (2963) TPS546: TPS546 CML Status: 02
E (2967) TPS546: communication error detected
```

I'll have to look into what is different between the 601 and the 800 HW and FW.
