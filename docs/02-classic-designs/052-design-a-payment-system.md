# 52. Design a payment system.

> Part B: Classic System Designs

**Answer:** Payment service talks to PSPs; idempotency keys; double-entry ledger; state machine (created, authorized, captured, refunded); reconciliation jobs against PSP reports; retries with dedup; PCI scope isolation (tokenization); async webhooks with signature verification.

```mermaid
flowchart LR
    n0["Checkout"]
    n1["Payment service"]
    n2["PSP"]
    n3["Ledger DB"]
    n4["Reconciliation"]
    n0 --> n1
    n1 --> n2
    n1 --> n3
    n1 --> n4
```

> 📘 **Want more?** Read the [deep dive: Payment System](../deep-dives/10-payment-system.md)

---
[⬆ Back to index](../../README.md#-question-index)
