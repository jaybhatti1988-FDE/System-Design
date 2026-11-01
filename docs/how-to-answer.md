# How to Answer a System Design Question

| Step | Time | What to do |
|:--|:--:|:--|
| 1. Requirements | 5 min | Features, users, read/write ratio, latency, consistency, availability |
| 2. Estimation | 5 min | DAU → QPS (÷86,400, peak ×2–5), storage, bandwidth |
| 3. API + data model | 5 min | Endpoints, entities, SQL vs NoSQL choice |
| 4. High-level design | 10 min | Client → LB → services → cache → DB / queues |
| 5. Deep dive | 15 min | Bottlenecks: sharding, caching, fan-out, hot keys |
| 6. Wrap-up | 5 min | Trade-offs, failure modes, monitoring, future work |

## Useful numbers
- 1 day ≈ 10^5 seconds; 1M requests/day ≈ 12 QPS
- Memory ≈ 100 ns · SSD ≈ 100 µs · same-DC RTT ≈ 0.5 ms · cross-continent ≈ 150 ms
