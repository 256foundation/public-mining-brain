# Agent Fleet & Nostr - HashScope Documentation

> Source: https://256foundation.github.io/HashScope/agent-fleet
> Collected: 2026-10-07
> Published: Unknown

# Distributed Agent Fleet[¶](https://256foundation.github.io#distributed-agent-fleet)

## Overview[¶](https://256foundation.github.io#overview)

The distributed agent fleet enables load testing and pool analysis across multiple geographic locations. Agents receive share events via a Nostr relay and submit them to target pools independently.

### Key Features[¶](https://256foundation.github.io#key-features)

- **Push-based Architecture**: Agents subscribe to share events via WebSocket (no polling)
- **Decentralized Coordination**: Nostr relay acts as pubsub for event distribution
- **Real-time Telemetry**: Agents report status, latency, and accept/reject ratios
- **Horizontal Scaling**: Add agents with `docker compose up -d --scale agent=N`
- **Geographic Distribution**: Deploy agents worldwide to test pool performance
- **Isolated Test Runs**: `RUN_ID` ensures no cross-talk between concurrent tests

## Architecture[¶](https://256foundation.github.io#architecture)

The system uses Nostr relay as a coordination layer:

```
graph TB
    Miner[Real Miner] --> MITM[MITM Proxy]
    MITM --> Pool[Mining Pool]
    MITM -->|Publish ShareEvent| Relay[Nostr Relay<br/>WebSocket PubSub]
    Relay -->|Subscribe ShareEvent| Agent1[Agent 1]
    Relay -->|Subscribe ShareEvent| Agent2[Agent 2]
    Relay -->|Subscribe ShareEvent| AgentN[Agent N]
    Agent1 -->|Submit Share| PoolTarget1[Target Pool]
    Agent2 -->|Submit Share| PoolTarget2[Target Pool]
    AgentN -->|Submit Share| PoolTargetN[Target Pool]
    Agent1 -->|Publish Telemetry| Relay
    Agent2 -->|Publish Telemetry| Relay
    AgentN -->|Publish Telemetry| Relay
    Relay -->|Subscribe Telemetry| MITM
    MITM -->|Display Stats| UI[Web UI]
```
1. **MITM** captures real miner's share submissions
2. **MITM** publishes **ShareEvent** to Nostr relay (background, non-blocking)
3. **Agents** maintain WebSocket subscriptions to relay
4. **Agents** receive ShareEvent immediately (push, no polling)
5. **Agents** submit to target pool and record results
6. **Agents** publish **TelemetryEvent** back to relay
7. **MITM** subscribes to telemetry and exposes via local API to UI

### Event Schemas[¶](https://256foundation.github.io#event-schemas)

#### ShareEvent (MITM → Agents)[¶](https://256foundation.github.io#shareevent-mitm-agents)

Nostr event with:
- **Kind**: `NOSTR_KIND_SHARE` (e.g., 30078)
- **Tags**: `["t", "hashscope"]`, `["run", "<RUN_ID>"]`, `["type", "share"]`
- **Content**: JSON with Stratum `mining.submit` details

#### TelemetryEvent (Agents → MITM)[¶](https://256foundation.github.io#telemetryevent-agents-mitm)

Nostr event with:
- **Kind**: `NOSTR_KIND_TELEMETRY` (e.g., 30079)
- **Tags**: `["t", "hashscope"]`, `["run", "<RUN_ID>"]`, `["agent", "<AGENT_ID>"]`
- **Content**: JSON with agent stats

## Configuration[¶](https://256foundation.github.io#configuration)

### MITM Proxy Settings[¶](https://256foundation.github.io#mitm-proxy-settings)

### Agent Settings[¶](https://256foundation.github.io#agent-settings)

## Quick Start[¶](https://256foundation.github.io#quick-start)

### 1. Configure Environment[¶](https://256foundation.github.io#1-configure-environment)

Create `.env` file:

### 2. Start the System[¶](https://256foundation.github.io#2-start-the-system)

### 3. Enable Broadcasting[¶](https://256foundation.github.io#3-enable-broadcasting)

1. Connect a miner to `localhost:3333`
2. Open UI at `http://localhost:3000`
3. In Sessions panel, toggle "Broadcast to Agents" to ON
4. Agents will now receive share events and submit to target pool

### 4. Monitor Agents[¶](https://256foundation.github.io#4-monitor-agents)

- **UI**: Check "Agent Fleet" panel for status
- **API**: `curl http://localhost:8000/api/agents | jq`
- **Logs**: `docker compose logs -f agent`

## Security Notes[¶](https://256foundation.github.io#security-notes)

- Keep Nostr private keys secret (auto-generated are ephemeral)
- Use unique `RUN_ID` per test to prevent cross-talk
- Public relays expose events publicly - use self-hosted relay for sensitive tests
- Agents authenticate with target pools like normal miners

## Scaling Agents[¶](https://256foundation.github.io#scaling-agents)

## Troubleshooting[¶](https://256foundation.github.io#troubleshooting)

### Agents not receiving shares[¶](https://256foundation.github.io#agents-not-receiving-shares)

- Check `RUN_ID` matches between MITM and agents
- Verify Nostr relay is accessible
- Check MITM logs for ShareEvent publishing
- Ensure broadcast is enabled for session in UI

### Agents not connecting to pool[¶](https://256foundation.github.io#agents-not-connecting-to-pool)

- Check pool host and port configuration
- Verify worker name and password
- Check agent logs for connection errors

### No telemetry in UI[¶](https://256foundation.github.io#no-telemetry-in-ui)

- Check agents are running: `docker compose ps`
- Verify Nostr relay connectivity
- Check browser console for errors
- Refresh UI page
