# 21. REST vs gRPC vs GraphQL?

> Part A: Fundamentals

**Answer:** REST: simple, cacheable, resource oriented. gRPC: HTTP/2, protobuf, streaming, low latency; good for internal service calls. GraphQL: client picks fields, avoids over/under-fetching; caching and N+1 complexity.

```
REST: many endpoints  |  GraphQL: one endpoint, flexible query
```

---
[⬆ Back to index](../../README.md#-question-index)
