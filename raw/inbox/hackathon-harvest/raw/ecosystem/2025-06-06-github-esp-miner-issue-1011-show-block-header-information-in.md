# bitaxeorg/ESP-Miner issue #1011: Show block header information in Axe-OS

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1011
> Collected: 2026-10-07
> Published: 2025-06-06

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1011
- State: closed
- Author: mutatrum
- Opened: 2025-06-06
- Closed: 2025-09-13
- Labels: none

## Description

Seeing https://x.com/boerst/status/1930754454451847375, it would make a lot of sense to show block header information on Axe-OS somewhere. Maybe a full clone of [stratum.work](stratum.work) is overkill, but at least show the miner tag (not sure what it's called) and possibly the merkle tree buildup would be interesting and educational.

## Comments

### mutatrum on 2025-07-03

Available information from `mining.notify`, from https://en.bitcoin.it/wiki/Stratum_mining_protocol:

> 1. Job ID. This is included when miners submit a results so work can be matched with proper transactions.
> 2. Hash of previous block. Used to build the header.
> 3. Generation transaction (part 1). The miner inserts ExtraNonce1 and ExtraNonce2 after this section of the transaction data.
> 4. Generation transaction (part 2). The miner appends this after the first part of the transaction data and the two ExtraNonce values.
> 5. List of merkle branches. The generation transaction is hashed against the merkle branches to build the final merkle root.
> 6. Bitcoin block version. Used in the block header.
> 7. nBits. The encoded network difficulty. Used in the block header.
> 8. nTime. The current time. nTime rolling should be supported, but should not increase faster than actual time.
> 9. Clean Jobs. If true, miners should abort their current work and immediately use the new job, even if it degrades hashrate in the short term. If false, they can still use the current job, but should move to the new one as soon as possible without impacting hashrate.
> 

Example:
```
{
   "params":[
      "684934fc000105be",
      "1a2b71b6673cf631e8cac92e242f374bdebc5c450001b10a0000000000000000",
      "01000000010000000000000000000000000000000000000000000000000000000000000000ffffffff370392ca0d0004b27c666804e66ff2190c",
      "0a636b706f6f6c1365752f736f6c6f2e636b706f6f6c2e6f72672fffffffff037a7c93120000000016001480bded37e3f86a1a546e099b15e2b02855d3843cfd0c61000000000016001451ed61d2f6aa260cc72cdf743e4e436a82c010270000000000000000266a24aa21a9ed2aaf372eab3aa252e8b72245d385e68a932bf06cf5c06ed51d013f6599d62d5b00000000",
      [
         "beae4aac6e4aeb10ca32e8f11fbc1a25a4302fe64a116a1191e1619e9212c1de",
         "8c585fbbdaf8d12c1db2559e31b5293cdd59bd10ff59204f184a9573629c460c",
         "34d87c63feec6fd781cba0f07b3a95dcea1dee44abb94429f7eaebf0ce7303a4",
         "657d00061258bbc58126457101c0be7845aa8595e54c079077cac86581863ca3",
         "8767b8b166ee4f897d1a995717061999073890e356e9a43dcab566d256998a44",
         "192ee34125f4cb8c0fcc31af96616504ce18e7bcf271e8d6bb1345029f10f353",
         "8995124df15b4b14b101716c6b30e9fa9911026cfa0a310daa94eebe08c4776d",
         "518640872502650b8e8332cb93b4c0e380ab63ac02e84b9c4f41a9a6f75d5d0a",
         "9939e54a1d6e5679f94ec4ed028cd7d3b4e905132adf92a22727f0b8767a0580",
         "1da2cb27cb378d70f6c5a6499a635e23b44014e229f4341b99028eb6a80583f3",
         "089e66f80e63c530607e55a266568864e36b9dd1f6abb2d12ba946953d5d8bbe",
         "e892068831e4a605a7535e56c18a8a15e5925aff023e2fc956396d89bd3f4d7f",
         "6b03fefe6749a362f9b807adae150e86181eb88345d8f69678077497016a7521"
      ],
      "20000000",
      "17026816",
      "68667cb2",
      false
   ],
   "id":null,
   "method":"mining.notify"
}
```

1: Show as hex, can be used to correlate information from `mining.submits`;
2: Show as hex
3: Show as hex
Insert current `extranonce` and `extranonce_2` values;
4: Contains the coinbase transaction, so that has the miner tag. In this case: `ckpooleu/solo.ckpool.org/`;
5: List of transactions to make up the merkle tree. Can be used in the same way as stratum.work;
6: Could be shown, not 100% sure. Can't remember which flags are currently in use;
7: Show as current network difficulty
8: Show as UTC
9: Ignore?

