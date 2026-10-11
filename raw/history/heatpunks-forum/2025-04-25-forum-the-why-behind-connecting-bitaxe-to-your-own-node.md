# The Why behind connecting Bitaxe to your own node?

> Source: https://forum.heatpunks.org/t/the-why-behind-connecting-bitaxe-to-your-own-node/102
> Collected: 2026-10-10
> Published: 2025-04-25
> Registry ID: heatpunks-forum

Gunrs17 | 2025-04-25 19:54:40 UTC | #1

By default the AXEoS settings have us connected to [public-pool.io](http://public-pool.io).  I run a full node and understand the steps to download the [public-pool.io](http://public-pool.io) app and change the AXEoS settings to point to my node.  I’m trying to understand WHY and what is happening differently when I switch out of the default AXEoS settings - Is it that with the default settings, we are trusting/relying on [public-pool.io](http://public-pool.io)’s node.  Meaning if they decide to change the software their node is running, we will be mining with the ‘new’ consensus rules of their node.  Whereas when I connect to my node I know what software I’m running.  Is that what is meant by ‘making your own block headers’

-------------------------

tronsington | 2025-05-13 15:42:37 UTC | #2

Your understanding is exactly correct. By mining to public-pool, you are using their node and block templates.

You can set up a Datum Gateway in “lotto” mode to effectively get the same results. Using your own node and block templates or you can set up your own public-pool instance that connects to your own node. sethforprivacy has good guide [here](https://github.com/sethforprivacy/sethforprivacy.com/blob/master/content/guides/run-your-own-bitcoin-pool.md).

-------------------------

thak777 | 2025-05-22 18:43:54 UTC | #3

I recently found out about Parasite: a lotto pool where the winner gets 1 BTC and everyone else receives “their share” of the hashrate. [https://parasite.space/](https://parasite.space/)

It’s certainly not as decentralized as mining on your own node, but if you’re onboarding someone with a Bitaxe…this payout methodology might be a way they’d bite.
