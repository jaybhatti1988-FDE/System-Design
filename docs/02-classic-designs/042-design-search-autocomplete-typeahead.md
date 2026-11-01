# 42. Design search autocomplete (typeahead).

> Part B: Classic System Designs

**Answer:** Trie (or prefix index) with top-K suggestions cached per node; built offline from query logs (aggregated by frequency/recency), served from memory/Redis; client debounce; shard by prefix; update via periodic rebuild or streaming.

```mermaid
flowchart LR
    n0["Query logs"]
    n1["Aggregator"]
    n2["Trie builder"]
    n3["Trie servers"]
    n4["Client"]
    n0 --> n1
    n1 --> n2
    n2 --> n3
    n3 --> n4
```

---
[⬆ Back to index](../../README.md#-question-index)
