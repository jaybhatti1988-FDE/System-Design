# 49. Design a hotel reservation system (Airbnb/Booking).

> Part B: Classic System Designs

**Answer:** Inventory per room-type per date with unique constraint/optimistic locking to avoid overbooking; search via Elasticsearch with availability filter; reservation state machine; idempotency keys; payments via saga; reviews and ranking separate services.

```mermaid
flowchart LR
    n0["Search (Elasticsearch)"]
    n1["Reservation service"]
    n2["Inventory DB (lock)"]
    n3["Payment"]
    n0 --> n1
    n1 --> n2
    n2 --> n3
```

---
[⬆ Back to index](../../README.md#-question-index)
