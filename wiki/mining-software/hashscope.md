# HashScope

> Sources: 256foundation/HashScope README, AGENTS.md and docs site (captured 2026-10-07); 256foundation/HashScope GitHub issue #1 and PR #2 (2026-03-09)
> Raw: [HashScope README](../../raw/mining-software/256f-tools/github-256foundation-hashscope.md); [HashScope AGENTS.md](../../raw/mining-software/256f-tools/github-hashscope-agents.md); [HashScope docs: architecture](../../raw/mining-software/256f-tools/github-hashscope-docs-architecture.md); [HashScope docs: agent fleet](../../raw/mining-software/256f-tools/github-hashscope-docs-agent-fleet.md); [HashScope docs: API reference](../../raw/mining-software/256f-tools/github-hashscope-docs-api-reference.md); [HashScope docs: quick start](../../raw/mining-software/256f-tools/github-hashscope-docs-quickstart.md)
> Updated: 2026-10-09
> As-Of: 2026-10-09
> Status: Draft

## Overview

HashScope is a 256 Foundation tool for looking inside the conversation between a miner and its pool. It is a transparent man-in-the-middle (MITM) proxy: you point miners at HashScope instead of the pool, it relays every Stratum v1 byte unchanged to the real pool, and it captures, decodes and shows each JSON-RPC message in a web UI in real time ([README](../../raw/mining-software/256f-tools/github-256foundation-hashscope.md); [docs overview](../../raw/mining-software/256f-tools/github-hashscope-docs-overview.md)). A second component, the agent fleet, replays captured shares to a target pool from many machines, coordinated over Nostr, so you can load-test and compare a pool from several places at once ([agent fleet](../../raw/mining-software/256f-tools/github-hashscope-docs-agent-fleet.md)). It is MIT licensed, copyright 2024 256 Foundation ([README](../../raw/mining-software/256f-tools/github-256foundation-hashscope.md)). The project assumes you have authorization to load-test your own pool ([AGENTS.md](../../raw/mining-software/256f-tools/github-hashscope-agents.md)).

## What it is for

The docs list these uses ([docs overview](../../raw/mining-software/256f-tools/github-hashscope-docs-overview.md)):

- Debugging miner connection issues.
- Understanding pool behaviour.
- Analysing share-submission patterns.
- Protocol debugging and development.
- Load-testing pools with distributed agents.

Practical recipes from the quick start ([quick start](../../raw/mining-software/256f-tools/github-hashscope-docs-quickstart.md)):

| Goal | What to look at |
|---|---|
| Debug a connection | Filter to the miner's session, look for pool error responses, check the authorization messages |
| Mining efficiency | `mining.notify` frequency, `mining.submit` responses, difficulty changes |
| Pool behaviour | Pool → Miner messages, job-notification patterns, pool response times |
| Protocol issues | "Show Errors Only", parse errors in the detail panel, raw bytes |

Parse errors are normal: not all pools speak standard Stratum v1, and messages are still relayed correctly ([quick start](../../raw/mining-software/256f-tools/github-hashscope-docs-quickstart.md)).

## Architecture

The core rule: the relay is always transparent and is never blocked by parsing, storage or Nostr publishing. Each message is forwarded byte-for-byte first; parsing and storage happen in parallel, and parse errors are stored and displayed without interrupting the relay ([architecture](../../raw/mining-software/256f-tools/github-hashscope-docs-architecture.md); [AGENTS.md](../../raw/mining-software/256f-tools/github-hashscope-agents.md)).

**Backend (Python, FastAPI, asyncio)** ([architecture](../../raw/mining-software/256f-tools/github-hashscope-docs-architecture.md)):

| Component | Role |
|---|---|
| `ProxyServer` | Listens on TCP :3333, creates one `ProxySession` per miner connection |
| `ProxySession` | Opens its own upstream pool connection, relays both directions as asyncio tasks, captures each message |
| `StratumParser` | Best-effort JSON-RPC decoding that never throws |
| `CaptureStorage` | In-memory ring buffer, per session and global, with filtered queries and WebSocket subscriptions |
| FastAPI app | Starts the proxy in the background, serves REST and WebSocket, CORS middleware |

