# 39. Design Instagram.

> Part B: Classic System Designs

**Answer:** Photo upload to object storage (multiple resolutions via async workers), metadata in sharded DB, follow graph, feed generation (hybrid), CDN for delivery, likes/comments counters via eventual consistency, explore/recommendation pipeline.

```mermaid
flowchart LR
    n0["Upload"]
    n1["Object store"]
    n2["Resize workers"]
    n3["CDN"]
    n4["Metadata DB shards"]
    n5["Feed cache"]
    n0 --> n1
    n1 --> n2
    n2 --> n3
    n0 --> n4
    n4 --> n5
```

---
[⬆ Back to index](../../README.md#-question-index)
