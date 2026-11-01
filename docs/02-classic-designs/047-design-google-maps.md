# 47. Design Google Maps.

> Part B: Classic System Designs

**Answer:** Map tiles (pre-rendered vector/raster pyramid by zoom) on CDN; road network graph partitioned hierarchically; routing with A*/Contraction Hierarchies; live traffic from probe data via streaming; ETA service; geocoding index.

```mermaid
flowchart LR
    n0["Client"]
    n1["Tile CDN"]
    n2["Routing service (graph shards)"]
    n3["Traffic stream"]
    n0 --> n1
    n0 --> n2
    n2 --> n3
```

---
[⬆ Back to index](../../README.md#-question-index)
