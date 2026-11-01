# 83. CQRS and Event Sourcing?

> Part C: Advanced Patterns and Reliability

**Answer:** CQRS separates write model from optimized read models. Event sourcing stores every state change as an immutable event; state = replay; supports audit and time travel; requires snapshots and event versioning. Projections update read stores asynchronously.

```mermaid
flowchart LR
    n0["Command"]
    n1["Event store"]
    n2["Projector"]
    n3["Read DB"]
    n4["Query"]
    n0 --> n1
    n1 --> n2
    n2 --> n3
    n3 --> n4
```

---
[⬆ Back to index](../../README.md#-question-index)
