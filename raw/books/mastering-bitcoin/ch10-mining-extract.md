# Mastering Bitcoin (2nd Ed) — ch. 10: Mining and Consensus (extract)

> Source: https://github.com/bitcoinbook/bitcoinbook/blob/develop/ch10.md (open source, CC BY-SA 4.0)
> Collected: 2026-10-10
> Published: 2017 (2nd ed.)
> Registry ID: bitcoinbook
> Posture: extract (key mechanics with section attribution; full text at source)

> Source note (2026-10-10): the `develop` branch has moved to the 3rd edition (AsciiDoc; mining content now in `ch12_mining.adoc`) and no `ch10.md` exists there. This extract was taken from the 2nd-edition source file `ch10.asciidoc` at repo tag `second_edition_print3`: https://github.com/bitcoinbook/bitcoinbook/blob/second_edition_print3/ch10.asciidoc (same CC BY-SA 4.0 license). Section numbers below follow the chapter's heading order.

## Key mechanics (by section)

### 10.1 Introduction
- "Mining is the mechanism that underpins the decentralized clearinghouse, by which transactions are validated and cleared." Mining "secures the Bitcoin system and enables the emergence of network-wide consensus without a central authority."
- "Bitcoin's blocks are generated every 10 minutes, on average. This is bitcoin's heartbeat and underpins the frequency of currency issuance and the speed of transaction settlement."

### 10.1.1 Bitcoin Economics and Currency Creation
- "Each block, generated on average every 10 minutes, contains entirely new bitcoin, created from nothing. Every 210,000 blocks, or approximately every four years, the currency issuance rate is decreased by 50%. For the first four years of operation of the network, each block contained 50 new bitcoin."
- "In November 2012, the new bitcoin issuance rate was decreased to 25 bitcoin per block. In July of 2016 it was decreased again to 12.5 bitcoin per block. It will halve again to 6.25 bitcoin at block 630,000."
- "The rate of new coins decreases like this exponentially over 32 'halvings' until block 6,720,000 (mined approximately in year 2137), when it reaches the minimum currency unit of 1 satoshi. Finally, after 6.93 million blocks, in approximately 2140, almost 2,099,999,997,690,000 satoshis, or almost 21 million bitcoin, will be issued."
- Script output: "Total BTC to ever be created: 2099999997690000 Satoshis". A miner may intentionally mine a block taking less than the full reward, "resulting in a lower total issuance of the currency."

### 10.2 Decentralized Consensus
- "Satoshi Nakamoto's main invention is the decentralized mechanism for emergent consensus... consensus is an emergent artifact of the asynchronous interaction of thousands of independent nodes, all following simple rules."
- Decentralized consensus emerges from four independent processes: (1) independent verification of each transaction by every full node, (2) independent aggregation of transactions into new blocks by mining nodes with Proof-of-Work, (3) independent verification of new blocks and assembly into a chain, (4) independent selection of the chain with the most cumulative Proof-of-Work.

### 10.3 Independent Verification of Transactions
- Every node verifies each transaction against a long checklist before relaying (functions `AcceptToMemoryPool`, `CheckTransaction`, `CheckInputs` in Bitcoin Core); valid unconfirmed transactions accumulate in the "transaction pool, memory pool, or mempool."
- Checklist literals include: transaction size less than `MAX_BLOCK_SIZE`; output values "less than 21m coins, more than the dust threshold"; "For each input, if the referenced output transaction is a coinbase output, it must have at least `COINBASE_MATURITY` (100) confirmations."

### 10.4 Mining Nodes
- Some nodes are specialized "miners": e.g., Jing's mining hardware "is connected to a server running a full bitcoin node," but "some miners mine without a full node, as we will see in Mining Pools."
- Receiving a valid new block means the current competition is lost and the next begins: "it is also the starting pistol in the race for the next block."

### 10.5 Aggregating Transactions into Blocks
- Validated transactions wait in the memory pool; the miner aggregates them into a "candidate block," which "becomes valid only if the miner succeeds in finding a solution to the Proof-of-Work algorithm."
- Worked example: block 277,316 — candidate block has "418 transactions with total transaction fees of 0.09094928 bitcoin"; block difficulty 1180923195.25802612, bits `0x1903a30c`, nonce 924591752.

