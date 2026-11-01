# 84. Transactional Outbox pattern?

> Part C: Advanced Patterns and Reliability

**Answer:** Write business data and an outbox event row in the same DB transaction; a relay (poller or CDC like Debezium) publishes to the broker. Guarantees no lost or phantom events; consumers must be idempotent.

```mermaid
flowchart LR
    n0["Transaction: update order + insert outbox"]
    n1["CDC relay"]
    n2["Kafka"]
    n0 --> n1
    n1 --> n2
```

---
[⬆ Back to index](../../README.md#-question-index)
