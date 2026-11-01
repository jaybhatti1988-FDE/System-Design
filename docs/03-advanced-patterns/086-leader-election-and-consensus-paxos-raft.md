# 86. Leader election and consensus (Paxos/Raft)?

> Part C: Advanced Patterns and Reliability

**Answer:** Raft: terms, randomized election timeouts, leader replicates log entries, committed when a majority acks; safety through log matching and majority quorums. Used by etcd, Consul. ZooKeeper uses ZAB. Tolerates f failures with 2f+1 nodes.

```
Follower -timeout-> Candidate -majority-> Leader -> AppendEntries
```

---
[⬆ Back to index](../../README.md#-question-index)
