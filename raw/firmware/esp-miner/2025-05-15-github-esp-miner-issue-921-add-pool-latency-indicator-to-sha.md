# bitaxeorg/ESP-Miner issue #921: Add Pool Latency Indicator to Shares Subsection in AxeOS Dashboard

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/921
> Collected: 2026-10-07
> Published: 2025-05-15

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 921
- State: closed
- Author: ClosedShift
- Opened: 2025-05-15
- Closed: 2025-06-25
- Labels: none

## Description

**Description**
This feature request is to add a Pool Latency indicator to the Shares subsection of the AxeOS Dashboard. The goal is to calculate the latency between share submissions ("stratum_api: tx:" for mining.submit) and their corresponding responses ("stratum_task: rx:" for result accepted). Since the web GUI logs do not include timestamps, the firmware must perform these calculations internally.

**Rationale**
Latency between submitting shares and receiving pool responses is critical for mining efficiency. High latency can increase the risk of stale or rejected shares. By providing latency metrics on the dashboard, users can monitor and optimize their network and pool performance. Ping tests measure raw network latency, but even when the server allows Ping tests they don’t account for protocol overhead or pool-specific processing delays.

**Proposed Dashboard Display**
The latency metrics should be displayed in the Shares subsection as:
    [count] Pool Latency ([last share ms]) ([avg ms])

[count]: Number of latency calculations in the last 10 minutes.
[last share ms]: Latency of the most recent share (in milliseconds).
[avg ms]: Average latency over the last 10 minutes (in milliseconds).

Examples:
    1 Pool Latency (32ms) (32ms avg) (first calculation)
    123 Pool Latency (42ms) (38ms avg) (after multiple calculations)

**Implementation Approach**
The firmware could be modified in the following ways:

Capture Submission Time: When a share is submitted ("stratum_api: tx:"), record the current timestamp (e.g., using millis()).
Capture Response Time: When a response is received ("stratum_task: rx:"), record its timestamp and calculate latency by subtracting the submission timestamp.
Match Events: Use a unique identifier (e.g., job ID or share hash from the Stratum protocol) to pair each submission with its response.
Store Data: Maintain a rolling 10-minute window of latency values in a memory-efficient structure (e.g., a queue).
Calculate Metrics:
Count of latency calculations in the last 10 minutes.
Latency of the most recent share.
Average latency over the last 10 minutes.

Update Dashboard: Expose these metrics to the AxeOS Dashboard for display in the Shares subsection.

**Technical Considerations**
Timestamp Precision: Use millis() for millisecond precision, which should be sufficient for latency tracking.
Memory Management: Implement a queue or circular buffer to store latency data, ensuring it fits within the ESP32’s resource constraints.
Event Matching: Accurately match "tx" and "rx" events using Stratum protocol identifiers.
Edge Cases:
Handle missing responses with a timeout mechanism.
Decide whether to include latency for rejected shares (recommendation: calculate for accepted shares only).

**Additional Suggestions**
Configurable Window: Allow users to adjust the time window (e.g., 5, 10, 15 minutes) via the dashboard.
API Endpoint: Optionally provide latency metrics through an API for external use.

**Questions for Discussion**
Should latency be calculated only for accepted shares, or all shares?
Does the proposed display format suit the dashboard’s layout?

This feature will enhance the AxeOS Dashboard by providing actionable latency insights directly to users. Let’s discuss how to proceed with the implementation!

## Comments

### skot on 2025-05-15

This is a really interesting idea. On one hand it would be useful to see the round trip timing on mining.submit. On the other hand I'm not sure it's an especially valid comparison across pools; why would stratum servers prioritize sending the share response?

### ClosedShift on 2025-05-15

If the ESP32’s limited memory makes the proposed 10-minute rolling average for mining share latency infeasible, or in order to reduce complexity and overhead, I would propose instead displaying a a simple constrained rolling average of real-time latency for share submissions to the mining pool via the Stratum protocol. This scaled-back feature will minimize memory usage on the Bitaxe, support variable share rates, and update the dashboard every 5 seconds, synchronized with the other AxeOS Dashboard metrics.

**Constrained Rolling Average (~28 bytes)**
Store the last 5 latencies in a fixed-size array (e.g., float latencies[5]) with a running sum and count for efficient averaging. On each new share, overwrite the oldest latency in a circular buffer and compute the average. Every AxeOS Dashboard update (~5 seconds), include the average to the web interface to update the "Pool Latency" label e.g., “Pool Latency: (260 ms) (avg, 5 shares)”. This smooths out network variability while remaining memory-efficient.

