# 16. How do you design a rate limiter?

> Part A: Fundamentals

**Answer:** Algorithms: token bucket (bursts allowed), leaky bucket (smooth), fixed window (boundary burst issue), sliding window log/counter. Store counters in Redis with atomic Lua/INCR + TTL, keyed by user/IP/API key. Return 429 with Retry-After. Distributed: central Redis or local limit + sync.

```
Req -> [Limiter: Redis counters] -> allow -> Service
                                 -> deny 429
```

---
[⬆ Back to index](../../README.md#-question-index)
