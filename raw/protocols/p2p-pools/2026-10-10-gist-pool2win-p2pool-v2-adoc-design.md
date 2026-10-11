# P2Poolv2 — design doc gist "P2Pool-v2" (pool2win), verbatim (AsciiDoc)

> Source: https://gist.github.com/pool2win/41f1c0011bd13dc993165c6128084b5d (file p2pool-v2.adoc; companion image trading-shares.png in same gist)
> Collected: 2026-10-10
> Published: 2024-12-05 (gist last updated)
> Registry ID: p2pool-v2

---

= P2Pool-v2

This gist describes a scheme to reboot p2pool with minimal changes to
P2Pool's design. The goal of the project is to reboot p2pool with a
linear chain with a transaction system to enable trading of shares
between miners. Smaller miners will trade their share with the larger
miners to get paid over lightning, while the larger miners are paid
out using the coinbase outputs.


== Sharechain

We propose using the linear sharechain of p2pool. We will use tools
like either libbitcoin or https://substrate.io[substrate] to build the
chain, they both have pros and cons we can weigh them to pick one of
the frameworks.

=== Sharechain Accounts

The sharechain supports miner accounts. This decision is motivated by
the need to roll up a miner's balance as they accumulate shares on
chain. Smaller miners will be able to build up balance of PPLNS shares
in their sharechain accounts. We describe how miners can trade their
shares for BTC in the <<Trading Shares>> section.

The miners shares that get included in the sharechain are associated
to the miner's account. This can be done exactly how it happened in
p2pool, i.e. by including public key in the share. This allows us to
update the miner's account balance each time a new share is included
in the share chain or p2pool finds a bitcoin block.


The accounts on sharechain include the followint to attributes for
managing payouts:

Balance:: The balance in normalised PPLNS shares that have been
accepted by the sharechain. This is updated each time the pool finds
blocks or a new share is added to the sharechain.
Payout Script Pub Key:: The output script that the miner can spend
using their account private key. A miner can submit transactions to
the sharechain, transferring their balance to another miner or a
market maker.

=== Transactions

The sharechain supports transactions which are explicit transactions,
i.e. they don't need a script engine and are more like stored
procedures or "smart contracts". These transactions work on the
accounts from the sharechain. We support the following transaction
types that an account owner can execute on their account.

Update payout script pubkey:: This updates the payout script for a
miner's shares. For large miners this is used in their coinbase
outputs. For smaller miners, this script is used to execute the `Trade
Shares` transaction.
Trade Shares:: This transaction uses the HTLC semantics to swap the
selected balance amount enabling an atomic swap of amount with the
other party's BTC on bitcoin. The balance that is swapped is deducted
from ther user's account balance.

Transactions on sharechain work on accounts and not on individual
shares. Swapping each N shares will result in N transactions on the
bitcoin blockchain for the other party. Instead working with
aggregates and balances, the swaps require only a single transaction
on bitcoin for the other party when swapping a number of shares. The
book keeping between shares and account balances is taken care of by
the sharechain. Note here, that substrate supports accounts, so we
don't have to build all this.

== Payout

The miners are paid by applying PPLNS accounting, and the payout
mechanism is two tiered:

Tier 1:: Top 16 miners are paid directly into the bitcoin block's
coinbase.
Tier 2:: The other miners will trade their shares with other miners or
market makers to earn BTC for their shares.

The Tier 1 miner payout is exactly the same as in original p2pool for
the largest miners - i.e. they are paid directly into their coinbase
outputs.

The Tier 2 miners will be able to trade their shares for bitcoin with
the Tier 1 miners or for any other buyers of the shares. The miners
are able to sell their shares to larger miners or market makers using
an atomic swap protocol because sharechain supports the HTLC behaviour
in the `Trade Shares` transaction type.

The image below shows the sum of the PPLNS shares for each miner at
different points in time and how the balances change when miners trade
their shares and when they are paid out.

.Small miner `q` trades shares with miner `M` before payouts
image::https://gist.github.com/pool2win/41f1c0011bd13dc993165c6128084b5d/raw/666e35f004d11d7fbd4b989d98e6f0e72795d96e/trading-shares.png[Trading Shares]

== Trading Shares

A miner with shares on sharechain can trade them for bitcoin BTC using
the script pub key in their sharechain account. The miner uses the
`Trade Shares` transaction to execute the sharechain end of an atomic
swap. At the end of the atomic swap the receiving miner has the
sending miner's balance and will be paid in the next coinbase when
these shares are mature enough to be paid.

Swapping the balance for BTC is the way that smaller miners are
paid. The market for shares and bitcoin BTC is supported by the MVP
with simple CLI commands. We believe, advanced markets will be built
around this simple mechanism.

=== The Economics of Trading Shares

The discount here can be seen as the "pool fee" for smaller miners and
as an extra earning for the larger miners. One can argue that this is
unfair to smaller miners. In case external market makers do not enter
the trading market, the larger miners are the only ones who can buy
the shares from the smaller miners and therefore they will charge much
higher fee rates. However, if larger miners push away smaller miners
from the pool with large fees, the pool's hashrate will fall and the
large miners will suffer increased variance in payouts and miss out of
making an extra yield no matter how small it be. It is also important
to remember that smaller miners can make a large proportion of total
hashrate of the pool due to the long tail phenomenon apparent in
mining.

[NOTE]
====
We need a more detailed analysis here. Our approach will attract some
criticism that it empowers larger miners even further.
====

== Development Plan

We need to develop the following components to ship an MVP.

Sharechain:: We should use an existing framework to build
p2pool-v2. Frameworks like https://substrate.io/[Substrate] allow us
to plug in the proof of work and difficulty adjustment algorithm we
want.

Stratum:: We need a stratum server that handles work and share
messages between miners and the P2Pool node. The server forwards the
messages to sharechain. We should use
https://bitbucket.org/ckolivas/ckpool[ckpool] here as it is the most
robust implementation of a stratum server in the public domain.

Trading and Wallet CLI:: This provides simple API to submit
transactions to the sharechain, and a standalone cli application to
build transactions, sign them and submit to the sharechain API. The
commands here allow miners to 1) update their payout script pubkeys,
and 2) trade their shares by submitting signed transactions to the
sharechain and unsigned transactions to other trading parties. The
closest examples here are lightning cli tools.

Miner stats API:: A websocket interface that provides JSON results for
miners statistics. We can build a dashboard around it later if we
want.

We leave other components like miner registration to support multiple
miners on a single p2pool node for the future. There is a case to
never build this, but p2pool did, so we should see what the miners
want.

[cols=3*]
|===
| Component
| Plan
| Estimated Work Size

| Sharechain
| Use substrate with PoW and uncles support, pruning, difficulty
  adjustment, transaction support.
| Large  

| Stratum
| Use ckpool. Need to add a message queue to consume the shares.
| Medium

| Trading CLI
| Use rust-bdk to implement a cli with the API and other tools
| Small

| Miner stats
| Provide an API in the long run to enable others to build a dashboard
| Small

|===
