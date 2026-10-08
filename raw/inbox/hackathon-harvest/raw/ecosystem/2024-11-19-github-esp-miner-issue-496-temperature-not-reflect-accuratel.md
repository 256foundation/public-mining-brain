# bitaxeorg/ESP-Miner issue #496: Temperature not reflect accurately in graph; not coming back down

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/496
> Collected: 2026-10-07
> Published: 2024-11-19

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 496
- State: closed
- Author: andrewschafer
- Opened: 2024-11-19
- Closed: 2025-04-16
- Labels: none

## Description

There is a bug in the temperature graph.  See the attached picture where the graph is stuck at ~69 deg, but the actual ASIC is at 63.5 deg.

I noticed because my BitAxe is on my garage workbench and the point where the graph goes up is when a heated car pulled up next to it (around 5 pm).  As the car cooled, the ASIC temp came down, but the graph did not reflect that.  I opened the garage door to let cold air in, which also reduced the ASIC more, but had no affect on the graph.


![Temp Graph](https://github.com/user-attachments/assets/1f270d08-cebc-4de0-a07c-3130189e9178)


Refreshing the dashboard in the browser fixed the issue with the graph.

## Comments

### skot on 2024-11-20

Interesting, I'm not seeing this on mine, but it looks like you have _a lot_ of datapoints! I wonder if that's causing the problem.

### skot on 2024-11-22

I got a bunch of datapoints on the graph last night. seems to be moving up and down ok. Although they are somewhat out of sync, and definitely not to the same precision
<img width="747" alt="image" src="https://github.com/user-attachments/assets/81d96133-6db2-4978-853f-8565e4c264cf">



### WantClue on 2024-12-10

Might be good if you could double check that again?
I also tested it on my devices and the temp chart does come down indeed.

### diegorodriguezv on 2025-01-26

I'm having problems like this also. I think what's happening is that the old points for the ASIC temp in the graph are "stuck", that is, not being removed from the left end of the graph after one hour has elapsed. I thought new points where being added to the right but now I'm not so sure. Maybe it has to do with the last upgrade to v2.5.1. I could have sweared that point where being added to the right and not removed from the left causing the graph to "compress" but unfortunately I didn't save a screenshot. After the upgrade, it just seems stuck.

### skot on 2025-01-26

Yes, the graph will "compress" untill it reaches about 12 hours, and then old data points will be removed from the left. This graph has been running for days; 

<img width="1528" alt="Image" src="https://github.com/user-attachments/assets/3a005230-ddae-4d05-937f-74957605b788" />

### diegorodriguezv on 2025-01-26

Here is a couple of screenshots I managed to get. Note that the temperature drop when I changed some settings, loses synchronization from the hash rate.

![Image](https://github.com/user-attachments/assets/f40c54da-344d-4e5d-8375-70c54144153a)

![Image](https://github.com/user-attachments/assets/ac78f955-b4ed-4a4e-82dd-712cf7d77db7)

### skot on 2025-01-27

> Here is a couple of screenshots I managed to get. Note that the temperature drop when I changed some settings, loses synchronization from the hash rate.

What bitaxe hardware do you have?

### diegorodriguezv on 2025-01-27

Bitaxe Gamma 601. Running version 2.5.1. Using Firefox in Ubuntu 24.04. 

### skot on 2025-01-27

Do you mind posting a picture of your Gamma? Unfortunately we've got a couple different "601" out there

### diegorodriguezv on 2025-01-27

I added the heatsinks to the voltage regulator.

![Image](https://github.com/user-attachments/assets/d57c4343-1048-4790-9a58-05acb795ab61)

![Image](https://github.com/user-attachments/assets/8758147d-dc34-4a4c-a547-379282987efc)

The vendor is "bitcoin merch".

### skot on 2025-01-27

hmm. Can you give it a try with those heatsinks (carefully) removed? I'm also curious if the guage below shows the same temperature as on the graph?

### diegorodriguezv on 2025-01-27

Before adding the heatsinks the voltage regulator temperature was about 8 C higher. The ASIC temp was the same. The auto-fan keeps it stable at 60 C (for weeks). That's why it was hard to spot the problem with the temp graph. Only when I updated the software and experimented a little with a higher frequency (thus creating "breaks" and "curves") was I able to spot the desynchronization between the temp and hashrate graphs.

### diegorodriguezv on 2025-01-27

Also I took great care so that the heatsinks aren't touching any components below.

### diegorodriguezv on 2025-01-27

![Image](https://github.com/user-attachments/assets/6723d8fd-e0d5-46cf-8438-37a8a9d3cefa)

### skot on 2025-01-27

I kinda think this is working as intended... What are you expecting to see that you're not?

### diegorodriguezv on 2025-01-28

I expect that all graphs  should have the same X-axis scale (time). But I believe that the hashrate graph has a 1h scale while the ASIC Temp graph has an undetermined scale. I believe that no old points are being removed from the left edge of the graph while new points are being added to the right up to a certain point. The timestamps reported while hovering over the ASIC Temp points are misleading since they reflect the timescale of the hashrate graph which seems to be updating correctly.

I just did an experiment. I left the page open for a day. Then I turned the autofan off and increased the fan speed to 99%. The ASIC temp dropped a couple of degrees which where visible in the Heat panel. After about an hour I decreased the fan speed to 45%. The ASIC temp started to climb up to the point where an overheat message was shown. But the ASIC temp graph remained unchanged, which leads me to believe that at some point the graphing library stops updating new data points. Which is what was first reported in this issue.

![Image](https://github.com/user-attachments/assets/85360183-c715-422e-843f-d45b44c413a8)

![Image](https://github.com/user-attachments/assets/1b83c7f4-5b78-440e-9fa9-641822c69858)

### skot on 2025-03-09

https://x.com/devjock/status/1898715377946820956?s=46&t=8isHpCQqCFogL4byGwt7DA

### diegorodriguezv on 2025-03-13

https://github.com/user-attachments/assets/702a252b-0961-40c2-b4a1-2a145d0a13a7

This is the video that was posted on twitter.

> Hashrate plot, it chucks oldest datapoints off the left side. Asic temperature, it doesn't "purge" datapoints. It gets stuck. Made a 5 minute recording. FFWD'ing through it shows the issue clear as day. Hope this helps!
