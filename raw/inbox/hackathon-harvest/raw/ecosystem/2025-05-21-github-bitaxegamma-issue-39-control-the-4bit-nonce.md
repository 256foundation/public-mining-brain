# bitaxeorg/bitaxeGamma issue #39: control the 4bit nonce.

> Source: https://github.com/bitaxeorg/bitaxeGamma/issues/39
> Collected: 2026-10-07
> Published: 2025-05-21

- Repository: bitaxeorg/bitaxeGamma
- Type: issue
- Number: 39
- State: closed
- Author: g1ass1
- Opened: 2025-05-21
- Closed: 2025-05-21
- Labels: none

## Description

is there a way to control or limit how the device interacts with the mining loop.  specifically, the 4byte nonce in the block header. 
I see how this can be done with extra nonce easily.  is the nonce controlled via asci hardware or the code.

## Comments

### skot on 2025-05-21

there is some rudimentary control over the nonce range that the ASIC rolls through. This is used when the ASICs are in long chains so that they don't duplicate work.

This is the hardware repo, the [esp-miner](https://github.com/bitaxeorg/esp-miner) or even better the [OSMU Discord](https://discord.gg/osmu) would be more appropriate for this discussion.
