# bitaxeorg/ESP-Miner issue #1411: Show banner if default payout address is used

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1411
> Collected: 2026-10-07
> Published: 2025-12-01

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1411
- State: closed
- Author: mutatrum
- Opened: 2025-12-01
- Closed: 2025-12-21
- Labels: none

## Description

Show a warning banner when the default stratum user is being used for hashing. Could be a mix between a thank you and a warning, as it's possible people do this on purpose, but we don't want people to continue hashing to an address that's not theirs.

## Comments

### duckaxe on 2025-12-01

I have often thought about how we can solve this. Not all manufacturers use the same address. Alternatively, we set a flag as soon as the user changes the address. We display the banner as long as they haven't done so.

### mutatrum on 2025-12-01

If a manufacturer changes the donation address, they can change the banner. 

### duckaxe on 2025-12-01

In my experience, many manufacturers manually enter new values for all the pool settings before delivery. They do not change the code. Ideally, we would also advise users to check their pool data in such cases. We should not check for a static address. We need a better solution that can help more users.


### Travetown on 2025-12-01

Perhaps it could work like this: ....
Couldn't you generate a one-time query and ask whether the specified address xxx is your own?
Once you have confirmed “yes,” this would have to be saved permanently and never asked again. 
However, everyone who has never done this before would then be asked to do so once. But perhaps it would also draw the attention of a few who have “overlooked” it so far. On the other hand, those who use a “wrong” address will probably never do a software update. 
It seems to be quite difficult. Maybe I shouldn't have written anything.   🤐

### mutatrum on 2025-12-01

I think it's a small effort. The firmware is from OSMU, so if we show a banner if someone is mining to the donation address (which has been the same since forever), it's a minimal effort to a potential oversight. If someone else overrides the default address, then can't help that. And as I said on Discord, the least we can say is thanks, so maybe just that should be the message:

_“Thank you for donating your hashrate to OSMU!”_

### etkaar on 2025-12-05

To find out if the Bitaxe very likely has not the users but the manufacturers address you can check if a connection to the Bitaxe has taken place and the WiFi credentials been changed, because this is typically a user would do (only) once after he receives the device.

### WantClue on 2025-12-12

> I think it's a small effort. The firmware is from OSMU, so if we show a banner if someone is mining to the donation address (which has been the same since forever), it's a minimal effort to a potential oversight. If someone else overrides the default address, then can't help that. And as I said on Discord, the least we can say is thanks, so maybe just that should be the message:
> 
> _“Thank you for donating your hashrate to OSMU!”_

I modified it a bit. But a thank you message would be nice as well :D 

### mutatrum on 2025-12-12

We could also add a marker on #1391
