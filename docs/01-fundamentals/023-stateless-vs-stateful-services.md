# 23. Stateless vs stateful services?

> Part A: Fundamentals

**Answer:** Stateless services keep no session in memory (state in DB/cache/token), so any instance can serve any request and scaling/failover is easy. Stateful (DBs, WebSocket servers) need partitioning, replication and sticky routing.

```
Req -> any of [S][S][S] -> shared Redis/DB
```

---
[⬆ Back to index](../../README.md#-question-index)
