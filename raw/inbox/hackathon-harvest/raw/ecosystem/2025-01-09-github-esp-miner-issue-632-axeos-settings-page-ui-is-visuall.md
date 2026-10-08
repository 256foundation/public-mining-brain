# bitaxeorg/ESP-Miner issue #632: AxeOS settings page UI is visually overwhelming

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/632
> Collected: 2026-10-07
> Published: 2025-01-09

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 632
- State: closed
- Author: skot
- Opened: 2025-01-09
- Closed: 2025-01-27
- Labels: enhancement, help wanted, good first issue

## Description

<img width="1491" alt="image" src="https://github.com/user-attachments/assets/ed435ddd-2bf9-492c-908b-1d2ec96390e2" />

This is what new users are confronted with when setting up a Bitaxe for the first time. I'd like to find a way to change the UI such that this is more approachable.

## Comments

### mrv777 on 2025-01-09

Not sure if it's better, but one idea
<img width="1286" alt="image" src="https://github.com/user-attachments/assets/3ca60ab7-dc83-4099-a0f6-6ccc88c10a1f" />


### skot on 2025-01-09

that looks so much better! Just gotta make sure it looks decent on phone

### dustinb on 2025-01-09

"Pools" on it's own page?  Then "Settings" would be hardware settings and firmware.  I was looking at this issue https://github.com/skot/ESP-Miner/issues/180, not sure if it will be accepted but would put even more pool stuff on the page.

### matlen67 on 2025-01-09

It would also be great if you could add at least one alternative pool in addition to the fallback pool and then choose between Pool1 and Pool2 using the checkbox. It's quite annoying when you have to re-enter all the pool data several times a day for research purposes. 

### skot on 2025-01-09

> It would also be great if you could add at least one alternative pool in addition to the fallback pool and then choose between Pool1 and Pool2 using the checkbox. It's quite annoying when you have to re-enter all the pool data several times a day for research purposes. 

Btw, you can script this with Python or something..

### Barnminer on 2025-01-09

I like the example. From a new user setup perspective, I think it is good to have the pool and settings on the same page. 

But, then think it may be better the settings are on a different tab since a lot of fist user issues can occur through changing defaults. It may be a plus not having the option to change freq/voltage on the same tab. 

### mrv777 on 2025-01-09

Hmm, tabs might be interesting.  People starting out shouldn't be messing with the hardware settings right away, so default to just show the pool settings may be good

### warioishere on 2025-01-13

from my experience as a reseller, I get some feedback too. Pool Settings and Hardware Settings should be split. Also the new UI @mrv777 with Main Pool and Fallback pool separated is a good idea to make things more clear.

### jason-me on 2025-04-08

Could you guys benefit from a design review? We are doing a [Designathon](https://event.bitcoin.design/) for [bitcoin.design](https://bitcoin.design) and increasing the usability and accessibility of FOSS mining UIs is one of the ideas we are considering for teams to focus on.
