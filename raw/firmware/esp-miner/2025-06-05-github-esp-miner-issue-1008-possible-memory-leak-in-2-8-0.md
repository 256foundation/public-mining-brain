# bitaxeorg/ESP-Miner issue #1008: Possible memory leak in 2.8.0

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1008
> Collected: 2026-10-07
> Published: 2025-06-05

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1008
- State: closed
- Author: remcoros
- Opened: 2025-06-05
- Closed: 2025-06-06
- Labels: none

## Description

**Describe the bug**
After upgrading from 2.7.1 to 2.8.0, the free heap is becoming less over time.

I am using prometheus to hit the api/system/info endpoint about every 15 sec.

this is the free heap graph from the last 7 days, notice the drop after the upgrade to 2.8.0

![Image](https://github.com/user-attachments/assets/6c4e797a-a8a2-49d2-939a-fa175e0ba1df)

These are 2 supras and a gamma, all upgraded at the same time from 2.7.1 to 2.8.0


## Comments

### mutatrum on 2025-06-05

As a test, can you have some script hit the same API endpoint every 15 seconds for a bit as well, to see if the free heap decreases faster?

### remcoros on 2025-06-05

It actually is decreasing faster, I have two prometheus instances, the first monitoring all three bitaxes, the second only the gamma. So the gamma gets hits twice every 15 seconds, hence the reason why it goes down twice as fast as the other two (which overlap almost perfectly).
So I suspect it's something new in the /api/system/info endpoint (a missing free?)

### KillerInk on 2025-06-06

yes looks like there is a leak.
set statistic to 1 hour 300 points

![Image](https://github.com/user-attachments/assets/d9d75f5b-a2cb-4b43-88e6-ee1996e8d43d)

im expected that ram drops aslong new data gets added. but after the 300 datapoints its still dropping

### mutatrum on 2025-06-06

Found it. `display` configuration string was not freed. This caused a 24 byte memory leak every time `api/system/info` was called. Thanks both for the details information, that gave a solid lead to where to start looking.
