# 58. Design a distributed cache (Redis/Memcached cluster).

> Part B: Classic System Designs

**Answer:** Shard keys with consistent hashing or hash slots (Redis Cluster 16384), replicas for failover, LRU/LFU eviction, client-side or proxy routing, persistence (RDB/AOF) optional, handle hot keys and rebalancing.

```mermaid
flowchart LR
    n0["Client"]
    n1["Proxy"]
    n2["Slot to node"]
    n3["Master + replica"]
    n0 --> n1
    n1 --> n2
    n2 --> n3
```

---
[⬆ Back to index](../../README.md#-question-index)
