# 40. Design a chat system (WhatsApp/Messenger).

> Part B: Classic System Designs

**Answer:** Persistent WebSocket connections to chat servers; a session service maps user->server; messages go to message queue/store (per-chat partition key), delivered online via the recipient's server or stored for offline + push notification. Ack states (sent/delivered/read), per-chat ordering with sequence IDs, group fan-out, E2E encryption.

```mermaid
flowchart LR
    n0["User A"]
    n1["Chat server 1 (WebSocket)"]
    n2["Message store / Kafka"]
    n3["Chat server 2"]
    n4["User B"]
    n5["Push notification (offline)"]
    n0 --> n1
    n1 --> n2
    n2 --> n3
    n3 --> n4
    n2 --> n5
```

> 📘 **Want more?** Read the [deep dive: Chat System (WhatsApp / Messenger)](../deep-dives/04-chat-system.md)

---
[⬆ Back to index](../../README.md#-question-index)
