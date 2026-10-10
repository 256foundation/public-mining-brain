# bitaxeorg/ESP-Miner issue #1665: Small memory leak in ESP-Miner v2.14.0b1

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1665
> Collected: 2026-10-07
> Published: 2026-04-17

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1665
- State: closed
- Author: aibaoku
- Opened: 2026-04-17
- Closed: 2026-04-19
- Labels: none

## Description

**Describe the bug**
There is a slow memory leak in ESP-Miner FW v2.14.0b1.
The device continuously loses about ~0.5KB of free heap per day.
The leak is small but accumulates over long uptime.

**To Reproduce**
1. Flash firmware v2.14.0b1
2. Start mining normally
3. Keep device running for 24+ hours
4. Monitor free heap (e.g. via logs or system status)
5. Observe gradual decrease in free memory over time

**Expected behavior**
Free heap should remain stable over time during normal mining operation.

**Logs**
uptime/s		            98	3853	56676	146840	167865	229471
freeHeapInternal	88491	88595	86871	85619	85375	84687
freeHeapSpiram	7615516	7616700	7615836	7615256	7610272	7614964


**Hardware (please complete the following information):**
 - Bitaxe HW version: 602
 - Bitaxe HW vendor: official
 - ESP-Miner FW version: 2.14.0b1
 - Hash Frequency: 750
 - Voltage: 1150
 - Pool URL, Port, User: public-pool.io 3333

**Additional context**
- The leak appears unrelated to pool communication (already tested)
- Happens on stable network conditions
- No crashes observed yet, but long-term uptime may be affected
- Estimated leak rate: ~0.5KB/day

## Comments

### mutatrum on 2026-04-17

Thank you, well spotted! Testing fixes now.
