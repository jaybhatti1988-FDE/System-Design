# 30. Blob/object storage vs file vs block storage?

> Part A: Fundamentals

**Answer:** Block: raw volumes for DBs/VMs (low latency). File: hierarchical shared FS (NFS/EFS). Object: flat namespace, HTTP API, huge scale, cheap, immutable objects (S3). Store media in object storage and metadata in a DB.

```mermaid
flowchart LR
    n0["App"]
    n1["Metadata DB (id, url)"]
    n2["Object store (bytes)"]
    n3["CDN"]
    n0 --> n1
    n0 --> n2
    n2 --> n3
```

---

---
[⬆ Back to index](../../README.md#-question-index)
