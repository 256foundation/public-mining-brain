# bitaxeorg/BitaxeGT issue #9: 800xxx does not boot with R7 installed.

> Source: https://github.com/bitaxeorg/BitaxeGT/issues/9
> Collected: 2026-10-07
> Published: 2025-08-11

- Repository: bitaxeorg/BitaxeGT
- Type: issue
- Number: 9
- State: open
- Author: skot
- Opened: 2025-08-11
- Closed: n/a
- Labels: bug

## Description

A user reported this to me;

the 800xxx schematic shows R7 at 14.7k;

<img width="552" height="225" alt="Image" src="https://github.com/user-attachments/assets/72f106b2-777e-41a6-be19-1646921fbcb3" />

But with this strapping resistor soldered in place the bitaxe doesn't boot. Removing the resistor and the Bitaxe boots normally (with the exception of https://github.com/bitaxeorg/ESP-Miner/issues/1185)

Interestingly the Webench design has R7 as DNP. (Rmsel1t)

<img width="560" height="299" alt="Image" src="https://github.com/user-attachments/assets/8703dde5-c7a5-42b5-a954-e7f48e17aea3" />

## Comments

### skot on 2025-08-28

I installed a 14.7k resistor at R7 as specified, and I'm not seeing this issue. 

### benjamin-wilson on 2025-08-31

Seems R7 is not required then, should we DNP?

### skot on 2025-08-31

It is my understanding that these strapping resistors set the default config of the VR. We always manually config the TPS546 over I2C anyways, so it would seem like none of them are needed. But I'd like to test and understand this more before making that call.

### skot on 2025-09-01

> It is my understanding that these strapping resistors set the default config of the VR. We always manually config the TPS546 over I2C anyways, so it would seem like none of them are needed. But I'd like to test and understand this more before making that call.

I'm looking into this here; https://github.com/bitaxeorg/BitaxeGT/issues/11
