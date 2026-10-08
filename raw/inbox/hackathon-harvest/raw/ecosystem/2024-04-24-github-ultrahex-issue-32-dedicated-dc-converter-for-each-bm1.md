# bitaxeorg/ultraHex issue #32: Dedicated DC converter for each BM1366?

> Source: https://github.com/bitaxeorg/ultraHex/issues/32
> Collected: 2026-10-07
> Published: 2024-04-24

- Repository: bitaxeorg/ultraHex
- Type: issue
- Number: 32
- State: closed
- Author: nikwest
- Opened: 2024-04-24
- Closed: 2024-05-03
- Labels: none

## Description

Sorry, that I use the issue tracker for this kind of generic question, but I don't know where else to put this.
I am about to build a bitaxeHex and was looking into more detail in the design and also other designs like the 0xaxe.
Everybody seems to go with a monolithic approach for providing power to all the ASICS from one source. But this doesn't seem to scale well to me. Wouldn't an approach to use a dedicated power of load regulator be more flexible and easier? Something like a 6A converter with programmable output (e.g. https://www.mouser.de/datasheet/2/1458/DS6203E_00-3104633.pdf). Costwise I don't think it makes a significant difference and it would open up the possibility to individually tune each BM1366 (not sure if that's possible at all though)?

## Comments

### nikwest on 2024-05-03

never mind. I guess you've been through all of that thinking before ;-)
Anyways the referenced part probably has to less Amperage anyways.
