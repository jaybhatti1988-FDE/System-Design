# 11. Database replication models?

> Part A: Fundamentals

**Answer:** Leader-follower (writes to leader, reads from followers; sync/async), multi-leader (multi-region writes, conflict resolution), leaderless (quorum, Dynamo style). Trade-offs: replication lag, failover, conflicts.

```mermaid
flowchart LR
    n0["Writes"]
    n1["Leader"]
    n2["Follower 1"]
    n3["Follower 2"]
    n4["Reads"]
    n0 --> n1
    n1 --> n2
    n1 --> n3
    n4 --> n2
    n4 --> n3
```

---
[⬆ Back to index](../../README.md#-question-index)
