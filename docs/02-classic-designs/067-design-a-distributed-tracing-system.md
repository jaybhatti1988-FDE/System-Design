# 67. Design a distributed tracing system.

> Part B: Classic System Designs

**Answer:** Propagate trace/span IDs through headers (W3C traceparent); services emit spans to collector; sample (head/tail-based); store in column store/ES; reassemble traces by trace_id; visualize latency waterfalls.

```mermaid
flowchart LR
    n0["Service A (span 1)"]
    n1["Service B (span 2)"]
    n2["Service C (span 3)"]
    n3["Collector"]
    n4["Trace store"]
    n0 --> n1
    n1 --> n2
    n2 --> n3
    n3 --> n4
```

---
[⬆ Back to index](../../README.md#-question-index)
