---
id: "T-Das2020-logGn-derivative-positivity-source-import"
type: "theorem"
title: "Das 2020 multiple gamma log derivative positivity F_n n plus one derivative positive"
status: "proved"
tags: ["das-2020", "derivative-positivity", "multiple-gamma", "proved", "source-import", "theorem", "true"]
parents: ["T-Special-function-normal-form-calculus-principle"]
refs: ["https://doi.org/10.5802/crmath.115", "librarian/audits/LA-20260612T1650-das-swaminathan-bernstein-negative-answer.json", "raw/student/20260612T1645-das-swaminathan-bernstein-negative-answer.md", "wiki/notes/frontier-das-swaminathan-multiple-gamma-pick-stieltjes.md"]
---

# Theorem: Das 2020 multiple gamma log derivative positivity F_n n plus one derivative positive

## Statement

For the Barnes multiple-gamma convention \(G_n=(\Gamma_n)^{(-1)^{n-1}}\), Das 2020 proves that if \(F_n(x)=\log G_n(x)\), then \(F_n^{(n+1)}(x)>0\) for every \(x>0\).

## Dependencies

- [[wiki/nodes/T-Special-function-normal-form-calculus-principle|Special-function normal-form calculus principle]]

## Proof and provenance references

- `https://doi.org/10.5802/crmath.115`
- `librarian/audits/LA-20260612T1650-das-swaminathan-bernstein-negative-answer.json`
- `raw/student/20260612T1645-das-swaminathan-bernstein-negative-answer.md`
- `wiki/notes/frontier-das-swaminathan-multiple-gamma-pick-stieltjes.md`

## Proof

The value \(G_n(1)=1\) is part of the normalization. For \(k\le n+1\), the recurrence gives
\[
G_n(k+1)=G_n(k)G_{n-1}(k).
\]
Inducting on \(n\), \(G_{n-1}(k)=1\) for \(1\le k\le n\), so all displayed values are \(1\).

Thus \(F_n(j)=0\) for \(j=1,\dots,n+1\).

For \(0<x<1\),
\[
(-1)^{n+1}F_n(x)>0.
\]
Also
\[
\operatorname{sgn} F_n'(1)=(-1)^n.
\]

The divided difference on the nodes \(x,1,2,\dots,n+1\) satisfies
\[
F_n[x,1,2,\dots,n+1]
=\frac{F_n^{(n+1)}(\xi)}{(n+1)!}>0
\]
for some \(\xi\in(x,n+1)\). Since \(F_n(1)=\cdots=F_n(n+1)=0\),
\[
F_n[x,1,2,\dots,n+1]
=\frac{F_n(x)}{\prod_{j=1}^{n+1}(x-j)}.
\]
The product has sign \((-1)^{n+1}\), proving the unit-interval sign.

Letting \(x\to1^-\) gives the repeated-node divided difference
\[
F_n[1,1,2,\dots,n+1]
=\frac{F_n'(1)}{\prod_{j=2}^{n+1}(1-j)}>0.
\]
The product has sign \((-1)^n\), so \(\operatorname{sgn}F_n'(1)=(-1)^n\).

_Proof source: `raw/student/20260612T1645-das-swaminathan-bernstein-negative-answer.md`._

## Tags

`das-2020`, `derivative-positivity`, `multiple-gamma`, `proved`, `source-import`, `theorem`, `true`
