# 18. Kafka vs RabbitMQ / SQS?

> Part A: Fundamentals

**Answer:** Kafka: distributed append-only log, partitions for ordering and parallelism, replay, high throughput, consumer groups. RabbitMQ/SQS: broker-style queues with per-message ack, routing, simpler task queues. Choose Kafka for streaming/event sourcing, SQS/Rabbit for job queues.

```
Topic: P0 [0 1 2 3]  P1 [0 1 2]    Consumer group reads per partition
```

---
[⬆ Back to index](../../README.md#-question-index)
