# bitaxeorg/bitaxeGamma issue #11: Add power input protection

> Source: https://github.com/bitaxeorg/bitaxeGamma/issues/11
> Collected: 2026-10-07
> Published: 2024-10-24

- Repository: bitaxeorg/bitaxeGamma
- Type: issue
- Number: 11
- State: open
- Author: BitMaker-hub
- Opened: 2024-10-24
- Closed: n/a
- Labels: none

## Description

Even could not be necessary, this is recommended to protect bitaxe from plug/unplug transients.
This should be on the power supply, but you can't always guarantee.
A SMAJ5.0A is enough

<img width="730" alt="gamma" src="https://github.com/user-attachments/assets/a54cba40-e729-4137-b450-fdd4753e7e25">


## Comments

### etkaar on 2024-11-17

Hi! Sounds good. I added the diode into the schematics and placed it on the backside:
https://github.com/etkaar/bitaxe-gamma/commit/5fe13252e808a77f498ea90b609bffe9aaf64e53

Position on PCB is not final though, since I also want to add a SMD fuse, see https://github.com/skot/bitaxeGamma/issues/17.

### etkaar on 2024-11-19

Unfortunately I am not so familiar with the PCB, so it is hard for me to add the SMD fuse.

However, regarding the TVS diode two important notes:

- I would **not** recommend adding it without adding the fuse, because if the TVS dies, it will cause a short.
- 400W for the SMAJ5.0A sounds much, but probably isn't enough. As far as I know some kind of ESD protection can be offered by capacitors as well and having some (bulk?) capacitance at 5 V input sounds not bad and we already have C2, C3 and C4. Others are more competent than me to answer the question if these are already enough and/or if we can use a bulk capacitance (e.g. a nice aluminum electrolytic capacitor) instead.

### skot on 2025-04-29

The SMAJ5.0A is close, but not ideal for the Bitaxe's input voltage range of 4.5V - 5.5V;

Stand-off Voltage (V_RWM): 5.0V – This is the maximum continuous voltage the diode can handle without conducting significant current. This means we will be conducting and dissipating heat at 5.0 - 5.5V

Clamping Voltage (V_C): Maximum 9.2V (at peak pulse current) – This is the voltage across the diode when it is clamping a transient. 9.2V is too high for most everything on the PCB. (We really need to clamp at 6-7V)

If anyone knows of a TVS with V_RWM around 5.5V and V_C closer to 6-7V, plz let me know!
