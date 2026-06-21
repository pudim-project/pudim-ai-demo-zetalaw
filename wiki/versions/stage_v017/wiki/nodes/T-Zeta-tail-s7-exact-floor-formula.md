---
id: "T-Zeta-tail-s7-exact-floor-formula"
type: "theorem"
title: "T-Zeta-tail-s7-exact-floor-formula"
status: "proved"
tags: ["application-bridge", "inverse-tail-floor", "proved", "source-open-solved", "telescoping-certificate", "theorem", "zeta-tail"]
parents: ["D-Tail-zeta-partition-function", "T-Zeta-tail-inverse-asymptotic-telescoping-template"]
refs: ["private proof note", "theory/latest/THEORY.tex#thm:tail-s7-floor"]
---

# Theorem: T-Zeta-tail-s7-exact-floor-formula

## Statement

For \(T_7(n)=\zeta_n(7)=\sum_{k=n}^\infty k^{-7}\), with \(Q(n)=120n^6-360n^5+660n^4-720n^3+354n^2-54n+375\) and \(P(n)=Q(n)/20\), one has \(\lfloor T_7(n)^{-1}\rfloor=\lfloor P(n)\rfloor\) for every \(n\ge28\), with the finite table in the staged APP-0005 theorem for \(1\le n\le27\).

## Dependencies

- [[wiki/nodes/D-Tail-zeta-partition-function|Tail zeta partition function]]
- [[wiki/nodes/T-Zeta-tail-inverse-asymptotic-telescoping-template|reusable Euler Maclaurin inverse-tail approximant plus telescoping sign certificate template]]

## Proof and provenance references

- `private proof note`
- `theory/latest/THEORY.tex#thm:tail-s7-floor`

## Proof

The proof instantiates the inverse-tail asymptotic telescoping template with \(s=7\), the partition function \(T_7\), and the specific approximation data \(Q,P\).  The template gives rational upper and lower reciprocal envelopes \(L_n\le T_7(n)^{-1}\le U_n\) with \(U_n-L_n<1\); by direct computation \(\lfloor L_n\rfloor=\lfloor U_n\rfloor=P(n)\) for \(n\ge28\).  The finite checked range \(1\le n\le27\) is recorded explicitly in the same staged source, so the floor identity holds for all \(n\ge1\).

_Proof source: `private proof note`._

## Tags

`application-bridge`, `inverse-tail-floor`, `proved`, `source-open-solved`, `telescoping-certificate`, `theorem`, `zeta-tail`
