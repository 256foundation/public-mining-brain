# API Reference - HashScope Documentation

> Source: https://256foundation.github.io/HashScope/api-reference
> Collected: 2026-10-07
> Published: Unknown

# API Reference[¶](https://256foundation.github.io#api-reference)

Once HashScope is running, the API is available at **http://localhost:8000**

Interactive API documentation: **http://localhost:8000/docs**

## REST Endpoints[¶](https://256foundation.github.io#rest-endpoints)

### Sessions[¶](https://256foundation.github.io#sessions)

#### GET /api/sessions[¶](https://256foundation.github.io#get-apisessions)

List all miner sessions.

**Response:**

#### GET /api/sessions/{id}[¶](https://256foundation.github.io#get-apisessionsid)

Get details for a specific session.

**Response:**

### Messages[¶](https://256foundation.github.io#messages)

#### GET /api/messages[¶](https://256foundation.github.io#get-apimessages)

List captured messages with optional filters.

**Query Parameters:**
- `session_id` (optional) - Filter by session
- `direction` (optional) - Filter by direction (`miner_to_pool`, `pool_to_miner`, `hashscope_to_pool`)
- `limit` (optional) - Max messages to return (default 100)

**Response:**

#### GET /api/messages/{id}[¶](https://256foundation.github.io#get-apimessagesid)

Get a specific message by ID.

**Response:** Same as single message in array above.

### Agents[¶](https://256foundation.github.io#agents)

#### GET /api/agents[¶](https://256foundation.github.io#get-apiagents)

List all agents and their telemetry.

**Response:**

## WebSocket[¶](https://256foundation.github.io#websocket)

### WS /api/ws[¶](https://256foundation.github.io#ws-apiws)

Real-time message stream.

**Protocol:**
- Connect to `ws://localhost:8000/api/ws`
- Server pushes messages as JSON
- Each message is same format as REST API message object
- Connection auto-reconnects on disconnect

**Example (JavaScript):**

## Configuration Endpoints[¶](https://256foundation.github.io#configuration-endpoints)

### GET /api/config[¶](https://256foundation.github.io#get-apiconfig)

Get current HashScope configuration (non-sensitive fields only).

**Response:**

## Error Responses[¶](https://256foundation.github.io#error-responses)

All endpoints return standard HTTP status codes:

- **200** - Success
- **404** - Resource not found
- **422** - Validation error
- **500** - Internal server error

**Error format:**
