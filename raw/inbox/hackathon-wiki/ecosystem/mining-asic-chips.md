# Bitmain Mining ASIC Chips

> Sources: Open Source Miners United (osmu.wiki, The OSMU Lab), collected 2026-10-07; Open Source Miners United (osmu.wiki, The BM1362), collected 2026-10-07; Open Source Miners United (osmu.wiki, The BM1366), collected 2026-10-07; Open Source Miners United (osmu.wiki, The BM1368), collected 2026-10-07; Open Source Miners United (osmu.wiki, The BM1370), collected 2026-10-07; Open Source Miners United (osmu.wiki, The BM1397), collected 2026-10-07; Open Source Miners United (osmu.wiki, Bitaxe 200 'Ultra'), collected 2026-10-07; Open Source Miners United (osmu.wiki, Bitaxe 400 'Supra'), collected 2026-10-07; Open Source Miners United (osmu.wiki, Bitaxe 600 'Gamma'), collected 2026-10-07; bitaxeorg (bitaxeMax README), collected 2026-10-07; bitaxeorg (bitaxeUltra README), collected 2026-10-07; bitaxeorg (bitaxeSupra README), collected 2026-10-07; bitaxeorg (bitaxeGamma README), collected 2026-10-07; bitaxeorg (ultraHex README), collected 2026-10-07; 256 Foundation (projects page), collected 2026-10-07
> Raw: [The OSMU Lab](../../raw/ecosystem/osmu-wiki-osmu-lab-about.md); [The BM1362](../../raw/ecosystem/osmu-wiki-osmu-lab-bm1362.md); [The BM1366](../../raw/ecosystem/osmu-wiki-osmu-lab-bm1366.md); [The BM1368](../../raw/ecosystem/osmu-wiki-osmu-lab-bm1368.md); [The BM1370](../../raw/ecosystem/osmu-wiki-osmu-lab-bm1370.md); [The BM1397](../../raw/ecosystem/osmu-wiki-osmu-lab-bm1397.md); [Bitaxe 200 'Ultra'](../../raw/ecosystem/osmu-wiki-bitaxe-200.md); [Bitaxe 400 'Supra'](../../raw/ecosystem/osmu-wiki-bitaxe-400.md); [Bitaxe 600 'Gamma'](../../raw/ecosystem/osmu-wiki-bitaxe-600.md); [bitaxeMax README](../../raw/ecosystem/github-bitaxeorg-bitaxemax.md); [bitaxeUltra README](../../raw/ecosystem/github-bitaxeorg-bitaxeultra.md); [bitaxeSupra README](../../raw/ecosystem/github-bitaxeorg-bitaxesupra.md); [bitaxeGamma README](../../raw/ecosystem/github-bitaxeorg-bitaxegamma.md); [ultraHex README](../../raw/ecosystem/github-bitaxeorg-ultrahex.md); [256foundation.org projects](../../raw/foundation/256foundation-org-projects.md)
> Updated: 2026-10-07

## Overview

Open miners like the Bitaxe are built around closed parts, above all the mining ASIC. The chips used so far are undocumented SHA256 ASICs from Bitmain, taken from Antminer machines. The OSMU Lab is the section of the OSMU wiki where the community publishes what it has learned by reverse engineering them, and where it plans to publish research papers. This article collects the lab pages on five chips, BM1397, BM1362, BM1366, BM1368 and BM1370, and compares them with what the Bitaxe READMEs say. Several figures differ between the two.

## Comparison from the OSMU Lab

| Chip | Mostly used in | Efficiency | Price in small quantities | Nominal hashrate | Open design using it |
|------|----------------|------------|---------------------------|------------------|----------------------|
| BM1397 | Antminer S17 and T17 | `0.03J/GH` | New: ~$20, used: ~$6 | not given | Bitaxe Max |
| BM1362 | Antminer S19jPro | 29.4J/TH | New: ~$5, used: ~$1 | not given | [Ember One](../hardware/ember-one.md) |
| BM1366 | Antminer S19 | 25J/TH | New: ~$25, used: ~$15 | not given | Bitaxe Ultra, Hex |
| BM1368 | Antminer S21 | ~18J/TH | New: ~$25, used: ~$15 | 600~750GH/s | Bitaxe Supra |
| BM1370 | Antminer S21 Pro | 15J/TH | unknown | 1~1.4TH/s | Bitaxe Gamma |

