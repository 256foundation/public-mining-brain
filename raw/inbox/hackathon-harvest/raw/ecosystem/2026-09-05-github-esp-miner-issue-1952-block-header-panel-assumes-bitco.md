# bitaxeorg/ESP-Miner issue #1952: Block Header panel assumes Bitcoin: shows "BTC" ticker and Base58 addresses for a Bitcoin Cash SV2 template

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1952
> Collected: 2026-10-07
> Published: 2026-09-05

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1952
- State: closed
- Author: solofurypool-code
- Opened: 2026-09-05
- Closed: 2026-09-08
- Labels: none

## Description

Describe the bug

When mining Bitcoin Cash over an SV2 extended channel, the Block Header panel decodes the coinbase template using Bitcoin conventions. Mining itself works perfectly (handshake, channel, shares, vardiff) — this is a display issue, but it defeats the purpose of the panel, which is letting the miner verify who gets paid.

Two things are wrong in the panel for a BCH template:

The ticker is hardcoded to "BTC". The value shown (3.12550206) is correct — it is the BCH block reward plus fees — but it is labelled BTC.
Output addresses are rendered as Bitcoin Base58 (1...). AxeOS takes the hash160 from each output script and encodes it with the Bitcoin P2PKH version byte. On Bitcoin Cash the same hash160 is normally shown as CashAddr (bitcoincash:q...), which is what every BCH wallet and explorer displays. A miner comparing the panel against the address they configured sees two strings that look unrelated, even though they encode the same key hash — so the verification the extended channel is meant to enable cannot actually be performed by eye.

Observed values:

Height     967203
Difficulty 437.90 G
Scriptsig  ...SoloFury
Value      3.12550206 BTC
Outputs    1Nv2Wx9X...Xt4pv    3.09424704 BTC
           1KZ7CuT2...qLf8o    0.03125502 BTC

To Reproduce

Configure a pool pointing to a Bitcoin Cash SV2 endpoint (Stratum V2, Extended Channels, pool authority key set).
Wait for the channel to open and the first job to arrive.
Open the AxeOS dashboard and look at the Block Header panel.
Ticker reads "BTC"; output addresses are shown in Bitcoin Base58 form instead of CashAddr.

Expected behavior

The ticker should reflect the chain being mined (BCH here), and addresses should be rendered in that chain's native format (CashAddr for Bitcoin Cash). If chain detection is out of scope, a minimal fix would be to show the raw hash160 / scriptPubKey next to the encoded address, so a user can compare it against their own address regardless of chain.

Possible approaches, in rough order of effort:

an optional per-pool "chain" setting (BTC / BCH / …) selecting ticker and address encoder;
inferring the chain from the template (a coinbase with no witness commitment output is not a Bitcoin template);
showing the raw hash160 alongside the encoded address.

Screenshots & Photos

(see attached AxeOS screenshot of the Block Header panel)

Hardware (please complete the following information):

Bitaxe HW version: Gamma Turbo 801
Bitaxe HW vendor: <inserisci dove l'hai comprato>
ESP-Miner FW version: 2.15.0
Hash Frequency: <da AxeOS → Settings>
Voltage: <da AxeOS → Settings>
Pool URL, Port, User: eu-bch.solofury.com, 7333 (Stratum V2, extended channel, authority key 9c5s3n4RzRrDhzMBr3iSJsUfreSLPGiHkQyyzJjYAVWK9YWaZf7), user = <your BCH CashAddr>.bitaxe801

Additional context

I'm happy to test any branch on real hardware against a live BCH SV2 endpoint and report back — it's a public pool, so anyone working on this can reproduce it without special setup.

Background on the pool side, including the SV2-on-BCH specifics that are relevant here (no witness commitment in the coinbase, CashAddr miner identity, per-block difficulty adjustment): https://solofury.com/blog/stratum-v2-bitcoin-cash-solo-mining/

## Comments

### WantClue on 2026-09-08

There is no second best, we only do bitcoin.

### solofurypool-code on 2026-09-08

Understood, thanks for the quick answer.

### WantClue on 2026-09-08

Your input is appreciate tho and we welcome any improvements as long as we focus on Bitcoin :-) 

### solofurypool-code on 2026-09-08

Thanks, appreciated — and fair enough.

While testing Stratum V2 for Bitcoin with Bitaxes on my pool (SoloFury) before putting it into production, I noted a few things from the pool side that might be useful for the firmware, in case any of them fits the roadmap. 

1. Coinbase verification: next to the decoded output addresses, showing the raw scriptPubKey (or hash160) would let a miner verify the payout byte-for-byte, regardless of address encoding (bech32 vs legacy, P2SH, P2TR). That's the whole point of the extended channel, and a raw field is the one thing that can never be mis-rendered.

2. OpenMiningChannel errors: when the pool answers with OpenMiningChannel.Error, stratum_v2_task.c currently logs "OpenChannel rejected by pool (msg_type=…)" and sets "SV2: Pool rejected miner", then retries. The error frame carries an error_code (invalid-username, unsupported-channel-type, …) — parsing it and surfacing it in that status string would tell the owner exactly why, instead of leaving them guessing. On the pool side we see it instantly in the log; the miner owner can't.

3. Share rejections: in a later round of SV2 tests a Bitaxe retried every second for minutes with every share rejected as invalid-channel-id (a bug on our side, since fixed). Rejections are already counted via SYSTEM_notify_rejected_share; a rule like "N consecutive invalid-channel-id → reopen the channel" would make that case self-healing.

Happy to test any of these on real hardware against a live SV2 endpoint whenever useful. Thanks for the fast responses.
