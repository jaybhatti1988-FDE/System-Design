# 25. How do you estimate capacity (back-of-envelope)?

> Part A: Fundamentals

**Answer:** QPS = DAU x actions/day / 86400; peak ≈ 2-5x avg. Storage = items/day x size x retention x replication. Bandwidth = QPS x payload. Remember: 1 day ≈ 10^5 s, 1M req/day ≈ 12 QPS. Latency numbers: memory ~100ns, SSD ~100µs, same-DC RTT ~0.5ms, cross-continent ~150ms.

```mermaid
flowchart LR
    n0["100M DAU x 10 req/day"]
    n1["Divide by 86,400 s"]
    n2["~11.5K QPS average"]
    n3["x3 for peak"]
    n4["~35K QPS"]
    n0 --> n1
    n1 --> n2
    n2 --> n3
    n3 --> n4
```

---
[⬆ Back to index](../../README.md#-question-index)
