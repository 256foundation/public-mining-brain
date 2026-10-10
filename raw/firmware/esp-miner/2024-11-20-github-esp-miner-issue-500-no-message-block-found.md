# bitaxeorg/ESP-Miner issue #500: No Message BLOCK FOUND

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/500
> Collected: 2026-10-07
> Published: 2024-11-20

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 500
- State: closed
- Author: matlen67
- Opened: 2024-11-20
- Closed: 2024-11-20
- Labels: none

## Description

I am currently mining DeVault (DVT) via mining-dutch.nl, when a block is found there is no notification on the display, bestdiff is still displayed.
(I am currently using a LuckyMiner LV06, but I am currently switching to Bitaxe Gamma)

![DeVault_block_found_2024-11-20 040219](https://github.com/user-attachments/assets/38cef9a1-c55f-46d8-91cd-ff717b99cfee)

![DeVault_difficulty](https://github.com/user-attachments/assets/0c8dd3f8-35b0-440b-9281-16f47fbe5fd6)

![lmlv06_display](https://github.com/user-attachments/assets/62bfb900-76e0-4e5b-b804-798cb3fd0cf6)


```c++
memset(module->oled_buf, 0, 20);
snprintf(module->oled_buf, 20, module->FOUND_BLOCK ? "!!! BLOCK FOUND !!!" : "Best: %s", module->best_diff_string);
OLED_writeString(0, 2, module->oled_buf);
```




## Comments

### mutatrum on 2024-11-20

There is no guarantee that LuckyMiner uses the same codebase. I doubt that, as that screen looks different than what other BitAxes have.

### skot on 2024-11-20

I am not able to reproduce when using a legitimate Bitaxe with a legitimate cryptocurrency.

### matlen67 on 2024-11-20

Just for your information, it is the esp-miner.bin v2.4.0 on my LuckyMiner. But I can understand that you don't want to take care of other people's hardware. I'll get back to you when the Gamma is there. 

### skot on 2024-11-20

Maybe your pool/crypto is using nBits differently? Here is how esp-miner gets network difficulty; https://github.com/skot/ESP-Miner/blob/d22b95647d0f6778079219224b12ff983cecc3b9/main/system.c#L574-L584

### matlen67 on 2024-11-20

Hi skot, I'll see if I can find out anything, but I don't know much about it. In any case, I get the mined blocks credited to my wallet. My Avalon Nano 3 shows the blocks found in the log.

### skot on 2024-11-20

can you post your bitaxe log from when this happens? ideally it would contain the stratum `mining.notify` message with the work and then `mining.submit` that contains the winning share.

### matlen67 on 2024-11-20

I'll run a comport log and hope that I can find a block quickly

### matlen67 on 2024-11-21

I found a block late in the evening. I hope I found the right place in the log file as I was no longer live from the PC. Here is a match from the block explorer versionHex with the log output asic_result: Vers: 2e4f2000 and the Nonce 03900262 match too, in explorer dec 59769442

![block_1330128](https://github.com/user-attachments/assets/6a4ed6c4-e7e1-4c8f-afbb-f44a911683fd)

[https://exploredvt.com/block-height/1330128](https://exploredvt.com/block-height/1330128)

**esp-miner log:**
```
(19964347) stratum_task: rx: {"id":null,"method":"mining.notify","params":["4456542d64366435-499","a876a99cddd5a58dc1e99bf0db73647fcc8684e0b7621225000001f800000000","01000000010000000000000000000000000000000000000000000000000000000000000000ffffffff5303d04b1404f5573e6708fabe6d6d3e5569dda78ccb5fdfd18c034c31b98b8ddd521ddc04cb90806a6ea7827349b40001000000000000","f301122f4d696e696e672d44757463682f2d3332330000000001000a13b901000000232102114e157d511bb0352de6a9406024b6ae06a9a008c462024cc92297cef3f2cd03ac00000000",[],"20000000","1a050a07","673e57e3",true]}

(19964377) stratum_task: Clean Jobs: clearing queue
(19964417) create_jobs_task: New Work Dequeued 4456542d64366435-499
(19964417) create_jobs_task: Job processed and queued: 4456542d64366435-499
(19966217) bm1366Module: Job ID: 30, Core: 66/7, Ver: 1012E000
(19966217) asic_result: Ver: 3012E000 Nonce 25C30084 diff 259.4 of 749.
(19966667) bm1366Module: Job ID: 38, Core: 69/0, Ver: 02450000
(19966667) asic_result: Ver: 22450000 Nonce 0685008A diff 261.0 of 749.
(19966987) bm1366Module: Job ID: 38, Core: 103/2, Ver: 05144000
(19966987) asic_result: Ver: 25144000 Nonce BCC802CE diff 504.8 of 749.
(19969747) bm1366Module: Job ID: 40, Core: 10/4, Ver: 0BE78000
(19969747) asic_result: Ver: 2BE78000 Nonce 086D0214 diff 637.1 of 749.
(19971947) bm1366Module: Job ID: 48, Core: 56/0, Ver: 0DA30000
(19971947) asic_result: Ver: 2DA30000 Nonce BFAA0270 diff 749.3 of 749.
(19971947) stratum_api: tx: {"id": 3253, "method": "mining.submit", "params": ["matlen67.lm_03", "4456542d64366435-499", "4e480000", "673e57e3", "bfaa0270", "0da30000"]}
(19971977) stratum_task: rx: {"id":3253,"result":true,"error":null}
(19971977) stratum_task: message result accepted
(19978017) bm1366Module: Job ID: 60, Core: 49/1, Ver: 0E4F2000

(19978017) asic_result: Ver: 2E4F2000 Nonce 03900262 diff 15111668.4 of 749.
(19978027) stratum_api: tx: {"id": 3254, "method": "mining.submit", "params": ["matlen67.lm_03", "4456542d64366435-499", "51480000", "673e57e3", "03900262", "0e4f2000"]}

(19978057) stratum_task: rx: {"id":3254,"result":true,"error":null}
(19978057) stratum_task: message result accepted
```



### matlen67 on 2024-11-26

Hello skot,
my gamma has now arrived and everything is working as it should.
Thanks for your support.

```
I (34929685) asic_result: Ver: 230DC000 Nonce 6C24018E diff 6568600.1 of 1672.
I (34929685) stratum_api: tx: {"id": 5276, "method": "mining.submit", "params": ["matlen67.bg", "4456542d343838-422", "f24d0100", "674512f1", "6c24018e", "030dc000"]}
I (34929715) SystemModule: FOUND BLOCK!!!!!!!!!!!!!!!!!!!!!! 6568600.090317 > 3280194.188883
I (34929715) SystemModule: Network diff: 3280194.188883
I (34929725) stratum_task: rx: {"id":5276,"result":true,"error":null}
I (34929725) stratum_task: message result accepted
```

![block_found](https://github.com/user-attachments/assets/a543e6af-9120-4ccf-ad24-2ad5656ef1ab)
