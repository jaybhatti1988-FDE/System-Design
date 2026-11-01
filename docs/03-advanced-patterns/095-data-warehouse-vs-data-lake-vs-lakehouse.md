# 95. Data warehouse vs data lake vs lakehouse?

> Part C: Advanced Patterns and Reliability

**Answer:** Warehouse: structured, schema-on-write, SQL BI (Snowflake, BigQuery). Lake: raw files in object storage, schema-on-read, cheap. Lakehouse: lake + ACID table formats and warehouse performance. Orchestrate ETL/ELT, catalog and governance.

```
Sources -> Lake (raw) -> Transform -> Warehouse/Lakehouse -> BI
```

---
[⬆ Back to index](../../README.md#-question-index)
