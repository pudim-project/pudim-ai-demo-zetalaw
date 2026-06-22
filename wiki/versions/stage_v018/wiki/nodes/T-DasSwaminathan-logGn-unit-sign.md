---
id: "T-DasSwaminathan-logGn-unit-sign"
type: "theorem"
title: "Das Swaminathan Barnes multiple gamma log G_n unit interval sign derivative at one sign"
status: "proved"
tags: ["divided-difference", "multiple-gamma", "primitive-growth", "proved", "sign-certificate", "theorem", "true"]
parents: ["T-Das2020-logGn-derivative-positivity-source-import", "T-Special-function-normal-form-calculus-principle"]
refs: ["librarian/audits/LA-20260612T1650-das-swaminathan-bernstein-negative-answer.json", "oracle/responses/OS-20260612T1625Z-das-swaminathan-multiple-gamma-pick-stieltjes-oracle-response.md", "raw/student/20260612T1645-das-swaminathan-bernstein-negative-answer.md", "wiki/notes/frontier-das-swaminathan-multiple-gamma-pick-stieltjes.md"]
---

# Theorem: Das Swaminathan Barnes multiple gamma log G_n unit interval sign derivative at one sign

## Statement

For the Barnes multiple-gamma functions \(G_n\), if \(F_n(x)=\log G_n(x)\), then \((-1)^{n+1}F_n(x)>0\) for \(0<x<1\) and \(\operatorname{sgn}F_n'(1)=(-1)^n\).

## Dependencies

- [[wiki/nodes/T-Das2020-logGn-derivative-positivity-source-import|Das 2020 multiple gamma log derivative positivity F_n n plus one derivative positive]]
- [[wiki/nodes/T-Special-function-normal-form-calculus-principle|Special-function normal-form calculus principle]]

## Proof and provenance references

- `librarian/audits/LA-20260612T1650-das-swaminathan-bernstein-negative-answer.json`
- `oracle/responses/OS-20260612T1625Z-das-swaminathan-multiple-gamma-pick-stieltjes-oracle-response.md`
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

`divided-difference`, `multiple-gamma`, `primitive-growth`, `proved`, `sign-certificate`, `theorem`, `true`
