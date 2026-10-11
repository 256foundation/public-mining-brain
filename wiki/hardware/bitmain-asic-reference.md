# Bitmain BM13xx ASIC Reference

> Sources: 256foundation/mujina BM13xx chip reference (REFERENCE.md, captured 2026-10-07) and mujina pull requests, 2026; OSMU wiki OSMU Lab chip pages (captured 2026-10-07); bitaxeorg hardware READMEs and issues, 2022 → 2026; bitaxeorg/ESP-Miner GitHub issues and releases, 2023-01 → 2026-10; Undermine 2025 / HPS 2026 summit recordings (auto-caption transcripts)
> Raw: [Mujina BM13xx reference](../../raw/firmware/mujina/github-mujina-mujina-miner-src-asic-bm13xx-reference.md); [OSMU wiki: BM1370](../../raw/hardware/bitaxe-osmu/osmu-wiki-osmu-lab-bm1370.md); [OSMU wiki: BM1366](../../raw/hardware/bitaxe-osmu/osmu-wiki-osmu-lab-bm1366.md); [bitaxeMax README](../../raw/hardware/bitaxe-osmu/github-bitaxeorg-bitaxemax.md); [bitaxeGamma README](../../raw/hardware/bitaxe-osmu/github-bitaxeorg-bitaxegamma.md); [ESP-Miner #248](../../raw/firmware/esp-miner/2024-07-02-github-esp-miner-issue-248-determine-proper-job-interval-for.md); [Undermine 2025 ASIC frontier](../../raw/history/heatpunks-summit/20251111-undermine-2025-the-bitcoin-asic-frontier.md); [Undermine 2025 heat-reuse panel](../../raw/history/heatpunks-summit/20251111-undermine-2025-exploring-the-heat-reuse-potential-of-bitcoin-mining.md); [HPS 2026 Chips on the Table (Talk 6)](../../raw/history/heatpunks-summit/2026/20260303-hps-2026-chips-on-the-table-home-mining-hardware-asics-talk-6.md); [Bitmain S23 XP Hyd. spec table](../../raw/hardware/bitmain/2026-10-10-bitmain-site-s23-xp-hyd.md); [Bitmain S23e U2H spec table](../../raw/hardware/bitmain/2026-10-10-bitmain-site-s23e-u2h.md); [Bitmain S21 XP+ Hyd. spec table](../../raw/hardware/bitmain/2026-10-10-bitmain-site-s21-xp-plus-hyd.md); [Bitmain S21 XP Hyd. spec table](../../raw/hardware/bitmain/2026-10-10-bitmain-site-s21-xp-hyd.md); [Bitmain S21 XP spec table](../../raw/hardware/bitmain/2026-10-10-bitmain-site-s21-xp.md); [Bitmain live catalog snapshot](../../raw/hardware/bitmain/2026-10-10-bitmain-site-product-catalog.md); [AMV Bitmain snapshot](../../raw/hardware/asicminervalue/2026-10-10-asicminervalue-bitmain.md); [MiningNow Bitmain snapshot](../../raw/hardware/miningnow/2026-10-10-miningnow-bitmain.md)
> Updated: 2026-10-10
> As-Of: 2026-10-10
> Status: Draft

## Overview

Bitmain's BM13xx chips are the SHA-256 mining ASICs inside Antminers (S9 → S17 → S19 → S21 generations) and, pulled individually, inside every Bitaxe and most open-source home miners. Bitmain publishes no documentation for them: everything known comes from reverse engineering, the OSMU Lab pages on the OSMU wiki, Skot's early BM1387/BM1397 work, the ESP-Miner driver code and issue tracker, and, most completely, the Mujina project's BM13xx chip reference. The Mujina reference was built from factory firmware and serial captures of a Bitaxe Gamma, an S21 Pro, an S19j Pro, an S19k Pro and an S19 XP ([Mujina BM13xx reference](../../raw/firmware/mujina/github-mujina-mujina-miner-src-asic-bm13xx-reference.md); [OSMU Lab about](../../raw/hardware/bitaxe-osmu/osmu-wiki-osmu-lab-about.md)). All chips speak the same framed UART protocol and are designed to be daisy-chained. The host assigns addresses, sets the PLL clock, splits the nonce space between chips with registers, and then broadcasts jobs. The chips return nonces that pass a ticket-mask filter. This page collects the published specs (including the figures sources disagree on), pinouts, the frame format, the register map, the nonce and version-rolling math, and the practical failure modes builders keep hitting: duplicate shares, PLL gaps, bad temperature readings and dead hash domains.

## Chip lineup and published specs

All efficiency numbers below are Bitmain claims relayed by community docs, or community estimates. None comes from a Bitmain datasheet.

| Chip | Antminer host | Efficiency claimed | Price (small qty) | Bitaxe board | Notes |
|---|---|---|---|---|---|
| BM1387 | S9 | 0.098j/Gh | around $1-2 each (AliExpress) | first bitaxe prototype (2 chips) | 1.8V serial, inverted reset ([BM1387 prototype README](../../raw/hardware/bitaxe-osmu/2022-05-26-bitaxe-bm1387-prototype-readme.md)) |
| BM1397 | S17 / T17 | 0.03J/GH | ~$20 new, ~$6 used | Max (100) | UART at 115200bps default, up to 6Mbps ([OSMU wiki: BM1397](../../raw/hardware/bitaxe-osmu/osmu-wiki-osmu-lab-bm1397.md); [bitaxeMax README](../../raw/hardware/bitaxe-osmu/github-bitaxeorg-bitaxemax.md)) |
| BM1362 | S19j Pro | 29.4J/TH | ~$5 new, ~$1 used | (EmberOne00, 12 chips) | 65 cores × 8 sub-cores ([OSMU wiki: BM1362](../../raw/hardware/bitaxe-osmu/osmu-wiki-osmu-lab-bm1362.md); [Mujina BM13xx reference](../../raw/firmware/mujina/github-mujina-mujina-miner-src-asic-bm13xx-reference.md)) |
| BM1366 | S19 XP, S19k Pro | disputed (below) | disputed (below) | Ultra (200), Ultra Hex (300) | 112 cores × 8 sub-cores; no die-temp diode |
| BM1368 | S21 | 17.5 J/TH (Supra README); ~18J/TH (OSMU) | ~$25 new, ~$15 used | Supra (400) | nominal 600~750GH/s; 16 sub-cores per core ([OSMU wiki: BM1368](../../raw/hardware/bitaxe-osmu/osmu-wiki-osmu-lab-bm1368.md); [bitaxeSupra README](../../raw/hardware/bitaxe-osmu/github-bitaxeorg-bitaxesupra.md)) |
| BM1370 | S21 Pro | 15 J/TH | unknown (pulled from S21 Pro at launch) | Gamma (600), Gamma Duo (650), GT (801), Gamma Hex (1300) | nominal 1~1.4TH/s; 128 cores × 16 sub-cores ([OSMU wiki: BM1370](../../raw/hardware/bitaxe-osmu/osmu-wiki-osmu-lab-bm1370.md); [bitaxeGamma README](../../raw/hardware/bitaxe-osmu/github-bitaxeorg-bitaxegamma.md)) |
| BM1340 | suspected S23-series prototype | — | — | BitaxeNaja (dual, untested) | ([BitaxeNaja README](../../raw/hardware/bitaxe-osmu/github-bitaxeorg-bitaxenaja.md)) |
| BM1372 / BM1373 | BM1373 suspected S23-series ASIC | — | — | Naja Duo (1201, dual) | default 327 MHz ([NajaDuo README](../../raw/hardware/bitaxe-osmu/github-bitaxeorg-naja-duo.md); [ESP-Miner #1902](../../raw/firmware/esp-miner/2026-08-21-github-esp-miner-issue-1902-axeos-reports-normal-bm1372-bm13.md)) |

The Gamma README's sizing math: the S21 Pro is nominally 234 TH/s from 3 hashboards of 65 chips (195 chips), so one chip gives "about" 1.2 TH/s. Bitmain's 15 J/TH claim is one the Gamma "can get pretty close" to ([bitaxeGamma README](../../raw/hardware/bitaxe-osmu/github-bitaxeorg-bitaxegamma.md)). At stock settings (525 MHz, 1.15V), Mujina's board doc puts a Gamma at approximately 1 TH/s ([Mujina: Bitaxe Gamma board](../../raw/firmware/mujina/github-mujina-mujina-miner-src-board-bitaxe-gamma.md)).

**Process node:** none of the captured sources states the process node of the BM13xx chips covered here. The only node on record is the earlier S19 Pro's BM1398 (7nm, 500 MHz, 114 chips per board, 110 TH/s), from Mujina's factory-test notes ([Mujina xilinx test fixture](../../raw/firmware/mujina/github-mujina-xilinx-platform-br2-external-bitmain-board-xil-2.md)). On the Undermine 2025 ASIC-frontier panel, the panelists put the industry's bleeding edge at 3 nanometer, with 2 nanometer "not too too long from now", and staying there "costs tens of millions of dollars" per generation ([00:06:57] [Undermine 2025 ASIC frontier](../../raw/history/heatpunks-summit/20251111-undermine-2025-the-bitcoin-asic-frontier.md)). They also cautioned that the node names themselves are "marketing terms": "they can't shrink it anymore they're doing other tricks" to deliver next-node performance without shrinking the transistor ([00:26:52] [Undermine 2025 ASIC frontier](../../raw/history/heatpunks-summit/20251111-undermine-2025-the-bitcoin-asic-frontier.md)).

> **Status: Disputed** (BM1366 efficiency, price, host machines)
> The Ultra README and Ultra prototype README cite Bitmain's 0.021J/GH and about $15 new ([bitaxeUltra README](../../raw/hardware/bitaxe-osmu/github-bitaxeorg-bitaxeultra.md); [Ultra prototype README](../../raw/hardware/bitaxe-osmu/2023-07-20-bitaxe-ultra-prototype-readme.md)). The ultraHex README says Bitmain claims 21.5 W/TH ([ultraHex README](../../raw/hardware/bitaxe-osmu/github-bitaxeorg-ultrahex.md)). The OSMU Lab page lists 25J/TH and ~$25 new / ~$15 used, and calls the chip "mostly used in the Antminer S19", where the READMEs say S19XP and S19k Pro ([OSMU wiki: BM1366](../../raw/hardware/bitaxe-osmu/osmu-wiki-osmu-lab-bm1366.md)). Best assessment: 0.021J/GH and 21.5 W/TH are the same order of Bitmain claim, while 25J/TH reads as a looser community figure. The price spread probably reflects different capture dates. Mujina's captures confirm the S19 XP and S19k Pro as BM1366 hosts ([Mujina BM13xx reference](../../raw/firmware/mujina/github-mujina-mujina-miner-src-asic-bm13xx-reference.md)).

> **Status: Disputed** (BM1370 footprint)
> The OSMU wiki says the BM1370 has a similar footprint and pinout to the BM1368 ([OSMU wiki: Bitaxe 600](../../raw/hardware/bitaxe-osmu/osmu-wiki-bitaxe-600.md)). The Gamma README says it differs from the BM1368, BM1366, BM1397 and BM1387 ([bitaxeGamma README](../../raw/hardware/bitaxe-osmu/github-bitaxeorg-bitaxegamma.md)). The pin tables agree on signal names, but the BM1370 adds numbered pins with ROSC_SEL and LITE_PAD at pins 10/11 ([OSMU wiki: BM1370](../../raw/hardware/bitaxe-osmu/osmu-wiki-osmu-lab-bm1370.md)). Best assessment: the two chips share signals but are not drop-in footprint-compatible. Lay out from the BM1370 footprint itself. The Gamma footprint was itself corrected in 2025 (see Board-level errata).

### Typical operating points seen in Bitaxe firmware

| Chip | Default frequency / core voltage | Source |
|---|---|---|
| BM1397 (Max) | 475 MHz / 1400 mV (also a 425 MHz v1.0 build) | [ESP-Miner #113](../../raw/firmware/esp-miner/2024-02-23-github-esp-miner-issue-113-firmware-v2-0-7-may-have-bm1397-r.md); [firmware release records](../../raw/hardware/bitaxe-osmu/bitaxe-firmware-release-records.md) |
| BM1366 (Ultra) | 485 MHz / 1320 mV | [firmware release records](../../raw/hardware/bitaxe-osmu/bitaxe-firmware-release-records.md) |
| BM1368 (Supra) | 490 MHz / 1166 mV (early units shipped at 1200) | [ESP-Miner #153](../../raw/firmware/esp-miner/2024-03-27-github-esp-miner-issue-153-query-bm1368-default-voltage.md) |
| BM1370 (Gamma) | 525MHz/1150mV (stock cooler cannot reliably hold more than 525MHz @ 1100mV) | [ESP-Miner #369](../../raw/firmware/esp-miner/2024-09-30-github-esp-miner-issue-369-lower-the-default-hash-frequency.md) |
| BM1372/BM1373 (Naja Duo) | 327 MHz; options 327, 350, 375, 380, 400, 410 MHz | [ESP-Miner #1902](../../raw/firmware/esp-miner/2026-08-21-github-esp-miner-issue-1902-axeos-reports-normal-bm1372-bm13.md) |

Core voltage is per chip. Boards stack chips in series voltage domains. An S17 feeds about 20V to roughly 13 chips in series so each sees about 1.5V ([ESP-Miner #3](../../raw/firmware/esp-miner/2023-01-21-github-esp-miner-issue-3-adc-is-using-deprecated-driver-need.md)). The BM1366 wants a 1.2V core, so three in series on the Ultra Hex need a 3.6V regulator output ([ultraHex #11](../../raw/hardware/bitaxe-osmu/2023-11-25-github-ultrahex-issue-11-change-nominal-tps40305-output-to-3.md)). The two-chip BM1387 prototype ran both chips in series from a VIN of about 1.6V ([BM1387 prototype README](../../raw/hardware/bitaxe-osmu/2022-05-26-bitaxe-bm1387-prototype-readme.md)).

## Pinouts

**BM1387 / BM1397.** The BM1397 shares the BM1387 footprint but has a very different pinout ([bitaxeMax README](../../raw/hardware/bitaxe-osmu/github-bitaxeorg-bitaxemax.md)). It has two pin "modes" that rearrange signal pins for daisy-chaining. The mode pin swaps which side the data input and output pins sit on, which simplifies PCB routing, and ESP-Miner does not care which mode the chip is in ([OSMU wiki: BM1397](../../raw/hardware/bitaxe-osmu/osmu-wiki-osmu-lab-bm1397.md); [ESP-Miner #31](../../raw/firmware/esp-miner/2023-09-10-github-esp-miner-issue-31-support-bm1397-in-mode-1.md)). Serial I/O on the BM1397 and BM1366 is 1.8V, so Bitaxe boards level-shift to the 3.3V ESP32 ([BM1397 platform README](../../raw/hardware/bitaxe-osmu/2023-05-11-bitaxe-bm1397-platform-readme.md); [Ultra prototype README](../../raw/hardware/bitaxe-osmu/2023-07-20-bitaxe-ultra-prototype-readme.md)).

**BM1366 / BM1368.** These chips have a different footprint from the BM1397/BM1387, and the BM1368 differs again from the BM1366 ([bitaxeUltra README](../../raw/hardware/bitaxe-osmu/github-bitaxeorg-bitaxeultra.md); [bitaxeSupra README](../../raw/hardware/bitaxe-osmu/github-bitaxeorg-bitaxesupra.md)). OSMU Lab lists the same signal set for both, and the BM1368 adds temperature-diode pins ([OSMU wiki: BM1366](../../raw/hardware/bitaxe-osmu/osmu-wiki-osmu-lab-bm1366.md); [OSMU wiki: BM1368](../../raw/hardware/bitaxe-osmu/osmu-wiki-osmu-lab-bm1368.md)):

| Signal (in / out) | Function |
|---|---|
| NRSTI / NRST0 | reset in / out (chained) |
| CI / CO | serial command in / out (toward the far end of the chain) |
| RI / RO | serial response in / out (toward the host) |
| BI / BO | busy in / out (response arbitration) |
| CLKI / CLK0, INV_CLK0 | clock in / out; inverted clock output (use unknown) |
| ADDR0 / ADDR1 | address pins, function unknown |
| PIN_MODE | pin-mode selector (mode0/mode1 BOM parts are the same ASIC) |
| VDD1/2/3_x | three internal voltage domains, for bypass capacitors |
| VDDIO_08 / VDDIO_18 | 0.8V IO and "1.8V" IO rails (the latter normally 1.2V now) |
| TEMP_P / TEMP_N | temperature diode (BM1368 only) |

The Ultra Hex BOM's "mode0" and "mode1" BM1366 parts are the same ASIC. PIN_MODE selects which side of the chip the inputs and outputs are on, and separate schematic symbols keep pin names matched ([ultraHex #49](../../raw/hardware/bitaxe-osmu/2025-06-25-github-ultrahex-issue-49-bm1366-mode-versions.md)).

**BM1370 (32 pins).** Pins 1–3 and 28–30 are the VDD3/2/1 bypass domains. Then come 4 VSS, 5 NRSTI, 6 CI, 7 RO, 8 CLKI, 9 BI, 10 ROSC_SEL, 11 LITE_PAD, 12 INV_CLK0, 13 PLL_VSS, 14/17 0.8V IO, 15/16 1.2V IO, 18 VSS, 19 PIN_MODE, 20/21 TEMP_P/TEMP_N, 22 BO, 23 CLK0, 24 RI, 25 CO, 26 NRST0, 27/32 VSS and 31 VDD ([OSMU wiki: BM1370](../../raw/hardware/bitaxe-osmu/osmu-wiki-osmu-lab-bm1370.md)).

## Serial protocol

### Link and chain

- **Baud.** Chips come out of reset at 115,740 baud (UART_BAUD 0x28 divider 26). Baud = 25 MHz / (8 × (divider + 1)). The host broadcasts a new divider once, waits for the write to drain at the old rate, then switches its own UART. In the captures, the S19j Pro and S21 Pro chains mine at 3,125,000 baud (divider 0) and the Bitaxe at 1,041,667 (divider 2) ([Mujina BM13xx reference](../../raw/firmware/mujina/github-mujina-mujina-miner-src-asic-bm13xx-reference.md)). Older docs describe the BM1397 as 115200bps by default, up to 6Mbps ([bitaxeMax README](../../raw/hardware/bitaxe-osmu/github-bitaxeorg-bitaxemax.md)).
- **Baud-change race.** Switching the ESP32 UART before the baud command finishes sending leaves the chip at the old rate, and it looks like a chip that finds no nonces. ESP-Miner added a 1ms delay for the BM1397 ([ESP-Miner #18](../../raw/firmware/esp-miner/2023-08-26-github-esp-miner-issue-18-local-baudrate-change-too-soon.md)). A similar post-baud-change race on the Supra was caught with an ASIC-count sanity check ([ESP-Miner #511](../../raw/firmware/esp-miner/2024-11-23-github-esp-miner-issue-511-ultra-does-not-start-hashing.md)).
- **Topology.** Commands and clock flow away from the host chip to chip, and responses flow back. A busy signal (BI/BO) arbitrates the shared response path. Chips in one voltage domain sit in parallel, and domains stack in series. Two registers configure boundary crossings: UART_RELAY (0x2C) and IO_DRIVER_STRENGTH (0x58). The S21 Pro's 65 BM1370s form 13 domains of five. Stock firmware raises only the clock-output drive (CLKO_DS = 0xF) on the last chip of each domain and writes UART_RELAY gap counts falling from 0x4F to 0x13 along the chain. The S19j Pro's 126 BM1362s form 42 domains of three, and its firmware configures neither boundary register ([Mujina BM13xx reference](../../raw/firmware/mujina/github-mujina-mujina-miner-src-asic-bm13xx-reference.md)).
- **Reset wiring.** The Ultra Hex briefly tried parallel reset within each domain, then reverted to Bitmain-style serial passthrough reset ([ultraHex #37](../../raw/hardware/bitaxe-osmu/2024-05-15-github-ultrahex-issue-37-reset-signals-connected-in-parallel.md)).

### Frame format

| Direction | Layout | CRC |
|---|---|---|
| Command (host → chip) | `55 AA` · Type/Flags · Length · payload · CRC | CRC5 (1 byte) for register ops, CRC16 (2 bytes, MSB first) for jobs |
| Response (chip → host) | `AA 55` · payload · CRC byte | response type in bits 7-5, CRC5 in bits 4-0 |

Type/Flags packs TYPE in bits 6-5 (2 = register ops, 1 = job), BROADCAST in bit 4, and CMD in bits 3-0. Common values are 0x40 set address, 0x41/0x51 write register (single/broadcast), 0x42/0x52 read register (0x52 = chip discovery), 0x53 chain inactive, and 0x21 send job. Register values go MSB first. Header fields (version, nbits, ntime, starting nonce, returned nonce) go in the header's little-endian serialization. Merkle root and prev-block hash go with their eight 4-byte words reversed ([Mujina BM13xx reference](../../raw/firmware/mujina/github-mujina-mujina-miner-src-asic-bm13xx-reference.md)).

Responses have no length field and are fixed-size. The format is 11 bytes once version rolling is enabled through MIDSTATE_CONFIG (0xA4), and 9 bytes from a freshly reset chip. The BM1397 always sends the 9-byte nonce response with no version field ([Mujina BM13xx reference](../../raw/firmware/mujina/github-mujina-mujina-miner-src-asic-bm13xx-reference.md)).

### CRC5 and CRC16

- **CRC5:** polynomial 0x05, initial value 0x1F, no output XOR, no reflection. It covers everything after the preamble, including the response's three type bits. **CRC16:** CRC-16-CCITT-FALSE (poly 0x1021, init 0xFFFF) for job frames ([Mujina BM13xx reference](../../raw/firmware/mujina/github-mujina-mujina-miner-src-asic-bm13xx-reference.md)). Mujina replaced a third-party crate with inline CRC-5-USB and CRC-16-CCITT-FALSE, tested exhaustively over all one- and two-byte inputs ([Mujina PR #103](../../raw/firmware/mujina/2026-08-21-github-mujina-pr-103-chore-deps-replace-crc-all-with-inline.md)).
- **Validation trick:** a byte-aligned CRC5 over the whole buffer, including the CRC5 byte, yields 0x00. Computing a CRC5 needs a bit-aligned algorithm (a reference Rust implementation is in bm13xx-rs) ([ESP-Miner #740](../../raw/firmware/esp-miner/2025-02-27-github-esp-miner-issue-740-look-for-correct-chip-id-response.md)). ESP-Miner originally got nonce-response CRC5 wrong by including the CRC bits. The fix excludes the preamble and CRC bits, and checking CRC lets firmware skip SHA-256 verification of corrupted results ([ESP-Miner #395](../../raw/firmware/esp-miner/2024-10-09-github-esp-miner-issue-395-how-to-handle-crc5-from-asic-mess.md)).
- **Resync:** fixed-length framing can lose the `aa 55` header. A logic-analyzer capture showed a BM1368 occasionally sending one extra byte, so ESP-Miner now flushes the buffer after any invalid frame ([ESP-Miner #268](../../raw/firmware/esp-miner/2024-08-05-github-esp-miner-issue-268-firmware-2-1-9-stops-working-afte.md); [ESP-Miner #24](../../raw/firmware/esp-miner/2023-09-03-github-esp-miner-issue-24-serial-synchronization.md)). Cheap logic analyzers usually can't keep up at full speed. A BM1397 Saleae analyzer exists (GPTechinno/bm13xx-hla) ([ESP-Miner #4](../../raw/firmware/esp-miner/2023-02-27-github-esp-miner-issue-4-bm1397-protocol-md.md)).

### Discovery and chip addressing

1. Broadcast-read CHIP_ID (0x00) with `55 AA 52 05 00 00 0A`. Each chip answers with its model bytes, for example `13 70` on the BM1370 and `13 62` on the BM1362 ([Mujina BM13xx reference](../../raw/firmware/mujina/github-mujina-mujina-miner-src-asic-bm13xx-reference.md)). Count only correctly formed replies (`AA 55 13 66 ...`, `AA 55 13 68 ...`, `AA 55 13 70 ...`) with valid checksums, and compare against the expected chip count ([ESP-Miner #740](../../raw/firmware/esp-miner/2025-02-27-github-esp-miner-issue-740-look-for-correct-chip-id-response.md)).
2. Broadcast ChainInactive (`55 AA 53 05 00 00 03`). Every chip enters addressing mode.
3. Send SetChipAddress (0x40) repeatedly. The first unaddressed chip takes the address, and addressed chips forward later commands down the chain. Addresses typically step by 2 (factory S21 Pro: 0x00 to 0x80) ([Mujina BM13xx reference](../../raw/firmware/mujina/github-mujina-mujina-miner-src-asic-bm13xx-reference.md)).

On the BM1362/BM1366, the address doubles as the high bits of the chip's starting nonce, so two chips should get 0x00 and 0x80 ([ESP-Miner #56](../../raw/firmware/esp-miner/2023-11-12-github-esp-miner-issue-56-bm1366-won-t-change-chip-address.md)). The byte after the core-number field in a CHIP_ID reply is the chip address, which stays 0 until software assigns one ([ESP-Miner #740](../../raw/firmware/esp-miner/2025-02-27-github-esp-miner-issue-740-look-for-correct-chip-id-response.md)). On cold boards, Mujina's Windows port waits 500ms after ASIC reset and retries BM1370 discovery up to 5× ([Mujina PR #76](../../raw/firmware/mujina/2026-07-05-github-mujina-pr-76-feat-native-windows-support-for-bitaxe-m.md)).

### Jobs and nonce responses

- **Full format (BM1362/66/68/70):** the chip computes its own midstates. An 88-byte frame carries the job_header (job id), num_midstates (always 0x01), starting_nonce, nbits, ntime, merkle_root, prev_block_hash and version. Factory firmware sends length byte 0x36, ESP-Miner sends the true 0x56, and the BM1370 accepts both ([Mujina BM13xx reference](../../raw/firmware/mujina/github-mujina-mujina-miner-src-asic-bm13xx-reference.md)).
- **Midstate format (BM1397 and older):** the host precomputes 1-4 midstates, 32 bytes each ([Mujina BM13xx reference](../../raw/firmware/mujina/github-mujina-mujina-miner-src-asic-bm13xx-reference.md)). ESP-Miner can skip midstate prep for the BM1366/1368/1370. Midstates also cannot verify shares on version-rolled headers, because the version bytes sit in the first SHA block ([ESP-Miner #1507](../../raw/firmware/esp-miner/2026-01-14-github-esp-miner-issue-1507-skip-midstates-for-bm1366-1368-1.md)).
- **Nonce response (TYPE=4, 11 bytes):** nonce · excess-difficulty · result header · rolled version (2 bytes) · CRC5+type. The result header echoes the job id, so the host can discard stale-job nonces after a new block. The BM1370 uses a 4-bit job id and a 4-bit sub-core id. The BM1362 splits it 5+3. On the BM1370, the nonce's top 7 bits name the finding core and the low 25 bits are a counter seeded from CHIP_NONCE_OFFSET. On the BM1362/BM1366, the nonce carries core ID, chip address bits 7-1 and an 18-bit sweep counter. The excess-difficulty byte reports how far the hash beat the ticket mask in half-bit log2 steps. The 16 rolled bits map into header version bits 28-13 ([Mujina BM13xx reference](../../raw/firmware/mujina/github-mujina-mujina-miner-src-asic-bm13xx-reference.md)).
- ASIC nonce messages are 11 bytes. Early ESP-Miner discarded a one-byte-misaligned read along with its whole 1024-byte buffer, losing potentially many messages ([ESP-Miner #350](../../raw/firmware/esp-miner/2024-09-25-github-esp-miner-issue-350-consolidation-of-serial-comms-iss.md)).

## Register map

From the Mujina reference unless noted ([Mujina BM13xx reference](../../raw/firmware/mujina/github-mujina-mujina-miner-src-asic-bm13xx-reference.md)):

| Reg | Name | What it does / key values |
|---|---|---|
| 0x00 | CHIP_ID | model bytes + unknown byte (0x00 on BM1370, 0x03 on BM1362) + address |
| 0x08 | PLL_DIVIDER | hash clock = fb_div × 25 MHz / (ref_div × post_div1 × post_div2); bit 31 lock readback, bit 28 VCOSEL (set at/above 2400 MHz VCO) |
| 0x0C | CHIP_NONCE_OFFSET | BM1370 per-chip sweep start (offset << 9); the S21 Pro writes it per chip, the S19j Pro never does |
| 0x10 | HASH_COUNTING_NUMBER (HCN) | sweep deadline in 25 MHz crystal ticks, not a nonce count; zero halts hashing |
| 0x14 | TICKET_MASK | reporting filter `hash & mask == 0` on top of 32 hardwired zero bits; per-byte bit-reversed on the wire (difficulty 256 → `00 00 00 FF`, 1024 → `00 00 C0 FF`) |
| 0x18 | MISC_CONTROL | "open core" report enables; BM1370 bits 28-31 gate core quarters 0-31/32-63/64-95/96-127; constants 0xB000C100 (BM1362), 0xFF0FC100 / 0xF000C100 (BM1366/68), 0xF000C100 (BM1370). On the BM1397 this register held the baud divider instead |
| 0x28 | UART_BAUD | divider in bits 15-8; reset value 0x01301A00 |
| 0x2C | UART_RELAY | per-domain relay enables + gap count on boundary chips |
| 0x3C | CORE_MAILBOX | indirect per-core registers: clock delay, core enable 0xAA, clock select, BM1370 nonce-bin overflow 0xEE |
| 0x54 | ANALOG_MUX | select 2 = temperature-diode readout (BM1370 production), 3 = default |
| 0x58 | IO_DRIVER_STRENGTH | 4-bit drive per output (RO, CLKO, NRSTO, BO, CO) |
| 0x68 | RING_OSC_PAD_DISABLE | guard pattern 0x5AA55AA5; written by BM1368/BM1370 only |
| 0xA4 | MIDSTATE_CONFIG | version rolling: bit 31 auto, bits 29-28 midstate count code, bits 15-0 rollable mask (pool mask >> 13: 0x1FFFE000 → 0xFFFF); every host writes 0x9000FFFF |
| 0xA8 | SOFT_RESET_CONTROL | first appears with the BM1362; BM1366/68/70 reset default 0x00070000, core reset 0x000701F0 |
| 0xB0–0xBD | on-die telemetry | BM1368/BM1370 voltage ADC; BM1368 temperature sensor |

ESP-Miner history around these registers:

- The BM1366 originally used a hardcoded version mask 0x1fffe000 instead of the pool-negotiated mask written to register A4 ([ESP-Miner #54](../../raw/firmware/esp-miner/2023-11-03-github-esp-miner-issue-54-fix-hardcoded-version-mask-on-bm13.md)).
- ESP-Miner hardcodes `version-rolling.mask` 0xFFFFFFFF in mining.configure. adammwest gave max roll = 65536/midstates and version mask = 65536<<13 for the BM13xx chips. A tested branch clamped the advertised mask to `1fffe000` for the BM1366/BM1368/BM1370 and left the BM1397 unchanged ([ESP-Miner #1169](../../raw/firmware/esp-miner/2025-07-25-github-esp-miner-issue-1169-hardcoded-version-rolling-mask-m.md)).
- skot's position: keep the ticket mask static and much lower than pool difficulty ([ESP-Miner #314](../../raw/firmware/esp-miner/2024-08-30-github-esp-miner-issue-314-add-current-pool-minimum-difficul.md)).
- v2.15.2 changed the BM1370 init sequence. ClockDelayCtrl (0x3C) went from `80 00 80 0C` to `80 00 80 10`. The release added a broadcast write of `00 00 00 FF` to 0x14, a `5A A5 5A A5` write to 0x68, Analog Mux 0x54 = `00 00 00 03`, and inter-write delays. One Gamma 601 then left one or two hash domains at 0 GH/s on every boot. The ClockDelayCtrl change is suspected but was not bisected (open as of the 2026-10-07 capture) ([ESP-Miner #2019](../../raw/firmware/esp-miner/2026-10-07-github-esp-miner-issue-2019-bm1370-gamma-601-v2-15-2-leaves.md)).

## PLL and frequency tables

The PLL multiplies the 25 MHz reference: VCO = fb_div × 25 MHz / ref_div, then two post dividers. Per-model limits ([Mujina BM13xx reference](../../raw/firmware/mujina/github-mujina-mujina-miner-src-asic-bm13xx-reference.md); [ESP-Miner #1044](../../raw/firmware/esp-miner/2025-06-17-github-esp-miner-issue-1044-pll-lookup-table-investigation.md)):

| Model | fb_div (Mujina, hex) | fb_divider (ESP-Miner, decimal) | VCO range |
|---|---|---|---|
| BM1362 | 0x10-0xFA | — | 2000-3200 MHz |
| BM1366 / BM1368 | 0x90-0xEB | 144 to 235 | unknown |
| BM1370 | 0xA0-0xEF | 160 to 239 | 1600-3200 MHz |

- **Pick the lowest VCO.** mutatrum enumerated every divider combination and found 2424 unique frequencies. When several combinations hit the same clock, prefer the lower-VCO one because it draws less power. For example, fb_divider=168 refdiv=2 postdiv1=2 postdiv2=2 gives a VCO of 2100Mhz, versus fb_divider=189 refdiv=1 postdiv1=3 postdiv2=3 at 4725MHz. A BM1370 solver rewrite that searched for the smallest refdiv dropped one miner to 15 watts from 16.5. Frequency became a float setting ([ESP-Miner #1044](../../raw/firmware/esp-miner/2025-06-17-github-esp-miner-issue-1044-pll-lookup-table-investigation.md)).
- **Gaps above 750 MHz.** Not every frequency above 750 MHz locks. Skot explained: "Due to the overlap of the two PLL registers on the ASIC, not all frequencies will be available". Chips can still ramp well over 1 GHz ([ESP-Miner #648](../../raw/firmware/esp-miner/2025-01-11-github-esp-miner-issue-648-unable-to-set-all-available-frequ.md)). Startup messages about unfound BM1370 frequencies above 750 MHz do not mean the clock is capped ([bitaxeGamma #21](../../raw/hardware/bitaxe-osmu/2025-01-11-github-bitaxegamma-issue-21-failure-to-find-select-pll-frequ.md)).
- v2.4.0 changed the BM1370 MHz settings to a 6.25 multiplier ([ESP-Miner releases](../../raw/firmware/esp-miner/github-esp-miner-releases.md)). The single-frequency command is shared across chips, which is why a BM1368 function once drove every model until it was split per ASIC ([ESP-Miner #575](../../raw/firmware/esp-miner/2024-12-12-github-esp-miner-issue-575-bm1368-send-hash-frequency-is-cal.md)).

## Nonce space, version rolling and HCN

**Search space.** One job is 2^32 nonces × 2^16 rolled versions (BIP320) = 2^48 headers. A BM1370 at 600 MHz (about 1.2 TH/s) would exhaust the bare nonces in under 4 ms. Version rolling stretches that to about four minutes ([Mujina BM13xx reference](../../raw/firmware/mujina/github-mujina-mujina-miner-src-asic-bm13xx-reference.md)). The BM1366 prototype README already noted the chip "appears to roll more than just the nonce", allowing longer chains and less frequent work ([Ultra prototype README](../../raw/hardware/bitaxe-osmu/2023-07-20-bitaxe-ultra-prototype-readme.md)).

**Parallel hierarchy.** Chips sweep disjoint nonce slices, set by address on the BM1362/BM1366 and by CHIP_NONCE_OFFSET on BM1370 chains. Cores split the chip's slice by a core-ID field in the nonce. Each sub-core of a core hashes the same nonces with its own rolled version. A BM1370 (16 sub-cores) therefore covers all 2^16 versions in 4,096 sweeps, and the BM1362/BM1366 (8 sub-cores) take 8,192. Chips report their model, not their geometry, so firmware hard-codes the core tables ([Mujina BM13xx reference](../../raw/firmware/mujina/github-mujina-mujina-miner-src-asic-bm13xx-reference.md)).

**Unused nonce space on partial-core chips.** The BM1366 has 112 of 128 core slots, so its highest nonce is 0xDFFFFFFF. The BM1368 (80 cores) tops out at 0x9FFFFFFF. The BM1370 has the full 128. Sweeping past the available space wastes time on single-chip miners and causes duplicates on multi-chip ones ([ESP-Miner #939](../../raw/firmware/esp-miner/2025-05-20-github-esp-miner-issue-939-custom-nonce-and-extra-nonce-rang.md)). On the BM1370 a starting nonce can be set through the job or the CNO register. On the BM1362/66/68 only HCN (0x10) sets the range ([ESP-Miner #939](../../raw/firmware/esp-miner/2025-05-20-github-esp-miner-issue-939-custom-nonce-and-extra-nonce-rang.md)).

**Computing HCN** (ESP-Miner PR #420, documented in Mujina) ([Mujina BM13xx reference](../../raw/firmware/mujina/github-mujina-mujina-miner-src-asic-bm13xx-reference.md)):

```text
cores_up = next_power_of_two(cores_per_chip)
chips_up = next_power_of_two(chain_length)
slice    = 2^32 / cores_up / chips_up
hcn      = floor(slice * refdiv * postdiv1 * postdiv2 / (2 * fbdiv))   # integer form
```

Round down, and subtract a 200-tick guard because the sweep overruns its deadline by about 130 ticks. Recompute on every frequency change. Stock firmware deliberately undershoots: factory HCN covers 80% of each slice on the S19j Pro and 73% on the S21 Pro ([Mujina BM13xx reference](../../raw/firmware/mujina/github-mujina-mujina-miner-src-asic-bm13xx-reference.md)).

**Version epoch.** An epoch is the time to roll all 2^16 versions: epoch = (2^16 / sub_cores_per_core) × hcn / 25 MHz. Past one epoch the chip silently re-hashes the same headers and gives no done signal, so the host must replace work within an epoch. Factory values ([Mujina BM13xx reference](../../raw/firmware/mujina/github-mujina-mujina-miner-src-asic-bm13xx-reference.md)):

| Machine | Chip | hcn | Epoch |
|---|---|---|---|
| Antminer S21 | BM1368 | 0x15A4 | 0.91 s |
| Antminer S21 Pro | BM1370 | 0x1EB5 | 1.29 s |
| Antminer S19k Pro | BM1366 | 0x115A | 1.46 s |
| Antminer S19j Pro | BM1362 | 0x1381 | 1.64 s |
| Antminer S19 XP | BM1366 | 0x151C | 1.77 s |

Field measurements on Bitaxes:

- An S19XP with 110 chips uses a 2.14s job interval, while an old ESP-Miner formula produced a far-too-short "ASIC Job Interval: 9.91 ms" ([ESP-Miner #248](../../raw/firmware/esp-miner/2024-07-02-github-esp-miner-issue-248-determine-proper-job-interval-for.md)).
- On a Supra, wrap-around time was 1860ms at both 525Mhz and 600Mhz, and 1.86 at 490 and 420 mhz ([ESP-Miner #514](../../raw/firmware/esp-miner/2024-11-24-github-esp-miner-issue-514-feature-don-t-calculate-asic-job.md)).
- A Gamma's nonce space takes about 2.8 seconds, against a 500ms single-chip job timeout ([ESP-Miner #1587](../../raw/firmware/esp-miner/2026-03-02-github-esp-miner-issue-1587-esp-miner-is-unable-to-handle-di.md)).

**Across multiple chains** the host must deduplicate work by one of these methods: disjoint extranonce2 slices, ntime offsets, separate upstream connections, nonce division extended across chains, or fixed version bits (draft BIP323 widens rollable bits to 24). SV2 header-only mining has no extranonce ([Mujina BM13xx reference](../../raw/firmware/mujina/github-mujina-mujina-miner-src-asic-bm13xx-reference.md)). Mujina's SV2 work notes a 280TH/s theoretical limit for standard-channel header-only mining, smaller still with sniffed Antminer register values ([Mujina PR #65](../../raw/firmware/mujina/2026-06-05-github-mujina-pr-65-feat-stratum-v2-add-sv2-support.md)).

## Duplicate shares: causes

| Cause | Mechanism | Evidence |
|---|---|---|
| Version wrap-around | job held past one epoch, or `asic_job_frequency_ms` too long, so the chip restarts the space | [ESP-Miner #939](../../raw/firmware/esp-miner/2025-05-20-github-esp-miner-issue-939-custom-nonce-and-extra-nonce-rang.md); [ESP-Miner #1729](../../raw/firmware/esp-miner/2026-05-29-github-esp-miner-issue-1729-rarely-we-get-duplicates-reduce.md) |
| HCN slightly too large | neighbouring cores' ranges overlap; duplicates arrive milliseconds apart; PLL variation can push a frequency-based range over (example "34 duplicate-share (0.36 %)"); proposal: nonce percent 95% for rolling chips, BM1397 timeout percent 95% | [ESP-Miner #1729](../../raw/firmware/esp-miner/2026-05-29-github-esp-miner-issue-1729-rarely-we-get-duplicates-reduce.md) |
| Sweeping past a partial-core chip's top nonce | multi-chip boards cross into the next chip's slice | [ESP-Miner #939](../../raw/firmware/esp-miner/2025-05-20-github-esp-miner-issue-939-custom-nonce-and-extra-nonce-rang.md) |
| Reporting quarters masked, no offset | re-sent identical work re-finds identical results | [Mujina BM13xx reference](../../raw/firmware/mujina/github-mujina-mujina-miner-src-asic-bm13xx-reference.md) |
| Faulty chip / power | a Gamma 601 re-emitted results ~195–207 times at ~11ms intervals, all from cores 66–79 (one of four domains); raising 1060 mV to 1150 mV roughly halved duplicates; dashboard inflated to 298 TH/s; fix: drop exact repeats keyed on (job_id, extranonce2, version, nonce) | [ESP-Miner #1820](../../raw/firmware/esp-miner/2026-07-19-github-esp-miner-issue-1820-asic-results-duplicated-200x-eac.md) |
| Stratum, not the chip | a repeated jobId with cleanJob=false; fixed by ignoring duplicate stratum jobIds | [ESP-Miner #1587](../../raw/firmware/esp-miner/2026-03-02-github-esp-miner-issue-1587-esp-miner-is-unable-to-handle-di.md) |

> **Status: Disputed** (how often HCN-overlap duplicates occur)
> adammwest reports rare duplicates on version-rolling chips and wants a 95% margin. mutatrum counters that ESP-Miner's job timeout is capped at 500ms / number of cores, so the full space is never traversed, and he had not seen duplicates on 66/68/70 devices ([ESP-Miner #1729](../../raw/firmware/esp-miner/2026-05-29-github-esp-miner-issue-1729-rarely-we-get-duplicates-reduce.md)). Best assessment: both can be true. Overlap needs an HCN sized to the full slice, which Mujina's guidance and multi-chip forks use and which ESP-Miner's capped timeout mostly avoids. The Mujina floor-plus-200-tick-guard rule removes the overlap without giving up 5% coverage ([Mujina BM13xx reference](../../raw/firmware/mujina/github-mujina-mujina-miner-src-asic-bm13xx-reference.md)).

## Expected hashrate and hash domains

**Formula:** expected hashrate = total small cores × hash frequency. ESP-Miner uses the per-chip total small-core count rather than cores × sub-cores ([ESP-Miner #248](../../raw/firmware/esp-miner/2024-07-02-github-esp-miner-issue-248-determine-proper-job-interval-for.md)):

| Chip | Small cores | Frequency | Expected | Measured (Braiins 1 h avg) |
|---|---|---|---|---|
| BM1366 | 894 | 485 MHz | 433.6 GH/s | 433 GH/s (Bitaxe 204) |
| BM1368 | 1276 | 490 MHz | 625.2 GH/s | 638 GH/s (Bitaxe 401) |

Georges760 corrected the BM1368 core count to 80 (not 90) in the same thread. A self-test bug multiplied the BM1368 core count by 8 midstates instead of 16 ([ESP-Miner #868](../../raw/firmware/esp-miner/2025-04-25-github-esp-miner-issue-868-self-test-calulation-error-for-bm.md)). For the non-rolling BM1397, adammwest's work-item formula is hashes_in_work = (168/256) × 4 × 2^32 ([ESP-Miner #350](../../raw/firmware/esp-miner/2024-09-25-github-esp-miner-issue-350-consolidation-of-serial-comms-iss.md)). Luck = hashrate / expected hashrate ([ESP-Miner #1105](../../raw/firmware/esp-miner/2025-07-01-github-esp-miner-issue-1105-add-luck-to-axeos.md)).

**Hashrate registers.** Chips can report their own hash counts. ESP-Miner first enabled the register for all chips by mistake and restricted it to the BM1370 ([ESP-Miner #1262](../../raw/firmware/esp-miner/2025-10-06-github-esp-miner-issue-1262-hashrate-reg-is-currently-at-all.md)). v2.11.0 then added hashrate registers for the BM1366, BM1368 and BM1397 ([firmware release records](../../raw/hardware/bitaxe-osmu/bitaxe-firmware-release-records.md)). Register-based readings sit near expected: a stock Gamma reads between 1.00 and 1.14Th/s around an expected 1.071 T/hs, where share-based estimates swung between 0.7 Th/s and 1.4 Th/s ([ESP-Miner #1379](../../raw/firmware/esp-miner/2025-11-23-github-esp-miner-issue-1379-reduced-hash-rate-and-increased.md)).

**Hash domains (BM1370).** ESP-Miner reports four hash domains per BM1370. Known faults:

- One domain can stick at 0 GH/s until a software restart. The unit then mines at ~75% of expectedHashrate while errorPercentage stays 0, because the error metric is error_hashrate / current_hashrate. Self-test fails a domain below ~1/3 of expected, but runtime had no such check ([ESP-Miner #2004](../../raw/firmware/esp-miner/2026-09-28-github-esp-miner-issue-2004-bm1370-hash-domain-stuck-at-0-gh.md)).
- One domain reading about three orders of magnitude high produced displays of around 200 TH/s on some Gamma 601s ([ESP-Miner #1445](../../raw/firmware/esp-miner/2025-12-11-github-esp-miner-issue-1445-bitaxe-gamma-shows-unrealistic-h.md)).
- A fixed 380 GH/s per-domain self-test ceiling falsely failed strong domains. A fork raised it to 500 GH/s ([ESP-Miner #1954](../../raw/firmware/esp-miner/2026-09-08-github-esp-miner-issue-1954-self-test-pwm-0-should-not-block.md)).

Mujina's MISC_CONTROL measurements also split the BM1370 core array into quarters. The sources do not say whether ESP-Miner's hash domains are the same quarters.

## Temperature sensing evolution

| Chip | On-chip sensing | How boards read it |
|---|---|---|
| BM1387 / BM1397 | Temp_P/Temp_N, just a diode inside the chip | one external reader per chip (EMC2101 on Bitaxe); skot notes this is why the S9 reports only a few chip temps via an NCT218 ([ESP-Miner #2](../../raw/firmware/esp-miner/2023-01-18-github-esp-miner-issue-2-not-an-issue-just-a-suggestion-on-e.md)) |
| BM1366 | no die-temp diode | EMC2101 internal sensor placed close to the ASIC ([bitaxeUltra README](../../raw/hardware/bitaxe-osmu/github-bitaxeorg-bitaxeultra.md)); Ultra 207 adds an external MMBT3904 diode near the ASIC ([ESP-Miner #1228](../../raw/firmware/esp-miner/2025-09-10-github-esp-miner-issue-1228-add-support-for-bitaxeultra-207.md)) |
| BM1368 | TEMP_P/TEMP_N pins plus an on-die sensor at 0xB0/0xB4 (temperature = code * 0.171342 - 299.5144 degrees Celsius, from factory firmware, unchecked on live hardware) | external diode via EMC2101 ([OSMU wiki: BM1368](../../raw/hardware/bitaxe-osmu/osmu-wiki-osmu-lab-bm1368.md); [Mujina BM13xx reference](../../raw/firmware/mujina/github-mujina-mujina-miner-src-asic-bm13xx-reference.md)) |
| BM1370 | on-die sensor inert (0xB4 reads zero); diode routed out via ANALOG_MUX select 2; voltage ADC at 0xB8-0xBD (wait about 60 ms) | external diode via EMC2101 (Gamma) or EMC2103 (GT) ([Mujina BM13xx reference](../../raw/firmware/mujina/github-mujina-mujina-miner-src-asic-bm13xx-reference.md)) |

BM1370 temperature has been the hardest case:

- skot called it "totally busted" in late 2024 and listed the analog mux register (compare with S21 dumps) and EMC2101 gain/ideality as suspects ([ESP-Miner #536](../../raw/firmware/esp-miner/2024-11-30-github-esp-miner-issue-536-improve-supra-bm1368-die-temp-rea.md)).
- PR #484 fixed under-reporting. After upgrading, users saw readings about 10 degrees Celsius warmer and fans about 2000 RPM faster ([ESP-Miner #512](../../raw/firmware/esp-miner/2024-11-23-github-esp-miner-issue-512-chip-temperature-2-3-0-2-4-0.md)).
- Overheating builds and bad die readings were closed as fixed by better temp-diode tuning on the EMC2101 ([bitaxeGamma #12](../../raw/hardware/bitaxe-osmu/2024-10-28-github-bitaxegamma-issue-12-some-bitaxegamma-builds-are-over.md); [bitaxeGamma #15](../../raw/hardware/bitaxe-osmu/2024-11-13-github-bitaxegamma-issue-15-some-asic-die-temperature-readin.md)).
- Swings of 20ºC or more between samples remain an open report ([bitaxeGamma #16](../../raw/hardware/bitaxe-osmu/2024-11-13-github-bitaxegamma-issue-16-fluctuating-asic-die-temperature.md)).
- On the GT's dual EMC2103, the slope was correct and a -10C offset was applied ([ESP-Miner #881](../../raw/firmware/esp-miner/2025-05-02-github-esp-miner-issue-881-need-to-tune-temperature-sensor-f.md)).

## Board-level errata tied to the chips

- **RI pull-up.** The last chip's RI pin needs an external pull-up because the internal one fails on some batches (e.g. BM1366AB), leaving the board unresponsive ([ultraHex #51](../../raw/hardware/bitaxe-osmu/2026-09-18-github-ultrahex-issue-51-issue-with-a-specific-batch-of-chip.md); [ultraHex PR #52](../../raw/hardware/bitaxe-osmu/2026-09-30-github-ultrahex-pr-52-issues-about-the-ri-pull-up-resistor-a.md)).
- **BM1370 footprint.** The GND pad was slightly too big and the VDD pad too small, and the 0.503mm pitch was questioned. This was fixed in commit 713e3ac ([bitaxeGamma #26](../../raw/hardware/bitaxe-osmu/2025-03-04-github-bitaxegamma-issue-26-improve-bm1370-footprint.md)).
- **Variants.** "AG" and "AL" BM1366 variants both work on the Ultra ([bitaxeUltra README](../../raw/hardware/bitaxe-osmu/github-bitaxeorg-bitaxeultra.md)). The BM1397 has multiple lettered versions ([OSMU wiki: BM1397](../../raw/hardware/bitaxe-osmu/osmu-wiki-osmu-lab-bm1397.md)).
- **Cracked die.** A crack across the middle of the die means overheating, probably during soldering, and the chip is destroyed ([OSMU wiki: BM1366](../../raw/hardware/bitaxe-osmu/osmu-wiki-osmu-lab-bm1366.md)).

## Reverse-engineering provenance (history)

- **2022 — BM1387.** Skot's first bitaxe used two S9 chips. At the README snapshot he had no serial response yet, though current draw changed on frequency commands ([BM1387 prototype README](../../raw/hardware/bitaxe-osmu/2022-05-26-bitaxe-bm1387-prototype-readme.md)).
- **2023 — BM1397 and BM1366.** The BM1397 bitaxe mined in excess of 400 GH/s under cgminer ([BM1397 platform README](../../raw/hardware/bitaxe-osmu/2023-05-11-bitaxe-bm1397-platform-readme.md)). The Ultra prototype got a BM1366AG serial response before ESP-Miner supported the chip, and asked for protocol insight ([Ultra prototype README](../../raw/hardware/bitaxe-osmu/2023-07-20-bitaxe-ultra-prototype-readme.md)). ESP-Miner v2.0.0 added initial BM1366 support and v2.1.0 added BM1368 support ([firmware release records](../../raw/hardware/bitaxe-osmu/bitaxe-firmware-release-records.md)).
- **OSMU Lab** set out to publish findings from reverse engineering closed parts like mining ASICs, and its chip pages carry the pinouts above ([OSMU Lab about](../../raw/hardware/bitaxe-osmu/osmu-wiki-osmu-lab-about.md)).
- **2026 — Mujina chip reference.** Mujina PR #86 grew the BM13xx protocol doc into a full chip reference ([Mujina PR #86](../../raw/firmware/mujina/2026-08-03-github-mujina-pr-86-docs-bm13xx-grow-protocol-doc-into-chip.md)). PR #77 and PR #105 restructured the driver from a single-chip Bitaxe model into a chain model for EmberOne00, S19 and S21, with typed registers tested against captured factory bytes ([Mujina PR #77](../../raw/firmware/mujina/2026-07-06-github-mujina-pr-77-feat-bm13xx-multi-chip-groundwork-for-em.md); [Mujina PR #105](../../raw/firmware/mujina/2026-08-30-github-mujina-pr-105-refactor-bm13xx-merge-the-first-part-of.md); [Mujina PR #118](../../raw/firmware/mujina/2026-09-29-github-mujina-pr-118-refactor-bm13xx-remove-bitvec-dependenc.md)). The reference credits ESP-Miner, cgminer, emberone-miner, Skot's BM1397 docs, older Bitmain datasheets (BM1380–BM1385), factory bmminer and single_board_test, and live experiments ([Mujina BM13xx reference](../../raw/firmware/mujina/github-mujina-mujina-miner-src-asic-bm13xx-reference.md)).
- **2026 — next generation.** ESP-Miner v2.15.2 (prerelease) added BM1372/BM1373 driver support ([ESP-Miner releases](../../raw/firmware/esp-miner/github-esp-miner-releases.md)). ESP-Miner's ASIC test suite builds isolated instances of the real BM1366/BM1368/BM1370/BM1373 and BM1397 drivers ([ESP-Miner ASIC test README](../../raw/firmware/esp-miner/github-esp-miner-components-asic-test-readme.md)).

### Chip supply and the desoldering economy (Undermine 2025 / HPS 2026 panels)

The provenance above — chips pulled from salvage boards — exists because the chip makers mostly do not sell chips. On the Undermine 2025 heat-reuse panel: "Antiner doesn't sell chips" — "Ant miner generally does not sell chips. you would have to have a very very large special case for them to consider that" ([00:43:57] [Undermine 2025 heat-reuse panel](../../raw/history/heatpunks-summit/20251111-undermine-2025-exploring-the-heat-reuse-potential-of-bitcoin-mining.md)). The ASIC-frontier panel heard the builder side of the same problem: every Bitaxe chip was "probably desoldered from an existing machine", which the panel called "pretty inefficient way to build things" ([00:13:45]–[00:14:16] [Undermine 2025 ASIC frontier](../../raw/history/heatpunks-summit/20251111-undermine-2025-the-bitcoin-asic-frontier.md)). Bob Bernett (self-introduced as Barefoot Mining CEO and part of the M5 ASIC team) argued the industry must split chip design from system manufacturing the way the PC industry split Intel from the OEMs: "There has to be an Intel, AMG, uh Harris, TI type companies that you can go buy uh these AS6 from", sold in flavors from "very low hash rate and very low voltages" up to "massive die sizes" ([00:05:23]–[00:13:13] [Undermine 2025 ASIC frontier](../../raw/history/heatpunks-summit/20251111-undermine-2025-the-bitcoin-asic-frontier.md)). The HPS 2026 "Chips on the Table" talk picked up the same roadblock from the community side: Scott (self-introduced as "Scott 9000, instigator of the Bitax project" — Bitaxe) named "access to the like essential building block of these systems, which is the mining ASIC itself", noting other chip industries "They'll give you designs. They they'll give you a thousandpage data sheet for a $1 part" while the ASIC market does not ([00:12:08]–[00:12:50] [HPS 2026 Chips on the Table (Talk 6)](../../raw/history/heatpunks-summit/2026/20260303-hps-2026-chips-on-the-table-home-mining-hardware-asics-talk-6.md)).

- **Block/Proto: chips at retail.** Zuber Ahmad (self-introduced as a product manager at Proto, part of Block) said Block is "committed to release chips and" rigs, and wants to "make our chips available for everybody", beginning with a mining development kit on Intel silicon: "we've given 256,000 chips" — "of those Intel chips to uh the 256 foundation" — as tape-and-reel parts with instructions, applied for through the 256 Foundation "to get a trunch of 5,000 10,000 of them" ([00:18:59]–[00:21:40] [Undermine 2025 ASIC frontier](../../raw/history/heatpunks-summit/20251111-undermine-2025-the-bitcoin-asic-frontier.md)). The moderator tied those chips to the Foundation's open-source stack: the Ember One 100-watt hashboard, an open-source control board, the Mujina firmware, a blockatcher and a one-click Hydropool ([00:21:09] [Undermine 2025 ASIC frontier](../../raw/history/heatpunks-summit/20251111-undermine-2025-the-bitcoin-asic-frontier.md)).
- **Canaan: the cost side of a chip.** Canaan's Leo (addressed by name on stage) benchmarked the wider electronics industry, where chip makers earn margins "ranging from 40% to 70%" with customer support embedded in the gross margin, and said "It is not the same in this industry" — "it cost us $30 million to take out one chip" (captioned as spoken; "take out" reads as tape-out) on cutting-edge nodes ([00:14:10]–[00:14:49] [HPS 2026 Chips on the Table (Talk 6)](../../raw/history/heatpunks-summit/2026/20260303-hps-2026-chips-on-the-table-home-mining-hardware-asics-talk-6.md)). On volume he said Canaan can back custom builders who can afford "the MQ" (minimum order quantity) at around 5,000 chips, and Scott answered "5,000Q, no problem" — "If you send data sheets, like let's go" ([00:15:34]–[00:17:56] [HPS 2026 Chips on the Table (Talk 6)](../../raw/history/heatpunks-summit/2026/20260303-hps-2026-chips-on-the-table-home-mining-hardware-asics-talk-6.md)).
- **Yields shape the machines.** The panel recalled COVID-era wafer pricing ("we had to update the wafer price every month") and first-wafer yields: "you could get 90% yield on on the first wafer" in one panelist's early career, "It's it's 30% now" — "You get 30% yield on the first wafer if you're lucky"; one panelist's 20-nanometer product took its first wafer and got one chip where 200-300 were expected ([00:25:17]–[00:26:20] [Undermine 2025 ASIC frontier](../../raw/history/heatpunks-summit/20251111-undermine-2025-the-bitcoin-asic-frontier.md)). That economics explains the machines themselves: the hundreds of chips inside a Bitmain, rather than a couple, exist because "they're dealing with those yields. They want little tiny slices of the wafer instead of bigger pieces" ([00:44:07]–[00:44:39] [Undermine 2025 ASIC frontier](../../raw/history/heatpunks-summit/20251111-undermine-2025-the-bitcoin-asic-frontier.md)).
- **Next-generation claims (M5).** The M5 project — self-described as 18 months in, staffed by ex-Samsung, Intel and Broadcom people including Intel 486 veterans — expects "somewhere between 20 and 30% improvement" still available "within the the hashing algorithms themselves", sub-10 "jewel per terahash" chips "this time next year" (with around-20-J/TH parts continuing on older processes), and techniques to "maybe push into the um 10 terraash per chip range" via larger dies — all "possible as you go into 2026" ([00:41:23]–[00:45:11] [Undermine 2025 ASIC frontier](../../raw/history/heatpunks-summit/20251111-undermine-2025-the-bitcoin-asic-frontier.md)). Best assessment: these are stage projections by an interested party, not measurements, and no Bitmain counter-claim is on record here.
- **Update 2026-10-10 — the sub-10 J/T claim meets a confirmed maker sheet.** Bitmain's own storefront now lists a shipping-soon machine at 8.9 J/T on wall @35℃: the S23 XP Hyd. spec table (600T-10, 5340 W, "Shipping from November 2026"), captured 2026-10-10 ([S23 XP Hyd. spec table](../../raw/hardware/bitmain/2026-10-10-bitmain-site-s23-xp-hyd.md)). The M5 text above stays a stage projection by an interested party; the Bitmain figure is a manufacturer spec-table claim carrying a ±5% band — neither is an independent measurement. No real conflict between the two, so both stand, date-stamped.

## Current-generation Antminer lineup (shop captures, 2026-10-10)

Machine-level captures to pair with the chip-level material above: direct pulls of Bitmain's shop product APIs, taken 2026-10-10 ([Bitmain catalog](../../raw/hardware/bitmain/2026-10-10-bitmain-site-product-catalog.md); per-SKU spec tables: [S23 XP Hyd.](../../raw/hardware/bitmain/2026-10-10-bitmain-site-s23-xp-hyd.md), [S23e U2H](../../raw/hardware/bitmain/2026-10-10-bitmain-site-s23e-u2h.md), [S21 XP+ Hyd.](../../raw/hardware/bitmain/2026-10-10-bitmain-site-s21-xp-plus-hyd.md), [S21 XP Hyd.](../../raw/hardware/bitmain/2026-10-10-bitmain-site-s21-xp-hyd.md), [S21 XP](../../raw/hardware/bitmain/2026-10-10-bitmain-site-s21-xp.md); profitability cross-checks: [AMV Bitmain snapshot](../../raw/hardware/asicminervalue/2026-10-10-asicminervalue-bitmain.md), [MiningNow Bitmain snapshot](../../raw/hardware/miningnow/2026-10-10-miningnow-bitmain.md)).

### S23 generation confirmed

- **Antminer S23 XP Hyd.** — spec table 600T-10: 600 T typical, 5340 W on wall @35℃, 8.9 J/T, 15300 USD (25.5 USD/T), product status 1 (pre-sale), "Shipping from November 2026" ([S23 XP Hyd. spec table](../../raw/hardware/bitmain/2026-10-10-bitmain-site-s23-xp-hyd.md)). Model article: [Antminer S23 XP Hyd](antminer-s23-xp-hyd.md).
- **Antminer S23e U2H** — spec table 865T-10: 865 T, 8650 W on wall @35℃, 10 J/T, 2U rack chassis (600*483*86 mm w/o package), 19030 USD, pre-sale, "Shipping from Q4 2026" ([S23e U2H spec table](../../raw/hardware/bitmain/2026-10-10-bitmain-site-s23e-u2h.md)). The same capture's hot-products list pairs it with the ANTSPACE HW7 container: "242 2U-type (S23e U2H) miners or 396 T-type miners" in a 2000 kW, $169,000 package ([Bitmain catalog](../../raw/hardware/bitmain/2026-10-10-bitmain-site-product-catalog.md)). Model article: [Antminer S23e U2H](antminer-s23e-u2h.md).
- The S23 XP Hyd. also appears in the shop's home "Hot Products" carousel at $15,300 ([Bitmain catalog](../../raw/hardware/bitmain/2026-10-10-bitmain-site-product-catalog.md)).

### The 8.9 → 17 J/T live ladder

Efficiency ladder across the 12 live SHA256 SKUs (catalog rows, wall-side claims): S23 XP Hyd. 8.9 J/T → S23e U2H 10 J/T → S21 XP+ Hyd. 11 J/T → S21j XP Hyd. / S21 XP Hyd. 12 J/T → U3S21EXPH / S21e XP Hyd. 13 J/T → S21 XP / S21 XP Imm. 13.5 J/T → S21+ Hyd. 15 J/T → S21 Imm. 16 J/T → S21e Hyd. 17 J/T ([Bitmain catalog](../../raw/hardware/bitmain/2026-10-10-bitmain-site-product-catalog.md)). Hydro is the flagship track; the best air-cooled number is the S21 XP at 13.5 J/T, 3645 W, 270 T, single-phase 220~277 V ([S21 XP spec table](../../raw/hardware/bitmain/2026-10-10-bitmain-site-s21-xp.md)). The ladder's top and bottom by host machine: 600 T / 5340 W (S23 XP Hyd.) down to 288 T / 4896 W (S21e Hyd.).

### ±band convention (wall-efficiency bands)

- Hydro SKUs state "power on wall @35℃" (inlet coolant temperature) with ±3% hashrate and ±5% power/efficiency bands; the air-cooled S21 XP states its wall numbers @25℃ inlet air ([S23 XP Hyd. spec table](../../raw/hardware/bitmain/2026-10-10-bitmain-site-s23-xp-hyd.md); [S21 XP spec table](../../raw/hardware/bitmain/2026-10-10-bitmain-site-s21-xp.md)). The two bands are not directly comparable across cooling classes.
- Cross-manufacturer comparisons should also respect band width: Bitmain quotes single typical TH/s values (±3%), while MicroBT's sheets quote ±10% hashrate ranges (capture-report note) — compare bands, not headlines ([Bitmain catalog](../../raw/hardware/bitmain/2026-10-10-bitmain-site-product-catalog.md); report at [raw index](../../raw/hardware/bitmain/_REPORT.md)).

### Prior generation (no live spec page)

Plain S21, S21 Pro, S21 Hyd. and T21 do not appear in the live 2026-10 shop catalog — prior-generation, "no spec page available from live shop" ([Bitmain catalog](../../raw/hardware/bitmain/2026-10-10-bitmain-site-product-catalog.md)). They remain documented only via the DB snapshots (AMV/MiningNow rows, values as of 2026-10-10) and as chip hosts in the sections above (S21 → BM1368, S21 Pro → BM1370). No fresh capture exists for them; numbers in this wiki for those SKUs come from DB rows, not maker sheets.

### DB cross-check (AMV vs MiningNow, 2026-10-10)

- AMV's site rate is $0.10/kWh; MiningNow's default is $0.07/kWh (user-editable) — their $/day profit cells are computed at different electricity rates and are not comparable ([AMV Bitmain snapshot](../../raw/hardware/asicminervalue/2026-10-10-asicminervalue-bitmain.md); [MiningNow Bitmain snapshot](../../raw/hardware/miningnow/2026-10-10-miningnow-bitmain.md)). Gross income (profit + power × 24 h × rate) agrees within about 1% on every model present in both leaderboards.
- The S23 family is fully present on both DBs: air 318 Th/s / 3498 W, Hyd 580 Th/s / 5510 W, Hyd 3U 1.16 Ph/s / 11020 W, XP Hyd 600 Th/s / 5340 W, Imm. 442 Th/s / 5304 W, S23e Hyd 2U 865 Th/s / 8650 W. Neither DB lists any S22-series SKU ([AMV Bitmain snapshot](../../raw/hardware/asicminervalue/2026-10-10-asicminervalue-bitmain.md); [MiningNow Bitmain snapshot](../../raw/hardware/miningnow/2026-10-10-miningnow-bitmain.md)).
- Catalog-only SKUs (no individual capture this loop, ≤6-file cap): S21j XP Hyd. 495 T / 5940 W / 12 J/T, U3S21EXPH 860 T / 11180 W / 13 J/T (3U hydro bundle at 7740 (9.0/T)), S21e XP Hyd. 430 T / 5590 W / 13 J/T, S21 XP Imm. 300 T / 4050 W / 13.5 J/T, S21+ Hyd. 358 T / 5370 W / 15 J/T, S21 Imm. 215 T / 3440 W / 16 J/T, S21e Hyd. 288 T / 4896 W / 17 J/T ([Bitmain catalog](../../raw/hardware/bitmain/2026-10-10-bitmain-site-product-catalog.md)).

### Model index (Antminer model articles)

- [Antminer S23 XP Hyd](antminer-s23-xp-hyd.md) — 600 T / 5340 W / 8.9 J/T, 15300 USD, shipping from November 2026
- [Antminer S23e U2H](antminer-s23e-u2h.md) — 865 T / 8650 W / 10 J/T, 2U rack hydro, HW7 fill unit
- [Antminer S21 XP+ Hyd](antminer-s21-xp-plus-hyd.md) — 480 T / 5280 W / 11 J/T (DBs still list 500 Th / 5500 W — disputed)
- [Antminer S21 XP Hyd](antminer-s21-xp-hyd.md) — 473 T / 5676 W / 12 J/T
- [Antminer S21 XP](antminer-s21-xp.md) — 270 T / 3645 W / 13.5 J/T air, 76 dBA, 550 CFM

## Contradictions & Open Questions

- BM1366 efficiency/price and BM1370 footprint compatibility: see the Disputed blocks above.
- The BM1368 core count is blank in Mujina's table (16 sub-cores only). ESP-Miner threads give 80 cores and 1276 small cores ([ESP-Miner #248](../../raw/firmware/esp-miner/2024-07-02-github-esp-miner-issue-248-determine-proper-job-interval-for.md); [ESP-Miner #939](../../raw/firmware/esp-miner/2025-05-20-github-esp-miner-issue-939-custom-nonce-and-extra-nonce-rang.md)).
- ADDR0/ADDR1, INV_CLK0, ROSC_SEL and LITE_PAD functions, the UART_RELAY gap-count units, and the BM1362's six-channel ADC block (0xD0/0xDC/0xE4) remain undecoded ([Mujina BM13xx reference](../../raw/firmware/mujina/github-mujina-mujina-miner-src-asic-bm13xx-reference.md)).
- v2.15.2 writes ANALOG_MUX select 3, which Mujina describes as the no-diode default, while BM1370 production firmware uses select 2 for temperature readout. Whether this matters for Gamma temperature readings is untested ([ESP-Miner #2019](../../raw/firmware/esp-miner/2026-10-07-github-esp-miner-issue-2019-bm1370-gamma-601-v2-15-2-leaves.md); [Mujina BM13xx reference](../../raw/firmware/mujina/github-mujina-mujina-miner-src-asic-bm13xx-reference.md)).
- The BM1372/BM1373 protocol and register details are not yet captured in any public reference here.
- S21 XP+ Hyd.: the live maker sheet reads 480T-10 / 5280 W while both DBs list 500 Th / 5500 W — recorded as Disputed in [Antminer S21 XP+ Hyd](antminer-s21-xp-plus-hyd.md).
- The S23e U2H shop table is short-form: no PSU, coolant or weight rows in the listing (catalog weight field: 30), so its hydro plumbing figures are unpublished in this capture ([S23e U2H spec table](../../raw/hardware/bitmain/2026-10-10-bitmain-site-s23e-u2h.md)).
- S23 XP Hyd. performance curves (hashrate and efficiency vs inlet coolant temperature) are embedded images only — curve values remain uncaptured ([S23 XP Hyd. spec table](../../raw/hardware/bitmain/2026-10-10-bitmain-site-s23-xp-hyd.md)).
- DB "best price" cells carry no stated provenance; spreads against maker MSRP (e.g. S21 XP Hyd. 8041 USD vs $1,413.00 MiningNow) are recorded, not resolved.

## See Also

- [Bitaxe Models](bitaxe-models.md)
- [Bitaxe Board Design and Errata](bitaxe-board-design-and-errata.md)
- [Ember One (BZM2)](ember-one-bzm2.md)
- [ASIC Thermals and Heat Reuse](asic-thermals-and-heat-reuse.md)
- [Libre Board and Control Boards](libre-board-and-control-boards.md)
- [ESP-Miner / AxeOS](../firmware/esp-miner-axeos.md)
- [Mujina](../firmware/mujina.md)
- [Bitaxe Troubleshooting](../getting-started/bitaxe-troubleshooting.md)
- [Stratum in Practice](../protocols/stratum-in-practice.md)
- [Repair, Supply and Vendors](../industry/repair-supply-and-vendors.md)
