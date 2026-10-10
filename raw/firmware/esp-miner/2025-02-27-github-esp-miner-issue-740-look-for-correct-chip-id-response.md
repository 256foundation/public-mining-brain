# bitaxeorg/ESP-Miner issue #740: look for correct CHIP_ID responses only

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/740
> Collected: 2026-10-07
> Published: 2025-02-27

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 740
- State: closed
- Author: skot
- Opened: 2025-02-27
- Closed: 2025-03-12
- Labels: enhancement, help wanted, good first issue

## Description

in the ASIC `_send_init()` in [bm1366.c](https://github.com/skot/ESP-Miner/blob/master/components/asic/bm1366.c) we read the [CHIP_ID](https://github.com/skot/BM1397/blob/master/bm1366_registers.md) register and count how many responses we get:

```C
    // read register 00 on all chips
    unsigned char init3[7] = {0x55, 0xAA, 0x52, 0x05, 0x00, 0x00, 0x0A};
    _send_simple(init3, 7);

    int chip_counter = 0;
    while (true) {
        if(SERIAL_rx(asic_response_buffer, 11, 1000) > 0) {
            chip_counter++;
        } else {
            break;
        }
    }
```

The problem is that this will accept any random 11 bytes as a correct response. We should only accept the specific bytes from a correct response, and throw an error otherwise.

correct BM1366 response: `AA 55 13 66 00 00 00 00 00 00 05`
correct BM1368 response: `AA 55 13 68 00 00 00 00 00 00 0F`
correct BM1370 response: `AA 55 13 70 00 00 00 00 00 00 10`
etc..


## Comments

### mutatrum on 2025-03-02

What's the final byte in the response, a checksum?

### skot on 2025-03-02

> What's the final byte in the response, a checksum?

Yes, but it's a different format than the others. I was never able to get it to work. I heard a rumor @Georges760 has gotten it though.

### Georges760 on 2025-03-03

Basically, because the CRC5 is 5 bits only, th 3bits left to padd to a byte need to be taken into account.

When you want to check if he CRC5 over a buffer is OK, just run the normal (byte-aligned) CRC5 algo over the full buffer (byte aligned: (N+1)*8, so containing the CRC5 itself at the end), and you should have 0x00.

When you want to compute the CRC5 over a buffer (bit aligned: N*8+3 bits len), you need a bit-aligned algo. Here is [my impl in Rust](https://github.com/GPTechinno/bm13xx-rs/blob/main/bm13xx-protocol/src/crc.rs#L29)


### adammwest on 2025-03-05

Im not 100% but I remember chains of chips have a different pattern 
when i was doing tests on a gekko A1 with bm1362  with 2 chips it gave me 00 and 80 responses before I enumerated it
AA 55 13 62 XX 00 00 00 00 00 CRC

like
AA 55 13 62 00 00 00 00 00 00 CRC
AA 55 13 62 80 00 00 00 00 00 CRC



### Georges760 on 2025-03-05

this byte should be constant for ever ASIC of the same family : [CORE_NUM](https://github.com/skot/BM1397/blob/master/registers.md#core_num)

But the one just after is [ADDR](https://github.com/skot/BM1397/blob/master/registers.md#core_num) and is 0 just after reset, but the SW can (and should) affect new address to every single chips in the chain. So if you enumerate them after the address allocations, you will see different values.

### skot on 2025-03-05

I have been playing with BM1362 a lot lately and have only seen CORE_NUM = 0x08. So far I've never seen anything besides 0x00 on BM1366, 1368 and 1370.

For this issue we only need to make sure we get the correct CHIP_ID and the correct number of them. If we can check the checksum too, thats nice to have. (it looks like this is what #745 has, thanks @mutatrum !)
