# 97. Handling time, ordering and clocks in distributed systems?

> Part C: Advanced Patterns and Reliability

**Answer:** Physical clocks drift; use logical clocks (Lamport), vector clocks for causality, hybrid logical clocks, or TrueTime-style bounded uncertainty. Order per partition via sequence numbers; avoid relying on wall-clock for correctness (use fencing tokens).

```
A:1 -> B:2 -> C:3     (Lamport: max(local, recv) + 1)
```

---
[⬆ Back to index](../../README.md#-question-index)
