# 89. Bloom filters and probabilistic structures?

> Part C: Advanced Patterns and Reliability

**Answer:** Bloom filter: bit array + k hashes; no false negatives, possible false positives; used to skip disk lookups, dedup crawlers, cache penetration protection. Count-Min Sketch (frequencies), HyperLogLog (cardinality), Cuckoo filter (supports delete).

```mermaid
flowchart LR
    n0["add(x)"]
    n1["Set k hash bits"]
    n2["query(x)"]
    n3["All bits set?"]
    n4["Maybe present"]
    n5["Definitely absent"]
    n0 --> n1
    n2 --> n3
    n3 --> n4
    n3 --> n5
```

---
[⬆ Back to index](../../README.md#-question-index)
