# 64. Design a recommendation system.

> Part B: Classic System Designs

**Answer:** Two stages: candidate generation (collaborative filtering, embeddings + ANN search) then ranking (ML model with features from a feature store), then re-ranking (diversity, business rules). Offline training pipeline + online serving, A/B testing, feedback loop.

```mermaid
flowchart LR
    n0["Request"]
    n1["Candidate generation (ANN)"]
    n2["Ranker"]
    n3["Re-rank"]
    n4["Results"]
    n5["Events"]
    n6["Feature store"]
    n7["Model training"]
    n0 --> n1
    n1 --> n2
    n2 --> n3
    n3 --> n4
    n5 --> n6
    n6 --> n7
    n7 --> n2
```

---
[⬆ Back to index](../../README.md#-question-index)
