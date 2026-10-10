# bitaxeorg/bitaxe-raw issue #10: Fan default behavior seems intermittent

> Source: https://github.com/bitaxeorg/bitaxe-raw/issues/10
> Collected: 2026-10-07
> Published: 2026-03-19

- Repository: bitaxeorg/bitaxe-raw
- Type: issue
- Number: 10
- State: open
- Author: jayrmotta
- Opened: 2026-03-19
- Closed: n/a
- Labels: none

## Description

I've noticed the fan behavior of my Bitaxe change (on/off by default) almost randomly when I power it up. It happens both when I start it normally or in boot mode.

I'm often on edge because I'm afraid the firmware isn't holding the ASIC on reset and might be generating heat without the fan to help cool it off. Once it actually got really hot and I thought it was idle, luckily no apparent damage happened. 

More recently in this https://github.com/256foundation/mujina/pull/33#issuecomment-4092356822 we aren't sure how safe it would be to rely on a fan default behavior, curious to hear if that's a common observation among others as well.

## Comments

### rkuester on 2026-03-31

100% agree the fan does not reliably start at power-up. I have seen this on all of my three Bitaxe Gamma 601's here. Whether the ASIC is held in reset is a thermally-related but separate issue. Here's what I know about both:

### Fan
At least through (1fc7d60), the bitaxe-raw firmware is making no attempt to initialize the fan, so we're relying on the hardware default. According to the EM2101 fan controller [datasheet](https://ww1.microchip.com/downloads/aemDocuments/documents/MSLD/ProductDocuments/DataSheets/EMC2101-Data-Sheet-DS20006703.pdf) section 4.2, the fan should turn full-on at startup due to the R24 5.6k pull-up.

This appears to be unreliable, however. @skot and I have talked about this quite a bit, but to no avail. (I'm kinda surprised I never filed a bug over in [bitaxeorg/bitaxeGamma](https://github.com/bitaxeorg/bitaxeGamma/issues) against the hardware, but I don't see one.)

An interesting wrinkle: this initial setting only applies if the part is the EMC2101-R variant, and not its close cousin the EMC2101 variant. The Bill of Materials indeed calls for an EMC2101-R. Of the three Bitaxe Gamma 601s I have, only one of them[^1] has what purports to be the EMC2101-R variant. **However, even the unit with the EMC2101-R suffers intermittency.** 🤷‍♂️

[^1]: For what it's worth, all three came from PlebSource in early 2025, perhaps ordered a couple months apart. My guess is they're not the only Bitaxe manufacturer that might inadvertently substitute the wrong part here, not realizing there is a difference. 

There is a product ID readable via I2C with identifies which variant the part is, and I've just added logging to Mujina in 256foundation/mujina@46db975 which prints it out at debug level. The numbers on the packages are slightly different too[^2].

[^2]: ![Image](https://github.com/user-attachments/assets/a7a30d8b-7934-4dd4-9191-1c00a264ddc1) ![Image](https://github.com/user-attachments/assets/5586d3ae-3387-455f-98fd-faeea4c4a414)

### Reset
I made sure reset was held low coming out of power-up way back in 025901d, after anonymizing a fingerprint by touching the heatsink in just such a case. Surprisingly, with reset low the ASIC still seems to draw about 2 W. That's enough power to make a fanless 40mm heat sink uncomfortable (60-degC/140-degF?).

### Conclusion
In hardware, the regulator powering the ASIC turns on by itself, and this bitaxe-raw firmware does nothing to stop it. The firmware probably should turn it off to mitigate this issue. The fan turning on by itself is a nice to have, but the hardware probably shouldn't draw real power until software wants it to.
