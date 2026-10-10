# System Architecture - HashScope Documentation

> Source: https://256foundation.github.io/HashScope/architecture
> Collected: 2026-10-07
> Published: Unknown

# Architecture Overview[¶](https://256foundation.github.io#architecture-overview)

## System Architecture[¶](https://256foundation.github.io#system-architecture)

HashScope consists of multiple components working together to capture and visualize mining traffic:

```
graph TB
    Miner1[Miner 1] --> Proxy[HashScope Proxy]
    Miner2[Miner 2] --> Proxy
    MinerN[Miner N] --> Proxy
    Proxy --> Pool[Mining Pool]
    Pool --> Proxy
    Proxy --> Capture[Capture & Decode]
    Capture --> Storage[In-Memory Storage]
    Storage --> API[FastAPI Server]
    API --> UI[Web UI Browser]
```
### Core Components[¶](https://256foundation.github.io#core-components)

#### Backend (Python + FastAPI)[¶](https://256foundation.github.io#backend-python-fastapi)

**ProxyServer** (`proxy/server.py`)
- Listen on TCP :3333
- Accept new miner connections
- Create ProxySession for each
- Manage session lifecycle

**ProxySession** (`proxy/session.py`)
- One per miner connection
- Connect to upstream pool
- Bidirectional relay (asyncio tasks)
- Capture messages before forwarding
- Handle disconnections gracefully

**StratumParser** (`stratum/parser.py`)
- Parse JSON-RPC messages
- Best-effort (never throws)
- Returns ParsedMessage with success/error
- Encode messages back to bytes

**CaptureStorage** (`capture/storage.py`)
- In-memory ring buffer
- Thread-safe with asyncio.Lock
- Per-session and global storage
- WebSocket subscription support
- Query with filters

**FastAPI App** (`api/app.py`)
- Starts ProxyServer in background
- Exposes REST endpoints
- WebSocket for real-time
- CORS middleware
- Lifespan management

#### Frontend (React + TypeScript)[¶](https://256foundation.github.io#frontend-react-typescript)

- **SessionList** - Displays all sessions
- **MessageFilters** - Search and filter controls
- **MessageTable** - Scrollable message list with live updates
- **MessageDetail** - Full message inspection
- **AgentStatus** - Agent fleet monitoring

## Data Flow[¶](https://256foundation.github.io#data-flow)

### Miner → Pool (Upstream)[¶](https://256foundation.github.io#miner-pool-upstream)

```
sequenceDiagram
    participant M as Miner
    participant P as Proxy
    participant Pool as Pool
    participant S as Storage
    participant UI as Web UI
    M->>P: mining.submit
    P->>Pool: forward message
    P->>P: parse & capture
    P->>S: store message
    P->>UI: WebSocket broadcast
    Pool->>P: result response
    P->>M: forward response
    P->>S: update message
    P->>UI: update via WebSocket
```
1. Miner sends message to HashScope :3333
2. ProxySession receives and immediately forwards to pool (byte-for-byte)
3. In parallel: StratumParser decodes the message
4. CaptureStorage stores the captured message
5. WebSocket broadcasts to connected UI clients
6. UI updates in real-time

### Pool → Miner (Downstream)[¶](https://256foundation.github.io#pool-miner-downstream)

1. Pool sends response to HashScope
2. ProxySession receives and immediately forwards to miner (byte-for-byte)
3. In parallel: StratumParser decodes the message
4. CaptureStorage stores and links to original request (if applicable)
5. WebSocket broadcasts to connected UI clients
6. UI updates the message pair

**Key Principle**: Relay is always transparent and never blocked by parsing or storage.
