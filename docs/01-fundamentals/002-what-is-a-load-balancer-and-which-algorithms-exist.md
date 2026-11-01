# 2. What is a load balancer and which algorithms exist?

> Part A: Fundamentals

**Answer:** Distributes traffic across servers for availability and throughput. L4 (TCP/IP, fast) vs L7 (HTTP aware, routing by path/header). Algorithms: round robin, weighted RR, least connections, IP hash, consistent hashing. Use health checks and run LBs in active-passive or active-active pairs.

```mermaid
flowchart LR
    n0["Client"]
    n1["Load balancer"]
    n2["Server 1"]
    n3["Server 2"]
    n4["Server 3"]
    n0 --> n1
    n1 --> n2
    n1 --> n3
    n1 --> n4
```

---
[⬆ Back to index](../../README.md#-question-index)
