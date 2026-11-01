# 34. Design a unique ID generator.

> Part B: Classic System Designs

**Answer:** Snowflake: 64-bit = timestamp(41) + datacenter/machine(10) + sequence(12); time-sortable, no coordination (needs clock sync handling). Alternatives: UUID (large, unordered), DB ticket servers, ULID.

```mermaid
flowchart LR
    n0["Sign bit 0"]
    n1["Timestamp 41 bits"]
    n2["Machine ID 10 bits"]
    n3["Sequence 12 bits"]
    n0 --> n1
    n1 --> n2
    n2 --> n3
```

---
[⬆ Back to index](../../README.md#-question-index)
