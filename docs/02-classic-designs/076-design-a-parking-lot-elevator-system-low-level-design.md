# 76. Design a parking lot / elevator system (low-level design).

> Part B: Classic System Designs

**Answer:** Identify entities (Lot, Level, Spot, Ticket, Vehicle, Payment), use enums and state machines, strategy pattern for pricing/spot allocation, thread-safe allocation, then extend to distributed (sharded by lot, DB constraints).

```mermaid
flowchart TD
    n0["Vehicle"]
    n1["Gate"]
    n2["Spot allocator"]
    n3["Ticket"]
    n4["Payment"]
    n5["Exit"]
    n0 --> n1
    n1 --> n2
    n2 --> n3
    n3 --> n4
    n4 --> n5
```

---
[⬆ Back to index](../../README.md#-question-index)
