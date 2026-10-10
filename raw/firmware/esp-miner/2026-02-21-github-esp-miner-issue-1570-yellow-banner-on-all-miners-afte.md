# bitaxeorg/ESP-Miner issue #1570: Yellow banner on all miners after upgrading to 2.13.0

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1570
> Collected: 2026-10-07
> Published: 2026-02-21

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1570
- State: closed
- Author: pjones112000
- Opened: 2026-02-21
- Closed: 2026-02-21
- Labels: none

## Description

I upgraded to 2.13.0 on my Bitaxe Gamma 601 devices (6 of them).  Now all miners have a yellow banner at the top saying "You don't have a share in the coinbase reward".

Steps to reproduce the behavior:
1. Install both www.bin and exp-miner.bin, reboot.
2. Wait for dashboard to load
3. See error

I wasn't expecting to see this message.

<img width="1846" height="286" alt="Image" src="https://github.com/user-attachments/assets/c315439d-af43-4376-affe-1c991d46dc87" />


**Hardware (please complete the following information):**
 - Bitaxe HW version: Gamma 601
 - Bitaxe HW vendor: Various from Amazon
 - ESP-Miner FW version: 2.13.0
 - Hash Frequency: Default
 - Voltage: Default
 - Pool URL, Port, User:  Doesn't matter what pool.... I'm running a local DGB pool but also connecting to Unmineable.com and Firepool.ca
 - 

**Additional context**
I don't know what to make of this error message...my pool is showing connectivity of the miners connecting to it so I know they are connecting so I don't understand the message or purpose of it.

I apologize if this is normal behavior or if I've missed some vital information as this is my first post for this particular application/solution.  I've been using BitaxeOS for about 4 weeks without issues.

## Comments

### LsLoki on 2026-02-21

As I am also not mining bitcoin chains - in my Axe OS I went to pool/pool configuration/advanced options and unchecked Decode Coinbase Tx - by default it is checked which is not what I/you need. 

### pjones112000 on 2026-02-21

Thank you, @LsLoki, that did the trick.

### Bradvani on 2026-03-06

I had the same issue until I unchecked the decode coinbase tx option under advanced pool settings just like @LsLoki suggested. Seems to be good now.