All five use UART as their serial protocol. The lab pages leave baud rate and footprint blank for every chip except the BM1397.

## BM1397

- Default baud rate is `115200bps`, and it can go up to `6Mbps`. The Max README says the higher rate is needed to feed mining jobs quickly enough to a daisy-chain of chips.
- Its footprint is the same as the older BM1387, but the Max README says the pinout is very different.
- It has two modes that move some signal pins around to make chaining chips easier.
- It comes in multiple versions. Both sources link an outside guide for choosing one.
- The serial port runs at 1.8V, so the Max uses level shifters to connect it to the 3.3V ESP32.

## BM1362

The lab page is short. It gives the table values above and the same cracked-chip note as the BM1366 page. The 256 Foundation's projects page lists the Bitmain BM1362 as the ASIC of its [Ember One](../hardware/ember-one.md) hash board.

## BM1366

The lab page gives a pin table. The pins cover three internal voltage domains, ground, reset in and out, clock in and out, serial command in and out, serial response in and out, busy in and out, two address pins of unknown function, and IO supplies at 0.8V and 1.8V. The page notes the 1.8V supply is normally 1.2V now.

The Ultra README adds two points. The chip has a different footprint and pinout from the BM1397 and BM1387. It also appears to roll more than just the nonce on the chip, which allows much longer serial chains and means new work is sent less often. The README says both the AG and AL variants work.

> **Status: Disputed**
> Source miner: the OSMU Lab says the BM1366 is mostly used in the Antminer S19. The bitaxeUltra README says the Antminer S19XP and the S19k Pro.
> Efficiency: the OSMU Lab lists 25J/TH. The bitaxeUltra README says Bitmain claims 0.021J/GH. The ultraHex README says Bitmain claims 21.5 W/TH.
> Price: the OSMU Lab lists new chips at ~$25 and used at ~$15. The bitaxeUltra and ultraHex READMEs say new chips cost around $15 each.

## BM1368

The pin table matches the BM1366 with two additions: `TEMP_P` and `TEMP_N`, the two sides of a temperature diode. The Supra README says the footprint and pinout differ from the BM1366, BM1397 and BM1387.

> **Status: Disputed**
> Efficiency: the OSMU Lab lists ~18J/TH. The bitaxeSupra README and the OSMU wiki's Supra page say Bitmain claims 17.5 J/TH.

## BM1370

The lab page numbers all of its pins. Compared with the older chips, the IO supplies are 0.8V and 1.2V, and the temperature diode pins are kept. The Gamma README estimates about 1.2 TH/s per chip, which sits inside the lab's nominal range. Both sources give 15 J/TH as Bitmain's claimed efficiency. The README says the Gamma gets pretty close to that.

> **Status: Disputed**
> Footprint: the OSMU wiki's Gamma page says the BM1370 has a similar footprint and pinout to the BM1368. The bitaxeGamma README says it has a different footprint and pinout from the BM1368, BM1366, BM1397 and BM1387.

## Sourcing and damage

- The Supra and Gamma sources each said, when written, that the chip was brand new and not yet sold on its own. The Gamma README says the best place to get a BM1370 is out of an S21 Pro.
- The BM1362 and BM1366 lab pages describe how to spot a destroyed chip: a crack through the middle of the die. It points to too much heat, probably during soldering, and means the chip will no longer work.

## Other chips in bitaxeorg designs

The Naja prototypes use newer Bitmain chips linked to the Antminer S23 series, and two boards use Intel's BZM2 instead of a Bitmain chip. See [Multi-Chip Bitaxe Designs](multi-chip-bitaxe-designs.md) and [Intel BZM2 Designs: BIRDS and Bonanza](intel-bzm2-designs.md).

## See Also

- [Bitaxe Model Lineup](bitaxe-models.md)
- [Multi-Chip Bitaxe Designs](multi-chip-bitaxe-designs.md)
- [Intel BZM2 Designs: BIRDS and Bonanza](intel-bzm2-designs.md)
- [Ember One](../hardware/ember-one.md)
