# Developer Guide - HashScope Documentation

> Source: https://256foundation.github.io/HashScope/developer-guide
> Collected: 2026-10-07
> Published: Unknown

# Developer Guide[¶](https://256foundation.github.io#developer-guide)

## Project Structure[¶](https://256foundation.github.io#project-structure)

## Technology Stack[¶](https://256foundation.github.io#technology-stack)

### Backend[¶](https://256foundation.github.io#backend)

- **Python 3.11+**
- **FastAPI** - Web framework
- **asyncio** - Async I/O for TCP
- **Pydantic** - Data validation
- **uvicorn** - ASGI server
- **pytest** - Testing

### Frontend[¶](https://256foundation.github.io#frontend)

- **React 18** - UI framework
- **TypeScript** - Type safety
- **Vite** - Build tool
- **shadcn/ui** - Component library
- **Tailwind CSS** - Styling
- **React Router** - Routing
- **Mermaid** - Diagrams

### Infrastructure[¶](https://256foundation.github.io#infrastructure)

- **Docker** - Containerization
- **docker-compose** - Orchestration
- **nginx** - Frontend serving

## Development Setup[¶](https://256foundation.github.io#development-setup)

### Backend[¶](https://256foundation.github.io#backend_1)

### Frontend[¶](https://256foundation.github.io#frontend_1)

Frontend dev server runs on http://localhost:5173 and proxies API requests to backend.

### Agent[¶](https://256foundation.github.io#agent)

## Coding Standards[¶](https://256foundation.github.io#coding-standards)

### Python[¶](https://256foundation.github.io#python)

- Type hints required for public functions
- Use `ruff` or `black` for formatting
- **No blocking calls in async code**
- Structured logging (JSON logs preferred)
- Best-effort parsing - never crash on malformed input

### TypeScript[¶](https://256foundation.github.io#typescript)

- Strict mode enabled
- Functional components with hooks
- Prefer composition over complex components
- Type all props and state

### Key Principles[¶](https://256foundation.github.io#key-principles)

1. **Never modify message contents** - byte-for-byte relay
2. **Best-effort parsing** - parse errors should not crash the proxy
3. **Security first** - treat all input as untrusted
4. **Type safety** - use type hints and TypeScript strictly
5. **Nostr events must be signed** - all events require valid signatures
6. **Publishing never blocks relaying** - background tasks only

## Message Model[¶](https://256foundation.github.io#message-model)

### CapturedMessage[¶](https://256foundation.github.io#capturedmessage)

## Testing[¶](https://256foundation.github.io#testing)

## Docker Workflow[¶](https://256foundation.github.io#docker-workflow)

**CRITICAL**: After making ANY code changes, rebuild affected services:

## Performance Characteristics[¶](https://256foundation.github.io#performance-characteristics)

### Scalability[¶](https://256foundation.github.io#scalability)

- **Concurrent miners**: Limited by system resources
- **Messages/second**: Thousands (async I/O)
- **Memory usage**: Bounded by ring buffer size
- **CPU usage**: Low (mostly I/O bound)

### Latency[¶](https://256foundation.github.io#latency)

- **Relay overhead**: \<1ms (in-memory copy)
- **Parse overhead**: \~0.1ms per message
- **WebSocket broadcast**: \<10ms to all clients

## Extension Points[¶](https://256foundation.github.io#extension-points)

The architecture supports future enhancements:

1. **Message Routing** - Add routing rules in ProxySession
2. **Persistent Storage** - Swap CaptureStorage implementation
3. **Authentication** - Add middleware to FastAPI
4. **Message Modification** - Add transform step before forwarding (future iterations)
5. **Additional Relays** - Secondary Nostr relays for redundancy
