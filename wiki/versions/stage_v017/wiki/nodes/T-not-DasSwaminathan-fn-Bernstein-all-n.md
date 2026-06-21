---
id: "T-not-DasSwaminathan-fn-Bernstein-all-n"
type: "theorem"
title: "Das Swaminathan multiple gamma f_n Bernstein question negative answer f4 negative near zero"
status: "proved"
tags: ["app-candidate", "bernstein-function", "multiple-gamma", "negative-answer", "primitive-growth", "proved", "source-open-solved", "theorem", "true"]
parents: ["T-Das2020-logGn-derivative-positivity-source-import", "T-DasSwaminathan-logGn-unit-sign", "T-Pointwise-obstruction-certificate-principle"]
refs: ["private librarian audit", "private Oracle response", "private proof note", "wiki/notes/frontier-das-swaminathan-multiple-gamma-pick-stieltjes.md"]
---

# Theorem: Das Swaminathan multiple gamma f_n Bernstein question negative answer f4 negative near zero

## Statement

The Das-Swaminathan source question asking whether \(f_n(x)=\log G_n(x+1)/(x^n\log x)\) is a Bernstein function has a negative answer: \(f_4(x)<0\) for all sufficiently small \(x>0\), so \(f_4\) is not Bernstein.

## Dependencies

- [[wiki/nodes/T-Das2020-logGn-derivative-positivity-source-import|Das 2020 multiple gamma log derivative positivity F_n n plus one derivative positive]]
- [[wiki/nodes/T-DasSwaminathan-logGn-unit-sign|Das Swaminathan Barnes multiple gamma log G_n unit interval sign derivative at one sign]]
- [[wiki/nodes/T-Pointwise-obstruction-certificate-principle|T-Pointwise-obstruction-certificate-principle]]

## Proof and provenance references

- `private librarian audit`
- `private Oracle response`
- `private proof note`
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

_Proof source: `private proof note`._

## Tags

`app-candidate`, `bernstein-function`, `multiple-gamma`, `negative-answer`, `primitive-growth`, `proved`, `source-open-solved`, `theorem`, `true`
