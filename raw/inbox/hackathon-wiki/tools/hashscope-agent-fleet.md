# HashScope Agent Fleet

> Sources: 256 Foundation (HashScope documentation, Agent Fleet & Nostr), collected 2026-10-07; 256 Foundation (HashScope README), collected 2026-10-07
> Raw: [HashScope agent fleet](../../raw/tools/docs-hashscope-agent-fleet.md); [HashScope README](../../raw/tools/github-256foundation-hashscope.md)
> Updated: 2026-10-07

## Overview

The agent fleet is the load-testing side of [HashScope](hashscope.md). When a real miner submits a share through the HashScope proxy, the proxy publishes that share as an event on a Nostr relay. Agents anywhere in the world are subscribed to the relay. Each one receives the event, submits the share to a target pool, and reports back how it went. The result is a view of how a pool behaves from many places at once.

## Why Nostr

The relay acts as a pubsub layer between the proxy and the agents.

- **Push, not polling.** Agents hold a WebSocket subscription and get share events at once.
- **Decentralized coordination.** The proxy and the agents only need to reach the same relay.
- **Horizontal scaling.** Add agents with `docker compose up -d --scale agent=N`.
- **Geographic spread.** Agents can run in many regions to test pool performance and latency.
- **Isolated runs.** A `RUN_ID` keeps concurrent tests from hearing each other.

## The flow

1. The proxy captures a real miner's share submission.
2. The proxy publishes a ShareEvent to the relay. This runs in the background and does not block the relay of mining traffic.
3. Agents receive the ShareEvent through their subscriptions.
4. Each agent submits the share to its target pool and records the result.
5. Each agent publishes a TelemetryEvent back to the relay.
6. The proxy subscribes to telemetry and serves it to the web UI through its local API.

## The two events

| Event | Direction | Tags | Content |
|-------|-----------|------|---------|
| ShareEvent | Proxy to agents | `hashscope`, the run ID, and type `share` | JSON with the Stratum `mining.submit` details |
| TelemetryEvent | Agents to proxy | `hashscope`, the run ID, and the agent ID | JSON with agent stats |

Each event type uses a custom Nostr event kind, set by `NOSTR_KIND_SHARE` and `NOSTR_KIND_TELEMETRY`. The telemetry kind is 30079 in both sources.

> **Status: Disputed**
> The agent fleet documentation gives 30078 as the example value for `NOSTR_KIND_SHARE`. The README's configuration table gives its default as `30080`. Check `env.example` in the repository before relying on either.

## What an agent is

An agent is a small Python program with two clients:

- **A pool client.** A full Stratum client. It connects to the target pool, does the handshake and authorization, and submits shares the way a real miner would.
- **A Nostr client.** It keeps a persistent subscription to the relay. It reconnects by itself and catches up on events missed while disconnected.

Agents report health, connection status, submission statistics, latency and errors at a set interval.

## Settings

| Variable | Default | Meaning |
|----------|---------|---------|
| `NOSTR_ENABLED` | `false` | Turns the agent features on |
| `NOSTR_RELAY_URL` | none | Relay WebSocket URL. Required when Nostr is enabled |
| `RUN_ID` | auto-generated | Must be the same for the proxy and all agents. Required when Nostr is enabled |
| `NOSTR_SK` | auto-generated | The proxy's Nostr private key, hex-encoded. Save it from the logs to keep it |
| `WORKER_NAME` | `hashscope_agent` | Worker name for pool authentication. Agents add a random suffix to stay unique |
| `WORKER_PASSWORD` | `x` | Worker password, if the pool needs one |
| `TELEMETRY_INTERVAL_SEC` | `5` | Seconds between telemetry events |

## Running a test

1. Set the Nostr variables in `.env`.
2. Start the system with Docker Compose.
3. Connect a miner to the proxy on port 3333.
4. Open the UI on port 3000.
5. In the Sessions panel, switch Broadcast to Agents on.

Agents then receive share events and submit them to the target pool. Watch them in the Agent Fleet panel, through `/api/agents` on port 8000, or with `docker compose logs -f agent`.

## Security notes

- Keep Nostr private keys secret. Auto-generated keys are ephemeral.
- Use a unique `RUN_ID` for each test.
- Public relays expose events publicly. Use a self-hosted relay for sensitive tests.
- Agents authenticate with target pools like normal miners.

## Troubleshooting

- **Agents get no shares.** Check that `RUN_ID` matches on the proxy and the agents. Check the relay is reachable. Check that broadcast is on for the session.
- **Agents cannot reach the pool.** Check pool host and port, worker name and password, and the agent logs.
- **No telemetry in the UI.** Check the agents are running and can reach the relay. Refresh the page.

## Gaps in the collected docs

The agent fleet page was collected without its code blocks. The Configuration, Scaling Agents and environment sections are headings with nothing under them. The settings above come from the README.

## See Also

- [HashScope](hashscope.md)
- [Hydrapool](../hydrapool/hydrapool.md)
