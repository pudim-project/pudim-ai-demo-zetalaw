---
id: "T-Bessel-I-Riccati-log-concavity-inequality"
type: "theorem"
title: "forall nu >= 0, u > 0, 1+(nu^2-1/2)/u^2-r/u-r^2 < 0 for r=I_nu'/I_nu"
status: "open"
tags: ["attack-plan", "bessel", "log-concavity", "open", "riccati", "theorem", "wide"]
parents: ["T-Bessel-I-sqrt-log-concavity-nu-ge-0", "T-not-Bessel-I-Riccati-log-concavity-inequality"]
refs: ["attack-plans/AP-20260526T123243-Bessel-I-log-concavity.json", "librarian/audits/LA-20260526T123243-attack-plan.json", "wiki/notes/frontier-bessel-i-log-concavity.md"]
---

# Theorem: forall nu >= 0, u > 0, 1+(nu^2-1/2)/u^2-r/u-r^2 < 0 for r=I_nu'/I_nu

## Statement

Let \(r_\nu(u)=I_\nu'(u)/I_\nu(u)\). For every \(\nu\ge0\) and \(u>0\), \(1+(\nu^2-1/2)/u^2-r_\nu(u)/u-r_\nu(u)^2<0\).

## Dependencies

- [[wiki/nodes/T-Bessel-I-sqrt-log-concavity-nu-ge-0|forall nu >= 0, u -> sqrt(u) I_nu(u) strictly log-concave on (0,infty)]]
- [[wiki/nodes/T-not-Bessel-I-Riccati-log-concavity-inequality|exists nu >= 0 and u > 0 such that Riccati log-concavity expression is nonnegative]]

## Proof and provenance references

- `attack-plans/AP-20260526T123243-Bessel-I-log-concavity.json`
- `librarian/audits/LA-20260526T123243-attack-plan.json`
- `wiki/notes/frontier-bessel-i-log-concavity.md`

## Tags

`attack-plan`, `bessel`, `log-concavity`, `open`, `riccati`, `theorem`, `wide`
