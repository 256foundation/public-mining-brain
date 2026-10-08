# bitaxeorg/ESP-Miner issue #939: Custom nonce and extra nonce range

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/939
> Collected: 2026-10-07
> Published: 2025-05-20

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 939
- State: open
- Author: precious8821
- Opened: 2025-05-20
- Closed: n/a
- Labels: none

## Description

Is it possible to modify the firmware or software so that a custom nonce range and extra nonce value can be used? So that way it could run a nonce range starting from say 2 billion to 4 billion, increasing by 1 per hash, and once 4 billion is reach then starting again at 2 billion, cycling through. All WHILE having a custom EXTRA NONCE range starting at say 17,446,744,000,000,000,000, or whatever custom value is entered not exceeding 2^64. And then every time all the nonces in the nonce range are all hashed and restart at the preset custom value of 2 billion, then the custom extra nonce value will increase by one and try all the nonces in the defined nonce range again. Repeating this process again and again.

If this modification is possible, could it also be possible to enter these custom range values within the web portal for the miner, rather than having to hard code the custom values in the firmware itself.   So that way the values won't have to be entered in the software code itself every time, and instead the custom nonce range and extra nonce range values can be entered into the admin screen through the web portal of the miner.

## Comments

### mutatrum on 2025-05-21

Sounds like some overlap with #824.

What's the rationale of wanting to choose the values?

### g1ass1 on 2025-05-21

I have the same ask. - but more so on the nonce... - I had implemented MQTT pub and sub logic to achieve changing the extra nonce range. but I am struggling in the firmware to find where the nonce range is controlled.

I'm not so much changing the sequential logic, (although control here would be nice) my ask is more basic on nonce - a start and end nonce to limit the logic to certain ranges.

I have been able to implement a range of various strategies for extra nonce control but struggling to find where to control the nonce is controlled.

if you could point this out in the code base, I'm happy to make my own local amendments / testing and go from there.


### precious8821 on 2025-05-22

G1ass1, could you share the coding you used to adjust the extra nonce range? Does your modification allow for a custom extra nonce starting value to be used, of course not exceeding 2^64?   Also, please share the file names where you added or modified the coding for the extra nonce.  Thank you.   Hopefully someone might have an answer to adjust the nonce range as well. 

### g1ass1 on 2025-05-22

```
uint32_t min = 0x33333333; // Top 80% of 32-bit range
        uint32_t max = 0xFFFFFFFF;
        while (GLOBAL_STATE->stratum_queue.count < 1 && GLOBAL_STATE->abandon_work == 0)
        {
            if (should_generate_more_work(GLOBAL_STATE))
            {
                // Generate extranonce_2 using double SHA-256 (Bitcoin style) of job_id, merkle_root, timestamp, and rand()
                char key_material[160];
                snprintf(key_material, sizeof(key_material), "%s_%s_%llu_%lu",
                    mining_notification->job_id,
                    merkle_root, // Use the previously calculated merkle_root for this job
                    (unsigned long long)esp_timer_get_time(),
                    (unsigned long)rand());
                uint8_t hash1[32], hash2[32];
                mbedtls_sha256((const unsigned char*)key_material, strlen(key_material), hash1, 0);
                mbedtls_sha256(hash1, 32, hash2, 0);
                // Use the last 4 bytes of the double SHA-256 for extranonce_2
                uint32_t extranonce_2 = (*(uint32_t*)&hash2[28]) % (max - min + 1) + min; // Ensure in top 80%
                generate_work(GLOBAL_STATE, mining_notification, extranonce_2);
            }
            else
            {
                vTaskDelay(100 / portTICK_PERIOD_MS);
            }
        }
```

these were the lines i amended in the create_jobs_tasks.c
I am working on a "bee-hive" approach to swarm an area.  this function selects the extranonce2 as a double to randomise selection of extranonce - the goal is to set a center, and a upper and lower window to limit search to increase focus on an area and randomly swarm it with activity, of nothing found back off, hit found center and focus more

this version just selects random exranonce hashes in the upper 80% of the range

### g1ass1 on 2025-05-22

