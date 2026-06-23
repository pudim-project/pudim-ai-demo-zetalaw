---
id: "T-Gini-diagonal-expansion"
type: "theorem"
title: "Gini mean diagonal expansion second order coefficient a plus b minus one over eight u"
status: "proved"
tags: ["bridge-patch", "diagonal-expansion", "gamma-quotient", "gini-mean", "proved", "theorem"]
parents: ["T-endpoint-log-derivative-monotonicity-principle"]
refs: ["librarian/audits/LA-20260530T-elegance-029-ab-reciprocal-gate.json", "raw/student/20260530T-elegance-029-ab-reciprocal-gini-gate.md", "wiki/definitions/gini-mean-and-ab-gamma-quotient.md", "wiki/notes/frontier-ab-reciprocal-gini-gamma-quotient.md"]
---

# Theorem: Gini mean diagonal expansion second order coefficient a plus b minus one over eight u

## Statement

For the Gini mean, as \(h\downarrow0\), \(G_{a,b}(u,u+h)=u+h/2+(a+b-1)h^2/(8u)+O(h^3)\), with the case \(a=b\) understood by continuity.

## Dependencies

- [[wiki/nodes/T-endpoint-log-derivative-monotonicity-principle|T-endpoint-log-derivative-monotonicity-principle]]

## Proof and provenance references

- `librarian/audits/LA-20260530T-elegance-029-ab-reciprocal-gate.json`
- `raw/student/20260530T-elegance-029-ab-reciprocal-gini-gate.md`
- `wiki/definitions/gini-mean-and-ab-gamma-quotient.md`
- `wiki/notes/frontier-ab-reciprocal-gini-gamma-quotient.md`

## Proof

For \(a,b\in\mathbb R\), the two-variable Gini mean is
\[
G_{a,b}(u,v)=
\left(\frac{u^a+v^a}{u^b+v^b}\right)^{1/(a-b)}
\qquad (a\ne b),
\]
with the diagonal parameter case \(a=b\) defined by continuity:
\[
G_{a,a}(u,v)
=\exp\left(
\frac{u^a\log u+v^a\log v}{u^a+v^a}
\right).
\]

Alzer--Berg define
\[
P_{a,b}(u,v;x)
=\frac{\Gamma(x+u)}{\Gamma(x+v)}
\exp\{(v-u)\psi(x+G_{a,b}(u,v))\},
\]
for \(v>u>0\). They determine the parameters for complete monotonicity of \(P_{a,b}\) and leave the reciprocal complete-monotonicity problem for \(1/P_{a,b}\) open.

_Proof source: `wiki/definitions/gini-mean-and-ab-gamma-quotient.md`._

## Tags

`bridge-patch`, `diagonal-expansion`, `gamma-quotient`, `gini-mean`, `proved`, `theorem`
