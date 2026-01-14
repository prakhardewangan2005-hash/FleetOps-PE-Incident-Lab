# 📊 Monitoring — FleetOps PE Incident Lab

This directory contains the **complete monitoring and alerting setup** used in the FleetOps
production-style incident response lab.  
It demonstrates **real SLO monitoring, alert firing, and incident validation** using Prometheus.

---

## 🔗 Live Prometheus (Codespaces Demo)

**Prometheus UI (Live):**  
https://vigilant-journey-97rwrj757665f97qp-9090.app.github.dev/query

> ⚠️ Note  
> This link works **only while the Codespace is running**.  
> If the Codespace is stopped, the URL may return **HTTP 502**.

---

## 📁 Files in this Directory

### 1️⃣ `prometheus.yml` — Scrape Configuration
Defines how Prometheus scrapes metrics from the FleetOps service.

**Key points:**
- Scrape interval optimized for demo/testing
- Scrapes metrics from:
