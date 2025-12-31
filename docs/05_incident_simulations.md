# Incident Simulations (Game Days)

Goal: validate that alerts are actionable, runbooks reduce MTTR, and mitigations are safe under pressure.

---

## Game Day format
**Inputs:** dashboards + alerts + recent deploy timeline  
**Output:** incident log + mitigation decision + follow-up tasks + postmortem link

**Rules**
- Prefer lowest-risk mitigation: kill-switch → scale → rate limit → rollback
- Communicate early and on a schedule (SEV discipline)
- Always end with prevention work

---

## Scenario S1 — Feed latency regression after rollout (SEV2)

### Trigger (what changed)
- A CPU-heavy feed path was enabled without canary gating/rate limiting.

### Detection (what paged)
- A1 latency alert: Feed p95 > 200ms (burn-rate)

### Symptoms
- p95 crosses 200ms, p99 spikes
- saturation rises (CPU/queue depth)

### Triage checklist (5 min)
- scope: global vs region
- correlation: deploy in last 30 min?
- cache hit rate drop? DB latency up?

### Mitigation steps (safe order)
1. **Kill-switch OFF** heavy feed path
2. **Scale out** feed replicas if saturation persists
3. **Rate limit** heavy endpoints at gateway
4. **Rollback** release if SLO remains breached

### Success criteria
- p95 < 200ms for 10 minutes
- 5xx < 1%
- saturation trending down

### Follow-up
- Postmortem: `docs/06_postmortems/INC-001_feed_latency_regression.md`

---

## Scenario S2 — Crash loop due to config mismatch (SEV1)

### Trigger
- A config change introduced an invalid setting causing startup failure.

### Detection
- A3 crash-loop / unhealthy instances alert

### Symptoms
- restarts spike
- availability drop and rising 5xx

### Mitigation steps
1. **Rollback config** to last known good
2. **Rollback deploy** if binary suspected
3. Restore baseline replicas and validate health checks

### Success criteria
- stable health for 10 minutes
- 5xx returns below threshold

### Follow-up
- Postmortem: `docs/06_postmortems/INC-002_crash_loop_config.md`

---

## What these simulations validate
- Alerts are low-noise and map to clear actions
- Runbooks are usable under stress
- Rollback and kill-switch mechanisms are documented
- Prevention work is created and tracked after incidents
