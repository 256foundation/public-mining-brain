# HashScope

> Sources: 256 Foundation (HashScope README), collected 2026-10-07; 256 Foundation (HashScope documentation, Home), collected 2026-10-07; 256 Foundation (HashScope documentation, Overview), collected 2026-10-07; 256 Foundation (HashScope documentation, System Architecture), collected 2026-10-07; 256 Foundation (HashScope documentation, Quick Start), collected 2026-10-07; 256 Foundation (HashScope documentation, API Reference), collected 2026-10-07; 256 Foundation (HashScope documentation, Developer Guide), collected 2026-10-07; 256 Foundation (HashScope documentation, Contributing), collected 2026-10-07
> Raw: [HashScope README](../../raw/tools/github-256foundation-hashscope.md); [HashScope docs home](../../raw/tools/docs-hashscope.md); [HashScope overview](../../raw/tools/docs-hashscope-overview.md); [HashScope architecture](../../raw/tools/docs-hashscope-architecture.md); [HashScope quick start](../../raw/tools/docs-hashscope-quickstart.md); [HashScope API reference](../../raw/tools/docs-hashscope-api-reference.md); [HashScope developer guide](../../raw/tools/docs-hashscope-developer-guide.md); [HashScope contributing](../../raw/tools/docs-hashscope-contributing.md)
> Updated: 2026-10-07

## Overview

HashScope is a man-in-the-middle proxy for Bitcoin mining. It sits between miners and a pool, relays the Stratum traffic untouched, and captures, decodes and shows every message in a web UI in real time. It is a tool for debugging miners, understanding pool behaviour, and load testing pools. It also has a distributed [agent fleet](hashscope-agent-fleet.md) coordinated over Nostr. It is licensed MIT.

## What it is for

You point your miners at HashScope instead of at the pool. HashScope passes everything through and keeps a copy. The docs list these uses:

- Debugging miner connection issues.
- Understanding pool behaviour.
- Analyzing share submission patterns.
- Protocol debugging and development.
- Load testing mining pools with distributed agents.

## Architecture

The flow is: miners connect to the proxy, the proxy connects to the pool, and a copy of each message goes to capture, in-memory storage, the API server, and the web UI.

### Backend

The backend is a Python FastAPI application.

| Component | Job |
|-----------|-----|
| ProxyServer | Listens for miners on TCP port 3333 and creates one session per connection |
| ProxySession | One per miner. Connects to the upstream pool and relays both ways. Captures each message |
| StratumParser | Decodes Stratum v1 JSON-RPC messages. Best-effort: it never throws |
| CaptureStorage | An in-memory ring buffer, per session and global. Supports queries with filters and WebSocket subscriptions |
| FastAPI app | Starts the proxy in the background. Serves the REST endpoints and the WebSocket |

### Frontend

The web UI is React and TypeScript, built with Vite and the shadcn/ui component library. It has a session list, message filters, a live message table, a message detail view, and an agent status panel.

### The key principle

The relay is always transparent and never blocked by parsing or storage. A message is forwarded byte-for-byte right away. Parsing and storing happen in parallel. The project's rules for contributors follow from this:

1. Never modify message contents.
2. Parse errors must not crash the proxy.
3. Treat all input as untrusted.
4. Use type hints and strict TypeScript.
5. Nostr events must be signed.
6. Publishing to Nostr never blocks relaying.

Parse errors are normal. Not all pools use standard Stratum v1. Messages are still relayed correctly.

### Performance figures in the developer guide

- Relay overhead: <1ms.
- Parse overhead: ~0.1ms per message.
- WebSocket broadcast: <10ms to all clients.
- Memory use is bounded by the ring buffer size.

## Quick start

HashScope is Docker-first. You need Docker and Docker Compose, and an upstream pool.

1. Copy `env.example` to `.env` and set at least `POOL_HOST` and `POOL_PORT`.
2. Run `docker compose up -d`.
3. Point your miner at HashScope on port 3333.
4. Open http://localhost:3000 in a browser.

This starts three things:

| Service | Port |
|---------|------|
| Proxy server, for miners | 3333 |
| API server | 8000 |
| Web UI | 3000 |

### What the UI shows

- **Sessions panel.** Connected miners, connection times, and message counts. Click one to filter.
- **Messages table.** A live stream with direction badges, method names, parameters, parse status, timestamps and latency.
- **Message detail.** The decoded JSON, the raw bytes, and any parse error.
- **Filters.** Search, direction, session, and errors only.

## Configuration

All settings are environment variables.

| Variable | Default | Meaning |
|----------|---------|---------|
| `POOL_HOST` | none, required | Upstream pool hostname |
| `POOL_PORT` | `3333` | Upstream pool port |
| `LISTEN_PORT` | `3333` | Port miners connect to |
| `API_PORT` | `8000` | API server port |
| `CAPTURE_MAX_MESSAGES` | `50000` | Most messages kept in memory in total |
| `CAPTURE_MAX_PER_SESSION` | `10000` | Most messages kept per miner session |

Nostr and agent settings are covered in [HashScope Agent Fleet](hashscope-agent-fleet.md).

## API

The API is served at http://localhost:8000. Interactive documentation is at http://localhost:8000/docs.

| Endpoint | Purpose |
|----------|---------|
| `GET /api/sessions` | List all miner sessions |
| `GET /api/sessions/{id}` | One session |
| `GET /api/messages` | List captured messages. Optional filters: `session_id`, `direction`, `limit` |
| `GET /api/messages/{id}` | One message |
| `GET /api/agents` | All agents and their telemetry |
| `GET /api/config` | Current configuration, non-sensitive fields only |
| `WS /api/ws` | Real-time message stream as JSON |

The message `limit` defaults to 100. Direction can be miner to pool, pool to miner, or HashScope to pool.

## Technology

- Backend: Python 3.11+, FastAPI, asyncio, Pydantic, uvicorn, pytest.
- Frontend: React 18, TypeScript, Vite, shadcn/ui, Tailwind CSS.
- Infrastructure: Docker, docker-compose, nginx for serving the frontend.

Backend tests run with `docker compose run --rm backend pytest -q`.

## Roadmap

The contributing guide describes the project in phases:

- **Core Proxy.** Transparent proxy with real-time visualization.
- **Distributed Testing.** Agent fleet with Nostr coordination for load testing.
- **Future Enhancements.** Additional protocol support, persistent storage, authentication.

The developer guide lists matching extension points, including message routing rules, swapping the storage for a persistent one, and secondary Nostr relays.

## Troubleshooting

- **Miner cannot connect.** Check port 3333 is free and reachable. Check `POOL_HOST` and `POOL_PORT`. Read the backend logs.
- **No messages.** Make sure the miner points at HashScope, not at the pool.
- **UI shows disconnected.** The backend may still be starting. Wait 10-20 seconds. Check the browser console for WebSocket or CORS errors.

## See Also

- [HashScope Agent Fleet](hashscope-agent-fleet.md)
- [Hydrapool](../hydrapool/hydrapool.md)
- [Running Your Own Hydrapool](../hydrapool/running-hydrapool.md)
- [asic-rs](asic-rs.md)
