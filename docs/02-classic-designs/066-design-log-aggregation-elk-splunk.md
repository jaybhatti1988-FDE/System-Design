# 66. Design log aggregation (ELK/Splunk).

> Part B: Classic System Designs

**Answer:** Agents (Filebeat/Fluentd) ship logs -> Kafka buffer -> parser/enricher -> index (Elasticsearch) hot/warm/cold tiers + raw archive in object storage; retention, sampling, PII scrubbing, dashboards and alerts.

```mermaid
flowchart TD
    n0["Apps"]
    n1["Agent"]
    n2["Kafka"]
    n3["Parser"]
    n4["Elasticsearch"]
    n5["Kibana"]
    n0 --> n1
    n1 --> n2
    n2 --> n3
    n3 --> n4
    n4 --> n5
```

---
[⬆ Back to index](../../README.md#-question-index)
