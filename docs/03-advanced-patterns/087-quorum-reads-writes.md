# 87. Quorum reads/writes?

> Part C: Advanced Patterns and Reliability

**Answer:** With N replicas, write to W and read from R; R+W>N guarantees overlap with the latest write. Tune: W=N (fast reads), R=1; or majority for balance. Sloppy quorums + hinted handoff boost availability.

```
N=3, W=2, R=2: write {A,B}, read {B,C} -> overlap B
```

---
[⬆ Back to index](../../README.md#-question-index)
