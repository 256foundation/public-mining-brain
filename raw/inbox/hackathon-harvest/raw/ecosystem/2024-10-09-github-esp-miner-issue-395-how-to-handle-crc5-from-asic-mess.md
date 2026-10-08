# bitaxeorg/ESP-Miner issue #395: How to handle CRC5 from asic messages

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/395
> Collected: 2026-10-07
> Published: 2024-10-09

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 395
- State: closed
- Author: adammwest
- Opened: 2024-10-09
- Closed: 2025-03-14
- Labels: bug, help wanted, accepted

## Description

Crc5 is incorrect for returning nonces, all other crc5 are correct (send commands)

according to 
https://github.com/skot/BM1397/blob/master/protocol.md
you need to crc all data in the message, excluding preamble  aa55 and the crc5 bits

in the current implemention, the crc5 bits are included, 
this can easily be corrected

by adding a bits offset to crc5 len parameter inside after the multiplication like so
https://github.com/skot/ESP-Miner/blob/master/components/asic/crc.c#L18
crc5(data,len,offset)
len *= 8
len = len + bit_offset

please note for sending data crc5(data,len,0) is required, this only applies to data from the chip

to get the correct crc5  you need to take the message remove the preamble and replace last byte with 0x80
aa 55 32 b9 bc c3 00 46 9c 
           32 b9 bc c3 00 46 80
buf = [32 b9 bc c3 00 46 80] this is what you create the CRC5 with

to match a crc5
test_val = last byte - 0x80
                         0x9c - 0x80 = 1c

crc5(buf,7,-5)  for bm1397
crc5(buf,9,-5)  for bm136X

the offset is -5 as that is the crc5 bit size

I have just checked quickly this works for 
Bm1397 not ESP miner
Bm1368 ESP miner

see https://github.com/adammwest/ESP-Miner/tree/crc_fix


proof
[0;32mI (2572655) asic_result: Ver: 25554000 Nonce DCA10210 diff 300.2 of 2048.[0m
[0;32mI (2572685) bm1368Module: crc 155 27[0m
155-27  = 128
[0;32mI (2570205) asic_result: Ver: 264B8000 Nonce 913A000E diff 423.5 of 2048.[0m
[0;32mI (2572655) bm1368Module: crc 151 23[0m
151-23 = 128
[0;32mI (2567295) asic_result: Ver: 27D68000 Nonce 10810054 diff 318.5 of 2048.[0m
[0;32mI (2567635) bm1368Module: crc 147 19[0m
147-19 = 128



## Comments

### skot on 2024-10-09

Ah very nice! I was never able to get the nonce crc5 to work (as you noticed). It does seem a little bit redundant to check the CRC as we would definitely catch any bit errors when we check the nonce difficulty...

But maybe this would save us having to do the much tougher SHA256 calc if there is a bit error..

### mutatrum on 2025-03-14

Fixed by #745
