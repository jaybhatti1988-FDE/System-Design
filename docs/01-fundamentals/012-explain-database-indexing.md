# 12. Explain database indexing.

> Part A: Fundamentals

**Answer:** Auxiliary structure (B-tree, hash, LSM, inverted, geo) for fast lookups at the cost of write overhead and storage. Use composite indexes in query order, covering indexes, avoid indexing low-cardinality columns, and check query plans.

```mermaid
flowchart LR
    n0["Query"]
    n1["Index (B-tree)"]
    n2["Row pointer"]
    n3["Table row"]
    n0 --> n1
    n1 --> n2
    n2 --> n3
```

---
[⬆ Back to index](../../README.md#-question-index)
