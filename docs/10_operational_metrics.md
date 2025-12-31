# Operational Metrics

Goal: make production health visible, actionable, and tied to SLOs.

---

## Golden signals (per service)
### Traffic
- RPS by endpoint (feed vs user)
- request distribution by region/zone (conceptual)

### Errors
- 5xx rate, error budget burn
- top error signatures (by endpoint)

### Latency
- p50/p95/p99 for each critical endpoint
- tail latency correlation with saturation and dependency latency

### Saturation
- CPU, memory, queue depth
- cache hit rate, DB latency/QPS

---

## Dashboards (what I would pin)
### 1) SLO Dashboard (exec view)
- Current month SLO attainment (availability + latency)
- Error budget remaining + burn-rate
- Top 3 active risks/alerts

### 2) Service Health Dashboard (on-call view)
- Feed/User p95/p99
- 5xx rate + retry rate
- CPU/queue depth
- cache hit rate + DB latency

### 3) Dependency Dashboard
- Cache: hit rate, evictions, memory pressure
- DB: p95 query latency, connections, timeouts
- Network: cross-tier latency

---

## Alert to metric mapping
- A1 latency burn-rate → latency p95/p99 + saturation + deploy timeline
- A2 5xx spike → top signatures + dependency health + retry rate
- A3 crash loop → restarts + health checks + config/version

---

## “Debug recipe” (first principles)
1. Identify symptom: latency/errors/saturation
2. Determine scope: endpoint + region + version
3. Correlate: deploy/config + dependency metrics
4. Mitigate safely: kill-switch → scale → rate limit → rollback
5. Prevent: add test/guardrail/alert/runbook update
