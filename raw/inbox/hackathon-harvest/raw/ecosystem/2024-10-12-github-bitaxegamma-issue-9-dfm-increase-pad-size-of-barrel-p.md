# bitaxeorg/bitaxeGamma issue #9: DFM - Increase pad size of barrel plug and inductor

> Source: https://github.com/bitaxeorg/bitaxeGamma/issues/9
> Collected: 2026-10-07
> Published: 2024-10-12

- Repository: bitaxeorg/bitaxeGamma
- Type: issue
- Number: 9
- State: open
- Author: benjamin-wilson
- Opened: 2024-10-12
- Closed: n/a
- Labels: bug

## Description

Increase the pad size of these two elements to provide more solder to the component - the barrel plug can be removed with a strong push of the thumb currently. 

## Comments

### 4xmajor on 2024-10-15

I have a few more suggestions/observations regarding these these parts...

1. Due to availability issues, I switched the barrel connector suggested in the schematic (54-00164) out for  PJ-036AH-SMT-TR. 

The pads and contacts are far more substantial than the 54-00164, and it is far more abundantly available (on DigiKey at least)... may be a better choice in general?

2. I have swapped out the suggested inductor (SLC1480-301ML)  with IHLP5050FDERR30M01 (Digikey 541-IHLP5050FDERR30M01CT-ND)

The package and solder pads are a little bit bigger and much better availability, but PCB needed a to be edited to squeeze it in!

EDIT: [PSPMAA1007-R30M-ANP-DC](https://www.lcsc.com/product-detail/Power-Inductors_PROD-Tech-PSPMAA1007-R30M-ANP-DC_C5273929.html) is another good alternative for L1

### skot on 2024-10-21

> I have a few more suggestions/observations regarding these these parts...
> 
> 1. Due to availability issues, I switched the barrel connector suggested in the schematic (54-00164) out for  PJ-036AH-SMT-TR.

funny story; we switched to 54-00164 previously because PJ-036AH-SMT-TR went 100% out of stock everywhere. It's wack-a-mole with these things. 


### BitMaker-hub on 2024-10-22

I also think 54-00164 is more standard, we can go furder and find compatible parts to it also. Sure there are more out there

### benjamin-wilson on 2024-11-02

Did this on 602 - sent to fab for verification
