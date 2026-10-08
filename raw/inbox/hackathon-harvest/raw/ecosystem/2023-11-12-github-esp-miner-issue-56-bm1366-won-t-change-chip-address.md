# bitaxeorg/ESP-Miner issue #56: BM1366 won't change chip address

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/56
> Collected: 2026-10-07
> Published: 2023-11-12

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 56
- State: closed
- Author: rvdgracht
- Opened: 2023-11-12
- Closed: 2024-01-20
- Labels: none

## Description

Hi,

I'm using a prototype board (hobby) with a esp32c6 coupled with 4 bm1366 asics. With some tweaking in hardware and software, I've got it running. All asics are operational (only at low freq now), but I'm unable to change their chip address.

I've removed the invalidate chain command so I've modified _send_init() a bit:
```
static void _send_init(uint64_t frequency)
{
...

#if (CONFIG_ASIC_COUNT == 1)                                                    
    // Set chain inactive                                                       
    unsigned char init6[7] = {0x55, 0xAA, 0x53, 0x05, 0x00, 0x00, 0x03};        
    _send_simple(init6, 7);                                                     
#endif

    //unsigned char init7[7] = {0x55, 0xAA, 0x40, 0x05, 0x00, 0x00, 0x1C};
    //_send_simple(init7, 7);

    for (int i = (CONFIG_ASIC_COUNT - 1); i <= 0; i--) 
        _set_chip_address(i * (256 / CONFIG_ASIC_COUNT));

    _send_read_address();

    unsigned char init135[11] = {0x55, 0xAA, 0x51, 0x09, 0x00, 0x3C, 0x80, 0x00, 0x85, 0x40, 0x0C};
    _send_simple(init135, 11);
...
```
They are all working on the full (same) nonce space. I get 4 times the same nonce when one is found.
The results from the send_read_address:
->[55 AA 40 05 C0 00 0F]  <- set chip with address 0 to 0xc0
->[55 AA 40 05 80 00 0F]  <- set chip with address 0 to 0x80
->[55 AA 40 05 40 00 0F]  <- set chip with address 0 to 0x40
->[55 AA 40 05 00 00 0F]  <- set chip with address 0 to 0x00
->[55 AA 52 05 00 00 0A]  <- read all addresses
rx: [AA 55 13 66 00 00 00 00 00 00 05]
rx: [AA 55 13 66 00 00 00 00 00 00 05]
rx: [AA 55 13 66 00 00 00 00 00 00 05]
rx: [AA 55 13 66 00 00 00 00 00 00 05]

Can anyone confirm changing the address is (not yet) possible? So I can rule out a hardware issue.
Thanks!

## Comments

### johnny9 on 2023-11-12

Amazing. You might be the first to try this.

Potentially nothing is wrong here. I dont actually know if it's a range or just an offset so each chip might hit the nonce. I think trying a read register command might be the easiest way to check the address assignment is working. 

### benjamin-wilson on 2023-11-12

Also if you could report back with any findings that'd be much appreciated by the OSMU team. 

### johnny9 on 2023-11-12

[startup.txt](https://github.com/skot/ESP-Miner/files/13328490/s19xp_luxos_startup.3.txt)
take a look at this trace as a reference.

### johnny9 on 2023-11-12

I suppose if version rolling is going on the bm1366 then there can't be nonce range overlap since that would mean the chip itself isnt creating new work fast enough which seems very unlikely. If you don't feed new jobs into the asic, however, it is possible the asic overflows the version and the nonce space and you get repeat nonces.

### rvdgracht on 2023-11-12

> Amazing. You might be the first to try this.
> 
> Potentially nothing is wrong here. I dont actually know if it's a range or just an offset so each chip might hit the nonce. I think trying a read register command might be the easiest way to check the address assignment is working.

I think the chip address is also used as the MSB for that chips starting nonce. So If you have 2 chips, you should give them address 0x00 and 0x80. This way your chain chews through the whole nonce range for a job twice as fast.

### rvdgracht on 2023-11-12

> [startup.txt](https://github.com/skot/ESP-Miner/files/13328490/s19xp_luxos_startup.3.txt) take a look at this trace as a reference.

This is helpfull! I'll look into this and keep you posted.

### rvdgracht on 2023-11-12

> I suppose if version rolling is going on the bm1366 then there can't be nonce range overlap since that would mean the chip itself isnt creating new work fast enough which seems very unlikely. If you don't feed new jobs into the asic, however, it is possible the asic overflows the version and the nonce space and you get repeat nonces.

I get them with miliseconds apart. I haven't adjusted the job feed rate in ESP miner. And I get exactly 4 no more no less.

Edit: milliseconds judging by the timestamp from a debug print in the uart ring buffer reading function, so its probably less.

### adammwest on 2023-12-08

This is cool, 

Going to the docs - https://github.com/skot/BM1397/blob/master/protocol.md which should be vaguely related to the BM1366
"To set Chip Address of all chips one by one, we must not send commands to ALL chips, just to the chip with Address = 0, so the first chip on the chain will get the command and not propagate it downward"

The "propagate it downward" leads me to think the chips need to be connected together in a daisy chained fashion via specific HW like the hash boards.

Are the Asics all independently connected to the ESP? and do you give the same job to all devices?

### rvdgracht on 2023-12-11

Hi Adammwest,

The chips are chained. I have 4 chips in 4 power domains. This is to keep the losses in the main power supply low.
I had some hardware issues, which prevented me from testing any further. I have made changes to my hardware, and
hope to resume testing soon.


### rvdgracht on 2024-01-20

Turned out to be a hardware issue. It's fixed now. Thank you for your help and sorry for the noise.
