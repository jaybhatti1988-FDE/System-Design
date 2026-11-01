# 99. Security in system design (zero trust, encryption, secrets)?

> Part C: Advanced Patterns and Reliability

**Answer:** TLS everywhere + mTLS between services, encryption at rest (KMS, envelope encryption), least privilege IAM, secrets manager rotation, input validation, WAF/DDoS protection, audit logging, PII minimization, defense in depth.

```mermaid
flowchart LR
    n0["User"]
    n1["WAF"]
    n2["Gateway (authN / authZ)"]
    n3["Service (mTLS)"]
    n4["DB (encrypted)"]
    n0 --> n1
    n1 --> n2
    n2 --> n3
    n3 --> n4
```

---
[⬆ Back to index](../../README.md#-question-index)
