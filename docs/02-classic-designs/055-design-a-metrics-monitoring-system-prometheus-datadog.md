# 55. Design a metrics/monitoring system (Prometheus/Datadog).

> Part B: Classic System Designs

**Answer:** Agents push/pull metrics -> Kafka -> time-series DB (compression, downsampling, retention tiers); query engine; alert evaluator -> notification routing; cardinality control; dashboards.

```mermaid
flowchart LR
    n0["Hosts"]
    n1["Collector"]
    n2["Kafka"]
    n3["Time-series DB"]
    n4["Dashboards"]
    n5["Alert manager"]
    n0 --> n1
    n1 --> n2
    n2 --> n3
    n3 --> n4
    n3 --> n5
```

---
[⬆ Back to index](../../README.md#-question-index)
