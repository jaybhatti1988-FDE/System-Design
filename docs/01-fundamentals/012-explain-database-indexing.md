# 12. Explain database indexing.

> Part A: Fundamentals

**Answer:** Auxiliary structure (B-tree, hash, LSM, inverted, geo) for fast lookups at the cost of write overhead and storage. Use composite indexes in query order, covering indexes, avoid indexing low-cardinality columns, and check query plans.

```
B-tree:        [50]
              /    \
        [20,30]    [70,90] -> leaf -> row pointer
```

---
[⬆ Back to index](../../README.md#-question-index)
