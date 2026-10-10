# bitaxeorg/bitaxeGamma issue #7: Switch from SN74AVC4T774 (AVC) SN74AXC4T774 (AXC)

> Source: https://github.com/bitaxeorg/bitaxeGamma/issues/7
> Collected: 2026-10-07
> Published: 2024-10-03

- Repository: bitaxeorg/bitaxeGamma
- Type: issue
- Number: 7
- State: open
- Author: benjamin-wilson
- Opened: 2024-10-03
- Closed: n/a
- Labels: none

## Description

The SN74AXC4T774  is a drop in replacement - I would also suggest using the WQFN package as it is more stocked and 2/3 the cost. 
"The AXC is faster, has a wider supply range and guarantees glitch free power up."

https://www.ti.com/lit/ds/symlink/sn74axc4t774.pdf?ts=1727875925731&ref_url=https%253A%252F%252Fwww.ti.com.cn%252Fproduct%252Fzh-cn%252FSN74AXC4T774%253FkeyMatch%253DSN74AXC4T774%2526tisearch%253Duniversal_search%2526usecase%253DGPN-ALT

## Comments

### person65278 on 2025-02-02

so what would happen if i swapped  it to SN74AXC4T774PWR from digi key. just unsoldered the old and slapped it on there?

### koendv on 2025-07-23

There is one difference: the SN74AXC4T774 has 71k internal pull-down resistors, the SN74AVC4T774 not. See datasheet. You can leave a SN74AXC4T774 data input (A0 - A3, B0 - B3) floating, a SN74AVC4T774 not.
