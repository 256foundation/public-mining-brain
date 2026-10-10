# Quick Start - HashScope Documentation

> Source: https://256foundation.github.io/HashScope/quickstart
> Collected: 2026-10-07
> Published: Unknown

# Quick Start Guide[¶](https://256foundation.github.io#quick-start-guide)

## 🚀 5-Minute Setup[¶](https://256foundation.github.io#5-minute-setup)

### Step 1: Set Your Pool Configuration[¶](https://256foundation.github.io#step-1-set-your-pool-configuration)

Or create a `.env` file in the project root:

### Step 2: Start HashScope[¶](https://256foundation.github.io#step-2-start-hashscope)

This will: - Start the proxy server on port 3333 (point your miners here) - Start the API server on port 8000 - Start the web UI on port 3000 (open http://localhost:3000)

### Step 3: Point Your Miner[¶](https://256foundation.github.io#step-3-point-your-miner)

Instead of connecting directly to your pool, point your miner to HashScope:

HashScope will transparently relay all traffic to the configured upstream pool.

### Step 4: View Messages[¶](https://256foundation.github.io#step-4-view-messages)

Open your browser to: **http://localhost:3000**

You'll see:
- **Real-time message stream** - every message flowing through the proxy
- **Decoded Stratum JSON-RPC** messages with full metadata
- **Session management** - track multiple miners independently
- **Filtering and search** - find exactly what you're looking for

## 📊 What You'll See[¶](https://256foundation.github.io#what-youll-see)

### Sessions Panel (Left)[¶](https://256foundation.github.io#sessions-panel-left)

- List of all connected miners
- Connection timestamps
- Message counts per session
- Click to filter messages by session

### Messages Table (Center)[¶](https://256foundation.github.io#messages-table-center)

- Live stream of all messages
- Direction badges (Miner → Pool / Pool → Miner)
- Method names and parameters
- Parse status
- Timestamps and latency

### Message Detail (Slide-in Panel)[¶](https://256foundation.github.io#message-detail-slide-in-panel)

- Full decoded JSON view
- Raw message bytes
- Parse error details (if any)
- Message metadata

### Filters (Top)[¶](https://256foundation.github.io#filters-top)

- Search across all messages
- Filter by direction
- Show errors only
- Filter by session

## 🔍 Common Use Cases[¶](https://256foundation.github.io#common-use-cases)

### Debug Connection Issues[¶](https://256foundation.github.io#debug-connection-issues)

1. Filter by session for the problematic miner
2. Look for error responses from pool
3. Check authorization messages

### Monitor Mining Efficiency[¶](https://256foundation.github.io#monitor-mining-efficiency)

1. View `mining.notify` frequency
2. Check `mining.submit` responses
3. Monitor difficulty changes

### Analyze Pool Behavior[¶](https://256foundation.github.io#analyze-pool-behavior)

1. Filter "Pool → Miner" messages
2. Look at job notification patterns
3. Check pool response times

### Find Protocol Issues[¶](https://256foundation.github.io#find-protocol-issues)

1. Enable "Show Errors Only"
2. Review parse errors in detail panel
3. Check raw bytes for corrupted messages

## 🛠️ Useful Commands[¶](https://256foundation.github.io#useful-commands)

## ❓ Troubleshooting[¶](https://256foundation.github.io#troubleshooting)

### Miner can't connect[¶](https://256foundation.github.io#miner-cant-connect)

- Check port 3333 is not already in use: `lsof -i :3333`
- Verify firewall allows connections
- Check backend logs: `docker compose logs backend`

### No messages appearing[¶](https://256foundation.github.io#no-messages-appearing)

- Ensure miner is connected to port 3333 (not directly to pool)
- Check WebSocket connection in browser console
- Verify `POOL_HOST` is correct

### "Disconnected" in UI[¶](https://256foundation.github.io#disconnected-in-ui)

- Backend may be starting up (wait 10-20 seconds)
- Check backend is running: `docker compose ps`
- Check for CORS errors in browser console

### Parse errors[¶](https://256foundation.github.io#parse-errors)

- This is normal! Not all pools use standard Stratum v1
- Messages are still relayed correctly (transparent proxy)
- View raw bytes in detail panel to debug
