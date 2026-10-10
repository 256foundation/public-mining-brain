# 256foundation/emberone00-pcb issue #39: Add USB-C Power Delivery sink support

> Source: https://github.com/256foundation/emberone00-pcb/issues/39
> Collected: 2026-10-07
> Published: 2025-05-01

- Repository: 256foundation/emberone00-pcb
- Type: issue
- Number: 39
- State: closed
- Author: mailinger-mate
- Opened: 2025-05-01
- Closed: 2025-06-09
- Labels: none

## Description

The EmberOne/00 currently accepts 12–24 V via a barrel jack but cannot negotiate USB-C Power Delivery. Adding PD sink support will allow the board to draw up to 20 V @ 5 A (100 W) directly from USB-C chargers, improving flexibility for field power.

**Objectives**  
- Negotiate and accept 20 V @ 5 A (100 W) over USB-C PD 3.0  
- Feed negotiated VBUS directly into the existing 12–24 V input net  
- Minimize impact on the current power-train (no additional DC–DC stages or firmware changes)

**Proposed Changes**  
1. **Add a Type-C receptacle** footprint rated for 5 A, if not already present.  
2. **Add STUSB4500 PD or other sink controller** in “auto-run” mode to negotiate 5 A@20 V on the CC lines.  
3. **Include supporting passives**: CC pull-resistors, VBUS discharge MOSFET (optional), TVS diode for surge protection.  
4. **Route negotiated VBUS** from the PD controller into the VIN net (12–24 V domain).
5. **Update PCB layout & DRC** to meet USB-C/C-EPR creepage/clearance and 5 A copper width requirements.  
6. **Optional**: add a simple power-path mux (diode or ideal-diode scheme) if barrel-jack coexistence is needed.
7. **Revise BOM** to include:
   - STUSB4500 IC  
   - USB-C 5 A receptacle  
   - CC resistors, MOSFETs/TVS, small passives

**Rough BOM cost**
| Component                           | Unit price             |
|----------------------------|------------------|
| STUSB4500 PD sink IC        |        US $ 2.11      |
| USB-C 5 A receptacle          |        US $ 0.92     |
| Passives & TVS diode           |       US $ 0.50*    |
| **Total incremental BOM**  | **≈ US $ 3.50**  |

**Acceptance Criteria**  
- Board powers up and negotiates 20 V @ 5 A from a compliant PD charger  
- No changes required to the rest of the power-train or firmware  
- Layout passes clearance checks for 20 V and high-current USB-C  
- BOM updated and documentation (silkscreen/schematic) reflects new components  

**References**  
- [STUSB4500 datasheet & application notes](https://www.mouser.com/c/semiconductors/interface-ics/usb-interface-ic/?series=STUSB4500)
- [USB Type C Connectors USB Connectors - Mouser Electronics](https://www.mouser.com/c/connectors/usb-connectors/?product=USB+Type+C+Connectors)
- [USB-IF Type-C Spec (Release 2.0, Aug 2019)](https://www.usb.org/sites/default/files/USB%20Type-C%20Spec%20R2.0%20-%20August%202019.pdf) See Section 3.2.1, “Reference Footprint for a USB Type-C Full-Featured Receptacle” (Figures 3-8 through 3-10) for recommended land patterns and mechanical dimensions. 

## Comments

### skot on 2025-05-01

USB-C power would be cool, but I think less practical for people who want to use several emberOne in a system. The most practical setup there would be a power bus bar, connecting several in parallel. That gets harder with USB-C.

USB-C power would be great for single emberOne setups. The thing I can't wrap my head around (same problem on Bitaxe); we use USB-C for data. Do we add separate USB-C ports for power and data? That gets confusing. There are some options for USB-C PD _and_ data on a single port but afaik this requires the user to buy an expensive adapter/cable to use both. Maybe you can ask ChatGPT about that 😉

### mailinger-mate on 2025-05-02

Thank you @skot, I didn't mean to be impersonal, im just lame in this subject and need help from ChatGPT.

How about using the USB-C for data only if the PD connection cannot be negotiated for the 100W needed?

A. With the barrel-jack support that would require more parts for OR-ing with diodes and for protection
B. Removing the barrel-jack: fewer parts, no OR-ing circuitry, simpler layout, and a single negotiated PD voltage to design around. Just keep the Type-C footprint, wire CC1/CC2 into your PD sink IC, beef up the VBUS copper for 5 A.

What do you think?

### skot on 2025-06-09

In an effort to keep things simple, I am not going to use USB-C PD for emberOne at this time.
