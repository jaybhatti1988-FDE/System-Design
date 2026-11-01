# 5. How does caching work and where do you place caches?

> Part A: Fundamentals

**Answer:** Store hot data in fast memory to cut latency and DB load. Layers: browser, CDN, API gateway, application (Redis/Memcached), DB buffer pool. Key concerns: eviction (LRU/LFU/TTL), invalidation, hit ratio, consistency.

```mermaid
flowchart LR
    n0["Client"]
    n1["App"]
    n2["Cache"]
    n3["Hit: return data"]
    n4["Miss: read DB"]
    n5["Fill cache"]
    n0 --> n1
    n1 --> n2
    n2 --> n3
    n2 --> n4
    n4 --> n5
```

---
[⬆ Back to index](../../README.md#-question-index)
