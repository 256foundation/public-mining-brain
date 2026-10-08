# bitaxeorg/ultraHex issue #37: Reset signals connected in parallel instead of series

> Source: https://github.com/bitaxeorg/ultraHex/issues/37
> Collected: 2026-10-07
> Published: 2024-05-15

- Repository: bitaxeorg/ultraHex
- Type: issue
- Number: 37
- State: closed
- Author: macphyter
- Opened: 2024-05-15
- Closed: 2024-05-25
- Labels: none

## Description

As suggested on the Discord channel, perhaps we should connect the ASIC reset signal to each ASIC individually within the voltage domain instead of passing it through the ASIC chain.  This should avoid any delays on the reset and have all the ASICs come out of reset at the same time.

## Comments

### macphyter on 2024-05-25

I eliminated all the RESET signal passthroughs on all the ASICs by connecting the signal in parallel within the domains, and directly through the level translators.  The RESET signal should get propagated to all ASICs at once now.
Fixed on Hex v304.


### macphyter on 2024-05-25

This change was reverted back to the serial passthrough reset signals.  After some discussion, it was decided that the serial passthrough reset works just fine, and there's no reason to change it.  There may even be a good reason that Bitmain uses this scheme, besides layout convenience.  In any case, there's no need to introduce risk to the design.
