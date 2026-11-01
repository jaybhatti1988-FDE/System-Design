# 96. Exactly-once processing: is it possible?

> Part C: Advanced Patterns and Reliability

**Answer:** Truly exactly-once delivery is impossible over unreliable networks; achieve effectively-once via at-least-once delivery + idempotent/transactional processing (dedup keys, Kafka transactions, atomic offset+state commit).

```mermaid
flowchart LR
    n0["At-least-once delivery (retries)"]
    n1["Dedup by id / transactions"]
    n2["Effectively once"]
    n0 --> n1
    n1 --> n2
```

---
[⬆ Back to index](../../README.md#-question-index)
