# 37. Design a news feed (Facebook/Twitter timeline).

> Part B: Classic System Designs

**Answer:** Fan-out on write (precompute feed in cache per follower; fast reads, heavy for celebrities) vs fan-out on read (compute on request). Hybrid: push for normal users, pull for celebrities. Rank with ML, store posts in DB, feed ids in Redis lists, media on CDN.

```mermaid
flowchart LR
    n0["New post"]
    n1["Fan-out service"]
    n2["Follower feed caches"]
    n3["Read feed"]
    n4["Feed cache + celebrity posts"]
    n5["Rank"]
    n6["Timeline"]
    n0 --> n1
    n1 --> n2
    n3 --> n4
    n4 --> n5
    n5 --> n6
```

> 📘 **Want more?** Read the [deep dive: News Feed](../deep-dives/03-news-feed.md)

---
[⬆ Back to index](../../README.md#-question-index)
