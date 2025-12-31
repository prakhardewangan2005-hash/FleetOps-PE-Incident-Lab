# Change Management

Goal: ship changes safely without violating SLOs or exhausting error budgets.

---

## Release principles
1. **Safety over speed** — rollback is a feature, not a failure.
2. **Small blast radius** — canary before full rollout.
3. **Signals decide** — SLOs and burn-rate drive go/no-go.
4. **Reversibility** — every change must have a rollback plan.

---

## Release safety ladder
1. **Pre-deploy checks**
   - Load test critical paths (p95/p99)
   - Verify dashboards and alerts exist
   - Confirm rollback mechanism (feature flag / revert)

2. **Canary rollout**
   - Start with **10% traffic**
   - Observe for **15 minutes**
   - Monitor latency, errors, saturation

3. **Ramp-up**
   - 10% → 25% → 50% → 100%
   - Hold at each step if signals degrade

4. **Automated rollback**
   - Triggered if:
     - p95 latency breaches SLO
     - 5xx error rate > threshold
     - burn-rate predicts budget exhaustion

---

## Rollback policy
Rollback immediately when:
- SLO breach persists for >5 minutes
- Error budget burn-rate is high
- Crash loops or severe errors detected

Rollback actions:
- Disable feature via kill-switch
- Revert config / deploy previous version
- Restore baseline replicas

---

## Error budget policy
- **Healthy budget:** normal release cadence
- **Budget burning:** slow down releases, increase monitoring
- **Budget exhausted:** release freeze until reliability improves

---

## Change review checklist
Before approving a change:
- [ ] Rollout plan written
- [ ] Rollback plan written
- [ ] Canary + kill-switch available
- [ ] Dashboards + alerts linked
- [ ] On-call owner identified

---

## Outcome
This process minimizes blast radius, reduces MTTR, and ensures reliability improves over time rather than degrading with velocity.
