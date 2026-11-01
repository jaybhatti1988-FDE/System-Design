# 100. How do you scale a system from 0 to millions of users?

> Part C: Advanced Patterns and Reliability

**Answer:** Start with a single server; separate web and DB; add load balancer and stateless app tier; DB replication, cache, CDN; move assets to object storage; shard the DB; introduce queues/async workers; split into services; multi-region; invest in monitoring and automation at each step. Optimize the current bottleneck, measured, not guessed.

```mermaid
flowchart TD
    n0["1 server"]
    n1["LB + N app servers"]
    n2["Cache + CDN"]
    n3["Read replicas"]
    n4["Shards"]
    n5["Services"]
    n6["Multi-region"]
    n0 --> n1
    n1 --> n2
    n2 --> n3
    n3 --> n4
    n4 --> n5
    n5 --> n6
```

---
[⬆ Back to index](../../README.md#-question-index)