### 10.5.1–10.5.2 The Coinbase Transaction; Coinbase Reward and Fees
- "The first transaction in any block is a special transaction, called a coinbase transaction," which "does not consume (spend) UTXO as inputs" — it "creates bitcoin from nothing" and pays the miner's own address (block 277,316 paid 25.09094928 BTC to `1MxTkeEP2PmHSMze5tUZ1hAV3YTKu2Gh1N`).
- "Total Fees = Sum(Inputs) - Sum(Outputs)".
- "The reward is calculated based on the block height, starting at 50 bitcoin per block and reduced by half every 210,000 blocks. Because this block is at height 277,316, the correct reward is 25 bitcoin." (Implemented in `GetBlockSubsidy`: `int halvings = nHeight / consensusParams.nSubsidyHalvingInterval;`)

### 10.5.3–10.5.4 Structure of the Coinbase Transaction; Coinbase Data
- Coinbase input: "Transaction Hash — All bits are zero: Not a transaction hash reference"; "Output Index — All bits are ones: 0xFFFFFFFF"; Coinbase Data Size "from 2 to 100 bytes"; Sequence "Set to 0xFFFFFFFF".
- "Coinbase data, which must be between 2 and 100 bytes... can be used by miners in any way they want; it is arbitrary data." As per BIP-34, "version-2 blocks... must contain the block height index as a script 'push' operation in the beginning of the coinbase field."
- Block 277,316 coinbase `03443b0403858402062f503253482f` decodes as: push-3 + little-endian height `0x443b04` → 277,316; extra nonce bytes `0385840206`; and `/P2SH/` (`2f503253482f`) signaling BIP-16 support. Genesis block coinbase carried "The Times 03/Jan/2009 Chancellor on brink of second bailout for banks".

### 10.6 Constructing the Block Header
- The mining node fills six fields: Version (4 bytes), Previous Block Hash (32 bytes), Merkle Root (32 bytes), Timestamp (4 bytes, "seconds from Unix Epoch"), Target (4 bytes, "The Proof-of-Work algorithm target for this block"), Nonce (4 bytes, "A counter used for the Proof-of-Work algorithm").
- By selecting the parent via Previous Block Hash, the miner is "committing his mining power to extending the chain that ends in that specific block... this is how Jing 'votes' with his mining power for the longest-difficulty valid chain."
- Target is stored as "target bits": "a mantissa-exponent encoding of the target. The encoding has a 1-byte exponent, followed by a 3-byte mantissa (coefficient)" — e.g., `0x1903a30c` = exponent `0x19` + coefficient `0x03a30c`.

### 10.7 Mining the Block / 10.7.1 Proof-of-Work Algorithm
- "Mining is the process of hashing the block header repeatedly, changing one parameter, until the resulting hash matches a specific target." SHA256 output is always 256 bits; the PoW "must produce a hash that is less than the target... The target and difficulty are inversely related."
- "At the current difficulty in the bitcoin network, miners have to try quadrillions of times before finding a nonce that results in a low enough block header hash."
- 32-bit nonce exhaustion: "after exhausting all the nonce possibilities (about 4 billion), the mining hardware changes the block header (adjusting the coinbase extra nonce space or timestamp) and resets the nonce counter."

### 10.7.2 Target Representation
- Block 277,316's target `0x0000000000000003A30C00...00` requires "more than 60 leading bits set to zero."
- "a single miner processing 1 trillion hashes per second (1 terahash per second or 1 TH/sec) would only find a solution once every 8,496 blocks or once every 59 days, on average."

### 10.7.3 Retargeting to Adjust Difficulty
- "Every 2,016 blocks, all nodes retarget the Proof-of-Work. The equation for retargeting measures the time it took to find the last 2,016 blocks and compares that to the expected time of 20,160 minutes (2,016 blocks times the desired 10-minute block interval)."
- Retarget formula: `New Target = Old Target * (Actual Time of Last 2016 Blocks / 20160 minutes)`. Parameters in chainparams.cpp: "Interval (2,016 blocks) and TargetTimespan (two weeks as 1,209,600 seconds)".
- Adjustment is clamped: "the retargeting adjustment must be less than a factor of four (4) per cycle"; large imbalances "might take several 2,016 block cycles to balance out."
- Off-by-one: retargeting "is based on the total time of the previous 2,015 blocks (not 2,016 as it should be), resulting in a retargeting bias toward higher difficulty by 0.05%."

