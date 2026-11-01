# 68. Design a feature flag service.

> Part B: Classic System Designs

**Answer:** Flag configs in DB/control plane, pushed to SDKs via streaming/polling and cached locally so evaluation is local and fast; targeting rules (percentage, segment, hash of user id); audit log, kill switches, fail-safe defaults.

```mermaid
flowchart LR
    n0["Admin UI"]
    n1["Flag store"]
    n2["CDN / stream"]
    n3["SDK (local evaluation)"]
    n0 --> n1
    n1 --> n2
    n2 --> n3
```

---
[⬆ Back to index](../../README.md#-question-index)
