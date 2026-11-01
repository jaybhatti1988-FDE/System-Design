# 7. How do you handle cache invalidation, stampede and hot keys?

> Part A: Fundamentals

**Answer:** Use TTL + explicit delete on write, versioned keys, and event-driven invalidation (CDC). Stampede (thundering herd): request coalescing/locks, jittered TTL, stale-while-revalidate, pre-warming. Hot keys: local in-process cache, key replication (key#1..N), read replicas.

```
1000 misses -> [lock per key] -> 1 DB query -> fill -> 999 wait
```

---
[⬆ Back to index](../../README.md#-question-index)
