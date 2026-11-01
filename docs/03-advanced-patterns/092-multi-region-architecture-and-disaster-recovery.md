# 92. Multi-region architecture and disaster recovery?

> Part C: Advanced Patterns and Reliability

**Answer:** Active-passive (cheaper, failover with RPO/RTO) vs active-active (low latency, needs conflict handling, global data replication, geo-DNS/anycast routing). Define RPO/RTO, regularly test failover, avoid cross-region sync calls on the critical path.

```mermaid
flowchart LR
    n0["Geo DNS"]
    n1["Region A (primary)"]
    n2["Replication"]
    n3["Region B (standby / active)"]
    n0 --> n1
    n1 --> n2
    n2 --> n3
```

---
[⬆ Back to index](../../README.md#-question-index)
