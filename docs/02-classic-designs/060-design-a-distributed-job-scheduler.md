# 60. Design a distributed job scheduler.

> Part B: Classic System Designs

**Answer:** Store jobs (cron, one-off) in DB with next_run time; scheduler nodes (leader-elected or partitioned) poll and enqueue due jobs to a queue; workers execute with leases/heartbeats; retries, priorities, idempotency, dedup to avoid double execution, DAG dependencies (Airflow).

```mermaid
flowchart LR
    n0["Job DB (next_run)"]
    n1["Scheduler"]
    n2["Queue"]
    n3["Workers"]
    n4["Status DB"]
    n0 --> n1
    n1 --> n2
    n2 --> n3
    n3 --> n4
```

---
[⬆ Back to index](../../README.md#-question-index)
