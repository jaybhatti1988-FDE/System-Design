# 97. Handling time, ordering and clocks in distributed systems?

> Part C: Advanced Patterns and Reliability

**Answer:** Physical clocks drift; use logical clocks (Lamport), vector clocks for causality, hybrid logical clocks, or TrueTime-style bounded uncertainty. Order per partition via sequence numbers; avoid relying on wall-clock for correctness (use fencing tokens).

```mermaid
flowchart LR
    n0["A: clock 1"]
    n1["B: clock 2"]
    n2["C: clock 3"]
    n0 --> n1
    n1 --> n2
```

---
[⬆ Back to index](../../README.md#-question-index)
