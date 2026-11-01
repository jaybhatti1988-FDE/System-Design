# 81. What is the Saga pattern?

> Part C: Advanced Patterns and Reliability

**Answer:** Long-running distributed transaction as a sequence of local transactions, each with a compensating action. Orchestration (central coordinator) vs choreography (events). Gives eventual consistency without 2PC locks.

```mermaid
flowchart LR
    n0["Order"]
    n1["Reserve stock"]
    n2["Charge"]
    n3["Ship"]
    n4["Fails: release stock"]
    n5["Cancel order"]
    n0 --> n1
    n1 --> n2
    n2 --> n3
    n2 --> n4
    n4 --> n5
```

---
[⬆ Back to index](../../README.md#-question-index)
