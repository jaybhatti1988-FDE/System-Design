# 22. Polling vs long polling vs WebSockets vs SSE?

> Part A: Fundamentals

**Answer:** Polling: simple, wasteful. Long polling: server holds request until data. SSE: one-way server push over HTTP. WebSocket: full-duplex persistent connection (chat, games). Scale WebSockets with sticky routing and a pub/sub backplane.

```mermaid
flowchart LR
    n0["Client"]
    n1["WebSocket gateway"]
    n2["Pub/Sub backplane"]
    n3["Other gateways"]
    n0 --> n1
    n1 --> n2
    n2 --> n3
```

---
[⬆ Back to index](../../README.md#-question-index)