One part of the screen could show all the current information.

The second part of the screen could be used to keep a running table of recent mining.notify messages, and add a few columns of the submits that are correlated to each job, f.e. showing the best achieved difficulty of each job, and maybe number of shares or so.

### mutatrum on 2025-07-03

Some more inspiration: https://hodl.camp/genesis_block

### skot on 2025-07-06

Ooo I really like this idea! Showing live info about the candidate block being mined would be awesome for learning about mining and something that no other miner does.

### bboerst on 2025-07-14

If you decode the coinbase tx from these `mining.notify` messages, you can get a bunch of interesting data, including the `height`. [BIP34](https://en.bitcoin.it/wiki/BIP_0034) requires that the `height` be included within the coinbase tx; so that's in there if you want to dig for it.

To decode the raw coinbase tx from the `mining.notify` message, it's:
```
coinbase1 + extranonce1 + "00".repeat(extranonce2_length) + coinbase2
```

...so in the case of the `mining.notify` example in the description above:

- `coinbase1` = `01000000010000000000000000000000000000000000000000000000000000000000000000ffffffff370392ca0d0004b27c666804e66ff2190c`
- `coinbase2` = `0a636b706f6f6c1365752f736f6c6f2e636b706f6f6c2e6f72672fffffffff037a7c93120000000016001480bded37e3f86a1a546e099b15e2b02855d3843cfd0c61000000000016001451ed61d2f6aa260cc72cdf743e4e436a82c010270000000000000000266a24aa21a9ed2aaf372eab3aa252e8b72245d385e68a932bf06cf5c06ed51d013f6599d62d5b00000000`
- `extranonce1` (the pool gives you this during `mining.subscribe`, but only the length matters) = `00000000`
- `extranonce2_length` (the pool gives you this during `mining.subscribe`) = `8` (this is the byte length, so `8` bytes is `0000000000000000`)

Concat these ^ and you get the raw coinbase tx:
```
01000000010000000000000000000000000000000000000000000000000000000000000000ffffffff370392ca0d0004b27c666804e66ff2190c0000000000000000000000000a636b706f6f6c1365752f736f6c6f2e636b706f6f6c2e6f72672fffffffff037a7c93120000000016001480bded37e3f86a1a546e099b15e2b02855d3843cfd0c61000000000016001451ed61d2f6aa260cc72cdf743e4e436a82c010270000000000000000266a24aa21a9ed2aaf372eab3aa252e8b72245d385e68a932bf06cf5c06ed51d013f6599d62d5b00000000
```

Decode that as you would normally decode a Bitcoin tx ([online decoder](https://www.blockchain.com/explorer/assets/btc/decode-transaction)) to get the script sig (tx input script). In this case the script sig is:
```
0392ca0d0004b27c666804e66ff2190c0000000000000000000000000a636b706f6f6c1365752f736f6c6f2e636b706f6f6c2e6f72672f
```
The height is at the front of this script:

The first byte (0x03) is a push opcode: push next 3 bytes

Next 3 bytes (0x92ca0d) is the height in little-endian

```
0x92 = 146
0xca = 202
0x0d = 13
```
Converting from little-endian: 146 + (202 × 256) + (13 × 256²) = 903826 <- the height

There's other stuff in this script sig too, like the ASCII script tag:
```
eu/solo.ckpool.org/
```
which would probably also be good to display in the firmware.

I think that showing all of this data would be great because it brings transparency and as skot mentioned, it would be an awesome real-time learning tool that no other mining hardware is doing.

### mutatrum on 2025-08-20

```
I (15601) stratum_task: Block height 910918
```
Now the question is: where to put it?

Also:
```
I (4255390) stratum_task: Miner tag: ckpooleu/solo.ckpool.org/
```

### skot on 2025-08-20

I think it should be on the main AxeOS tab.. maybe a new block header info card?

### mutatrum on 2025-08-20

Can start there. I would like to extend it to its own tab, with history of jobs and best diffs per job, and a proper header breakdown. IMO that's a good education tool.

### mutatrum on 2025-08-20

A new card is quite involved, as it will be a whole new line of cards.

This maybe?

<img width="677" height="317" alt="Image" src="https://github.com/user-attachments/assets/cfb83cb6-86b7-410b-9299-354f5648d0e0" />

Hailing @duckaxe as the UI master. Next to block height, there's miner tag, and it could also do payout addres(ses) with amounts and network difficulty.
