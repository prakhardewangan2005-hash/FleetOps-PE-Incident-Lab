# INC-001 — Feed Latency Regression

## Summary
A rollout enabled a CPU-heavy feed path without safety guards, causing p95 latency to exceed the SLO.

## Impact
- Feed loads slowed; risk of timeouts
- p95 peaked ~480ms (simulated)
- Error budget burn-rate increased

## Detection
- A1 latency burn-rate alert fired ~3 minutes after regression

## Root Cause
- CPU-heavy path lacked rate limiting and canary gating
- Insufficient pre-deploy load testing for tail latency (p99)

## Resolution
- Disabled heavy path via kill-switch (feature flag)
- Scaled feed replicas temporarily to reduce saturation
- Prepared rollback plan if SLO remained breached

## Prevention / Action Items
1. Canary rollout with automated rollback on SLO breach
2. Rate limit heavy endpoint at the gateway
3. Add pre-deploy load test for p95/p99 + saturation checks
4. Add alert for sustained CPU > 70% with latency correlation

## What went well
- Fast detection (minutes)
- Runbook led to safe mitigation without guesswork

## What didn’t go well
- Missing canary gate allowed regression to hit too much traffic
- Tail latency testing wasn’t enforced before ramp

## Follow-up owner (example)
- Reliability owner: PE on-call rotation (weekly)
