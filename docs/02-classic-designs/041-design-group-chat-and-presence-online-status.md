# 41. Design group chat and presence (online status).

> Part B: Classic System Designs

**Answer:** Group messages fan-out to members (small groups push, large via pull/channels). Presence via heartbeats stored in Redis with TTL; publish status changes only to friends who are online; avoid broadcasting every blip (debounce).

```mermaid
flowchart LR
    n0["Client"]
    n1["Heartbeat"]
    n2["Presence service (Redis TTL)"]
    n3["Pub/Sub"]
    n4["Online friends"]
    n0 --> n1
    n1 --> n2
    n2 --> n3
    n3 --> n4
```

---
[⬆ Back to index](../../README.md#-question-index)
