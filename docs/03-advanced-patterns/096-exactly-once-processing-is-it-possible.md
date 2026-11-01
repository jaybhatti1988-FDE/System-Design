# 96. Exactly-once processing: is it possible?

> Part C: Advanced Patterns and Reliability

**Answer:** Truly exactly-once delivery is impossible over unreliable networks; achieve effectively-once via at-least-once delivery + idempotent/transactional processing (dedup keys, Kafka transactions, atomic offset+state commit).

```
retry delivery + dedup(id) = effectively once
```

---
[⬆ Back to index](../../README.md#-question-index)
