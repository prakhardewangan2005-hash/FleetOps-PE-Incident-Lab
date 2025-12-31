# On-call Playbook

## Paging rules
- Page only for likely user impact (SLO breach / fast burn-rate / crash loop).
- Every page must map to a runbook.
- Prefer safe mitigations: kill-switch → scale → rate limit → rollback.

## Severity definitions
- **SEV1:** major outage / widespread unavailability, crash loops
- **SEV2:** partial outage / SLO breach with significant user impact
- **SEV3:** degradation without clear user impact (ticket, not page)

## First 5 minutes checklist (SEV2/SEV1)
1. Identify impacted service: **Feed vs User**
2. Confirm scope: **global vs region/zone**
3. Check deploy timeline: changes in last **30 minutes**
4. Check golden signals:
   - latency p95/p99
   - 5xx error rate
   - saturation (CPU/queues)
   - cache hit rate / DB latency
5. Choose lowest-risk mitigation:
   - kill-switch OFF risky path
   - scale out if saturated
   - rate limit to stop retry storm
   - rollback if correlated with release

## Communication cadence
- **SEV1:** update every 10 minutes
- **SEV2:** update every 15 minutes
- Always include: status, impact, mitigation, next update time

## After mitigation (stabilization)
- Validate SLO recovery for 10 minutes
- Confirm errors stabilize (<1%)
- Create postmortem within 24 hours
- Track prevention actions to completion
