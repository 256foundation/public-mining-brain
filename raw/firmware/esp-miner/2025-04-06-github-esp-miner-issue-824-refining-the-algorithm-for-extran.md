# bitaxeorg/ESP-Miner issue #824: Refining the algorithm for extranonce2.

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/824
> Collected: 2026-10-07
> Published: 2025-04-06

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 824
- State: open
- Author: vaavdeev
- Opened: 2025-04-06
- Closed: n/a
- Labels: question

## Description

At the moment, the program assigns a value of 0 by default and iterates over all nonce.
Then, when the nonce values ​​are exhausted, it increases the value of extranonce2 by one and again iterates over all nonce.
A new block appears in the network every 10 minutes, and the task is formed anew.
In 10 minutes, Bitax Gamma manages to go through a maximum of 0 to 167 extranonce2 values.
Each time in a new task, we have the same range for work from 0 to 167.
Please refine the program with the ability to select the initial value for the extranonce2 range.
For example, in the WEB interface of the device.
Thank you.

## Comments

### mutatrum on 2025-04-06

The nonce space algorithm is also non-exhaustive, there's already a PR for that: #420 

The time spent on the nonce is time limited (~500ms), so it won't exhaust it. At the end of a specific time period, it goed to the next job goes to the next extranonce2. In the linked issue is some work to scan the full nonce range. Only after that has been done, would it make sense to look at the extranonce2 range.

But IMO it doesn't make a difference what range you pick, as it's all input for the hash anyways. Or are there cases where you need a specific extranonce2 range?

### vaavdeev on 2025-04-06

Yes, I understand about the input data for hash.
However, I wanted to experiment with extranonce2.
we are limited to the range 0-160 unlike the pools
Since extranonce2 is part of coinbase_script.
Basically, we make coinbase_script.
coinbase_script is part of tx_make_coinbase.
I think I'll try my luck in another range of extranonce2.
I plan to choose the range intuitively.
At the moment, I can't influence the calculations.
I want to add a human factor.
I have a friend who is a psychic :-)

Maybe it would be better to add random generation of extranonce2
Or several options for formation extranonce2

### skot on 2025-04-06

> I plan to choose the range intuitively.
> At the moment, I can't influence the calculations.
> I want to add a human factor.
> I have a friend who is a psychic :-)

I think this is a really interesting idea. I have experimented with this also.

That said, this would be much more appropriate in an esp-miner fork tailored for these types of experiments.

Also, fyi in normal usage on the Bitaxe the extranonce hardly ever gets changed.



### vaavdeev on 2025-04-07

> > I plan to choose the range intuitively.
> > At the moment, I can't influence the calculations.
> > I want to add a human factor.
> > I have a friend who is a psychic :-)
> 
> I think this is a really interesting idea. I have experimented with this also.
> 
> That said, this would be much more appropriate in an esp-miner fork tailored for these types of experiments.
> 
> Also, fyi in normal usage on the Bitaxe the extranonce hardly ever gets changed.

The idea is to change extranonce_2.

extranonce is a different story. It is a constant in the session.
It is assigned Stratum server.

The code is proposed to be changed in the file main/tasks/create_jobs_task.c

At the moment, there is such code:
**// Increase extranonce_2 for the next job.
extranonce_2++;**

I think to make a fork

### vaavdeev on 2025-04-11

The idea with extranonce_2 is intended for a version of your own costum stratum server.
Receiving a new task within 10 minutes or custom intervals.
During this period it is possible to run through a large range of values of extranonce_2.
When using public pools like solo.ckpool.org, the task changes every 30 seconds.
Therefore, there is no point in changing the extranonce_2 algorithm when using public pools.
