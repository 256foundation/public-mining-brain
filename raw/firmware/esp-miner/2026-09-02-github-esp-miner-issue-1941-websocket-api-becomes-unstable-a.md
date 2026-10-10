# bitaxeorg/ESP-Miner issue #1941: WebSocket API becomes unstable after long runtime due to httpd_ws_send_frame_async() being called outside the HTTPD worker task

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1941
> Collected: 2026-10-07
> Published: 2026-09-02

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1941
- State: open
- Author: seby1302
- Opened: 2026-09-02
- Closed: n/a
- Labels: none

## Description

# WebSocket instability caused by HTTPD send context and stale/dead WebSocket sessions

## Description

After running ESP-Miner for an extended period with the Web UI open, the API WebSocket can become unstable and repeatedly disconnect/reconnect.

Typical log output looks like:

```text
websocket: Removed WebSocket api client, fd: 46, slot: 0
websocket: Added WebSocket api client, fd: 43, slot: 0
websocket: Removed WebSocket api client, fd: 43, slot: 0
websocket: Added WebSocket api client, fd: 43, slot: 0
```

Occasional isolated WebSocket reconnects are normal and expected.

The problem is a persistent reconnect loop which, in testing, could start after roughly 30 minutes and then continue almost continuously.

The miner itself continues mining normally while the WebSocket/API becomes unstable.

Tested with:

```text
ESP-IDF v5.5.3
```

---

## Issue 1: `httpd_ws_send_frame_async()` called outside the HTTPD worker task

ESP-Miner's `websocket_api_task()` is a separate FreeRTOS task.

It periodically calls:

```c
process_and_send_update(last_full_json, -1);
```

which eventually reaches:

```text
websocket_broadcast()
    -> websocket_send_to_client()
        -> httpd_ws_send_frame_async()
```

The current implementation therefore calls:

```c
httpd_ws_send_frame_async(server_handle, fd, pkt);
```

directly from a task that is not the HTTP server worker task.

This does not match the intended ESP-IDF usage of this low-level API.

The ESP-IDF documentation states for `httpd_ws_send_frame_async()`:

> "This API should rarely be called directly, with an exception of asynchronous send using httpd_queue_work."

Despite its name, `httpd_ws_send_frame_async()` performs the actual send synchronously in the context of the calling task.

ESP-IDF issue #18080 also summarizes the API behavior:

* `httpd_ws_send_frame_async()` performs a synchronous send and must run on the HTTPD worker task.
* `httpd_ws_send_data()` may be called outside the worker task and blocks until the queued send completes.
* `httpd_ws_send_data_async()` may be called outside the worker task and does not block.

The ESP-IDF implementation confirms this distinction.

`httpd_ws_send_data()` creates a transfer object and queues:

```c
httpd_queue_work(handle, httpd_ws_send_cb, transfer);
```

The HTTPD worker then executes:

```c
httpd_ws_send_frame_async(...)
```

in the correct task context.

---

## Important exception: initial WebSocket connection

Simply replacing every call to:

```c
httpd_ws_send_frame_async()
```

with:

```c
httpd_ws_send_data()
```

causes a deadlock in ESP-Miner.

During the WebSocket handshake, `websocket_handler()` is already executing inside the HTTPD worker task and calls:

```c
websocket_api_on_connect(fd);
```

This sends the initial state to the newly connected client.

Calling blocking `httpd_ws_send_data()` from this path queues work back to the same HTTPD worker and waits for that queued work to complete.

The worker therefore waits for itself.

For this reason the two execution contexts must remain separate.

---

## Proposed fix for Issue 1

Keep the direct send for messages originating from the HTTP/WebSocket handler context:

```c
void websocket_send_to_client(int fd, httpd_ws_frame_t *pkt)
{
    if (server_handle == NULL || fd == -1) return;

    if (httpd_ws_send_frame_async(server_handle, fd, pkt) != ESP_OK) {
        ESP_LOGW(TAG, "Failed to send WebSocket frame to fd: %d", fd);
    }
}
```

Add a queued/blocking variant for broadcasts originating from `websocket_api_task()`:

```c
static void websocket_send_to_client_queued(int fd, httpd_ws_frame_t *pkt)
{
    if (server_handle == NULL || fd == -1) return;

    if (httpd_ws_get_fd_info(server_handle, fd) !=
        HTTPD_WS_CLIENT_WEBSOCKET)
    {
        return;
    }

    esp_err_t ret = httpd_ws_send_data(server_handle, fd, pkt);

    if (ret != ESP_OK) {
        ESP_LOGW(
            TAG,
            "Failed queued WebSocket send to fd: %d (%s)",
            fd,
            esp_err_to_name(ret)
        );
    }
}
```

