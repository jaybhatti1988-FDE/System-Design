# 69. Design a CI/CD system.

> Part B: Classic System Designs

**Answer:** Webhook triggers pipeline; orchestrator schedules stages (build, test, scan, deploy) as DAG on elastic worker pool (containers); artifact registry, caching, secrets, parallel tests; deploy via canary/blue-green with auto rollback.

```mermaid
flowchart TD
    n0["Push"]
    n1["Orchestrator"]
    n2["Build"]
    n3["Test"]
    n4["Artifact repo"]
    n5["Deploy"]
    n0 --> n1
    n1 --> n2
    n2 --> n3
    n3 --> n4
    n4 --> n5
```

---
[⬆ Back to index](../../README.md#-question-index)
