# 48. Design a ticket booking system (Ticketmaster).

> Part B: Classic System Designs

**Answer:** Prevent double-booking: seat hold with TTL (Redis lock or DB row version/optimistic lock), then payment, then confirm. Use virtual waiting room/queue for flash demand, inventory in strongly consistent DB, idempotent payments.

```
Select -> HOLD(seat, ttl 5m) -> Pay -> CONFIRM | expire -> release
```

---
[⬆ Back to index](../../README.md#-question-index)
