# 32. Design Pastebin.

> Part B: Classic System Designs

**Answer:** Store paste text in object storage, metadata (id, expiry, owner) in DB; id from key-generation service. CDN/caching for popular pastes; cleanup job for expired pastes; size limits and abuse detection.

```mermaid
flowchart LR
    n0["Client"]
    n1["App"]
    n2["Metadata DB"]
    n3["Object store"]
    n4["CDN"]
    n0 --> n1
    n1 --> n2
    n1 --> n3
    n3 --> n4
```

---
[⬆ Back to index](../../README.md#-question-index)
