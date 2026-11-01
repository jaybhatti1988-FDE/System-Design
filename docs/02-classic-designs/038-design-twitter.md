# 38. Design Twitter.

> Part B: Classic System Designs

**Answer:** Services: tweet, user graph, timeline, search, trends, notifications. Tweets in sharded store (Snowflake IDs), timelines via hybrid fan-out, search via inverted index (Earlybird/Elasticsearch), trends via streaming counts, media in object store + CDN.

```mermaid
flowchart LR
    n0["Client"]
    n1["Gateway"]
    n2["Tweet service"]
    n3["Tweet DB"]
    n4["Timeline service"]
    n5["Redis"]
    n6["Search and trends"]
    n7["Stream processing"]
    n0 --> n1
    n1 --> n2
    n2 --> n3
    n1 --> n4
    n4 --> n5
    n1 --> n6
    n6 --> n7
```

---
[⬆ Back to index](../../README.md#-question-index)
