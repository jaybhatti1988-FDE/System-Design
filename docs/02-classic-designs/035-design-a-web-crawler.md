# 35. Design a web crawler.

> Part B: Classic System Designs

**Answer:** URL frontier (priority + politeness queues per host), fetchers, DNS cache, HTML parser, dedup (URL set via bloom filter, content hash/simhash), robots.txt, storage, link extraction feeding the frontier. Distribute by host hash; handle spider traps and recrawl scheduling.

```mermaid
flowchart TD
    n0["Seed URLs"]
    n1["URL frontier"]
    n2["Fetcher"]
    n3["Parser"]
    n4["Dedup"]
    n5["Store"]
    n6["New URLs"]
    n0 --> n1
    n1 --> n2
    n2 --> n3
    n3 --> n4
    n4 --> n5
    n3 --> n6
    n6 --> n1
```

---
[⬆ Back to index](../../README.md#-question-index)
