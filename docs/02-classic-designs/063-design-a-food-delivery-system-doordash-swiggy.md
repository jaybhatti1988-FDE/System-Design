# 63. Design a food delivery system (DoorDash/Swiggy).

> Part B: Classic System Designs

**Answer:** Services: restaurants/menu, search, order, dispatch, tracking, payments, ETA. Dispatch matches courier by proximity and batching; order state machine with events; live location via streaming; ETA models.

```mermaid
flowchart LR
    n0["Order"]
    n1["Restaurant"]
    n2["Dispatch"]
    n3["Courier (live location)"]
    n4["Customer"]
    n0 --> n1
    n1 --> n2
    n2 --> n3
    n3 --> n4
```

---
[⬆ Back to index](../../README.md#-question-index)
