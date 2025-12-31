# Risk Register

Goal: proactively identify production risks and define clear mitigations before incidents occur.

---

## Risk matrix

| Risk | Likelihood | Impact | Detection Signal | Mitigation |
|---|---|---|---|---|
| Latency regression after deploy | Medium | High | p95/p99 spike | Canary + rollback + kill-switch |
| Crash loop from bad config | Medium | High | Restart loop alert | Config validation + staged rollout |
| Cache miss storm | High | Medium | Cache hit rate drop, DB QPS spike | TTL tuning + cache warmup + rate limit |
| DB slow queries | Medium | High | DB latency/QPS alerts | Degrade features + query optimization |
| Retry storm | Medium | High | RPS spike + error amplification | Rate limit + backoff |
| Traffic surge / event spike | Low | High | RPS spike | Autoscaling + headroom |
| Network latency spike | Low | High | Cross-tier latency | Traffic shift + zone isolation |

---

## High-risk areas (focus)
- **Feed service:** tail latency sensitivity
- **DB dependency:** saturation cascades
- **Config changes:** high blast radius if unvalidated
- **Rollouts:** primary source of incidents historically

---

## Risk ownership
- Each high-risk item must have:
  - an owner (team / on-call rotation)
  - a detection signal
  - a documented mitigation or runbook

---

## Review cadence
- Review risk register **monthly**
- Update after every SEV1/SEV2 postmortem
- Close risks only when mitigations are proven effective

---

## Outcome
Maintaining a live risk register shifts reliability work from reactive firefighting to proactive prevention.
