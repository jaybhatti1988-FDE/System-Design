# 26. Availability and SLAs: how do you reach 99.99%?

> Part A: Fundamentals

**Answer:** 99.99% ≈ 52 min downtime/year. Remove single points of failure: redundancy across AZs/regions, health checks, auto-failover, graceful degradation, retries with backoff, circuit breakers, canary deploys, and chaos testing. Availability of serial components multiplies; parallel redundancy improves it.

```mermaid
flowchart LR
    n0["Load balancer"]
    n1["AZ1: app + DB"]
    n2["AZ2: app + DB replica"]
    n0 --> n1
    n0 --> n2
```

---
[⬆ Back to index](../../README.md#-question-index)
