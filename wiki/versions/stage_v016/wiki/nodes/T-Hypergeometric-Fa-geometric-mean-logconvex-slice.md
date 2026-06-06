---
id: "T-Hypergeometric-Fa-geometric-mean-logconvex-slice"
type: "theorem"
title: "bounded hypergeometric F_a geometric/arithmetic mean slice for c<=1"
status: "proved"
tags: ["attack-plan", "hypergeometric", "log-convexity", "means", "proved", "stronger", "theorem"]
parents: ["T-Convex-duality-curvature-principle"]
refs: ["attack-plans/AP-20260528T124000-baricz-hypergeometric-means.json", "librarian/audits/LA-20260528T124000-baricz-hypergeometric-attack-plan.json", "librarian/audits/LA-20260528T125000-baricz-hypergeometric-student.json", "raw/scout/sources/baricz-turan-type-inequalities.txt", "raw/student/20260528T124500-baricz-hypergeometric-means.md", "wiki/notes/frontier-baricz-hypergeometric-means.md"]
---

# Theorem: bounded hypergeometric F_a geometric/arithmetic mean slice for c<=1

## Statement

For \(0<c\le1\), \(a_1,a_2\in(0,c)\), and \(r\in(0,1)\), Baricz's concavity theorem gives \(\sqrt{F_{a_1}(r)F_{a_2}(r)}\le (F_{a_1}(r)+F_{a_2}(r))/2\le F_{(a_1+a_2)/2}(r)\).

## Dependencies

- [[wiki/nodes/T-Convex-duality-curvature-principle|Convex duality and curvature principle]]

## Proof and provenance references

- `attack-plans/AP-20260528T124000-baricz-hypergeometric-means.json`
- `librarian/audits/LA-20260528T124000-baricz-hypergeometric-attack-plan.json`
- `librarian/audits/LA-20260528T125000-baricz-hypergeometric-student.json`
- `raw/scout/sources/baricz-turan-type-inequalities.txt`
- `raw/student/20260528T124500-baricz-hypergeometric-means.md`
- `wiki/notes/frontier-baricz-hypergeometric-means.md`

## Proof

For \(0<a<c\) and \(0<r<1\), Euler's integral for the Gauss hypergeometric function gives
\[
{}_2F_1(A,B;C;r)
=
\frac{\Gamma(C)}{\Gamma(B)\Gamma(C-B)}
\int_0^1
t^{B-1}(1-t)^{the B 1}(1-rt)^{-A}\,dt
\]
when \(C>B>0\).

With \(A=a\), \(B=c-a\), and \(C=c\), this becomes
\[
F_a(r)
=
\frac{\Gamma(c)}{\Gamma(c-a)\Gamma(a)}
\int_0^1
t^{c-a-1}(1-t)^{a-1}(1-rt)^{-a}\,dt.
\]
Equivalently,
\[
F_a(r)
=
\mathbb E_{T\sim\mathrm{Beta}(c-a,a)}
\left[(1-rT)^{-a}\right].
\]

This is a positive-kernel bridge into the local Gamma/Beta and moment-ratio layer, but the \(a\)-dependence appears both in the beta law and in the integrand, so it does not immediately solve the full Baricz classification.

From Baricz's strict concavity theorem for \(0<a<c\le1\), the arithmetic/geometric mean slice follows:
\[
G(F_{a_1}(r),F_{a_2}(r))
\le
F_{A(a_1,a_2)}(r),
\]
where
\[
G(x,y)=\sqrt{xy},
\qquad
A(x,y)=\frac{x+y}{2}.
\]

This is a nontrivial instance of the Baricz template with \(m_1=G\), \(m_2=A\), direction \(\le\), and parameter range
\[
0<a_1,a_2<c\le1,\qquad 0<r<1.
\]

The broad classification node remains open.

_Proof source: `raw/student/20260528T124500-baricz-hypergeometric-means.md`._

## Tags

`attack-plan`, `hypergeometric`, `log-convexity`, `means`, `proved`, `stronger`, `theorem`
