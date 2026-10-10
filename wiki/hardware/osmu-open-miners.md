# OSMU Open Miners: NerdMiner, PiAxe, QAxe & BitForge

> Sources: OSMU wiki project pages (collected 2026-10-07), bitaxeorg/foss-miner-list README, bitaxeorg/bitaxe-web-flasher issue/PR records
> Raw: [OSMU wiki: NerdMiner](../../raw/hardware/bitaxe-osmu/osmu-wiki-nerdminer-about.md); [NerdNOS](../../raw/hardware/bitaxe-osmu/osmu-wiki-nerdnos-about.md); [NerdAxe](../../raw/hardware/bitaxe-osmu/osmu-wiki-nerdaxe-about.md); [NerdQAxe+](../../raw/hardware/bitaxe-osmu/osmu-wiki-nerdqaxeplus-about.md); [NerdQAxe++](../../raw/hardware/bitaxe-osmu/osmu-wiki-nerdqaxeplusplus-about.md); [PiAxe](../../raw/hardware/bitaxe-osmu/osmu-wiki-piaxe-about.md); [PiAxe assembly](../../raw/hardware/bitaxe-osmu/osmu-wiki-piaxe-assembly.md); [PiAxe building](../../raw/hardware/bitaxe-osmu/osmu-wiki-piaxe-building.md); [QAxe](../../raw/hardware/bitaxe-osmu/osmu-wiki-qaxe-about.md); [QAxe assembly](../../raw/hardware/bitaxe-osmu/osmu-wiki-qaxe-assembly.md); [QAxe installation](../../raw/hardware/bitaxe-osmu/osmu-wiki-qaxe-installation.md); [BitForge](../../raw/hardware/bitaxe-osmu/osmu-wiki-bitforge-bitforge.md); [foss-miner-list README](../../raw/hardware/bitaxe-osmu/github-bitaxeorg-foss-miner-list.md); [web-flasher #16](../../raw/hardware/bitaxe-osmu/2025-01-27-github-bitaxe-web-flasher-pr-16-nerdaxified.md); [web-flasher #27](../../raw/hardware/bitaxe-osmu/2025-11-19-github-bitaxe-web-flasher-issue-27-nerdqaxe-not-updateable.md)
> Updated: 2026-10-10
> As-Of: 2026-10-10
> Status: Draft

The Bitaxe is the best-known open home miner, but the OSMU wiki documents a wider family of open hardware and firmware that grew up beside it. Three lineages matter: the **NerdMiner** line (an ESP32 mining solo on software alone, grown into display hybrids around Bitaxe-class silicon), the **PiAxe/QAxe** line (a Raspberry Pi HAT and its quad-chip spin-off, controlled by external software), and the **BitForge Nano** (a standalone dual-BM1370 unit with its own firmware). The community keeps a canonical registry of all of them, the bitaxeorg/foss-miner-list, which is also where the board-number convention used across this family is written down ([foss-miner-list](../../raw/hardware/bitaxe-osmu/github-bitaxeorg-foss-miner-list.md)). For the core Bitaxe line itself, see [Bitaxe Models & Open-Source Miner Family](bitaxe-models.md).

## The NerdMiner line

The Nerdminer is the entry point: a free and open source project whose stated goal is to let you "try to reach a bitcoin block with a small piece of hardware", learn about mining, and have a nice object on the desk. It descends from Valerio Vaccaro's HAN Miner and is an implementation of the Stratum protocol on the ESP32 microcontroller, mining solo by default against Public Pool. It began on ESP32-S3 and now supports other boards, configures over WiFiManager to SPIFFS, and is genuinely multicore: both ESP32 cores hash while other threads handle stratum and Wi-Fi, updating work on every stratum job notification to avoid stale shares. Three built-in screens ship by default — NerdMiner (own mining data), ClockMiner (a clock that mines), and GlobalStats (network stats) ([OSMU wiki: NerdMiner](../../raw/hardware/bitaxe-osmu/osmu-wiki-nerdminer-about.md)).

The line then grows by attaching real hashing silicon:

- **NerdNOS** is an add-on board for a Nerdminer that lifts its hashrate to 150~200 GH/s using a BM1397 (the Bitaxe Max chip), deliberately underclocked to draw about 8W. Setup runs through the miner's own access point: connect to "NerdMinerAP" (password `MineYourCoins`), enter your Bitcoin address in the WiFiManager page, and monitor the address on the pool. Button 1 switches displays (hold while powering on to edit entries, 5 seconds to factory-reset), button 2 toggles the display without stopping mining, and the board wants a USB port rated for at least 2A ([OSMU wiki: NerdNOS](../../raw/hardware/bitaxe-osmu/osmu-wiki-nerdnos-about.md)).
- **NerdAxe** pairs the Nerdminer display with Bitaxe Ultra hardware: a modified Bitaxe Ultra board (BM1366) plus the Lilygo T-Display S3, talking to the ASIC over GPIO pins and reaching 500GH/s — the Ultra-class number. It runs its own ESP-Miner fork, ESP-Miner-NerdAxe ([OSMU wiki: NerdAxe](../../raw/hardware/bitaxe-osmu/osmu-wiki-nerdaxe-about.md)).
- **NerdQAxe+** scales the same display-plus-logic idea to four ASIC chips on a modified QAxe+ board, up to 2.5TH/s, still with the Lilygo T-Display S3 and shufps' modified AxeOS ([OSMU wiki: NerdQAxe+](../../raw/hardware/bitaxe-osmu/osmu-wiki-nerdqaxeplus-about.md)).
- **NerdQAxe++** moves to four BM1370 chips (the Antminer S21 series part) at up to 4.8 TH/s on roughly 60 watts — among the most efficient home miners — in a silent, compact package ([OSMU wiki: NerdQAxe++](../../raw/hardware/bitaxe-osmu/osmu-wiki-nerdqaxeplusplus-about.md)).

One spec conflict is live in the sources: the OSMU wiki's NerdQAxe+ page says four BM1366 chips, while foss-miner-list lists the NerdQAxe+ as four BM1368 ([OSMU wiki: NerdQAxe+](../../raw/hardware/bitaxe-osmu/osmu-wiki-nerdqaxeplus-about.md); [foss-miner-list](../../raw/hardware/bitaxe-osmu/github-bitaxeorg-foss-miner-list.md)).

## PiAxe and QAxe

The PiAxe takes a different shape: a Raspberry Pi HAT carrying one BM1366, controlled over the Pi's GPIO pins, powered by 12V, and running the Python-based piaxe-miner software on the Pi. Its hashrate matches a Bitaxe Ultra at around 500GH/s. The board work emphasizes hand assembly — smallest parts are 0805 size — with a TVS diode and fuses added and a revised buck regulator; an LM75-compatible temperature sensor is on board ([OSMU wiki: PiAxe](../../raw/hardware/bitaxe-osmu/osmu-wiki-piaxe-about.md)). OSMU hosts step-by-step assembly and building guides for it ([OSMU wiki: PiAxe assembly](../../raw/hardware/bitaxe-osmu/osmu-wiki-piaxe-assembly.md); [building](../../raw/hardware/bitaxe-osmu/osmu-wiki-piaxe-building.md)).

The QAxe extends the PiAxe to four BM1366 chips on an STM32-controlled board, with three revisions: rev1 tested at about 1.8TH/s average, rev2 reaching the same after minor fixes, and rev3 fixing misplaced 330µF caps and adding a boot switch. It is a PiAxe/Bitaxe hybrid design ([OSMU wiki: QAxe](../../raw/hardware/bitaxe-osmu/osmu-wiki-qaxe-about.md)). Two build details are worth knowing before assembling one:

- You can run a QAxe with a single ASIC installed and work up to all four; cover the pads of unpopulated ASIC positions before heatsinking and testing ([OSMU wiki: QAxe assembly](../../raw/hardware/bitaxe-osmu/osmu-wiki-qaxe-assembly.md)).
- Flashing changed for the better: the STM32L072CB variant has an integrated DFU bootloader entered by holding the BOOT button during reset, after which dfu-utils flashes the firmware. The older CMSIS-DAP path (Picoprobe on a Raspberry Pi Pico, or shufps' three-part low-cost DAP board) is explicitly deprecated as "quite a hassle" for one-time flashers; rev3 boards were supposed to make DFU entry universal ([OSMU wiki: QAxe installation](../../raw/hardware/bitaxe-osmu/osmu-wiki-qaxe-installation.md)).

Both PiAxe and QAxe depend on a separate computer running piaxe-miner — neither is standalone ([OSMU wiki: QAxe](../../raw/hardware/bitaxe-osmu/osmu-wiki-qaxe-about.md)).

## BitForge Nano

The BitForge Nano is the standalone entrant: a dual-BM1370 miner developed by WantClue with manufacturer DTV Electronics (board designed in Germany, produced by DTV), with the case, custom heatsink and airflow CFD contributed by "I Am GPIO" of The Solo Mining Co. An ESP32-S3-WROOM-1 manages mining, cooling and connectivity; the unit is Wi-Fi only, with no Ethernet. It runs ForgeOS, an open-source firmware with a browser dashboard for pool configuration, monitoring and tuning. Three performance profiles span roughly 2.0 TH/s (eco) to about 2.6 TH/s (performance) at approximately 40W — around 15 J/TH — cooled by two 40×20mm 12V PWM fans at measured noise around 30 dB ([OSMU wiki: BitForge](../../raw/hardware/bitaxe-osmu/osmu-wiki-bitforge-bitforge.md)).

## Firmware forks and the web flasher

The family maintains its own firmware forks rather than patching ESP-Miner itself, and the fork registry in foss-miner-list is the map: ESP-Miner (AxeOS) for Bitaxes, ESP-Miner-NerdAxe for the NerdAxe single-chip variants, shufps' ESP-Miner-NerdQAxePlus for NerdQAxe+/++ and Octaxe-class boards, ESP-Miner-TCH for the TinyChipHub 70x boards, and ForgeOS for the BitForge Nano ([foss-miner-list](../../raw/hardware/bitaxe-osmu/github-bitaxeorg-foss-miner-list.md)).

The official Bitaxe web flasher has a complicated relationship with these forks. In January 2025 shufps' PR #16 "Nerdaxified" the flasher — replacing its Bitaxe entries with Nerd*axe variants ([web-flasher #16](../../raw/hardware/bitaxe-osmu/2025-01-27-github-bitaxe-web-flasher-pr-16-nerdaxified.md)) — but coverage is not uniform: a NerdQAxe++ owner found the flasher reported a successful update while the firmware stayed on 1.0.33, and the resolution was that the NerdQAxe is "a different repo" the Bitaxe flasher does not serve ([web-flasher #27](../../raw/hardware/bitaxe-osmu/2025-11-19-github-bitaxe-web-flasher-issue-27-nerdqaxe-not-updateable.md)). Practical rule: flash Nerd-family boards from their own firmware repos unless the flasher explicitly lists the variant.

## foss-miner-list as the family registry

The bitaxeorg/foss-miner-list README is the closest thing the ecosystem has to a canonical index, and its hardware table shows the family extends beyond any single org: NerdAxe Ultra (1x BM1366) and NerdAxe Gamma (1x BM1370) under BitMaker-hub; the NerdQAxe line under BitMaker-hub and shufps; a community NerdQAxe++ rev.7 under benjamin-wilson; NerdOCTAXE-Plus (8x BM1368) and NerdOCTAXE-Gamma (8x BM1370) under Patsch91; the TinyChipHub Supra Hex and Gamma Hex forks; and the WantClue BitForge Nano ([foss-miner-list](../../raw/hardware/bitaxe-osmu/github-bitaxeorg-foss-miner-list.md)).

## See Also

- [Bitaxe Models & Open-Source Miner Family](bitaxe-models.md)
- [Public Pool](../pools/public-pool.md)
- [ESP-Miner / AxeOS](../firmware/esp-miner-axeos.md)
- Different topic: [Mining Policy and Legal](../industry/mining-policy-and-legal.md)
