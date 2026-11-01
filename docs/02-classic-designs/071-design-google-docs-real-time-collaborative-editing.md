# 71. Design Google Docs (real-time collaborative editing).

> Part B: Classic System Designs

**Answer:** Concurrent edits merged by Operational Transformation (central server transforms ops) or CRDTs (commutative, peer-friendly). WebSocket per doc session, ops log + periodic snapshots, cursor presence, offline sync, version history.

```mermaid
flowchart LR
    n0["Clients"]
    n1["Collab server (OT / CRDT)"]
    n2["Broadcast to clients"]
    n3["Ops log + snapshots"]
    n0 --> n1
    n1 --> n2
    n1 --> n3
```

---
[⬆ Back to index](../../README.md#-question-index)
