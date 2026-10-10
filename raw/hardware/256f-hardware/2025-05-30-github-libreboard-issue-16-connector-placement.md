# 256foundation/libreboard issue #16: Connector Placement

> Source: https://github.com/256foundation/libreboard/issues/16
> Collected: 2026-10-07
> Published: 2025-05-30

- Repository: 256foundation/libreboard
- Type: issue
- Number: 16
- State: closed
- Author: econoalchemist
- Opened: 2025-05-30
- Closed: 2025-09-24
- Labels: none

## Description

## Considerations for Connector Placement

Among all the various connectors on the Libre Board, they can be separated into two general categories: externally accessible and internally accessible. External meaning that these are connectors that will require easy access once the board is installed in an enclosure. Internal access meaning that these are connectors that get plugged in during system assembly and then typically do not need to be readily accessible from outside. 

Keep in mind that matching the existing [Ember One 00 v4](https://github.com/256-Foundation/emberone00-pcb/tree/v4) configuration would be a good starting point. For example, the power input and USB-C data connector on the Ember One are on the same edge, opposite the ASIC chips; by placing the power and data connectors on the Libre Board along the matching edge when the mounting holes are aligned, we could make it possible for end-users to keep those wires contained in the back of their enclosure. Therefore, placing as many externally accessible connectors along the opposite edge would help facilitate making each of those readily available through the front of the enclosure.

With these two general categories in mind and taking into consideration pending feature requests, here are how all the connectors are separated in my opinion:

### Externally Accessible Connectors

Each of the following connectors would need to be placed along an edge so that they can be accessed via through holes in the enclosure. Ideally most of this could be placed opposite of the edge where the power input and USB3 double stacks are placed. However, not all of these would necessarily need to be placed along the same edge; for example, it might make sense to put the the power button, boot mode button, SD card slot, and LED indicator along a perpendicular edge from the rest of the connectors in this category so that they could be accessible from the top of an enclosure while the remaining connectors are accessible from the front of an enclosure. 

#### Top Edge
- Power Button
- Boot mode button
- SD Card slot
- LED indicator

#### Front Edge
- MIPI
- HDMI
- Ethernet
- Single USB-C port
- 4-pin JST SH connector

<br>

### Internally Accessible Connections:

Each of the following connectors can be separated into two more specific categories, those that need to be along the back edge of the board and those that are accessible perpendicular to the face of the board and that do not need to be along an edge at all. The connectors in this latter category could be placed closer to the center of the board or where ever they fit best to preserve space along the edges for the connectors that need edge placement. 

#### Back Edge
- Power Input (12-24v)
- USB3 Double Stack (x2)

#### Board Face
- Hashboard fans (x4)
- Raspberry Pi HAT
- Two 100-pin Compute Module connectors
- Battery
- Control board fan
- NVME SSD connector

For clarity, attached is an example graphic displaying what I'm calling the "top", "bottom", and "front" edges.

![Image](https://github.com/user-attachments/assets/37813f11-246e-4848-811f-ee7fb73c5b72)

## Comments

### Schnitzel on 2025-06-09

I've updated the complete design of the Libreboard according to the suggestions of @econoalchemist 

Updated rendering:

![Image](https://github.com/user-attachments/assets/be2fb670-f511-4cbf-a88a-fa9a096c8178)

A couple of remarks:

Top Edge:
- There are in total 3 LEDs (red and green by Raspi, plus the RGB LED that we also have on the EmberOne), I've put all of them at the Top Edge
- There is actually a fourth LED which is the M2 Slot Indicator LED, I've left that one next to the M2 slot, meaning it is not routed to any edge and can only be seen from within the enclosure.
- I moved the Battery into the PCB as there was no space for it, anyway I don't think it needs to be exposed to an edge.
- There is an USB2/USB-C connector that is used to flash the eMMC of the CM5, after that it probably will not be used anymore, as it does not provide USB3. As the power button and boot button are also on that Edge I've put this connector also there.

Front Edge:
- I did NOT place the 4-pin JST SH connector (Qwicc/STEMMA QT) on this edge, as I believe that any I2C boards would be internally to the enclosure and therefore is placed on the Board Top Face next to the M2 Slot

Back Edge:
- I aligned the position of the power input connectors to the same as on the Ember One (which I had to create a PR for: https://github.com/256-Foundation/emberone00-pcb/pull/43 as I need the position slightly different than it's currently on the emberone)

Board Face:
- Added the mentioned Qwicc connector

Therefore the connectors are now as following:

**Top Edge:**
-  Power Button
-  Boot mode button
-  SD Card slot
-  Red Power LED indicator
-  Green Activity LED indicator
-  RGB Status LED indicator

![Image](https://github.com/user-attachments/assets/ce234eaa-4a5e-4ed8-9eb2-12862a70d1d2)

**Front Edge:**
- MIPI
- HDMI
- Ethernet
- Single USB-C port

![Image](https://github.com/user-attachments/assets/c1310bef-df8f-4685-ac26-a89e9719bd93)

**Back Edge**
- Power Input (12-24v)
- USBC Double Stack (x2)

![Image](https://github.com/user-attachments/assets/abc741f5-3b7b-45dc-aaa3-adf8a893879d)

**Board Face**
- Hashboard fans (x4)
- Raspberry Pi HAT
- Two 100-pin Compute Module connectors
- Compute Module fan
- Battery
- M2/NVME SSD connector
- Qwicc/STEMMA QT 4-pin JST SH connector

Lets see if there is any other feedback

### rkuester on 2025-06-09

Nice! A few thoughts:

1. I love that the boot mode button will be accessible from the main, user-facing edge. Maybe it should not be as prominent and as easy to press as the power button. I'm picturing one of those right-angle, momentary push-buttons without a long plunger that has to be pushed with paper clip through a hole in the enclosure. Not a dealbreaker; just a suggestion.
2. @Schnitzel, I just want to confirm the top-edge USB port corresponds to J11 USB-C port on the front panel of the I/O breakout board. For software's sake, it's important they be the same; the USB ports aren't entirely fungible.
3. Maybe the emberOne LED should be aligned with the Libre Board's LED at the next opportunity.

### Schnitzel on 2025-06-18

@rkuester 

1. Boot Mode Button: Mhh good idea, will check what buttons I can find that we could put instead on it.
2. Correct the J11 USB-C connectors on the IO Board is the top-edge USB port. I chose specifically that one because this is the one that can be used for flashing, etc
3. LED: Good point, will put at the same place

### rkuester on 2025-06-18

> 3. LED: Good point, will put at the same place

Actually, I like where you have it—on the top edge, the user facing edge. I was thinking perhaps @skot could move the emberOne's LED to match if it's not too late.
