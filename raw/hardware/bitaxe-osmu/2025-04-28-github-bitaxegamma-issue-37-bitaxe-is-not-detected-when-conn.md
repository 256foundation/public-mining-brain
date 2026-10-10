# bitaxeorg/bitaxeGamma issue #37: Bitaxe is not detected when connected to a USB-C port

> Source: https://github.com/bitaxeorg/bitaxeGamma/issues/37
> Collected: 2026-10-07
> Published: 2025-04-28

- Repository: bitaxeorg/bitaxeGamma
- Type: issue
- Number: 37
- State: open
- Author: rkuester
- Opened: 2025-04-28
- Closed: n/a
- Labels: bug

## Description

A Bitaxe Gamma is not detected when connected to an upstream USB-C port. Presumably, this is due to lack of pull-downs on the Bitaxe's USB-C CC pins. USB Sources detect the attachment of devices through USB-C physical connections by utilizing the CC pins.

I have verified this behavior on both a modern MacBook Air and a Linux server with USB-C ports. Presumably, this would also be an issue with hubs that have USB-C ports facing downstream.

There is no issue when a Bitaxe is connected via a USB-C to USB-A cable, because USB-A ports detect attachment via devices pulling up D+ and or D- (in the Bitaxe's case, internally in the USB controller).

## Comments

### MyOwn2C on 2025-04-28

Known issue but not fixed. 
Only my oldest Ultra works with USB. 
All my other Supra (2x) and Gamma (3x) none of them worked with USB. 
I just use UART to update if webpage update does not work. 

### skot on 2025-04-28

Uuuf, you are totally right. I'm kicking myself for removing these pulldowns a while back. I'll get these put back on in future revs. In the mean time you'll have to use a USB-C to USB-A adapter and cable 😭

I swear I had a USB-C to C cable that magically worked.

### skot on 2025-05-12

- Connect a 5.1 kΩ resistor from CC1 to ground.
- Connect a 5.1 kΩ resistor from CC2 to ground.

### skot on 2025-07-03

I have heard that Bitaxes work on (some) USB-C ports that are not also Thunderbolt ports.

### skot on 2025-07-03

Confirmed adding 5.1k pulldown resistors on CC1 and CC2 on a BitaxeGamma 601 allows it to mount on my MacBook USB-C thunderbolt ports.

### skot on 2025-07-14

The work around if you want to use a thunderbolt USB port with a Bitaxe (or you have a Mac and only have thunderbolt USB ports) is to use a USB-C to USB-A adapter. 

<img src="https://github.com/user-attachments/assets/d78e578e-1632-48c6-8eb5-e5483259bc24" width=200px>

And then use a USB-A to USB-C cable with your adapter.

<img src="https://github.com/user-attachments/assets/daec5f41-c67c-4cd1-83c9-5559b1ebc330" width=200px>

And going forward I'll get this fixed on new Bitaxe HW revisions.

### NickNack67 on 2025-08-10

Couldn't we use 5.6k Ohm resistors to reduce BOM parts?

### skot on 2025-08-19

> Couldn't we use 5.6k Ohm resistors to reduce BOM parts?

technically, no.

>The USB-C specification defines the tolerance for the pull-up (Rp) and pull-down (Rd) resistors on the Configuration Channel (CC) pins to ensure proper detection and configuration of USB-C connections. According to the USB Type-C Cable and Connector Specification (Revision 2.2):

>Pull-Down Resistor (Rd):
>Nominal Value: 5.1 kΩ
>Tolerance: ±10%
>Range: 4.59 kΩ to 5.61 kΩ

a 1% tolerance 5.6k resistor could be as much as 5.656k which is greater than the 5.61k upper limit allowed by the USB spec.

In practice, _maybe_? Not sure it's worth it considering how many different USB hosts there are out there.

### skot on 2025-09-10

Looks like this bug was introduced on 204 hardware. everything prior to that _should_ be unaffected.

### jaymine-jvvs on 2025-11-04

The issue I'm having is it connects then disconnects just as fast I can't catch it to lock it in

### skot on 2025-11-04

> The issue I'm having is it connects then disconnects just as fast I can't catch it to lock it in

This is likely because esp-miner is crashing and restarting, in a loop. If you plug in your Bitaxe barrel power while holding the BOOT button, it should drop into the ESP32 bootloader. then with the bitaxe in the bootloader you can restore working firmware with https://flasher.bitaxe.org (use Chrome browser)