**Frontend:** React 18 with TypeScript, Vite, shadcn/ui and Tailwind; live updates over WebSocket; served by nginx in Docker ([developer guide](../../raw/mining-software/256f-tools/github-hashscope-docs-developer-guide.md)). Panels: session list, message filters, live message table, message detail, and agent fleet status ([architecture](../../raw/mining-software/256f-tools/github-hashscope-docs-architecture.md)).

**Stated performance:** relay overhead <1ms, parse overhead ~0.1ms per message, WebSocket broadcast <10ms, memory bounded by the ring buffer ([developer guide](../../raw/mining-software/256f-tools/github-hashscope-docs-developer-guide.md)). These are design figures from the docs, not published benchmarks.

Contributor rules that follow from the design ([developer guide](../../raw/mining-software/256f-tools/github-hashscope-docs-developer-guide.md); [AGENTS.md](../../raw/mining-software/256f-tools/github-hashscope-agents.md)): never modify message contents; parse errors must not crash the proxy; treat all miner and pool data as untrusted; sign every Nostr event; publishing to Nostr never blocks relaying.

## Quick start and configuration

1. Copy `env.example` to `.env` and set at least `POOL_HOST` and `POOL_PORT` (or export them) ([README](../../raw/mining-software/256f-tools/github-256foundation-hashscope.md); [quick start](../../raw/mining-software/256f-tools/github-hashscope-docs-quickstart.md)).
2. Run `docker compose up -d`. This starts the proxy on port 3333, the API on port 8000 (interactive docs at `/docs`) and the web UI on port 3000 ([README](../../raw/mining-software/256f-tools/github-256foundation-hashscope.md)).
3. Point miners at `stratum+tcp://localhost:3333` (or the host running HashScope) instead of the pool ([quick start](../../raw/mining-software/256f-tools/github-hashscope-docs-quickstart.md)).
4. Open the UI at `http://localhost:3000`. If it shows "Disconnected", the backend may still be starting (the docs say wait 10-20 seconds) or there may be CORS errors in the browser console ([quick start](../../raw/mining-software/256f-tools/github-hashscope-docs-quickstart.md)).

Core settings, all environment variables ([README](../../raw/mining-software/256f-tools/github-256foundation-hashscope.md)):

| Variable | Default | Meaning |
|---|---|---|
| `POOL_HOST` | none (required) | Upstream pool, e.g. `stratum+tcp://your-pool.com` |
| `POOL_PORT` | `3333` | Upstream pool port |
| `LISTEN_HOST` / `LISTEN_PORT` | `0.0.0.0` / `3333` | Where miners connect |
| `API_HOST` / `API_PORT` | `0.0.0.0` / `8000` | API server |
| `CAPTURE_MAX_MESSAGES` | `50000` | Total messages held in memory |
| `CAPTURE_MAX_PER_SESSION` | `10000` | Messages held per miner session |

Captures live only in memory; SQLite is optional future work ([AGENTS.md](../../raw/mining-software/256f-tools/github-hashscope-agents.md)). Backend tests run with `docker compose run --rm backend pytest -q` ([README](../../raw/mining-software/256f-tools/github-256foundation-hashscope.md)).

## API

Base URL `http://localhost:8000` ([API reference](../../raw/mining-software/256f-tools/github-hashscope-docs-api-reference.md)):

| Endpoint | Returns |
|---|---|
| `GET /api/sessions` | All miner sessions: peer, first/last seen, message count, per-direction and parse-error stats |
| `GET /api/sessions/{id}` | One session |
| `GET /api/messages` | Captured messages; filters `session_id`, `direction`, `limit` (default 100) |
| `GET /api/messages/{id}` | One message |
| `GET /api/agents` | Agent fleet telemetry |
| `GET /api/config` | Current non-sensitive configuration |
| `WS /api/ws` | Live stream; each push is a message object in the REST format |

