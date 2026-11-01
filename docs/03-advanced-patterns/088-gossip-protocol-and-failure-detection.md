# 88. Gossip protocol and failure detection?

> Part C: Advanced Patterns and Reliability

**Answer:** Nodes periodically exchange state with random peers; information spreads in O(log N) rounds; scalable membership and failure detection (heartbeat counters, phi-accrual) without a central coordinator (Cassandra, Consul).

```mermaid
flowchart LR
    n0["Node A"]
    n1["Node D"]
    n2["Node F"]
    n3["Node B"]
    n4["Eventually all nodes know"]
    n0 --> n1
    n1 --> n2
    n2 --> n3
    n3 --> n4
```

---
[⬆ Back to index](../../README.md#-question-index)
