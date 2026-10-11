# Mastering Bitcoin (2nd ed.), Chapter 10: Mining and Consensus — mining extract

> Registry ID: bitcoinbook
> Source: https://raw.githubusercontent.com/bitcoinbook/bitcoinbook/second_edition_print3/ch10.asciidoc
> Collected: 2026-10-10
> Published: 2017 (Second Edition; tag `second_edition_print3`, ch10 "Mining and Consensus")
> Posture: extract
> As-Of: 2026-10-10

Faithful extract of the mining signal from the open-source book's mining chapter (Antonopoulos, *Mastering Bitcoin*, 2nd ed.). Wording below is quoted verbatim from ch10.asciidoc; asciidoc anchor macros and internal cross-references are stripped for readability. Full chapter (~42 KB) at the source URL.

## Purpose of mining

> The word "mining" is somewhat misleading. By evoking the extraction of precious metals, it focuses our attention on the reward for mining, the new bitcoin created in each block. Although mining is incentivized by this reward, the primary purpose of mining is not the reward or the generation of new coins. [...] Mining is the mechanism that underpins the decentralized clearinghouse, by which transactions are validated and cleared. Mining is the invention that makes bitcoin special, a decentralized security mechanism that is the basis for P2P digital cash.

> The purpose of mining is not the creation of new bitcoin. That's the incentive system. Mining is the mechanism by which bitcoin's _security_ is _decentralized_.

## Block structure — the six header fields

> To construct the block header, the mining node needs to fill in six fields.

|Size| Field | Description|
| 4 bytes | Version | A version number to track software/protocol upgrades |
| 32 bytes | Previous Block Hash | A reference to the hash of the previous (parent) block in the chain |
| 32 bytes | Merkle Root | A hash of the root of the merkle tree of this block's transactions |
| 4 bytes | Timestamp | The approximate creation time of this block (seconds from Unix Epoch) |
| 4 bytes | Target | The Proof-of-Work algorithm target for this block |
| 4 bytes | Nonce | A counter used for the Proof-of-Work algorithm |

> By selecting the specific _parent_ block, indicated by the Previous Block Hash field in the candidate block header, Jing is committing his mining power to extending the chain that ends in that specific block. In essence, this is how Jing "votes" with his mining power for the longest-difficulty valid chain.

> The coinbase transaction is listed as the first transaction in the block.

## Proof-of-Work, nonce and extraNonce

> The goal is now to find a value for the nonce that results in a block header hash that is less than the target. The mining node will need to test billions or trillions of nonce values before a nonce is found that satisfies the requirement.

> [...] the mining node running on Jing's desktop transmits the block header to his mining hardware, which starts testing trillions of nonces per second. Because the nonce is only 32 bits, after exhausting all the nonce possibilities (about 4 billion), the mining hardware changes the block header (adjusting the coinbase extra nonce space or timestamp) and resets the nonce counter, testing new combinations.

> The solution was to use the coinbase transaction as a source of extra nonce values. Because the coinbase script can store between 2 and 100 bytes of data, miners started using that space as extra nonce space [...]. The coinbase transaction is included in the merkle tree, which means that any change in the coinbase script causes the merkle root to change. Eight bytes of extra nonce, plus the 4 bytes of "standard" nonce allow miners to explore a total 2^96 (8 followed by 28 zeros) possibilities _per second_ without having to modify the timestamp.

> Currently, miners use the coinbase data to include extra nonce values and strings identifying the mining pool.

## Target and difficulty

> This notation expresses the Proof-of-Work target as a coefficient/exponent format, with the first two hexadecimal digits for the exponent and the next six hex digits as the coefficient. In this block, therefore, the exponent is +0x19+ and the coefficient is +0x03a30c+.

> target = coefficient * 2^(8*(exponent–3))

> Every 2,016 blocks, all nodes retarget the Proof-of-Work. The equation for retargeting measures the time it took to find the last 2,016 blocks and compares that to the expected time of 20,160 minutes (2,016 blocks times the desired 10-minute block interval). [...] In simple terms: If the network is finding blocks faster than every 10 minutes, the difficulty increases (target decreases). If block discovery is slower than expected, the difficulty decreases (target increases).

> New Target = Old Target * (Actual Time of Last 2016 Blocks / 20160 minutes)

## Pool-era mining

> Even the fastest consumer ASIC mining system cannot keep up with commercial systems that stack tens of thousands of these chips in giant warehouses near hydroelectric powerstations. Miners now collaborate to form mining pools, pooling their hashing power and sharing the reward among thousands of participants.

> Mining pools coordinate many hundreds or thousands of miners, over specialized pool-mining protocols. The individual miners configure their mining equipment to connect to a pool server, after creating an account with the pool.

> Pool miners connect to the pool server using a mining protocol such as Stratum (STM) or GetBlockTemplate (GBT). An older standard called GetWork (GWK) has been mostly obsolete since late 2012, because it does not easily support mining at hash rates above 4 GH/s. Both the STM and GBT protocols create block _templates_ that contain a template of a candidate block header. The pool server constructs a candidate block by aggregating transactions, adding a coinbase transaction (with extra nonce space), calculating the merkle root, and linking to the previous block hash.

> The mining pool sets a higher target (lower difficulty) for earning a share, typically more than 1,000 times easier than the bitcoin network's target.

Managed pools: a pool operator "charges pool miners a percentage fee of the earnings"; the pool server runs full node(s) so miners need not. P2Pool (2011): "a peer-to-peer mining pool without a central operator," implemented via a _share chain_ "running at a lower difficulty than the bitcoin blockchain," one share block every 30 seconds.

## Consensus changes

> While the consensus rules are invariable in the short term and must be consistent across all nodes, they are not invariable in the long term.

Hard fork: a change that makes previously invalid blocks/transactions valid, requiring all nodes to upgrade ("non-upgraded nodes... reject"). Soft fork: "a forward-compatible change to the consensus rules that allows unupgraded clients to continue to operate in consensus with the new rules"; "soft fork upgrades can only be used to constrain the consensus rules, not to expand them." Signaling via block version: BIP-34 (coinbase height in version field) and BIP-9 (version bits).

---
*Note: this is the 2nd-edition text (2017-era figures: 12.5 BTC reward, ~$1,000/BTC, "100 to 150 GB" full-node disk). The repo's develop branch now carries the 3rd edition as `ch12_mining.adoc`.*
