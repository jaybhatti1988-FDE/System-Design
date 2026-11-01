# 44. Design Google Drive / Dropbox.

> Part B: Classic System Designs

**Answer:** Split files into chunks (4MB), hash each, upload only changed chunks (delta sync), dedup via content-hash, metadata service in SQL, blobs in object store, notification service (long poll/WS) for sync, conflict resolution (versioning), sharing ACLs.

```
Client(chunker) -> Metadata svc + Block svc -> Object store
                <- Notification svc
```

---
[⬆ Back to index](../../README.md#-question-index)
