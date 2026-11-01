# 61. Design a leaderboard.

> Part B: Classic System Designs

**Answer:** Redis sorted sets (ZADD, ZREVRANGE, ZRANK) give O(log N) updates and top-K; shard by score range or user for huge scale; persist to DB; periodic snapshots for daily/weekly boards; approximate rank for large N.

```mermaid
flowchart LR
    n0["Score event"]
    n1["Redis sorted set"]
    n2["Top 10"]
    n3["My rank"]
    n0 --> n1
    n1 --> n2
    n1 --> n3
```

---
[⬆ Back to index](../../README.md#-question-index)
