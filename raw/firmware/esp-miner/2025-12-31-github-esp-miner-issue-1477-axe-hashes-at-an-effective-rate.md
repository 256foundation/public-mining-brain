# bitaxeorg/ESP-Miner issue #1477: axe hashes at an effective rate of half or worse, likely when on non-bitcoind backends

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1477
> Collected: 2026-10-07
> Published: 2025-12-31

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1477
- State: closed
- Author: 0xf0xx0
- Opened: 2025-12-31
- Closed: 2026-07-25
- Labels: none

## Description

**Describe the bug**
some boots my axe will report full hashrate in axeos but the actual submission rate is half or a quarter, with lots of 0 diff `asic_result`s in the logs.

**To Reproduce**
Steps to reproduce the behavior:  
unknown :\ i just know by my pool estimating my hashrate at half what axeos reports.

**Hardware:**
 - Bitaxe HW version: Gamma 601
 - Bitaxe HW vendor: GekkoScience
 - ESP-Miner FW version: v2.13.0b1
 - Hash Frequency: 550
 - Voltage: 1080
 - PSU: Meanwell GST60A05-P1J
 - Input voltage under load: 4.7-4.8v

**Additional context**

[boot logs](https://github.com/user-attachments/files/24390431/boot.log)


## Comments

### KillerInk on 2026-01-02

you are sure with the voltage?

### 0xf0xx0 on 2026-01-02

chip or input? chip is measured at 1074 due to the sag, input voltage is recorded from axeos and the api.

E: also grabbin a higher power psu and xt60 pigtails to rule out the barrel

### dem10 on 2026-01-12





> chip or input? chip is measured at 1074 due to the sag, input voltage is recorded from axeos and the api.
> 
> E: also grabbin a higher power psu and xt60 pigtails to rule out the barrel

It's not the power supply. For some reason, the firmware is breaking the hash. The registered hash never rises above 300-400Gh/s.

<img width="1536" height="864" alt="Image" src="https://github.com/user-attachments/assets/531ac124-d835-40d2-b171-369073e0da9a" />

<img width="1536" height="864" alt="Image" src="https://github.com/user-attachments/assets/760834a2-3de9-4ab9-9cdf-bca5ff84c967" />

### 0xf0xx0 on 2026-01-15

> chip or input? chip is measured at 1074 due to the sag, input voltage is recorded from axeos and the api.
> 
> E: also grabbin a higher power psu and xt60 pigtails to rule out the barrel

debugged on a lrs100, same issue  
switched backend nodes from btcd to bitcoind and 0 diffs disappeared? this needs further investigation but its definitely not a power issue

if someone else can run a pool with btcd and try and reproduce thatd be great

### 0xf0xx0 on 2026-01-15

> It's not the power supply. For some reason, the firmware is breaking the hash. The registered hash never rises above 300-400Gh/s.

unrelated and not an issue, add up the domains @dem10 

### dem10 on 2026-01-16

> > It's not the power supply. For some reason, the firmware is breaking the hash. The registered hash never rises above 300-400Gh/s.
> 
> unrelated and not an issue, add up the domains [@dem10](https://github.com/dem10)

The pool reports that there is no hash rate of 1 terahash, although there was one previously.

<img width="1536" height="864" alt="Image" src="https://github.com/user-attachments/assets/e6220f2a-de00-4448-938a-7b63cfd21ffe" />

### 0xf0xx0 on 2026-01-16

hm, which pool? does it happen on a different pool? are there `diff 0.0`s in your logs?

### dem10 on 2026-01-19

> hm, which pool? does it happen on a different pool? are there `diff 0.0`s in your logs?

solo.ckpool.org 



### 0xf0xx0 on 2026-07-25

closing for now, will revisit at some point
