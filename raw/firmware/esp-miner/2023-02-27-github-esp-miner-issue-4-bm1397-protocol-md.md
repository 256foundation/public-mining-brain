# bitaxeorg/ESP-Miner issue #4: bm1397_protocol.md

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/4
> Collected: 2026-10-07
> Published: 2023-02-27

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 4
- State: closed
- Author: rapsacw
- Opened: 2023-02-27
- Closed: 2023-05-24
- Labels: none

## Description

I think you 'mislogged' your data? According to the source the driver does not send anything else after the midstate(s) and checksum..

## Comments

### skot on 2023-02-27

That would be great! I have been having trouble figuring out what that last line is.

This output is from debug print statements I put in cgminer. And I have seen this a couple times now. Maybe I'm just printing over the end of the buffer?? -- I'll take a look.

### BastelPichi on 2023-03-28

> That would be great! I have been having trouble figuring out what that last line is.
> 
> This output is from debug print statements I put in cgminer. And I have seen this a couple times now. Maybe I'm just printing over the end of the buffer?? -- I'll take a look.

Have you ever tried hooking up an logic analyzer? You can get cheap 5$ ones if you search for "saleae" (fake) on ebay.
Might require level shifting tho...

### skot on 2023-03-28

Yes I have tried it. There is even a [BM1397 Saleae protocol analyzer](https://github.com/GPTechinno/bm13xx-hla). I think you'll find that cheaper logic analyzers don't have the bandwidth to keep up with full speed ASIC communication though. 

### skot on 2023-03-28

> I think you 'mislogged' your data? According to the source the driver does not send anything else after the midstate(s) and checksum..

Yes, I definitely did log the data incorrectly. I've fixed that and updated the document.

### BastelPichi on 2023-03-28

> Yes I have tried it. There is even a [BM1397 Saleae protocol analyzer](https://github.com/GPTechinno/bm13xx-hla). I think you'll find that cheaper logic analyzers don't have the bandwidth to keep up with full speed ASIC communication though.

That might be a good point. But 115200 should be ez...

### skot on 2023-03-28

> > Yes I have tried it. There is even a [BM1397 Saleae protocol analyzer](https://github.com/GPTechinno/bm13xx-hla). I think you'll find that cheaper logic analyzers don't have the bandwidth to keep up with full speed ASIC communication though.
> 
> 
> 
> That might be a good point. But 115200 should be ez...

Yes, 115200 works. Though most miner software switches to a higher baud rate pretty soon after startup.
