# 10. What is consistent hashing?

> Part A: Fundamentals

**Answer:** Nodes and keys are placed on a hash ring; a key belongs to the next node clockwise. Adding/removing a node remaps only ~1/N keys. Virtual nodes balance load and handle heterogeneous machines.

```
      N1
     /  \
   N4    N2     key -> next clockwise node
     \  /
      N3
```

---
[⬆ Back to index](../../README.md#-question-index)
