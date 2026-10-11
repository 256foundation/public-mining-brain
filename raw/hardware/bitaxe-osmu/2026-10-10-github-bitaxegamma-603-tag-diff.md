# bitaxeGamma gamma-603 tag diff (Gamma-602...gamma-603)

> Source: https://github.com/bitaxeorg/bitaxeGamma/compare/Gamma-602...gamma-603
> Collected: 2026-10-10
> Published: 2026-02-17
> Registry ID: bitaxe-hw

- Repository: bitaxeorg/BitaxeGamma
- Compare: Gamma-602...gamma-603 (status: ahead, ahead_by 11 commits, behind_by 0)
- Base commit (Gamma-602 tag): 95d0658 "Revert \"added pullup resistors for #25\"" — i.e. Gamma-602 shipped WITHOUT the #25 pullups; gamma-603 re-adds them (f513149)
- Merge base: 95d0658 (same)

## Release record (GitHub API `releases`, captured verbatim)

Release "bitaxeGamma 603" (2026-02-17): body contains only the auto-generated Full Changelog link — no release notes.

```
**Full Changelog**: https://github.com/bitaxeorg/bitaxeGamma/compare/Gamma-602...gamma-603
```

Release metadata: tag `gamma-603`, name "bitaxeGamma 603", published 2026-02-17T22:54:44Z, created 2026-02-17T22:53:42Z, target main, draft: false, prerelease: false, author: skot. (For contrast: Gamma-602, published 2025-04-07, was prerelease: true with body "**Full Changelog**: https://github.com/bitaxeorg/bitaxeGamma/commits/Gamma-602 … DFM and routing improvements".)

## Commits (11)

- a094838 2025-04-24 Skot: exported BOM. Updated KiCad files to v9
- f7309c3 2025-04-24 Skot: BOM cleanup
- 4e21ab7 2025-04-24 Skot: removed old BOM. added iBOM
- 1967a18 2025-04-24 Skot: pcb sync
- 4bcb769 2025-04-29 Skot: remove incorrect J3 partno for #28. removed random dust from mounting hole positions for #32. bumped version to 603. added NRSTO pulldown. added NRSTI pulldown for #36. removed old manufacturing files.
- f513149 2025-04-29 Skot: added pullup resistors for #25
- 4f7187e 2025-04-29 Skot: added USB ID pulldown resistors for #37
- c83fabc 2025-06-19 Ben: removed unused fan header
- 1cb5c3f 2025-06-19 Ben: silkscreen, drc
- cc36793 2026-02-17 Skot: add 3d models
- ef21ec1 2026-02-17 Skot: update worksheet

## Files changed (24)

Generation files removed (old manufacturing outputs), KiCad files upgraded to v9 format, ECO-level schematic/PCB changes, version bump to 603. Note: `README.md`/`readme.md` is NOT in this diff — the readme was not touched between Gamma-602 and gamma-603.

