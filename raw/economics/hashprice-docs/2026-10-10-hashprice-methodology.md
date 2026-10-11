# Hashprice — Luxor Documentation (Hashprice Index Methodology)

> Registry ID: hashprice-docs
> Source: https://docs.luxor.tech/hashrateindex/hashprice
> Collected: 2026-10-10
> Published: n/d (living docs page; changelog-adjacent entries reviewed through 2026-09-30)
> Posture: verbatim
> As-Of: 2026-10-10

> Capture note: direct `.md` route (https://docs.luxor.tech/hashrateindex/hashprice.md) returned HTTP 403
> (Cloudflare "Attention Required" block page) for plain curl. Captured verbatim instead from the
> agent-friendly corpus https://docs.luxor.tech/llms-full.txt (HTTP 200), section
> "# Hashprice (https://docs.luxor.tech/hashrateindex/hashprice)". Text below is verbatim from that corpus
> (Markdown link syntax preserved as served). Discovery route: https://docs.luxor.tech/llms.txt (HTTP 200).

---

# Hashprice [#hashprice]

## What is Hashprice? [#what-is-hashprice]

Hashprice – a term coined by Luxor in 2019 – quantifies how much a bitcoin miner can expect to earn from a specific quantity of hashrate. Hashrate is the speed at which a computer (i.e., ASIC, GPU, CPU) is completing a cryptographic computation as part of a cryptocurrency's protocol. It is measured in hashes per second.

Common units of hashrate include:

* TeraHash per second (1 TH/s = 1 trillion hashes per second)
* PetaHash per second (1 PH/s = 1,000 TH/s)
* ExaHash per second (1 EH/s = 1,000 PH/s)

Luxor's Bitcoin Hashprice Index quantifies the expected value of 1 PetaHash per second (PH/s) of hashrate per day on the Bitcoin Network. Hashprice is the true value a miner gets paid for the commodity they produce: hashrate.

Hashprice can be denominated in USD or BTC:

* BTC hashprice is a function of three inputs: block subsidy, transaction fees, and network difficulty.
* USD hashprice is a function of four inputs: block subsidy, transaction fees, network difficulty, and bitcoin price.

You can track live Hashprice [here](https://data.hashrateindex.com/network-data/btc).

## How is Hashprice calculated? [#how-is-hashprice-calculated]

Bitcoin's hashprice changes with every new block added to the blockchain (i.e., block height). Luxor's Bitcoin Hashprice Index uses a 144-block lagging simple moving average to account for transaction fees, and a simple average of the spot price for bitcoin on three US-based cryptocurrency exchanges to account for USD conversion. The BTC hashprice formula is used by a majority of mining pools to pay miners for their hashrate. USD-denominated hashprice is positively correlated with changes to Bitcoin's spot price, block subsidy and transaction fees and negatively correlated with changes to Bitcoin's network difficulty.

## Factors that impact Hashprice [#factors-that-impact-hashprice]

### Block Subsidy [#block-subsidy]

* The block subsidy is the amount of newly minted bitcoin generated in each additional block on the Bitcoin blockchain.
* The emission schedule sets out the block subsidy at each block and is determined by Bitcoin's source code.
* Bitcoin's subsidy started at 50 BTC per block and is halved every 210,000 blocks (roughly 4 years), until block 6,930,000 (projected in 2140) when the block subsidy becomes zero and mining revenue will come exclusively from transaction fees.
* The block subsidy is currently 3.125 BTC and the next "halving" is projected for April 2028.

### Transaction Fees [#transaction-fees]

* Transaction fees are the amount paid by bitcoin owners when they transfer funds to another address.
* They are collected by the miner or mining pool adding the block containing the corresponding transaction data to the Bitcoin blockchain.
* Transaction fees allow users to prioritize their transaction getting included in the Bitcoin blockchain.
* Bitcoin blocks can hold up to 1 MB of transaction data and miners have an economic incentive to include transactions with the highest associated fees.
* Transaction fees can vary depending on transaction volumes, network congestion, Bitcoin upgrades, layer 2's, and transaction batching.

### Network Difficulty [#network-difficulty]

* Network difficulty is a quantitative measure of the probability of a miner or mining pool submitting a valid hash to the Bitcoin network's cryptographic hash function (i.e., SHA-256).
* Higher network difficulty indicates a lower probability of a miner submitting a valid hash.
* Network difficulty is adjusted every 2,016 blocks (approximately every two weeks) to a level that targets an average block time of ten minutes.
* If network hashrate grows (declines) and blocks are found earlier (later) than 10 minutes on average over the previous period, the network difficulty will increase (decrease).
* Network hashrate / difficulty can vary depending on technological advancement, supply chain developments, geopolitical relations, and government regulation.

### Bitcoin Price [#bitcoin-price]

* Hashprice can be denominated in USD or BTC.
* If the block subsidy, transaction fees and network difficulty are stable, the bitcoin price is the main determinant of USD-denominated hashprice.
* The spot price of one bitcoin can vary depending on private sector adoption, speculative demand, government regulation, monetary policy, production costs, and supply issuance.
* The price of exchange-traded bitcoin futures can be evaluated for consensus views on future bitcoin prices.