> Sounds like some overlap with [#824](https://github.com/bitaxeorg/ESP-Miner/issues/824).
> 
> What's the rationale of wanting to choose the values?

bump on this?

I have tried defining starting and ending nonce, and with the BIP MinerHardwareBinaryProtocol - assumption being that if it isn't defined its default behavior. no luck, board stops hashing when ending nonce is defined.

at abit of a loss here so any direction would be appreciated.



### precious8821 on 2025-05-23

G1ass1:  on the extra nonce in your code you provided, it looks like you are only using 32 bits, with 4,294,967,295 as the max value for the extra nonce , i.e 2^32.   However, since the extra nonce can be up to 8 bytes, or 2^64.  Shouldn't your extra nonce max value should be closer to 18,446,744,073,709,551,616 ??   Only the nonce value is limited to 2^32, not the 'extra nonce'.   So the 80% top of extra nonce range should have a minimum value of 14,757,395,258,967,641,292 with a maximum value of 18,446,744,073,709,551,616.   Let me know your thoughts.

Also, please share your 'bee-hive' approach coding for the extra nonce when you complete it, as that does sound interesting to try out.

### Nexus9090 on 2025-05-23

It seems to me that it would be useful to implement a few options in terms of the extranonce range and search patterns.

1. Linear,  extranonce starts at zero incrementing by one each time (I'm not sure but I think this is how it works presently, which means a large amount of the extranonce space is never explored)
2. Inverse Linear,  start at 2^64 and decrement by one each time
3. Swapped linear, a combination of Linear and Inverse linear on each alternate extranonce (one at the bottom, next one at the top alternately)
4. Swapped linear within range, same as 3 but specifying the start and end values of extranonce
5. Random within range, so specify an extranonce range that you'd like to search with a random search pattern
6. Max random, random extranonce over the whole extranonce 2^64 range 
7. Random base with linear, start point is random in the 2^64 range but search is linear from that point



### g1ass1 on 2025-05-23

**precious8821** - you are correct - this was an easy and obvious place to start.  The beehive approach is the SHA randomization of the next extranonce2, based on a hash over a certain difficulty, with some hardware inputs as entropy.  not the first apart of it, which is stock behaviors atm. - and dynamically shrinking the search range around the location with the hit or widening if no hits are found.  I had it working, but the code got corrupted as I forgot to back it up so I'm re-working on it.  but again, was only extranonce2.

Will share when complete again - personal experience with stock vs beehive approach, suggests beehive is more effective, but this wasn't tested side by side empirically, and realistically it just ran overnight or for a day so pretty much no test data.  beehive likely to have more unique hashes vs entire community and less collisions so more effective use of hash power. so in that aspect its better, but realistically chances of hitting a block not likely to improve - just that I'm not waiting my limited Hash power providing results someone else likely already has - especially in the first 3 mins or less on a new block.

I added mqtt as a means to have a pub/sub - intention being to visualize the activity on a Grafana dashboard as a neat thing, and control the ranges dynamically via outside input as opposed to hard coded logic.

**Nexus9090** - yes - but all of these approaches require control of the nonce incrementation logic and range which im trying to figure out.  bmjobs seems to be the be it. But i need three points - start, stop and directional logic.

I have a feeling that detailed nonce selection/randomization is done because the esp32 just isn't fast enough to keep up with the asci chip at this level, so start, end and direction (up/down) may be all that's possible - which I feel is probably the case

but again, having trouble setting just the end nonce- i.e to limit the range

### Nexus9090 on 2025-05-23

You're probably correct, if I've understood correctly the entire nonce range (2^32) at 1TH/s will be consumed in around 4.3mS (four point three milliseconds) so the ESP would have to prepare the extranonce(2^64) and new job that often in order to keep it going without loosing hashrate. Not an impossible task for the ESP32 since thats only around 230 times a second. Though still non-trivial.

Unfortunately I've not dug that deep into the workings of how the jobs are created and issued to the ASIC, so I dont understand the specifics of it.

But I would imagine there's some mechanism for increasing extranonce on each job. So the logic for how the other options and ranges would be done at this point. 

However my lack of knowledge in this area just leads me to speculate on how its done. I'm hopeful one of the core developers will have a better idea.

If I'm right about the 4.3mS@1TH/S time for the nonce range, in the average 10 minute hashing period per block the extranonce would only be updated 600/0.0043 ~= 139,534 times. A tiny fraction of the available search range of 2^64.

It seems an awful waste of extranonce and a high reduction in odds of finding a hash of network target if it is only done incrementally. Random over the 2^64 extranonce range would surely improve the odds massively.

### precious8821 on 2025-05-26

G1ass1, thanks for the info.   Do you know if bitaxeorg can mine directly to bitcoin core's bitcoind, that way the extra nonce value won't be partially limited by the pool server?   My reason for wanting to modify the extra nonce is as follows.  To take the global network's hash rate in hashes/second times 60 times X gives around the total hashes tried to find a block in X minutes.   Then set the starting extra nonce value to that amount.

### precious8821 on 2025-05-26

G1ass1:  on my last comment how I explained how I plan to set the extra nonce by taking the take the global network's hash rate in hashes/second times 60 times X gives around the total hashes tried to find a block in X minutes. Then set the starting extra nonce value to that amount.   I forgot to say to also divide that number by the total nonces of 4,294,967,296., and then set that calculated value as the extra nonce.   So that will estimate theoretically the hashes performed in those 10 minutes, if you set X to 10.   To summarize, the plan is to take the (global network's hashes/s times 60 times X)/4,294,967,296, with X being the minutes it takes to mine a block, so set X to maybe 10 or 5 or whatever the average is for the last most recently blocks mined.  And then set that value as the starting extra nonce.  

I look forward to seeing your beehive attack script when its ready.   

 Also, let me know if you know if bitaxe can mine directly to bitcoin core's bitcoind.   That way there won't be the issue of the extranonce being partially preset by the mining pool, since the value will be sent straight to bitcoind.

### Nexus9090 on 2025-05-26

> G1ass1, thanks for the info. Do you know if bitaxeorg can mine directly to bitcoin core's bitcoind, that way the extra nonce value won't be partially limited by the pool server? My reason for wanting to modify the extra nonce is as follows. To take the global network's hash rate in hashes/second times 60 times X gives around the total hashes tried to find a block in X minutes. Then set the starting extra nonce value to that amount.

Presently ESP-Miner only mines to Stratum pools, I did ask if there was any development plans to allow direct to bitcoin core mining here :- #901 

@mutatrum seems to have a better grip on the technical details, so hopefully they'll come up with a workable solution for mining direct to bitcoin core.

### mutatrum on 2025-05-26

I don't think you have access to the nonce algorithm, that's inside the ASIC and it just runs through them linearly, and will loop around in around 1 or 2 seconds, maybe if we finally figure out all the flags, half a minute maybe (see #420). So it's been given new work, which either is an incremented extranonce2 value, or new work from the pool.

With this is mind, it will only do a few dozen extranonce2 values at most, before the pool gives you new work which will be a completely new search space. So resetting it at 0 (what happens currently) or continuing the extranonce2 range doesn't make a difference IMO. So to me it's still unclear what the goal would be for having custom ranges and orders here?

### Nexus9090 on 2025-05-26

> I don't think you have access to the nonce algorithm, that's inside the ASIC and it just runs through them linearly, and will loop around in around 1 or 2 seconds, maybe if we finally figure out all the flags, half a minute maybe (see [#420](https://github.com/bitaxeorg/ESP-Miner/pull/420)). So it's been given new work, which either is an incremented extranonce2 value, or new work from the pool.
> 
> With this is mind, it will only do a few dozen extranonce2 values at most, before the pool gives you new work which will be a completely new search space. So resetting it at 0 (what happens currently) or continuing the extranonce2 range doesn't make a difference IMO. So to me it's still unclear what the goal would be for having custom ranges and orders here?

Thanks for your help
Seems I've misunderstood something somewhere, nonce is 2^32 isnt it? extranonce is 2^64, at least I thought it was.

So, is the pool issuing nonce and part of extranonce i.e. the lower 32 bits of extranonce? 

And hence the implementation of extranonce2 which would repressent the upper 32 bits of extranonce, is that correct?

I'm a little confused, I only thought pools issued nonce and the whole extranonce was calculated locally before generating work. with the ASIC's only itterating linearly through the 2^32 of nonce before requiring new work.

So, that would mean the ASIC is also incrementing extranonce. I didn't know that was the case.

Obviously I need to dig deeper.

### mutatrum on 2025-05-26

I'm not 100% sure exactly which parts are provided by the pool, which part ESP-Miner handles, and which part is handled inside the ASIC. It's also slightly different between ASICs.

There is some related discussion on this here: https://discord.com/channels/1091348375301013615/1094385611718270977/1364651145095548959

### Nexus9090 on 2025-05-26

Thanks I'll take a look once I've managed to log back into discord, its not letting me on presently.

I'm going to dig deeper, I think something fundamental is missing here. That may just be my understanding of how it works but I'll figure it out.


### precious8821 on 2025-05-26

Nexus9090:  the extranonce value is partially assigned by the mining pool to each miner.  However, when submitting a block directly to Bitcoin core's bitcoind RPC, then the miner gets to submit the full extranonce value without a part being partially assigned by the pool.   So the entire concept of using a custom extra nonce value is best to be done when submitting blocks direc

### precious8821 on 2025-05-26

I accidentally clicked the close issue button again.   Just reopened it.

### precious8821 on 2025-05-26

Mutatrum:  the idea of using a custom extra nonce range is to try passing by the 'typically unsuccessful extra nonce values already mined in the network for a block and to try estimating at what point the extranonce values are at when a successful block is found.   For example, if you take the global network's hash rate in hashes per second, and multiple that times 60, and then multiple that number by the average time it takes to mine a block in the last day (typically it should be 10 minutes).  And then get that entire number and divide it by 4,294,967,296 which is the total nonces available.  So assuming a block took 10 minutes to complete, and assuming the global miners were cycling through all the nonces and then increase the extra nonce value by one before cycling through all the nonces again.  It means you can approximate what the extra nonce value will be in 10 minutes.    Therefore, instead you could set your miner to start mining with the extra nonce value which is typically reached by the 'network' in theory after 10 minutes of mining at the global hash rate. And your miner will start hashing from that value and up.  But for this calculated extra nonce value to be useful, the block would need to be submitted to bitcoin core's bitcoind RPC since you can submit the full extra nonce value to bitcoind without the value being partially preset by the mining pool.   The problem with the mining pools, even the solo mining pool is that they do in fact partially preset the extranonce value to each miner, which makes it impossible to fully use your own calculated extra nonce range to start at.

### Nexus9090 on 2025-05-26

> Nexus9090: the extranonce value is partially assigned by the mining pool to each miner. However, when submitting a block directly to Bitcoin core's bitcoind RPC, then the miner gets to submit the full extranonce value without a part being partially assigned by the pool. So the entire concept of using a custom extra nonce value is best to be done when submitting blocks direc

Thank you @precious8821 , some of the detail is starting to make some sense now.

This looks like another really rather good reason to implement Mine to local Bitcoin Core GBT #901  

@mutatrum “We choose to getblocktemplate, and do the other things, not because they are easy, but because they are hard.” 🚀

It might be hard, but more and more I'm thinking for solo mining that it is absolutely necessary.

### Nexus9090 on 2025-05-27

Just an FYI, after spending most of the day yesterday getting the IDF toolchain installed and learning how to get it working properly I finally managed to compile a working binary based on 2.7.1 late last night.

Having done that I then modified the extranonce2 calculation to make it random.

This was done by edits to create_jobs_task.c

Adding 
`#include "esp_random.h"`


and modifying the code section

```
 uint32_t extranonce_2 = 0;
        while (GLOBAL_STATE->stratum_queue.count < 1 && GLOBAL_STATE->abandon_work == 0)
        {
            if (should_generate_more_work(GLOBAL_STATE))
            {
                generate_work(GLOBAL_STATE, mining_notification, extranonce_2);

                // Increase extranonce_2 for the next job.
                // extranonce_2++;
               
               // make extranonce_2 a random
              extranonce_2 = esp_random();

            }
            else
            {
                // If no more work needed, wait a bit before checking again.
                vTaskDelay(100 / portTICK_PERIOD_MS);
            }
        }

```

So far it has made little or no obvious noticable difference to the returned share values, I will continue to monitor over the next week or so. It does however mean that the upper part of the extranonce is being explored at random, instead of linearly.

TBH, I'm not sure if it will yeild any better results and truth is, unless I start winning back to back blocks with it its unlikely to ever prove its self.

Never the less, nothing ventured and all that

### g1ass1 on 2025-05-27

Extranonce2 isn’t the problem — I’ve implemented a stable random generation method using a combination of SHA hashing, the Merkle root, job ID changes, and timestamps as seed inputs. It’s been running solidly for a week now, providing a genuinely random value for extranonce2. The potential here is enormous.

This randomization has allowed me to start developing a build that defines a central "focus" or search centroid, dynamically increasing or limiting search renomination in areas that demonstrate a difficulty hit or increase. Later, I’ll integrate MQTT PUB/SUB to visualize this in Grafana and enable external control of these parameters. The foundation is already in place: my board has an MQTT broker pushing data to my Home Assistant MQTT instance. I expect to have this visualization and remote-control capability ready by mid-June or July. (This ties into the beehive logic I mentioned earlier.)

The core insight here is that, while SHA provides true randomness, the structure of how we approach hashing introduces significant inefficiencies. Most pools begin at a low nonce and increment upward, starting from broadly similar timestamps and logic. Because there is no inter-pool coordination, it's highly likely that many miners re-hash the same space in the initial 3–5 minutes of a new job — resulting in massive overlap and wasted hashing power.

It’s akin to starting with a crisp TV image that gradually degrades into ideal white noise — except we always begin with the image. Instead, I’m trying to start from the noise — from unique, randomized input — to minimize duplication globally. While this may not statistically improve individual chance, it practically increases efficiency by contributing non-redundant work to the network.

The remaining issue is nonce control — specifically, setting predefined start and stop ranges (e.g., starting at 0x00000000 and stopping at 0x33333333), or reversing the direction to start high and decrement. I want to combine this with extranonce2 randomization to further diversify the search space.

While the protocol suggests that specifying nonce ranges is possible, implementing this is where I’ve hit a wall. I’ve tried to integrate this logic into bm_jobs, which seems to be the right function. But when I add a stop condition, hashing halts — suggesting either the method is incorrect or I’ve misimplemented it.

If anyone has successfully implemented nonce range limits or has insight into integrating this within bm_jobs without breaking hashing, I’d appreciate the input.








### Nexus9090 on 2025-05-27

FYI, The "esp_random" uses a hardware TRNG, so no overheads of hashing.



### g1ass1 on 2025-05-27

Yep - not cryptographically secure levels of randomness though - but likely for this if seeded with a strong seed and as you point out definitely easier to implement with less overhead.  I got abit carried away there to be fair.

so, what are next steps?
id love to understand if limiting of the nonce range is possible.

### Nexus9090 on 2025-05-27

If a TRNG isn't random given that it seeds from thermal noise, then I dont know what is.

As for next steps, I really dont know presently. I'm going to see how things go with a random extranonce_2 for a while, then I might try a decrementing version or an alternate high/low version.

I'm going to run it for at least a week in each scenario and just manually monitor it.

I'm not sure how you're going to go about a ranged version given that with Stratum you dont have full control over the nonce values.

With Stratum It seems the only bit a miner can adjust for a job is the upper portion of the total extranonce i.e extranonce_2. The rest is determined by the pool code and the linear counting actions within the ASIC.

One thing I might add is a counter to see how many extranonce_2 values are produced in a typical block period. If its only a few thousand values, then random would definately be the right way to go.

Additional thought for the end of the day.

I wonder if the lower part of extranonce can be overridden by the miner code, or if the pool will simply reject it



### precious8821 on 2025-05-31

Until the bitaxe is made to directly mine to Bitcoind's RPC, it does seem that setting a custom extra nonce range or even randomization, won't make too sense or could be a problem, due to the mining pools partially setting their own extranonce values in the coinbase.  Here is part of the problem.  The pools even use part of their own extranonces as  'coin base 1 & 2' values nearly as an extranonce signature unique to their mining pools.  Technically, according to Bitcoind's RPC guidelines, the extranonce value can be up to 100 bytes, not only 8 bytes. But with the pools, they are setting their own random partial extranonces, so it's hard to say how much of the 100 bytes available they are using up for their own partial extranonce values,  which includes their coinbase 1 & 2 values,  all of which is placed for the coinbase transaction.   Therefore, if you randomize the extranonce or set it on a custom range with a high value, you could end up exceeding the 100 byte maximum for the coinbase transaction if the mining pool is using a lot of bytes for their partial extranonce values.  Unless you set some type of limiter so that your custom extranonce plus the pools own partial extra nonce doesn't exceed 100 bytes.

### Nexus9090 on 2025-05-31

Well, my board has been running with random extranonce_2 for the past 4 days or so with a couple of interruptions while I was testing software developments and I can report that it's made little or no noticable difference to the returned share values. 

The best share during that time was 110M with most shares in the 1-10K region and occasional in the 10-500K region. So, realistically nothing different from normal.

Looking at all of the technical challenges of controlling extranonce in a meaningful way the overheads of developing something probably outweighs the benefits.

It would be nice to see ESP-Miner have a GBT function and full control over extranonce and hopefully someone will implement it. However that's not going to be me.

**_Hypothetically and unproven_** a thing that does bother me is that when a share of low value is submitted, rather than carry on from where it was found it appears to start a new job. So within a given hashing range its possible you'll get a share above pool difficulty right away not knowing that the very next hash in line is the one that wins it by which time your miner has been instructed by the pool or pre-prepared work to go look elsewhere. 

Its a bit like counting to three then being told to start again from 4billion. there's a big gap inbetween. Its a bit confusing really.

Anyway, that's me done on this topic for a while.

Good luck working it all out.

### mutatrum on 2025-05-31

> **_Hypothetically and unproven_** a thing that does bother me is that when a share of low value is submitted, rather than carry on from where it was found it appears to start a new job. So within a given hashing range its possible you'll get a share above pool difficulty right away not knowing that the very next hash in line is the one that wins it by which time your miner has been instructed by the pool or pre-prepared work to go look elsewhere.

A share submit does not stop the current nonce range, it is possible to have multiple accepted shares from a single job. The end of a job is only controlled by `asic_job_frequency_ms`, which is a time period. You can test this by making this longer, but if it's too long, the ASIC will start over in the nonce range and you'll get duplicate shares.

Also see #514 where I experimented with this. The weirdest thing I still cannot explain is that this wrap-around takes the same amount of time, no matter what the frequency is. https://github.com/bitaxeorg/ESP-Miner/issues/514#issuecomment-2548242583

### adammwest on 2025-06-02

> id love to understand if limiting of the nonce range is possible.

read PR420 in detail it contains information about size and timing for nonce ranges
https://github.com/bitaxeorg/ESP-Miner/pull/420

you need a gamma to use start location

use the  starting nonce from a  job paramater, for the bm1370 it works or you can use CNO register for start aswell
```c
int start_nonce = 512;// a number between 0-512
int start_nonce_n0 = (uint32_t)(start_nonce & 0xff;
int start_nonce_n1 = (uint32_t)(start_nonce) & 0xff;
next_bm_job->starting_nonce =  (start_nonce_n1 << 8) + start_nonce_n0;
```

for the size use hcn register 0x10 PR420 has the details and functions
```python
size = 512 # number between 0 and 512
percent = size/512
hcn_val = percent *256*256*256 * 25/(freq_mhz) 
timeout_ms = percent* 2**25 /(freq_mhz*1000)
```

nonces_rolled = size*2**16 (each core rolls this)
nonces_in_parallel = 128 (each core gets 1)

that will control the bit range
[0-7] core id
[7-16] controllable 
[16-32] rolled per core

if you use other BM chips (BM1362/66/68) only the HCN is usable meaning you get a 
0->size control only

### johnnyBytes66 on 2026-09-23

I know this is an old thread, but there is something that you may have not realized in your investigation into the HCN register (0x10). I see the 0x10 register as a timer on the Version Rolling feature only. The combination of the register x10 value and the set frequency of the ASIC determine how far into the nonce space hashing is achieved for each Version Rolled. Version Rolling continues until the hashing time limit has been reached and a new job is started. Increasing 0x10 register value will hash deeper into the nonce space. And lowering the 0x10 register value will hash less of the available nonce space before rolling the version. Increasing the hashing frequency will also hash deeper into the available nonce space without needing to change the 0x10 register.

**IMPORTANT NOTE:**
However, both the BM1366 and BM1368 are nonce limited in their hashing nonce space. And the simple formula is like this:

For BM1366: (core_count / 128) * 100 = (112 / 128) * 100 = 87.5% (12.5% not available)
The highest possible nonce for the BM1366 is 0xDFFFFFFF

For BM1368: (core_count / 128) * 100 = (80 / 128) * 100 = 62.5% (37.5% not available)
The highest possible nonce for the BM1368 is 0x9FFFFFFF

Hashing past the available nonce space (single ASIC only) for both the BM1366 and BM1368 will cause no further output until the Version is rolled. Which is why no duplicate submissions occur. The time spent past the available nonce space will lower the expected hash-rate by the amount of time wasted. However on miners with more than a single ASIC, duplicates will be submitted due to ASICs crossing boundaries into other ASIC's nonce space and rehashing nonces already hashed and this also lowers the expected hash-rate. So to prevent duplicates on multi ASIC miners, set the 0x10 register value such that hashing stays within the limits of the ASIC's available nonce space.

The BM1370 and newer ASICs don't have this nonce limitation since they have the full 128 core count. But if the 0x10 Register is set too high, the full nonce space will be hashed with time to spare which stalls hashing until the Version is rolled. The expected hash-rate will still be lower than expected with no duplicate submissions (single ASIC only of course and assuming no Version wrap-around occurs).

**ALSO NOTE:**
Duplicates will always occur on any single or multi ASIC miner if the job time is long enough that Version Rolling wraps around back to the start and hashes versions already hashed. To avoid this, decrease the job time so wrap-around never occurs. And at the same time ensure the 0x10 register value is low enough that hashing does not go beyond the ASIC's available nonce space as well.
