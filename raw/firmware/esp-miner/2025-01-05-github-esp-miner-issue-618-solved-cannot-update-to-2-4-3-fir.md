# bitaxeorg/ESP-Miner issue #618: SOLVED - cannot update to 2.4.3 firmware / website - bitaxe gamma 600 with ESP MON16, crashing when updating

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/618
> Collected: 2026-10-07
> Published: 2025-01-05

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 618
- State: closed
- Author: filipponeri
- Opened: 2025-01-05
- Closed: 2025-01-07
- Labels: none

## Description

Hi, I cannot update to the 2.4.3 firmware / website on a bitaxe gamma 600 with ESP MON16. 
The upload of the two files keeps freezing the web interface. After restart the onboard display does not turn on. I had to downgrade back to 2.4.2.
I bought from bitronics.store
 

## Comments

### matlen67 on 2025-01-06

I had the same problem today with my 601 when updating from 2.4.3 -> 2.4.4. The updates stopped between 30% and 99% of the time. After several update attempts, I entered an invalid address in the stratum host (also fallback) so that it would not start mining after a restart (host= abc.de). After that the update worked. 

Addendum. Back to v2.4.3 the www.bin hung up and I ended up in recovery. Recover worked and then I went back to 2.4.4, which worked perfectly.

### filipponeri on 2025-01-06

same problem with the 2.4.4 release

### TowyTowy on 2025-01-06

Happens to me too, I have to reflash the firmware every time I've tried...

### WantClue on 2025-01-07

resolved with v2.4.5

### filipponeri on 2025-01-07

SOLVED with v2.4.5. It works.
