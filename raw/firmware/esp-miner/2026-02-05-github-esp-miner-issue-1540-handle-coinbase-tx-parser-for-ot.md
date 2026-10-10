# bitaxeorg/ESP-Miner issue #1540: Handle coinbase tx parser for other chains

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1540
> Collected: 2026-10-07
> Published: 2026-02-05

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1540
- State: closed
- Author: mutatrum
- Opened: 2026-02-05
- Closed: 2026-02-12
- Labels: none

## Description

#1391 raised some concerns of confusion when people are mining other pools. I wrote this on Discord, but for continuity, I copied it here:

This (1391) was added so people can verify what the payout address is. There have been a [few instances of scam pools ](https://github.com/mweinberg/stratum-speed-test/tree/main/findings) that say they mine bitcoin, but replace the work and payout for something completely different. I'm not talking about other chain pools, or shared pools, these were advertised as bitcoin pools with the intention of stealing the miners work. This gives the user details on what the actual work for the pool is, so they verify this work. It automates what other people have created to verify the ⁨`mining.notify⁩` stratum messages. IMO this is a valuable addition.

Having said that, this is a bitcoin only solution. Part of this is indeed philosophical: OSMU is focused on bitcoin mining, and while these miners work on other chains, there is no specific support for them in the firmware. However, besides this philosophical point is also a technical point: there is no information in the stratum protocol on what the job actually is. The addresses in the coinbase transaction are stored as hashes, not in base58 or bech32. The prefixes of the address are derived from the output script. These are the same for all forks, but each fork has their own address prefixes. Instead of `⁨1`⁩, `⁨3`⁩, `⁨bc1q`⁩ and `⁨bc1p`⁩ they use different prefixes. We don't know - and will never know - what these are if the user is mining something different.

A small bit of information is the address format of the payout address in the pool user field. However, there are pools that pay out in bitcoin, but mine something else. So assuming the chain is or is not bitcoin cannot be derived solely from the user address. Other detection methods (block height, network diff) are approximate as well, and are suboptimal.

This leaves little options left to do:
1) Do nothing and have confused users;
2) Have a checkbox at the pool configuration to disable this;
3) Be able to disable the warning; (This might be tricky with fallback pools).
4) Anything else?...

## Comments

### skot on 2026-02-06

I do not think other coins should be added. There are too many fly-by-night shitcoins to have any hope of good support.

### sz4bi on 2026-02-06

Option 2 sounds good. Don't waste too much energy on any other coins.

### bonifacio123 on 2026-02-07

I believe this is a great feature - thank you for taking the time the add this. Option #2 is best in my opinion. However, I think the feature should be turned off by default with a tool-top stating this is only for BTC.

### skot on 2026-02-08

Perhaps instead of an exact value of the coinbase split we can show a percentage? This would eliminate the need to show the "BTC" units and confusing shitcoiners.

### bonifacio123 on 2026-02-09

> Perhaps instead of an exact value of the coinbase split we can show a percentage? This would eliminate the need to show the "BTC" units and confusing shitcoiners.

This is a really good idea :)

### mutatrum on 2026-02-09

> Perhaps instead of an exact value of the coinbase split we can show a percentage? This would eliminate the need to show the "BTC" units and confusing shitcoiners.

For bitcoin mining, we already show this:
<img width="589" height="221" alt="Image" src="https://github.com/user-attachments/assets/2d80610a-0958-45e9-81fc-6d42fb82ba14" />

With #1544 the BTC unit is only show when the option is enabled. For other chains it only shows the total value of outputs. We can't do percentage there as we can't compare the user address with the output tx script.
