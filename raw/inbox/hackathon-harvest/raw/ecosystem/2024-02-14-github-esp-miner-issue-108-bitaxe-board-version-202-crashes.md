# bitaxeorg/ESP-Miner issue #108: BitAxe Board Version: 202 - Crashes after approximately 24hrs: Unhandled Exception

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/108
> Collected: 2026-10-07
> Published: 2024-02-14

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 108
- State: closed
- Author: qubyt3
- Opened: 2024-02-14
- Closed: 2024-10-10
- Labels: help wanted

## Description

BitAxe will reboot after a period of approximately 24hr when Free Heap Memory reaches below +- 30000 bytes, and resumes mining automatically after reboot.

Model: BM1366 Ultra
Version: v2.0.7
Board Version: 0.11 / 202
Pool: solo.ckpool.org:3333

Log: 

I (97083047) stratum_task: rx: {"result":true,"error":null,"id":30620}
I (97083047) stratum_task: message result accepted
Guru Meditation Error: Core  0 panic'ed (StoreProhibited). Exception was unhandled.

Core  0 register dump:
PC      : 0x4005706c  PS      : 0x00060730  A0      : 0x8209966c  A1      : 0x3fcc9be0  
A2      : 0x00000000  A3      : 0x3c0b743c  A4      : 0x0000000a  A5      : 0x00000000  
A6      : 0x0000000a  A7      : 0xb33fffff  A8      : 0x00000000  A9      : 0x00000000  
A10     : 0x0000001b  A11     : 0x00000800  A12     : 0x600fe048  A13     : 0x05c96a41  
A14     : 0x3c0b7474  A15     : 0x3fcc8160  SAR     : 0x00000004  EXCCAUSE: 0x0000001d  
EXCVADDR: 0x00000000  LBEG    : 0x40054bf0  LEND    : 0x40054c0f  LCOUNT  : 0x00000000  


Backtrace: 0x40057069:0x3fcc9be0 |<-CORRUPTED




ELF file SHA256: c148b21719898fc7

Rebooting...



## Comments

### skot on 2024-02-14

what pool are you using?

### qubyt3 on 2024-02-15

Hi @skot, the pool used for this log was solo.ckpool.org. I just switched to public-pool.io to see if the issue follows, I'll update in about 24hr. 

### qubyt3 on 2024-02-16

Results for public-pool.io after approximately 24hr ran out of memory. 

Model: BM1366 Ultra
Version: v2.0.7
Board Version: 0.11 / 202
Pool: public-pool.io:21496

Log: 

Guru Meditation Error: Core  1 panic'ed (StoreProhibited). Exception was unhandled.

Core  1 register dump:
PC      : 0x4005706c  PS      : 0x00060730  A0      : 0x8209966c  A1      : 0x3fcc3160  
A2      : 0x00000000  A3      : 0x3c0c3f28  A4      : 0x0000000a  A5      : 0x00000000  
A6      : 0x0000000a  A7      : 0xb33fffff  A8      : 0x00000000  A9      : 0x00000000  
A10     : 0x0000001b  A11     : 0x00000800  A12     : 0x600fe048  A13     : 0x0435ab09  
A14     : 0x3c0c3f1c  A15     : 0x3c0c4330  SAR     : 0x00000004  EXCCAUSE: 0x0000001d  
EXCVADDR: 0x00000000  LBEG    : 0x40056f5c  LEND    : 0x40056f72  LCOUNT  : 0xffffffff  


Backtrace: 0x40057069:0x3fcc3160 |<-CORRUPTED




ELF file SHA256: c148b21719898fc7

Rebooting...

### qubyt3 on 2024-02-16

@skot I think the issue might be from keeping a AxeOS web session open for an extended period of time.

I'm wondering if there isn't an issue with how memory is allocated then freed when a socket times out, closes...etc?  

To replicated try opening a AxeOS session tab and keep it open, you should see the memory slowly drop over an hr, and it will eventually run out and reboot (24hr'ish).

Chrome, Safari, Firefox seems to all behave the same. 

if you close the tab, it doesn't seem to recover the memory either. 

  

### skot on 2024-02-16

Interesting. @benjamin-wilson think we might be leaking memory with the http_server somewhere?

### benjamin-wilson on 2024-02-16

Ack

### benjamin-wilson on 2024-02-25

> @skot I think the issue might be from keeping a AxeOS web session open for an extended period of time.
> 
> I'm wondering if there isn't an issue with how memory is allocated then freed when a socket times out, closes...etc?
> 
> To replicated try opening a AxeOS session tab and keep it open, you should see the memory slowly drop over an hr, and it will eventually run out and reboot (24hr'ish).
> 
> Chrome, Safari, Firefox seems to all behave the same.
> 
> if you close the tab, it doesn't seem to recover the memory either.

Are you simply on the web page or are you leaving logs open too

### qubyt3 on 2024-02-25

@benjamin-wilson great question. I don't recall exactly if I had the logs on or off. 

I tried quickly and I have a feeling they were on to reproduce the issue.

Give me 48hrs and I'll try both, and respond back. 

update:  log was on. 

### skot on 2024-04-05

To help isolate this, can you clarify: Does the problem happen with the dashboard open but the logs closed?

### qubyt3 on 2024-04-15

@skot sorry for the late reply; logs open only. 

### skot on 2024-10-10

We have resolved a lot of memory leaks recently. Feel free to open another issue if this happens again.
