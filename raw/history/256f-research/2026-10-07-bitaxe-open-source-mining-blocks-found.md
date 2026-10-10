# Solo blocks found by Bitaxe / open-source miners — research notes (2026-10-07)

> Source: press reports and community pools/explorers as linked per entry
> Collected: 2026-10-07
> Published: various (per entry)

Method: web search across press + block-explorer miner-tag listings. Heights and timestamps below come from the cited sources; **before public/demo use, verify every height and timestamp against a block explorer** (e.g. `curl https://mempool.space/api/block-height/{height}` then `GET /api/block/{hash}` for timestamp and `GET /api/block/{hash}/txid/0` + tx for coinbase tag). Items marked UNVERIFIED were claimed only in secondary/vendor content.

## Verified-by-multiple-sources / on-chain-tag blocks

1. **Block 853,742 — 2024-07-24 (~11:43 UTC). First widely-known Bitaxe block.**
   - Relayed by Solo CKPool; 290th solo block relayed by the pool; reward 3.192 BTC (~$200–207K at the time).
   - Reported hashrate ~3 TH/s per Dr. -ck (ckpooldev) X post: "Congratulations to miner with the first bitaxe block, only a tiny 3TH ... 290th solo block on solo ckpool ... once every 3500 YEARS on average, or 1 in 1.2 MILLION chance per day!" Altair Technology reported ~500 GH/s device. Hardware generation not definitively identified (community speculation included multi-chip variants).
   - Sources: https://cointelegraph.com/news/tiny-500gh-home-bitcoin-mining-device-produced-a-block-earning-over-200k-btc · https://www.theenergymag.com/news/2024-07-24/solo-bitcoin-miner-block · https://forklog.com/en/solo-miner-strikes-bitcoin-block-earning-212000/ · https://www.nobsbitcoin.com/a-bitaxe-has-found-a-block/ · https://thebitcoinmanual.com/articles/bitaxe-nets-block/ · https://stacker.news/items/621289

2. **Block 888,989 — 2025-03-22 (20:30:28 UTC). First "Public Pool on Umbrel" block.**
   - Coinbase tag: `Public Pool on Umbrel` (block-explorer miner-tag listing). Total reward ~3.15 BTC.
   - Hardware not proven: Umbrel community forum analysis found the miner had left Solo CKPool 17 days earlier and the hashrate pattern was "likely a Bitaxe" and "not a NerdMiner". Attribution = probable-Bitaxe, self-hosted Public Pool on an Umbrel home server.
   - Sources: https://community.umbrel.com/t/a-legendary-day-for-umbrel-and-bitcoin/21957 · https://memepool.space/mining/pool/publicpool

3. **Block 920,440 — 2025-10-23. NerdQaxe++ Rev 6 on self-hosted Public Pool (Umbrel).**
   - Coinbase tag: `Public Pool on Umbrel`. Operator reported a cluster of six NerdQaxe++ + one Avalon Q (~130 TH/s total); best share ~2.08P; payout ≈ 3.14 BTC (~$342–347K).
   - Sources: https://www.solosatoshi.com/nerdqaxe-revision-6-block-found-on-public-pool/ · https://www.tradingview.com/news/cointelegraph:a44649ca2094b:0-solo-bitcoin-miner-scores-347k-pure-self-soverignty-in-action/ · https://bitcointalk.org/index.php?topic=5563335.0 · https://stacker.news/items/1263692

4. **Later "Public Pool"-tagged blocks** (from block-explorer miner-tag listing, timestamps UTC):
   - 928,985 — 2025-12-22 09:50:14 — tag `Public Pool on Umbrel`
   - 937,218 — 2026-02-18 06:22:29 — tag `Public Pool on Umbrel`
   - 947,073 — 2026-04-28 18:52:18 — tag `Public Pool on Umbrel` (Reddit r/BitAxe thread same day: https://www.reddit.com/r/BitAxe/comments/1syh7zw/)
   - 948,146 — 2026-05-06 05:28:35 — tag `Public Pool on Umbrel`
   - 957,382 — 2026-07-09 23:30:34 — tag `Public-Pool`
   - Source: https://memepool.space/mining/pool/publicpool (listing as of 2026-10-07; one additional row was partially truncated in capture — pull the live listing for the authoritative full set).

## UNVERIFIED (claim, needs on-chain check)

- **Block 868,790 — "October 2024"**: D-Central blog claims a Bitaxe Gamma (~1.2 TH/s) found this block "on Public Pool". It does not appear with a Public Pool coinbase tag in the listing above (Public Pool tags begin at 888,989), and hardware/pool attribution is sourced only to the vendor blog. Verify coinbase tag before demo use.
  - Source: https://d-central.tech/historic-moment-for-bitcoin-mining-the-first-pleb-fu-block-mined-by-a-bitaxe/

## Demo-relevant framing (from sources)

- CoinTelegraph (2024-07-24): the ~500 GH/s device had "1 in 1.1 billion" chance per 10 minutes against ~552 EH/s network.
- ckpooldev: 1 in 1.2M chance per day at 3 TH/s; ~once per 3,500 years on average.
- Bitcointalk (2025-10-24): "Users who host Public Pool themselves have found 2 blocks in 7 months" (888,989 and 920,440 era).

## On-chain verification recipe (for the build team)

```
curl -s https://mempool.space/api/block-height/853742          # → block hash
curl -s https://mempool.space/api/block/<hash>                 # → timestamp, size, reward fields
curl -s https://mempool.space/api/block/<hash>/txid/0          # → coinbase txid
curl -s https://mempool.space/api/tx/<coinbase_txid>           # → vin[0].scriptsig (hex) → decode ASCII for pool tag
```
