# 50. Design an e-commerce platform (Amazon).

> Part B: Classic System Designs

**Answer:** Services: catalog (search), cart, inventory, orders, payments, shipping, recommendations. Order flow uses saga/outbox events; inventory reserved then committed; cart in Redis/DynamoDB; product pages heavily cached; search via inverted index.

```mermaid
flowchart LR
    n0["UI"]
    n1["API gateway"]
    n2["Catalog"]
    n3["Cart"]
    n4["Order"]
    n5["Inventory"]
    n6["Payment"]
    n7["Shipping"]
    n0 --> n1
    n1 --> n2
    n1 --> n3
    n1 --> n4
    n4 --> n5
    n5 --> n6
    n6 --> n7
```

---
[⬆ Back to index](../../README.md#-question-index)
