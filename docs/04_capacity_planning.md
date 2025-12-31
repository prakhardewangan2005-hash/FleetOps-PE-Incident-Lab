# Capacity Planning

## Goals
- Maintain SLOs during peak traffic and bursts
- Keep safe **headroom (30%)** to avoid saturation-driven incidents
- Define clear autoscaling triggers that protect tail latency

---

## Traffic model (peak assumptions)
> (Simulated but consistent across repo)

- Feed: **900 RPS** peak
- User: **600 RPS** peak
- Burst factor: **1.5×** during events / spikes
- Target headroom: **30%**
- Primary risk: **tail latency (p95/p99)** under saturation

---

## Baseline sizing (service-level)
### Feed Service
- Observed target stability at peak with ~6 replicas (conceptual)
- Apply 30% headroom ⇒ **8 replicas baseline**
- Autoscale range: **6 → 12**

### User Service
- Baseline: **4 replicas**
- Autoscale range: **3 → 8**

---

## Scaling policy (safe + SLO-aligned)
### Scale out (fast)
Trigger when **any** is true for 3 minutes:
- CPU > 65% sustained  
- Queue depth rising (work backlog)
- Feed p95 crosses 200ms (SLO pressure)

### Scale in (slow)
Only when stable for 15 minutes:
- CPU < 45%
- p95 comfortably under SLO
- No recent deploy / incident activity

---

## Dependency protection (avoid cascades)
### Cache
- Maintain hit rate > 90% (feed path)
- During incident: increase TTL temporarily to reduce churn

### DB
- Protect via:
  - rate limiting / load shedding at gateway
  - degraded mode (disable heavy features)
  - query budget (pagination limits, fanout reduction)

---

## Capacity risks & mitigations
| Risk | What happens | Mitigation |
|---|---|---|
| Cache miss storm | DB QPS spikes, latency climbs | warm cache + TTL increase + rate limit |
| Release regression | p95/p99 spikes at same RPS | canary + rollback + kill-switch |
| Retry storm | errors trigger retries → overload | rate limit failing routes + backoff |
| Hot partitions/keys | uneven load, tail latency | caching + key sharding (conceptual) |

---

## “Ready for on-call” checklist
Before ramping traffic:
- dashboards exist for traffic/errors/latency/saturation
- paging alerts mapped to runbooks
- rollback plan is written and tested (conceptual)
- kill-switch available for high-risk paths

---

## Output artifacts (what this doc provides)
- Baseline replica counts + autoscale ranges
- Clear triggers tied to SLO pressure
- Dependency protection strategy to avoid cascading failures
