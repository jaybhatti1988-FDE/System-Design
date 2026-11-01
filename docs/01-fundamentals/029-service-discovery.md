# 29. Service discovery?

> Part A: Fundamentals

**Answer:** Services register with a registry (Consul, etcd, Eureka, Kubernetes DNS) and clients find healthy instances. Client-side discovery (client picks instance) vs server-side (LB/proxy does). Use heartbeats/TTL to drop dead nodes; service mesh (Envoy/Istio) adds sidecar routing.

```mermaid
flowchart LR
    n0["Service"]
    n1["Registers in registry"]
    n2["Client"]
    n3["Looks up registry"]
    n4["Healthy instance"]
    n0 --> n1
    n2 --> n3
    n3 --> n4
```

---
[⬆ Back to index](../../README.md#-question-index)
