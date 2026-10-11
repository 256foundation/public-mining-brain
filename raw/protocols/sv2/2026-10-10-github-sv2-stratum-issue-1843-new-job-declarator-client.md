# SRI issue #1843 — New Job Declarator Client (closed, 31 comments)

> Source: https://github.com/stratum-mining/stratum/issues/1843
> Collected: 2026-10-10
> Published: see body
> Registry ID: sv2-repo

NUM: 1843 STATE: closed CREATED: 2025-08-24T05:44:05Z CLOSED: 2025-09-24T09:06:55Z COMMENTS: 31
TITLE: New Job Declarator Client
LABELS: 

This PR introduces the new Job Declarator Client (JDC).
It adopts a new architecture that makes the flow leaner and easier to comprehend, while leveraging the new channel APIs and other improvements in the SRI stack.

This is still a work in progress, with ongoing polishing of rough edges.

Please review the overall diff rather than going commit by commit, the holistic view will make the changes clearer.

Currently, we have channel id unique across downstream, which gonna fix and make it unique per downstream.

This PR closes: https://github.com/stratum-mining/stratum/issues/1674 and all its sub-issues.

WIP

* [x] Make fallback deterministic (currently it explodes into a cascade of errors, requiring the setup to re-run multiple times).
* [x] Add improved documentation explaining the flow.
* [x] Update README.
* [x] Replace the old JDC with the new one and update integration tests.
* [x] Update CI Workflow to include new-jdc.

Closes: stratum-mining/stratum#1897


### TOP COMMENTS #1843

--- @plebhash (2025-09-20T00:43:25Z):
I'm doing some testing with:
- two WhatsMiners from BOB space
- tProxy in non-aggregated mode at a7a6bdd3e41eb093ae99f29677669e7247615213
- JDC at a7a6bdd3e41eb093ae99f29677669e7247615213

below are logs from Pool, where shares are arriving from JDC with bad `sequence_number`: 1, 2, 4, 9

<img width="892" height="990" alt="image" src="https://github.com/user-attachments/assets/6075fefe-3cbe-42f6-a55d-082bdac1f3c8" />


--- @bit-aloo (2025-09-20T08:47:35Z):
> I'm doing some testing with:
> 
> * two WhatsMiners from BOB space
> * tProxy in non-aggregated mode at [a7a6bdd](https://github.com/stratum-mining/stratum/commit/a7a6bdd3e41eb093ae99f29677669e7247615213)
> * JDC at [a7a6bdd](https://github.com/stratum-mining/stratum/commit/a7a6bdd3e41eb093ae99f29677669e7247615213)
> 
> below are logs from Pool, where shares are arriving from JDC with bad `sequence_number`: 1, 2, 4, 9
> 
> <img alt="image" width="892" height="990" src="https://private-user-images.githubusercontent.com/147345153/491850148-6075fefe-3cbe-42f6-a55d-082bdac1f3c8.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NTgzNTY5OTMsIm5iZiI6MTc1ODM1NjY5MywicGF0aCI6Ii8xNDczNDUxNTMvNDkxODUwMTQ4LTYwNzVmZWZlLTNjYmUtNDJmNi1hNTVkLTA4MmJkYWMxZjNjOC5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1T

--- @plebhash (2025-09-22T17:04:11Z):
the same issues reported on https://github.com/stratum-mining/stratum/issues/1899 are happening here

I'd suggest a fix similar to https://github.com/stratum-mining/stratum/pull/1900

--- @bit-aloo (2025-09-23T05:25:52Z):
> the same issues reported on stratum-mining/stratum#1899 are happening here
> 
> I'd suggest a fix similar to stratum-mining/stratum#1900

Updated the logs accordingly, Thanks.
