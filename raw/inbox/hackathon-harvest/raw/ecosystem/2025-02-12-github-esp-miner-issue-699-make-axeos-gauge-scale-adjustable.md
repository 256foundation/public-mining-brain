# bitaxeorg/ESP-Miner issue #699: make AxeOS gauge scale adjustable for different Bitaxe models

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/699
> Collected: 2026-10-07
> Published: 2025-02-12

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 699
- State: closed
- Author: skot
- Opened: 2025-02-12
- Closed: 2025-03-27
- Labels: enhancement, help wanted, design

## Description

<img width="1470" alt="Image" src="https://github.com/user-attachments/assets/74cfdc69-4fa3-435c-86b9-d02901c9e3b7" />

Currently it looks like the scaling for the AxeOS scales are hardcoded. This is tough when we need to support different Bitaxe models with (some drastic) differences in readings.

Ideally AxeOS would update the gauge scales from a call to a function in `/main/power/power.c`

Also, it would be nice if the Input Voltage nominal marker was always in the middle of the gauge.

## Comments

### skot on 2025-02-18

this is to support https://github.com/skot/ESP-Miner/issues/718

### w3irdrobot on 2025-02-21

yeah I can look into this. if the values we get through the info endpoint have been hooked up, then this should be pretty simple. 

### w3irdrobot on 2025-03-07

@skot perhaps i'm missing it, but do we have a way of obtaining some of these board-specific constants right now? maybe i'm just missing it in the code, but I only see, in `power.c` for example, how we get the current value, not the maximum allowed value based on the board. 

### skot on 2025-03-07

> @skot perhaps i'm missing it, but do we have a way of obtaining some of these board-specific constants right now? maybe i'm just missing it in the code, but I only see, in `power.c` for example, how we get the current value, not the maximum allowed value based on the board. 

You're right we don't have functions to return those board specific constants yet. I think power.c is probably the right place for them.

If you're working on the front end components can you just pretend they exist and then I'll add them?

### w3irdrobot on 2025-03-25

@skot i've been busier than expected. i'm not sure i'll be able to get this over the line in a timely manner. i can still do the work if it can wait. otherwise, it might be better if someone else picked this one up.

### WantClue on 2025-03-27

#793 closes this
