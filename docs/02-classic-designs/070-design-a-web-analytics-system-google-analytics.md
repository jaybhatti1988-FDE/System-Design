# 70. Design a web analytics system (Google Analytics).

> Part B: Classic System Designs

**Answer:** JS tracker -> collector endpoint -> Kafka -> stream processing (sessionization, dedup, bot filter) -> OLAP store for dashboards; raw data lake for batch; sampling/pre-aggregation to control cost.

```mermaid
flowchart TD
    n0["Browser"]
    n1["Collector"]
    n2["Kafka"]
    n3["Flink"]
    n4["OLAP"]
    n5["Dashboard"]
    n0 --> n1
    n1 --> n2
    n2 --> n3
    n3 --> n4
    n4 --> n5
```

---
[⬆ Back to index](../../README.md#-question-index)
