# AntPool — Help Center: Miners Settings & Fees / Daily Payout Time

> Source: https://antpoolsupport-hc.zendesk.com/hc/en-us/articles/5983010227993-Miners-Settings-Fees
> Collected: 2026-10-10
> Published: 2022-12-14 (updated)
> Registry ID: antpool

---

# Miners Settings & Fees

*(ANTPOOL Help Center, author "Susie", December 14, 2022, marked "Updated")*

**1. Mining nodes**

Currently, ANTPOOL has deployed mining nodes in many regions at home and abroad and is adding more nodes continuously. When connecting to ANTPOOL, miners will be automatically allocated to their nearest nodes to ensure the stability of mining and to avoid delay of hashrate submission.

**2. Mining addresses and fees**

*(Fee/address table presented as an image in the original article — mceclip0.png. Percentages are NOT given in article text. A legacy AntPool gitbook (antpool.gitbooks.io, now stale, ETH era) listed PPS+ 4% / PPLNS 0% for BTC with 0.001 BTC minimum payout — historical only.)*

**How to configure merged mining?** (Go to "Settings" page — choose LTC account — Click "Configure"… configure DOGE wallet address for merged mining.)

ANTPOOL supports four payment methods: PPS, PPLNS, FPPS (with effect from July 13, 2020).

You can go to "Settings" page to choose the method you prefer based on your risk tolerance level.

**1) FPPS** — FPPS is full PPS. The payment distribution includes: fixed block reward (current 6.25 BTC) + package transaction fee. The actual income of FPPS is not affected by the pool's luck.

**2) PPS (Pay Per Share)** — you are rewarded for your hashrate on a share basis. The more hashrate you have, the more shares you can submit per second.

**3) PPLNS (Pay Per Last N Shares)** — similar to Proportional, but the miner's reward is calculated on a basis of N last shares, instead of all shares for the last round. Transaction fees not paid out to miners are for maintenance and bonus for our engineers. With PPLNS, miners' payout is connected to number of blocks founded.

**3. Miner configuration** — format of miner is "sub-account.miner ID"…

**4. Obtain miner IP** — IP Reporter software (Bitmain download link).

**5. Connect Miner** — default username/password root:root.

---

# When is the daily payout time?

> Source: https://antpoolsupport-hc.zendesk.com/hc/en-us/articles/5985391549977-When-is-the-daily-payout-time
> Published: 2022-12-12 (updated)

To receive your payout, you will first need to configure a valid wallet under "Settings".

Check the minimum payout value in the "Settings" interface. Payment will only be initiated when your balance is above the minimum payout threshold.

The default minimum payout value for Bitcoin is 0.005 BTC. You can modify the value under "Settings" according to your needs.

The minimum payout value is 0.001 for LTC, ZEC and DASH, 0.01 for BCH, 0.1 for XMC and 1 for BTM. Earnings less than the minimum payout value cannot be paid. You can modify the payout value for all coins.

ANTPOOL will process all accounts at 9 o'clock every day. If your balance has reached the minimum payment after today's settlement (after 9 o'clock), payment will be processed next day.

---

*Capture notes (2026-10-10):*
- *Payout schemes (help center): PPS, PPLNS, FPPS (added July 13, 2020). Homepage (untranslated Chinese) also names FPPS/PPS/PPLNS. Legacy gitbook also listed PPS+/SOLO — current Zendesk article does not mention SOLO.*
- *Fee %: not disclosed in text — the "Mining addresses and fees" table is an embedded image (checked the Zendesk article); no numeric BTC fee percentage is published in any crawlable text.*
- *Payout threshold/cadence: default 0.005 BTC minimum payout (user-adjustable); accounts processed daily at 9:00 (timezone unstated in article — legacy docs say Beijing time, payouts 08:00–15:00 Beijing).*
- *Custody: pool holds and pays out rewards; KYC is required — the same help-center section contains "ANTPOOL Individual KYC User Guide" and "ANTPOOL Institutional KYC User Guide" (individual + institutional KYC). Homepage consent gate bars sanctioned countries and mainland-China residents.*
- *Strategic partners listed: BITMAIN, BITFUFU, ANTALPHA (AntPool is the Bitmain-affiliated pool).*
- *No Stratum V2 / DATUM mention in either article. Zendesk 403s plain curl (exit 56); captured via alternate fetcher.*
