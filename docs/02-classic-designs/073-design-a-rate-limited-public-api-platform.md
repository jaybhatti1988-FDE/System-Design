# 73. Design a rate-limited public API platform.

> Part B: Classic System Designs

**Answer:** Gateway enforces auth (API keys), quotas per plan, throttling per endpoint, usage metering via async events to billing, versioning, developer portal, webhooks with retries and signatures.

```
Dev -> Gateway(key, quota) -> Services; usage events -> Billing
```

---
[⬆ Back to index](../../README.md#-question-index)