**Additional Considerations**
The Bitaxe will transmit latency data to the AxeOS dashboard via WiFi about every 5 seconds, included with other dashboard metrics. If no shares are received in a 5-second window, the label will continue to display the last calculated average. Upon initial startup the label could display empty parens ( ) or (no data). This ensures a lightweight, cohesive feature that integrates seamlessly with the Shares subsection.

### ClosedShift on 2025-05-15

> "This is a really interesting idea. On one hand it would be useful to see the round trip timing on mining.submit. On the other hand I'm not sure it's an especially valid comparison across pools; why would stratum servers prioritize sending the share response?"

Thanks for the feedback and for highlighting the potential challenges of comparing round-trip latency across pools! I agree that the mining.submit round-trip time is a valuable metric for miners to monitor pool connection stability, and your point about cross-pool consistency is well-taken.

To address your question about Stratum server prioritization: most pools prioritize share responses because they’re critical for miner feedback and accurate payout accounting. Fast responses prevent miners from stalling and ensure the pool’s hash rate remains optimal. Stratum’s lightweight design and optimized server software typically handle mining.submit responses in high-priority queues, even during bursts (e.g., multiple shares per second). While rare cases of server overload or network issues could introduce delays, these are exceptions, and the 5-share rolling average in our feature smooths out such variations.

Regarding cross-pool comparisons, you’re right that network conditions (e.g., geographic distance) or pool load can affect latency, making direct comparisons trickier. However, the “Pool Latency” label (updated every 5 seconds in the AxeOS Shares subsection) is primarily designed to help users assess a single pool’s performance over time or detect issues like timeouts. The rolling average ensures stable readings, even with variable share rates. This makes it a practical tool for Bitaxe users, while still offering some basis for comparing pools, assuming similar network conditions.

I’d love to hear your thoughts on how we could further refine this to address comparison concerns—perhaps by adding a note in the dashboard about interpreting latency across pools? Thanks again for the input!

### skot on 2025-05-16

> To address your question about Stratum server prioritization: most pools prioritize share responses because they’re critical for miner feedback and accurate payout accounting. Fast responses prevent miners from stalling and ensure the pool’s hash rate remains optimal. Stratum’s lightweight design and optimized server software typically handle mining.submit responses in high-priority queues, even during bursts (e.g., multiple shares per second). While rare cases of server overload or network issues could introduce delays, these are exceptions, and the 5-share rolling average in our feature smooths out such variations.

That's the thing, I don't think the pool's response to the mining.submit from the miner is critical at all. I could definitely imagine a leisurely latency there. This would be easier to test out with a python script or something. 



### ClosedShift on 2025-05-16

Thanks for your feedback! I want to make sure I’m following your point about mining.submit responses not being critical. Are you suggesting that the Pool Latency feature in the AxeOS dashboard might not be that important because miners can keep working even with slow pool responses? Or do you think there’s a better way to measure something like the network delay for sending shares to the pool, rather than the full response time?

I'm in agreement that a better way would be measuring only the time it takes for the mining.submit message to reach the pool’s server (one-way transmission time). But if we can't get that, I still think the Pool Latency feature is the next best thing for users because it shows the pool’s overall responsiveness.

Your idea to test this with a Python script sounds interesting! But I'm not sure I exactly understand about what you’d like to test—maybe how the miner handles delayed responses, the accuracy of the latency display, or something else? I’d love to explore this to see if the feature needs tweaking or if there is a way to measure one-way transmission time. I’m open to any insights you may have toward incorporating a more useful feature.

### skot on 2025-05-16

> Thanks for your feedback! I want to make sure I’m following your point about mining.submit responses not being critical. Are you suggesting that the Pool Latency feature in the AxeOS dashboard might not be that important because miners can keep working even with slow pool responses? 

Yes, that is what I'm suggesting. 

Thank you for bringing up this idea, it is an interesting one. However, I don't appreciate having this conversation with chatGPT. I'm going to drop out of this thread.


### ClosedShift on 2025-05-17

Ok just trying to help with a network/pool latency idea I though could be useful for the community. I didn't mean to make you feel unappreciated, I just wanted to give a good writeup. Thanks for all you're doing, I know something like this isn't high on the priority list, just thought it would be nice to be able to get a measure of which pool is actually better for my location.
