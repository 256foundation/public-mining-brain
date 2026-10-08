# 256foundation/asic-rs issue #162: default Display impl for ePIC looks strange

> Source: https://github.com/256foundation/asic-rs/issues/162
> Collected: 2026-10-07
> Published: 2026-03-09

- Repository: 256foundation/asic-rs
- Type: issue
- Number: 162
- State: closed
- Author: DanNicolau
- Opened: 2026-03-09
- Closed: 2026-03-12
- Labels: none

## Description

the default impl shows EPic and ePIC matches the brand's styling for downstream users of asic-rs

## Comments

### DanNicolau on 2026-03-09

I can get the PR for this as well if asic-rs is open to this change

### b-rowan on 2026-03-09

Yep, definitely open to this.  I think that is a derived impl, so its just grabbing the real name of the struct, which is named that way to keep linters from complaining about it, and it make the naming scheme more consistent.  Should be simple enough to change it.

### b-rowan on 2026-03-09

@jpcomps might also have some comments here?

### b-rowan on 2026-03-09

I think I fixed this one - 
https://github.com/256foundation/asic-rs/blob/19e2ea96d7a464112983dfeda41fe84529570371/src/data/device/models/epic.rs#L7-L9

Here in #158 -
https://github.com/b-rowan/asic-rs/blob/c38a9443969b4152450d84f78bd73de677160273/asic-rs-makes/epic/src/make.rs#L10-L14

Are there any other places you're seeing this?

### jpcomps on 2026-03-09

@DanNicolau is right, it should be ePIC, had just left it in the original implementation to match what was there. Think this is the right fix 

### DanNicolau on 2026-03-09

I'm seeing it in https://github.com/256foundation/asic-rs/blob/master/src/data/device/mod.rs#L12C1-L29C2
since only the serde has the override, not the display.

### b-rowan on 2026-03-09

Ah, its coming from the strum derive.  Should be some tag for that...

### b-rowan on 2026-03-09

Also fixed in #158 -
https://github.com/256foundation/asic-rs/blob/c38a9443969b4152450d84f78bd73de677160273/asic-rs-firmwares/epic/src/firmware.rs#L67-L71

> I'm seeing it in https://github.com/256foundation/asic-rs/blob/master/src/data/device/mod.rs#L12C1-L29C2 since only the serde has the override, not the display.



### jpcomps on 2026-03-09

Confirmed will work on that PR:
- 10.X.X.XXX S21 (ePIC)
