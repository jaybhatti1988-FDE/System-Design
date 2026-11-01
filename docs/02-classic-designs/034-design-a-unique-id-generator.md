# 34. Design a unique ID generator.

> Part B: Classic System Designs

**Answer:** Snowflake: 64-bit = timestamp(41) + datacenter/machine(10) + sequence(12); time-sortable, no coordination (needs clock sync handling). Alternatives: UUID (large, unordered), DB ticket servers, ULID.

```
[0 | timestamp 41 | machine 10 | seq 12]
```

---
[⬆ Back to index](../../README.md#-question-index)
