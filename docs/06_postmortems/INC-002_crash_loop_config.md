# INC-002 — Crash Loop from Config Mismatch

## Summary
A configuration change introduced an invalid setting that caused the service to fail on startup and enter a restart loop.

## Impact
- Elevated 5xx errors on feed endpoints (simulated)
- Partial unavailability until rollback

## Detection
- A3 crash-loop alert triggered (restart count + failing health checks)

## Root Cause
- Config change lacked schema validation and staged rollout
- No automated config linting in CI

## Resolution
- Rolled back config to last known good
- Restarted stable replicas
- Release freeze until verification completed

## Prevention / Action Items
1. Add config schema validation + linting in CI
2. Stage config rollouts (10% → 25% → 50% → 100%)
3. Add runbook step to validate config version during triage
4. Add automated rollback on restart-loop detection

## What went well
- Clear signal and fast rollback path

## What didn’t go well
- Missing validation allowed invalid config to reach production
