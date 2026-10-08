# bitaxeorg/ESP-Miner issue #328: make AxeOS plot lines straight.

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/328
> Collected: 2026-10-07
> Published: 2024-09-06

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 328
- State: closed
- Author: skot
- Opened: 2024-09-06
- Closed: 2024-10-10
- Labels: enhancement, help wanted, good first issue

## Description

<img width="462" alt="image" src="https://github.com/user-attachments/assets/564ec7e5-e1e5-4829-80a5-db08d6a20d9f">

It's kinda silly IMO to have the plot lines be these bezier-like curves. Can we make them just straight lines? It will avoid this "time travel" look.

## Comments

### mrv777 on 2024-09-27

This should be changing tension: .4, to tension: 0
(Might be able to get away with a little curve like .1)
