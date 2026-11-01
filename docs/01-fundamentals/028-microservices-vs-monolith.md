# 28. Microservices vs monolith?

> Part A: Fundamentals

**Answer:** Monolith: simple to build, deploy, test; scales as one unit. Microservices: independent scaling/deploys/tech, team autonomy; cost is network failures, distributed transactions, observability. Start modular monolith, split on clear boundaries.

```mermaid
flowchart LR
    n0["Monolith: A + B + C"]
    n1["Split on clear boundaries"]
    n2["Service A"]
    n3["Service B"]
    n4["Service C"]
    n0 --> n1
    n1 --> n2
    n1 --> n3
    n1 --> n4
```

---
[⬆ Back to index](../../README.md#-question-index)
