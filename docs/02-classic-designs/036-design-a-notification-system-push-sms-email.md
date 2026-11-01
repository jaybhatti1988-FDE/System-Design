# 36. Design a notification system (push/SMS/email).

> Part B: Classic System Designs

**Answer:** API validates and enqueues; per-channel queues and workers call providers (APNs/FCM, Twilio, SES); user preferences, templates, rate limiting, dedup, retries with backoff, DLQ, delivery tracking and analytics.

```
Service -> [Notif API] -> Kafka -> Push/SMS/Email workers -> Providers
```

---
[⬆ Back to index](../../README.md#-question-index)