Then use the queued variant for broadcasts:

```c
void websocket_broadcast(WebSocketClientType type, httpd_ws_frame_t *pkt)
{
    if (server_handle == NULL)
        return;

    for (int i = 0; i < MAX_WEBSOCKET_CLIENTS; i++)
    {
        int fd = clients[i].fd;

        if (fd == -1 || clients[i].type != type)
            continue;

        if (httpd_ws_get_fd_info(server_handle, fd) !=
            HTTPD_WS_CLIENT_WEBSOCKET)
        {
            ESP_LOGW(TAG, "Removing stale WebSocket fd: %d", fd);
            websocket_remove_client(fd);
            continue;
        }

        websocket_send_to_client_queued(fd, pkt);
    }
}
```

This gives two clearly separated paths:

```text
WebSocket handshake / HTTPD worker
    -> websocket_api_on_connect()
    -> websocket_send_to_client()
    -> httpd_ws_send_frame_async()


websocket_api_task / external FreeRTOS task
    -> websocket_broadcast()
    -> websocket_send_to_client_queued()
    -> httpd_ws_send_data()
    -> httpd_queue_work()
    -> HTTPD worker
```

---

# Issue 2: dead/stale WebSocket sessions can temporarily stall the HTTP server

A second related failure can be reproduced when the WebSocket peer disappears, for example after a network interruption.

The existing implementation can reach:

```text
httpd_txrx: httpd_sock_err: error in send : 11
httpd_ws: httpd_ws_send_frame_async: Failed to send WS header
websocket: Failed queued WebSocket send to fd: 42 (ESP_FAIL)
```

The miner continues mining normally, but the Web UI becomes very difficult or impossible to access.

This appears to be a separate HTTPD/WebSocket session handling problem rather than a mining failure.

`error in send : 11` is especially interesting because the same failure pattern is documented in ESP-IDF issue #18080.

That issue describes a dead WebSocket peer causing repeated:

```text
httpd_sock_err: error in send : 11
httpd_ws_send_frame_async: Failed to send WS header
```

It also explains that `httpd_sess_trigger_close()` itself uses `httpd_queue_work()`.

If many failed send operations are already queued, the session-close operation may therefore be placed behind those sends, delaying recovery.

This can cause the HTTPD worker to remain occupied with failed WebSocket work while normal HTTP requests become slow or temporarily unavailable.

### Observed behavior

With the old send implementation, after entering this state the Web UI could remain effectively unusable and a restart was required to recover reliably.

Example:

```text
httpd_txrx: httpd_sock_err: error in send : 11
httpd_ws: httpd_ws_send_frame_async: Failed to send WS header
websocket: Failed queued WebSocket send to fd: 42 (ESP_FAIL)
```

Mining itself continued normally.

With the modified send path described above, the same type of failure has still been observed, but the WebSocket/HTTP interface recovered automatically after approximately 1–2 minutes and continued operating normally afterwards.

This suggests that Issue 1 and Issue 2 are related but distinct:

```text
Issue 1
Wrong execution context for periodic WebSocket broadcasts
    ->
long-term WebSocket instability / reconnect loop


Issue 2
Dead or stale WebSocket peer
    ->
send() error 11
    ->
Failed to send WS header
    ->
HTTPD worker temporarily impaired
    ->
eventual recovery or, with the old implementation,
persistent broken Web UI until restart
```

---

## Possible additional hardening

A failed or stale WebSocket should ideally be removed from ESP-Miner's own client table immediately so that the periodic API task does not continue attempting broadcasts to that file descriptor.

Before broadcasting, the socket state can also be checked with:

```c
httpd_ws_get_fd_info(server_handle, fd)
```

and clients which are no longer:

```c
HTTPD_WS_CLIENT_WEBSOCKET
```

can be removed from the local WebSocket client list.

Additionally, after a failed send, triggering closure of the HTTPD session may help prevent repeated attempts to use a dead connection.

However, ESP-IDF issue #18080 notes that `httpd_sess_trigger_close()` is also queued through `httpd_queue_work()`, so a close can itself be delayed if the HTTPD work queue is already backed up with failed sends.

