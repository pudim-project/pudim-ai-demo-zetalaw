---
id: "T-Gamma-rational-envelope-supremum-bridge"
type: "theorem"
title: "Gamma rational upper parameter equals sup H with strict-bound infimum convention"
status: "proved"
tags: ["attack-plan", "bridge-layer", "gamma-function", "proved", "proved-bridge", "rational-envelope", "student", "theorem"]
parents: ["T-Special-function-normal-form-calculus-principle", "T-Gamma-rational-p1-unique-critical-certificate"]
refs: ["private librarian audit", "private proof note", "wiki/notes/frontier-gamma-rational-p1.md"]
---

# Theorem: Gamma rational upper parameter equals sup H with strict-bound infimum convention

## Statement

For \(0<x<1\), define \(H(x)=x(\Gamma(1+x)-x)/(1-\Gamma(1+x))\). The Yang--Qian--Chu--Zhang upper-parameter problem is equivalent to certifying \(p_1^*=\sup_{0<x<1}H(x)\), with strict upper bounds holding for every \(p>p_1^*\) and failing for every \(p<p_1^*\).

## Dependencies

- [[wiki/nodes/T-Special-function-normal-form-calculus-principle|Special-function normal-form calculus principle]]
- [[wiki/nodes/T-Gamma-rational-p1-unique-critical-certificate|H has unique global maximizer xi and p1 star equals H(xi)]]

## Proof and provenance references

- `private librarian audit`
- `private proof note`
- `wiki/notes/frontier-gamma-rational-p1.md`

## Proof

First, \(0<\Gamma(1+x)<1\) on \(0<x<1\). Positivity is standard. For the upper bound, \(\log\Gamma\) is strictly convex on \((0,\infty)\), and
\[
\log\Gamma(1)=\log\Gamma(2)=0.
\]
Strict convexity therefore gives
\[
\log\Gamma(1+x)<(1-x)\log\Gamma(1)+x\log\Gamma(2)=0
\]
for \(0<x<1\), hence \(\Gamma(1+x)<1\).

For fixed \(x\in(0,1)\), put
\[
R_p(x)=\frac{x^2+p}{x+p}.
\]
Then
\[
\frac{\partial R_p(x)}{\partial p}
=\frac{x-x^2}{(x+p)^2}>0
\]
for \(p>0\), so the envelope is strictly increasing in the parameter.

Solving the pointwise inequality gives
\[
\Gamma(1+x)<\frac{x^2+p}{x+p}
\]
if and only if
\[
x\Gamma(1+x)+p\Gamma(1+x)<x^2+p.
\]
Equivalently,
\[
p(\Gamma(1+x)-1)<x^2-x\Gamma(1+x).
\]
Since \(\Gamma(1+x)-1<0\), division reverses the inequality and gives
\[
p>\frac{x(\Gamma(1+x)-x)}{1-\Gamma(1+x)}=H(x).
\]

Thus a single \(p\) works for every \(x\in(0,1)\) exactly when \(p>H(x)\) for every \(x\). This proves that every \(p>\sup H\) works, and every \(p<\sup H\) fails by the definition of supremum. The endpoint convention for \(p=\sup H\) follows directly: if a maximizer exists, the pointwise inequality becomes equality there, so the source's strict upper inequality fails at that parameter. The infimal upper parameter is nevertheless \(\sup H\).

This proves the Gamma rational envelope supremum bridge.

Let \(y=\Gamma(1+x)\). Differentiating
\[
H(x)=\frac{x(y-x)}{1-y}
\]
gives
\[
H'(x)=\frac{F(x)}{(1-y)^2},
\]
where
\[
F(x)=(y-2x)(1-y)+x(1-x)y\psi(1+x).
\]

High-precision numerical first contact gives a single apparent zero
\[
\xi\approx0.1927776581313346099476289523248920004
\]
and
\[
H(\xi)\approx1.7552752098189566314896646434355937518.
\]
The endpoint values are consistent with an interior maximum:
\[
\lim_{x\to0^+}H(x)=\frac1\gamma\approx1.7324547146,
\qquad
\lim_{x\to1^-}H(x)=\frac{\gamma}{1-\gamma}\approx1.3652721186.
\]

The quick proof route is to certify one sign change of \(F\). A direct monotonicity argument was not immediate: \(F\) mixes the terms \((y-2x)(1-y)\) and \(x(1-x)y\psi(1+x)\), and their signs do not align globally. A rigorous proof looks feasible by log-Gamma Taylor enclosures plus interval arithmetic, but it would require a fresh global certificate rather than a short extension of the bridge proof.

_Proof source: `private proof note`._

## Tags

`attack-plan`, `bridge-layer`, `gamma-function`, `proved`, `proved-bridge`, `rational-envelope`, `student`, `theorem`