Each captured message records an id, receive and forward timestamps (`ts_recv`, `ts_fwd`), direction, session, peer, raw bytes, decoded JSON-RPC, `parse_error` and size in bytes ([developer guide](../../raw/mining-software/256f-tools/github-hashscope-docs-developer-guide.md); [API reference](../../raw/mining-software/256f-tools/github-hashscope-docs-api-reference.md)). The gap between `ts_recv` and `ts_fwd` is the proxy's own added latency.

## The agent fleet over Nostr

The fleet turns one real miner's shares into a multi-location pool test ([agent fleet](../../raw/mining-software/256f-tools/github-hashscope-docs-agent-fleet.md); [AGENTS.md](../../raw/mining-software/256f-tools/github-hashscope-agents.md)):

1. The proxy sees a real miner's `mining.submit`.
2. In a background task it publishes a signed **ShareEvent** to a Nostr relay.
3. Agents hold push (WebSocket REQ) subscriptions filtered by tags, so they receive it at once, with no polling.
4. Each agent, already connected to the target pool as a normal Stratum client (`mining.subscribe`, `mining.authorize`), submits the share and records accept/reject and latency.
5. Agents publish **TelemetryEvents** (shares received, submits attempted/accepted/rejected, last submit latency, connection state); the proxy subscribes, aggregates, and serves them to the UI.

The relay is external and not part of docker-compose; self-hosting is preferred ([AGENTS.md](../../raw/mining-software/256f-tools/github-hashscope-agents.md)). Events are tagged `t=hashscope`, `run=<RUN_ID>` and `type=share` or `type=telemetry`. `RUN_ID` isolates concurrent test runs and must match on the proxy and every agent ([AGENTS.md](../../raw/mining-software/256f-tools/github-hashscope-agents.md)).

Running a test ([agent fleet](../../raw/mining-software/256f-tools/github-hashscope-docs-agent-fleet.md)):

- Set `NOSTR_ENABLED=true`, `NOSTR_RELAY_URL` and `RUN_ID` in `.env`, plus the agent's worker name and password.
- Start the proxy and UI, then scale agents with `docker compose up -d --scale agent=N`.
- Connect a miner, open the UI, and switch "Broadcast to Agents" on for that session in the Sessions panel; broadcasting is per session.
- Monitor in the Agent Fleet panel, via `/api/agents`, or with `docker compose logs -f agent`.

Resilience: relay reconnects use exponential backoff capped at ~30s and resubscribe with `since` set to slightly before the last seen event (e.g. 10s overlap); agents redo the Stratum handshake if the pool drops; ShareEvent publishing queues up to a limit and drops the oldest if the relay is down; a ShareEvent is a notification, not a guarantee ([AGENTS.md](../../raw/mining-software/256f-tools/github-hashscope-agents.md)).

Security notes ([agent fleet](../../raw/mining-software/256f-tools/github-hashscope-docs-agent-fleet.md)): keep Nostr private keys secret (auto-generated ones are ephemeral); use a unique `RUN_ID` per test; public relays expose events publicly, so use a self-hosted relay for sensitive tests; agents authenticate to pools like normal miners. A public relay will also expect rate limits ([AGENTS.md](../../raw/mining-software/256f-tools/github-hashscope-agents.md)).

## Known inconsistencies in the docs

The README, AGENTS.md and docs site do not fully agree. Check the repo's `env.example` and code before relying on any of these:

> **Status: Disputed** — ShareEvent kind
> The README's configuration table gives `NOSTR_KIND_SHARE` a default of `30080` ([README](../../raw/mining-software/256f-tools/github-256foundation-hashscope.md)); AGENTS.md and the agent-fleet doc use 30078 ([AGENTS.md](../../raw/mining-software/256f-tools/github-hashscope-agents.md); [agent fleet](../../raw/mining-software/256f-tools/github-hashscope-docs-agent-fleet.md)). All three agree telemetry is 30079. AGENTS.md says exact kind numbers are an implementation choice. Best assessment: unknown without the code; a proxy and agents built from different docs would not hear each other.

