# 90. Backpressure and load shedding?

> Part C: Advanced Patterns and Reliability

**Answer:** Prevent overload by propagating slowness upstream: bounded queues, rate limits, reactive streams, shedding low-priority work (return 503/degrade), adaptive concurrency limits, autoscaling with warm capacity.

```mermaid
flowchart LR
    n0["Producer"]
    n1["Bounded queue"]
    n2["Consumer"]
    n3["Full: reject or slow producer"]
    n0 --> n1
    n1 --> n2
    n1 --> n3
```

---
[⬆ Back to index](../../README.md#-question-index)