---

## Result

With the modified WebSocket send path, ESP-Miner now recovers from stale or broken WebSocket connections instead of remaining stuck in a persistent error loop.

Observed recovery sequence:

```text
httpd_txrx: httpd_sock_err: error in send : 11
httpd_ws: httpd_ws_send_frame_async: Failed to send WS header
websocket: Failed queued WebSocket send to fd: 42 (ESP_FAIL), closing client
websocket: Added WebSocket api client, fd: 44, slot: 1
websocket: Removed WebSocket api client, fd: 42, slot: 0

Mining continues normally during the recovery.

Most importantly, the previous persistent `ESP_FAIL` / reconnect loop no longer continues indefinitely. 
The stale connection is removed, the WebSocket reconnects, 
and the Web UI becomes usable again without restarting the miner.

Occasional isolated reconnects or transient `send : 11` errors can still occur, 
but they now self-recover instead of leaving the WebSocket subsystem permanently degraded.
```

---

## ESP-IDF references

ESP-IDF v5.5 HTTP Server documentation:

https://docs.espressif.com/projects/esp-idf/en/v5.5/esp32/api-reference/protocols/esp_http_server.html

ESP-IDF WebSocket implementation:

https://github.com/espressif/esp-idf/blob/master/components/esp_http_server/src/httpd_ws.c

ESP-IDF issue #18080 — stale WebSocket connections, send error 11, 
queued session close, and explanation of the WebSocket send API semantics:

https://github.com/espressif/esp-idf/issues/18080

ESP-IDF issue #9250 — clarification that the `async` name of `httpd_ws_send_frame_async()` is misleading and that the function itself does not queue the operation:

https://github.com/espressif/esp-idf/issues/9250

ESP-IDF issue #14495 — near-simultaneous calls to `httpd_ws_send_frame_async()` causing malformed frames and browser disconnects:

https://github.com/espressif/esp-idf/issues/14495

ESP-IDF WebSocket example showing asynchronous WebSocket work being queued through the HTTP server worker:

https://github.com/espressif/esp-idf/blob/master/examples/protocols/http_server/ws_echo_server/main/ws_echo_server.c

**### See modified attachments

ESP-Miner\main\http_server\websocket.c**

[websocket.zip](https://github.com/user-attachments/files/31722791/websocket.zip)

## Comments

### mutatrum on 2026-09-02

Thank you, your findings are valid, but please revisit them onto the current master, especially for the 2nd issue. Some parts of this issue have been fixed in #1803, but some hardenings can still be applied. Also note that we're building on ESP-IDF 6.0.2 in #1829, this changed the upgrade check.

Having a stale dashboard is something I've seen, and #1913 did fix some instances, but it looks like this issue also improves the backend.

Looking forward to a PR.

### seby1302 on 2026-09-03

I retested this on the current master with ESP-IDF 6.0.2.

After a Wi-Fi disconnect/reconnect, the WebSocket behavior is now mostly normal. The current master already contains several of the hardening changes that were relevant to my original findings, including stale client removal/session close handling and improved client list handling during broadcasts.

So at this point, I would say that most of the original issue has already been addressed upstream.

There is still one part I want to keep an eye on: the broadcast path still eventually calls `httpd_ws_send_frame_async()`, so I want to continue testing whether the send-context behavior can still cause rare long-runtime issues. But so far, with the current master and IDF 6.0.2, I have not been able to reproduce the previous persistent reconnect/error loop in the same way.


### mutatrum on 2026-09-03

> I retested this on the current master with ESP-IDF 6.0.2.
> 
> After a Wi-Fi disconnect/reconnect, the WebSocket behavior is now mostly normal. The current master already contains several of the hardening changes that were relevant to my original findings, including stale client removal/session close handling and improved client list handling during broadcasts.
> 
> So at this point, I would say that most of the original issue has already been addressed upstream.
> 
> There is still one part I want to keep an eye on: the broadcast path still eventually calls `httpd_ws_send_frame_async()`, so I want to continue testing whether the send-context behavior can still cause rare long-runtime issues. But so far, with the current master and IDF 6.0.2, I have not been able to reproduce the previous persistent reconnect/error loop in the same way.

Thank you for the re-visit. The use of `httpd_ws_send_frame_async` is still incorrect, as it's out of context. And the hardening with a pre-flight check on FD also makes sense to add.

The frontend fixes might mask the issue, but they are still valid.
