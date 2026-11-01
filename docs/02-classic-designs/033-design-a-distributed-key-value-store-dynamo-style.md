# 33. Design a distributed key-value store (Dynamo-style).

> Part B: Classic System Designs

**Answer:** Partition via consistent hashing, replicate to N nodes, quorum reads/writes (R+W>N), vector clocks or LWW for conflicts, hinted handoff, read repair, anti-entropy with Merkle trees, gossip for membership, LSM storage with WAL.

```mermaid
flowchart LR
    n0["Client"]
    n1["Coordinator"]
    n2["Replica N1"]
    n3["Replica N2"]
    n4["Replica N3"]
    n0 --> n1
    n1 --> n2
    n1 --> n3
    n1 --> n4
```

---
[⬆ Back to index](../../README.md#-question-index)
