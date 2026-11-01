# 18. Kafka vs RabbitMQ / SQS?

> Part A: Fundamentals

**Answer:** Kafka: distributed append-only log, partitions for ordering and parallelism, replay, high throughput, consumer groups. RabbitMQ/SQS: broker-style queues with per-message ack, routing, simpler task queues. Choose Kafka for streaming/event sourcing, SQS/Rabbit for job queues.

```mermaid
flowchart LR
    n0["Producer"]
    n1["Topic partitions P0, P1"]
    n2["Consumer group"]
    n0 --> n1
    n1 --> n2
```

---
[⬆ Back to index](../../README.md#-question-index)
