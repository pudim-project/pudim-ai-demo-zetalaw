---
id: "T-Q2-J-rational-interval-terminal-certificate"
type: "theorem"
title: "deterministic rational interval certificate on J for R Lambda G Q2 proves terminal endpoint"
status: "open"
tags: ["attack-plan", "microinterval", "open", "rational-interval-arithmetic", "terminal-route", "theorem", "wide"]
parents: ["T-Q2-terminal-exact"]
refs: ["attack-plans/AP-20260525T184428-Q2-rational-interval.json", "wiki/notes/frontier-q2-endpoint.md"]
---

# Theorem: deterministic rational interval certificate on J for R Lambda G Q2 proves terminal endpoint

## Statement

Let \(J=[287345/1000000,287346/1000000]\). There is a deterministic rational interval-arithmetic certificate, using the true atanh logarithm-enclosure lemma and the true Hurwitz-zeta integral-tail enclosure lemma, that gives certified rational enclosures for \(R(x)\), \(\Lambda(x)\), \(G(x)\), and \(Q_2(x)\) on the needed subdivisions of \(J\), proves \(G(287345/1000000)>0>G(287346/1000000)\), gives a rational lower witness \(q_J<Q_2(\xi)\) for the unique zero \(\xi\in J\), and combines with certified complement upper intervals to determine \(L_2=Q_2(\xi)\) and \(\mathcal I_2=(Q_2(\xi),3]\).

## Dependencies

- [[wiki/nodes/T-Q2-terminal-exact|determine exact I_2 via certified L_2 description]]

## Proof and provenance references

- `attack-plans/AP-20260525T184428-Q2-rational-interval.json`
- `wiki/notes/frontier-q2-endpoint.md`

## Tags

`attack-plan`, `microinterval`, `open`, `rational-interval-arithmetic`, `terminal-route`, `theorem`, `wide`
