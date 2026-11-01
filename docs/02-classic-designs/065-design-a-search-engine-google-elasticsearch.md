# 65. Design a search engine (Google/Elasticsearch).

> Part B: Classic System Designs

**Answer:** Crawl -> parse -> build inverted index (term -> postings) sharded by document; query: tokenize, fetch postings across shards, rank (BM25/PageRank/ML), merge results; caching, spell correction, index refresh via segments.

```mermaid
flowchart LR
    n0["Documents"]
    n1["Indexer"]
    n2["Index shards"]
    n3["Query broker"]
    n4["Client"]
    n0 --> n1
    n1 --> n2
    n2 --> n3
    n3 --> n4
```

---
[⬆ Back to index](../../README.md#-question-index)
