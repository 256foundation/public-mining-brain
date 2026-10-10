# bitaxeorg/bitaxeGamma issue #6: unused level shifter inputs should not be left floating.

> Source: https://github.com/bitaxeorg/bitaxeGamma/issues/6
> Collected: 2026-10-07
> Published: 2024-09-25

- Repository: bitaxeorg/bitaxeGamma
- Type: issue
- Number: 6
- State: closed
- Author: skot
- Opened: 2024-09-25
- Closed: 2025-04-29
- Labels: bug

## Description

From the [SN74AVC4T774 datasheet](https://www.ti.com/lit/ds/symlink/sn74avc4t774.pdf)

> Since this device has CMOS inputs, it is very important to not allow them to float. If the inputs are not driven to either a high VCC state, or a low-GND state, an undesirable larger than expected ICC current may result. Since the input voltage settlement is governed by many factors (for example, capacitance, board-layout, package inductance, surrounding conditions, and so forth), ensuring that they these inputs are kept out of erroneous switching states and tying them to either a high or a low level minimizes the leakage-current.

We need to either connect the input B4 to ground, or tie DIR4 high to make B4 an output.

<img width="502" alt="image" src="https://github.com/user-attachments/assets/2eefeec2-4d6b-4a88-b04f-223bcbbbb5b7">


## Comments

### skot on 2025-04-29

this has been fixed. 

<img width="679" alt="Image" src="https://github.com/user-attachments/assets/496f1520-e003-42b1-a510-cfbcdeab204c" />
