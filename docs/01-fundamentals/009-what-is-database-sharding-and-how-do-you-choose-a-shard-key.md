# 9. What is database sharding and how do you choose a shard key?

> Part A: Fundamentals

**Answer:** Splitting data across nodes. Strategies: range, hash, directory/lookup, geo. A good key has high cardinality, even distribution, and matches query patterns (avoids cross-shard queries). Challenges: hotspots, resharding, joins, transactions.

```mermaid
flowchart LR
    n0["user_id hash mod 3"]
    n1["Shard 0"]
    n2["Shard 1"]
    n3["Shard 2"]
    n0 --> n1
    n0 --> n2
    n0 --> n3
```

---
[⬆ Back to index](../../README.md#-question-index)
