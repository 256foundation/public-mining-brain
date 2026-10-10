# bitaxeorg/ESP-Miner issue #1166: add BIP-34 block height parsing to esp-miner and display on AxeOS

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1166
> Collected: 2026-10-07
> Published: 2025-07-25

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1166
- State: closed
- Author: skot
- Opened: 2025-07-25
- Closed: 2025-09-13
- Labels: enhancement, help wanted, good first issue, design

## Description

[BIP-34](https://github.com/bitcoin/bips/blob/master/bip-0034.mediawiki) has been activated for over a decade, so it's probably safe to say it's supported by all pools/stratum servers.

Part of this change adds the current Bitcoin block height into the coinbase transaction of blocks. Mining pools will send this as a part of block template in the `mining.notify` stratum message. We should be able to parse this out and keep track of the current block height for display on the AxeOS dashboard.

Of course we'll need proper error handling in for the inevitable situation that a stratum server doesn't send it  😅


## Comments

### adammwest on 2025-07-30

Here are the steps to convert sigscript into the height

e.g for block [907826](https://mempool.space/tx/af7f82aa77dd25d33899d94800ed052ac4667156b05687b3555c6b1e6a595703)


the sigscript of transcaction 0 is 
```
0332da0d0493348a682f466f756e6472792055534120506f6f6c202364726f70676f6c642ffabe6d6db0c6491b73cbf859808ca18d196f4a0bf7c514dbf0c7b30b9e6f1f1864dcd200010000000000000042cc8d8a0ea4000000000000
```
sigscript is encoded like [size][data],...
decomposing the first data
```
03 size in bytes
32da0d 3 bytes of data
```

finally byte reversing the first data 
```
32da0d
0dda32
````

we arrive at the encoded block height
```
0x0dda32 = 907826
```





### mutatrum on 2025-08-19

Duplicate of #1011.
