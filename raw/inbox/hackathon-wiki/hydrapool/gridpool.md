# GridPool

> Sources: AgentP (256 Foundation forum: New GridPool landing page is up), 2026-06-16; AgentP (256 Foundation forum: GridPool 1-click packages are released), 2026-09-15
> Raw: [forum: New GridPool landing page is up](../../raw/hydrapool/2026-06-16-forum-new-gridpool-landing-page-is-up.md); [forum: GridPool 1-click packages are released](../../raw/hydrapool/2026-09-15-forum-gridpool-1-click-packages-are-released.md)
> Updated: 2026-10-07

## Overview

GridPool is a community project by forum member AgentP for splitting Bitcoin mining rewards with no pool operator. It is not a 256 Foundation project. It appears in this wiki because it was presented on the foundation's show, discussed on the foundation's forum, and reviewed by foundation contributors. Each miner builds its own block templates, and the nodes agree on a shared payout list by a heaviest-list rule instead of a sharechain. One-click packages for Umbrel and StartOS were released in September 2026 as a beta.

## What it claims

From the release announcement:

- Rewards are split with no pool operator.
- Miners keep solo-style template control, with much lower payout variance.
- No custodial wallet, no sharechain, and no central share accountant.
- Each miner keeps its own templates hidden.

## How it works

The forum posts describe the design only in passing. What they do say:

- **Payout slots.** Miners earn slots on a payout list, called the Winners List, by finding high-difficulty shares.
- **Slot-0.** The miner that builds a template takes Slot-0 and all transaction fees for itself. So the block finder makes slightly more than the others.
- **Heaviest list rule.** If a node sees another node working on a different list, it asks for the full proof. That proof includes the original proof-of-work shares behind the list, each with its Slot-0 address. The node can then verify that each miner earned its spot, and add up the difficulty behind the list. A node switches to a list with more work behind it. AgentP compares this to the heaviest chain rule.
- **Version 2 of the protocol.** The active payout list is synced more often with the list of best shares. New miners can get a payout sooner, instead of waiting a full pool block.
- **Compact Share Relay.** Shares are cut down to just enough for other nodes to rebuild the proof: Slot-0 address, nonce, time and version. The aim is under 1200 bytes so a share fits in one UDP packet. AgentP described this as still untested.

Miners can join by pointing a DATUM client at AgentP's demo node, or by running their own GridPool node. Instructions are at gridpool.net.

## Early feedback

On 2026-06-25 AgentP recorded four pieces of feedback and the replies.

1. **Reward split.** Jason Hughes doubted that a large miner would give up 50% of the reward for their work, since on average it takes work worth a full block reward to find a block. Lotto-minded miners might try it. AgentP said this led to Version 2, the biggest change to GridPool in a while.
2. **Pool hopping.** Jungly, who maintains [Hydrapool](hydrapool.md), raised a classic problem. A miner can win a high-difficulty share, then leave and mine elsewhere. A large miner could earn many slots and go, leaving small miners to find a block that pays someone no longer working. A time limit on shares would punish honest miners who are still mining but less lucky. AgentP replied that the strategy does not seem to pay, because a miner holding extra slots gains most by finding the block itself. AgentP also promised to try to break it.
3. **Consensus.** Jungly called the approach loose consensus and recommended an explicit consensus protocol, as radpool used, if membership is known. AgentP answered that GridPool does have a consensus layer, the heaviest list rule, and that the rule also handles two cases:
   - *Latency.* A last-minute share can split the pool, with each half on a different list. The stronger list wins in time. Some work on the weaker side is lost.
   - *Censorship.* A miner that discards another miner's shares ends up on a lighter list. Its own shares then carry the wrong payout list and the rest of the network discards them. AgentP thought this holds even for a miner with 99% of the pool's hashrate, not just 51%, but said it needs to be gamed out more carefully.
4. **Evidence.** Another developer said many claims lacked supporting data, especially on network modelling, bandwidth and latency. AgentP agreed and put careful network testing high on the list, once more nodes are set up.

## The beta release

AgentP announced one-click packages on 2026-09-15.

- Install on Umbrel or StartOS, paste a payout address, and the node joins the GridPool network.
- The beta is SV2 only. AgentP asked people running Umbrel or Start9 with SV2 firmware to join.
- Package versions named in the post: v0.2.2-beta.7 for StartOS and v0.2.2-beta.9 for Umbrel.
- A main package for other server setups is published in the `gridlabs-science/boot-protocol` repository.

AgentP thanked the 256 Foundation Red Team, naming Schnitzel, for finding some key vulnerabilities that were fixed before release.

## A note on dates

The first post of the landing-page thread is stamped 2026-06-17 09:46:53 UTC. The raw file's header and file name carry a published date one day earlier.

## See Also

- [Hydrapool](hydrapool.md)
- [Running Your Own Hydrapool](running-hydrapool.md)
