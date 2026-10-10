# bitaxeorg/ESP-Miner issue #710: Profiles for different configurations for easily switching settings

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/710
> Collected: 2026-10-07
> Published: 2025-02-15

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 710
- State: open
- Author: DerekMiner
- Opened: 2025-02-15
- Closed: n/a
- Labels: none

## Description

It would be nice to offer the ability to save settings to a profile list where the user can then easily switch between these profiles.
It would take all the settings in the settings page, allow the user to save it to a profile name, and then load other profiles that were previously saved into this list. 

This helps with a few things: 
1) As the number of options increase, a user may want to save particular configs for usage later for easily switching between the configs.
2) Allows a user to test out and compare settings for these configs quickly
3) If a user has different pools they want to easily switch between, for example a user could setup one config for mining to a solo pool, they could have another profile for mining in a larger pool shared with other users

Some other ideas for these profiles, is to save an average of the Hashrate, energy usage, and other stats while running in that profile to the profile so a user can easily compare previously run profile stats.

I think it would make the most sense to implement the settings via a JSON file, it would not require much storage at all, even to save average stats.
