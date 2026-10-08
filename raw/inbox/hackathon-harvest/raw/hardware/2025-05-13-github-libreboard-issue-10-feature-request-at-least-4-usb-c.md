# 256foundation/libreboard issue #10: Feature request: at least 4 USB-C ports

> Source: https://github.com/256foundation/libreboard/issues/10
> Collected: 2026-10-07
> Published: 2025-05-13

- Repository: 256foundation/libreboard
- Type: issue
- Number: 10
- State: closed
- Author: rkuester
- Opened: 2025-05-13
- Closed: 2025-09-24
- Labels: enhancement

## Description

The Libre Board should have at least four USB-C ports in addition to the power and diagnostic port currently adjacent to the SD card slot.

The design currently has only two, but I think that's insufficient. Two ports allows for only one hash board plus one accessory (USB drive, keyboard, etc.); however, one of our modular system's selling points is that you can connect multiple hash boards via USB. One of the firmware's selling points is that it can talk to a variable number and types of hash boards, connected via USB. Thus I believe the out-of-the-box hardware should be able to show off these features without resort to an external hub.

Having four ports allows for three hash boards plus one accessory. Additionally, the design of ICs and connectors is such that four ports is like as easy to design-in as three ports.

If board space is an issue, I'd consider shifting the MIPI, HDMI, and Ethernet connectors over and eliminating the space between the Ethernet and HDMI connector.

## Comments

### Schnitzel on 2025-06-09

this has been implemented in the newest version - see 2 USB3 stacks on the top:

![Image](https://github.com/256-Foundation/Libre-Board/blob/main/assets/renders/face_top.png?raw=true)

this is not routed yet, also there is no USB controller yet, leaving this open until we have that.
