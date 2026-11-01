# 85. Circuit breaker, retry, timeout, bulkhead?

> Part C: Advanced Patterns and Reliability

**Answer:** Timeouts bound waiting; retries with exponential backoff + jitter (only idempotent calls); circuit breaker opens after failures to fail fast and half-opens to probe; bulkheads isolate resource pools; fallbacks degrade gracefully.

```mermaid
flowchart LR
    n0["CLOSED"]
    n1["OPEN (failures over threshold)"]
    n2["HALF-OPEN (after timeout)"]
    n0 --> n1
    n1 --> n2
    n2 --> n0
    n2 --> n1
```

---
[⬆ Back to index](../../README.md#-question-index)
