# 100 Most Important System Design Questions

Answers and ASCII diagrams for interview prep.

- **Part A:** Fundamentals (1–30)
- **Part B:** Classic system designs (31–80)
- **Part C:** Advanced patterns and reliability (81–100)

> **How to answer any design question:**
> 1. Clarify requirements (functional and non-functional)
> 2. Estimate scale (QPS, storage, bandwidth)
> 3. Define APIs and data model
> 4. Draw the high-level design
> 5. Deep-dive bottlenecks
> 6. Discuss trade-offs, failures and monitoring

---

## Part A: Fundamentals

### 1. Vertical vs horizontal scaling?

**Answer:** Vertical = bigger machine (simple, limited, single point of failure). Horizontal = more machines (needs stateless services, load balancing, data partitioning; near-unlimited scale). Prefer horizontal for web tiers; scale DBs vertically first, then replicate and shard.

```
Vertical:   [Small] -> [BIG]
Horizontal: [S] -> [S][S][S][S] behind LB
```

### 2. What is a load balancer and which algorithms exist?

**Answer:** Distributes traffic across servers for availability and throughput. L4 (TCP/IP, fast) vs L7 (HTTP aware, routing by path/header). Algorithms: round robin, weighted RR, least connections, IP hash, consistent hashing. Use health checks and run LBs in active-passive or active-active pairs.

```
Client -> [LB] -> Server1
              -> Server2
              -> Server3
```

### 3. Explain the CAP theorem.

**Answer:** During a network partition you must choose Consistency or Availability. CP: reject/delay requests to stay consistent (HBase, etcd, MongoDB default). AP: serve possibly stale data (Cassandra, DynamoDB). Without partition, trade latency vs consistency (PACELC).

```
        C
       / \
     CP   CA (not realistic in distributed)
     /     \
    P ------- A   (AP)
```

### 4. Strong vs eventual consistency?

**Answer:** Strong: every read sees the latest write (linearizable; higher latency). Eventual: replicas converge over time (low latency, high availability). Intermediate: read-your-writes, monotonic reads, causal consistency. Pick strong for payments/inventory, eventual for feeds/likes.

```
Write -> Leader -> (async) -> Replica   read may be stale
Write -> Leader -> (sync)  -> Replica   read always fresh
```

### 5. How does caching work and where do you place caches?

**Answer:** Store hot data in fast memory to cut latency and DB load. Layers: browser, CDN, API gateway, application (Redis/Memcached), DB buffer pool. Key concerns: eviction (LRU/LFU/TTL), invalidation, hit ratio, consistency.

```
Client -> App -> [Cache] hit -> return
                    | miss
                    v
                  [DB] -> fill cache
```

### 6. Cache write strategies?

**Answer:** Cache-aside (app loads on miss; most common). Read-through (cache loads). Write-through (write cache+DB synchronously; consistent, slower). Write-back (write cache, flush async; fast, risk of loss). Write-around (write DB only; avoids cache pollution).

```
Write-through: App -> Cache -> DB (sync)
Write-back:    App -> Cache ..async..> DB
```

### 7. How do you handle cache invalidation, stampede and hot keys?

