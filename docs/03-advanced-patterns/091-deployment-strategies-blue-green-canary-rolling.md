# 91. Deployment strategies: blue-green, canary, rolling?

> Part C: Advanced Patterns and Reliability

**Answer:** Blue-green: two environments, switch traffic instantly, easy rollback. Canary: route small percentage, watch metrics, ramp up. Rolling: replace instances gradually. Use feature flags and backward-compatible DB migrations (expand/contract).

```mermaid
flowchart LR
    n0["Load balancer"]
    n1["95% to v1"]
    n2["5% to v2 (canary)"]
    n0 --> n1
    n0 --> n2
```

---
[⬆ Back to index](../../README.md#-question-index)
