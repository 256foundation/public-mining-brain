# bitaxeorg/ESP-Miner issue #350: Consolidation of serial comms issues

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/350
> Collected: 2026-10-07
> Published: 2024-09-25

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 350
- State: open
- Author: adammwest
- Opened: 2024-09-25
- Closed: n/a
- Labels: bug

## Description

This is a super issue relating to all the chip related data. 
I will try and keep this updated and not stale

**Related issues**
https://github.com/skot/ESP-Miner/issues/69 [PR merged, DONE]
https://github.com/skot/ESP-Miner/issues/24 [PR made]
https://github.com/skot/ESP-Miner/issues/286
https://github.com/skot/ESP-Miner/issues/395 [PR merged, DONE]
https://github.com/skot/ESP-Miner/issues/248  [PR made]


**Items on List**
Key
[ ] not started
[X] done
[=] started

List
[X] the warning if consecutive RX have no messages or they are failing to convert to nonces
[=] the counting of TX (work) send fails
[  ] the counting of successful conversion of RX_bytes->nonces and RX_Bytes==0
[=] make RX byte processing handle offset problems
[X] handle crc from nonces
[X] determine fullscan for chips


**(2) Metric TX send % (no issue)**
 bad TX under fast CPU conditions
https://github.com/skot/ESP-Miner/pull/462

https://github.com/skot/ESP-Miner/blob/master/components/asic/bm1366.c#L623
https://github.com/skot/ESP-Miner/blob/master/components/asic/bm1368.c#L357
https://github.com/skot/ESP-Miner/blob/master/components/asic/bm1370.c#L435

for all chips the return value of send_work is ignored, this can be counted, in a metric like send TX fails/total TX  send
counting the raw values rather than the division is preferable.

TX_send % = end TX fails/total TX  send
the metric proves data is sent to the chip

if the fullscan_ms is not less than half of the time when dups appear, a TX send fail will result in duplicates, it has explanatory power.


**(3) Metric asic message conversions to nonces (no issue)**
conversion_rate = chip_diff_nonces /(asic_rx_bytes/11)

this metric calculated how many bytes recived from the chip and compares it to how many nonces have been recovered
it can be thought of how good the RX handling is.


**(4) For RX byte handling https://github.com/skot/ESP-Miner/issues/24**
a fix for this problem may also resolve https://github.com/skot/ESP-Miner/issues/286

there is already a pr https://github.com/skot/ESP-Miner/pull/48/commits
it would need to be extended for BM68/70  and tested

if misalignment by 1 byte many cases where nonce could exist this is not handled

0xYY represents any value
0xYY 0x55 0xaa 11 bytes fails but could be nonce
0x55 0xaa 0xYY 11 bytes fails but could be nonce
0x55 0xaa 10 bytes fails but could be nonce
not only that but for all these fails the whole 1024 buffer is cleared with a potential 93 messages 
clear buf should not be executed on asic message fails, only if offset messages are handled correctly
buf size should be multiple of expected nonce asic message len 11 maybe 11*100
when a misalignment happens the function serial rx should be calling an adjustment length to realign rather than 11

finally if a nonce is given at the end of a timeout it can be split over 2 calls
https://github.com/espressif/esp-idf/blob/master/components/esp_driver_uart/src/uart.c#L1504C3-L1543C2
the first call will get a portion of the message (invalid) and the second call will be misaligned (invalid)
in such a case the nonce that is split is lost, im not sure if it is worth to be reconstructed


**(5) handling crc messages https://github.com/skot/ESP-Miner/issues/395**
there is some work started here already

by counting the following
potential messages = crc5_ok/(asic_bytes/11)
it explains whether the chip is giving the right message structure back to the software


**(6) fullscan estimations https://github.com/skot/ESP-Miner/issues/248**
pr https://github.com/skot/ESP-Miner/pull/420
this is chip dependant and much harder, there is various work scattered around but not finished

by correctly calulating, the time at which dups occour, you can scale this number depending on
version rolls,frequency, chips, hcn.

and then there is another number
hashes_count how many hashes did the chip do
this is not the output rate of nonces. this number is the input of headers the 'true' hashrate

anyway if you know how many hashes are in a work item you have time and can calculate it. Its not trivial.
for the bm1397 single chip
hashes_in_work = (168/256) * 4* 2**32 per work item
hashes_count = (fullscan/max_fullscan)*work_items_sent* hashes_in_work
then you can correctly normalise the chip performance, by dividing output rate by this number.


finally with all the above, you have a good foundation of the chip performance, at the SW level.



## Comments

### skot on 2024-10-08

I agree there is a lot of room for improvement here!
