# 7. How do you handle cache invalidation, stampede and hot keys?

> Part A: Fundamentals

**Answer:** Use TTL + explicit delete on write, versioned keys, and event-driven invalidation (CDC). Stampede (thundering herd): request coalescing/locks, jittered TTL, stale-while-revalidate, pre-warming. Hot keys: local in-process cache, key replication (key#1..N), read replicas.

```mermaid
flowchart LR
    n0["1000 concurrent misses"]
    n1["Per-key lock"]
    n2["1 DB query"]
    n3["Fill cache"]
    n4["999 requests read cache"]
    n0 --> n1
    n1 --> n2
    n2 --> n3
    n3 --> n4
```

---
[⬆ Back to index](../../README.md#-question-index)
