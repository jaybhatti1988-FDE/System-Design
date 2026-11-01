# 13. B-tree vs LSM-tree storage engines?

> Part A: Fundamentals

**Answer:** B-tree: in-place updates, great reads, used by Postgres/MySQL. LSM: append to memtable, flush to sorted SSTables, compaction; great write throughput, used by Cassandra/RocksDB. LSM has read/space amplification, mitigated by bloom filters.

```
Write -> WAL + Memtable -> flush -> SSTables -> compaction
```

---
[⬆ Back to index](../../README.md#-question-index)
