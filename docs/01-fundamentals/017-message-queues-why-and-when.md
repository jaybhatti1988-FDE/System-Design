# 17. Message queues: why and when?

> Part A: Fundamentals

**Answer:** Decouple producers and consumers, absorb spikes, enable async processing and retries. Semantics: at-most-once, at-least-once (default; needs idempotent consumers), exactly-once (hard; transactions/dedup). Use DLQs for poison messages.

```mermaid
flowchart LR
    n0["Producer"]
    n1["Queue"]
    n2["Consumers"]
    n3["DLQ after repeated failure"]
    n0 --> n1
    n1 --> n2
    n2 --> n3
```

---
[⬆ Back to index](../../README.md#-question-index)
