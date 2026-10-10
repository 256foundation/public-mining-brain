# bitaxeorg/ESP-Miner issue #686: mining.suggest_difficulty sends incorrect format, causing pool disconnection

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/686
> Collected: 2026-10-07
> Published: 2025-02-02

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 686
- State: closed
- Author: bitraedev
- Opened: 2025-02-02
- Closed: 2025-02-04
- Labels: none

## Description

# **Bug Report: `mining.suggest_difficulty` Sends Incorrect Format, Causing Pool Disconnection**

## **Summary**
The miner incorrectly formats the `mining.suggest_difficulty` Stratum request by sending the difficulty value inside an **array (`[1000]`)** instead of as a **single number (`1000`)**. This causes pools that use software like **Miningcore** to throw a `System.InvalidCastException` error and disconnect the miner, preventing successful mining.

---

## **Steps to Reproduce**
1. Connect the miner to a **Stratum V1 pool** (that uses Miningcore software).
2. The miner sends the `mining.suggest_difficulty` request in the following format:
   ```json
   {"id": 4, "method": "mining.suggest_difficulty", "params": [1000]}
   ```
3. The pool logs show an error similar to:
   ```
   [E] [btcsolo] Unable to convert suggested difficulty [
     1000
   ] System.InvalidCastException: Object must implement IConvertible.
   ```
4. The pool **closes the connection**, causing the miner to repeatedly reconnect.

---

## **Expected Behavior**
- The miner should send the difficulty **as a single number, not inside an array**.
- The correct Stratum request format should be:
   ```json
   {"id": 4, "method": "mining.suggest_difficulty", "params": 1000}
   ```
- This would ensure compatibility with **Miningcore software and other Stratum V1 pools**.

---

## **File Location**
- **File Path:** [`main/tasks/stratum_task.c`](https://github.com/skot/ESP-Miner/blob/master/main/tasks/stratum_task.c)
- **Line Number:** **251**

---

## **Possible Fix**
Modify **`stratum_task.c`** where `mining.suggest_difficulty` is sent.

### **Current Code (Incorrect)**
Located at **line 251** in `stratum_task.c`:
```c
// mining.suggest_difficulty - ID: 4
STRATUM_V1_suggest_difficulty(GLOBAL_STATE->sock, STRATUM_DIFFICULTY);
```
#### **Issue:**
- The difficulty value is placed **inside square brackets (`[%d]`)**, which generates an **array `[1000]` instead of a single value `1000`**.
- This causes the pool to **fail type conversion and disconnect the miner**.

---

### **Proposed Fix (Correct Format)**
Modify the same section of code to send a **single number** instead of an array:
```c
// mining.suggest_difficulty - ID: 4 (Fixed)
char difficulty_request[128];
snprintf(difficulty_request, sizeof(difficulty_request),
         "{\"id\": 4, \"method\": \"mining.suggest_difficulty\", \"params\": %d}", STRATUM_DIFFICULTY);

STRATUM_V1_send_request(GLOBAL_STATE->sock, difficulty_request);
```
#### **Fixes:**
✅ Removes the square brackets (`[%d]`) so the difficulty is sent as a **direct number (`1000`)**.  
✅ Ensures compatibility with **Miningcore and other Stratum pools**.  
✅ Prevents the pool from **disconnecting the miner** due to a type conversion error.  

---

## **Logs**
### **Miner Log (At Time of Issue)**
```
(14183) stratum_task: setup message rejected: unknown
(14203) stratum_task: rx: {"jsonrpc":"2.0","method":"mining.set_difficulty","params":[4096.0],"id":null}
(14213) stratum_task: Set stratum difficulty: 4096
```

### **Pool Log (At Time of Issue)**
```
[E] [btcsolo] Unable to convert suggested difficulty [
  1000
] System.InvalidCastException: Object must implement IConvertible.
[I] [btcsolo] [0HN9G6VABIQOA] Connection closed
```

---

## **System Information**
- **Miner Version:** _(v2.5.1)_
- **Pool Software:** Miningcore
- **Pool Stratum Version:** Stratum V1
- **Operating System:** _(AxeOS)_
- **Hardware:** _(Bitaxe Gamma)_

---

## **Additional Notes**
- This issue prevents **successful mining** because the pool forcefully **disconnects the miner**.
- Fixing this would **ensure compatibility with standard Stratum pools**.
- If needed, I can submit a **pull request** with the fix.

---

## **Request**
Please confirm if this is an issue, and let me know if a **pull request (PR)** would be helpful!


## Comments

### eandersson on 2025-02-02

This looks like a bug on the Miningcore side. @benjamin-wilson can probably confirm.

Here are some Stratum V1 references I found that indicates that the current ESP-Miner implementation is correct.
https://github.com/braiins/bmminer/blob/93ad6af550c3f5bf592dedadec1aff5926e7cfd6/util.c#L2601
https://bitcointalk.org/index.php?topic=557866.msg6078255#msg6078255
https://github.com/benjamin-wilson/public-pool/blob/ddb7a89615b812cd32a8278b7f696619b7897db8/src/models/stratum-messages/SuggestDifficultyMessage.ts#L36

### benjamin-wilson on 2025-02-04

Yes I think this is correct, Miningcore should adjust their code to bring it up to the consensus of being an array. 

### Georges760 on 2025-02-04

> Here are some Stratum V1 references I found that indicates that the current ESP-Miner implementation is correct.
> https://github.com/braiins/bmminer/blob/93ad6af550c3f5bf592dedadec1aff5926e7cfd6/util.c#L2601
> https://bitcointalk.org/index.php?topic=557866.msg6078255#msg6078255
> https://github.com/benjamin-wilson/public-pool/blob/ddb7a89615b812cd32a8278b7f696619b7897db8/src/models/stratum-messages/SuggestDifficultyMessage.ts#L36

Strange to note that all these implementations encode `mining.suggest_difficulty` as a RPC Request from Client to Server (with an non-null `id`), and not a Notification (with a null `id`). But the Server never reply any RPC Response (as a Request would like to) so it  is more like a Notification... lol
