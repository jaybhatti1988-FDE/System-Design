# 36. Design a notification system (push/SMS/email).

> Part B: Classic System Designs

**Answer:** API validates and enqueues; per-channel queues and workers call providers (APNs/FCM, Twilio, SES); user preferences, templates, rate limiting, dedup, retries with backoff, DLQ, delivery tracking and analytics.

```mermaid
flowchart LR
    n0["Service"]
    n1["Notification API"]
    n2["Kafka"]
    n3["Push / SMS / Email workers"]
    n4["Providers"]
    n0 --> n1
    n1 --> n2
    n2 --> n3
    n3 --> n4
```

> 📘 **Want more?** Read the [deep dive: Notification System](../deep-dives/05-notification-system.md)

---
[⬆ Back to index](../../README.md#-question-index)
