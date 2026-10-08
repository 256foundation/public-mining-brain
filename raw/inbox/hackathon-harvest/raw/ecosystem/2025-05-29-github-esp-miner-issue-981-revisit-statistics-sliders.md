# bitaxeorg/ESP-Miner issue #981: Revisit statistics sliders

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/981
> Collected: 2026-10-07
> Published: 2025-05-29

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 981
- State: closed
- Author: mutatrum
- Opened: 2025-05-29
- Closed: 2025-06-17
- Labels: none

## Description

Currently, the two sliders for statistics are a bit confusing. See https://github.com/bitaxeorg/ESP-Miner/pull/940#issuecomment-2917775619 for more information.

## Comments

### duckaxe on 2025-06-06

@terratec Shall we tackle the issue?

> Maybe we can use a single frequency slider with exponential values and show an expected value for the duration?

Which mapping for exponential values? So that I understand how the slider should work.

### mutatrum on 2025-06-06

The Display Sleep slider. If we stick to 720 datapoints, it can go from 30 minutes (1/minute) to (almost) 2 years (1/day). Not sure if the latter is useful, I haven't often seen uptimes over 1 month.

So maybe something like 

- 30 minutes
- 1, 2, 4, 8 hours
- 1,2,3 days
- 1, 2 weeks
- 1 month

Don't know. Something feels off with this, but I'm not sure. The 720 datapoint limit makes it weird. A nicer solution would be to have several series on different timescales, but that's a way bigger change.

### terratec on 2025-06-06

Something like this?

![Image](https://github.com/user-attachments/assets/99c74a59-ba5a-4b21-a350-2726fcfa09a7)

![Image](https://github.com/user-attachments/assets/375bdd89-ec70-49fc-9ba7-cc578ddc4c55)

![Image](https://github.com/user-attachments/assets/2752705d-aa6e-446a-bf9e-186681a71f7a)

![Image](https://github.com/user-attachments/assets/53beb75b-2e39-44ee-a095-f7e04a788ee6)
