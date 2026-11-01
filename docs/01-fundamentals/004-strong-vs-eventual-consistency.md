# 4. Strong vs eventual consistency?

> Part A: Fundamentals

**Answer:** Strong: every read sees the latest write (linearizable; higher latency). Eventual: replicas converge over time (low latency, high availability). Intermediate: read-your-writes, monotonic reads, causal consistency. Pick strong for payments/inventory, eventual for feeds/likes.

```mermaid
flowchart LR
    n0["Write"]
    n1["Leader"]
    n2["Replica (async: may be stale)"]
    n3["Replica (sync: always fresh)"]
    n0 --> n1
    n1 --> n2
    n1 --> n3
```

---
[⬆ Back to index](../../README.md#-question-index)
