# Bitcoin Mining Handbook — ch. 56+63: Stratum V2 — Hashrate Robbery & Decentralization (2 chapters, extract)

> Source: https://braiins.com/books/bitcoin-mining-handbook (PDF: https://cdn.prod.website-files.com/5e5fcd39a7ed2643c8f70a6a/63ebadbe407c5bc4621f0d2a_Handbook%20I_web%20verze_3.pdf) (Braiins Publishing, free PDF)
> Collected: 2026-10-10
> Published: 2022
> Registry ID: braiins-books
> Posture: extract (key information with chapter attribution; full text at source PDF)

## Key points (ch. 56 — Hashrate Robbery: Stratum V2 Fixes This (and More))

- Context (2021): "Bitcoin's total network hashrate has increased by nearly 200% in the past year alone." (p. 56)
- Scale reference: "a single new-generation ASIC today has roughly 700x more hashing power than the entire network did" when Slush Pool mined its first block in 2010. (p. 57)
- V1 security flaw: "Stratum V1 has a major security flaw: it's vulnerable to man-in-the-middle (MITM) attacks. The worst of these attacks is hashrate hijacking, in which a malicious third party is able to steal a miner's proof of work before it reaches their target pool." (p. 58)
- Stealth theft: "an attacker can steal their hashrate completely undetected... they might steal only 1% or 2% — enough to impact the miner's bottom line, but not enough for the miner to be sure that they are being attacked." (p. 58)
- Fix: "Connections between miners and pools in V2 are encrypted with a scheme known as authenticated encryption with associated data (AEAD), which protects the integrity of the data transfers." (p. 58)
- Prevalence: "we are aware of miners from China, Kazakhstan, Russia, and Europe who strongly suspect that they are having hashrate hijacked... it's possible that this problem is far bigger than anybody realizes." (p. 58)
- Efficiency gains: "Every day at Slush Pool, we process millions of data transfers across tens of thousands of individual physical connections. Stratum V2 decreases both the size and quantity of those data transfers." (p. 59)
- Multiplexing: "Stratum V2's multiplexing feature makes it possible for miners to mine multiple coins on a single connection as well as doing zero-time backend switching." (p. 59)
- Header-only mining: "a simplified mining mode for ASICs... gives miners the option to avoid merkle path handling, simplifying firmware and making work validation lighter for pools... results in lower hashrate variance for miners." (p. 59)
- Adoption path: "a full implementation of Stratum V2 in our BOSminer software component, which will be free and open-source", plus "translation proxies for V2 -> V1 and vice versa" so miners can use V2 on V1 pools and vice versa. (pp. 60–61)

## Key points (ch. 63 — Bitcoin's Decentralization with Stratum V2)

- V1 flow: pool "sends miner job assignments (i.e. block templates to work on, without full transaction sets)"; "Pools and solo miners are the only entities that are constructing block templates." (p. 64)
- V2 Job Negotiation flow: the Job Negotiator requests a block template from the pool; "Pool verifies that the transactions included are valid"; "Pool verifies coinbase transaction outputs are correct (i.e. paid to the pool address)"; "If a block is found, the miner can propagate the block themselves and censorship by the pool is not possible." (pp. 64–65)
- Payout economics under V2 (verbatim): "every miner is paid based on the value of the shares they submit, not based on the value of the block that gets mined." Example: "Block Template 1 value: 8.0 BTC" vs "Block Template 2 value: 7.5 BTC" — miners on the higher-value template "will be paid proportionally more for their valid shares." (p. 65)
- Latency handling: "an asynchronous start, which means that miners can begin working on their own blocks immediately while the pool is still validating them"; if a proposed template is invalid, "the shares from those few seconds of work are rejected". (p. 65)
- Early-warning property: a rejected-but-valid template is a signal — "the miner is tipped off that they should reconnect to a different pool or solo mine" — Job Negotiation "serves as an early warning system that alerts miners to possible issues with pool operators." (p. 65)
- State-attack scenario: 4 pools with a combined majority commandeered by "a malicious party (e.g., their nation's government)"; miners proposing their own work "could effectively prevent a sustained 51% attack by switching pools as soon as their original pools start censoring them", dropping the attackers below 50%. (p. 66)
- Custody risk bounds: "Pools send payouts frequently (multiple times per day in most cases), so the financial risk for miners of not getting paid for valid work is minimal. Meanwhile, pools who don't pay their miners risk permanent reputational damage." (p. 67)
- Decentralization economics: "By running their own full nodes and working on their own block templates, miners can add redundancy (safety) to the network and strengthen Bitcoin's fundamentals at minimal added cost." (p. 68)
