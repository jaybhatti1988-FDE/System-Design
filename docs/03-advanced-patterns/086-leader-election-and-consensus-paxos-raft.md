# 86. Leader election and consensus (Paxos/Raft)?

> Part C: Advanced Patterns and Reliability

**Answer:** Raft: terms, randomized election timeouts, leader replicates log entries, committed when a majority acks; safety through log matching and majority quorums. Used by etcd, Consul. ZooKeeper uses ZAB. Tolerates f failures with 2f+1 nodes.

```mermaid
flowchart LR
    n0["Follower"]
    n1["Candidate (election timeout)"]
    n2["Leader (majority votes)"]
    n3["AppendEntries to followers"]
    n0 --> n1
    n1 --> n2
    n2 --> n3
```

---
[⬆ Back to index](../../README.md#-question-index)