| File | Status | +a/-d | Notes |
|---|---|---|---|
| Manufacturing Files/bitaxeGamma BOM.csv | removed | +0/-41 | old BOM removed (header: `Qty,Reference,Value,Footprint,DK,PARTNO,DNP`) |
| Manufacturing Files/gerbers/bitaxeGamma-B_Cu.gbr | removed | +0/-4318 | gerber removal |
| Manufacturing Files/gerbers/bitaxeGamma-B_Mask.gbr | removed | +0/-2316 | gerber removal |
| Manufacturing Files/gerbers/bitaxeGamma-B_Paste.gbr | removed | +0/-377 | gerber removal |
| Manufacturing Files/gerbers/bitaxeGamma-B_Silkscreen.gbr | removed | +0/-3358 | gerber removal |
| Manufacturing Files/gerbers/bitaxeGamma-Edge_Cuts.gbr | removed | +0/-46 | gerber removal |
| Manufacturing Files/gerbers/bitaxeGamma-F_Cu.gbr | removed | +0/-4047 | gerber removal |
| Manufacturing Files/gerbers/bitaxeGamma-F_Mask.gbr | removed | +0/-792 | gerber removal |
| Manufacturing Files/gerbers/bitaxeGamma-F_Paste.gbr | removed | +0/-520 | gerber removal |
| Manufacturing Files/gerbers/bitaxeGamma-F_Silkscreen.gbr | removed | +0/-8128 | gerber removal |
| Manufacturing Files/gerbers/bitaxeGamma-In1_Cu.gbr | removed | +0/-8293 | gerber removal |
| Manufacturing Files/gerbers/bitaxeGamma-In2_Cu.gbr | removed | +0/-5540 | gerber removal |
| Manufacturing Files/gerbers/bitaxeGamma-NPTH.drl | removed | +0/-35 | drill file removal |
| Manufacturing Files/gerbers/bitaxeGamma-PTH.drl | removed | +0/-423 | drill file removal |
| bitaxe.kicad_wks | modified | +1730/-2947 | KiCad worksheet/frame format v9 update ("update worksheet" commit) |
| bitaxe.pretty/TENSILITY_54-00164.kicad_mod 2 | added | +398/-0 | duplicate copy (note trailing " 2" in filename) of existing fan-header footprint (J1 = Tensility 54-00164 per 602 BOM), added by "add 3d models" commit |
| bitaxe.pretty/USB_10118193-0001LF_AMP.kicad_mod 2 | added | +69/-0 | duplicate copy (trailing " 2") of existing USB footprint, same commit |
| bitaxeGamma.kicad_pcb | modified | +11762/-6690 | layout change |
| bitaxeGamma.kicad_pro | modified | +62/-65 | KiCad v9 project format + new DRC rule settings |
| bitaxeGamma.kicad_sch | modified | +452/-94 | title block rev 602→603, KiCad v9 re-export, symbol-library cosmetics |
| bm1370.kicad_sch | modified | +1442/-408 | ECO resistors added (patch too large for API; deltas computed from both file versions) |
| esp32.kicad_sch | modified | +1366/-547 | ECO resistors added (patch too large for API) |
| fan.kicad_sch | modified | +306/-484 | unused fan header removed, R51→R24 |
| power.kicad_sch | modified | +947/-405 | no component deltas — v9 re-export only |

### Component-count deltas (computed from file contents at both tags)

- bm1370.kicad_sch: refs ADDED R17 (10k 0402), R18 (1k 0402), R19 (1k 0402), R20 (1k 0402), R21 (2k 0402), R26 (10k 0402); R6 (0 Ω, per 602 BOM `RC0402JR-070RL`) went from 3 symbol instances on this sheet to 0 (one R6 instance remains on power sheet in both). Matches commits "added NRSTO pulldown. added NRSTI pulldown for #36" and "added pullup resistors for #25".
- esp32.kicad_sch: refs ADDED R27 (5.6k 0402), R28 (5.6k 0402), R29 (5.1k 0402), R30 (5.1k 0402). Matches commit "added USB ID pulldown resistors for #37".
- fan.kicad_sch: refs REMOVED J7 (Conn_01x04 — commit "removed unused fan header"), J (Conn_01x04_MountingPin), R51 (5.6k); ref ADDED R24 (5.6k 0402) — R51→R24 renumber/move.
- bitaxeGamma.kicad_pcb: footprints 131 → 137 (+R20 R21 R26 R27 R28 R29 R30, −J7); via count 300 → 306.
- All 5 .kicad_sch title blocks: `(rev "602")` date 2024-09-26 → `(rev "603")` date 2025-04-29.

### Verbatim patch excerpts (load-bearing hunks)

bitaxeGamma.kicad_sch hunk 1 — version/rev bump + KiCad v9:

```
@@ -1,17 +1,21 @@
 (kicad_sch
-	(version 20231120)
+	(version 20250114)
 	(generator "eeschema")
-	(generator_version "8.0")
+	(generator_version "9.0")
 	(uuid "e63e39d7-6ac0-4ffd-8aa3-1841a4541b55")
 	(paper "A")
 	(title_block
 		(title "bitaxeGamma")
-		(date "2024-09-26")
-		(rev "602")
+		(date "2025-04-29")
+		(rev "603")
+		(company "bitaxeorg")
+		(comment 1 "OHLv2")
 	)
```

fan.kicad_sch — unused fan header J7 removal (symbol `Connector_Generic:Conn_01x04` instance, 4 pin rectangles deleted):

```
@@ -180,50 +189,6 @@
 			)
 			(symbol "Conn_01x04_1_1"
-				(rectangle
-					(start -1.27 -4.953)
-					(end 0 -5.207)
...
```

bitaxeGamma.kicad_pro — new DRC rules introduced with v9 project (selection from diff):

