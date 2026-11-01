# 87. Quorum reads/writes?

> Part C: Advanced Patterns and Reliability

**Answer:** With N replicas, write to W and read from R; R+W>N guarantees overlap with the latest write. Tune: W=N (fast reads), R=1; or majority for balance. Sloppy quorums + hinted handoff boost availability.

```mermaid
flowchart LR
    n0["N=3, W=2, R=2"]
    n1["Write to A, B"]
    n2["B overlaps"]
    n3["Latest value found"]
    n4["Read from B, C"]
    n0 --> n1
    n1 --> n2
    n2 --> n3
    n0 --> n4
    n4 --> n2
```

---
[⬆ Back to index](../../README.md#-question-index)
