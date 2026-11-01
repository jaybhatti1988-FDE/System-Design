# 57. Design a distributed message queue.

> Part B: Classic System Designs

**Answer:** Topics split into partitions, each an append-only log replicated (leader + ISR); producers pick partition by key; consumer groups track offsets; segment files, page cache, zero-copy; controller via ZooKeeper/Raft; retention and compaction.

```mermaid
flowchart LR
    n0["Producer"]
    n1["Broker (partition leader)"]
    n2["Replicas"]
    n3["Consumer group"]
    n0 --> n1
    n1 --> n2
    n3 --> n1
```

---
[⬆ Back to index](../../README.md#-question-index)
