# 78. Design an IoT telemetry platform.

> Part B: Classic System Designs

**Answer:** Devices publish via MQTT to brokers -> Kafka -> stream processing -> time-series DB + cold storage; device registry/shadow, OTA updates, auth via certificates, edge aggregation for intermittent connectivity.

```mermaid
flowchart LR
    n0["Devices"]
    n1["MQTT broker"]
    n2["Kafka"]
    n3["Time-series DB / lake"]
    n4["Dashboards / alerts"]
    n0 --> n1
    n1 --> n2
    n2 --> n3
    n3 --> n4
```

---
[⬆ Back to index](../../README.md#-question-index)
