# Bitcoin Mining Economics — ch. 135–146: Transaction Fees & Halving Cycles (2 chapters, extract)

> Source: https://braiins.com/books/bitcoin-mining-economics (PDF: https://cdn.prod.website-files.com/5e5fcd39a7ed2643c8f70a6a/64bf960e8f1e7d89f67dbdb3_Mining%20eco_PDF%20sazba.pdf) (Braiins Publishing, free PDF)
> Collected: 2026-10-10
> Published: 2023
> Registry ID: braiins-books
> Posture: extract (key information with chapter attribution; full text at source PDF)

## Key points (ch. 135–136 — Transaction Fees and Halving Cycles, section intro)

- "Every 4 years, new BTC issuance earned by miners gets cut in half. Historically... the block subsidy portion of the block reward—has accounted for the vast majority of total mining revenue, while transaction fees make up the rest." (p. 135)
- The block subsidy "ultimately hits zero by the year 2140"; "there is no identifiable 'correct' value in BTC or fiat terms for the block subsidy to be sufficient to ensure bitcoin's decentralization and resistance to attacks" — total revenue (the "security budget") "doesn't necessarily tell us how distributed hashrate is geographically and politically". (p. 135)

## Key points (ch. 137–146 — Transaction Fee "Luck" for Bitcoin Miners)

- Bear-market fee share: "the average transaction fee amount per block over the past couple of years is 0.095 BTC—a mere 1.5% of the total block reward" (excluding "the ordinal-fueled fee boom of Q2 2023"). (p. 137)
- Block luck baseline: a pool with "a static 10% market share of the total network hashrate... [is] expected to find 1 of every 10 blocks, or 1 block per 100 minutes given a 10-minute average block time"; over "long time periods (months to years), luck balances out towards 100%." (p. 138)
- FPPS risk transfer: FPPS "pays miners according to the expected value of their hashrate, regardless of the actual blocks mined by the pool. In this system, the pools are taking on all the short-term variance risk, which requires deep BTC reserves to remain solvent through bad luck periods." (p. 138)
- Fee luck definition: "finding a block very quickly after the previous block was found is 'unlucky' because it will result in relatively lower fees... finding a block after a long network-wide block finding drought is 'lucky' because it gives the mempool time to fill up with higher-fee transactions." (p. 139)
- Sample window (Blocks #764132–#764145): "The average block value in this stretch is 6.44 BTC, or approximately 0.19 BTC average transaction fees per block"; average 1-block duration "10:11". (p. 139)
- Luck correlation confirmed: "By far the most valuable block in the batch, #764136, had an extremely long 1-block duration at 59:19 and racked up ~0.456 BTC of fees—over double the average. Even though it was followed by a block just 4:33 later, there were enough high-fee transactions leftover... ~0.297 BTC of fees", the 2nd highest value. (p. 140)
- Fast blocks are poor: "5 blocks were found within 3 minutes of the previous block, and these 5 blocks rank as the 1st, 2nd, 3rd, 4th, and 6th least valuable in the batch." (p. 140)
- Timestamp nuance: "the timestamp does not need to be exact, and modern-day miners actually alter it in 1 second increments on purpose to expand their search space in a process known as nTime rolling... (nonce range * ntime range)" — the source of a "-3 second" block duration. (p. 140)
- Far-future framing (2034): "the block subsidy has halved 3 more times and sits at 0.78125 BTC"; holding fees constant, today's fee spread turns "the 4.11% difference from the average block value" in Halving Epoch 4 into "a 27.24% difference in Halving Epoch 7", with "5 of the 14 blocks having an over 10% difference". (pp. 141–142)
- Epoch 10 extrapolation: "total block values are > 20% away from the average in 10 of 14 blocks" with fees "14.51%"–"82.35%" of block value — though the author calls this extreme case "not particularly realistic" given future demand and off-chain settlement. (p. 142)
- Future hedges: "Hashrate forwards and hashvalue/hashprice futures" (locking revenue "weeks or months into the future") and "Out-of-band payments... agreements with block space consumers (e.g. exchanges) to include their transactions in blocks for a subscription-type fee paid separately (off-chain)". (p. 143)
- Pool solvency warning (verbatim): "Pools can do everything by the book and still become insolvent if their reserves are not deep enough to withstand bad luck, especially if they have bad block finding luck and bad transaction fee luck at the same time." (p. 143)
- Stratum V2 accounting: template-based share valuation adds "block finding luck, transaction fee luck, and block template luck. Variance^3. The mining pool business is rough." (p. 145)
- Ordinals addendum: out-of-band payments "have undoubtedly increased significantly (albeit maybe temporarily) thanks to ordinals, as well as increased demand for transaction accelerator services where pools take an off-chain payment to prioritize a lower fee transaction in their blocks". (p. 146)
