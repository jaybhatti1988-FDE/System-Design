# 56. Design an ad click aggregation system.

> Part B: Classic System Designs

**Answer:** Click events -> Kafka -> stream processor (Flink) with tumbling windows aggregates per ad/minute, dedup by click id, late data via watermarks; store aggregates in OLAP DB (Druid/ClickHouse) and raw events in object storage; reconcile with batch (lambda/kappa).

```mermaid
flowchart LR
    n0["Clicks"]
    n1["Kafka"]
    n2["Flink windows"]
    n3["OLAP DB"]
    n4["Raw events in S3"]
    n5["Batch reconcile"]
    n0 --> n1
    n1 --> n2
    n2 --> n3
    n1 --> n4
    n4 --> n5
```

---
[⬆ Back to index](../../README.md#-question-index)
