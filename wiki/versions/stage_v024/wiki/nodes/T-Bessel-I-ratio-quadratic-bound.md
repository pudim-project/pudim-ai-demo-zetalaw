---
id: "T-Bessel-I-ratio-quadratic-bound"
type: "theorem"
title: "forall nu >= 0, u > 0, q^2+(2nu+1)q/u+(nu+1/2)/u^2 > 1 for q=I_{nu+1}/I_nu"
status: "open"
tags: ["attack-plan", "bessel", "open", "ratio-bound", "stronger", "theorem", "turan"]
parents: ["T-Bessel-I-sqrt-log-concavity-nu-ge-0"]
refs: ["attack-plans/AP-20260526T123243-Bessel-I-log-concavity.json", "librarian/audits/LA-20260526T123243-attack-plan.json", "wiki/notes/frontier-bessel-i-log-concavity.md"]
---

# Theorem: forall nu >= 0, u > 0, q^2+(2nu+1)q/u+(nu+1/2)/u^2 > 1 for q=I_{nu+1}/I_nu

## Statement

Let \(q_\nu(u)=I_{\nu+1}(u)/I_\nu(u)\). For every \(\nu\ge0\) and \(u>0\), \(q_\nu(u)^2+(2\nu+1)q_\nu(u)/u+(\nu+1/2)/u^2>1\).

## Dependencies

- [[wiki/nodes/T-Bessel-I-sqrt-log-concavity-nu-ge-0|forall nu >= 0, u -> sqrt(u) I_nu(u) strictly log-concave on (0,infty)]]

## Proof and provenance references

- `attack-plans/AP-20260526T123243-Bessel-I-log-concavity.json`
- `librarian/audits/LA-20260526T123243-attack-plan.json`
- `wiki/notes/frontier-bessel-i-log-concavity.md`

## Tags

`attack-plan`, `bessel`, `open`, `ratio-bound`, `stronger`, `theorem`, `turan`
