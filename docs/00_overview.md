# Overview

## Goal
This repo is a documentation-first Production Engineering artifact that demonstrates:
- Reliability targets (SLOs) and error budgets
- Burn-rate alerting + paging discipline
- Runbooks that reduce MTTR
- Capacity planning with headroom and scaling policy
- Incident simulations and postmortems
- Change management + risk controls

## What makes this PE-grade
1. **Production-first:** safety > speed; rollback is a feature.
2. **Signal-driven:** latency (p50/p95/p99), errors, traffic, saturation.
3. **On-call ready:** deterministic runbooks, not tribal knowledge.
4. **Prevention culture:** postmortems with action items and owners.
5. **Capacity aware:** peak modeling + 30% headroom baseline.

## Modeled system
- API Gateway (routing, rate limiting, canary/kill-switch controls)
- User Service (low-latency reads/writes)
- Feed Service (high traffic + tail latency sensitive)
- Cache + DB (conceptual dependencies)
- Observability (metrics/logs/traces) + alerting + on-call workflow

## How to read
Start with:
- `docs/02_slos_and_alerts.md`
- `docs/03_runbooks.md`
Then review:
- `docs/06_postmortems/`
