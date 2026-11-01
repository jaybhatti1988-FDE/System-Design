# 48. Design a ticket booking system (Ticketmaster).

> Part B: Classic System Designs

**Answer:** Prevent double-booking: seat hold with TTL (Redis lock or DB row version/optimistic lock), then payment, then confirm. Use virtual waiting room/queue for flash demand, inventory in strongly consistent DB, idempotent payments.

```mermaid
flowchart LR
    n0["Select seat"]
    n1["Hold seat (TTL 5 min)"]
    n2["Pay"]
    n3["Confirm"]
    n4["Expired: release seat"]
    n0 --> n1
    n1 --> n2
    n2 --> n3
    n1 --> n4
```

> 📘 **Want more?** Read the [deep dive: Ticket Booking (Ticketmaster)](../deep-dives/09-ticket-booking.md)

---
[⬆ Back to index](../../README.md#-question-index)