- **Agent environment variable names.** The README lists `WORKER_NAME`, `WORKER_PASSWORD` and `TELEMETRY_INTERVAL_SEC`; the agent-fleet doc uses `AGENT_`-prefixed names (`AGENT_POOL_HOST`, `AGENT_WORKER_NAME`, `AGENT_RUN_ID`, `AGENT_NOSTR_RELAY_URL`) ([README](../../raw/mining-software/256f-tools/github-256foundation-hashscope.md); [agent fleet](../../raw/mining-software/256f-tools/github-hashscope-docs-agent-fleet.md)).
- **Proxy secret key.** README: `NOSTR_SK`; AGENTS.md: `MITM_NOSTR_SK` ([README](../../raw/mining-software/256f-tools/github-256foundation-hashscope.md); [AGENTS.md](../../raw/mining-software/256f-tools/github-hashscope-agents.md)).
- **Is `RUN_ID` required?** The README lists it as auto-generated but required when Nostr is enabled; AGENTS.md lists it as required ([README](../../raw/mining-software/256f-tools/github-256foundation-hashscope.md); [AGENTS.md](../../raw/mining-software/256f-tools/github-hashscope-agents.md)).
- **Service name.** Scaling and logs use `agent` in the agent-fleet doc, but the README and developer guide use `agents` (`docker compose logs -f agents`, `docker compose build agents`) ([agent fleet](../../raw/mining-software/256f-tools/github-hashscope-docs-agent-fleet.md); [README](../../raw/mining-software/256f-tools/github-256foundation-hashscope.md)).
- **Message directions.** AGENTS.md defines two (`miner_to_pool`, `pool_to_miner`); the developer guide and API reference add `hashscope_to_pool` ([AGENTS.md](../../raw/mining-software/256f-tools/github-hashscope-agents.md); [API reference](../../raw/mining-software/256f-tools/github-hashscope-docs-api-reference.md)).
- **Telemetry tags.** AGENTS.md requires a `type=telemetry` tag; the agent-fleet doc's telemetry example lists only `t`, `run` and `agent` ([AGENTS.md](../../raw/mining-software/256f-tools/github-hashscope-agents.md); [agent fleet](../../raw/mining-software/256f-tools/github-hashscope-docs-agent-fleet.md)).
- **Dev server command.** AGENTS.md runs `uvicorn hashscope.api.app:app`; the developer guide uses `hashscope.api.app:create_app --factory` ([AGENTS.md](../../raw/mining-software/256f-tools/github-hashscope-agents.md); [developer guide](../../raw/mining-software/256f-tools/github-hashscope-docs-developer-guide.md)).

## History

- The README and docs carry a 2024 copyright, and the README labels the Nostr agent features "Iteration 2" ([README](../../raw/mining-software/256f-tools/github-256foundation-hashscope.md)).
- 2026-03-09: issue #1 reported frontend display overflow, and PR #2 proposed a fix the same day; the author said the change was written with Claude and tested locally. Both were still open at capture ([issue #1](../../raw/mining-software/256f-tools/2026-03-09-github-hashscope-issue-1-frontend-display-overflows.md); [PR #2](../../raw/mining-software/256f-tools/2026-03-09-github-hashscope-pr-2-fix-don-t-overflow-so-much.md)).
- Future work named in the docs: message routing rules, swappable persistent storage, authentication middleware, a transform step before forwarding, and secondary Nostr relays ([developer guide](../../raw/mining-software/256f-tools/github-hashscope-docs-developer-guide.md)).

## See Also

- Same topic: [asic-rs and the Fleet-Tooling Stack](asic-rs.md)
- [Stratum in Practice](../protocols/stratum-in-practice.md)
- [Decentralized Pool Designs](../protocols/decentralized-pool-designs.md)
- [Hydrapool](../pools/hydrapool.md)
- [Public Pool](../pools/public-pool.md)
- [Pool Choice for Heat Miners](../pools/pool-choice-for-heat-miners.md)
- [Bitaxe Troubleshooting](../getting-started/bitaxe-troubleshooting.md)
