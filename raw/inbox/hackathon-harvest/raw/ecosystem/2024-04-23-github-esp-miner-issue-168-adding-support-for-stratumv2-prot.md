# bitaxeorg/ESP-Miner issue #168: Adding Support for StratumV2 Protocol

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/168
> Collected: 2026-10-07
> Published: 2024-04-23

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 168
- State: closed
- Author: c03rad0r
- Opened: 2024-04-23
- Closed: 2026-05-29
- Labels: none

## Description

**Enhancement Request:**
I would like to propose adding support for the StratumV2 protocol to the ESP-Miner project. StratumV2 offers significant improvements over the current StratumV1, including enhanced security, reduced bandwidth requirements, and the ability for miners to construct their own block templates.

**Key Benefits:**
- **Security:** StratumV2 provides better protection against security threats, implementing end-to-end encryption to prevent hashrate hijacking and other man-in-the-middle attacks [Stratum V2 Overview](https://braiins.com/stratum-v2).
- **Efficiency:** The protocol reduces unnecessary data transmission, optimizing operations by using a more efficient binary encoding, which significantly lowers the data payload size compared to the JSON-RPC used in Stratum V1 [Stratum V2 Documentation](https://stratumprotocol.org/).
- **Decentralization:** Allows greater control over block construction, supporting decentralized mining practices by enabling miners to select their own transaction sets, thus improving the decentralization of mining [Bitcoin Manual on Stratum V2](https://thebitcoinmanual.com/articles/what-is-stratum-v2).

**Consideration:**
While it is possible to use a translation proxy to avoid making significant changes to the ESP-Miner, this approach would not allow hashers to benefit from the direct security and efficiency improvements offered by StratumV2. Thus, implementing StratumV2 natively in ESP-Miner could provide more substantial benefits to mining operations.

Thank you for considering this addition.


## Comments

### c03rad0r on 2024-04-23

Sjors already created bitcoin core [binaries ](https://github.com/Sjors/bitcoin/releases/tag/sv2-tp-0.1.2) for his StratumV2 [pull request](https://github.com/bitcoin/bitcoin/pull/29432). There is a testing guide [here](https://github.com/Sjors/bitcoin/blob/2023/11/sv2-poll/doc/stratum-v2.md#testing-guide).



### benjamin-wilson on 2024-04-23

I would suggest it does not improve decentralization as the pool can always reject a template proposal and or not propagate a valid solution. 

I agree on the security and efficiency, however both of those benefits can be gained by using the translation proxy outside of the LAN. 

IMO esp-miner could benefit but this is a low priority item. 

### c03rad0r on 2024-04-23

Perhaps I can try to implement it once I have built a Bitaxe that I can test with. Would you be open to PRs in this direction? 

### benjamin-wilson on 2024-04-23

Absolutely 

### TheBlueMatt on 2024-04-26

> I would suggest it does not improve decentralization as the pool can always reject a template proposal and or not propagate a valid solution.

This is a common misconception and inaccurate - the Stratumv2 reference implementation (SRI) and the intended use mandate that if the pool declares they wish to reject your template that you immediately fall back to an alternative pool or solo mine. There is no world where an Sv2 mining device which is doing custom template selection will *ever* stop mining on the template it wants to, the pool saying no just may change how the payouts for that job work.

### skot on 2024-04-26

The Bitaxe controller (ESP32) is a pretty resource constrained device.. do you think it would be better to have a SV2 proxy running on your node that you point your SV1 Bitaxe to?

### TheBlueMatt on 2024-04-28

For those doing custom work selection there's no much difference, indeed. However, for those doing legacy pooling Sv2 would at least substantially improve their security. ISTM its worth at least seeing if a minimal Sv2 implementation can fit on the ESP32, but if not its not a huge deal.

### Sjors on 2024-05-01

In sv2 block template creation is handled by the node, which presumably is running on a different machine. I think there's three approaches here:

1. On the device with the full node, run the SRI Job Declarator Client and the Translator roles. The miner on the device simply points to the translator and can keep speaking sv1. Main downside: the translator adds complexity, more stuff to configure, makes debugging more difficult, etc. But it's the easiest place to start.

2. Make the ESP32 firmware speak native Sv2, i.e. add noise encryption and small number of messages. Then on the node machine you only need to run the SRI Job Declarator Client.

3. Add the Job Declarator Client to the ESP32 firmware. It will fetch job templates from the full node, and communicate with the pool. This requires much more data processing on the ESP32 device, but not block validation so maybe it's doable. The major benefit is that it's plug and play. User just needs to provide a pool address (and job declarator server address if it's different).

Though perhaps in some future upgrade Bitcoin Core could also handle the work done by the Job Declarator Client. The current PR doesn't.

### benjamin-wilson on 2024-05-01

> > I would suggest it does not improve decentralization as the pool can always reject a template proposal and or not propagate a valid solution.
> 
> This is a common misconception and inaccurate - the Stratumv2 reference implementation (SRI) and the intended use mandate that if the pool declares they wish to reject your template that you immediately fall back to an alternative pool or solo mine. There is no world where an Sv2 mining device which is doing custom template selection will _ever_ stop mining on the template it wants to, the pool saying no just may change how the payouts for that job work.

I never suggested the device would stop mining but the pool can effectively censor the transactions you proposed, you must go somewhere else, similar to v1. Or worse they accept the template but withhold a valid block. 

>
> Add the Job Declarator Client to the ESP32 firmware. It will fetch job templates from the full node, and communicate with the pool. This requires much more data processing on the ESP32 device, but not block validation so maybe it's doable. The major benefit is that it's plug and play. User just needs to provide a pool address (and job declarator server address if it's different).

3. is almost certainly too much for the esp to handle on top of the mining work.



### TheBlueMatt on 2024-05-01

> I never suggested the device would stop mining but the pool can effectively censor the transactions you proposed, you must go somewhere else, similar to v1. Or worse they accept the template but withhold a valid block.

The key value here is that it changes an active action to a passive one. We've seen time and time and time and time again that miners don't really care and will simply do whatever their software does for them. In the current world, if a pool starts censoring, miners learn nothing about it, they keep on happily mining the censored transaction, and we rely on one person (0xB10C is, as far as I'm aware, the *only* one monitoring to detect such things) to notice this is happening and then get the word out via Twitter to miners and then hope that they tear up their existing business contracts and move to a new pool. During all this time Bitcoin is being actively censored.

Instead, with Sv2, miners selecting their own work will continue to mine the work that contains any transaction the pool wants to censor, and then one of two things will happen. Either (a) the pool will send a rejection message to the Sv2 miner who's software will then automatically fall back to a fallback pool or solo mine or (b) the pool will do nothing and simply not pay out, at which point the miner can go to their existing contract and either sue the pool for breach and lost revenue or move to another pool and throw away a few days of revenue.

Sure, a miner could, when they notice the issue, go back to their previous pool and start mining censored blocks, but that takes an *active* decision on the part of the miner some substantial (human-response) time after some censored transaction(s) were mined. This is an absolutely massive change compared to today.

### benjamin-wilson on 2024-05-01

> > I never suggested the device would stop mining but the pool can effectively censor the transactions you proposed, you must go somewhere else, similar to v1. Or worse they accept the template but withhold a valid block.
> 
> The key value here is that it changes an active action to a passive one. We've seen time and time and time and time again that miners don't really care and will simply do whatever their software does for them. In the current world, if a pool starts censoring, miners learn nothing about it, they keep on happily mining the censored transaction, and we rely on one person (0xB10C is, as far as I'm aware, the _only_ one monitoring to detect such things) to notice this is happening and then get the word out via Twitter to miners and then hope that they tear up their existing business contracts and move to a new pool. During all this time Bitcoin is being actively censored.
> 
> Instead, with Sv2, miners selecting their own work will continue to mine the work that contains any transaction the pool wants to censor, and then one of two things will happen. Either (a) the pool will send a rejection message to the Sv2 miner who's software will then automatically fall back to a fallback pool or solo mine or (b) the pool will do nothing and simply not pay out, at which point the miner can go to their existing contract and either sue the pool for breach and lost revenue or move to another pool and throw away a few days of revenue.
> 
> Sure, a miner could, when they notice the issue, go back to their previous pool and start mining censored blocks, but that takes an _active_ decision on the part of the miner some substantial (human-response) time after some censored transaction(s) were mined. This is an absolutely massive change compared to today.

Do you have any insight on the possible block withholding? 

### TheBlueMatt on 2024-05-01

What possible block witholding, not sure what you're referring to. A miner doing custom JD will broadcast any blocks they find directly (in addition to the pool doing so).

### benjamin-wilson on 2024-05-01

> A miner doing custom JD will broadcast any blocks they find directly

Ok, that's what I was looking for. I was unsure if this was expected default behavior. 

### plebhash on 2024-05-02

I don't think it makes sense to integrate Job Declaration Protocol (negotiating templates) into the ESPminer.

This part of the protocol is not relevant at a firmware level.

If the miner wants to participate in Job Declaration, they should deploy a Job Declaration Client and one or more Proxies on their LAN infrastructure.

The ESPminer simply sends shares to the Proxy, which forwards them to JDC.

With SV2, the ESPminer will be consuming less bandwidth and computation, so it's still an improvement.

### Sjors on 2024-05-02

> If the miner wants to participate in Job Declaration, they should deploy a Job Declaration Client and one or more Proxies on their LAN infrastructure.

This seems too complicated, unless you have some node-in-the-box solution that installs and configures all that.

> is almost certainly too much for the esp to handle on top of the mining work.

Right, so this needs to be something that's easy to install next to the node.

### plebhash on 2024-05-21

After some reflection, I'm redacting my previous comment where I said that it doesn't make sense to add JD functionality to ESPminer.

Assuming the ESP32 has enough computation power, it would be an interesting feature (as @Sjors already described above).

### plebhash on 2024-05-21

@benjamin-wilson already stated that this is a low-prio task, so it will probably take a while before it starts being implemented. Although it seems maybe @chGoodchild might eventually give it a shot?

Anyways, if you guys eventually start planning to dive into this, please let the SRI contributors know on the github issue linked above, because FFI coverage will have to be expanded. Unless you want to do the full-Rust avenue, or you use some pure-C implementation (which I'm unaware of, so please let me know if you find some).

### benjamin-wilson on 2024-05-21

A rust implantation of esp-miner is in the very early stages of development. I'm not sure how much it will be worked on.

https://github.com/bitaxeorg/esp-miner-rs

### c03rad0r on 2024-05-22

> @benjamin-wilson already stated that this is a low-prio task, so it will probably take a while before it starts being implemented. Although it seems maybe @chGoodchild might eventually give it a shot?
> 
> Anyways, if you guys eventually start planning to dive into this, please let the SRI contributors know on the github issue linked above, because FFI coverage will have to be expanded. Unless you want to do the full-Rust avenue, or you use some pure-C implementation (which I'm unaware of, so please let me know if you find some).

I haven't started yet. This is something I really want to work on, but realistically I won't be able to start before July. 

I'll be sure to ping you and other SRI contributors before starting to make sure I have a viable/suitable approach. 

Thanks! 

### forrestbice on 2024-07-19

@chGoodchild any chance you have picked this back up?

### c03rad0r on 2024-07-19

Not yet unfortunately... 

Others are welcome to pick this up if they have the bandwidth.

I've been working on Bitcoin and nostr support for OpenWRT Routers lately: https://njump.me/nevent1qqsqfh934xqc6ymx4uj5f2uwpl80qhkav38vjgngzgxkz5lmvgaa6mspz9mhxue69uhkummnw3ezuamfdejj7q3qvfl7v8fgwxnv88u6n5t3pwsmzqg7xajclmtlfqncpaf2crefqr9qxpqqqqqqzmu300a



### Sjors on 2024-08-20

> A rust implantation of esp-miner is in the very early stages of development. I'm not sure how much it will be worked on.
> 
> https://github.com/bitaxeorg/esp-miner-rs

Unfortunately no commits there in the past 4 months.

Stratum v2 currently has implementations in Rust (SRI) and c++ (Bitcoin Core). Redoing it in c sounds like hell. The c++ code in Bitcoin Core is not easy to export as a library, though it might be possible? But then you still have to implement a lot of stuff in c.

Rust is probably the better route?

It seems overkill to rewrite _all_ of ESP-miner in Rust though. 

### Georges760 on 2024-08-21

I am actively working on it, you didn't look at the correct branch ;) Sv2 though will come later.

Happy to see you here @Sjors, I am of course using your BTC Node for SV2 testing!

### Sjors on 2024-08-21

Excellent! I expect to receive my own Axe very soon(tm) so can test stuff.

### Georges760 on 2024-08-21

> Excellent! I expect to receive my own Axe very soon(tm) so can test stuff.

I am nowhere near to have a Sv2 client in no_std no-alloc yet, but it will come hopefully by end of the year. First I focus on esp-miner-rs implementation using my Sv1 no_std no-alloc client and my bm13xx-rs driver crate for the Asics. Then I will work on the Sv2 client.

### Sjors on 2024-08-26

I heard recently that it's actually possible to compile c++ for ESP-IDF. In that case it might be easier to use `sv2_noise.{h,cpp}` from https://github.com/bitcoin/bitcoin/pull/29346. That takes care of the noise encryption. There's a few includes you would also need to copy.

That's not all there is to the protocol though. In order to establish a connection and generate / parse stratum v2 messages, you would need https://github.com/bitcoin/bitcoin/pull/30315, https://github.com/Sjors/bitcoin/pull/50 and a few bits of https://github.com/Sjors/bitcoin/pull/49. However that code builds on top of a fairly large chunk of other Bitcoin Core code. It may be possible to split that out into a library, but that will take a while.

### Sjors on 2024-09-13

I have a experimental (and not working) pull request to put Sv2Noise and Sv2Transport in a new library called `libbitcoinsv2`: https://github.com/Sjors/bitcoin/pull/62

To build just the library:

```
cmake -B build -DWITH_SV2=ON -DBUILD_SV2_LIB=ON -DBUILD_DAEMON=OFF -DBUILD_CLI=OFF -DBUILD_TX=OFF -DBUILD_UTIL=OFF -DENABLE_EXTERNAL_SIGNER=OFF -DBUILD_TESTS=OFF
cmake --build build
```

This currently compiles nothing :-(

I'm not a build system or cmake guru, so please let me know what changes you need in order to be able to include this.

Since Bitcoin Core is a large mono repo, it's probably easiest to just include (my fork of) it as a git submodule.

cc @dsbaars

### warioishere on 2026-02-12

Hey everyone,

I’ve been following this issue with interest and wanted to ask from a practical perspective.

Since ESP-Miner is already built around a C/C++ codebase (ESP-IDF environment), would the Bitaxe firmware team be open to integrating a minimal, native Stratum V2 mining client directly into ESP-Miner, implemented in pure C/C++ and without external runtime dependencies?

The intention would not be to implement the full SV2 stack (no embedded Job Declarator, no async runtime, no large external frameworks), but rather a lightweight mining client capable of:

Performing the Noise_NX handshake

Opening a standard mining channel

Handling NewMiningJob / SetNewPrevHash

Submitting shares

The Job Declarator (JD) component could remain external and optional. The goal would simply be to allow Bitaxe devices to connect to an SV2 pool (or an external JD proxy) using a clean, minimal implementation that respects embedded constraints (flash/RAM limits, deterministic behavior, no heavy abstractions).

This would mainly serve as a first step into the SV2 ecosystem from a firmware perspective. More advanced features (extended channels, deeper JD integration, etc.) could always be explored later if there’s interest.

Before investing time into prototyping something like this, I’d like to understand whether there is general interest from the core developers in moving ESP-Miner in this direction — or whether this would be better maintained as a separate experimental fork.

Looking forward to your thoughts.

### 1ma on 2026-02-14

I concur with @warioishere, the BitAxe only needs to speak the Sv2 Mining Protocol to encrypt and authenticate the session with the server (thus decreasing bandwidth and latency, and making MITM attacks impossible).

Job Declaration and Template Distribution roles are better solved at the server level, where Sv2 isn't even needed. For instance the DATUM gateway combined with any node that supports the getblocktemplate RPC call + blocknotify already fulfills both roles in a much simpler way (but is still missing an Sv2 Mining endpoint, though).

### adammwest on 2026-05-18

https://github.com/bitaxeorg/ESP-Miner/pull/1553 was merged


### 1ma on 2026-05-19

@warioishere Would it be technically possible to extract an Sv2 C library from the code in your PR? I'd like to see Sv2 Mining Protocol support in the DATUM gateway.

I'm not asking you to do it, just curious if that would make sense or the code in your PR is only relevant for the client side.

### WantClue on 2026-05-29

has been recently implemented #1553
