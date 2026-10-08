# bitaxeorg/ultraHex issue #29: optimize voltage regulator input and output capacitors

> Source: https://github.com/bitaxeorg/ultraHex/issues/29
> Collected: 2026-10-07
> Published: 2024-04-22

- Repository: bitaxeorg/ultraHex
- Type: issue
- Number: 29
- State: closed
- Author: skot
- Opened: 2024-04-22
- Closed: 2024-06-04
- Labels: enhancement

## Description

From a Discord chat today, there are some things on the TPS546 input and output cap filter sections that could be improved.

<img width="1283" alt="image" src="https://github.com/skot/bitaxeHex/assets/140785/2fbbae62-77b7-46ad-9af5-072293a57b3a">
<img width="656" alt="image" src="https://github.com/skot/bitaxeHex/assets/140785/88d53938-8e46-49ef-8f8e-7b0a7aadb1da">

Switch electrolytic caps to ceramic. This isn't super straight forward because there aren't direct ceramic replacements for the 180uF el caps. 
- Try checking the OUTPUT_CAP_TYPE = ceramic option in Webench and see what they reccommend
- check out this PDF from K1, especially the bit about Antiresonance
[emi-murata.pdf](https://github.com/skot/bitaxeHex/files/15066768/emi-murata.pdf)
- LCSC has some [100uF 16V ceramic](https://www.lcsc.com/product-detail/Multilayer-Ceramic-Capacitors-MLCC-SMD-SMT_Chinocera-HGC1210R5107M160NSVK_C7432790.html) capacitors that could work?

## Comments

### macphyter on 2024-06-04

Replaced 180 uF electrolytic capacitors with 2x 100 uF ceramic capacitors.  Rearranged some regulator caps to get them out from under the heatsink.  Selected new low-ESR caps all around.
Fixed in v304.
