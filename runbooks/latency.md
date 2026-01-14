# Latency Incident Runbook (FleetOps)

## Detection
- Alert: **HighLatency**
- Symptom: p95 latency > 1s for 2 minutes

## Immediate Checks
1. Confirm service is reachable:
   - `curl http://localhost:8080`
2. Check metrics endpoint:
   - `curl http://localhost:8080/metrics | head`

## Diagnosis (Prometheus)
- Open Prometheus: `http://localhost:9090`
- Query (p95 latency):
  - `histogram_quantile(0.95, rate(http_request_latency_seconds_bucket[5m]))`

## Mitigation Options
- Restart service (fastest):
  - `docker compose restart app`
- Reduce load (if traffic generator running)
- Rollback recent change (if applicable)

## Verification
- p95 latency returns below 500ms
- Alert resolves
