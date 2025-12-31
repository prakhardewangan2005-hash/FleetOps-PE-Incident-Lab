# SLOs & Alerts

## Service Objectives (monthly)
### Availability
- Feed API: **99.9%**
- User API: **99.95%**

### Latency (steady-state)
- Feed: **p95 < 200ms**, **p99 < 400ms**
- User: **p95 < 150ms**, **p99 < 300ms**

### Errors
- 5xx error rate: **< 1%** (global)

### Saturation guardrails
- CPU sustained < 70%
- Memory sustained < 75%
- Cache hit rate > 90% (feed path)

---

## Error budgets (why they matter)
- Feed 99.9% monthly ⇒ ~43.2 minutes unavailability/month.
- If budget burn-rate is high: **release freeze** + reliability work becomes priority.

---

## Alert philosophy (paging discipline)
- Page only for likely user impact.
- Prefer **burn-rate** alerts over noisy static thresholds.
- Every alert must map to a runbook.

---

## Paging alerts (examples)
### A1 — Feed latency burn-rate (SEV2 page)
Triggers when:
- p95 latency > 200ms for 5 minutes **OR**
- burn-rate predicts error budget exhaustion within hours

Runbook: `docs/03_runbooks.md#runbook-r1-feed-latency`

### A2 — 5xx error spike (SEV2 page)
Triggers when:
- 5xx > 2% for 3 minutes

Runbook: `docs/03_runbooks.md#runbook-r2-error-spike`

### A3 — Crash loop / unhealthy instances (SEV1 page)
Triggers when:
- health checks failing OR restarts spike

Runbook: `docs/03_runbooks.md#runbook-r3-crash-loop`

---

## Non-paging alerts (ticket)
- Cache hit rate dipping
- DB latency drift
- CPU creeping upward week-over-week

These create follow-up work **without waking on-call**.
