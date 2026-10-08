# bitaxeorg/ESP-Miner issue #1604: BitAxe doesn't connect if primary pool is Datum v0.4.1beta server

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1604
> Collected: 2026-10-07
> Published: 2026-03-11

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1604
- State: open
- Author: tlindi
- Opened: 2026-03-11
- Closed: n/a
- Labels: none

## Description

Note: Issues are not for customer support, configuration or discussion. For those topics please consult with your HW vendor or the OSMU Discord at: https://osmu.bitaxe.org

**Describe the bug**
If I configure my Datum service running on MyNodeBTC as primary pool on bitaxe, and eg ckpool as second. Bitaxe always connects to ckpool. But if I place exactly same datum settings as fallback, BitAxe connects to Datum correctly.

**To Reproduce**
Steps to reproduce the behavior:
1. Go to Poolsetup 
2. set primary pool to datum
3. set fallback pool to some other pool
4. Restart bitaxe and Check logs
5. * You see it tries to connect to Datum, but fallbacks without any error shown
6. Add datum also to fallback
7. Restart bitaxe and Check logs
8. You will see bitaxe connecting to datum.

**Screenshots & Photos**
Can deliver if needed.

**Hardware (please complete the following information):**
 - Bitaxe HW version: 601
 - Bitaxe HW vendor: * dunno *
 - ESP-Miner FW version: 2.13.1 (BM1370)
 - Hash Frequency: ( doesn't matter )
 - Voltage:  ( doesn't matter )
 - Pool URL, Port, User: onprem Datum v0.4.1beta on MyNodeBTC v0.3.42

**Additional context**
I have limited access to device so as many as needed debug advices appreciated given at once.

## Comments

### mutatrum on 2026-03-13

Is there a datum gateway publicly accessible, so we can test this?

### tlindi on 2026-03-13

Unfor the one I encounted issue cant make public, but I could create clearnet one too.

How could I deliver address to it in private to you?

### mutatrum on 2026-03-13

> How could I deliver address to it in private to you?

Please join the OSMU Discord, that would make it easier.

### tlindi on 2026-03-13

Will do. At latest Next friday when I'm back at BTCHEL Community Hub...

### tlindi on 2026-03-22

Joined, posted issue and now send DM(?) for someone who said could test.

### tlindi on 2026-03-26

@mutatrum DM'ed you more info
