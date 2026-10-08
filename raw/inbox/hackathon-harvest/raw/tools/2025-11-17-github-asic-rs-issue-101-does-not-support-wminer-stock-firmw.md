# 256foundation/asic-rs issue #101: Does not support WMiner stock firmware older than 20220929.12.REL for MS30s

> Source: https://github.com/256foundation/asic-rs/issues/101
> Collected: 2026-10-07
> Published: 2025-11-17

- Repository: 256foundation/asic-rs
- Type: issue
- Number: 101
- State: closed
- Author: moonbootspleb
- Opened: 2025-11-17
- Closed: 2025-12-01
- Labels: none

## Description

Confirmation that scan does not recognize firmwares for older than 20220929.12.REL.

Sample responses for each confirmed unrecognized miner.

Query:

```#!/bin/bash
#
# cgminer_query.sh
# Queries cgminer API on a specified IP for multiple commands
# and writes output to a file in the format "{command} - {result}"
#

# Check usage
if [ $# -ne 1 ]; then
    echo "Usage: $0 <ip-address>"
    exit 1
fi

IP="$1"
PORT=4028        # default cgminer API port
OUTPUT_FILE="cgminer_${IP}.log"

# Commands to run
COMMANDS=("devs" "get_version" "get_psu" "pools" "status" "summary")

# Function to query cgminer API
query_cgminer() {
    local cmd="$1"
    # Send command to cgminer API and capture result
    # cgminer uses JSON-like strings over a TCP socket
    result=$(echo "{\"command\":\"$cmd\"}" | nc "$IP" "$PORT" 2>/dev/null)
    echo "$result"
}

# Start writing output file
echo "CGMiner API Query Results for $IP" > "$OUTPUT_FILE"
echo "--------------------------------------" >> "$OUTPUT_FILE"
echo "" >> "$OUTPUT_FILE"

# Loop through commands and append results
for cmd in "${COMMANDS[@]}"; do
    echo "Running command: $cmd"
    result=$(query_cgminer "$cmd")
    if [ -z "$result" ]; then
        result="(no response)"
    fi
    echo "{$cmd} - {$result}" >> "$OUTPUT_FILE"
    echo "" >> "$OUTPUT_FILE"
done

echo "All results saved to $OUTPUT_FILE"
```

Response Logs
[cgminer_querylogs.zip](https://github.com/user-attachments/files/23585546/cgminer_querylogs.zip)



## Comments

### b-rowan on 2025-11-19

AFAIU this should be fixed by https://github.com/256foundation/asic-rs/pull/102/commits/f3b7759cf784e458940444feecd527a746e683d6
