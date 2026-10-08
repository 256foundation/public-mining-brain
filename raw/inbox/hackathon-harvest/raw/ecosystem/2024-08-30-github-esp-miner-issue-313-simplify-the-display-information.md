# bitaxeorg/ESP-Miner issue #313: Simplify the display information

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/313
> Collected: 2026-10-07
> Published: 2024-08-30

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 313
- State: closed
- Author: skot
- Opened: 2024-08-30
- Closed: 2024-10-09
- Labels: enhancement, good first issue

## Description

I think we can remove a lot of the information from the OLED. It's all available in AxeOS and the API for people who really care.

1st screen:
- Hashrate
- Efficiency
- Best Difficulty
- Temp

2nd screen:
- pool url
- esp-miner version
- IP address

It might also help to modernize the display library at the same time, as suggested in #299 

## Comments

### Barnminer on 2024-08-30

Sounds like a good idea to me. It would deff make it less busy, 

### WantClue on 2024-09-02

Working on this this week 

### WantClue on 2024-09-03

@skot https://github.com/WantClue/ESP-Miner-WantClue/tree/simplify_screen
