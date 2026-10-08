# 256foundation/asic-rs issue #246: dont check for active hbs when sleeping

> Source: https://github.com/256foundation/asic-rs/issues/246
> Collected: 2026-10-07
> Published: 2026-04-30

- Repository: 256foundation/asic-rs
- Type: issue
- Number: 246
- State: closed
- Author: DanNicolau
- Opened: 2026-04-30
- Closed: 2026-04-30
- Labels: none

## Description

(no description)

## Comments

### DanNicolau on 2026-04-30

oops wrong repo

### b-rowan on 2026-04-30

It probably isn't a bad idea on our end?

### DanNicolau on 2026-04-30

I think this is probably interpreted differently than I intended for our internal work: I was using this for a safety check to see if a rig is actually sleeping but it didn't really make sense to actually check the boards if the hashrate is 0 and the miner reports sleeping.

I haven't looked into when asic-rs checks for active hbs. asic-rs already exposes the apis that I need :)
