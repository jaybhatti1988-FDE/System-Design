# 43. Design YouTube / Netflix (video streaming).

> Part B: Classic System Designs

**Answer:** Upload to object store, transcoding pipeline (DAG of workers) into multiple bitrates/codecs, chunked adaptive streaming (HLS/DASH), CDN/ISP caches (Open Connect), metadata DB, recommendations, view counts via streaming aggregation.

```
Upload -> Raw store -> Transcode -> Segments -> CDN -> Player (ABR)
```

---
[⬆ Back to index](../../README.md#-question-index)
