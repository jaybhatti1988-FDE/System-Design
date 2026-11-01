# 92. Multi-region architecture and disaster recovery?

> Part C: Advanced Patterns and Reliability

**Answer:** Active-passive (cheaper, failover with RPO/RTO) vs active-active (low latency, needs conflict handling, global data replication, geo-DNS/anycast routing). Define RPO/RTO, regularly test failover, avoid cross-region sync calls on the critical path.

```
GeoDNS -> Region A (primary) <-replication-> Region B (standby/active)
```

---
[⬆ Back to index](../../README.md#-question-index)
