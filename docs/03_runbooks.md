# Runbooks

> Goal: Reduce MTTR by making mitigation steps deterministic under stress.
> Rule: Always start with the lowest-risk mitigation (kill-switch → scale → rate limit → rollback).

---

## Runbook R1 — Feed latency regression (p95 > 200ms)

### Symptoms
- p95 rising; p99 spikes (tail latency)
- user complaints: slow feed loads / timeouts
- saturation may increase (CPU, queues)

### Triage (first 5 minutes)
1. **Confirm scope:** global vs single region / zone  
2. **Check correlations:**
   - 5xx rising with latency? (could be overload)
   - CPU/memory/queue depth spikes?
   - cache hit rate drop? DB latency up?
3. **Check deploy timeline:** any rollout/config change in last 30 minutes?

### Safe mitigations (lowest risk first)
1. **Kill-switch:** disable heavy feed path / expensive features
2. **Scale out:** increase replicas if CPU/queues show saturation
3. **Rate limit / shed load:** protect DB + stabilize tail latency
4. **Rollback:** if correlated with a release and SLO stays breached

### Validation
- p95 < 200ms for 10 minutes
- 5xx < 1%
- saturation trending down

### Follow-up
- Postmortem + prevention: canary gating, load tests, p99 guardrails

---

## Runbook R2 — Error spike (5xx > 2%)

### Symptoms
- 5xx climbs quickly; retries may amplify load
- some endpoints fail more than others

### Triage
1. Identify **which endpoint** is failing (feed vs user)
2. Inspect **top error signatures** (config, dependency, timeout)
3. Check dependency health (cache/DB)

### Mitigation
1. **Rollback** last release if correlated
2. **Rate limit** the failing route (stop retry storms)
3. **Degrade** optional features to reduce load
4. If dependency is failing: apply safe fallback / circuit-breaker behavior (conceptual)

### Validation
- 5xx < 1% sustained
- request rate stabilizes

---

## Runbook R3 — Crash loop / unhealthy instances (SEV1)

### Symptoms
- restart loop, health checks failing
- sharp availability drop

### Triage (fast)
1. Confirm restart loop: recent config/env change?
2. Is it all instances or subset (zone-specific)?

### Mitigation
1. **Rollback config** to last known good (fastest)
2. **Rollback deploy** if binary change is suspected
3. Bring up stable replicas (restore baseline capacity)

### Validation
- health checks stable for 10 minutes
- error rate returns below threshold

---

## Runbook R4 — Cache miss storm (hit rate < target)

### Symptoms
- cache hit rate drops; DB QPS spikes
- latency increases without obvious CPU rise in service

### Mitigation
1. Increase TTL temporarily (reduce churn)
2. Warm cache for hot keys
3. Rate limit expensive endpoints (protect DB)
4. Verify eviction policy and memory pressure

---

## Runbook R5 — DB slow queries / saturation

### Symptoms
- DB latency up; timeouts; queue depth rises

### Mitigation
1. Degrade non-critical features that hit DB heavily
2. Reduce fan-out (batching / pagination limits)
3. Rate limit heavy endpoints
4. Create follow-up: indexing + query optimization

---

## Runbook R6 — Network latency spike between tiers

### Symptoms
- cross-tier latency jumps; intermittent errors

### Mitigation
1. Shift traffic away from unhealthy zone/region (conceptual)
2. Reduce cross-zone calls if possible
3. Temporarily tune timeouts ONLY with caution (avoid cascading failures)
