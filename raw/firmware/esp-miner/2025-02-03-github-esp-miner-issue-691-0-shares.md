# bitaxeorg/ESP-Miner issue #691: 0 shares

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/691
> Collected: 2026-10-07
> Published: 2025-02-03

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 691
- State: closed
- Author: ovik88
- Opened: 2025-02-03
- Closed: 2025-02-15
- Labels: none

## Description

Is this ok? HAving 0 shares yet, geting found nounce?

![Image](https://github.com/user-attachments/assets/356523f6-950b-45d8-b16a-c4a112167afc)

## Comments

### MyOwn2C on 2025-02-03

If it stays like this for more than 10 mins, then it’s not working. 
If you have nonce but no shares, you likely used a pool with high diff. 

### ovik88 on 2025-02-03

i didnt change pool and it was working just fine before.. but i was playing with voltage and freq. so mby i messed up something. I hade to restart it few times and now im hassing again, but mby it was issue on public-pool.io im mining , dunno

### MyOwn2C on 2025-02-03

Pubic pool was down over the weekend

### ovik88 on 2025-02-04

> Pubic pool was down over the weekend

thats strange, i didnt notice any outage during the weekend. Anyway so is there any other explanation why i was finding nounces but no shares? 

### skot on 2025-02-04

Hmmm. This is a strange one. You said you were changing settings -- it would seem like the share counter got reset without resetting the best diff somehow.

### ovik88 on 2025-02-04

> Hmmm. This is a strange one. You said you were changing settings -- it would seem like the share counter got reset without resetting the best diff somehow.

nop, i think it was just opposite. Share counter got stucked at 0 while "best difficulties -  since system boot" were updating everytime i found new high

### skot on 2025-02-04

> > Hmmm. This is a strange one. You said you were changing settings -- it would seem like the share counter got reset without resetting the best diff somehow.
> 
> nop, i think it was just opposite. Share counter got stucked at 0 while "best difficulties - since system boot" were updating everytime i found new high

Ok, then it's prolly what @MyOwn2C said. Can you restart your Bitaxe and try this again now that public-pool is back up?

### ovik88 on 2025-02-05

yes, im back online. but for me it seems log are very general and usualy when something wrong  happens i dont see anything in there. Mby add some more logging for error states?
