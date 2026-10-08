# Running Your Own Hydrapool

> Sources: Hydrapool project (GitHub README), collected 2026-10-07; 256 Foundation (hydrapool.org home page), collected 2026-10-07; Karpuzmining, jungly, econoalchemist (256 Foundation forum: Hydrapool on Umbrel), 2026-07-27
> Raw: [256foundation/hydrapool README](../../raw/hydrapool/github-256foundation-hydrapool.md); [hydrapool.org home](../../raw/hydrapool/hydrapool-org-home.md); [forum: Hydrapool on Umbrel](../../raw/hydrapool/2026-07-27-forum-hydrapool-on-umbrel.md)
> Updated: 2026-10-07

## Overview

Hydrapool is meant to be run by its users, not only by the foundation. This article covers how: the three ways to install it, the settings that matter, how to make room for the coinbase, the dashboards, the share-accounting API, upgrades, and the community work on an Umbrel app. For what Hydrapool is, see [Hydrapool](hydrapool.md).

## What you need

- A Bitcoin node that supports Bitcoin RPC, with ZMQ block notifications turned on.
- A Linux machine, a self-hosted computer or a VPS.
- Docker, for the simplest path.

The project site walks through one full example: an old Dell Optiplex 9020 desktop, Ubuntu Server 24.04.3 LTS, Bitcoin Core installed from Snap, and the Hydrapool Docker files. The example stores chain data on a 2TB auxiliary drive.

## Three ways to install

| Method | How | Notes |
|--------|-----|-------|
| Docker | Download `docker-compose.yml` and `config-example.toml` from the latest release, then `docker compose -f docker-compose.yml up` | Starts the pool and the monitoring containers together |
| Binaries | Run the `hydrapool-installer.sh` script from the releases page | Installs `hydrapool` and `hydrapool_cli`. Linux, Windows and MacOS binaries are provided. Docker is still recommended for the dashboard |
| Source | Clone the repository and run `cargo build --release` | Needs Rust at least 1.88.0 |

Docker images are signed. They can be verified with cosign.

With Docker, the Stratum server listens on port 3333 and the dashboard on port 3000.

## Settings that matter

### In config.toml

At the very least, edit `bitcoinrpc`, `zmqpubhashblock` and `network` to match your node. The network is signet or main. On main, change `bootstrap_address` too.

The site guide adds detail:

- **bootstrap_address.** Your own bitcoin address. A block found in the first 10-seconds or so after the server boots pays out here.
- **Donation.** Optional. A share of the block reward sent to any address. It is set in basis points, so 100 = 1%. Off by default.
- **Operator fee.** Optional. A share the operator keeps for running the server, also in basis points. Off by default.
- **pool_signature.** Can be changed from the default. Max 16 bytes.
- **RPC and ZMQ addresses.** When the node and Docker share a machine, use the special hostname `host.docker.internal`. The guide uses port 8332 for RPC on mainnet and port 28334 for ZMQ.
- Store, stratum, logging and api fields can stay on their defaults.

### In bitcoin.conf

The compose file runs Hydrapool on an isolated, bridged Docker network. The node must accept RPC from it. For Bitcoin Core on the same host that means binding RPC to all interfaces and allowing the Docker range:

- `rpcbind=0.0.0.0`
- `rpcallowip=172.16.0.0/12`

If the node is on a different host, point Hydrapool at that host. The node must allow RPC from the Docker host's IP address, because container traffic is NATed.

## Making room for the coinbase

Hydrapool pays miners straight from the coinbase, so the coinbase transaction is large. Bitcoin Core's default maximum block weight is 4,000,000 weight units. If regular transactions fill it, the block template can be rejected. The `blockmaxweight` setting reserves room.

| P2PKH outputs in coinbase | Suggested blockmaxweight |
|---------------------------|--------------------------|
| 20 | `3997000` |
| 100 | `3986000` |
| 200 | `3972500` |
| 500 | `3930000` |
| 1000 | `3860000` |

These figures assume standard P2PKH outputs. SegWit outputs need slightly less space.

### How many users

The README says the pool only accommodates up to 100 users for now, for coinbase and block weight reasons. Workers are limited only by hardware.

> **Status: Disputed**
> The README presents 100 users as a current limit. The hydrapool.org home page says Hydra Pool supports 100 unique users in the coinbase by default and that the user can configure this with the blockmaxweight instructions. The README's own table suggests values for up to 1000 outputs.

## Securing a public server

If the API server is reachable from outside, turn on authentication.

1. Generate credentials with `docker compose run --rm hydrapool-cli gen-auth <USERNAME> <PASSWORD>`.
2. Paste the resulting `auth_user` and `auth_token` lines into config.toml.
3. Put the same username and password into a custom `prometheus.yml`, then restart the prometheus service.
4. Put them into the healthcheck line of `docker-compose.yml`, then bring the stack up again.

By default Prometheus uses built-in credentials. A custom `prometheus.yml` overrides them.

For public dashboards and a public API, the README recommends nginx as a reverse proxy.

## Dashboards

Dashboards are built with Prometheus and Grafana.

- **Pool dashboard.** Pool hashrate, shares per second, the highest difficulty reached by any worker, users and workers over time, and how hashrate is split between users.
- **Users dashboard.** Stats for one user: total hashrate and each worker's hashrate, with a worker filter. A public version lists every user's address. A private version asks for the address first. The public one is the default.

## The API server

An API server starts with the pool, on the port set in the config file. Prometheus uses it to build the dashboards. Users use it to check the accounting.

- `/pplns_shares` downloads a JSON file of all PPLNS shares the pool tracks for distributing block rewards.
- It takes optional `start_time` and `end_time` parameters in RFC3339 format.
- `/health` is the health check the Docker setup uses.

## Upgrading

Pull the new images while the services are still running, then recreate the containers. Downtime is minimal.

Moving from v1.x.x to v2.x.x or higher is different. The database schema changed and needs a one-time reset: pull, bring the stack down with its volumes, and start again.

## Hydrapool on Umbrel

On 2026-07-27 a forum member, Karpuzmining, reported getting Hydrapool running as a native Umbrel app and mining to it with a Bitaxe. Karpuzmining asked whether to propose the work back to the main project or maintain it separately.

- Jungly, the Hydrapool maintainer, asked for a PR to the hydrapool repo. Building Umbrel images could then become part of the release tools.
- econoalchemist said the team had wanted an Umbrel/Start9 app but needed someone from the community to lead it.
- Karpuzmining planned to submit a PR once things were further along.

The thread does not say whether the PR was submitted.

## Small differences between the sources

- The README describes a private solo pool or a private PPLNS pool. The site describes a private solo pool or a public PPLNS pool.
- The README points to a mainnet instance at test.hydrapool.org. The site asks testers to use pool.256foundation.org on port 3333.
- The site's feature list says AGPLv3, like the README, but its opening sentence links the words open-source to a GPL 3.0 page.

## See Also

- [Hydrapool](hydrapool.md)
- [Hydrapool Hardware Tests](hydrapool-hardware-tests.md)
- [GridPool](gridpool.md)
- [HashScope](../tools/hashscope.md)
