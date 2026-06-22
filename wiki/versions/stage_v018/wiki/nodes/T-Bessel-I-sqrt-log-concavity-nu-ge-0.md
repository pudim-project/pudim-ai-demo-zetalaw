---
id: "T-Bessel-I-sqrt-log-concavity-nu-ge-0"
type: "theorem"
title: "forall nu >= 0, u -> sqrt(u) I_nu(u) strictly log-concave on (0,infty)"
status: "open"
tags: ["bessel", "fresh-forage", "log-concavity", "open", "open-problem", "special-functions", "terminal", "theorem"]
parents: ["T-Bessel-I-Riccati-log-concavity-inequality", "T-Bessel-I-ratio-quadratic-bound", "T-Bessel-I-split-regime-log-concavity-certificate"]
refs: ["librarian/audits/LA-20260526T122752-forage-ingest.json", "raw/scout/FI-20260526T122752Z.md", "raw/scout/RS-FI-20260526T122752Z.json", "scout/forage/inbox/FI-20260526T122752Z.json", "wiki/notes/forage-20260526-fresh-open-problems.md"]
---

# Theorem: forall nu >= 0, u -> sqrt(u) I_nu(u) strictly log-concave on (0,infty)

## Statement

For every \(\nu\ge0\), the function \(u\mapsto \sqrt{u}\,I_\nu(u)\) is strictly log-concave on \((0,\infty)\).

## Dependencies

- [[wiki/nodes/T-Bessel-I-Riccati-log-concavity-inequality|forall nu >= 0, u > 0, 1+(nu^2-1/2)/u^2-r/u-r^2 < 0 for r=I_nu'/I_nu]]
- [[wiki/nodes/T-Bessel-I-ratio-quadratic-bound|forall nu >= 0, u > 0, q^2+(2nu+1)q/u+(nu+1/2)/u^2 > 1 for q=I_{nu+1}/I_nu]]
- [[wiki/nodes/T-Bessel-I-split-regime-log-concavity-certificate|three-regime certified proof of Bessel I sqrt log-concavity via small-u series, large-u asymptotics, compact interval certificate]]

## Proof and provenance references

- `librarian/audits/LA-20260526T122752-forage-ingest.json`
- `raw/scout/FI-20260526T122752Z.md`
- `raw/scout/RS-FI-20260526T122752Z.json`
- `scout/forage/inbox/FI-20260526T122752Z.json`
- `wiki/notes/forage-20260526-fresh-open-problems.md`

## Tags

`bessel`, `fresh-forage`, `log-concavity`, `open`, `open-problem`, `special-functions`, `terminal`, `theorem`
