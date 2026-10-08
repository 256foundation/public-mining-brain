# 256foundation/asic-rs pull request #192: fix(antminer): allow `BHB42XXX` to be found as an unknown stock antminer model

> Source: https://github.com/256foundation/asic-rs/pull/192
> Collected: 2026-10-07
> Published: 2026-03-19

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 192
- State: closed
- Author: b-rowan
- Opened: 2026-03-19
- Closed: 2026-03-20
- Labels: none

## Description

Fixes: #191 

## Comments

### glitchpixelz on 2026-03-20

LGTM

### s0kil on 2026-03-20

Does it make sense to introduce the 6060 API here?

### b-rowan on 2026-03-20

> Does it make sense to introduce the 6060 API here?

It doesn't change anything, since the issue was with a control board with no boards connected 😆 

### s0kil on 2026-03-20

:6060/productName is available on all bitmain firmware's, going back to 2020.

### s0kil on 2026-03-20

> > Does it make sense to introduce the 6060 API here?
> 
> It doesn't change anything, since the issue was with a control board with no boards connected 😆

I'm thinking if we read the /productName we can get an actual model, instead of falling back to UnknownMinerModel

### b-rowan on 2026-03-20

> > > Does it make sense to introduce the 6060 API here?
> 
> > 
> 
> > It doesn't change anything, since the issue was with a control board with no boards connected 😆
> 
> 
> 
> I'm thinking if we read the /productName we can get an actual model, instead of falling back to UnknownMinerModel

Might be possible, but doesn't the CB read the miner type from the board EEPROMs?  Therefore if no boards we still need unknown...

### s0kil on 2026-03-20

> > > > Does it make sense to introduce the 6060 API here?
> > 
> > 
> > > 
> > 
> > 
> > > It doesn't change anything, since the issue was with a control board with no boards connected 😆
> > 
> > 
> > I'm thinking if we read the /productName we can get an actual model, instead of falling back to UnknownMinerModel
> 
> Might be possible, but doesn't the CB read the miner type from the board EEPROMs? Therefore if no boards we still need unknown...

the /productName endpoint reads from the firmware config files, so it knows ahead of time what model it is. at the end of the day, the FW is build for each model, and model specific config.

### b-rowan on 2026-03-20

> the /productName endpoint reads from the firmware config files, so it knows ahead of time what model it is. at the end of the day, the FW is build for each model, and model specific config.

Interesting...  I wouldn't be opposed to it, I would be curious as to what that returns on the CB that the issue OP has.

### glitchpixelz on 2026-03-20

<img width="1893" height="1028" alt="Weird model" src="https://github.com/user-attachments/assets/12f07c52-780e-46a0-a268-e8ec876a5d6b" />
Here is one with hashboards connected to it.

### glitchpixelz on 2026-03-20

<img width="485" height="119" alt="3 boards" src="https://github.com/user-attachments/assets/613eea65-f479-4176-8746-9bed7b05705b" />
Ive seen this on T21s as well.
I'll see if flashing eeprom fixes it.

### b-rowan on 2026-03-20

Can you test that 6060 API in that before flashing EEPROM?