### 10.8 Successfully Mining the Block
- "Almost 11 minutes after starting to mine block 277,316," nonce 924,591,752 yields hash `0000000000000001b6b9a13b095e96db41c4a928b97ef2d944a9b31b2cc7bdc4`, less than the target.
- Peers validate and propagate; "By building on top of Jing's newly discovered block, the other miners are essentially 'voting' with their mining power and endorsing Jing's block."

### 10.9 Validating a New Block
- Block validation checklist (Bitcoin Core `CheckBlock` / `CheckBlockHeader`) includes: "The block header hash is less than the target (enforces the Proof-of-Work)"; "The block timestamp is less than two hours in the future (allowing for time errors)"; "The first transaction (and only the first) is a coinbase transaction".
- "Why don't miners write themselves a transaction for a thousand bitcoin instead of the correct reward? Because every node validates blocks according to the same rules" — cheating miners lose reward and waste electricity.

### 10.10 Assembling and Selecting Chains of Blocks / 10.10.1 Blockchain Forks
- "The 'main chain' at any time is whichever valid chain of blocks has the most cumulative Proof-of-Work associated with it" — also called "the longest chain or greatest cumulative work chain." Nodes keep secondary chains and an orphan block pool (child-before-parent arrivals).
- Natural forks occur "whenever two miners solve the Proof-of-Work algorithm within a short period of time"; both sides are valid perspectives and "Only in hindsight will one prevail"; forks are "resolved by eventual reconvergence as more blocks are added to one of the forks."

### 10.11 Mining and the Hashing Race
- Network hash rate growth, first eight years: 2009 0.5 MH/sec–8 MH/sec (16× growth); 2010 8 MH/sec–116 GH/sec (14,500×); 2011 116 GH/sec–9 TH/sec (78×); 2012 9 TH/sec–23 TH/sec (2.5×); 2013 23 TH/sec–10 PH/sec (450×); 2014 10 PH/sec–300 PH/sec (30×); 2015 300 PH/sec–800 PH/sec (2.66×); 2016 800 PH/sec–2.5 EH/sec (3.12×).
- "In 2013 the introduction of ASIC mining lead to another giant leap in mining power, by placing the SHA256 function directly on silicon chips"; chips approached "a feature size (resolution) of 16 nanometers (nm)" aiming at 14 nm; "the industry has reached the forefront of Moore's Law, which stipulates that computing density will double approximately every 18 months."

### 10.11.1 The Extra Nonce Solution
- "As difficulty increased, miners often cycled through all 4 billion values of the nonce without finding a block"; once hardware exceeded 4 GH/sec (and later TH/sec), "The solution was to use the coinbase transaction as a source of extra nonce values" (coinbase script can store 2–100 bytes).
- "Eight bytes of extra nonce, plus the 4 bytes of 'standard' nonce allow miners to explore a total 2^96 (8 followed by 28 zeros) possibilities per second without having to modify the timestamp."

### 10.11.2 Mining Pools (incl. managed pools, P2Pool)
- Pool share accounting: miners earn "shares" for work against a pool target "typically more than 1,000 times easier than the bitcoin network's target"; "When someone in the pool successfully mines a block, the reward is earned by the pool and then shared with all miners in proportion to the number of shares they contributed." Dice analogy: network target "less than four," pool share target "less than eight."
- Solo-mining example (2017): 14 TH/s hardware, "approximately $2,500 USD," 1375 watts, "33 kW-hours a day, at a cost of $1 to $2 per day"; solo-mines a block "approximately once every 4 years" — P = (14×10^12 / 3×10^18) × 210240 = 0.98 (98% probability over four years; 210,240 blocks in four years at 3 EH/sec network). Pool participation instead yields "approximately $50 to $60 per week."
- Managed pools: "The owner of the pool server is called the pool operator, and he charges pool miners a percentage fee"; pool server runs a full node (miners avoid "at least 100 to 150 GB of persistent storage (disk) and at least 2 to 4 GB of memory (RAM)"); mining protocols: "Stratum (STM) or GetBlockTemplate (GBT)"; "An older standard called GetWork (GWK) has been mostly obsolete since late 2012, because it does not easily support mining at hash rates above 4 GH/s."
- P2Pool (proposed 2011): "a peer-to-peer mining pool without a central operator" using a "share chain... mining shares on the share chain at a rate of one share block every 30 seconds"; "conceivably vulnerable to 51% attacks against the share chain itself."

