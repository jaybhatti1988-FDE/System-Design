# 53. Design a digital wallet.

> Part B: Classic System Designs

**Answer:** Balance changes via double-entry ledger in ACID DB; transfers between shards via distributed transaction (2PC or saga with reservation) or event sourcing with replay; idempotent ops; audit log; fraud checks.

```mermaid
flowchart LR
    n0["Debit A (hold)"]
    n1["Credit B"]
    n2["Commit"]
    n3["Failure: compensate"]
    n0 --> n1
    n1 --> n2
    n1 --> n3
```

---
[⬆ Back to index](../../README.md#-question-index)
