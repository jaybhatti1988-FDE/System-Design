# 59. Design a distributed lock service.

> Part B: Classic System Designs

**Answer:** Use Redis SET NX PX with unique token + Lua release, or better ZooKeeper/etcd ephemeral nodes with leases. Add fencing tokens (monotonic) so stale holders cannot write. Beware clock drift, GC pauses, and prefer idempotency over locks where possible.

```mermaid
flowchart LR
    n0["Client"]
    n1["etcd lease key"]
    n2["Fencing token n"]
    n3["Storage rejects stale tokens"]
    n0 --> n1
    n1 --> n2
    n2 --> n3
```

---
[⬆ Back to index](../../README.md#-question-index)
