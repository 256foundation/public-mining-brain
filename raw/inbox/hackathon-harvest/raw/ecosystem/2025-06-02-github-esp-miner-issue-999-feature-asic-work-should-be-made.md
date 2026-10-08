# bitaxeorg/ESP-Miner issue #999: Feature: Asic work should be made from the newest stratum job

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/999
> Collected: 2026-10-07
> Published: 2025-06-02

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 999
- State: closed
- Author: adammwest
- Opened: 2025-06-02
- Closed: 2026-01-21
- Labels: none

## Description


**Relevent quotes** 
this was discussed in PR420
skot 
```
It sounds like even if clean_jobs = false the pool does expect the miner to switch over to the new work (new JobID) in some amount of time.

Can we realistically switch on every mining.notify?
``` 

ben 
```
The miner should switch to new work sent by the pool as fast as reasonably possible to avoid missing out on new/high fee txs
```



**Problem**
Currently the stratum messages are put in a queue, then jobs are made by rolling extranonce2
a few jobs can come in, but work is still being generated from an old stratum job. because a single chip is quite slow the extranonce2 range will never be exhausted therefore the job wont change until clean_jobs=true.

**Solution**
Clear the work queue immidiatly after a new stratum job message comes in regardless of clean_jobs=
then only generate work from this new stratum message


**Benefit**
Higher transaction fees/newer tx in a block

**Status**
Awaiting others opinions before this is decided as a good approach

## Comments

### mutatrum on 2025-06-02

I'm currently running a proof of concept without `ASIC_task`. In `generate_work` a new job is not put on the `ASIC_jobs_queue` but it's directly passed onto `ASIC_send_work`. Of course, this is only feasible for chips that can run long enough on a single job to get to the next `mining.notify`. One aspect is that `extranonce_2` never changes and that `ASIC_job_timeout` is not needed anymore.

### mutatrum on 2025-06-04

Proof of concept code: https://github.com/mutatrum/ESP-Miner/tree/no-asic-task

I don't think this will work on chips without version rolling, as the total work time is too short.

### 0xf0xx0 on 2025-06-05

runnin the poc for a day on my gamma with various clock settings, pretty good so far ![Image](https://github.com/user-attachments/assets/d86a5bf8-7d27-495c-aab1-6d1a83a02632)

### mutatrum on 2025-06-05

It should be tested on a Max, without version rolling. Don't think that'll work though.

I did notice lower rejected shares as well on my Gamma btw.
