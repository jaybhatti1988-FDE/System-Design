# 15. What is an API gateway?

> Part A: Fundamentals

**Answer:** Single entry point handling routing, auth, rate limiting, TLS termination, request aggregation, logging and versioning in front of microservices. Avoid making it a bottleneck: scale horizontally and keep business logic out.

```mermaid
flowchart LR
    n0["Clients"]
    n1["API gateway: auth, rate limit"]
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
