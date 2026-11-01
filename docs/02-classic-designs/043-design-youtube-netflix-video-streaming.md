# 43. Design YouTube / Netflix (video streaming).

> Part B: Classic System Designs

**Answer:** Upload to object store, transcoding pipeline (DAG of workers) into multiple bitrates/codecs, chunked adaptive streaming (HLS/DASH), CDN/ISP caches (Open Connect), metadata DB, recommendations, view counts via streaming aggregation.

```mermaid
flowchart TD
    n0["Upload"]
    n1["Raw store"]
    n2["Transcode"]
    n3["Segments"]
    n4["CDN"]
    n5["Player (adaptive bitrate)"]
    n0 --> n1
    n1 --> n2
    n2 --> n3
    n3 --> n4
    n4 --> n5
```

> 📘 **Want more?** Read the [deep dive: Video Streaming (YouTube / Netflix)](../deep-dives/06-video-streaming.md)

---
[⬆ Back to index](../../README.md#-question-index)
