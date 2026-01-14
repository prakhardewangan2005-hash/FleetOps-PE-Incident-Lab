# INC-001 — High Latency Incident (FleetOps)

## Summary
High latency alert triggered for FleetOps service when p95 latency exceeded the 1s threshold. Incident was mitigated by stopping load and removing the latency injection from the request path.

## Customer Impact
- Elevated response times; p95 reached ~2.2s
- No data loss

## Detection
- Alert: **HighLatency** (Prometheus)
- Condition: p95 latency > 1s (short window for lab demo)

## Timeline (IST)
- T0: Alert **HighLatency** entered FIRING
- T+1m: On-call validated via PromQL (p95 ~2.2s)
- T+2m: Identified root cause: intentional latency injection in request handler
- T+3m: Mitigation: stopped load generator, reduced sleep to normal range
- T+4m: Service restarted
- T+5m: Alert resolved (state INACTIVE)

## Root Cause
Artificial latency injection (`sleep`) in the request path caused sustained slow responses under load.

## Resolution
- Removed/rolled back high sleep value
- Restarted app container
- Verified p95 returned to normal range and alert resolved

## What Went Well
- Monitoring + metrics were available
- Alerting detected the issue quickly
- Clear runbook guided verification and mitigation

## What Didn’t Go Well
- No automated rollback / guardrails for injected latency
- Alert tuning needed for fresh environments (demo window)

## Action Items
- Add a controlled fault-injection endpoint (feature flag / env var)
- Add error-rate SLO + alert (5xx)
- Add simple load test to CI (smoke performance check)
