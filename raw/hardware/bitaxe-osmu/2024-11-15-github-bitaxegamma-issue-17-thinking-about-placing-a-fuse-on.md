# bitaxeorg/bitaxeGamma issue #17: Thinking about placing a fuse on the 5 V input

> Source: https://github.com/bitaxeorg/bitaxeGamma/issues/17
> Collected: 2026-10-07
> Published: 2024-11-15

- Repository: bitaxeorg/bitaxeGamma
- Type: issue
- Number: 17
- State: open
- Author: etkaar
- Opened: 2024-11-15
- Closed: n/a
- Labels: none

## Description

While the Mean Well PSUs are short-circuit safe, it may be wise to place a fuse on the 5V input as MLCCs can fail and become very hot. Some users use high-power PSUs for multiple Bitaxes, so I am unsure if that would be safe without an extra fuse.

A Littlefuse 217 Series (fast) with up to 40 A interruption rating has a voltage drop of 130 mV at 4 A:
https://cdn-reichelt.de/documents/datenblatt/C400/217_ENG_DATASHEET.pdf

I welcome any feedback from electrical engineers!


## Comments

### etkaar on 2024-11-19

If addressed, this should be addresses as well, as it requires space on the PCB: https://github.com/skot/bitaxeGamma/issues/11

### skot on 2025-03-03

I don't think 130mV drop is going to be good with only 5V anyways.

Either way a traditional fuse is very bad user experience in my opinion. Also the overclockers are not going to like it. I would consider a resettable, adjustable eFuse... If you know of a good one.

We currently do have the ability to do overcurrent shutdown in the TPS546 voltage regulator.

### etkaar on 2025-03-04

Please have a look to the NerdQAxe:
https://github.com/BitMaker-hub/NerdQaxe

They actually use a SMD fuse, you can see it here:

![Image](https://github.com/user-attachments/assets/00277b06-e0de-40c9-8636-f6981d059198)

Safety is an issue since people will print PLA based housings which could burn like hell in case of a catastrophic failure. But maybe I am wrong and it is not required. It would be great if there would be someone who is more experienced than me to evaluate this.

### skot on 2025-03-04

Yes, As I mentioned above I don't think the is the right approach.
