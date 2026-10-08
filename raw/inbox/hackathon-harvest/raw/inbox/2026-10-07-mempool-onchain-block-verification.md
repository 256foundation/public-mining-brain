# On-chain verification: Public Pool / Bitaxe-era solo blocks (2026-10-07)

> Source: https://mempool.space/api (mempool.space public REST API)
> Collected: 2026-10-07
> Published: N/A (live point-in-time verification)

## Results

| Height | UTC timestamp | On-chain coinbase tag (verbatim) | Payout address (vout 0) | Verdict |
|---|---|---|---|---|
| 853742 | 2024-07-24 17:43:43 | `/solo.ckpool.org/` (ckpool solo, no Public Pool tag) | bc1qk4czgwtfhxwfd9r696kzledtmlu8yukdzpzn3u (312,864,161 sats) | NO-matching-tag |
| 868790 | 2024-11-04 06:06:05 | `/ViaBTC/` (ViaBTC pool, no Public Pool tag) | 1PuJjnF476W3zXfVYmJfGnouzFDAXakkL4 (317,294,197 sats) | NO-matching-tag |
| 888989 | 2025-03-23 00:30:28 | `Public Pool on Umbrel` | bc1qx2g6p9etqu0dtt4xm9nzdusql6vv55jgp9qazc (315,188,086 sats) | CONFIRMED-tag |
| 920440 | 2025-10-23 19:32:45 | `Public Pool on Umbrel` | bc1qt6j9nefpkrv465slpk7pt9hfc4xjnkwmphq3wh (314,115,228 sats) | CONFIRMED-tag |
| 928985 | 2025-12-22 14:50:14 | `Public Pool on Umbrel` | bc1q9mnprx0vjfa927v5qujygyg7rcxarw5cwtaqsp (312,788,664 sats) | CONFIRMED-tag |
| 937218 | 2026-02-18 11:22:29 | `Public Pool on Umbrel` | bc1q5n82h4mkgn4g2q8vp8kpdlh64w26a7kh9kg45q (314,345,306 sats) | CONFIRMED-tag |
| 947073 | 2026-04-28 22:52:18 | `Public Pool on Umbrel` | bc1qzwh6045qaspz57u7gz0m4atjlnx4y8vsp8wlr0 (314,143,172 sats) | CONFIRMED-tag |
| 948146 | 2026-05-06 09:28:35 | `Public Pool on Umbrel` | bc1q08yxd5h4sr9645vn5xhzayzpq7nat6hacrvw0g (315,458,553 sats) | CONFIRMED-tag |
| 957382 | 2026-07-10 03:30:34 | `Public-Pool` (variant tag without "on Umbrel") | bc1q0pp74ghs25vpn2ah6auz4vkehvzy8z8ddyzts7 (313,823,506 sats) | CONFIRMED-tag |

## Disputed block 868790

Block 868790 (2024-11-04 06:06:05 UTC, hash `0000000000000000000021c11aae5e2a60a20726c2229a844c6733411a56f714`) shows **no Public Pool tag of any kind**. Its decoded coinbase scriptSig reads `/ViaBTC/`, and mempool.space attributes the block to the ViaBTC pool (`/api/v1/mining/pool/publicpool/blocks` does not list it). A vendor-blog claim that 868790 was a Public Pool solo block is not supported by on-chain data.

Block 853742 carries the solo.ckpool.org tag (`/solo.ckpool.org/`), i.e., the solo-customer flavor of CK Pool, not Public Pool.

## Authoritative Public Pool listing

`/api/v1/mining/pool/publicpool` (HTTP 200): pool id 161, `"regexes":["Public-Pool","Public Pool on Umbrel"]`, `blockCount.all = 8`, `blockCount.1w = 0`, `estimatedHashrate = 0`, `totalReward = 2514629969` sats, avgBlockHealth 99.8.

`/api/v1/mining/pool/publicpool/blocks` returns exactly 8 blocks:

