# 82. Two-phase commit (2PC) vs 3PC vs Saga?

> Part C: Advanced Patterns and Reliability

**Answer:** 2PC: coordinator asks prepare, then commit; atomic but blocking if the coordinator fails and slow. 3PC reduces blocking but is rarely used. Saga trades atomicity for availability. Use 2PC inside tightly-coupled DBs, Saga across services.

```mermaid
flowchart LR
    n0["Coordinator: PREPARE"]
    n1["All vote yes"]
    n2["COMMIT"]
    n3["Any vote no"]
    n4["ABORT"]
    n0 --> n1
    n1 --> n2
    n0 --> n3
    n3 --> n4
```

---
[⬆ Back to index](../../README.md#-question-index)
