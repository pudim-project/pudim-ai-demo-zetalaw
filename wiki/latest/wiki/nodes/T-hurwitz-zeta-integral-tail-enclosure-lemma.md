---
id: "T-hurwitz-zeta-integral-tail-enclosure-lemma"
type: "theorem"
title: "integral tail bounds give exact rational Hurwitz zeta enclosures for rational a"
status: "proved"
tags: ["hurwitz-zeta", "interval-arithmetic", "proved", "student", "theorem", "true-helper"]
parents: ["T-Complete-monotonicity-closure-calculus-principle"]
refs: ["raw/student/20260525T183817-q2-atanh-microinterval-roll.md"]
---

# Theorem: integral tail bounds give exact rational Hurwitz zeta enclosures for rational a

## Statement

For rational \(a>0\), integer \(s>1\), and integer \(N\ge1\), if \(S_N=\sum_{k=0}^{N-1}(a+k)^{-s}\), then \(S_N+(a+N)^{1-s}/(s-1)\le Z_s(a)\le S_N+(a+N-1)^{1-s}/(s-1)\). Thus \(Z_s(a)\) has exact rational upper and lower enclosures.

## Dependencies

- [[wiki/nodes/T-Complete-monotonicity-closure-calculus-principle|Complete-monotonicity closure calculus principle]]

## Proof and provenance references

- `raw/student/20260525T183817-q2-atanh-microinterval-roll.md`

## Proof

The following reusable lemma is proved locally.

Let \(a>0\), \(s>1\), and \(N\ge1\), with \(a\) rational and \(s,N\) integers. Define
\[
S_N=\sum_{k=0}^{N-1}(a+k)^{-s}.
\]
Since \(t\mapsto(a+t)^{-s}\) is positive and decreasing on \([0,\infty)\),
\[
\int_N^\infty (a+t)^{-s}\,dt
\le
\sum_{k=N}^{\infty}(a+k)^{-s}
\le
\int_{N-1}^{\infty}(a+t)^{-s}\,dt.
\]
Therefore
\[
S_N+\frac{(a+N)^{1-s}}{s-1}
\le
Z_s(a)
\le
S_N+\frac{(a+N-1)^{1-s}}{s-1}.
\]

For rational \(a\), both endpoints are rational. This proves an exact rational enclosure method for \(Z_s(a)\), covering the \(s=3,4,5\) Hurwitz-zeta terms needed by \(R\), \(\Lambda\), \(G\), and \(Q_2\).

This proves the claim.

The atanh logarithm helper and the Hurwitz-zeta integral-tail helper reduce the ingredients to exact rational intervals at rational points. The missing terminal work is still the nonlinear interval propagation:

certify the signs of \(G\) at the microinterval endpoints with intervals narrower than the right-endpoint margin;
prove a one-zero pattern on the compact bracket outside \(J\);
produce a finite outside-bracket upper cover for \(Q_2\) below an inner certified lower witness.

_Proof source: `raw/student/20260525T183817-q2-atanh-microinterval-roll.md`._

## Tags

`hurwitz-zeta`, `interval-arithmetic`, `proved`, `student`, `theorem`, `true-helper`
