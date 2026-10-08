# bitaxeorg/ESP-Miner issue #134: Bitaxe 202 reboot, goes in protection mode

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/134
> Collected: 2026-10-07
> Published: 2024-03-12

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 134
- State: closed
- Author: monster4866
- Opened: 2024-03-12
- Closed: 2024-03-15
- Labels: none

## Description

Hi, my bitaxe 202 (ultra) keeps restarting after 30 seconds, then goes into protection mode, no matter what settings, whether 485/1200 or more or less, sometimes it goes for 20 minutes. Then it crashes and it freezes .

I have already tried all versions (factory reset), from 2.0.3 to 2.1.0

<img width="1193" alt="Screenshot 2024-03-12 at 23 53 29" src="https://github.com/skot/ESP-Miner/assets/119421965/dd153641-7551-4641-8563-d74d3cb1b6ee">
<img width="1218" alt="Screenshot 2024-03-13 at 00 00 10" src="https://github.com/skot/ESP-Miner/assets/119421965/8423909a-39e3-425f-b101-cee713b06662">

the logs shows nothing, or if it runs for a while the normal stuff

## Comments

### skot on 2024-03-12

uh oh, that doesn't sound good!
these screen shots don;t show the bitaxe in overtemp protection mode..  Do you ever see a hashrate above 0?

### monster4866 on 2024-03-12

<img width="1023" alt="Screenshot 2024-03-13 at 00 31 59" src="https://github.com/skot/ESP-Miner/assets/119421965/0bf43bae-398d-4384-aff7-1e1064870760">

with 2.1.1 it runs for a while,I'll see what happens,
It was also the case with the other versions that the hashrate ran occasionally for a while

### skot on 2024-03-13

Ok, so it is hashing in the beginning. In the case where it is hashing for a while and then stops, that's usually a network problem or a stratum/pool problem. What pool are you using?

### monster4866 on 2024-03-13

hi, after the update to 2.1.1 it has been running for 17 hours now, I have 9 more bitaxes in my own network, they run without any problems, I use ckpool

### skot on 2024-03-13

ok, keep an eye on it. It would be very helpful to see a log from when this happens.

### monster4866 on 2024-03-14

2 days - no problems, I'm surprised that the update seems to have solved the problem. I probably flashed the bitaxe 5-6 times with each firmware and the same problem every time, until after the update

can therefore be closed as solved @all: just update to 2.1.1 :D
