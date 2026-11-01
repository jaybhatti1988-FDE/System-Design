# 3. Explain the CAP theorem.

> Part A: Fundamentals

**Answer:** During a network partition you must choose Consistency or Availability. CP: reject/delay requests to stay consistent (HBase, etcd, MongoDB default). AP: serve possibly stale data (Cassandra, DynamoDB). Without partition, trade latency vs consistency (PACELC).

```mermaid
flowchart LR
    n0["Network partition"]
    n1["CP: stay consistent (reject requests)"]
    n2["AP: stay available (may be stale)"]
    n0 --> n1
    n0 --> n2
```

---
[⬆ Back to index](../../README.md#-question-index)
