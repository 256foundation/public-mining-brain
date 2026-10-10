# bitaxeorg/ESP-Miner issue #1688: Braiins pool reporting block found on low difficulty share

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1688
> Collected: 2026-10-07
> Published: 2026-05-12

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1688
- State: open
- Author: pea76nuttmining-lang
- Opened: 2026-05-12
- Closed: n/a
- Labels: none

## Description

I was on brains pool, and I found a block so I took a screenshot of it, but they said, I did not find a block.The miner said, I found one brainspool told me to contact the manufacturer.I'm trying to find out what happened

<img width="1856" height="2160" alt="Image" src="https://github.com/user-attachments/assets/1a1fa543-8dd8-4225-9e1f-a03201f562c8" />
<img width="1856" height="2160" alt="Image" src="https://github.com/user-attachments/assets/4b6834c3-9db6-4d7d-9d63-1829abf9d692" />
<img width="1856" height="2160" alt="Image" src="https://github.com/user-attachments/assets/cd70819c-110d-4408-9fc1-98979a75853a" />

## Comments

### mutatrum on 2026-05-12

What version of the firmware are you running? Maybe you can post a screenshot from the System tab.

### pea76nuttmining-lang on 2026-05-13

I'll check it when I go home.ill let you know

Yahoo Mail: Search, Organize, Conquer 
 
  On Tue, May 12, 2026 at 5:58 PM, ***@***.***> wrote:   mutatrum left a comment (bitaxeorg/ESP-Miner#1688)
What version of the firmware are you running? Maybe you can post a screenshot from the System tab.

—
Reply to this email directly, view it on GitHub, or unsubscribe.
Triage notifications on the go with GitHub Mobile for iOS or Android.
You are receiving this because you authored the thread.Message ID: ***@***.***>
   


### pea76nuttmining-lang on 2026-05-13

I will check it when I get home.I will let you know

### shufps on 2026-05-13

I saw something similar being reported by a couple of people on the Nerd*axes too, I thought maybe Braiins pool is dishonest and mixes other jobs (another low-difficulty coin) into the Stratum stream. The false positive founds raised suspicion and was one reason for working on the "lottery mining verify" but after a short first test Braiins is reported 100% honest.

Total best difficulty needs to be reported with  >132.47 T, according to your screenshots your Bitaxe only reports 1G what is a false positive.

Following this issue with interest because I haven't found an explanation yet (other than assuming dishonesty from the pool - or a bug in the stratum server code)

Could you please drop the exact pool URL so I can use the same setting for further tests? 



### mutatrum on 2026-05-13

I assume this is solo.stratum.braiins.com?

Need to catch it in the logs to see what happens.

### shufps on 2026-05-13

> I assume this is solo.stratum.braiins.com?
> 
> Need to catch it in the logs to see what happens.

I think too yes, I'm investigation this one.

I'm currently running a test that prints information about the coinbase, let's see maybe we see some blips in the reported network difficulty. 

I'll let it run for some days, maybe it's a glitch in the Stratum pool or so ...

### pea76nuttmining-lang on 2026-05-13

Last night I got in pretty late. I forgot but I will send you a screenshot of the software on.

### shufps on 2026-05-13

Btw according to your screenshot it seems to have happened around bitcoin difficulty adjustment.

I think the next one should be in some few days (approx on 15th), maybe ckpool (braiin uses a self-hosted ckpool in their backend) pushes some weird difficulty temporary when it changes 🤔 

But maybe it was concidence, but nonetheless I'll be prepared to watch it closely 🫡 

(the last 9h were free of glitches according to the log)

### pea76nuttmining-lang on 2026-05-14

<img width="1856" height="2160" alt="Image" src="https://github.com/user-attachments/assets/92e42536-5c1b-4720-aaab-b8732009365f" />

### pea76nuttmining-lang on 2026-05-14

So, what exactly does that mean?.So did the miner hit a block

Yahoo Mail: Search, Organize, Conquer 
 
  On Wed, May 13, 2026 at 12:06 PM, Thomas ***@***.***> wrote:   shufps left a comment (bitaxeorg/ESP-Miner#1688)
Btw according to your screenshot it seems to have happened around bitcoin difficulty adjustment.

I think the next one should be in some few days, maybe ckpool pushes some weird difficulty temporary when it changes 🤔

—
Reply to this email directly, view it on GitHub, or unsubscribe.
Triage notifications on the go with GitHub Mobile for iOS or Android.
You are receiving this because you authored the thread.Message ID: ***@***.***>
   


### mutatrum on 2026-05-14

No, best diff is 1.07G, that's too low. It seems to be either a bug in the braiins pool, or the Bitaxe firmware, or both. 2.11 is a bit older, so updating this to the latest would help, as it's difficult to analyse and fix bugs on older firmware versions. I haven't had time to test with braiins pool yet.

### shufps on 2026-05-14

I don't think it's the firmware.

I tested the nbits -> difficulty function from the bitaxe (and nerd*) against the reference from bitcoin core and there doesn't seem to be any problem with it.

[fuzz_difficulty.c](https://github.com/user-attachments/files/27776466/fuzz_difficulty.c)

test with `gcc -O3 fuzz_difficulty.c -lm` and start `./a.out`

> I haven't had time to test with braiins pool yet.

My tests are still running, today the next difficulty adjustment should happen 🤞 

### pea76nuttmining-lang on 2026-05-15

Ok

Yahoo Mail: Search, Organize, Conquer 
 
  On Thu, May 14, 2026 at 4:26 PM, Thomas ***@***.***> wrote:   shufps left a comment (bitaxeorg/ESP-Miner#1688)
I don't think it's the firmware.

I tested the nbits -> difficulty function from the bitaxe against a reference and there doesn't seem to be any problem with it.

fuzz_difficulty.c

test with gcc -O3 fuzz_difficulty.c -lm and start ./a.out

—
Reply to this email directly, view it on GitHub, or unsubscribe.
Triage notifications on the go with GitHub Mobile for iOS or Android.
You are receiving this because you authored the thread.Message ID: ***@***.***>
   


### shufps on 2026-05-16

<img width="699" height="118" alt="Image" src="https://github.com/user-attachments/assets/48a596b0-0593-4f2d-a15d-16fa62742838" />

I couldn't observe glitches over 3 days test, no idea 🤷‍♂️  Difficulty adjustment went smooth, nothing suspicious.

### adammwest on 2026-06-02

> I saw something similar being reported by a couple of people on the Nerd*axes too, I thought maybe Braiins pool is dishonest and mixes other jobs (another low-difficulty coin) into the Stratum stream. The false positive founds raised suspicion and was one reason for working on the "lottery mining verify" but after a short first test Braiins is reported 100% honest.

I reported in discord that braiins gives jobs from other pools even other chains, this could be relevant here, it could be braiins sent a job for another pool/chain, The source of nbits comes from the pool mining.notify if it is low bitaxe would think it hit a high diff.

I get 2.2% non btc blocks (block heights that are not possible < 900000) accross my ~30 bitaxes for over the last month or so all on braiins pool (not solo though).

### sololuckio on 2026-07-05

i can only dream my bitaxe, nerdqaxe and octaxe showing that one day =)
