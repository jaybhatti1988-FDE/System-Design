<div align="center">

# 🏗️ System Design Interview Handbook

**100 essential system design questions — with concise answers and diagrams.**

![Questions](https://img.shields.io/badge/questions-100-blue?style=for-the-badge)
![Diagrams](https://img.shields.io/badge/diagrams-included-success?style=for-the-badge)
![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen?style=for-the-badge)
![License](https://img.shields.io/badge/license-MIT-lightgrey?style=for-the-badge)

[Start learning](#-roadmap) · [Question index](#-question-index) · [How to answer](docs/how-to-answer.md) · [Contribute](CONTRIBUTING.md)

</div>

---

## 📖 About

A practical, interview-focused guide to system design. Every question has a short answer, key trade-offs and a diagram so you can revise quickly.

- **Part A – Fundamentals:** scaling, caching, databases, queues, APIs
- **Part B – Classic designs:** URL shortener, chat, Uber, YouTube, payments…
- **Part C – Advanced patterns:** saga, CQRS, Raft, multi-region, observability

## 🗺️ Roadmap

```mermaid
flowchart LR
    A[Fundamentals<br/>Q1-30] --> B[Classic Designs<br/>Q31-80] --> C[Advanced Patterns<br/>Q81-100] --> D[Mock Interviews]
```

| Week | Focus | Questions |
|:--:|:--|:--|
| 1 | Scaling, LB, caching, DB basics | 1–15 |
| 2 | Queues, APIs, reliability, estimation | 16–30 |
| 3–4 | Classic designs | 31–80 |
| 5 | Patterns, consensus, multi-region | 81–100 |
| 6 | Mock interviews + revision | All |

## 🎯 How to answer any question

1. Clarify requirements (functional / non-functional)
2. Estimate scale (QPS, storage, bandwidth)
3. Define API and data model
4. Draw high-level design
5. Deep-dive bottlenecks
6. Discuss trade-offs, failures, monitoring

More in [docs/how-to-answer.md](docs/how-to-answer.md).

## 📚 Question index

<!-- INDEX:START -->
### Part A: Fundamentals

| # | Question |
|--:|:--|
| 1 | [Vertical vs horizontal scaling?](docs/01-fundamentals/001-vertical-vs-horizontal-scaling.md) |
| 2 | [What is a load balancer and which algorithms exist?](docs/01-fundamentals/002-what-is-a-load-balancer-and-which-algorithms-exist.md) |
| 3 | [Explain the CAP theorem.](docs/01-fundamentals/003-explain-the-cap-theorem.md) |
| 4 | [Strong vs eventual consistency?](docs/01-fundamentals/004-strong-vs-eventual-consistency.md) |
| 5 | [How does caching work and where do you place caches?](docs/01-fundamentals/005-how-does-caching-work-and-where-do-you-place-caches.md) |
| 6 | [Cache write strategies?](docs/01-fundamentals/006-cache-write-strategies.md) |
| 7 | [How do you handle cache invalidation, stampede and hot keys?](docs/01-fundamentals/007-how-do-you-handle-cache-invalidation-stampede-and-hot-keys.md) |
| 8 | [SQL vs NoSQL?](docs/01-fundamentals/008-sql-vs-nosql.md) |
| 9 | [What is database sharding and how do you choose a shard key?](docs/01-fundamentals/009-what-is-database-sharding-and-how-do-you-choose-a-shard-key.md) |
| 10 | [What is consistent hashing?](docs/01-fundamentals/010-what-is-consistent-hashing.md) |
| 11 | [Database replication models?](docs/01-fundamentals/011-database-replication-models.md) |
| 12 | [Explain database indexing.](docs/01-fundamentals/012-explain-database-indexing.md) |
| 13 | [B-tree vs LSM-tree storage engines?](docs/01-fundamentals/013-b-tree-vs-lsm-tree-storage-engines.md) |
| 14 | [What is a CDN?](docs/01-fundamentals/014-what-is-a-cdn.md) |
| 15 | [What is an API gateway?](docs/01-fundamentals/015-what-is-an-api-gateway.md) |
| 16 | [How do you design a rate limiter?](docs/01-fundamentals/016-how-do-you-design-a-rate-limiter.md) |
| 17 | [Message queues: why and when?](docs/01-fundamentals/017-message-queues-why-and-when.md) |
| 18 | [Kafka vs RabbitMQ / SQS?](docs/01-fundamentals/018-kafka-vs-rabbitmq-sqs.md) |
| 19 | [Pub/Sub vs point-to-point?](docs/01-fundamentals/019-pub-sub-vs-point-to-point.md) |
| 20 | [What is idempotency and how do you implement it?](docs/01-fundamentals/020-what-is-idempotency-and-how-do-you-implement-it.md) |
| 21 | [REST vs gRPC vs GraphQL?](docs/01-fundamentals/021-rest-vs-grpc-vs-graphql.md) |
| 22 | [Polling vs long polling vs WebSockets vs SSE?](docs/01-fundamentals/022-polling-vs-long-polling-vs-websockets-vs-sse.md) |
| 23 | [Stateless vs stateful services?](docs/01-fundamentals/023-stateless-vs-stateful-services.md) |
| 24 | [Authentication and authorization (OAuth2, JWT, sessions)?](docs/01-fundamentals/024-authentication-and-authorization-oauth2-jwt-sessions.md) |
| 25 | [How do you estimate capacity (back-of-envelope)?](docs/01-fundamentals/025-how-do-you-estimate-capacity-back-of-envelope.md) |
| 26 | [Availability and SLAs: how do you reach 99.99%?](docs/01-fundamentals/026-availability-and-slas-how-do-you-reach-99-99.md) |
| 27 | [Latency vs throughput?](docs/01-fundamentals/027-latency-vs-throughput.md) |
| 28 | [Microservices vs monolith?](docs/01-fundamentals/028-microservices-vs-monolith.md) |
| 29 | [Service discovery?](docs/01-fundamentals/029-service-discovery.md) |
| 30 | [Blob/object storage vs file vs block storage?](docs/01-fundamentals/030-blob-object-storage-vs-file-vs-block-storage.md) |

### Part B: Classic System Designs

| # | Question |
|--:|:--|
| 31 | [Design a URL shortener (TinyURL).](docs/02-classic-designs/031-design-a-url-shortener-tinyurl.md) |
| 32 | [Design Pastebin.](docs/02-classic-designs/032-design-pastebin.md) |
| 33 | [Design a distributed key-value store (Dynamo-style).](docs/02-classic-designs/033-design-a-distributed-key-value-store-dynamo-style.md) |
| 34 | [Design a unique ID generator.](docs/02-classic-designs/034-design-a-unique-id-generator.md) |
| 35 | [Design a web crawler.](docs/02-classic-designs/035-design-a-web-crawler.md) |
| 36 | [Design a notification system (push/SMS/email).](docs/02-classic-designs/036-design-a-notification-system-push-sms-email.md) |
| 37 | [Design a news feed (Facebook/Twitter timeline).](docs/02-classic-designs/037-design-a-news-feed-facebook-twitter-timeline.md) |
| 38 | [Design Twitter.](docs/02-classic-designs/038-design-twitter.md) |
| 39 | [Design Instagram.](docs/02-classic-designs/039-design-instagram.md) |
| 40 | [Design a chat system (WhatsApp/Messenger).](docs/02-classic-designs/040-design-a-chat-system-whatsapp-messenger.md) |
| 41 | [Design group chat and presence (online status).](docs/02-classic-designs/041-design-group-chat-and-presence-online-status.md) |
| 42 | [Design search autocomplete (typeahead).](docs/02-classic-designs/042-design-search-autocomplete-typeahead.md) |
| 43 | [Design YouTube / Netflix (video streaming).](docs/02-classic-designs/043-design-youtube-netflix-video-streaming.md) |
| 44 | [Design Google Drive / Dropbox.](docs/02-classic-designs/044-design-google-drive-dropbox.md) |
| 45 | [Design Uber / ride hailing.](docs/02-classic-designs/045-design-uber-ride-hailing.md) |
| 46 | [Design a proximity service (Yelp / nearby friends).](docs/02-classic-designs/046-design-a-proximity-service-yelp-nearby-friends.md) |
| 47 | [Design Google Maps.](docs/02-classic-designs/047-design-google-maps.md) |
| 48 | [Design a ticket booking system (Ticketmaster).](docs/02-classic-designs/048-design-a-ticket-booking-system-ticketmaster.md) |
| 49 | [Design a hotel reservation system (Airbnb/Booking).](docs/02-classic-designs/049-design-a-hotel-reservation-system-airbnb-booking.md) |
| 50 | [Design an e-commerce platform (Amazon).](docs/02-classic-designs/050-design-an-e-commerce-platform-amazon.md) |
| 51 | [Design a flash sale system.](docs/02-classic-designs/051-design-a-flash-sale-system.md) |
| 52 | [Design a payment system.](docs/02-classic-designs/052-design-a-payment-system.md) |
| 53 | [Design a digital wallet.](docs/02-classic-designs/053-design-a-digital-wallet.md) |
| 54 | [Design a stock exchange / order matching engine.](docs/02-classic-designs/054-design-a-stock-exchange-order-matching-engine.md) |
| 55 | [Design a metrics/monitoring system (Prometheus/Datadog).](docs/02-classic-designs/055-design-a-metrics-monitoring-system-prometheus-datadog.md) |
| 56 | [Design an ad click aggregation system.](docs/02-classic-designs/056-design-an-ad-click-aggregation-system.md) |
| 57 | [Design a distributed message queue.](docs/02-classic-designs/057-design-a-distributed-message-queue.md) |
| 58 | [Design a distributed cache (Redis/Memcached cluster).](docs/02-classic-designs/058-design-a-distributed-cache-redis-memcached-cluster.md) |
| 59 | [Design a distributed lock service.](docs/02-classic-designs/059-design-a-distributed-lock-service.md) |
| 60 | [Design a distributed job scheduler.](docs/02-classic-designs/060-design-a-distributed-job-scheduler.md) |
| 61 | [Design a leaderboard.](docs/02-classic-designs/061-design-a-leaderboard.md) |
| 62 | [Design a video conferencing system (Zoom/Meet).](docs/02-classic-designs/062-design-a-video-conferencing-system-zoom-meet.md) |
| 63 | [Design a food delivery system (DoorDash/Swiggy).](docs/02-classic-designs/063-design-a-food-delivery-system-doordash-swiggy.md) |
| 64 | [Design a recommendation system.](docs/02-classic-designs/064-design-a-recommendation-system.md) |
| 65 | [Design a search engine (Google/Elasticsearch).](docs/02-classic-designs/065-design-a-search-engine-google-elasticsearch.md) |
| 66 | [Design log aggregation (ELK/Splunk).](docs/02-classic-designs/066-design-log-aggregation-elk-splunk.md) |
| 67 | [Design a distributed tracing system.](docs/02-classic-designs/067-design-a-distributed-tracing-system.md) |
| 68 | [Design a feature flag service.](docs/02-classic-designs/068-design-a-feature-flag-service.md) |
| 69 | [Design a CI/CD system.](docs/02-classic-designs/069-design-a-ci-cd-system.md) |
| 70 | [Design a web analytics system (Google Analytics).](docs/02-classic-designs/070-design-a-web-analytics-system-google-analytics.md) |
| 71 | [Design Google Docs (real-time collaborative editing).](docs/02-classic-designs/071-design-google-docs-real-time-collaborative-editing.md) |
| 72 | [Design an email service (Gmail).](docs/02-classic-designs/072-design-an-email-service-gmail.md) |
| 73 | [Design a rate-limited public API platform.](docs/02-classic-designs/073-design-a-rate-limited-public-api-platform.md) |
| 74 | [Design a distributed file system (GFS/HDFS).](docs/02-classic-designs/074-design-a-distributed-file-system-gfs-hdfs.md) |
| 75 | [Design S3 (object store).](docs/02-classic-designs/075-design-s3-object-store.md) |
| 76 | [Design a parking lot / elevator system (low-level design).](docs/02-classic-designs/076-design-a-parking-lot-elevator-system-low-level-design.md) |
| 77 | [Design a multiplayer game backend.](docs/02-classic-designs/077-design-a-multiplayer-game-backend.md) |
| 78 | [Design an IoT telemetry platform.](docs/02-classic-designs/078-design-an-iot-telemetry-platform.md) |
| 79 | [Design a Slack-like workplace messaging system.](docs/02-classic-designs/079-design-a-slack-like-workplace-messaging-system.md) |
| 80 | [Design an online voting / polling system with real-time results.](docs/02-classic-designs/080-design-an-online-voting-polling-system-with-real-time-result.md) |

### Part C: Advanced Patterns and Reliability

| # | Question |
|--:|:--|
| 81 | [What is the Saga pattern?](docs/03-advanced-patterns/081-what-is-the-saga-pattern.md) |
| 82 | [Two-phase commit (2PC) vs 3PC vs Saga?](docs/03-advanced-patterns/082-two-phase-commit-2pc-vs-3pc-vs-saga.md) |
| 83 | [CQRS and Event Sourcing?](docs/03-advanced-patterns/083-cqrs-and-event-sourcing.md) |
| 84 | [Transactional Outbox pattern?](docs/03-advanced-patterns/084-transactional-outbox-pattern.md) |
| 85 | [Circuit breaker, retry, timeout, bulkhead?](docs/03-advanced-patterns/085-circuit-breaker-retry-timeout-bulkhead.md) |
| 86 | [Leader election and consensus (Paxos/Raft)?](docs/03-advanced-patterns/086-leader-election-and-consensus-paxos-raft.md) |
| 87 | [Quorum reads/writes?](docs/03-advanced-patterns/087-quorum-reads-writes.md) |
| 88 | [Gossip protocol and failure detection?](docs/03-advanced-patterns/088-gossip-protocol-and-failure-detection.md) |
| 89 | [Bloom filters and probabilistic structures?](docs/03-advanced-patterns/089-bloom-filters-and-probabilistic-structures.md) |
| 90 | [Backpressure and load shedding?](docs/03-advanced-patterns/090-backpressure-and-load-shedding.md) |
| 91 | [Deployment strategies: blue-green, canary, rolling?](docs/03-advanced-patterns/091-deployment-strategies-blue-green-canary-rolling.md) |
| 92 | [Multi-region architecture and disaster recovery?](docs/03-advanced-patterns/092-multi-region-architecture-and-disaster-recovery.md) |
| 93 | [Observability: logs, metrics, traces, SLO/SLI?](docs/03-advanced-patterns/093-observability-logs-metrics-traces-slo-sli.md) |
| 94 | [Data pipeline architectures: Lambda vs Kappa; batch vs stream?](docs/03-advanced-patterns/094-data-pipeline-architectures-lambda-vs-kappa-batch-vs-stream.md) |
| 95 | [Data warehouse vs data lake vs lakehouse?](docs/03-advanced-patterns/095-data-warehouse-vs-data-lake-vs-lakehouse.md) |
| 96 | [Exactly-once processing: is it possible?](docs/03-advanced-patterns/096-exactly-once-processing-is-it-possible.md) |
| 97 | [Handling time, ordering and clocks in distributed systems?](docs/03-advanced-patterns/097-handling-time-ordering-and-clocks-in-distributed-systems.md) |
| 98 | [Multi-tenancy and data isolation (SaaS)?](docs/03-advanced-patterns/098-multi-tenancy-and-data-isolation-saas.md) |
| 99 | [Security in system design (zero trust, encryption, secrets)?](docs/03-advanced-patterns/099-security-in-system-design-zero-trust-encryption-secrets.md) |
| 100 | [How do you scale a system from 0 to millions of users?](docs/03-advanced-patterns/100-how-do-you-scale-a-system-from-0-to-millions-of-users.md) |
<!-- INDEX:END -->

## 🤝 Contributing

PRs are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md) and the [question template](docs/TEMPLATE.md).

## ⭐ Support

If this helps you, star the repo and share it with a friend preparing for interviews.

## 📄 License

[MIT](LICENSE)
