---
id: "C-PD-Copulas-AllDimensions-Lambda-LeMinusOne"
type: "corollary"
title: "Pearse-Bondell PD copulas in all dimensions for lambda <= -1"
status: "proved"
tags: ["app-0092", "archimedean-copula", "corollary", "proved", "source-consequence", "true"]
parents: ["T-PD-Inverse-Complete-Monotonicity-All-Lambda-LeMinusOne"]
refs: ["oracle/responses/OFC-20260623T0410-pd-copula-first-contact-oracle-first-contact-response.md", "raw/student/20260623T0428-pd-copula-inverse-cm.md"]
---

# Corollary: Pearse-Bondell PD copulas in all dimensions for lambda <= -1

## Statement

Using the Archimedean complete-monotonicity criterion cited by Pearse--Bondell, the power-divergence copulas with \(\lambda\le -1\) are valid in all dimensions because \(\phi_\lambda^{-1}\) is completely monotone on \((0,\infty)\).

## Dependencies

- [[wiki/nodes/T-PD-Inverse-Complete-Monotonicity-All-Lambda-LeMinusOne|Pearse-Bondell inverse complete monotonicity for all lambda <= -1]]

## Proof and provenance references

- `oracle/responses/OFC-20260623T0410-pd-copula-first-contact-oracle-first-contact-response.md`
- `raw/student/20260623T0428-pd-copula-inverse-cm.md`

## Proof

Write \(\lambda=-\gamma\) with \(\gamma\ge1\). The source formula gives, for \(\gamma>1\),
\[
\phi_{-\gamma}(x)=\frac{x^{1-\gamma}+(\gamma-1)x-\gamma}{\gamma(\gamma-1)},\qquad 0<x\le1,
\]
and for \(\gamma=1\),
\[
\phi_{-1}(x)=x-1-\log x.
\]
In both cases,
\[
\phi_{-\gamma}'(x)=\frac{1-x^{-\gamma}}{\gamma}
=-\frac{1-x^\gamma}{\gamma x^\gamma}<0,\qquad 0<x<1.
\]
Moreover \(\phi_{-\gamma}(1)=0\) and \(\phi_{-\gamma}(0+)=+\infty\), so \(u(t)=\phi_{-\gamma}^{-1}(t)\) is a strict \(C^\infty\) inverse from \((0,\infty)\) to \((0,1)\). By the inverse-function theorem,
\[
u'(t)=-\frac{\gamma u(t)^\gamma}{1-u(t)^\gamma}.
\]
Set
\[
H_\gamma(x)=\frac{\gamma x^\gamma}{1-x^\gamma}
=\gamma\sum_{m\ge1}x^{m\gamma},\qquad 0<x<1,
\]
and define \(L_\gamma=H_\gamma(x)\frac{d}{dx}\). For any smooth \(F\),
\[
\frac{d}{dt}F(u(t))=-\bigl(L_\gamma F\bigr)(u(t)).
\]
Let \(P_0(x)=x\) and \(P_{n+1}=L_\gamma P_n\). Then induction gives
\[
(-1)^n u^{(n)}(t)=P_n(u(t)).
\]

It remains to prove \(P_n(x)>0\) on \((0,1)\). For \(n\ge1\), repeated expansion gives
\[
P_n(x)=\gamma^n\sum_{m_1,\ldots,m_n\ge1}
\left(\prod_{j=0}^{n-1}\beta_j\right)x^{\beta_n},
\qquad
\beta_j=1-j+\gamma(m_1+\cdots+m_j),\quad \beta_0=1.
\]
Since \(\gamma\ge1\) and \(m_i\ge1\),
\[
\beta_j\ge1-j+\gamma j=1+j(\gamma-1)>0.
\]
Thus every coefficient and every exponent in the displayed generalized power series is positive. For each compact interval \(0<x\le r<1\), the coefficient factor grows polynomially in \(m_1+\cdots+m_n\), while \(r^{\gamma(m_1+\cdots+m_n)}\) gives geometric decay. Hence the series converges locally uniformly and is strictly positive on \((0,1)\).

Therefore \(P_n(u(t))>0\) for every \(n\ge0\) and \(t>0\), so
\[
(-1)^n u^{(n)}(t)>0,\qquad n\ge0,\ t>0.
\]
This proves that \(\phi_\lambda^{-1}\) is strictly completely monotone on \((0,\infty)\) for every \(\lambda\le-1\). Since \(u(t)\uparrow1\) as \(t\downarrow0\), the inverse extends continuously to \(u(0)=1\). Its derivative may diverge at \(0\), but the source's complete-monotonicity convention is the standard interior condition.

_Proof source: `raw/student/20260623T0428-pd-copula-inverse-cm.md`._

## Tags

`app-0092`, `archimedean-copula`, `corollary`, `proved`, `source-consequence`, `true`
