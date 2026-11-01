# 72. Design an email service (Gmail).

> Part B: Classic System Designs

**Answer:** SMTP ingest -> spam/virus filter -> mailbox store (per-user partition, wide-column) + search index; IMAP/web API for reads; attachments in object store; queues for outbound with retries; SPF/DKIM/DMARC.

```mermaid
flowchart LR
    n0["SMTP in"]
    n1["Spam / virus filter"]
    n2["Mailbox store + index"]
    n3["API / IMAP"]
    n4["Outbound queue"]
    n5["SMTP out"]
    n0 --> n1
    n1 --> n2
    n2 --> n3
    n4 --> n5
```

---
[⬆ Back to index](../../README.md#-question-index)
