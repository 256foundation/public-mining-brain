# The BM1366

> Source: https://osmu.wiki/osmu-lab/bm1366/
> Collected: 2026-10-07
> Published: Unknown

# The BM1366

The BM1366 is an undocumented SHA256 mining ASIC from Bitmain. It’s mostly used in the Antminer S19.

| Price | New: \~$25 Used: \~$15 in small quantities | 
| Efficiency | 25J/TH | 
| Serial Protocol | UART | 
| Baudrate | - | 
| Footprint | - | 

## Pinout

[Section titled “Pinout”](https://osmu.wiki#pinout)

| Pinout | Explanation | 
|---|---|
| VDD1\_0 | Internal voltage domain 1. (for bypass capacitors) | 
| VDD2\_0 | Internal voltage domain 2. (for bypass capacitors) | 
| VDD3\_0 | Internal voltage domain 3. (for bypass capacitors) | 
| VSS | Ground | 
| NRSTI | Reset input | 
| BI | Busy Input | 
| RO | Serial Response Output | 
| CLKI | Clock Input | 
| CI | Serial Command Input | 
| ADDR0 | Address 0 (unknown functionality) | 
| ADDR1 | Address 1 (unknown functionality) | 
| PLL\_VSS | Phase Locked Loop Ground | 
| VDDIO\_08\_0 | 0.8V IO voltage | 
| VDDIO\_18\_0 | 1.8V IO voltage (this is normally 1.2V now) | 
| VDD1\_1 | Internal voltage domain 1. (for bypass capacitors) | 
| VDD2\_1 | Internal voltage domain 2. (for bypass capacitors) | 
| VDD3\_1 | Internal voltage domain 3. (for bypass capacitors) | 
| VSS | Ground | 
| NRST0 | Reset Output | 
| BO | Busy Output | 
| RI | Serial Response Input | 
| CLK0 | Clock output | 
| CO | Serial Command Output | 
| INV\_CLK0 | Inverted Clock Output (unknown use) | 
| PIN\_MODE | Pin mode selector | 
| VSS | Ground | 
| VDI0\_08\_1 | 0.8V IO voltage | 
| VSI0\_08\_1 | 1.8V IO voltage (this is normally 1.2V now) | 

## Versions

[Section titled “Versions”](https://osmu.wiki#versions)

## How to identify a cracked “destroyed” chip

[Section titled “How to identify a cracked “destroyed” chip”](https://osmu.wiki#how-to-identify-a-cracked-destroyed-chip)

Here you can cleary see a crack right in the middle of the die. This indicates too much heat on the chip itself probably during a soldering attempt. This crack identifies that this chip will no longer work and therefore has been destroyed. It has multiple versions.
