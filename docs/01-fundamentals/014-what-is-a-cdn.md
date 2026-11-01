# 14. What is a CDN?

> Part A: Fundamentals

**Answer:** Geographically distributed edge caches serving static (and some dynamic) content near users. Pull CDN fetches from origin on miss; push CDN pre-uploads. Handle cache-control headers, invalidation/purge, signed URLs for private content.

```mermaid
flowchart LR
    n0["User"]
    n1["Edge cache"]
    n2["Content (hit)"]
    n3["Origin (miss)"]
    n0 --> n1
    n1 --> n2
    n1 --> n3
```

---
[⬆ Back to index](../../README.md#-question-index)
