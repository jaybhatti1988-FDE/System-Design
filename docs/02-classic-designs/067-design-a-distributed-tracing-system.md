# 67. Design a distributed tracing system.

> Part B: Classic System Designs

**Answer:** Propagate trace/span IDs through headers (W3C traceparent); services emit spans to collector; sample (head/tail-based); store in column store/ES; reassemble traces by trace_id; visualize latency waterfalls.

```
SvcA(span1) -> SvcB(span2) -> SvcC(span3) -> Collector -> Store
```

---
[⬆ Back to index](../../README.md#-question-index)
