# 45. Design Uber / ride hailing.

> Part B: Classic System Designs

**Answer:** Drivers send location every ~4s to a location service (geohash/quadtree/S2 index in Redis); rider request -> matching service finds nearby drivers, ranks by ETA, offers with timeout; trip service state machine; pricing (surge); maps/ETA; payments. Use WebSockets for live updates.

```mermaid
flowchart LR
    n0["Driver"]
    n1["Location service (geo index)"]
    n2["Matching service"]
    n3["Rider"]
    n4["Trip service"]
    n5["Payments"]
    n0 --> n1
    n1 --> n2
    n3 --> n2
    n2 --> n4
    n4 --> n5
```

> 📘 **Want more?** Read the [deep dive: Ride Hailing (Uber)](../deep-dives/07-ride-hailing.md)

---
[⬆ Back to index](../../README.md#-question-index)
