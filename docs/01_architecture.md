# Architecture

## High-level flow
```text
Clients
  ↓
API Gateway (routing, rate limiting, canary / kill-switch)
  ↓
User Service  —— Cache
  ↓
Feed Service  —— Cache —— DB
  ↓
Observability (metrics + logs + traces)
  ↓
Alerts → On-call → Runbook → Mitigation → Postmortem → Prevention

Component responsibilities
API Gateway

Routing by endpoint + version

Rate limiting / load shedding under stress

Canary ramp + fast rollback hooks (change safety)

Request IDs / correlation propagation

User Service

Low-latency profile reads/writes

Strong focus on correctness and predictable latency

Cache-aside pattern for hot reads

Feed Service

Latency-sensitive, high traffic

Tail latency (p95/p99) is the primary risk

Uses cache to protect DB and stabilize p99

Cache + DB (modeled dependencies)

Cache absorbs burst traffic and reduces DB fanout

DB is the reliability bottleneck (slow queries, lock contention, connection limits)

Observability

Minimum viable “PE contract” per component:

Metrics: RPS, 5xx rate, p50/p95/p99 latency, saturation

Logs: structured + request-id / trace-id

Traces: high-latency sampling for p99 debugging

Failure domains (what breaks in production)
Domain	Example failure	Primary symptom	Fastest safe mitigation
Release regression	heavier code path enabled	p95/p99 latency spike	kill-switch OFF + rollback
Crash loop	bad config/env	5xx spike + restarts	rollback config + restart stable replicas
Cache miss storm	TTL/eviction issue	DB QPS spike + latency	increase TTL + warm cache + rate limit
DB degradation	slow query / lock	rising latency + timeouts	degrade optional features + shed load
Network spike	packet loss/latency	cross-tier latency jump	shift traffic / reduce cross-zone calls
What I would monitor first (golden signals)

Traffic: RPS per endpoint (feed vs user)

Errors: 5xx %, top error signatures

Latency: p50/p95/p99 (tail latency focus)

Saturation: CPU/memory/queue depth + dependency QPS

Design choices that reduce MTTR

Kill-switch at gateway for risky paths

Canary rollout ladder with rollback triggers

Runbooks organized by symptoms, not components

Postmortems produce prevention actions (tests, limits, alerts)
