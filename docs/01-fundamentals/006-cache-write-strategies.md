# 6. Cache write strategies?

> Part A: Fundamentals

**Answer:** Cache-aside (app loads on miss; most common). Read-through (cache loads). Write-through (write cache+DB synchronously; consistent, slower). Write-back (write cache, flush async; fast, risk of loss). Write-around (write DB only; avoids cache pollution).

```mermaid
flowchart LR
    n0["Write-through: App"]
    n1["Cache (wt)"]
    n2["DB (sync)"]
    n3["Write-back: App"]
    n4["Cache (wb)"]
    n5["DB (async flush)"]
    n0 --> n1
    n1 --> n2
    n3 --> n4
    n4 --> n5
```

---
[⬆ Back to index](../../README.md#-question-index)
