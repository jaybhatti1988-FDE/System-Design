# 95. Data warehouse vs data lake vs lakehouse?

> Part C: Advanced Patterns and Reliability

**Answer:** Warehouse: structured, schema-on-write, SQL BI (Snowflake, BigQuery). Lake: raw files in object storage, schema-on-read, cheap. Lakehouse: lake + ACID table formats and warehouse performance. Orchestrate ETL/ELT, catalog and governance.

```mermaid
flowchart LR
    n0["Sources"]
    n1["Lake (raw)"]
    n2["Transform"]
    n3["Warehouse / lakehouse"]
    n4["BI"]
    n0 --> n1
    n1 --> n2
    n2 --> n3
    n3 --> n4
```

---
[⬆ Back to index](../../README.md#-question-index)
