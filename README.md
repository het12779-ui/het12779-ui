<a href="https://github.com/het12779-ui">
  <img src="assets/banner.svg" alt="Het Patel — full-stack engineer building ad-tech systems: spend pacing, attribution, anomaly detection" width="100%">
</a>

<p align="center">
  <a href="https://github.com/het12779-ui/paceguard"><img src="https://img.shields.io/badge/pacing-guardrails-3ddc97?style=flat-square&labelColor=0b0f14" alt="PaceGuard"></a>
  <a href="https://github.com/het12779-ui/channeltruth"><img src="https://img.shields.io/badge/attribution-5%20models-a78bfa?style=flat-square&labelColor=0b0f14" alt="ChannelTruth"></a>
  <a href="https://github.com/het12779-ui/adsentry"><img src="https://img.shields.io/badge/anomalies-log%20search-f6b73c?style=flat-square&labelColor=0b0f14" alt="AdSentry"></a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white" alt="FastAPI">
  <img src="https://img.shields.io/badge/SQL%20Server-CC2927?style=flat-square&logo=microsoftsqlserver&logoColor=white" alt="SQL Server">
  <img src="https://img.shields.io/badge/Vue%203-4FC08D?style=flat-square&logo=vuedotjs&logoColor=white" alt="Vue 3">
  <img src="https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white" alt="Docker">
  <img src="https://img.shields.io/badge/GitHub%20Actions-2088FF?style=flat-square&logo=githubactions&logoColor=white" alt="GitHub Actions">
</p>

I build the unglamorous layer of advertising software: the part that decides whether
₹3,00,000 of budget lands on schedule, which channel actually earned a conversion, and
whether a campaign broke at 2am while everyone was asleep.

Three services, one lifecycle — **ingest → model → monitor** — each with a real database
schema, a browser UI, tests that touch no mocks, and a CI job that boots the app and
curls it.

---

## Selected work

<table>
<tr>
<td width="33%" valign="top">
<a href="https://github.com/het12779-ui/paceguard"><img src="assets/paceguard.webp" width="100%" alt="PaceGuard dashboard"></a>

<b><a href="https://github.com/het12779-ui/paceguard">PaceGuard</a></b><br>
<sub>Budget pacing &amp; spend governance</sub>

A campaign spending 70% of its budget by day 5 is not "70% done". Projects final spend
along the campaign's own curve and raises guardrail alerts that fire once, not every
hour.

<sub><b>46 tests</b> · 72 ms p50 @ 1,000 campaigns · query count constant</sub>
</td>
<td width="33%" valign="top">
<a href="https://github.com/het12779-ui/channeltruth"><img src="assets/channeltruth.webp" width="100%" alt="ChannelTruth dashboard"></a>

<b><a href="https://github.com/het12779-ui/channeltruth">ChannelTruth</a></b><br>
<sub>Multi-touch attribution &amp; ROAS</sub>

The same journeys scored under five models at once — because "which channel gets
credit" is a decision, not a fact. Google reads 1.57× under last-touch and 0.55× under
first-touch; the disagreement is the product.

<sub><b>102 tests</b> · 0.37 s @ 5,000 journeys · identical totals across models</sub>
</td>
<td width="33%" valign="top">
<a href="https://github.com/het12779-ui/adsentry"><img src="assets/adsentry.webp" width="100%" alt="AdSentry dashboard"></a>

<b><a href="https://github.com/het12779-ui/adsentry">AdSentry</a></b><br>
<sub>Anomaly detection &amp; log search</sub>

Robust z-scores against same-weekday baselines, stateful incidents that cannot storm,
and an inverted-index log search in SQL — the "is it broken, and why" layer, without
standing up a second cluster to page about.

<sub><b>39 tests</b> · 246 ms @ 1,000 campaigns · 7 ms search @ 20k events</sub>
</td>
</tr>
</table>

<p align="center"><sub>Every screenshot is the seeded demo running against its own API — no mockups.</sub></p>

---

## How the three fit together

```mermaid
flowchart LR
    subgraph sources["Platform sync"]
        S1["Spend events"]
        S2["Touches + conversions"]
        S3["Daily delivery metrics"]
    end

    subgraph services["Services (FastAPI · SQL · Vue 3)"]
        P["<b>PaceGuard</b><br/>pacing, projections,<br/>guardrail alerts"]
        C["<b>ChannelTruth</b><br/>journeys, 5 models,<br/>ROAS by channel"]
        A["<b>AdSentry</b><br/>detection, incidents,<br/>log search"]
    end

    S1 -->|idempotent upsert| P
    S2 -->|journey assembly| C
    S3 -->|metric restatement| A

    P --> D["<b>Decision</b><br/>shift budget, pause,<br/>or call the client"]
    C --> D
    A -->|root cause| D

    classDef svc fill:#0e1420,stroke:#3ddc97,stroke-width:1px,color:#eef2f8
    classDef out fill:#0e1420,stroke:#a78bfa,stroke-width:1px,color:#eef2f8
    class P,C,A svc
    class D out
```

---

## What I care about in code

**Tenant isolation is a query property, not a filter.** `account_id` is the first argument
of every repository function and appears in every statement. Cross-tenant reads return
**404, not 403** — the API must not confirm that another tenant's id exists. A schema test
fails if a new table forgets the column.

**Idempotency belongs in the database.** At-least-once sync means retries will happen.
Uniqueness lives in tenant-scoped constraints, because application-level checks race.

**Money is integer minor units.** Never `float`, never SQL `MONEY`. Formatting happens at
the edge, after all arithmetic is exact.

**An alert must be explainable to a non-engineer.** Every one carries the observed value,
the baseline and the threshold that fired. "Anomaly detected" is not a diagnosis;
"clicks dropped 61% versus the last four Mondays" is.

**Evaluation is not a read-path side effect.** Detection and pacing run on ingest or an
explicit trigger, never while serving a dashboard, so latency stays predictable and
results are replayable.

---

## Evidence, not adjectives

| | PaceGuard | ChannelTruth | AdSentry |
|---|---:|---:|---:|
| Tests (pytest + BDD, no DB mocks) | 46 | 102 | 39 |
| Endpoint latency, p50 | 72 ms @ 1k campaigns | 0.37 s @ 5k journeys | 246 ms @ 1k campaigns |
| Data model | SQL Server DDL, filtered + partial unique indexes | same | same |
| UI | Vue 3, no build step | same | same |
| CI | Actions: 3.11 + 3.12 + live smoke | same | same |

Benchmarks are reproducible with `make bench` in each repo; the READMEs state the
honest limits (unpaginated overview, SQLite demo store) rather than rounding them away.

---

## Currently

- **Learning C#** — the services here are Python because that is what I could build and
  test end to end. The REST contracts, multi-tenant schema and BDD scenarios port
  directly, and I would rather say that than borrow confidence I have not earned.
- **Reading** production postmortems from ad-tech outages; the failure modes are
  consistently boring (pixels, timezones, retries) and consistently expensive.
- **Open to** Associate Product Engineer / full-stack roles on advertising or data
  platforms.

---

<p align="center">
  <a href="mailto:het12779@gmail.com"><img src="https://img.shields.io/badge/email-het12779@gmail.com-3ddc97?style=flat-square&labelColor=0b0f14" alt="Email"></a>
  <a href="https://github.com/het12779-ui?tab=repositories"><img src="https://img.shields.io/badge/repositories-all%20projects-a78bfa?style=flat-square&labelColor=0b0f14" alt="Repositories"></a>
</p>

<p align="center"><sub>Built and measured on a laptop, not a slide deck.</sub></p>
