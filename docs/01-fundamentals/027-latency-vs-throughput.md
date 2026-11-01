# 27. Latency vs throughput?

> Part A: Fundamentals

**Answer:** Latency = time per request (watch p50/p95/p99); throughput = requests/sec. Improve latency via caching, locality, async, fewer hops; throughput via parallelism, batching, queues. Batching raises throughput but adds latency.

```mermaid
flowchart LR
    n0["Batching"]
    n1["Higher throughput"]
    n2["Higher latency"]
    n3["Caching"]
    n4["Lower latency"]
    n0 --> n1
    n1 --> n2
    n3 --> n4
```

---
[⬆ Back to index](../../README.md#-question-index)