### 10.12 Consensus Attacks
- "Consensus attacks can only affect future consensus, or at best, the most recent past (tens of blocks)... A consensus attack cannot steal bitcoin, spend bitcoin without signatures, redirect bitcoin, or otherwise change past transactions or ownership records."
- 51% attack: majority-hash miners "can cause deliberate 'forks' in the blockchain and double-spend transactions or execute denial-of-service attacks against specific transactions or addresses"; "an attacker can invalidate six or more blocks in a row, causing transactions that were considered immutable (six confirmations) to be invalidated"; a double-spend "can only be done on the attacker's own transactions."
- Defense: "a merchant selling large-value items must wait at least six confirmations"; waiting 24 hours "would correspond to approximately 144 confirmations." The name overstates the bar: "such an attack can be attempted with a smaller percentage... with as little as 30% of the hashing power" (statistical modeling).
- Pool-operator risk: "The pool operator in a managed pool controls the construction of candidate blocks and also controls which transactions are included," enabling subtle for-profit attacks; a sustained denial-of-service can target specific addresses while the majority of mining power is controlled.

### 10.13 Changing the Consensus Rules (hard forks, soft forks)
- Hard fork: "after the fork the network does not reconverge onto a single chain. Instead, the two chains evolve independently"; hard forks develop in four stages — "a software fork, a network fork, a mining fork, and a chain fork."
- Diverging-miners difficulty math: after an 80%–20% split, the majority chain sees blocks "on average every 12.5 minutes," retargeting after "approximately 25,200 minutes... or 17.5 days"; the minority chain mines "every 50 minutes on average," waiting "approximately 10 weeks" for retarget — reducing transaction capacity "by a factor of 5."
- Soft fork: "a forward-compatible change to the consensus rules that allows unupgraded clients to continue to operate in consensus with the new rules"; "soft fork upgrades can only be used to constrain the consensus rules, not to expand them." Mechanisms include reinterpreting NOP1–NOP10 opcodes (e.g., BIP-65 `CHECKLOCKTIMEVERIFY` reinterpreted NOP2) and segwit.
- Criticisms of soft forks: technical debt, "validation relaxation" (unmodified clients are "blind to the new rules"), and "irreversible upgrades" (reversing a soft fork "could result in a loss of funds under the old rules").

### 10.13.1–10.13.2 Soft Fork Signaling: BIP-34 and BIP-9
- BIP-34 (activated March 2013; required block height in coinbase, block version ≥ 2) used a "rolling window of 1000 blocks": "If 75% (750 of the most recent 1000 blocks) are marked with version '2'... version '1' blocks are still accepted"; "When 95% (950 of the most recent 1000 blocks) are version '2,' version '1' blocks are no longer considered valid." BIP-66 (Strict DER, version "3") and BIP-65 (CHECKLOCKTIMEVERIFY, version "4") activated the same way.
- BIP-9 (activated July 2016) "interprets the block version as a bit field instead of an integer" — 29 signal bits; proposals carry name, bit (0–28), starttime, endtime (Median Time Past); TIMEOUT expiry rejects the proposal.
- "BIP-9 counts activation signaling in whole intervals based on the difficulty retarget period of 2016 blocks. For every retarget period, if the sum of blocks signaling for a proposal exceeds 95% (1916 of 2016), the proposal will be activated one retarget period later." State machine: DEFINED → STARTED → LOCKED_IN → ACTIVE, or FAILED. First used for CHECKSEQUENCEVERIFY (BIPs 68, 112, 113), "activated successfully in July of 2016."

### 10.14 Consensus Software Development
- "while miners can theoretically change the rules by simple majority (51%), they are constrained by the consent of the other constituencies... the rest of the participants may simply refuse to follow them, keeping the economic activity on a minority chain."
- "The 95% threshold for soft forks is reflective of this reality"; "change is difficult and consensus forces compromise."
