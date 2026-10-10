# Ember One & the BZM2 Hardware Stack

> Sources: 256 Foundation Telegram group (t.me/the256foundation), 2024-02-24 → 2026-10-07; 256foundation/emberone00-pcb README, release notes, issues & PRs, 2024-10 → 2026-03 (captured 2026-10-07); emberone.org; 256foundation/emberone-usbserial-fw PRs, 2026-01 → 2026-03; bitaxeorg/bitaxeBIRDS & bitaxeBonanza READMEs, docs and issues, 2025-08 → 2026-02; Mujina PRs on BZM2/RDS, 2026-06 → 2026-10; 256 Foundation newsroom & Assembling Freedom newsletter, 2025-05 → 2026-04
> Raw: [256F Telegram signal digest](../../raw/history/2026-10-08-256f-telegram-signal.md); [emberone00-pcb README](../../raw/hardware/256f-hardware/github-256foundation-emberone00-pcb.md); [emberone00-pcb releases](../../raw/hardware/256f-hardware/github-emberone00-pcb-releases.md); [emberone.org](../../raw/hardware/256f-hardware/emberone-org-home.md); [bitaxeBIRDS README](../../raw/hardware/bitaxe-osmu/github-bitaxeorg-bitaxebirds.md); [Mujina PR #117 (BZM2/RDS baseline)](../../raw/firmware/mujina/2026-09-28-github-mujina-pr-117-feat-bzm2-add-bzm2-asic-support.md)
> Updated: 2026-10-09
> As-Of: 2026-10-09
> Status: Draft

## Overview

The 256 Foundation's open hardware program: **Ember One** hashboards (a model series keyed to chip vendors), the **Intel BZM2** chips that made a non-Bitmain board real (donated by Proto), **BitaxeBIRDS / Bonanza** (the Bitaxe-family BZM2 boards), **aditBoard** (a bridge to native Antminer hashboards), and **Libre Board** (the open control board that drives them — see [Libre Board & Mining Control Boards](libre-board-and-control-boards.md)). An Ember One is a ~100W, 12-24 VDC, 125mm x 125mm hashboard that talks USB-C to a separate control board ([emberone.org](../../raw/hardware/256f-hardware/emberone-org-home.md)). Unlike a Bitaxe, which merges hashboard and ESP32 controller on one single-chip PCB, Ember One is a multi-chip series string of ASICs that needs that separate controller ([newsroom: Ember One grant](../../raw/history/256f-org/256foundation-org-newsroom-ember-one-first-grant.md)). The first model, **emberOne/00**, uses twelve Bitmain BM1362 chips harvested from the Antminer S19j Pro; the through-line of the program is to move to chips on reels with proper documentation, so anyone can build a miner without dismantling Bitmain hardware. Builders should read the specs, errata and revision tables below before ordering boards; newcomers can skip to the history sections.

## The emberOne model series

- emberOne is named by chip vendor: emberOne/00 = Bitmain BM1362, emberOne/01 = Intel BZM2 (Blockscale), emberOne/02 maybe Auradine — each a reference design for vendors willing to work cooperatively with the community [#2266 · 2025-05-22 · Ryan] [#2270 · 2025-05-23 · Skot Bitaxe]
- The website roadmap names Intel BZM2, Auradine and Proto Mining ASIC versions, all in the same standardized form factor, with each six-month grant cycle meant to bring a version for a different ASIC ([emberone.org](../../raw/hardware/256f-hardware/emberone-org-home.md)). By April 2026 Skot said there were no immediate plans for an Auradine-based Ember One — a cool project for someone else ([forum: Auradine support](../../raw/history/256f-org/2026-04-28-forum-auradine-support.md)).
- The captured `emberone01-pcb` README is still identical to the 00 README (BM1362), so no distinct 01 design is documented yet ([emberone01-pcb README](../../raw/hardware/256f-hardware/github-256foundation-emberone01-pcb.md)).
- Positioning: a 100 W-class board for use-cases where a full-size Antminer hashboard (roughly a kilowatt) doesn't fit; usable as-is or as a dev board for other hashboards [#2172 · 2025-05-15 · Skot Bitaxe]
- Future emberOnes deliberately use chips from new vendors selling directly to hardware producers — 'blazing the trail for a new category of mining systems'; the stated goal is never needing a Bitmain-chip model again [#2177 · 2025-05-16 · Ryan] [#2267 · 2025-05-22 · Ryan]
- Design rationale: the 12-24 vdc input range and USB communication let users run one or several hashboards, choose their ASIC and interchange parts ([emberone.org](../../raw/hardware/256f-hardware/emberone-org-home.md)). Team: lead engineer Skot, project manager econoalchemist.
- Product vision data point: a plug-in 1,500W 256F BZM2 miner-heater would deliver ~40 TH with wifi controls [#1871 · 2025-04-23 · Reckless Apotheosis] [#1874 · 2025-04-23 · Reckless Apotheosis]

## emberOne/00 (BM1362) reference

| Item | Value | Source |
|---|---|---|
| ASIC | 12 × Bitmain BM1362 (from the Antminer S19j Pro), in series | [README](../../raw/hardware/256f-hardware/github-256foundation-emberone00-pcb.md), [#53](../../raw/hardware/256f-hardware/2026-02-17-github-emberone00-pcb-issue-53-vdd-limited-to-3-16v-by-vddio.md) |
| Power | 100W class | [README](../../raw/hardware/256f-hardware/github-256foundation-emberone00-pcb.md) |
| Input | Wide 12-24VDC (v3/v4); 12-17vdc from v5 | [README](../../raw/hardware/256f-hardware/github-256foundation-emberone00-pcb.md), [newsletter, 2025-10-28](../../raw/history/256f-newsletter/2025-10-28-assembling-freedom-10.md) |
| Expected hashrate | "It should reach about 3.5 TH/s" | [README](../../raw/hardware/256f-hardware/github-256foundation-emberone00-pcb.md) |
| Measured (v3) | 2 TH/s @ 500MHz and 3.4V on Pyminer test firmware | [v3 release](../../raw/hardware/256f-hardware/github-emberone00-pcb-releases.md) |
| Form factor | 125mm x 125mm | [emberone.org](../../raw/hardware/256f-hardware/emberone-org-home.md) |
| Board MCU | RP2040 running emberone-usbserial-fw | [README](../../raw/hardware/256f-hardware/github-256foundation-emberone00-pcb.md) |
| USB ID | 1209:256f (pid.codes); bcdDevice major = hardware revision | [usbserial PR #16](../../raw/hardware/256f-hardware/2026-02-06-github-emberone-usbserial-fw-pr-16-feat-usb-use-pid-codes-vi.md), [PR #15](../../raw/hardware/256f-hardware/2026-01-18-github-emberone-usbserial-fw-pr-15-feat-usb-set-bcddevice-to.md) |
| Design files | KiCad — "Please fork, hack and release!" | [README](../../raw/hardware/256f-hardware/github-256foundation-emberone00-pcb.md) |

**Compatible chips**: use BM1362AA, AB, AC or AD; AI and BD might work but are untested; AJ and AK will not work ([README](../../raw/hardware/256f-hardware/github-256foundation-emberone00-pcb.md)). Chips on one board should be the same bin — see the supply section below.

**Cooling**: the v3 release warns to cool both the ASICs and the 4 power MOSFETs (Q1-Q4) ([v3 release](../../raw/hardware/256f-hardware/github-emberone00-pcb-releases.md)). No public waterblock STL exists; the prototypes used at Telehash #3 came from CryoByte Labs ([forum: waterblock STL](../../raw/history/256f-org/2026-05-15-forum-waterblock-stl.md)).

**Firmware**: initial mining support was hacked into a PiAxe/Pyminer fork (`skot/emberone-miner`, branch `emberone-BM1362-support`); full support is in [Mujina](../firmware/mujina.md) ([README](../../raw/hardware/256f-hardware/github-256foundation-emberone00-pcb.md)). The board's RP2040 control protocol (ports, packet format, command pages, the pending response-format change) is documented in [Libre Board & Mining Control Boards](libre-board-and-control-boards.md#emberone-usbserial-fw-rp2040-board-management).

### USB identity and revision detection

- Placeholder VID:PID 0xc0de:0xcafe was replaced by **1209:256f**, allocated to the Ember One project via pid.codes (merged 2026-02-18) ([usbserial PR #16](../../raw/hardware/256f-hardware/2026-02-06-github-emberone-usbserial-fw-pr-16-feat-usb-use-pid-codes-vi.md)).
- **bcdDevice**: major = hardware revision, minor.patch = firmware version, restarting with each hardware revision (v5.0.0 for hardware 5), so Mujina can tell v4, v5 and later boards apart (merged 2026-03-20) ([usbserial PR #15](../../raw/hardware/256f-hardware/2026-01-18-github-emberone-usbserial-fw-pr-15-feat-usb-set-bcddevice-to.md)).
- USB serial numbers come from the flash chip's per-chip unique ID; the JEDEC ID used before gave every board the same serial ([usbserial PR #19](../../raw/hardware/256f-hardware/2026-03-19-github-emberone-usbserial-fw-pr-19-fix-usb-derive-serial-num.md)).

### Hand assembly (toaster-oven reflow)

The board *can* be hand built ([README](../../raw/hardware/256f-hardware/github-256foundation-emberone00-pcb.md)): a convection toaster oven never used for food, a thermocouple, and Sn63/Pb37 no-clean leaded paste kept cold. Soak at 140-150C for 2 minutes once the thermocouple hits 140C, then high heat; hold around 200-220C for 30 seconds, then switch off and cool with the door open. Inspect under a microscope for dry pads and bridges (especially QFP/QFN) and fix with flux, braid and an iron; double-sided boards can sit on a small metal stand ([assembly tips](../../raw/hardware/256f-hardware/github-emberone00-pcb-assembly.md)).

## Design reference and errata

### The voltage-stacked chain

- The S19j Pro ships with the APW121215 (12-15V output); with 42 voltage domains per hashboard each chip gets 285mV to 357mV. On Ember One the LM25119 output is trimmed by a DS4432U; setting R_FS (R11) to 39kOhms gives 239mV to 360mV for each of the 12 ASICs ([#21](../../raw/hardware/256f-hardware/2025-02-28-github-emberone00-pcb-issue-21-change-full-scale-range-resis.md)).
- The 12 chips are stacked in series; each domain's local ground sits at (VDD / 12) * N above board ground ([#53](../../raw/hardware/256f-hardware/2026-02-17-github-emberone00-pcb-issue-53-vdd-limited-to-3-16v-by-vddio.md)). Because grounds float, only the first ASIC's internal temp diode is easy to measure ([#34](../../raw/hardware/256f-hardware/2025-04-24-github-emberone00-pcb-issue-34-measure-at-least-the-first-as.md)).
- POD256 #105 noted stacked domains are efficient but prone to cascading failures in long chains ([newsletter, 2026-02-19](../../raw/history/256f-newsletter/2026-02-19-assembling-freedom-17-unpacking-pod256-episode-105-chips-cha.md)).

### Serial-chain errata (fixed in v3)

| Issue | Fix | Source |
|---|---|---|
| Last chip needs a pull-up on RI | 1k pull-up | [#16](../../raw/hardware/256f-hardware/2025-02-22-github-emberone00-pcb-issue-16-last-chip-in-the-chain-needs.md) |
| PIN_MODE inverted on v2 columns 0 and 2 (U45-U47, U63-U65) | Corrected | [#17](../../raw/hardware/256f-hardware/2025-02-24-github-emberone00-pcb-issue-17-pin-mode-on-asic-columns-0-2.md) |
| BM1362 footprint pins too close to centre pads (pin-pitch mismatch) | Spacing corrected | [#18](../../raw/hardware/256f-hardware/2025-02-25-github-emberone00-pcb-issue-18-double-check-bm1362-footprint.md) |
| NRST lines lacked pulldowns (S19j Pro uses 2k pulldowns, 33ohm series across domains) | Pulldowns added | [#22](../../raw/hardware/256f-hardware/2025-03-05-github-emberone00-pcb-issue-22-nrst-signals-should-have-pull.md) |
| Stray 0xFF bytes with core voltage on; last ASIC sometimes silent at 3.6V | Still open; possibly cured by RI/NRST fixes | [#19](../../raw/hardware/256f-hardware/2025-02-26-github-emberone00-pcb-issue-19-noise-on-asic-serial-line-wit.md), [#29](../../raw/hardware/256f-hardware/2025-04-18-github-emberone00-pcb-issue-29-last-asic-in-chain-doesn-t-re.md) |

Noise benchmark from #19: an S9 regulator underclocked across 3 hashboards measured 176mV p-p (4.88% of output), while the tuned emberOne at 3.6V reached 60mV p-p (1.66%) ([#19](../../raw/hardware/256f-hardware/2025-02-26-github-emberone00-pcb-issue-19-noise-on-asic-serial-line-wit.md)).

### LM25119 buck bring-up (v1–v4)

- Early reports — shutdown above 18.00V input, output collapsing from 3.6V to 1.6V above 9A — were bench-PSU settings mistakes, not design faults (closed 2024-10-29) ([#1](../../raw/hardware/256f-hardware/2024-10-29-github-emberone00-pcb-issue-1-lm25119-shuts-down-when-input.md), [#2](../../raw/hardware/256f-hardware/2024-10-29-github-emberone00-pcb-issue-2-lm25119-output-voltage-drops-w.md)).
- Ramp capacitors C6/C10 must be 5% C0G/NP0; TI guidance says CRAMP under 2 nF, and 820 pF was used ([#3](../../raw/hardware/256f-hardware/2024-10-29-github-emberone00-pcb-issue-3-ramp-capacitors-need-better-to.md)).
- Being unable to adjust the output via the DS4432U was a test-firmware bug ([#20](../../raw/hardware/256f-hardware/2025-02-26-github-emberone00-pcb-issue-20-can-t-adjust-lm25119-output-v.md)); the U10 LDO "mismatch" was a late BOM change ([#15](../../raw/hardware/256f-hardware/2025-02-05-github-emberone00-pcb-issue-15-double-check-bom-on-u10.md)).

### Snubber and TVS lessons

- Low-side snubbers dissipate real power: the LM25119 guidance is a 2512, 1W package placed very close to the low-side MOSFET ([#27](../../raw/hardware/256f-hardware/2025-04-14-github-emberone00-pcb-issue-27-low-side-snubbers-need-to-be.md)).
- Issue #30 debated adding 100 pF + 10 Ω snubbers across the high-side MOSFETs; Skot pointed to the datasheet's low-side placement with EVM values of 1000pF and 5.1 Ohm. GitBobCat's sizing method: Csnb = 3*Cpar and Rdmp = SQRT(L/Cpar), with Cpar found from the ringing frequency before and after adding a known capacitor; he argued edge spikes are unclamped inductive energy a 5R1 snubber won't catch, and recommended tight decoupling at the upper device and probing tight to drain-source ([#30](../../raw/hardware/256f-hardware/2025-04-19-github-emberone00-pcb-issue-30-add-pads-for-high-side-mosfet.md)). C28 and C29 should match, folded into that work ([#47](../../raw/hardware/256f-hardware/2025-07-04-github-emberone00-pcb-issue-47-c28-and-c29-should-be-the-sam.md)).
- TVS: SMCJ28A on VIN and SMBJP6KE6.8A-TP on VOUT, air-wired first ([#28](../../raw/hardware/256f-hardware/2025-04-18-github-emberone00-pcb-issue-28-add-tvs-protection-diodes-on.md)); on USB, SMBJP6KE6.8A-TP on VBUS and TPD1E05U06 on the data lines ([#31](../../raw/hardware/256f-hardware/2025-04-21-github-emberone00-pcb-issue-31-add-protection-on-usb-vusb-an.md)).
- Reverse polarity (v4): zbomz cited Loki rigs where about half of tinkerers blew a hashboard and proposed an ideal-diode circuit; selected parts were the AP74700QW6-7 controller, NVMFS5C645NL MOSFET and SMBJ30CA TVS ([#37](../../raw/hardware/256f-hardware/2025-04-24-github-emberone00-pcb-issue-37-add-reverse-polarity-protecti.md)).

### Power, USB and interface decisions

- USB budget: while mining the board drew 50-60mA from USB depending on the LED ([#33](../../raw/hardware/256f-hardware/2025-04-24-github-emberone00-pcb-issue-33-check-usb-power.md)).
- USB-C PD sink (20 V @ 5 A via STUSB4500) was rejected on 2025-06-09 to keep things simple; multi-board systems are better fed from a parallel power bus bar ([#39](../../raw/hardware/256f-hardware/2025-05-01-github-emberone00-pcb-issue-39-add-usb-c-power-delivery-sink.md)).
- No fan header: VIN is 12-24V with no fixed 12V rail, so a VIN fan header risks burning fans, and an on-board 12V regulator would tax immersion/hydro users ([#36](../../raw/hardware/256f-hardware/2025-04-24-github-emberone00-pcb-issue-36-add-a-fan-connector.md)). An "EOAP" accessory port (like Bitaxe's BAP) was proposed ([#35](../../raw/hardware/256f-hardware/2025-04-24-github-emberone00-pcb-issue-35-add-the-eoap-for-hacking-poss.md)); v5 broke out pins for optional fan-control daughter-boards ([newsletter, 2025-11-24](../../raw/history/256f-newsletter/2025-11-24-assembling-freedom-11.md)).
- INA260 reads occasionally return 0xFFFF (81.92 A), causing false overcurrent shutdowns at 0.1s polling — a sensor-readiness issue, not firmware ([#40](../../raw/hardware/256f-hardware/2025-05-01-github-emberone00-pcb-issue-40-temperature-power-readings-fa.md)); the INA260AIPW went Last Time Buy, swapped for the reel-packaged INA260AIPWR ([#46](../../raw/hardware/256f-hardware/2025-06-21-github-emberone00-pcb-issue-46-ic-current-monitor-approachin.md)).
- Mechanical: VDC connectors moved to line up when stacked with Libre Board ([PR #43](../../raw/hardware/256f-hardware/2025-06-08-github-emberone00-pcb-pr-43-align-the-vdc-connectors-at-the.md)); fiducials came out as holes ([#49](../../raw/hardware/256f-hardware/2025-08-04-github-emberone00-pcb-issue-49-fiducials-ended-up-being-hole.md)); order 2mm-thick PCBs ([#51](../../raw/hardware/256f-hardware/2025-09-23-github-emberone00-pcb-issue-51-order-thicker-pcbs.md)).

### v5 → v6.1 errata

- **IO voltage domain bug (#53, found by rkuester, 2026-02-17)**: on v5 VDD could not exceed ~3.16V because the shared-5V MCP1824T VDDIO LDOs (2.1V minimum input) in the upper domains lost regulation; chips started oscillating near VDD = 3.12V, last chip first. Workaround: at VDD = 3.1V the chain ran stably to ~225 MHz for ~1.6 TH/s. Fix: boost USB 5V to 6V for VDDIO, allowing VDD up to 4.25V; a hacked v5 with 6V injected mined at VDD=3.6V and 500MHz, and a 6V boost regulator was added in commit ddfc8d9 ([#53](../../raw/hardware/256f-hardware/2026-02-17-github-emberone00-pcb-issue-53-vdd-limited-to-3-16v-by-vddio.md)). The fix was done desk-side on POD256 #105, reaching ~2 TH/s ([newsletter, 2026-02-19](../../raw/history/256f-newsletter/2026-02-19-assembling-freedom-17-unpacking-pod256-episode-105-chips-cha.md)).
- **RP2040 boot race (#54)**: the RP2040's power-on reset releases near 1V but the W25Q16JV flash needs 2.7V, so v6.1 added a voltage supervisor on RUN — kept optional after korbin reported no issue on dozens of RP2xxx boards ([#54](../../raw/hardware/256f-hardware/2026-03-16-github-emberone00-pcb-issue-54-rp2040-may-attempt-flash-read.md)).
- **PGOOD (#56)**: read good with VIN absent (pulled up to 3.3V); v6.1 uses a divider from VIN ([#56](../../raw/hardware/256f-hardware/2026-03-16-github-emberone00-pcb-issue-56-pgood-reads-good-when-vin-is.md)). Series resistance was suggested on signals crossing the VIN and USB domains ([#55](../../raw/hardware/256f-hardware/2026-03-16-github-emberone00-pcb-issue-55-consider-series-resistance-on.md)).
- **Reset paths (#57)**: the ASIC chain resets cleanly via its switched domain, but the TPS546D24 can only be hard-reset by removing VIN, and the always-on 3V3 rail only by unplugging USB — hence the request for a per-port power-switched hub on Libre Board ([#57](../../raw/hardware/256f-hardware/2026-03-16-github-emberone00-pcb-issue-57-consider-watchdog-driven-3v3.md)).
- v6.1 also added ESD protection on the reset button and renamed active-low nets (`CHAIN_RST_N`, `THERM_N`, `SMB_ALRT_N`) with no electrical change ([#58](../../raw/hardware/256f-hardware/2026-03-16-github-emberone00-pcb-issue-58-consider-esd-protection-on-th.md), [#59](../../raw/hardware/256f-hardware/2026-03-19-github-emberone00-pcb-issue-59-docs-schematic-rename-active.md)).

## Revision history

| Rev | Date | Key changes | Source |
|---|---|---|---|
| v1 | 2024-11 | Voltage-regulator test PCBs (tag `v1_pcb_order`), JLCPCB boards, DigiKey parts; footprint reverse-engineered from desoldered ASICs under a microscope | [#8](../../raw/hardware/256f-hardware/2024-11-18-github-emberone00-pcb-issue-8-source-test-pcb-vendor.md), [#10](../../raw/hardware/256f-hardware/2024-11-18-github-emberone00-pcb-issue-10-reverse-engineer-chip-mechani.md) |
| v2 | 2025-02 | First full hashboard; serial-chain errata above | [#17](../../raw/hardware/256f-hardware/2025-02-24-github-emberone00-pcb-issue-17-pin-mode-on-asic-columns-0-2.md) |
| v3 | 2025-04-30 | First official release, "12-24VIN @ 100W"; 2 TH/s on test firmware | [v3 release](../../raw/hardware/256f-hardware/github-emberone00-pcb-releases.md) |
| v4 | validated Sep 2025 | Reverse-polarity protection, USB TVS, RP2040 BOOT/RESET buttons, one TMP1075 replaced by on-die sensing; declared production-ready, ~3.5Th/s on BM1362AC | [#32](../../raw/hardware/256f-hardware/2025-04-22-github-emberone00-pcb-issue-32-add-boot-and-reset-buttons-fo.md), [#44](../../raw/hardware/256f-hardware/2025-06-09-github-emberone00-pcb-issue-44-move-tmp1075-temp-sensors-out.md), [newsletter, 2025-09-25](../../raw/history/256f-newsletter/2025-09-25-rig-bitcoin-mining-re-imagined.md) |
| v5 | RC Oct 2025 | TPS546D24 regulator with live power metrics and programmable over-temp shutdown, TPS22919 VDDIO load switch, MCP1824T VDDIO LDOs; input narrowed to 12-17vdc; impedance-matched traces | [#53](../../raw/hardware/256f-hardware/2026-02-17-github-emberone00-pcb-issue-53-vdd-limited-to-3-16v-by-vddio.md), [newsletter, 2025-10-28](../../raw/history/256f-newsletter/2025-10-28-assembling-freedom-10.md), [newsletter, 2025-11-24](../../raw/history/256f-newsletter/2025-11-24-assembling-freedom-11.md) |
| v6.1 | Mar 2026 | 6V VDDIO boost, RUN supervisor, PGOOD divider, reset ESD, `_N` net names | [#53](../../raw/hardware/256f-hardware/2026-02-17-github-emberone00-pcb-issue-53-vdd-limited-to-3-16v-by-vddio.md), [#59](../../raw/hardware/256f-hardware/2026-03-19-github-emberone00-pcb-issue-59-docs-schematic-rename-active.md) |

> **Status: Disputed** — input voltage range
> The README advertises "Wide 12-24VDC input voltage" ([README](../../raw/hardware/256f-hardware/github-256foundation-emberone00-pcb.md)), an open issue (2025-09-11) asks the silkscreen to say 12-18V ([#50](../../raw/hardware/256f-hardware/2025-09-11-github-emberone00-pcb-issue-50-change-silkscreen-to-indicate.md)), and the v5 newsletter says input narrows to 12-17vdc ([newsletter, 2025-10-28](../../raw/history/256f-newsletter/2025-10-28-assembling-freedom-10.md)). Best assessment: 12-24V applies to v3/v4; treat v5 and later as 12-17V until the README is updated.

### Production timeline (Telegram)

- 2025-06-12: v4 changed enough from the released v3 that the plan became prototype-first, then a 100+ unit order; pending list ~110 hashboards (largest: jstefanop 50, Scott Offord 25) [#2456 · 2025-06-12 · econoalchemist]
- 2025-07-02: production order slipped to mid-July with ~4-week turnaround → shipping mid-August; hashboards only — no PSU, heat-sink, fan, firmware or control board [#2643 · 2025-07-02 · econoalchemist]
- 2025-08-27: Skot resolved the ASIC-communication issue with v4 validation expected that week; production moved from Ben's original quote ($150/unit + $500 setup) to econoalchemist's new in-house pick-and-place line (100 units) [#2983 · 2025-08-27 · econoalchemist]. The line is a private venture (Neoden 4 pick-and-place, Neoden IN6 reflow) separate from the Foundation ([newsletter, 2025-09-25](../../raw/history/256f-newsletter/2025-09-25-rig-bitcoin-mining-re-imagined.md)).
- v5 release candidate (published 2025-09-26): voltage-regulator circuit gutted and upgraded (Vishay-class reg); max-input requirement dropped from 24V to 17V — far more practical for high-current, low-voltage regulators; the OVP circuit still needs a prototype-sacrifice test [#3059 · 2025-09-23 · econoalchemist] [#3063 · 2025-09-23 · Jstefanop] [#3087 · 2025-09-25 · Skot Bitaxe] [#3089 · 2025-09-26 · econoalchemist] [#3091 · 2025-09-26 · econoalchemist]
- 2025-12-09: prototype PCBs + components on hand for only 5 boards — validate, revise, re-prototype before production; one Libre Board drives 4 Ember Ones (roughly 400 watts) [#3843 · 2025-12-09 · econoalchemist] [#3855 · 2025-12-09 · econoalchemist]
- 2026-01-02: first Ember One 00 v5 prototype finally on the pick-and-place [#4025 · 2026-01-02 · econoalchemist]
- 2026-01-08: first two Ember One (00 v5) boards assembled and shipped to Ryan to start validation; v5 remains a release candidate until validated [#4193 · 2026-01-08 · econoalchemist] [#4167 · 2026-01-07 · econoalchemist]
- September 2026: Ember One and Libre Board still need final validation of their latest revisions ([Presidio fundraiser newsroom](../../raw/history/256f-org/256foundation-org-newsroom-presidio-bitcoin-fundraiser.md)).

### Sleep-mode hazard (field report)

- csh2000/Loki: in sleep mode, hashboards with a PIC shut down, but PIC-less boards keep the VRM active — chips stay hot while not mining, leaving you fully dependent on fans; he had repeated fan-failure meltdowns/PSU trips before diagnosing it; flagged as critical for the Ember HB on PSUs with no regulation/communication [#3053 · 2025-09-18 · csh2000] [#3054 · 2025-09-18 · csh2000]
- emberOne can cut all power to the ASIC chips → very low quiescent draw [#3058 · 2025-09-23 · Skot Bitaxe]; an RP2040-controlled load switch on the 5V VDDIO rail was proposed for exactly this ([#52](../../raw/hardware/256f-hardware/2025-09-23-github-emberone00-pcb-issue-52-add-load-switch-on-5v-power-t.md)).
- Stacking note (NebulaMiner): with Libre Board bottom facing emberOne bottom, LED + USB share a corner (only power-tab polarity flips) and ASIC heatsink heat ends up opposite the compute module and other M.2-sensitive components [#3075 · 2025-09-24 · NebulaMiner] [#3076 · 2025-09-24 · NebulaMiner]

## Grant, licensing and funding

- The original grant (issue #4) funded one project manager and up to two engineers to build "a modular ~100W 2-4 Terahash open-source Bitcoin miner hashboard" from S19 J-Pro ASICs; firmware, enclosure, manufacturing, sales and support were excluded. It officially started November 1, 2024 and was to conclude April 30, 2025, with six-month renewals and a confidential budget paid monthly ([issue #4](../../raw/hardware/256f-hardware/2024-11-18-github-emberone00-pcb-issue-4-release-validated-ember-one-de.md)).
- The grant work plan was posted as issues (specify VR components → order components → VR test PCB → test vendor → test vregs → reverse-engineer chip mechanicals → layout → bring-up → bug fixes) ([#5](../../raw/hardware/256f-hardware/2024-11-18-github-emberone00-pcb-issue-5-specify-voltage-regulator-comp.md), [#12](../../raw/hardware/256f-hardware/2024-11-18-github-emberone00-pcb-issue-12-layout-actual-hashboard.md), [#13](../../raw/hardware/256f-hardware/2024-11-18-github-emberone00-pcb-issue-13-bring-up.md)). Issue #4 was closed 2025-06-21 pointing at the v3 release as the initial validated design ([issue #4](../../raw/hardware/256f-hardware/2024-11-18-github-emberone00-pcb-issue-4-release-validated-ember-one-de.md)).
- Mid-2025 funding: OpenSats' eleventh wave and an HRF grant funding Ember One work ([newsletter, 2025-06-19](../../raw/history/256f-newsletter/2025-06-19-you-know-i-m-something-of-a-decentralized-pool-myself.md)).

> **Status: Disputed** — license
> The grant proposal says "This project is fully open-source GPL licensed" ([issue #4](../../raw/hardware/256f-hardware/2024-11-18-github-emberone00-pcb-issue-4-release-validated-ember-one-de.md)) and the Foundation's grant announcement calls it a GPL-licensed reference design ([newsroom: Ember One grant](../../raw/history/256f-org/256foundation-org-newsroom-ember-one-first-grant.md)); emberone.org links its open-source claim to CERN-OHL-S ([emberone.org](../../raw/hardware/256f-hardware/emberone-org-home.md)). Best assessment: the hardware is intended to be CERN-OHL-S (the hardware analogue of GPL, matching Libre Board and Bitaxe); check the repo LICENSE file before relying on either.

## BM1362 supply crunch (July 2025)

- BM1362 unavailable new in trays/reels (Power Mining could not find any); hashboards are easy to buy but require desolder/clean/test labor [#2656 · 2025-07-03 · Kristaps Stikuts]
- Only AA/AB/AC/AD variants exist (different footprints); Skot had been ordering new from NBTC until 'supply chain nonsense' cut supply — harvest from S19j Pro boards is the fallback [#2657 · 2025-07-03 · Skot Bitaxe] [#2658 · 2025-07-03 · Skot Bitaxe]
- emberOne requires same-bin chips (some bins don't work well together); all chips on a single jPro hashboard are likely one bin — a silver lining of harvesting [#2659 · 2025-07-03 · Skot Bitaxe]
- Harvest economics: disassembly + prep + cleaning + testing ≈ 5 minutes per chip; SMT feeders need pristine cleaning [#2660 · 2025-07-03 · Kristaps Stikuts] [#2666 · 2025-07-03 · Kristaps Stikuts]
- Repair-side data point: new chips by the bin haven't been purchasable since the S17 days [#2661 · 2025-07-03 · Mæstro Juergen]
- Juergen's harvest method: 300×300 heat plate, ultrasonic board cleaning, flux — chips come off needing little cleanup; works even on boards with soldered-on bottom heatsinks [#2662 · 2025-07-03 · Mæstro Juergen] [#2664 · 2025-07-03 · Mæstro Juergen] [#2667 · 2025-07-03 · Mæstro Juergen]
- Counter-data: Nick from Mega Miner can supply BM1362AC brand-new on the reel (quoted July 2025); bin matching unknown [#2665 · 2025-07-03 · econoalchemist]

## The BZM2 windfall

- Provenance: Proto donated the Intel ASICs (the canceled-2023 BZM2) to the Foundation at NEMS fall 2024; Proto had bought the chips while winding down, planning mass MDK production, but their own internal ASIC took off [#3007 · 2025-09-02 · Mæstro Juergen] [#3009 · 2025-09-02 · Reckless Apotheosis] [#3012 · 2025-09-02 · Reckless Apotheosis]
- On September 2 (2025) the Foundation took possession; the chips were roughly 3-years old with about S19j Pro-level efficiency, and all were disbursed to developers. Technical documentation could not be included in the donation — a BZM2 Bitaxe and the next Ember One would carry docs, and a separate group was preparing an open subset ([newsletter, 2025-10-28](../../raw/history/256f-newsletter/2025-10-28-assembling-freedom-10.md)). Mujina later notes the BZM2 is publicly documented, with its hardware reference in Blockscale-Solutions/bzm2-hwref (CC-BY-SA) ([Mujina PR #69](../../raw/firmware/mujina/2026-06-11-github-mujina-pr-69-feat-asic-intel-bzm2-bonanza-mine-2-asic.md)).
- For open-source devs the chips are free, brand-new on reel, no desoldering; Tom's Hardware covered the story [#3021 · 2025-09-03 · econoalchemist] [#3035 · 2025-09-03 · econoalchemist] [#3038 · 2025-09-05 · econoalchemist]

> **Status: Disputed** — how many chips
> The newsletter says the Foundation took possession of "the 256,000 Intel BZM2 ASIC chips donated by Proto Mining" ([newsletter, 2025-10-28](../../raw/history/256f-newsletter/2025-10-28-assembling-freedom-10.md)), and Telegram says 256k [#3007 · 2025-09-02 · Mæstro Juergen]; Mujina PR #69 describes the BZM2 as the chip the Foundation "received as a 54,000-unit grant" ([Mujina PR #69](../../raw/firmware/mujina/2026-06-11-github-mujina-pr-69-feat-asic-intel-bzm2-bonanza-mine-2-asic.md)). Best assessment: 256,000 is the Foundation's own repeated figure; the 54,000 may refer to a sub-allocation, unverified.

### BZM2 chip facts

- Chip marking decoded from the reel: HASH IC, 12W, 5nm TSMC Process, LGA BZM2-HASH-IC-FF0.5, 99ALPD — DVT1 silicon [#3681 · 2025-11-24 · Reckless Apotheosis] [#3673 · 2025-11-24 · Skot Bitaxe]
- Nominally 0.7V with approx 350 GH/s @ 1.15 GHz; on-chip digital temperature and voltage sensors; ntime rolling ([BIRDS README](../../raw/hardware/bitaxe-osmu/github-bitaxeorg-bitaxebirds.md)). Telegram estimates appx 400 GH/s per chip [#2183 · 2025-05-16 · Mike Hamilton].
- **Serial**: a 9-bit multidrop UART where the 9th bit marks address vs data, at 5Mbaud; TDM result reads; a 20x12 logical engine grid; chain enumeration walks IDs from the `0xFA` power-on default ([Mujina PR #69](../../raw/firmware/mujina/2026-06-11-github-mujina-pr-69-feat-asic-intel-bzm2-bonanza-mine-2-asic.md); [Bonanza #4](../../raw/hardware/bitaxe-osmu/2025-10-31-github-bitaxebonanza-issue-4-esp32s3-can-t-really-do-9bit-se.md)). The ESP32-S3 cannot do 9-bit serial natively (parity-bit abuse falls out of sync at speed; RMT emulation is limited), so BZM2 boards use an RP2040/RP2350 or FPGA sidecar — STM32F4 and RP2xxx have native 9-bit UARTs ([Bonanza #4](../../raw/hardware/bitaxe-osmu/2025-10-31-github-bitaxebonanza-issue-4-esp32s3-can-t-really-do-9bit-se.md)).
- **Pinout / PINSEL**: pin 36 PINSEL swaps the data-pin functions — with PINSEL = 0 pins 17/18 are RESET_IN/UART_RX_IN, with PINSEL = 1 they are UART_TX_IN/TRIP_IN for chaining; REFCLKIN/REFCLKOUT pass the reference clock along, and a JTAG interface (TDO/TDI/TCK/TMS/TRST) is exposed ([BZM2 pinout](../../raw/hardware/bitaxe-osmu/github-bitaxebirds-doc-bzm2-pinout.md)).
- NOOP (opcode 4'hF) is the ASIC ping; the BZM2 answers 2ZB in the wild, while the datasheet says 24'h425A4D ("BZM") and the architectural spec says "BZ2" — the Intel docs disagree with each other [#3687 · 2025-11-24 · Skot Bitaxe] [#3697 · 2025-11-24 · Skot Bitaxe] [#3700 · 2025-11-24 · Reckless Apotheosis]. Mujina's driver expects NOOP to return "BZ2" ([Mujina PR #69](../../raw/firmware/mujina/2026-06-11-github-mujina-pr-69-feat-asic-intel-bzm2-bonanza-mine-2-asic.md)).
- Backdoor reality check: you couldn't really hide a backdoor in the ASIC itself — the vectors are hashboard control chips, the control-board FPGA, or its software [#3033 · 2025-09-03 · Reckless Apotheosis] [#3034 · 2025-09-03 · Reckless Apotheosis] [#3032 · 2025-09-03 · Jstefanop]

**Single-chip characterization** (excerpt of the BIRDS table; columns as published) ([BIRDS specs](../../raw/hardware/bitaxe-osmu/github-bitaxebirds-doc-specs.md)):

| Voltage (V) | Frequency (GHz) | Hashrate (TH/s) | Power (Watt) | Efficiency (J/TH) |
|---|---|---|---|---|
| 0.680 | 0.60 | 0.187 | 5.0 | 26.5 |
| 0.680 | 0.80 | 0.250 | 6.6 | 26.4 |
| 0.7 | 1.15 | 0.357 | 10.36 | 29.02 |
| 0.740 | 1.50 | 0.465 | 15.2 | 32.8 |
| 0.810 | 1.85 | 0.577 | 21.95 | 38.04 |

Read it as: efficiency is best at low clocks; the top rows trade noticeably more joules per terahash for extra hashrate.

## BitaxeBIRDS & Bonanza (Bitaxe-family BZM2 boards)

- **BIRDS** (Bitaxe Intel Reference Design System): four BZM2 in series for firmware development — "still an untested prototype" per its README; 11-13V XT30 input; TPS546D24S single-phase regulator tuned for 2.8V output @ 20A; no EMC2101; controlled by a Raspberry Pi Pico 2W (RP2350) whose PIO handles the 9-bit serial, with preliminary bitaxe-raw-pico firmware targeting the pin-compatible RP2040 Pico; Gerbers withheld to discourage low-quality clones ([BIRDS README](../../raw/hardware/bitaxe-osmu/github-bitaxeorg-bitaxebirds.md)).
- bitaxeBIRDS repo published 2025-11-13 [#3311 · 2025-11-13 · Skot Bitaxe]; first bring-up established communication with all 4 chips after fixes tracked in the repo issues [#3647 · 2025-11-23 · Skot Bitaxe]
- Bring-up ran bitaxe-raw-pico on an RP2040 Pico exposing the ASIC chain serial over USB; RP2350 (Pico 2) port by johnny9; test scripts at github.com/skot/bzm-raw-py [#3660 · 2025-11-23 · Skot Bitaxe] [#3661 · 2025-11-23 · Skot Bitaxe] [#3662 · 2025-11-23 · Skot Bitaxe] [#3663 · 2025-11-23 · Skot Bitaxe] [#3664 · 2025-11-23 · Skot Bitaxe] [#3665 · 2025-11-23 · Skot Bitaxe]
- ASIC_ID changed to 0x42 and NOOP answered from all 4 BZM2s; TPS546D24 voltage regulator and new manual fan control verified [#3747 · 2025-11-30 · Skot Bitaxe]
- High-speed serial: 5 Mbaud 9-bit serial working on the RP2040; Mike Hamilton's custom S9 control-board FPGA image does 10 Mbaud 9-bit and talks to BZM2s [#3314 · 2025-11-13 · Skot Bitaxe] [#3318 · 2025-11-13 · Mike Hamilton]
- Form factors compared: emberOne 130×130 mm vs BitaxeBIRDS 68×123 mm [#3745 · 2025-11-30 · Loren Lang]
- BoM reality: ~$30/board before it 'does quite a few boards' (no fan, heatsink or Pico included); buy Coilcraft inductors directly from coilcraft.com [#3785 · 2025-12-02 · Reckless Apotheosis] [#3791 · 2025-12-02 · Skot Bitaxe]
- Up to 25 BitaxeBIRDS targeted assembled in time for NEMS 2026 [#4029 · 2026-01-03 · Reckless Apotheosis]

**BIRDS errata**

| Issue | Fix | Source |
|---|---|---|
| TX_IN level-shifter pull resistors (R36, R42, R48) pulled high / referenced to GND_H | Pull down to GND_L; PR #3 closed 2026-02-10 | [#2](../../raw/hardware/bitaxe-osmu/2025-11-21-github-bitaxebirds-issue-2-tx-in-level-shifter-needs-to-pull.md), [PR #3](../../raw/hardware/bitaxe-osmu/2025-11-30-github-bitaxebirds-pr-3-fix-the-tx-in-pull-down-resistor-to.md) |
| Chain end: last ASIC's TX_IN (pin 17) / TRIP_IN (pin 18) | 1k pull-up optional (internal pull-ups), 10k pull-down on TRIP_IN wise | [#1](../../raw/hardware/bitaxe-osmu/2025-11-21-github-bitaxebirds-issue-1-last-asic-in-the-chain-needs-tx-i.md) |
| C60-C64 on unused REFCLK outputs listed as 0.1 μF instead of 120 pF | Value corrected (0.1uF boards still worked) | [#5](../../raw/hardware/bitaxe-osmu/2026-02-02-github-bitaxebirds-issue-5-part-value-mismatch-with-listed-d.md) |
| PINSEL pins tied to GND2 while chip VSS was GND3 | Fixed 2026-02-15 | [#7](../../raw/hardware/bitaxe-osmu/2026-02-14-github-bitaxebirds-issue-7-improper-gnd-used-for-pinsel-pins.md) |
| Tiny level-shifter diode / IO LDO packages | Bigger packages; ERC cleanup | [#6](../../raw/hardware/bitaxe-osmu/2026-02-09-github-bitaxebirds-issue-6-use-bigger-packages-for-level-shi.md), [#4](../../raw/hardware/bitaxe-osmu/2025-12-02-github-bitaxebirds-issue-4-clan-up-erc-errors-on-schematic.md) |

Peer review of the schematic caught the TX_IN problem post-fab: 'wish I had noticed that before getting boards made' [#3736 · 2025-11-29 · Loren Lang] [#3739 · 2025-11-29 · Skot Bitaxe]; a second build holding TXO low traced to an ASIC soldering issue [#3750 · 2025-11-30 · Skot Bitaxe].

- **Bonanza** (eight BZM2): the 1001x board had RX/TX swapped on the 1.2V-3.3V level shifter and wrong TPS546 strapping resistors, fixed in 1002x (2026-02-12), and the BIRDS pre-Bonanza branch became Bonanza 1002x ([Bonanza #3](../../raw/hardware/bitaxe-osmu/2025-09-12-github-bitaxebonanza-issue-3-level-shifter-1-2v-3-3v-rx-and.md), [Bonanza #1](../../raw/hardware/bitaxe-osmu/2025-08-04-github-bitaxebonanza-issue-1-tps546-strapping-resistors-are.md), [BIRDS #7](../../raw/hardware/bitaxe-osmu/2026-02-14-github-bitaxebirds-issue-7-improper-gnd-used-for-pinsel-pins.md)). POD256 (April 2026) showed it targeting ~1.2 TH/s per unit with a 12V fan and a sidecar for the 9-bit serial ([newsletter, 2026-04-05](../../raw/history/256f-newsletter/2026-04-05-pod256-episode-110-newsletter-april-fools-real-progress-open.md)). Bonanza Bridge firmware requires a safety lease before enabling 5 V or releasing reset; BIRDS `bzmd` detected all four ASICs and powered on in 4 seconds ([bitaxe-raw PR #18](../../raw/hardware/bitaxe-osmu/2026-07-25-github-bitaxe-raw-pr-18-update-bitaxebonanza-raw-for-bridge.md)).

> **Status: Disputed** — does Bonanza work?
> The captured README still says the design does not work because of issue #3 and might never work because of issue #4 ([Bonanza README](../../raw/hardware/bitaxe-osmu/github-bitaxeorg-bitaxebonanza.md)), but issue #4 was closed as fixed with 1002x on 2026-02-12 ([Bonanza #4](../../raw/hardware/bitaxe-osmu/2025-10-31-github-bitaxebonanza-issue-4-esp32s3-can-t-really-do-9bit-se.md)) and bridge/raw firmware work continued through July 2026. Best assessment: the README warning predates 1002x and is likely stale.

## Satoshi Starter

- Reckless Systems + My First Bitcoin: single-ASIC BZM2 miner crowdfund on Geyser — soft launch 2025-10-30, hard launch on White Paper Day 2025-10-31; billed as the first commercial BZM2 miner, first DIY-solderable kit miner, and the first miner with open ASIC documentation [#3166 · 2025-10-28 · Reckless Apotheosis] [#3187 · 2025-10-30 · Reckless Apotheosis] [#3202 · 2025-10-31 · Reckless Apotheosis] [#3203 · 2025-10-31 · Reckless Apotheosis]
- The newsletter frames it as an open reference hardware design whose documentation covers how the chip works and how to interface with it, so no reverse engineering is needed ([newsletter, 2025-11-24](../../raw/history/256f-newsletter/2025-11-24-assembling-freedom-11.md)).

## BZM2 power-domain math

- 16 BZM2 arranged in 4 domains of 4 chips: 2.8V for the whole stack at nominally 70A, on a 4-phase TPS546 for headroom; alternative: 8 domains of 2 → about 5.6V and only 35A [#5106 · 2026-07-22 · Skot Bitaxe] [#5119 · 2026-07-22 · Skot Bitaxe] [#5121 · 2026-07-22 · Aadhi M]
- The TPS546's limiting factor is its 5.5V max Vout (TI app note sdaa417 linked as a workaround path) [#5111 · 2026-07-22 · Skot Bitaxe]
- Aadhi shrank his domains to a 9-chip version on the same buck and switched to LTC regulators for high-VIN use [#5109 · 2026-07-22 · Aadhi M] [#5117 · 2026-07-22 · Aadhi M]
- Skot: the emberOne form factor needs to be re-thought, informed by next-gen Bitaxe work on the TPS546 (which is on the more recent emberOne revs) [#5087 · 2026-07-22 · Skot Bitaxe]

## RDS bring-up and baseline (September 2026)

- Attempting a community PR on an Intel RDS with 300× BZM2 ASICs — if it works on the Intel controller it would be the highest-hashrate Mujina system so far; the first 2026 firmware build was written by Claude and deployed fully remotely [#5482 · 2026-09-14 · Reckless Apotheosis] [#5489 · 2026-09-14 · Reckless Apotheosis]
- 3.8kW of Mujina-controlled hash available to dump into a tank for the NYC workshop [#5522 · 2026-09-29 · Reckless Apotheosis]
- **Baseline** (run `20261001T085812Z`, 3.5 h, 300-ASIC RDS mining to Ocean, Mujina PR #117): 1207 accepted shares, 0 rejected; share-derived hashrate 107.85 TH/s; supply power mean 3674.53 W; 32.17 J/TH by the wall-meter step and 34.07 J/TH by supply power (a separate 2 h run measured 33.64 J/TH at the wall); hottest die 81.87 °C; first accepted share 5 s after bring-up; 0 faults. The platform ran stock OpenWrt 18.06.2 ([Mujina PR #117](../../raw/firmware/mujina/2026-09-28-github-mujina-pr-117-feat-bzm2-add-bzm2-asic-support.md)). The `rds-2.0` platform is a 3-board, 300-ASIC chassis ([Mujina PR #121](../../raw/firmware/mujina/2026-10-01-github-mujina-pr-121-feat-bzm2-add-rds-platform-support.md)).
- Mujina's BZM2 board driver retunes on thermal 85 °C and voltage-imbalance 150 mV triggers ([Mujina PR #70](../../raw/firmware/mujina/2026-06-11-github-mujina-pr-70-feat-board-bzm2-board-driver-with-calibr.md)).

## aditBoard & Auradine

- aditBoard (github.com/skot/aditBoard): adaptor from Antminer's proprietary data ribbon to USB-C so Libre Board + Mujina can eventually drive native Antminer hashboards; Libre Board provides 4 USB-C hashboard connectors (3 boards + spare) [#2166 · 2025-05-15 · econoalchemist] [#2250 · 2025-05-22 · econoalchemist]
- aditBoard as designed targets the S19j Pro, but should be mechanically and electrically compatible with everything down to the S9 — the remainder is software work (plus level shifters for Bitmain's 1.2V core) [#2446 · 2025-06-10 · Dimi8146] [#2451 · 2025-06-10 · Skot Bitaxe]
- Adit Board v2 talks to Antminer hashboards over USB, and the AntHat lets a Raspberry Pi drive Antminer fans and PSU through it ([newsletter, 2025-09-25](../../raw/history/256f-newsletter/2025-09-25-rig-bitcoin-mining-re-imagined.md)).
- Mike Hamilton wrote firmware that exercised S19 PSUs and offered to dig up his old code/documentation on their I2C interface [#2452 · 2025-06-10 · Mike Hamilton]
- aditBoard production: 100 boards quoted at $450 total; later 250 panelized boards sitting ready for the pick-and-place, queued behind Ember One & Libre Board prototypes [#2733 · 2025-07-31 · Dimi8146] [#3506 · 2025-11-21 · econoalchemist]
- Auradine: samples of 4nm and 3nm ASICs in hand, and the 256 Foundation was granted an entire reel of the 3nm ASICs; Auradine has tape-out in December [#3450 · 2025-11-20 · Reckless Apotheosis] [#3454 · 2025-11-20 · Reckless Apotheosis]; 'Auradine ASICs up for grabs' announcement [#3342 · 2025-11-18 · econoalchemist]
- Nobody sells Bitcrane or aditBoard yet (as of Nov 2025) — expected to change 'now that there is something to do with them' [#3504 · 2025-11-21 · Skot Bitaxe]

## Libre Board status (summary)

Full detail lives in [Libre Board & Mining Control Boards](libre-board-and-control-boards.md); the Telegram highlights:

- Compute is open: any module conforming to the two-100-pin standard — Raspberry Pi CM5, x86, even RISC-V; ≥2 TB storage recommended so a full node fits [#2252 · 2025-05-22 · econoalchemist] [#2254 · 2025-05-22 · econoalchemist]
- First revision's connectors/layout opened for community feedback (GitHub issue #16) before the first test production [#2514 · 2025-06-17 · Michael Schmid @Schnitzel]
- Heater cases like the Stealth Miner expose only a single board edge, so port/button/SD placement matters for flashing without disassembly; Libre Board settled on two edges with user-accessible ports (front and top) [#2523 · 2025-06-18 · AgentP] [#2526 · 2025-06-18 · Michael Schmid @Schnitzel]
- Community PSU shortlist for a 10-hashboard stack: Bitmain APW7 (OK at 240V, weaker at 110V, keep under 80% load), Mean Well SE-1500-15, HP DPS-600PB, Mean Well LRS-600-12 [#2291 · 2025-05-27 · Toobahlou] [#2300 · 2025-05-28 · Toobahlou]
- rev 3 (July 2026): ~70% done in PCB design + schematic; remaining = build via assembly service and test; ~2 months to a validated rev 3, ~3 months if a rev 4 is needed; full documentation to follow [#5085 · 2026-07-22 · Michael Schmid @Schnitzel] [#5086 · 2026-07-22 · Michael Schmid @Schnitzel]
- 'Libreboard and Mujina already have full emberOne support' [#5102 · 2026-07-22 · Skot Bitaxe]

### Mini-rack direction (July 2026)

- After seeing rjk256's sous-vide setup, Skot proposed a native mini-rack form factor: 1U is 1.75-inch tall — fit a hashboard and heatsink in that and call it EmberOneU; one controller per rack driving hashboards over a USB hub; two 1200W APW3/7 PSUs side-by-side in 2U; possible hydro option [#5088 · 2026-07-22 · Skot Bitaxe] [#5093 · 2026-07-22 · Skot Bitaxe] [#5094 · 2026-07-22 · Skot Bitaxe] [#5097 · 2026-07-22 · Skot Bitaxe] [#5098 · 2026-07-22 · Skot Bitaxe] [#5100 · 2026-07-22 · Skot Bitaxe]
- POD256 brainstorm: Ember One boards fit an S9 chassis (up to six boards) and suit fanless passive heating with large heat sinks ([newsletter, 2025-11-24](../../raw/history/256f-newsletter/2025-11-24-assembling-freedom-11.md)).

## Form-factor explorations

- The PC-AXE, a WIP drop-in graphics-card replacement: 'a drop in replacement for your graphics card with 14.4Th/s Hashrate at 180W' [#2472 · 2025-06-16 · Tyler Stevens]
- Skeptics: a PCIe slot supplies only 75W (hence extra power connectors), and dumping the heat inside a closed PC chassis is the real problem — called a non-starter without blower-style airflow [#2474 · 2025-06-16 · Reckless Apotheosis] [#2482 · 2025-06-16 · Reckless Apotheosis] [#2486 · 2025-06-16 · Reckless Apotheosis]
- Dimi's counter-direction: skip the GPU form factor — put hashboards on a server backplane (power + heat management integrated) with aditboards, or a unifi-style mini-lab where one 8-inch RU holds two stacked Ember Ones [#2501 · 2025-06-16 · Dimi8146] [#2508 · 2025-06-16 · Dimi8146] [#2510 · 2025-06-16 · Dimi8146]
- Proof-of-Steak: 'the first sous vide Bitcoin cooked steak' [#4356 · 2026-01-22 · Reckless Apotheosis]
- ProofofPrint: 3D-printer heated-bed hashrate project surfacing in the community (NYC collab) [#4412 · 2026-02-08 · MΛRCUS]

## Contradictions & Open Questions

- Priority dispute: aditBoard-first vs emberOne-first (and what the foundation's economic logic even is) — see [Open Mining Economics](../economics/open-mining-economics.md).
- Whether BM1362 can be bought new on reels at all: Power Mining found none, Skot's NBTC channel dried up, yet Mega Miner quoted BM1362AC new on reel in July 2025 — bin matching unverified [#2656 · 2025-07-03 · Kristaps Stikuts] [#2665 · 2025-07-03 · econoalchemist].
- Target hashrate: the README says "about 3.5 TH/s" ([README](../../raw/hardware/256f-hardware/github-256foundation-emberone00-pcb.md)) while POD256 #105 coverage says the board targets 3.6 TH/s ([newsletter, 2026-02-19](../../raw/history/256f-newsletter/2026-02-19-assembling-freedom-17-unpacking-pod256-episode-105-chips-cha.md)); measured results so far are 2 TH/s (v3) and ~2 TH/s (patched v5).
- Ember One form factor: emberone.org says 125mm x 125mm, but a Telegram comparison gives emberOne 130×130 mm [#3745 · 2025-11-30 · Loren Lang]; Libre Board issue #6 records the change from 128mm to 125x125mm ([libreboard #6](../../raw/hardware/256f-hardware/2025-04-09-github-libreboard-issue-6-agree-on-formfactor.md)). Best assessment: 125mm.
- BZM2 donation size (256,000 vs 54,000), license (GPL vs CERN-OHL-S), input range and Bonanza status — see the Disputed blocks above.
- Proto-rig immersion claims (air/immersion convertible) questioned: flow-reversal warnings, asymmetric heatsinks and fan handling would need work; the 48V-fan boost reg sits on the hashboard [#2848 · 2025-08-15 · Wade Bowlin] [#2849 · 2025-08-15 · Wade Bowlin] [#2852 · 2025-08-15 · econoalchemist] [#2854 · 2025-08-15 · Wade Bowlin] [#2861 · 2025-08-15 · Skot Bitaxe] [#2863 · 2025-08-15 · Wade Bowlin]

## See Also

- [Libre Board & Mining Control Boards](libre-board-and-control-boards.md)
- [Mujina](../firmware/mujina.md)
- [Bitaxe Board Design & Errata](bitaxe-board-design-and-errata.md)
- [Bitaxe Models](bitaxe-models.md)
- [Bitmain ASIC Reference](bitmain-asic-reference.md)
- [ASIC Thermals and Heat Reuse](asic-thermals-and-heat-reuse.md)
- [Open Mining Economics](../economics/open-mining-economics.md)
- [Repair, Supply & Vendors](../industry/repair-supply-and-vendors.md)
- [256F Community Timeline](../history/256f-community-timeline.md)
