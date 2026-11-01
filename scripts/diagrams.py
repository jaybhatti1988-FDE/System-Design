"""Mermaid diagrams for the 100 questions, written as chains of nodes (A -> B -> C)."""

def esc(s):
    return s.replace('"', "'")

def to_mermaid(chains):
    ids, decl, edges, seen = {}, [], [], set()
    for ch in chains:
        for label in ch:
            if label not in ids:
                ids[label] = f"n{len(ids)}"
                decl.append(f'    {ids[label]}["{esc(label)}"]')
        for a, b in zip(ch, ch[1:]):
            e = (ids[a], ids[b])
            if e not in seen:
                seen.add(e)
                edges.append(f"    {e[0]} --> {e[1]}")
    direction = "TD" if max(len(c) for c in chains) > 5 else "LR"
    return f"flowchart {direction}\n" + "\n".join(decl + edges)

DEEP_DIVES = {
    16: "02-rate-limiter.md", 31: "01-url-shortener.md", 36: "05-notification-system.md",
    37: "03-news-feed.md", 40: "04-chat-system.md", 43: "06-video-streaming.md",
    44: "08-file-storage-sync.md", 45: "07-ride-hailing.md", 48: "09-ticket-booking.md",
    52: "10-payment-system.md",
}

D = {
1: [["Small server", "Bigger server (vertical)"], ["Small server", "Many servers behind a load balancer (horizontal)"]],
2: [["Client", "Load balancer", "Server 1"], ["Load balancer", "Server 2"], ["Load balancer", "Server 3"]],
3: [["Network partition", "CP: stay consistent (reject requests)"], ["Network partition", "AP: stay available (may be stale)"]],
4: [["Write", "Leader", "Replica (async: may be stale)"], ["Leader", "Replica (sync: always fresh)"]],
5: [["Client", "App", "Cache"], ["Cache", "Hit: return data"], ["Cache", "Miss: read DB", "Fill cache"]],
6: [["Write-through: App", "Cache (wt)", "DB (sync)"], ["Write-back: App", "Cache (wb)", "DB (async flush)"]],
7: [["1000 concurrent misses", "Per-key lock", "1 DB query", "Fill cache", "999 requests read cache"]],
8: [["SQL: tables, joins, ACID"], ["NoSQL: key to document or columns"]],
9: [["user_id hash mod 3", "Shard 0"], ["user_id hash mod 3", "Shard 1"], ["user_id hash mod 3", "Shard 2"]],
10: [["Key", "Hash ring position", "Next node clockwise"], ["Add or remove a node", "Only ~1/N keys move"]],
11: [["Writes", "Leader", "Follower 1"], ["Leader", "Follower 2"], ["Reads", "Follower 1"], ["Reads", "Follower 2"]],
12: [["Query", "Index (B-tree)", "Row pointer", "Table row"]],
13: [["Write", "WAL + memtable", "Flush to SSTable", "Compaction"]],
14: [["User", "Edge cache", "Content (hit)"], ["Edge cache", "Origin (miss)"]],
15: [["Clients", "API gateway: auth, rate limit", "Service A"], ["API gateway: auth, rate limit", "Service B"], ["API gateway: auth, rate limit", "Service C"]],
16: [["Request", "Rate limiter (Redis counters)", "Allow: service"], ["Rate limiter (Redis counters)", "Deny: HTTP 429"]],
17: [["Producer", "Queue", "Consumers"], ["Consumers", "DLQ after repeated failure"]],
18: [["Producer", "Topic partitions P0, P1", "Consumer group"]],
19: [["Publisher", "Topic", "Subscriber A"], ["Topic", "Subscriber B"]],
20: [["POST /pay + idempotency key", "Key seen?"], ["Key seen?", "No: process and save result"], ["Key seen?", "Yes: return saved result"]],
21: [["REST: many resource endpoints"], ["gRPC: protobuf over HTTP/2"], ["GraphQL: one flexible endpoint"]],
22: [["Client", "WebSocket gateway", "Pub/Sub backplane", "Other gateways"]],
23: [["Request", "Any stateless instance", "Shared Redis / DB"]],
24: [["User", "IdP login", "Auth code", "Access token", "API verifies signature"]],
25: [["100M DAU x 10 req/day", "Divide by 86,400 s", "~11.5K QPS average", "x3 for peak", "~35K QPS"]],
26: [["Load balancer", "AZ1: app + DB"], ["Load balancer", "AZ2: app + DB replica"]],
27: [["Batching", "Higher throughput", "Higher latency"], ["Caching", "Lower latency"]],
28: [["Monolith: A + B + C", "Split on clear boundaries", "Service A"], ["Split on clear boundaries", "Service B"], ["Split on clear boundaries", "Service C"]],
29: [["Service", "Registers in registry"], ["Client", "Looks up registry", "Healthy instance"]],
30: [["App", "Metadata DB (id, url)"], ["App", "Object store (bytes)", "CDN"]],
31: [["Client", "Load balancer", "App", "Redis cache", "DB (code, url)"], ["App", "Key generation service"]],
32: [["Client", "App", "Metadata DB"], ["App", "Object store", "CDN"]],
33: [["Client", "Coordinator", "Replica N1"], ["Coordinator", "Replica N2"], ["Coordinator", "Replica N3"]],
34: [["Sign bit 0", "Timestamp 41 bits", "Machine ID 10 bits", "Sequence 12 bits"]],
35: [["Seed URLs", "URL frontier", "Fetcher", "Parser", "Dedup", "Store"], ["Parser", "New URLs", "URL frontier"]],
36: [["Service", "Notification API", "Kafka", "Push / SMS / Email workers", "Providers"]],
37: [["New post", "Fan-out service", "Follower feed caches"], ["Read feed", "Feed cache + celebrity posts", "Rank", "Timeline"]],
38: [["Client", "Gateway", "Tweet service", "Tweet DB"], ["Gateway", "Timeline service", "Redis"], ["Gateway", "Search and trends", "Stream processing"]],
39: [["Upload", "Object store", "Resize workers", "CDN"], ["Upload", "Metadata DB shards", "Feed cache"]],
40: [["User A", "Chat server 1 (WebSocket)", "Message store / Kafka", "Chat server 2", "User B"], ["Message store / Kafka", "Push notification (offline)"]],
41: [["Client", "Heartbeat", "Presence service (Redis TTL)", "Pub/Sub", "Online friends"]],
42: [["Query logs", "Aggregator", "Trie builder", "Trie servers", "Client"]],
43: [["Upload", "Raw store", "Transcode", "Segments", "CDN", "Player (adaptive bitrate)"]],
44: [["Client (chunker)", "Metadata service", "Object store"], ["Client (chunker)", "Block service", "Object store"], ["Notification service", "Client (chunker)"]],
45: [["Driver", "Location service (geo index)", "Matching service"], ["Rider", "Matching service", "Trip service", "Payments"]],
46: [["lat/lng", "Geohash cell", "Query cell + 8 neighbors", "Filter by distance"]],
47: [["Client", "Tile CDN"], ["Client", "Routing service (graph shards)", "Traffic stream"]],
48: [["Select seat", "Hold seat (TTL 5 min)", "Pay", "Confirm"], ["Hold seat (TTL 5 min)", "Expired: release seat"]],
49: [["Search (Elasticsearch)", "Reservation service", "Inventory DB (lock)", "Payment"]],
50: [["UI", "API gateway", "Catalog"], ["API gateway", "Cart"], ["API gateway", "Order", "Inventory", "Payment", "Shipping"]],
51: [["Users", "CDN / WAF", "Queue", "Redis stock DECR", "Order workers", "DB"]],
52: [["Checkout", "Payment service", "PSP"], ["Payment service", "Ledger DB"], ["Payment service", "Reconciliation"]],
53: [["Debit A (hold)", "Credit B", "Commit"], ["Credit B", "Failure: compensate"]],
54: [["Orders", "Gateway (risk checks)", "Sequencer", "Matching engine", "Trades", "Market data"]],
55: [["Hosts", "Collector", "Kafka", "Time-series DB", "Dashboards"], ["Time-series DB", "Alert manager"]],
56: [["Clicks", "Kafka", "Flink windows", "OLAP DB"], ["Kafka", "Raw events in S3", "Batch reconcile"]],
57: [["Producer", "Broker (partition leader)", "Replicas"], ["Consumer group", "Broker (partition leader)"]],
58: [["Client", "Proxy", "Slot to node", "Master + replica"]],
59: [["Client", "etcd lease key", "Fencing token n", "Storage rejects stale tokens"]],
60: [["Job DB (next_run)", "Scheduler", "Queue", "Workers", "Status DB"]],
61: [["Score event", "Redis sorted set", "Top 10"], ["Redis sorted set", "My rank"]],
62: [["Participant A", "SFU"], ["Participant B", "SFU"], ["Participant C", "SFU"], ["SFU", "Subscribers"]],
63: [["Order", "Restaurant", "Dispatch", "Courier (live location)", "Customer"]],
64: [["Request", "Candidate generation (ANN)", "Ranker", "Re-rank", "Results"], ["Events", "Feature store", "Model training", "Ranker"]],
65: [["Documents", "Indexer", "Index shards", "Query broker", "Client"]],
66: [["Apps", "Agent", "Kafka", "Parser", "Elasticsearch", "Kibana"]],
67: [["Service A (span 1)", "Service B (span 2)", "Service C (span 3)", "Collector", "Trace store"]],
68: [["Admin UI", "Flag store", "CDN / stream", "SDK (local evaluation)"]],
69: [["Push", "Orchestrator", "Build", "Test", "Artifact repo", "Deploy"]],
70: [["Browser", "Collector", "Kafka", "Flink", "OLAP", "Dashboard"]],
71: [["Clients", "Collab server (OT / CRDT)", "Broadcast to clients"], ["Collab server (OT / CRDT)", "Ops log + snapshots"]],
72: [["SMTP in", "Spam / virus filter", "Mailbox store + index", "API / IMAP"], ["Outbound queue", "SMTP out"]],
73: [["Developer", "Gateway (key, quota)", "Services"], ["Services", "Usage events", "Billing"]],
74: [["Client", "NameNode (metadata)"], ["Client", "DataNodes (replicated chunks)"]],
75: [["PUT object", "Front end", "Metadata index"], ["Front end", "Storage nodes (erasure coded)"]],
76: [["Vehicle", "Gate", "Spot allocator", "Ticket", "Payment", "Exit"]],
77: [["Matchmaker", "Game server (tick loop)", "Clients"]],
78: [["Devices", "MQTT broker", "Kafka", "Time-series DB / lake", "Dashboards / alerts"]],
79: [["Client", "WebSocket gateway", "Pub/Sub", "Message service", "Store + search"]],
80: [["Vote", "Queue", "Counter shards", "Aggregator", "Cache", "SSE", "Clients"]],
81: [["Order", "Reserve stock", "Charge", "Ship"], ["Charge", "Fails: release stock", "Cancel order"]],
82: [["Coordinator: PREPARE", "All vote yes", "COMMIT"], ["Coordinator: PREPARE", "Any vote no", "ABORT"]],
83: [["Command", "Event store", "Projector", "Read DB", "Query"]],
84: [["Transaction: update order + insert outbox", "CDC relay", "Kafka"]],
85: [["CLOSED", "OPEN (failures over threshold)", "HALF-OPEN (after timeout)", "CLOSED"], ["HALF-OPEN (after timeout)", "OPEN (failures over threshold)"]],
86: [["Follower", "Candidate (election timeout)", "Leader (majority votes)", "AppendEntries to followers"]],
87: [["N=3, W=2, R=2", "Write to A, B", "B overlaps", "Latest value found"], ["N=3, W=2, R=2", "Read from B, C", "B overlaps"]],
88: [["Node A", "Node D", "Node F", "Node B", "Eventually all nodes know"]],
89: [["add(x)", "Set k hash bits"], ["query(x)", "All bits set?", "Maybe present"], ["All bits set?", "Definitely absent"]],
90: [["Producer", "Bounded queue", "Consumer"], ["Bounded queue", "Full: reject or slow producer"]],
91: [["Load balancer", "95% to v1"], ["Load balancer", "5% to v2 (canary)"]],
92: [["Geo DNS", "Region A (primary)", "Replication", "Region B (standby / active)"]],
93: [["Service", "Metrics", "Dashboards + alerts"], ["Service", "Logs", "Dashboards + alerts"], ["Service", "Traces", "Dashboards + alerts"]],
94: [["Source", "Kafka", "Stream job", "Serving"], ["Kafka", "Lake (replay)"]],
95: [["Sources", "Lake (raw)", "Transform", "Warehouse / lakehouse", "BI"]],
96: [["At-least-once delivery (retries)", "Dedup by id / transactions", "Effectively once"]],
97: [["A: clock 1", "B: clock 2", "C: clock 3"]],
98: [["Tenant", "Router", "Shared pool"], ["Router", "Dedicated DB (big tenants)"]],
99: [["User", "WAF", "Gateway (authN / authZ)", "Service (mTLS)", "DB (encrypted)"]],
100: [["1 server", "LB + N app servers", "Cache + CDN", "Read replicas", "Shards", "Services", "Multi-region"]],
}

DIAGRAMS = {n: to_mermaid(c) for n, c in D.items()}
