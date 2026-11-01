# 85. Circuit breaker, retry, timeout, bulkhead?

> Part C: Advanced Patterns and Reliability

**Answer:** Timeouts bound waiting; retries with exponential backoff + jitter (only idempotent calls); circuit breaker opens after failures to fail fast and half-opens to probe; bulkheads isolate resource pools; fallbacks degrade gracefully.

```
CLOSED -fail threshold-> OPEN -timeout-> HALF-OPEN -> CLOSED/OPEN
```

---
[⬆ Back to index](../../README.md#-question-index)
