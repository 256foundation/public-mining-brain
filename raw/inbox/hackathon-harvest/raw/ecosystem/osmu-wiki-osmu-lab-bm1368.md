# The BM1368

> Source: https://osmu.wiki/osmu-lab/bm1368/
> Collected: 2026-10-07
> Published: Unknown

# The BM1368

The BM1368 is an undocumented SHA256 mining ASIC from Bitmain. It’s mostly used in the Antminer S21.

## Hashrate

[Section titled “Hashrate”](https://osmu.wiki#hashrate)

The nominal hashrate of the BM1368 is between 600\~750GH/s.

| Price | New: \~$25 Used: \~$15 in small quantities | 
| Efficiency | \~18J/TH | 
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
| TEMP\_P | Temperature postitive diode side | 
| TEMP\_N | Temperature negative diode side | 
| CO | Serial Command Output | 
| INV\_CLK0 | Inverted Clock Output (unknown use) | 
| PIN\_MODE | Pin mode selector | 
| VSS | Ground | 
| VDI0\_08\_1 | 0.8V IO voltage | 
| VSI0\_08\_1 | 1.8V IO voltage (this is normally 1.2V now) | 

## Versions

[Section titled “Versions”](https://osmu.wiki#versions)

It has multiple versions.
