# 10. What is consistent hashing?

> Part A: Fundamentals

**Answer:** Nodes and keys are placed on a hash ring; a key belongs to the next node clockwise. Adding/removing a node remaps only ~1/N keys. Virtual nodes balance load and handle heterogeneous machines.

```mermaid
flowchart LR
    n0["Key"]
    n1["Hash ring position"]
    n2["Next node clockwise"]
    n3["Add or remove a node"]
    n4["Only ~1/N keys move"]
    n0 --> n1
    n1 --> n2
    n3 --> n4
```

---
[⬆ Back to index](../../README.md#-question-index)
