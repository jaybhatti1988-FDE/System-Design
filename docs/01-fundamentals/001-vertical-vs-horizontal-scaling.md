# 1. Vertical vs horizontal scaling?

> Part A: Fundamentals

**Answer:** Vertical = bigger machine (simple, limited, single point of failure). Horizontal = more machines (needs stateless services, load balancing, data partitioning; near-unlimited scale). Prefer horizontal for web tiers; scale DBs vertically first, then replicate and shard.

```mermaid
flowchart LR
    n0["Small server"]
    n1["Bigger server (vertical)"]
    n2["Many servers behind a load balancer (horizontal)"]
    n0 --> n1
    n0 --> n2
```

---
[⬆ Back to index](../../README.md#-question-index)
