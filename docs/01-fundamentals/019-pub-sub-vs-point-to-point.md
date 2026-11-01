# 19. Pub/Sub vs point-to-point?

> Part A: Fundamentals

**Answer:** Point-to-point: each message consumed by one consumer. Pub/Sub: each subscriber gets a copy (fan-out). Combine: fan-out to multiple queues, each with competing consumers.

```mermaid
flowchart LR
    n0["Publisher"]
    n1["Topic"]
    n2["Subscriber A"]
    n3["Subscriber B"]
    n0 --> n1
    n1 --> n2
    n1 --> n3
```

---
[⬆ Back to index](../../README.md#-question-index)
