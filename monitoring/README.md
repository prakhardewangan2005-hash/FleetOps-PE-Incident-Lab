# 📊 Monitoring – FleetOps PE Incident Lab

This folder contains all monitoring and alerting configuration used in the FleetOps
production-style incident response lab.

## Contents

### 🔹 Prometheus Configuration
- **File:** `prometheus.yml`
- Defines scrape targets and global scrape interval
- Scrapes metrics from the FleetOps service (`/metrics` endpoint)

### 🔹 Alert Rules
- **File:** `alerts.yml`
- Defines SLO-based alerting
- Example alert:
  - **HighLatency**: Fires when p95 latency exceeds threshold

## How it is used
1. FleetOps service exposes Prometheus metrics
2. Prometheus scrapes metrics from the service
3. Alert rules evaluate latency SLOs
4. Alerts trigger incident response workflows

## Related Docs
- 📘 Runbooks: [`../runbooks/`](../runbooks/)
- 🧾 Incidents / Postmortems: [`../incidents/`](../incidents/)
- 📄 Root overview: [`../README.md`](../README.md)
