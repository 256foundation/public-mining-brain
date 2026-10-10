# 256foundation/emberone00-pcb issue #18: Double check BM1362 footprint spacing

> Source: https://github.com/256foundation/emberone00-pcb/issues/18
> Collected: 2026-10-07
> Published: 2025-02-25

- Repository: 256foundation/emberone00-pcb
- Type: issue
- Number: 18
- State: closed
- Author: skot
- Opened: 2025-02-25
- Closed: 2025-04-09
- Labels: none

## Description

It seems like the BM1362 pins extend a little too close to the center power pads. Double check the spacing with the S19j Pro hashboard footprint

## Comments

### skot on 2025-03-11

In 67fa04b I changed the spacing between the pads and the pins and moved the VDD pad up a little bit.

I think there still might be an issue with the pin pitch.

### econoalchemist on 2025-03-12

I see three potential variables that could complicate efforts to ensure the spacing is correct:

1) The pin spacing from chip to chip might vary. Could be worth measuring two or more chips to test this theory. 

2) The PCB manufacturer may have a loose tolerance that misplaced some of the pin pads. Could be worth measuring the PCB itself to ensure it matches the requested design measurements. 

3) The required precision might be beyond the resolution capabilities of the imaging equipment. Could be helpful to sharpen the image in GIMP or Photoshop or an online tool prior to feeding the image to the measuring software to mitigate aliasing.  

### skot on 2025-03-14

I hot glued the chip at 90º to the PCB, with the pins lined up as best as I could. Then took a pic through the microscope with the PCB at 45º.

<img width="395" alt="Image" src="https://github.com/user-attachments/assets/319fd90b-ef8e-4ae2-957e-e15d62362442" />

Left side is the emberOne/00 v2 pads. right side is a BM1362AA chip. It looks like at the bottom of the image the top of the pin is lined up with the top of the pad. Then by the time we get to the top of the image, the pin and pad bottoms are aligned.

### skot on 2025-04-09

fixed in v3
