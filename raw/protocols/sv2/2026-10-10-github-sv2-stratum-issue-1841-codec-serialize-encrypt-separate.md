# SRI issue #1841 — Enable Serializing and Encrypting Separately in Codec encoder API (open, 12 comments)

> Source: https://github.com/stratum-mining/stratum/issues/1841
> Collected: 2026-10-10
> Published: see body
> Registry ID: sv2-repo

NUM: 1841 STATE: open CREATED: 2025-08-22T15:31:51Z CLOSED: open COMMENTS: 12
TITLE: Enable Serializing and Encrypting Separately in Codec encoder API
LABELS: 

When broadcasting jobs, it is most performant to serialize once, and share the serialized bytes to each client tcp writer, so it would be good to allow this in the api as `encode(&mut self, data: Arc<Vec<u8>>)` and `encode(&mut self, data: &[u8])`
