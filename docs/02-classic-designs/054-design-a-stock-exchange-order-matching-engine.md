# 54. Design a stock exchange / order matching engine.

> Part B: Classic System Designs

**Answer:** Single-threaded deterministic matching per symbol (price-time priority) with in-memory order book, sequencer for total ordering, event-sourced journal replicated for recovery, market data publishers, risk checks at gateway, ultra-low latency networking.

```mermaid
flowchart TD
    n0["Orders"]
    n1["Gateway (risk checks)"]
    n2["Sequencer"]
    n3["Matching engine"]
    n4["Trades"]
    n5["Market data"]
    n0 --> n1
    n1 --> n2
    n2 --> n3
    n3 --> n4
    n4 --> n5
```

---
[⬆ Back to index](../../README.md#-question-index)
