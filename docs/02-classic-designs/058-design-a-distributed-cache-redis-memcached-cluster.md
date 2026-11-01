# 58. Design a distributed cache (Redis/Memcached cluster).

> Part B: Classic System Designs

**Answer:** Shard keys with consistent hashing or hash slots (Redis Cluster 16384), replicas for failover, LRU/LFU eviction, client-side or proxy routing, persistence (RDB/AOF) optional, handle hot keys and rebalancing.

```
Client -> proxy -> slot->node (M1 R1 | M2 R2 | M3 R3)
```

---
[⬆ Back to index](../../README.md#-question-index)