**Answer:** Use TTL + explicit delete on write, versioned keys, and event-driven invalidation (CDC). Stampede (thundering herd): request coalescing/locks, jittered TTL, stale-while-revalidate, pre-warming. Hot keys: local in-process cache, key replication (key#1..N), read replicas.

```
1000 misses -> [lock per key] -> 1 DB query -> fill -> 999 wait
```

### 8. SQL vs NoSQL?

**Answer:** SQL: relational, ACID, joins, strong schema; good for transactions and complex queries. NoSQL: key-value, document, wide-column, graph; flexible schema, horizontal scale, tuned access patterns. Choose by access pattern, consistency and scale, and polyglot persistence is normal.

```
SQL: tables + joins        NoSQL: {key -> document/columns}
```

### 9. What is database sharding and how do you choose a shard key?

**Answer:** Splitting data across nodes. Strategies: range, hash, directory/lookup, geo. A good key has high cardinality, even distribution, and matches query patterns (avoids cross-shard queries). Challenges: hotspots, resharding, joins, transactions.

```
user_id % 3 -> Shard0 | Shard1 | Shard2
```

### 10. What is consistent hashing?

**Answer:** Nodes and keys are placed on a hash ring; a key belongs to the next node clockwise. Adding/removing a node remaps only ~1/N keys. Virtual nodes balance load and handle heterogeneous machines.

```
      N1
     /  \
   N4    N2     key -> next clockwise node
     \  /
      N3
```

### 11. Database replication models?

**Answer:** Leader-follower (writes to leader, reads from followers; sync/async), multi-leader (multi-region writes, conflict resolution), leaderless (quorum, Dynamo style). Trade-offs: replication lag, failover, conflicts.

```
Writes -> [Leader] -> [Follower1]
                   -> [Follower2] <- Reads
```

### 12. Explain database indexing.

**Answer:** Auxiliary structure (B-tree, hash, LSM, inverted, geo) for fast lookups at the cost of write overhead and storage. Use composite indexes in query order, covering indexes, avoid indexing low-cardinality columns, and check query plans.

```
B-tree:        [50]
              /    \
        [20,30]    [70,90] -> leaf -> row pointer
```

### 13. B-tree vs LSM-tree storage engines?

**Answer:** B-tree: in-place updates, great reads, used by Postgres/MySQL. LSM: append to memtable, flush to sorted SSTables, compaction; great write throughput, used by Cassandra/RocksDB. LSM has read/space amplification, mitigated by bloom filters.

```
Write -> WAL + Memtable -> flush -> SSTables -> compaction
```

### 14. What is a CDN?

**Answer:** Geographically distributed edge caches serving static (and some dynamic) content near users. Pull CDN fetches from origin on miss; push CDN pre-uploads. Handle cache-control headers, invalidation/purge, signed URLs for private content.

```
User -> [Edge] hit -> content
           | miss
           v
        [Origin]
```

### 15. What is an API gateway?

**Answer:** Single entry point handling routing, auth, rate limiting, TLS termination, request aggregation, logging and versioning in front of microservices. Avoid making it a bottleneck: scale horizontally and keep business logic out.

```
Clients -> [API GW: auth, rate limit] -> Svc A / Svc B / Svc C
```

### 16. How do you design a rate limiter?

**Answer:** Algorithms: token bucket (bursts allowed), leaky bucket (smooth), fixed window (boundary burst issue), sliding window log/counter. Store counters in Redis with atomic Lua/INCR + TTL, keyed by user/IP/API key. Return 429 with Retry-After. Distributed: central Redis or local limit + sync.

```
Req -> [Limiter: Redis counters] -> allow -> Service
                                 -> deny 429
```

### 17. Message queues: why and when?

**Answer:** Decouple producers and consumers, absorb spikes, enable async processing and retries. Semantics: at-most-once, at-least-once (default; needs idempotent consumers), exactly-once (hard; transactions/dedup). Use DLQs for poison messages.

```
Producer -> [Queue] -> Consumer(s) -> DLQ on failure
```

### 18. Kafka vs RabbitMQ / SQS?

**Answer:** Kafka: distributed append-only log, partitions for ordering and parallelism, replay, high throughput, consumer groups. RabbitMQ/SQS: broker-style queues with per-message ack, routing, simpler task queues. Choose Kafka for streaming/event sourcing, SQS/Rabbit for job queues.

```
Topic: P0 [0 1 2 3]  P1 [0 1 2]    Consumer group reads per partition
```

### 19. Pub/Sub vs point-to-point?

**Answer:** Point-to-point: each message consumed by one consumer. Pub/Sub: each subscriber gets a copy (fan-out). Combine: fan-out to multiple queues, each with competing consumers.

```
Pub -> [Topic] -> Sub A
               -> Sub B
```

### 20. What is idempotency and how do you implement it?

**Answer:** Repeating a request yields the same effect. Client sends an idempotency key; server stores key->result (with TTL) and returns the stored result on retry. Essential for payments and at-least-once messaging. Use unique constraints or conditional writes.

```
POST /pay (key=abc) -> check store -> new? process+save : return saved
```

### 21. REST vs gRPC vs GraphQL?

**Answer:** REST: simple, cacheable, resource oriented. gRPC: HTTP/2, protobuf, streaming, low latency; good for internal service calls. GraphQL: client picks fields, avoids over/under-fetching; caching and N+1 complexity.

```
REST: many endpoints  |  GraphQL: one endpoint, flexible query
```

### 22. Polling vs long polling vs WebSockets vs SSE?

**Answer:** Polling: simple, wasteful. Long polling: server holds request until data. SSE: one-way server push over HTTP. WebSocket: full-duplex persistent connection (chat, games). Scale WebSockets with sticky routing and a pub/sub backplane.

```
Client <==WebSocket==> Gateway <-> PubSub <-> Other gateways
```

### 23. Stateless vs stateful services?

**Answer:** Stateless services keep no session in memory (state in DB/cache/token), so any instance can serve any request and scaling/failover is easy. Stateful (DBs, WebSocket servers) need partitioning, replication and sticky routing.

```
Req -> any of [S][S][S] -> shared Redis/DB
```

### 24. Authentication and authorization (OAuth2, JWT, sessions)?

**Answer:** Sessions: server-side state, easy revocation. JWT: signed stateless token; short expiry + refresh tokens; revocation is hard. OAuth2/OIDC: delegated access via authorization code flow (+PKCE). Authorization via RBAC/ABAC, enforced at gateway and service.

```
User -> IdP login -> auth code -> token -> API (verify signature)
```

### 25. How do you estimate capacity (back-of-envelope)?

**Answer:** QPS = DAU x actions/day / 86400; peak ≈ 2-5x avg. Storage = items/day x size x retention x replication. Bandwidth = QPS x payload. Remember: 1 day ≈ 10^5 s, 1M req/day ≈ 12 QPS. Latency numbers: memory ~100ns, SSD ~100µs, same-DC RTT ~0.5ms, cross-continent ~150ms.

```
100M DAU x 10 req / 86400 ≈ 11.5K QPS avg -> ~35K peak
```

### 26. Availability and SLAs: how do you reach 99.99%?

**Answer:** 99.99% ≈ 52 min downtime/year. Remove single points of failure: redundancy across AZs/regions, health checks, auto-failover, graceful degradation, retries with backoff, circuit breakers, canary deploys, and chaos testing. Availability of serial components multiplies; parallel redundancy improves it.

```
[LB] -> [AZ1: app+db]
     -> [AZ2: app+db replica]
```

### 27. Latency vs throughput?

**Answer:** Latency = time per request (watch p50/p95/p99); throughput = requests/sec. Improve latency via caching, locality, async, fewer hops; throughput via parallelism, batching, queues. Batching raises throughput but adds latency.

```
Latency |---->|        Throughput: ||||||| per second
```

### 28. Microservices vs monolith?

**Answer:** Monolith: simple to build, deploy, test; scales as one unit. Microservices: independent scaling/deploys/tech, team autonomy; cost is network failures, distributed transactions, observability. Start modular monolith, split on clear boundaries.

```
Monolith [ A B C ]  ->  [A] [B] [C] via API/events
```

### 29. Service discovery?

**Answer:** Services register with a registry (Consul, etcd, Eureka, Kubernetes DNS) and clients find healthy instances. Client-side discovery (client picks instance) vs server-side (LB/proxy does). Use heartbeats/TTL to drop dead nodes; service mesh (Envoy/Istio) adds sidecar routing.

```
Svc -> register -> [Registry] <- lookup <- Client
```

### 30. Blob/object storage vs file vs block storage?

**Answer:** Block: raw volumes for DBs/VMs (low latency). File: hierarchical shared FS (NFS/EFS). Object: flat namespace, HTTP API, huge scale, cheap, immutable objects (S3). Store media in object storage and metadata in a DB.

```
App -> metadata DB (id, url)
    -> Object store (bytes) -> CDN
```

---

## Part B: Classic System Designs

### 31. Design a URL shortener (TinyURL).

**Answer:** Generate a 7-char base62 code (62^7 ≈ 3.5T) via counter + base62 (ranges per app server) or a key-generation service; store code->URL in a KV store/NoSQL. Redirect with HTTP 301/302; cache hot codes in Redis; read-heavy (100:1). Handle expiry, custom aliases, analytics asynchronously.

```
Client -> LB -> App -> Redis cache -> DB (code,url)
                   \-> KeyGen service
```

### 32. Design Pastebin.

**Answer:** Store paste text in object storage, metadata (id, expiry, owner) in DB; id from key-generation service. CDN/caching for popular pastes; cleanup job for expired pastes; size limits and abuse detection.

```
Client -> App -> Metadata DB
              -> Object store -> CDN
```

### 33. Design a distributed key-value store (Dynamo-style).

**Answer:** Partition via consistent hashing, replicate to N nodes, quorum reads/writes (R+W>N), vector clocks or LWW for conflicts, hinted handoff, read repair, anti-entropy with Merkle trees, gossip for membership, LSM storage with WAL.

```
Client -> coordinator -> N1,N2,N3 (replicas on ring)
```

### 34. Design a unique ID generator.

**Answer:** Snowflake: 64-bit = timestamp(41) + datacenter/machine(10) + sequence(12); time-sortable, no coordination (needs clock sync handling). Alternatives: UUID (large, unordered), DB ticket servers, ULID.

```
[0 | timestamp 41 | machine 10 | seq 12]
```

### 35. Design a web crawler.

**Answer:** URL frontier (priority + politeness queues per host), fetchers, DNS cache, HTML parser, dedup (URL set via bloom filter, content hash/simhash), robots.txt, storage, link extraction feeding the frontier. Distribute by host hash; handle spider traps and recrawl scheduling.

```
Seed -> [Frontier] -> Fetcher -> Parser -> Dedup -> Store
           ^______________ new URLs ___________|
```

### 36. Design a notification system (push/SMS/email).

**Answer:** API validates and enqueues; per-channel queues and workers call providers (APNs/FCM, Twilio, SES); user preferences, templates, rate limiting, dedup, retries with backoff, DLQ, delivery tracking and analytics.

```
Service -> [Notif API] -> Kafka -> Push/SMS/Email workers -> Providers
```

### 37. Design a news feed (Facebook/Twitter timeline).

**Answer:** Fan-out on write (precompute feed in cache per follower; fast reads, heavy for celebrities) vs fan-out on read (compute on request). Hybrid: push for normal users, pull for celebrities. Rank with ML, store posts in DB, feed ids in Redis lists, media on CDN.

```
Post -> Fanout svc -> follower feed caches
Read -> feed cache + celebrity posts merge -> rank
```

### 38. Design Twitter.

**Answer:** Services: tweet, user graph, timeline, search, trends, notifications. Tweets in sharded store (Snowflake IDs), timelines via hybrid fan-out, search via inverted index (Earlybird/Elasticsearch), trends via streaming counts, media in object store + CDN.

```
Client -> GW -> Tweet svc -> DB
             -> Timeline svc -> Redis
             -> Search/Trends (stream)
```

### 39. Design Instagram.

**Answer:** Photo upload to object storage (multiple resolutions via async workers), metadata in sharded DB, follow graph, feed generation (hybrid), CDN for delivery, likes/comments counters via eventual consistency, explore/recommendation pipeline.

```
Upload -> Object store -> Resize workers -> CDN
Meta -> DB shards; Feed -> cache
```

### 40. Design a chat system (WhatsApp/Messenger).

**Answer:** Persistent WebSocket connections to chat servers; a session service maps user->server; messages go to message queue/store (per-chat partition key), delivered online via the recipient's server or stored for offline + push notification. Ack states (sent/delivered/read), per-chat ordering with sequence IDs, group fan-out, E2E encryption.

```
A <-WS-> ChatSrv1 -> [MsgStore/Kafka] -> ChatSrv2 <-WS-> B
                                      |-> Push (offline)
```

### 41. Design group chat and presence (online status).

**Answer:** Group messages fan-out to members (small groups push, large via pull/channels). Presence via heartbeats stored in Redis with TTL; publish status changes only to friends who are online; avoid broadcasting every blip (debounce).

```
Client --heartbeat--> Presence svc (Redis TTL) -> pubsub -> friends
```

### 42. Design search autocomplete (typeahead).

**Answer:** Trie (or prefix index) with top-K suggestions cached per node; built offline from query logs (aggregated by frequency/recency), served from memory/Redis; client debounce; shard by prefix; update via periodic rebuild or streaming.

```
Query logs -> Aggregator -> Trie builder -> Trie servers <- Client
```

### 43. Design YouTube / Netflix (video streaming).

**Answer:** Upload to object store, transcoding pipeline (DAG of workers) into multiple bitrates/codecs, chunked adaptive streaming (HLS/DASH), CDN/ISP caches (Open Connect), metadata DB, recommendations, view counts via streaming aggregation.

```
Upload -> Raw store -> Transcode -> Segments -> CDN -> Player (ABR)
```

### 44. Design Google Drive / Dropbox.

**Answer:** Split files into chunks (4MB), hash each, upload only changed chunks (delta sync), dedup via content-hash, metadata service in SQL, blobs in object store, notification service (long poll/WS) for sync, conflict resolution (versioning), sharing ACLs.

```
Client(chunker) -> Metadata svc + Block svc -> Object store
                <- Notification svc
```

### 45. Design Uber / ride hailing.

**Answer:** Drivers send location every ~4s to a location service (geohash/quadtree/S2 index in Redis); rider request -> matching service finds nearby drivers, ranks by ETA, offers with timeout; trip service state machine; pricing (surge); maps/ETA; payments. Use WebSockets for live updates.

```
Driver -> Location svc (geo index) <- Match svc <- Rider
                                         |-> Trip svc -> Payments
```

### 46. Design a proximity service (Yelp / nearby friends).

**Answer:** Geospatial indexes: geohash (prefix = nearby, check neighbors), quadtree (adaptive), S2/H3 cells. Static businesses: DB with geohash index + cache; moving entities: in-memory grid/Redis GEO. Search the cell and its 8 neighbors, then filter by distance.

```
lat/lng -> geohash "9q8yy" -> query cell + neighbors
```

### 47. Design Google Maps.

**Answer:** Map tiles (pre-rendered vector/raster pyramid by zoom) on CDN; road network graph partitioned hierarchically; routing with A*/Contraction Hierarchies; live traffic from probe data via streaming; ETA service; geocoding index.

```
Client -> Tile CDN
       -> Routing svc (graph shards) <- Traffic stream
```

### 48. Design a ticket booking system (Ticketmaster).

**Answer:** Prevent double-booking: seat hold with TTL (Redis lock or DB row version/optimistic lock), then payment, then confirm. Use virtual waiting room/queue for flash demand, inventory in strongly consistent DB, idempotent payments.

```
Select -> HOLD(seat, ttl 5m) -> Pay -> CONFIRM | expire -> release
```

### 49. Design a hotel reservation system (Airbnb/Booking).

**Answer:** Inventory per room-type per date with unique constraint/optimistic locking to avoid overbooking; search via Elasticsearch with availability filter; reservation state machine; idempotency keys; payments via saga; reviews and ranking separate services.

```
Search(ES) -> Reservation svc -> Inventory DB (lock) -> Payment
```

### 50. Design an e-commerce platform (Amazon).

**Answer:** Services: catalog (search), cart, inventory, orders, payments, shipping, recommendations. Order flow uses saga/outbox events; inventory reserved then committed; cart in Redis/DynamoDB; product pages heavily cached; search via inverted index.

```
UI -> GW -> Catalog | Cart | Order -> Inventory -> Payment -> Shipping
```

### 51. Design a flash sale system.

**Answer:** Absorb spikes: CDN static, rate limit/queue at edge, pre-load stock in Redis with atomic DECR, async order creation via queue, DB write on confirmation only, overselling prevention, idempotent orders, degrade non-critical features.

```
Users -> CDN/WAF -> Queue -> Redis stock DECR -> Order workers -> DB
```

### 52. Design a payment system.

**Answer:** Payment service talks to PSPs; idempotency keys; double-entry ledger; state machine (created, authorized, captured, refunded); reconciliation jobs against PSP reports; retries with dedup; PCI scope isolation (tokenization); async webhooks with signature verification.

```
Checkout -> Payment svc -> PSP
               |-> Ledger DB
               |-> Reconciliation
```

### 53. Design a digital wallet.

**Answer:** Balance changes via double-entry ledger in ACID DB; transfers between shards via distributed transaction (2PC or saga with reservation) or event sourcing with replay; idempotent ops; audit log; fraud checks.

```
Transfer: debit A (hold) -> credit B -> commit | compensate
```

### 54. Design a stock exchange / order matching engine.

**Answer:** Single-threaded deterministic matching per symbol (price-time priority) with in-memory order book, sequencer for total ordering, event-sourced journal replicated for recovery, market data publishers, risk checks at gateway, ultra-low latency networking.

```
Orders -> Gateway -> Sequencer -> Matching engine -> Trades -> Market data
```

### 55. Design a metrics/monitoring system (Prometheus/Datadog).

**Answer:** Agents push/pull metrics -> Kafka -> time-series DB (compression, downsampling, retention tiers); query engine; alert evaluator -> notification routing; cardinality control; dashboards.

```
Hosts -> Collector -> Kafka -> TSDB -> Query/Dashboards
                           \-> Alert mgr
```

### 56. Design an ad click aggregation system.

**Answer:** Click events -> Kafka -> stream processor (Flink) with tumbling windows aggregates per ad/minute, dedup by click id, late data via watermarks; store aggregates in OLAP DB (Druid/ClickHouse) and raw events in object storage; reconcile with batch (lambda/kappa).

```
Clicks -> Kafka -> Flink windows -> OLAP DB
              \-> raw -> S3 -> batch reconcile
```

### 57. Design a distributed message queue.

**Answer:** Topics split into partitions, each an append-only log replicated (leader + ISR); producers pick partition by key; consumer groups track offsets; segment files, page cache, zero-copy; controller via ZooKeeper/Raft; retention and compaction.

```
Producer -> Broker(leader P0) -> replicas
Consumer group <- offsets
```

### 58. Design a distributed cache (Redis/Memcached cluster).

**Answer:** Shard keys with consistent hashing or hash slots (Redis Cluster 16384), replicas for failover, LRU/LFU eviction, client-side or proxy routing, persistence (RDB/AOF) optional, handle hot keys and rebalancing.

```
Client -> proxy -> slot->node (M1 R1 | M2 R2 | M3 R3)
```

### 59. Design a distributed lock service.

**Answer:** Use Redis SET NX PX with unique token + Lua release, or better ZooKeeper/etcd ephemeral nodes with leases. Add fencing tokens (monotonic) so stale holders cannot write. Beware clock drift, GC pauses, and prefer idempotency over locks where possible.

```
Client -> etcd lease key -> token n -> storage checks token >= last
```

### 60. Design a distributed job scheduler.

**Answer:** Store jobs (cron, one-off) in DB with next_run time; scheduler nodes (leader-elected or partitioned) poll and enqueue due jobs to a queue; workers execute with leases/heartbeats; retries, priorities, idempotency, dedup to avoid double execution, DAG dependencies (Airflow).

```
Job DB -> Scheduler -> Queue -> Workers -> status DB
```

### 61. Design a leaderboard.

**Answer:** Redis sorted sets (ZADD, ZREVRANGE, ZRANK) give O(log N) updates and top-K; shard by score range or user for huge scale; persist to DB; periodic snapshots for daily/weekly boards; approximate rank for large N.

```
Score event -> Redis ZSET -> top 10 / my rank
```

### 62. Design a video conferencing system (Zoom/Meet).

**Answer:** Signaling server (WebSocket) for session setup (SDP/ICE), WebRTC media; 1:1 P2P, groups use SFU (selective forwarding; scalable) vs MCU (mixing; heavy). TURN for NAT traversal, simulcast/adaptive bitrate, regional media servers.

```
A --\
B ---> [SFU] --> subscribers     (signaling via WS)
C --/
```

### 63. Design a food delivery system (DoorDash/Swiggy).

**Answer:** Services: restaurants/menu, search, order, dispatch, tracking, payments, ETA. Dispatch matches courier by proximity and batching; order state machine with events; live location via streaming; ETA models.

```
Order -> Restaurant -> Dispatch -> Courier (live loc) -> Customer
```

### 64. Design a recommendation system.

**Answer:** Two stages: candidate generation (collaborative filtering, embeddings + ANN search) then ranking (ML model with features from a feature store), then re-ranking (diversity, business rules). Offline training pipeline + online serving, A/B testing, feedback loop.

```
Events -> Feature store -> Train -> Model
Request -> Candidates(ANN) -> Ranker -> Rerank -> Results
```

### 65. Design a search engine (Google/Elasticsearch).

**Answer:** Crawl -> parse -> build inverted index (term -> postings) sharded by document; query: tokenize, fetch postings across shards, rank (BM25/PageRank/ML), merge results; caching, spell correction, index refresh via segments.

```
Docs -> Indexer -> Index shards <- Query broker <- Client
```

### 66. Design log aggregation (ELK/Splunk).

**Answer:** Agents (Filebeat/Fluentd) ship logs -> Kafka buffer -> parser/enricher -> index (Elasticsearch) hot/warm/cold tiers + raw archive in object storage; retention, sampling, PII scrubbing, dashboards and alerts.

```
Apps -> Agent -> Kafka -> Logstash -> Elasticsearch -> Kibana
```

### 67. Design a distributed tracing system.

**Answer:** Propagate trace/span IDs through headers (W3C traceparent); services emit spans to collector; sample (head/tail-based); store in column store/ES; reassemble traces by trace_id; visualize latency waterfalls.

```
SvcA(span1) -> SvcB(span2) -> SvcC(span3) -> Collector -> Store
```

### 68. Design a feature flag service.

**Answer:** Flag configs in DB/control plane, pushed to SDKs via streaming/polling and cached locally so evaluation is local and fast; targeting rules (percentage, segment, hash of user id); audit log, kill switches, fail-safe defaults.

```
Admin UI -> Flag store -> CDN/stream -> SDK (local eval)
```

### 69. Design a CI/CD system.

**Answer:** Webhook triggers pipeline; orchestrator schedules stages (build, test, scan, deploy) as DAG on elastic worker pool (containers); artifact registry, caching, secrets, parallel tests; deploy via canary/blue-green with auto rollback.

```
Push -> Orchestrator -> Build -> Test -> Artifact repo -> Deploy
```

### 70. Design a web analytics system (Google Analytics).

**Answer:** JS tracker -> collector endpoint -> Kafka -> stream processing (sessionization, dedup, bot filter) -> OLAP store for dashboards; raw data lake for batch; sampling/pre-aggregation to control cost.

```
Browser -> Collector -> Kafka -> Flink -> OLAP -> Dashboard
```

### 71. Design Google Docs (real-time collaborative editing).

**Answer:** Concurrent edits merged by Operational Transformation (central server transforms ops) or CRDTs (commutative, peer-friendly). WebSocket per doc session, ops log + periodic snapshots, cursor presence, offline sync, version history.

```
Clients --ops--> Collab server (OT/CRDT) -> broadcast -> ops log
```

### 72. Design an email service (Gmail).

**Answer:** SMTP ingest -> spam/virus filter -> mailbox store (per-user partition, wide-column) + search index; IMAP/web API for reads; attachments in object store; queues for outbound with retries; SPF/DKIM/DMARC.

```
SMTP in -> Filter -> Mailbox store + Index <- API/IMAP
Outbound queue -> SMTP out
```

### 73. Design a rate-limited public API platform.

**Answer:** Gateway enforces auth (API keys), quotas per plan, throttling per endpoint, usage metering via async events to billing, versioning, developer portal, webhooks with retries and signatures.

```
Dev -> Gateway(key, quota) -> Services; usage events -> Billing
```

### 74. Design a distributed file system (GFS/HDFS).

**Answer:** Master/NameNode stores namespace and chunk locations; files split into large chunks (64-128MB) replicated 3x across racks; clients read/write directly to chunkservers; heartbeats, re-replication, write pipeline.

```
Client -> NameNode (metadata)
Client <-> DataNodes (chunks, replicated)
```

### 75. Design S3 (object store).

**Answer:** Flat key space with metadata index (partitioned) separate from data layer; objects stored with replication or erasure coding across AZs; multipart upload, versioning, lifecycle policies, strong read-after-write consistency, checksums and scrubbing for durability (11 nines).

```
PUT -> Front-end -> Metadata index + Storage nodes (erasure coded)
```

### 76. Design a parking lot / elevator system (low-level design).

**Answer:** Identify entities (Lot, Level, Spot, Ticket, Vehicle, Payment), use enums and state machines, strategy pattern for pricing/spot allocation, thread-safe allocation, then extend to distributed (sharded by lot, DB constraints).

```
Vehicle -> Gate -> SpotAllocator -> Ticket -> Payment -> Exit
```

### 77. Design a multiplayer game backend.

**Answer:** Authoritative game servers with tick loops (20-60Hz), UDP/WebSocket, client prediction + reconciliation, matchmaking service (skill/latency), regional shards, session state in memory with snapshots, anti-cheat.

```
Clients <-UDP-> Game server (tick) <- Matchmaker
```

### 78. Design an IoT telemetry platform.

**Answer:** Devices publish via MQTT to brokers -> Kafka -> stream processing -> time-series DB + cold storage; device registry/shadow, OTA updates, auth via certificates, edge aggregation for intermittent connectivity.

```
Devices -MQTT-> Broker -> Kafka -> TSDB/Lake -> Dashboards/Alerts
```

### 79. Design a Slack-like workplace messaging system.

**Answer:** Workspaces/channels, messages stored per channel partition with monotonically increasing IDs, WebSocket gateways with channel subscriptions via pub/sub, search index, threads, files in object store, unread counts via per-user cursors, notifications.

```
Client <-WS-> Gateway <-> PubSub <-> Message svc -> Store + Search
```

### 80. Design an online voting / polling system with real-time results.

**Answer:** Writes via queue to prevent overload, dedup per user with unique constraint, sharded counters aggregated periodically, results broadcast via SSE/WebSocket from cache; integrity via auditing and idempotency.

```
Vote -> Queue -> Counter shards -> Aggregator -> Cache -> SSE -> Clients
```

---

## Part C: Advanced Patterns and Reliability

### 81. What is the Saga pattern?

**Answer:** Long-running distributed transaction as a sequence of local transactions, each with a compensating action. Orchestration (central coordinator) vs choreography (events). Gives eventual consistency without 2PC locks.

```
Order -> Reserve stock -> Charge -> Ship
fail at Charge -> release stock -> cancel order
```

### 82. Two-phase commit (2PC) vs 3PC vs Saga?

**Answer:** 2PC: coordinator asks prepare, then commit; atomic but blocking if the coordinator fails and slow. 3PC reduces blocking but is rarely used. Saga trades atomicity for availability. Use 2PC inside tightly-coupled DBs, Saga across services.

```
Coord: PREPARE -> all yes -> COMMIT   (any no -> ABORT)
```

### 83. CQRS and Event Sourcing?

**Answer:** CQRS separates write model from optimized read models. Event sourcing stores every state change as an immutable event; state = replay; supports audit and time travel; requires snapshots and event versioning. Projections update read stores asynchronously.

```
Command -> Event store -> Projector -> Read DB <- Query
```

### 84. Transactional Outbox pattern?

**Answer:** Write business data and an outbox event row in the same DB transaction; a relay (poller or CDC like Debezium) publishes to the broker. Guarantees no lost or phantom events; consumers must be idempotent.

```
Tx[ update order + insert outbox ] -> CDC -> Kafka
```

### 85. Circuit breaker, retry, timeout, bulkhead?

**Answer:** Timeouts bound waiting; retries with exponential backoff + jitter (only idempotent calls); circuit breaker opens after failures to fail fast and half-opens to probe; bulkheads isolate resource pools; fallbacks degrade gracefully.

```
CLOSED -fail threshold-> OPEN -timeout-> HALF-OPEN -> CLOSED/OPEN
```

### 86. Leader election and consensus (Paxos/Raft)?

**Answer:** Raft: terms, randomized election timeouts, leader replicates log entries, committed when a majority acks; safety through log matching and majority quorums. Used by etcd, Consul. ZooKeeper uses ZAB. Tolerates f failures with 2f+1 nodes.

```
Follower -timeout-> Candidate -majority-> Leader -> AppendEntries
```

### 87. Quorum reads/writes?

**Answer:** With N replicas, write to W and read from R; R+W>N guarantees overlap with the latest write. Tune: W=N (fast reads), R=1; or majority for balance. Sloppy quorums + hinted handoff boost availability.

```
N=3, W=2, R=2: write {A,B}, read {B,C} -> overlap B
```

### 88. Gossip protocol and failure detection?

**Answer:** Nodes periodically exchange state with random peers; information spreads in O(log N) rounds; scalable membership and failure detection (heartbeat counters, phi-accrual) without a central coordinator (Cassandra, Consul).

```
A <-> D, D <-> F, F <-> B ... eventually all know
```

### 89. Bloom filters and probabilistic structures?

**Answer:** Bloom filter: bit array + k hashes; no false negatives, possible false positives; used to skip disk lookups, dedup crawlers, cache penetration protection. Count-Min Sketch (frequencies), HyperLogLog (cardinality), Cuckoo filter (supports delete).

```
add(x): set bits h1(x)..hk(x);  query: all set? maybe : no
```

### 90. Backpressure and load shedding?

**Answer:** Prevent overload by propagating slowness upstream: bounded queues, rate limits, reactive streams, shedding low-priority work (return 503/degrade), adaptive concurrency limits, autoscaling with warm capacity.

```
Producer -> [bounded queue] -x full -> reject/slow producer
```

### 91. Deployment strategies: blue-green, canary, rolling?

**Answer:** Blue-green: two environments, switch traffic instantly, easy rollback. Canary: route small percentage, watch metrics, ramp up. Rolling: replace instances gradually. Use feature flags and backward-compatible DB migrations (expand/contract).

```
LB -> 95% v1 | 5% v2 (canary)
```

### 92. Multi-region architecture and disaster recovery?

**Answer:** Active-passive (cheaper, failover with RPO/RTO) vs active-active (low latency, needs conflict handling, global data replication, geo-DNS/anycast routing). Define RPO/RTO, regularly test failover, avoid cross-region sync calls on the critical path.

```
GeoDNS -> Region A (primary) <-replication-> Region B (standby/active)
```

### 93. Observability: logs, metrics, traces, SLO/SLI?

**Answer:** Metrics (RED: rate, errors, duration; USE for resources), structured logs with correlation IDs, distributed traces. Define SLIs/SLOs and error budgets; alert on symptoms (user impact) not causes; runbooks and post-mortems.

```
Service -> metrics + logs + traces -> dashboards/alerts
```

### 94. Data pipeline architectures: Lambda vs Kappa; batch vs stream?

**Answer:** Lambda: batch layer (accurate) + speed layer (fast) merged at serving. Kappa: a single streaming path with log replay for reprocessing. Modern: stream-first with lakehouse (Iceberg/Delta), exactly-once semantics via checkpoints.

```
Source -> Kafka -> Stream job -> Serving
                \-> Lake (replay)
```

### 95. Data warehouse vs data lake vs lakehouse?

**Answer:** Warehouse: structured, schema-on-write, SQL BI (Snowflake, BigQuery). Lake: raw files in object storage, schema-on-read, cheap. Lakehouse: lake + ACID table formats and warehouse performance. Orchestrate ETL/ELT, catalog and governance.

```
Sources -> Lake (raw) -> Transform -> Warehouse/Lakehouse -> BI
```

### 96. Exactly-once processing: is it possible?

**Answer:** Truly exactly-once delivery is impossible over unreliable networks; achieve effectively-once via at-least-once delivery + idempotent/transactional processing (dedup keys, Kafka transactions, atomic offset+state commit).

```
retry delivery + dedup(id) = effectively once
```

### 97. Handling time, ordering and clocks in distributed systems?

**Answer:** Physical clocks drift; use logical clocks (Lamport), vector clocks for causality, hybrid logical clocks, or TrueTime-style bounded uncertainty. Order per partition via sequence numbers; avoid relying on wall-clock for correctness (use fencing tokens).

```
A:1 -> B:2 -> C:3     (Lamport: max(local, recv) + 1)
```

### 98. Multi-tenancy and data isolation (SaaS)?

**Answer:** Models: shared DB shared schema (tenant_id column + row-level security), schema per tenant, database per tenant (strong isolation). Add per-tenant rate limits and quotas (noisy neighbor), encryption keys per tenant, tenant-aware sharding.

```
Tenant -> Router -> Shared pool | Dedicated DB (big tenants)
```

### 99. Security in system design (zero trust, encryption, secrets)?

**Answer:** TLS everywhere + mTLS between services, encryption at rest (KMS, envelope encryption), least privilege IAM, secrets manager rotation, input validation, WAF/DDoS protection, audit logging, PII minimization, defense in depth.

```
User -> WAF -> GW(authN/Z) -> Svc (mTLS) -> DB (encrypted)
```

### 100. How do you scale a system from 0 to millions of users?

**Answer:** Start with a single server; separate web and DB; add load balancer and stateless app tier; DB replication, cache, CDN; move assets to object storage; shard the DB; introduce queues/async workers; split into services; multi-region; invest in monitoring and automation at each step. Optimize the current bottleneck, measured, not guessed.

```
1 box -> LB+N app -> cache+CDN -> replicas -> shards -> services -> multi-region
```
