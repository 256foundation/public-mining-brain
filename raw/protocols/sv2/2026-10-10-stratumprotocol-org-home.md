# Stratum V2 — stratumprotocol.org (homepage)

> Source: https://stratumprotocol.org
> Collected: 2026-10-10
> Published: 2026-10-10 (site ongoing; protocol v1 2012, SV2 since 2019)
> Registry ID: stratum-v2

Stratum V2 is a mining protocol that makes mining operations more efficient, profitable, secure, private and decentralized.
Start Mining  (#start-mining-steps)

## Why Stratum V2?

Stratum V2 (SV2) upgrades the Stratum mining protocol (SV1), which was introduced in 2012, back when mining was largely for hobbyists. SV2 is engineered for modern mining, eliminating SV1's inefficiencies. Designed by Jan Čapek and Pavel Moravec, together with Matt Corallo, SV2 is now maintained by an independent open source community.

### ~70% less bandwidth

Reduction for pools and miners

SV1's JSON messages are bandwidth heavy, while SV2 uses a lean binary format, lowering CPU load and cutting bandwidth use by about 60% for pools and 70% for miners, reducing operating costs for the pool, and helping bandwidth-constrained miners run more reliably.

### Security

Protecting profit

Stratum V2 secures miner to pool traffic with encryption and authentication. This prevents man in the middle attack that hijacks hashrate by swapping pool credentials and redirects work. Encrypted transport also makes traffic far harder to inspect or tamper with by ISPs, or attackers carrying out large scale routing attacks. SV2 increases transparency and eliminates out of band payments by allowing miners themselves to construct block templates.

### Up to 7.4% profit increase

Proven in real-world deployments

Stratum V2's technical upgrades translate into measurable profitability gains. Faster template delivery and lower latency reduce wasted work and capture more transaction fees per block, and combined with improvements like end-to-end encryption and faster block propagation can increase profits by up to 7.4%. Read the case study → (https://stratumprotocol.org/blog/hashlabs)

### Privacy Improvements

Prevent ISP surveillance

Stratum V2 encrypts mining traffic, preventing Internet Service Provider (ISP) and other network intermediaries from observing plaintext shares and messages. In Stratum V1, this data can be used to infer a miner's hashrate and roughly estimate earnings based on that hashrate.

### Transaction Selection

Miners choose what goes in blocks

A few mining pools now dominate Bitcoin's block space, with some acting as proxies for others. Pools can selectively include or exclude transactions, creating censorship risk. Stratum V2 empowers miners to build their own block templates, shifting them from passive hashers to active participants in securing Bitcoin's censorship resistance.

### Flexibility

Modular architecture

A free, open-source, modular infrastructure with permissive license, empowering developers to build and innovate. A composable design lets you adopt only the components you need. Integrate gradually without disrupting existing infrastructure, and extend functionality as requirements evolve.

### Compatibility

No need to upgrade firmware

Translation proxies allow SV2 pools to accept connections from legacy SV1 firmware. Upgrade your infrastructure incrementally while maintaining full backward compatibility.

### Interoperable & Neutral

Community-driven governance

Community-driven governance and clear specifications ensure interoperability, preventing vendor lock-ins and fragmentation. Specifications are maintained by an independent working group anyone can join to help accelerate an open-standard for mining.

Miner

10110101

00110011

11100101

Pool

STRATUM V2

Miner

{"method":"mining.submit"}

{"id":42, "params":[...]}

{"error":null}

{"jsonrpc": "2.0"}

{"difficulty": 1024}

{"worker":"full_node_1"}

{"job_id":"0x83a..."}

Pool

STRATUM V1

Miner

Pool

STRATUM V2

Miner

{"method":"mining.authorize"}

 {"params":["user","pass"]}

{"id":1}

{"jsonrpc": "2.0"}

{"result":true}

{"worker":"worker1"}

{"job_id":"0x83a..."}

Pool

STRATUM V1

Share Acceptance Rate

99.8%

SV1

99.91%

SV2

100%

SV2 + JD

Near-zero stale shares with Job Declaration

Job Latency

228ms

SV1

57.7ms

SV2

2.44ms

SV2 + JD

Job latency impacts how fast the new job is received from the Pool

Block Propagation Time

96.3ms

SV1

3.44ms

SV2 + JD

28× faster block propagation

ISP

Miner

Pool

Stratum V2

Miner

Block

Pool

Block

Miner selects transactions and builds the block

Stratum V1

Miner

Block

Pool

Block

Pool controls transaction selection and block construction

Job Declaration

Template Distribution

Mining Protocol

SV1

Proxy

SV2

TRANSLATION PROXY

#### Working Group Members

[img: Antpool]  [img: Antpool]   (https://www.antpool.com/) [img: Auradine]   (https://auradine.com/) [img: Block]  [img: Block]   (https://block.xyz/) [img: Braiins]   (https://braiins.com/) [img: DMND]   (https://www.dmnd.work/) [img: F2Pool]  [img: F2Pool]   (https://www.f2pool.com/) [img: Foundry]  [img: Foundry]   (https://foundrydigital.com/) [img: MARA Foundation]  [img: MARA Foundation]   (https://foundation.mara.com/) [img: mempool.space]  [img: mempool.space]   (https://mempool.space/) [img: Spiderpool]  [img: Spiderpool]   (https://www.spiderpool.com/) [img: Spiral]  [img: Spiral]   (https://spiral.xyz/)
View Specifications → (https://stratumprotocol.org/specification/)

## Mine with SV2 UI

Monitor your mining fleet in one place.Solo mine with your node or via a pool.Pool mine with any SV2-compatible pool.Works with existing SV1 firmware. No upgrade required.

[img: SV2 dashboard interface showing stratum endpoint, hashrate metrics, chart, and worker table]  [img: SV2 dashboard interface showing stratum endpoint, hashrate metrics, chart, and worker table]

### Install SV2 UI App

If you own an Umbrel node or run umbrelOS, install the SV2 UI App from the Umbrel App Store.

Install from App Store  (https://apps.umbrel.com/app/sv2-ui)

1 Download & Install Docker Download  (https://www.docker.com/products/docker-desktop/)

2 Run the container

docker run --rm \ --name sv2-ui \ -p 8080:8080 \ -e HOST_HOME=$HOME \ -v /var/run/docker.sock:/var/run/docker.sock \ -v sv2-config:/app/data/config \ stratumv2/sv2-ui:latest

3 Open the UI Open  (http://localhost:8080/)

Open locally at http://localhost:8080/ (http://localhost:8080/)

Custom Template Creation Coming Soon

Custom template creation on Windows is not yet supported. Progress is tracked in bitcoin-core/libmultiprocess#231 (https://github.com/bitcoin-core/libmultiprocess/pull/231).

## Building blocks for innovation

Reduce complexity, vertically integrate, and build applications more efficiently with our open, thoroughly documented protocol and reference implementation, libraries and even applications. Build a proxy, mining monitoring software, a pool or efficient firmware.

Stratum V2

Rust Libraries  (https://github.com/stratum-mining/stratum)

Reference Implementation  (https://github.com/stratum-mining)

Reference Applications  (https://github.com/stratum-mining/sv2-apps)

Language Bindings  (https://github.com/stratum-mining/sv2-uniffi)

Docker Support  (https://hub.docker.com/u/stratumv2)

Clear Specification  (/specification/)

## SV2 Adoption

Tested and deployed by industry leaders across hardware, firmware, and pool infrastructure.

### Hardware & Firmware

[img: Auradine]

Auradine SV2 native support across all ASICs via FluxOS
 (https://velaura.ai/products/)
[img: Bitaxe]

Bitaxe Native Stratum V2 firmware support
 (https://github.com/bitaxeorg/ESP-Miner/releases)
[img: BraiinsOS]

BraiinsOS Native Stratum V2 firmware support
 (https://braiins.com/os-firmware)
[img: Mujina]

Mujina Work in progress towards SV2 support
 (https://mujina.org/)
[img: NerdAxe]  [img: NerdAxe]

NerdAxe Native Stratum V2 firmware support
 (https://github.com/shufps/ESP-Miner-NerdQAxePlus/releases)
[img: Proto]

Proto, Block Inc. Work in progress towards SV2 support
 (https://github.com/block/proto-fleet/pull/81)

### Pools

[img: Blitzpool]

Blitzpool In production solo pool
 (https://blitzpool.yourdevice.ch/)
[img: Braiins Pool]

Braiins Pool In production pool
 (https://braiins.com/pool)
CK

CKPool In production solo pool
 (https://solo.ckpool.org)
[img: DMND]

DMND In production pool, enabling miner selected templates
 (https://www.dmnd.work/)
[img: NexusPool]

NexusPool In production solo pool
 (https://nexuspool.io/)
[img: Public Pool]

Public Pool In production solo pool
 (https://web.public-pool.io/#/)
[img: PyBlock Pool]

PyBlock Pool In production solo pool
 (https://pyblock.xyz:8443)

[img: SRI Community Pool]

SRI Community Pool Solo & pool mining with custom templates, testing only

### Software & Research

[img: Braiins Hashrate]

Braiins Hashrate Hashrate marketplace supporting SV2-compatible pools
 (https://hashpower.braiins.com/)
[img: Hashlabs]

Hashlabs Site of the head-to-head V1 vs V2 test
 (https://www.hashlabs.io/)
[img: Pluto Mining]

Pluto Mining Working on mining management software implementing SV2 compatibility
 (https://www.plutomining.io/)
[img: StarkWare]

StarkWare Developed a zero-knowledge-proof prototype built on Stratum V2
 (https://x.com/AbdelStark/status/1935354385795592491)
[img: Umbrel]

Umbrel Stratum V2 UI app supported
 (https://apps.umbrel.com/app/sv2-ui)

Running SV2? Tell us on Discord → (https://discord.gg/fsEW23wFYs)

## Support for Stratum V2

### About the Working Group

The Stratum V2 Working Group is community-governed and independent of any single entity. We foster ecosystem collaboration to drive permissionless innovation in Bitcoin mining.

View Specifications  (https://stratumprotocol.org/specification)

## Community

Community-driven governance and specifications ensure interoperability, so teams can focus on innovating instead of patching incompatibilities.

### GitHub

Free and open-source Stratum V2 implementation developed as a public good by industry contributors. Built in Rust with bindings for other languages, plus libraries and applications you can build on.

EXPLORE CODEBASE

 (https://github.com/stratum-mining/)

### Discord Community

The heart of our discussion. Join developers and miners to discuss proposals, get support, and collaborate.

 (https://discord.gg/fsEW23wFYs)

### Follow Updates

Latest news, threads, and ecosystem announcements.

 (https://x.com/StratumV2)
