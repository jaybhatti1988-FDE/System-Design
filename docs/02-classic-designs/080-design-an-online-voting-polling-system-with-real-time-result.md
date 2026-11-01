# 80. Design an online voting / polling system with real-time results.

> Part B: Classic System Designs

**Answer:** Writes via queue to prevent overload, dedup per user with unique constraint, sharded counters aggregated periodically, results broadcast via SSE/WebSocket from cache; integrity via auditing and idempotency.

```mermaid
flowchart TD
    n0["Vote"]
    n1["Queue"]
    n2["Counter shards"]
    n3["Aggregator"]
    n4["Cache"]
    n5["SSE"]
    n6["Clients"]
    n0 --> n1
    n1 --> n2
    n2 --> n3
    n3 --> n4
    n4 --> n5
    n5 --> n6
```

---

---
[⬆ Back to index](../../README.md#-question-index)
