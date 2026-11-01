# 73. Design a rate-limited public API platform.

> Part B: Classic System Designs

**Answer:** Gateway enforces auth (API keys), quotas per plan, throttling per endpoint, usage metering via async events to billing, versioning, developer portal, webhooks with retries and signatures.

```mermaid
flowchart LR
    n0["Developer"]
    n1["Gateway (key, quota)"]
    n2["Services"]
    n3["Usage events"]
    n4["Billing"]
    n0 --> n1
    n1 --> n2
    n2 --> n3
    n3 --> n4
```

---
[⬆ Back to index](../../README.md#-question-index)
