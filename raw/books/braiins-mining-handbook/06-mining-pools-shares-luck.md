# Bitcoin Mining Handbook — ch. 47: Bitcoin Mining Pools: Luck, Shares, and Estimated Hashrate Explained (extract)

> Source: https://braiins.com/books/bitcoin-mining-handbook (PDF: https://cdn.prod.website-files.com/5e5fcd39a7ed2643c8f70a6a/63ebadbe407c5bc4621f0d2a_Handbook%20I_web%20verze_3.pdf) (Braiins Publishing, free PDF)
> Collected: 2026-10-10
> Published: 2022
> Registry ID: braiins-books
> Posture: extract (key information with chapter attribution; full text at source PDF)

## Key points (ch. 47)

- Shares vs blocks in the dice analogy: "all the dice rolls below '99' result in shares being submitted to the pool, while they still have to be below '4' to produce a new block." (pp. 48–49)
- Target summary: "Hash outputs < 4: produce a block (and shares); Hash outputs < 99: produce shares; Hash outputs > 99: doesn't meet target, nothing sent to the pool." (p. 49)
- Verification: "To verify the validity of the shares you submitted, the pool simply repeats the same hash computation that you did to produce the shares in the first place." (p. 49)
- Stale shares: "'stale' or 'rejected' shares can occur when you submit shares after the block for those shares has already been found, something which typically occurs in the few milliseconds immediately following a block find" — hence "connect to the nearest pool stratum server to your geographic location." (p. 49)
- Why shares matter: "without shares, pools would have to redo ALL the hashes that miners do... public mining pools couldn't exist without shares." (p. 49)
- Per-miner share difficulty: "a miner with 100 PH/s will have a higher share difficulty... than a miner with 15 TH/s. The goal in setting this share target is for miners to be submitting shares about once every 2-3 seconds." (p. 49)
- Share accounting: "1 share = 1 proof of work on difficulty 1"; "5 shares = 1 proof of work on difficulty 5"; "100 shares = 1 proof of work on difficulty 100" — a hash below share target D is worth D shares, so pools validate big miners without linearly scaling their own work. (p. 50)
- Luck definition (verbatim): "Pool luck is defined as the expected number of shares to find a block divided by the actual number of shares it took for the pool to find a block." (p. 51)
- Worked example: 10 miners × 10 shares/second = 100 shares/s; expected 600,000 shares per block → "6,000 seconds (100 minutes)... the pool should find a block once every 1 hour and 40 minutes"; a block after 300,000 shares = "600k/300k*100% = 200%" luck; after 1,200,000 shares = "600k/1200k*100% = 50%". (p. 51)
- "luck always trends towards 100% over time—it's just math." (pp. 52–53)
- What luck ignores: "it doesn't matter whether other miners / pools find 20 blocks or 0 blocks in that time—the only things that matter for pool luck is the quantity of shares submitted to the pool and the network difficulty." (p. 52)
- Rewards translation: at a constant share of pool hashrate, "luck translates 1:1 with your actual vs. expected mining rewards" — 200% luck = 2x expected, 50% luck = half. (pp. 52–53)
- No market timing: "Every hash is just as likely as any other to produce a new block"; "since mining is pure math without any human emotion element (unlike markets), it is even more pointless to try to time it." (p. 53)
- Estimated hashrate methodology: "the period we use is 720 blocks, which works out to 5 days of mining activity if the average block time is 10 minutes" — a compromise between variance and lag; "this is why different dashboards can have different numbers—there's no one 'correct' way to do it." (p. 54)
- "As long as pool operators are honest in reporting their hashrate, the reported hashrate values will always be more accurate than the estimated hashrate values because estimated hashrate incorporates the natural short-term variance in bitcoin mining." (p. 54)
