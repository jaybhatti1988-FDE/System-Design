# 77. Design a multiplayer game backend.

> Part B: Classic System Designs

**Answer:** Authoritative game servers with tick loops (20-60Hz), UDP/WebSocket, client prediction + reconciliation, matchmaking service (skill/latency), regional shards, session state in memory with snapshots, anti-cheat.

```mermaid
flowchart LR
    n0["Matchmaker"]
    n1["Game server (tick loop)"]
    n2["Clients"]
    n0 --> n1
    n1 --> n2
```

---
[⬆ Back to index](../../README.md#-question-index)