| Height | UTC timestamp |
|---|---|
| 957382 | 2026-07-10T03:30:34+00:00 |
| 948146 | 2026-05-06T09:28:35+00:00 |
| 947073 | 2026-04-28T22:52:18+00:00 |
| 943466 | 2026-04-03T06:07:40+00:00 |
| 937218 | 2026-02-18T11:22:29+00:00 |
| 928985 | 2025-12-22T14:50:14+00:00 |
| 920440 | 2025-10-23T19:32:45+00:00 |
| 888989 | 2025-03-23T00:30:28+00:00 |

This matches the 7 CONFIRMED-tag heights above plus **943466 (2026-04-03)**, a Public Pool block attributable per the API that was not in the requested verification list (not individually inspected here). Neither 853742 nor 868790 appears in the Public Pool block list, consistent with their coinbase tags.

Additional endpoint attempts:
- `/api/v1/mining/pools/1w` — HTTP 200, but Public Pool not present (1-week window; its most recent block is 2026-07).
- `/api/v1/mining/pool/publicpool/blocks/all` — HTTP 500 ("Failed to get blocks for pool").
- `/api/v1/mining/pool/publicpool/hashrate/1y` — HTTP 404.

## Method log

Commands that worked (run with curl; JSON parsed with python3):

```bash
# 1. height -> block hash
curl -s https://mempool.space/api/block-height/{HEIGHT}

# 2. block metadata (timestamp, height)
curl -s https://mempool.space/api/block/{HASH}

# 3. coinbase txid (index 0)
curl -s https://mempool.space/api/block/{HASH}/txid/0

# 4. coinbase tx; decode vin[0].scriptsig hex -> ASCII for the tag; read vout[0]
curl -s https://mempool.space/api/tx/{TXID} \
  | python3 -c "import json,sys; d=json.load(sys.stdin); ss=d['vin'][0]['scriptsig']; print(bytes.fromhex(ss)); print(d['vout'][0].get('scriptpubkey_address'), d['vout'][0].get('value'))"

# 5. pool profile + attribution regexes
curl -s https://mempool.space/api/v1/mining/pool/publicpool

# 6. pool's attributed block list
curl -s https://mempool.space/api/v1/mining/pool/publicpool/blocks
```

Timestamps converted with `datetime.fromtimestamp(ts, timezone.utc)`. All endpoints above returned HTTP 200 except where noted.

## Addendum (same collection session, same method)

- **943466 individually inspected**: 2026-04-03 06:07:40 UTC, coinbase ASCII contains `Public-Pool` — CONFIRMED-tag. Total verified Public Pool blocks = 8: 888989, 920440, 928985, 937218, 943466, 947073, 948146, 957382 (all-time per pool listing).
- **Additional press-claimed Bitaxe-family blocks verified on-chain** (Solo CKPool relay, hardware attribution from press reports only — chain shows pool tag, not hardware):
  - 887212 — 2025-03-10 19:22:04 UTC — coinbase tag `/solo.ckpool.org/` — CONFIRMED as Solo CKPool relay (press: Bitaxe cluster ~480 GH/s, CoinTelegraph 2025-03-10)
  - 889975 — 2025-03-29 13:12:09 UTC — coinbase tag `/solo.ckpool.org/` — CONFIRMED as Solo CKPool relay (press: stock Bitaxe Gamma, Decrypt/CT ~2025-03)
  - 924569 — 2025-11-21 14:13:06 UTC — coinbase tag `/solo.ckpool.org/` — CONFIRMED as Solo CKPool relay (press: Bitaxe Gamma-class, Decrypt 2025-11-21)

Cross-reference: where timestamps differ from raw/inbox/2026-10-07-bitaxe-open-source-mining-blocks-found.md, the on-chain values in THIS file are authoritative (that file's timestamps came from an explorer display listing). The vendor-blog claim about 868790 is resolved above: `/ViaBTC/` tag — claim not supported on-chain.

Aggregate verified solo-block picture (2024-07 → 2026-07): 4 Solo-CKPool-relayed blocks with press Bitaxe attribution (853742, 887212, 889975, 924569) + 8 Public Pool-tagged blocks (888989 → 957382) = 12 open-source-mining-era solo blocks with on-chain verification as of 2026-10-07.
