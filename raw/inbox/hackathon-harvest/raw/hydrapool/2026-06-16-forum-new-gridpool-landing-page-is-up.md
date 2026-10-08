# New GridPool landing page is up

> Source: https://forum.256foundation.org/t/new-gridpool-landing-page-is-up/61
> Collected: 2026-10-07
> Published: 2026-06-16

AgentP | 2026-06-17 09:46:53 UTC | #1

Hi cypherpunks!  Many thanks again to the 256 Foundation team for giving me time on the show last week.

A new landing page for GridPool is live now at gridpool.net, and provides some explanatory material and resources.

If you like the idea and want to contribute to the project:

* Send some hash to the pool, either using my demo node and your DATUM client or by spinning up your own GridPool node.  Instructions are on the main site.
* Give me feedback please! Either on Github or on this forum, whatever is easier for you.  I’m trying hard to make this easy to understand and easy to use.

AgentP

![gridpool_logo|500x500](upload://53rGZuy8o2W8dl8Ry61dOqsEtlr.png)

-------------------------

AgentP | 2026-06-25 11:55:11 UTC | #2

I’ve gotten some great early feedback on the gridpool concept, and want to record it here to make sure the knowledge isn’t lost.

1/4: Jason Hughes noted on X ( https://x.com/wk057/status/2067784321134453103?s=20 ).  Further: “You may attract some brief lotto-miner minded folks to give a shot as-is, but I think it'll be pretty tough to have any large miner give up 50% of the reward for their work since, on avg, it'll take work worth the full block reward to find the block.”

This feedback resulted in the biggest change to GridPool in a while, Version 2 of the protocol, in which the active payout list is more frequently synced with the list of best shares.  The Genesis block payout is thus a reflection of the work put into that first block, and new miners can get an actual payout sooner, rather than waiting a full pool block later.

@jungly noted two things:

2/4: “One thing that is not clear to me is gridpool’s vulnerability to pool hopping. A miner can get a decent high difficulty share and then leave the pool to point the hashrate elsewhere. This is a classic pool hopping problem. We could put a TTL on the shares, but that will punish honest miners who won a high diff share and are still mining, but not being as lucky as in the past.

The same can be extended as saying, a large miner comes along, earns a bunch of slots and then goes away to mine on low variance pools. Then the small miners are working on gridpool to find a block where a no-longer-active large miner will get paid for small amount of total work done.”

My response: “This always struck me as a strategy used by miners who don’t understand statistics, I don’t think the strategy you described works out in their favor.  But perhaps I haven’t given the strategies enough careful attention.  The clearest reason I can point to is that in GridPool the block finder makes slightly more, because all miners take Slot-0 + all transaction fees for themselves on the templates they build.  If a miner hit a lucky streak and earned a bunch of extra payout slots, they should want to put point extra power into GridPool since that is their chance to actually mine a block that gives them an unusually high payout.
But I will dig into this a bit more to see if I can break it, it’s worth understanding better.”

3/4: “The other concern is the loose consensus approach taken in gridpool. You say in the docs that if a server finds its coinbase (or was it winners list) is not the same as the one received from the other server, it tries to sync with the remote server to reach consistency. This is exactly the consensus problem that sharechain solves in p2pool and was solved explicitly by using a consensus protocol in radpool. If your membership is known, I would recommend using a consensus protocol to reach coinbase and accounting consistency just like radpool did.”

My response got long-winded:  
”GridPool definitely uses a consensus layer, just not a long chain.  In GridPool its analogous to the “heaviest chain rule”, basically the “heaviest Winners List” rule.  This is actually a critical piece of the system.  If your node finds another node working on a different list than it’s own, it asks for the complete proof of that list.  This includes all of the original PoW shares that were used to create that list, each with their own Slot-0 address for attribution and other header data so that your node can trustlessly prove that each of those miners actually earned that spot.  It also allows your node to total up the difficulty of all the shares that built that list (or this might be median, I can’t recall, I’ll check).  A higher difficulty list indicates a stronger team with more hashrate.  Selfishly, most miners would want to join the team that has the most hashrate and the highest chance of actually hitting a real block.  So if your node through gossip finds that there is a group of miners with a higher powered list, it will switch it’s active list to match, and build templates that are consensus valid (pays the correct addresses) with that newer stronger team.
This rule is also used to deal with two other important scenarios:
1/2 Latency:  An edge case is that half the pool sees a last minute share come in just before the next Bitcoin block, and thus include it in the new locked payout list. The other half, due to latency, sees the last minute share afterwards.  This creates a “pool split”, which we’d rather avoid.  Both groups continue mining on the best list they see, but eventually word will get around of the stronger list.  This does result in some lost work, since miners on the minority list will spend some time producing shares for the weaker side.  To mitigate this, I added “Compact Share Relay”.  For nodes that support it, shares are reduced to just enough info for other nodes to reconstruct the share proof (slot-0 address, nonce, time, version). This should be <1200 Bytes so it fits in a single UDP packet, FIBRE style.  This is still untested, but should help a lot.
2/2 Censorship:  A naive miner might decide to try to censor the shares of another miner.  Though transaction selection is blinded, maybe they want to censor that miner’s coinbase payout (Slot-0 address).  If they discard these “banned” shares, they will end up working on a lower difficulty list than miners who accept the shares.  As long as one node on the network keeps the shares, they will produce a list that is stronger (heavier) than the censored list, and most nodes should be economically interested in working for the strong team. The miner that “forked off” will start producing shares that don’t include the correct payout list, and their shares will be discarded by the rest of the network.  I think this is even true if they had 99% of the pool’s hashrate, not just 51%, although I think I need to game this out more carefully to make sure I’m not overclaiming.”

4/4: Finally, another dev noted that “There are a lot of claims being made that I am unable to find supporting data for.”  Especially regarding modeling and simulation of the network, and bandwidth and latency performance.  
This is really good feedback, and some careful testing of the network performance should be very high on my list once I can get more nodes setup to test with.

-------------------------
