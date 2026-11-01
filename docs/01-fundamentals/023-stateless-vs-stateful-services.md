# 23. Stateless vs stateful services?

> Part A: Fundamentals

**Answer:** Stateless services keep no session in memory (state in DB/cache/token), so any instance can serve any request and scaling/failover is easy. Stateful (DBs, WebSocket servers) need partitioning, replication and sticky routing.

```mermaid
flowchart LR
    n0["Request"]
    n1["Any stateless instance"]
    n2["Shared Redis / DB"]
    n0 --> n1
    n1 --> n2
```

---
[⬆ Back to index](../../README.md#-question-index)
