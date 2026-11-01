# 94. Data pipeline architectures: Lambda vs Kappa; batch vs stream?

> Part C: Advanced Patterns and Reliability

**Answer:** Lambda: batch layer (accurate) + speed layer (fast) merged at serving. Kappa: a single streaming path with log replay for reprocessing. Modern: stream-first with lakehouse (Iceberg/Delta), exactly-once semantics via checkpoints.

```mermaid
flowchart LR
    n0["Source"]
    n1["Kafka"]
    n2["Stream job"]
    n3["Serving"]
    n4["Lake (replay)"]
    n0 --> n1
    n1 --> n2
    n2 --> n3
    n1 --> n4
```

---
[⬆ Back to index](../../README.md#-question-index)
