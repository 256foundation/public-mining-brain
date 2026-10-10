# bitaxeorg/ESP-Miner issue #1789: Simplify Bitaxe OLED display

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1789
> Collected: 2026-10-07
> Published: 2026-06-26

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1789
- State: open
- Author: skot
- Opened: 2026-06-26
- Closed: n/a
- Labels: enhancement, Feedback

## Description

I'm starting to think we're showing too much on the bitaxe OLED. It's a really small screen that gets cluttered easily. I think we should focus on showing the absolute minimum amount of data;
- hashrate
- temperature
- best difficulty
and then maybe a secondary screen that only comes up when you press boot;
- IP address
- ?

All of the rest of the data that we currently show is useful, but it's better shown on the dashboard where there is plenty of room.

## Comments

### skot on 2026-06-27

Something like this 

<img width="512" height="129" alt="Image" src="https://github.com/user-attachments/assets/75507ced-0e5d-4182-8c88-afae938d1f59" />

I created a LVGL Pro XML file to do this if anyone can figure out that madness; https://github.com/skot/bitaxe-oled
