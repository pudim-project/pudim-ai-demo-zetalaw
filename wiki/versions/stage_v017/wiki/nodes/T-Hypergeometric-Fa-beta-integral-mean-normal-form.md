---
id: "T-Hypergeometric-Fa-beta-integral-mean-normal-form"
type: "theorem"
title: "Euler beta integral positive-kernel normal form for hypergeometric F_a(r)"
status: "proved"
tags: ["attack-plan", "beta-integral", "hypergeometric", "positive-kernel", "proved", "theorem", "wide"]
parents: ["T-positive-Laplace-kernel-complete-monotonicity-principle"]
refs: ["private attack plan", "private librarian audit", "private librarian audit", "private proof note", "wiki/notes/frontier-baricz-hypergeometric-means.md"]
---

# Theorem: Euler beta integral positive-kernel normal form for hypergeometric F_a(r)

## Statement

For \(0<a<c\) and \(0<r<1\), \(F_a(r)={}_2F_1(a,c-a;c;r)\) has the Euler beta-integral normal form \(F_a(r)=\frac{\Gamma(c)}{\Gamma(a)\Gamma(c-a)}\int_0^1 t^{a-1}(1-t)^{c-a-1}(1-rt)^{a-c}\,dt\).

## Dependencies

- [[wiki/nodes/T-positive-Laplace-kernel-complete-monotonicity-principle|T-positive-Laplace-kernel-complete-monotonicity-principle]]

## Proof and provenance references

- `private attack plan`
- `private librarian audit`
- `private librarian audit`
- `private proof note`
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

_Proof source: `private proof note`._

## Tags

`attack-plan`, `beta-integral`, `hypergeometric`, `positive-kernel`, `proved`, `theorem`, `wide`
