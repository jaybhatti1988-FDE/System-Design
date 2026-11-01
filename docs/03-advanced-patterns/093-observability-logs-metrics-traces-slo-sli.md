# 93. Observability: logs, metrics, traces, SLO/SLI?

> Part C: Advanced Patterns and Reliability

**Answer:** Metrics (RED: rate, errors, duration; USE for resources), structured logs with correlation IDs, distributed traces. Define SLIs/SLOs and error budgets; alert on symptoms (user impact) not causes; runbooks and post-mortems.

```mermaid
flowchart LR
    n0["Service"]
    n1["Metrics"]
    n2["Dashboards + alerts"]
    n3["Logs"]
    n4["Traces"]
    n0 --> n1
    n1 --> n2
    n0 --> n3
    n3 --> n2
    n0 --> n4
    n4 --> n2
```

---
[⬆ Back to index](../../README.md#-question-index)
