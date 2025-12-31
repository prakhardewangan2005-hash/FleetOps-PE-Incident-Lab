<div align="center">

# FleetOps — PE Incident Lab  
### Production Engineering case study: SLOs • burn-rate alerts • runbooks • capacity planning • postmortems • change safety

<p>
  <img alt="Status" src="https://img.shields.io/badge/status-active-success">
  <img alt="Focus" src="https://img.shields.io/badge/focus-Production%20Engineering-blue">
  <img alt="Docs" src="https://img.shields.io/badge/artifact-documentation--first-informational">
</p>

**What this repo shows:** how I would operate and harden a high-traffic service in production — with operational rigor.

</div>

**Notes:** Docs-first PE portfolio artifact: SLOs, runbooks, postmortems, change safety.


---

## Why this maps strongly to Meta Production Engineering
Meta PEs debug **live production** issues, define **SLOs**, enforce paging discipline, write runbooks to reduce MTTR, and plan capacity for peak traffic.

This repo demonstrates:
- **Reliability & performance**: SLOs, error budgets, burn-rate alerts  
- **Incident response**: triage → mitigation → validation → postmortem  
- **Capacity planning**: headroom, scaling triggers, burst modeling  
- **Change safety**: canary, rollback, risk controls

---

## System modeled
```text
Clients
  ↓
API Gateway (routing, rate limiting, canary controls)
  ↓
User Service —— Cache
  ↓
Feed Service —— Cache —— DB
  ↓
Observability (metrics + logs + traces)
  ↓
Alerts → On-call → Runbook → Mitigation → Postmortem → Prevention
```

## Quick start (recruiter path)
1) `docs/02_slos_and_alerts.md`  
2) `docs/03_runbooks.md`  
3) `docs/06_postmortems/`  
4) `docs/08_change_management.md`

Tip: Start with SLOs → Runbooks → Postmortems to see incident handling end-to-end.

## Key artifacts
- SLOs & alerts: `docs/02_slos_and_alerts.md`
- Runbooks: `docs/03_runbooks.md`
- Postmortems: `docs/06_postmortems/`
- Change safety: `docs/08_change_management.md`

## Docs index
- `docs/00_overview.md` — scope + how to read
- `docs/01_architecture.md` — system + failure domains
- `docs/02_slos_and_alerts.md` — SLOs, error budgets, burn-rate alerts
- `docs/03_runbooks.md` — triage → mitigate → validate
- `docs/04_capacity_planning.md` — headroom, scaling triggers
- `docs/05_incident_simulations.md` — game days + drills
- `docs/06_postmortems/` — incident writeups + prevention
- `docs/07_oncall_playbook.md` — oncall habits + escalation
- `docs/08_change_management.md` — canary/rollback + guardrails
- `docs/09_risk_register.md` — risks + mitigations
- `docs/10_operational_metrics.md` — golden signals + dashboards