```
+        "creepage": "error",
+        "footprint_filters_mismatch": "ignore",
+        "hole_to_hole": "error",
+        "mirrored_text_on_front_layer": "warning",
+        "nonmirrored_text_on_back_layer": "warning",
+        "text_on_edge_cuts": "error",
+        "track_angle": "error",
+        "track_segment_length": "error",
-          "td_onpadsmd": true,
+          "td_onpthpad": true,
+          "td_onsmdpad": true,
-          "td_onviapad": true
+          "td_onvia": true
+    "layer_pairs": [],
+        "flipBoard": false,
```

Removed old BOM (Manufacturing Files/bitaxeGamma BOM.csv) — first rows, showing 602-era BOM structure with DK part numbers:

```
Qty,Reference,Value,Footprint,DK,PARTNO,DNP
1,C6,4700pF,Capacitor_SMD:C_0402_1005Metric,490-1309-1-ND,GRM155R71E472KA01D,
1,J1,54-00164,bitaxe:TENSILITY_54-00164,839-54-00164CT-ND,54-00164,
1,J5,USB_C_Receptacle_USB2.0,bitaxe:USB_C_Receptacle_GCT_USB4105-xx-A,2073-USB4105-GF-ACT-ND,USB4105-GF-A,
1,J6,Conn_01x04,bitaxe:470531000,WM4330-ND,470531000,
```

## README at gamma-603

Note: the file is `readme.md` (lowercase), 5318 bytes. It still instructs "Gerbers are in the `Manufacturing Files` dir" — but the gamma-603 diff REMOVED the entire Manufacturing Files directory, so the readme's gerber pointer is stale at this tag. Full content verbatim (base64-decoded via `gh api repos/bitaxeorg/BitaxeGamma/contents/readme.md?ref=gamma-603`):

````markdown
```
Open Source is Intrinsic to Bitcoin
```
# The bitaxeGamma
bitaxe is a fully open source Bitcoin ASIC miner aimed at decentralizing mining. bitaxeGamma is the 5th major revision of the bitaxe that now includes the BM1370 ASIC from the Antminer S21 Pro

![bitaxeUltra assembled](doc/gamma.png)

## Goals
- **Easy**: Just plug it in and mine Bitcoin over WiFi. No external computer needed.
- **Practical**: low cost, low noise, low power, low maintenance. You can run this at home.
- **ASIC Power**: High efficiency and hashrate, based on the latest and greatest Application Specific Integrated Circuits.
- **Versatile**: Mine to any StratumV1 pool, Lottery mine, Solo mine, Or hack it to do whatever you want.
- **Bitcoin Ethos**: Fully open source, permissionless and decentralized to support the worldwide freedom money.

## ASIC
At the heart of the bitaxeGamma is a BM1370 Bitcoin mining ASIC from the Antminer S21 Pro from Bitmain. It's not open source.

- Bitmain claims the BM1370 has 15 J/TH efficiency. We can get pretty close to that with the BitaxeGamma
- The Antminer S21 Pro has a nominal hashrate of 234 TH/s. There are 3 hashboards with 65 chips each, for a total of 195 chips. The bitaxeGamma has a single one of these chips. That means _about_ 1.2 TH/s per bitaxeGamma. Initial testing looks good!
- The BM1370 is brand new and isn't available individually yet. The best place to get these chips is right out of a S21 Pro.
- The BM1370 has a different footprint and pinout from the BM1368, BM1366, BM1397 and BM1387 in previous bitaxe.

