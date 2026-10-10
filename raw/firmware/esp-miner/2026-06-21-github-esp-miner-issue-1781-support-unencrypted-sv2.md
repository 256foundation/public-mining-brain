# bitaxeorg/ESP-Miner issue #1781: support unencrypted sv2

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1781
> Collected: 2026-10-07
> Published: 2026-06-21

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1781
- State: closed
- Author: 0xf0xx0
- Opened: 2026-06-21
- Closed: 2026-07-05
- Labels: enhancement

## Description

[the spec states encryption is optional for lan and mandatory for remote conns](https://stratumprotocol.org/specification/04-protocol-security/). since we're for home miners, should we have an encryption toggle?

## Comments

### 0xf0xx0 on 2026-07-05

https://github.com/bitaxeorg/ESP-Miner/pull/1796#issuecomment-4881919459
> you've basically got it right on the split, small correction: it's not encryption that's optional on LAN, that part's always on (Noise_NX establishes the session unconditionally). what's optional/mandatory is specifically the auth step - verifying the server cert against the authority pubkey. that's the "optional LAN, mandatory remote" language.
