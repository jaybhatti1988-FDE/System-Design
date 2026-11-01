# 13. B-tree vs LSM-tree storage engines?

> Part A: Fundamentals

**Answer:** B-tree: in-place updates, great reads, used by Postgres/MySQL. LSM: append to memtable, flush to sorted SSTables, compaction; great write throughput, used by Cassandra/RocksDB. LSM has read/space amplification, mitigated by bloom filters.

```mermaid
flowchart LR
    n0["Write"]
    n1["WAL + memtable"]
    n2["Flush to SSTable"]
    n3["Compaction"]
    n0 --> n1
    n1 --> n2
    n2 --> n3
```

---
[⬆ Back to index](../../README.md#-question-index)