## Current Status
- Prototype BitaxeGamma 600x have been built and are hashing! There might still be HW issues.
- initial BM1370 firmware support has been added to [esp-miner](https://github.com/skot/esp-miner) This still needs some work.
- Be sure to check the [HW issues](https://github.com/skot/bitaxe/issues) for known bugs, reworks and errata.
- This is an _advanced_ build! You can do it, but if you're not looking for a project, it might be best to buy one pre-assembled from one of the [many sellers](https://bitaxe.org/legit.html). Check [Skot's method](assembly.md) of hand assembling PCBs.

## PCB Hardware
This repo contains all of the design files for the PCB. [KiCAD](https://www.kicad.com) software is used. There is a BOM file for all of the components that get soldered to the PCB. 

- Order PCBs from your favorite PCB shop, like [JLCPCB](https://jlcpcb.com), [SeeedStudio](https://www.seeedstudio.com/fusion_pcb.html) or [PCBWay](https://www.pcbway.com)
    - Gerbers are in the `Manufacturing Files` dir. PCBs are 4-layer, 6mil trace/space and 0.3mm hole compatible. 1oz outer / 0.5oz inner layer thickness works well.
    - Make sure to order stencils too. These are the "paste" layers in the gerbers folder. one for top and one for bottom.
- All PCB parts except the ASIC are available from [DigiKey](https://www.digikey.com/en/products) and others. You can find Digikey part numbers on the DK tab of the BOM

## Extra Hardware
There are a few other hardware components that are needed for a complete bitaxe.

- **Heatsink**
	- [40x40mm heatsink and 5V fan](https://www.aliexpress.com/item/2251832861666365.html) from a random AliExpress seller. The fans are crap, but the heatsinks are good.  
- **Fan**
	- You **must** have active cooling on the bitaxe. The heatsink alone is not enough.
	- The Bitaxe has a connector for a 4pin, 5V PWM fan. 40mm square, 20mm thick fans work nicely with the suggested heatsink. Make sure to get a 5V fan! 12V will not work.
	- Upgrade your fan with the [Noctua NF-A4x10](https://noctua.at/en/nf-a4x10-5v-pwm) 5V 4-Pin fan for a much more pleasant experience.
- **Thermal compound**
	- Use a good quality thermal compound between the heatsink and ASIC. [Thermal Grizzly Kryonaut](https://www.amazon.com/dp/B07FLL3QDZ) is recommended.  
- **Display**
	- Supports 0.91" SSD1306-based I2C OLED Module. [Example Amazon seller](https://www.amazon.com/gp/product/B08ZY4YBHL). Make sure to get the male pins to interface with the Bitaxe PCB. 
- **Power Supply**
	- **5V DC Only!** Anything else will damage the Bitaxe. Be careful and double-check your power supply is 5V. Many other voltage power supplies use the same connector.
	- [30W 5VDC Power supply](https://www.amazon.com/MTDZKJG-100-240V-Converter-Transformers-5-5x2-5mm/dp/B0CJHKS28K). The power supply needs to supply 3A (15W) and not drop below 5V. Often times you have to use a power supply rated for 25-30W to get this!
	- The bitaxe uses a 5.5x2.1mm, center-positive barrel jack. 5.5x2.5mm plugs have been known to work.
- **Stand**
	- The PCB has corner mounting holes. You're going to want a stand to mount your Bitaxe. Many excellent 3D printed designs are available.

## Firmware
- The [ESP-Miner](https://github.com/skot/ESP-Miner) has initial support for the BM1370 ASIC. Improvements are ongoing.



### ESP32 Programming Requirements
- As of the bitaxeUltra, all ESP32 programming is done through a USB-C cable and connector on the bitaxe. See [ESP-Miner](https://github.com/skot/ESP-Miner) for more details.

## More Information
- Project page at [bitaxe.org](https://bitaxe.org)
- [Open Source Miners United](discord.gg/osmu) Discord chat
- [building.md](building.md) for PCB ordering tips
- [assembly.md](assembly.md) for assembly tips
````

(Transcription note: the PCB-ordering bullet is reproduced as it appears in the raw file; minor list-indentation variants exist between the raw bytes and this rendering.)

## 603-question summary (official-603 vs ECO-603)

The official `gamma-603` tag contains the ECO-level fixes as part of the tag itself: commit 4bcb769 (2025-04-29) simultaneously "bumped version to 603", added NRSTO/NRSTI pulldowns (#36), fixed J3 partno (#28), cleaned mounting-hole dust (#32), and removed old manufacturing files; pullups for #25 (f513149) and USB ID pulldowns for #37 (4f7187e) followed the same day. Net schematic delta vs Gamma-602: 10 new 0402 resistors (R17–R21, R26 on the BM1370 sheet; R27–R30 on the ESP32 sheet; R24 on fan sheet), one removed connector (J7). The release published 2026-02-17 is those April-2025 hardware changes plus June-2025 cleanup (fan header J7 removal, silkscreen/DRC) and Feb-2026 cosmetics (3d models, worksheet) — the tag carried no fresh gerber/BOM set (Manufacturing Files were deleted, not regenerated), and no README/spec changes at all.
