# 79. Design a Slack-like workplace messaging system.

> Part B: Classic System Designs

**Answer:** Workspaces/channels, messages stored per channel partition with monotonically increasing IDs, WebSocket gateways with channel subscriptions via pub/sub, search index, threads, files in object store, unread counts via per-user cursors, notifications.

```
Client <-WS-> Gateway <-> PubSub <-> Message svc -> Store + Search
```

---
[⬆ Back to index](../../README.md#-question-index)
