# Proof Of Print - Filament Dryer Prototype

> Source: https://forum.heatpunks.org/t/proof-of-print-filament-dryer-prototype/269
> Collected: 2026-10-10
> Published: 2026-05-05
> Registry ID: heatpunks-forum

PizzAndy | 2026-05-05 17:42:17 UTC | #1

Hey gang! Now that April craziness is behind me and the 2026 conference is in the books, I finally have a minute to do the write up on my filament dryer.

[![POP-FD1 iso beauty shot](https://forum.heatpunks.org/uploads/default/optimized/1X/945bad8bfb0b3fb24ac0d97a8b805aa0710d22b8_2_333x500.jpeg)POP-FD1 iso beauty shot1920×2880 843 KB](https://forum.heatpunks.org/uploads/default/original/1X/945bad8bfb0b3fb24ac0d97a8b805aa0710d22b8.jpeg)

---

## Overview

I put together a filament dryer powered by a Canaan Avalon Nano 3S.

[![Nano 3S](https://forum.heatpunks.org/uploads/default/optimized/1X/68ad4c39d68c5a42e32aa2cef6fe5831a678e2a2_2_250x250.jpeg)Nano 3S800×800 33.5 KB](https://forum.heatpunks.org/uploads/default/original/1X/68ad4c39d68c5a42e32aa2cef6fe5831a678e2a2.jpeg)

Compact, self-contained unit that dries filament while producing up to ~6 TH/s.

Project kicked off March 22 after securing a table for RMRRF, with a working demo shown April 18–19.

This is most likely an easier sell for a consumer product for Proof Of Print. This being system agnostic, is certainly more appealing to those who already have 3D Printers they are satisfied with.

---

## Why Filament Drying Matters

Most common printing materials are hygroscopic, they absorb moisture from the air over time.

When that happens, print quality drops off quickly:

- Steam bubbles and inconsistent extrusion

- Increased stringing

- Poor layer adhesion

- Rough surface finish

For materials like Nylon, and TPU, keeping filament dry is critical if you want consistent results.

At a basic level, filament drying just requires controlled heat and airflow, which lines up well with the kind of steady, low-grade heat small mining hardware produces.

---

## Build Photos

[![2026-04-26_0001](https://forum.heatpunks.org/uploads/default/optimized/1X/1ec95b1dc0fa10482dda0ac0987fd032359ef417_2_333x500.jpeg)2026-04-26_00011920×2880 843 KB](https://forum.heatpunks.org/uploads/default/original/1X/1ec95b1dc0fa10482dda0ac0987fd032359ef417.jpeg)

[![2026-04-26_0006](https://forum.heatpunks.org/uploads/default/optimized/1X/a9cfc8e4f921fb258214c77a7176526a91c624fa_2_345x230.jpeg)2026-04-26_00061920×1280 471 KB](https://forum.heatpunks.org/uploads/default/original/1X/a9cfc8e4f921fb258214c77a7176526a91c624fa.jpeg)

[![image](https://forum.heatpunks.org/uploads/default/optimized/1X/a11c086bd2585a1def3f8b18c6909df2c5a57bbe_2_432x500.jpeg)image595×688 80.8 KB](https://forum.heatpunks.org/uploads/default/original/1X/a11c086bd2585a1def3f8b18c6909df2c5a57bbe.jpeg)

---

## Key Specs

- ASIC hardware: Avalon Nano 3S

- Power: ~140W

- Hashrate: ~6 TH/s

- Enclosure size: 230 × 230 × 330 mm (9.1 × 9.1 × 13.0 in)

- Heat management:

    - Replaced stock (3×) 50 mm fans to (2×) 80 mm fans for improved packaging and ducting

---

## Comparison to Commercial Filament Dryers

For reference, this sits very close to something like the [Sovol SH02](https://www.amazon.com/dp/B0D4YXF8V6?th=1).

[![SOVOL SH02](https://forum.heatpunks.org/uploads/default/optimized/1X/b8793f4b18b5d5ad236a2f39f49c86f33ba548ad_2_240x250.jpeg)SOVOL SH021401×1454 230 KB](https://forum.heatpunks.org/uploads/default/original/1X/b8793f4b18b5d5ad236a2f39f49c86f33ba548ad.jpeg)

**Sovol SH02:**

- ~150W PTC resistive heater

- Preset temperature range (40–70°C)

- Built-in touchscreen control

- Internal circulation fan(s)

[![SH02-Internals](https://forum.heatpunks.org/uploads/default/optimized/1X/9c1fa458df6ba88ef3a8a7e0789e0bfa3a1dc89a_2_228x249.jpeg)SH02-Internals1920×2105 679 KB](https://forum.heatpunks.org/uploads/default/original/1X/9c1fa458df6ba88ef3a8a7e0789e0bfa3a1dc89a.jpeg)

At roughly the same power level, it ends up being a pretty direct apples-to-apples comparison. The thing about this dryer though is it’s a piece of garbage. It constantly shuts off from overheating, the filament feed path makes no sense. The lid is a pain in the ass because the hinge is at the back. Both spools feed out through the lid, so swapping out a spool is a pain because the already fed spool forces the lid closed. I could go on. This thing clearly is a super high markup, get it out quickly, device made to disposable standards.

---

## Electronics + Control

- Controller: Raspberry Pi Zero - powered from LED socket

- Display: 3.5” Touchscreen driven directly from the Pi

- Communication: WiFi to the Nano 3S

- Network: Uses hotspot from 3D printer prototype

- Humidity sensor: SHT31-D

Keeps everything self-contained and portable while still allowing direct interaction with the miner. Theoretically one could program the printer to send out specific commands to the dryer to automatically correspond to the filament type.

[![POP-FD1 test setup, Standby screen shown](https://forum.heatpunks.org/uploads/default/optimized/1X/e01902719789c9dde1ddc58b21d7b57e5401e82f_2_345x194.jpeg)POP-FD1 test setup, Standby screen shown1920×1080 478 KB](https://forum.heatpunks.org/uploads/default/original/1X/e01902719789c9dde1ddc58b21d7b57e5401e82f.jpeg)

[![Current User Interface](https://forum.heatpunks.org/uploads/default/optimized/1X/15642b17b869772f11671218755a85bfc72b6bf7_2_345x207.png)Current User Interface800×480 22.1 KB](https://forum.heatpunks.org/uploads/default/original/1X/15642b17b869772f11671218755a85bfc72b6bf7.png)

---

## Design Notes

### Airflow

- Fan swap was driven primarily by space constraints and ducting layout

- Curved lid promotes more uniform air distribution across the spool

~140W ends up being a really nice operating point for desiccation. Enough energy to maintain useful drying temps without overshooting or requiring aggressive throttling. It would be nice to include the PSU in the enclosure somehow to assist in the heat generation; that brick gets quite hot.

[![POP-FD1 Ducting](https://forum.heatpunks.org/uploads/default/optimized/1X/246964a184a9a41b86f8e3225a40e915582417ce_2_289x250.jpeg)POP-FD1 Ducting1920×1657 599 KB](https://forum.heatpunks.org/uploads/default/original/1X/246964a184a9a41b86f8e3225a40e915582417ce.jpeg)

[![Miner ducting exploded view](https://forum.heatpunks.org/uploads/default/optimized/1X/2b974f5245c0590a960dfa27250a52961390509a_2_341x250.png)Miner ducting exploded view731×535 104 KB](https://forum.heatpunks.org/uploads/default/original/1X/2b974f5245c0590a960dfa27250a52961390509a.png)

### Assembly

Everything is cram packed in this unit. There is basically no room to spare.This was one of the trickier parts of the build. It’s one thing to fit everything in a space claim, it’s an entirely different thing to fit everything together in a specific sequence so there’s access to the relevant fasteners. Good example below is the big section removed from the inlet duct in order to accommodate the display and its connectors. The front panel swings out in order to seat the mining duct assembly.

[![Exploded view 1](https://forum.heatpunks.org/uploads/default/optimized/1X/7b63d523710d9ddf2696d006673eed9a8e3d168a_2_323x500.png)Exploded view 1467×721 71.4 KB](https://forum.heatpunks.org/uploads/default/original/1X/7b63d523710d9ddf2696d006673eed9a8e3d168a.png)

### Materials

All printed components are [3D-Fuel PCTG](https://t.co/0bEiFshBmU)
(Shameless plug- coupon code **PROOFOFPRINT** for 10% off if anyone wants the best USA made filament)

### Why the Avalon Nano 3S

This build was only practical because of how open the Avalon ecosystem is.

Firmware and API access made it straightforward to:

- Monitor temps and hashrate

- Communicate over WiFi from an external controller

- Build a custom UI without fighting the stack

Nano 3S Repos:

- Firmware: [Canaan.io · GitHub](https://github.com/Canaan-Creative)

- API / examples: [https://github.com/Canaan-Creative/avalon-examples](https://github.com/Canaan-Creative/avalon-examples)

---

## Notes from Rocky Mountain RepRap Festival 2026

Bringing this to RMRRF was a great time. Different audience than typical bitcoin events, but people immediately understood the “heater that does work anyway” concept. Showed them a whole new side to bitcoin they never considered. I highly recommend other Heatpunks attend relevant cross-over industry events/expos/conventions to really inject yourself and what we’re doing into the broader public eye.

[![POP-FD1 (20)](https://forum.heatpunks.org/uploads/default/optimized/1X/4b1e2ba12e232cf8b3116eb04abfe8aeaab89349_2_690x388.jpeg)POP-FD1 (20)1920×1080 604 KB](https://forum.heatpunks.org/uploads/default/original/1X/4b1e2ba12e232cf8b3116eb04abfe8aeaab89349.jpeg)

---

## Development Direction

Currently pushing on a few fronts:

- Moving away from the stock low / medium / high power modes toward discrete temperature set points. The goal is to run the miner in a true closed-loop configuration where dryer temperature/humidity directly drives hashrate and power draw via firmware control, rather than selecting from predefined power tiers.

- More direct firmware-level control to tighten both temperature and humidity regulation, using feedback from the SHT31-D or similar

- Improving airflow uniformity across the spools

- A port of Mujina to the Nano 3S would be very interesting here. That’s far beyond my abilities, but It would open up much finer-grained control than what’s available today

- Same idea with something like a LibreBoard. More inputs for additional sensors (temp, humidity, airflow, etc.) would make this kind of system much more capable. Could potentially even make a hat module for a Libreboard to run the 3D Printer directly.

I’ve started conversations with Canaan about a potential production-oriented version of something like this. It’d be a great candidate in terms of required development time. It’s basically a fancy wrapper for their existing product save for some interface/firmware tweaks. In that case, the Raspberry Pi Zero would be eliminated in favor of the on board linux box running both interface and mining operations.

If the Canaan route doesn’t pan out, the hash boards with the BZM2 chips being developed for the POP build plate could easily be repurposed for this application.

Longer term, I plan to release the files for this prototype version so others can build on it, but want to iterate a bit further first. This is still a prototype even if it is easy on the eyes.

I also spoke with a couple companies at RMRRF that showed interest in offering this as a kit, which could be another path worth exploring.

---

## Conclusion / Takeaways

- ~140W lands in a very usable range for small-scale thermal applications like filament drying

- The current limitation is control, not hardware. Moving to discrete temperature targets and tighter firmware integration is the obvious next step

- Open firmware and accessible APIs are what make builds like this viable, especially this quickly

This is a simple implementation, but it maps cleanly onto more advanced systems once the control side is more developed. Canaan seems open to our Heatpunk ways too so that’s exciting!

Always be building.

-PizzAndy

-------------------------

tronsington | 2026-05-06 20:27:43 UTC | #2

do you have any additional photos of the Nano 3s teardown? Curious what the internals look like

-------------------------

PizzAndy | 2026-05-07 19:30:18 UTC | #3

Apologies for the kapton tape obscuring the control board, I can yank it off if you’re more curious. It doesn’t have it on there normally. That’s my addition.

As a bonus:
[Here’s a link to the Hashboard’s CAD file I made](https://github.com/PizzAndy/Avalon_Nano3s-mod/blob/master/Avalon-nano-3s_hashboard.STEP)

[![Nano3s_innerds (4)](https://forum.heatpunks.org/uploads/default/optimized/1X/afcbb1eb21a63e98f95da8696a27e15040346d0b_2_138x250.jpeg)Nano3s_innerds (4)1868×3368 1.04 MB](https://forum.heatpunks.org/uploads/default/original/1X/afcbb1eb21a63e98f95da8696a27e15040346d0b.jpeg)

[![Nano3s_innerds (3)](https://forum.heatpunks.org/uploads/default/optimized/1X/73e5678d55da25668b47d0b9c49c210b1a795c47_2_148x250.jpeg)Nano3s_innerds (3)1920×3235 707 KB](https://forum.heatpunks.org/uploads/default/original/1X/73e5678d55da25668b47d0b9c49c210b1a795c47.jpeg)

[![Nano3s_innerds (2)](https://forum.heatpunks.org/uploads/default/optimized/1X/42b8497ee86c717ce0d1ebc89e962752f34d8fb2_2_345x136.jpeg)Nano3s_innerds (2)1920×761 243 KB](https://forum.heatpunks.org/uploads/default/original/1X/42b8497ee86c717ce0d1ebc89e962752f34d8fb2.jpeg)

[![Nano3s_innerds (1)](https://forum.heatpunks.org/uploads/default/optimized/1X/7c370b30924252c78195d7673a9c8fb8a0d37ba2_2_345x149.jpeg)Nano3s_innerds (1)1920×832 258 KB](https://forum.heatpunks.org/uploads/default/original/1X/7c370b30924252c78195d7673a9c8fb8a0d37ba2.jpeg)

-------------------------

tylerkstevens | 2026-05-16 15:33:01 UTC | #4

This is epic. Congratulations.
