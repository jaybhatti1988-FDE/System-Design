# 20. What is idempotency and how do you implement it?

> Part A: Fundamentals

**Answer:** Repeating a request yields the same effect. Client sends an idempotency key; server stores key->result (with TTL) and returns the stored result on retry. Essential for payments and at-least-once messaging. Use unique constraints or conditional writes.

```mermaid
flowchart LR
    n0["POST /pay + idempotency key"]
    n1["Key seen?"]
    n2["No: process and save result"]
    n3["Yes: return saved result"]
    n0 --> n1
    n1 --> n2
    n1 --> n3
```

---
[⬆ Back to index](../../README.md#-question-index)
