# 79. Design a Slack-like workplace messaging system.

> Part B: Classic System Designs

**Answer:** Workspaces/channels, messages stored per channel partition with monotonically increasing IDs, WebSocket gateways with channel subscriptions via pub/sub, search index, threads, files in object store, unread counts via per-user cursors, notifications.

```mermaid
flowchart LR
    n0["Client"]
    n1["WebSocket gateway"]
    n2["Pub/Sub"]
    n3["Message service"]
    n4["Store + search"]
    n0 --> n1
    n1 --> n2
    n2 --> n3
    n3 --> n4
```

---
[⬆ Back to index](../../README.md#-question-index)
