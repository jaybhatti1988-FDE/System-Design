# 51. Design a flash sale system.

> Part B: Classic System Designs

**Answer:** Absorb spikes: CDN static, rate limit/queue at edge, pre-load stock in Redis with atomic DECR, async order creation via queue, DB write on confirmation only, overselling prevention, idempotent orders, degrade non-critical features.

```mermaid
flowchart TD
    n0["Users"]
    n1["CDN / WAF"]
    n2["Queue"]
    n3["Redis stock DECR"]
    n4["Order workers"]
    n5["DB"]
    n0 --> n1
    n1 --> n2
    n2 --> n3
    n3 --> n4
    n4 --> n5
```

---
[⬆ Back to index](../../README.md#-question-index)
