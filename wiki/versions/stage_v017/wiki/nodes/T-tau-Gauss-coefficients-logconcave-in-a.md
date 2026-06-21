---
id: "T-tau-Gauss-coefficients-logconcave-in-a"
type: "theorem"
title: "tau Gauss hypergeometric coefficients log concave in symmetric parameter"
status: "proved"
tags: ["gamma-ratio", "log-concavity", "partial-progress", "proved", "tau-hypergeometric", "theorem", "trigamma"]
parents: ["T-Exact-finite-certificate-verification-principle"]
refs: ["private attack plan", "private librarian audit", "private proof note", "wiki/notes/frontier-bmr-tau-hypergeometric-midpoint.md"]
---

# Theorem: tau Gauss hypergeometric coefficients log concave in symmetric parameter

## Statement

For fixed \(c>0\), \(\tau>0\), and every \(k\ge0\), the coefficient \(A_k(a)\) in \({}_2\phi^\tau_1(a,c-a;c;z)\) is log-concave in \(a\in(0,c)\), strictly for \(k\ge1\).

## Dependencies

- [[wiki/nodes/T-Exact-finite-certificate-verification-principle|Exact finite certificate verification principle]]

## Proof and provenance references

- `private attack plan`
- `private librarian audit`
- `private proof note`
- `wiki/notes/frontier-bmr-tau-hypergeometric-midpoint.md`

## Proof

Write
\[
F(a,z)={}_2\phi^\tau_1(a,c-a;c;z)=\sum_{k=0}^\infty A_k(a)\frac{z^k}{k!},
\]
where
\[
A_k(a)=
\frac{\Gamma(c)}{\Gamma(a)\Gamma(c-a)}
\frac{\Gamma(a+k\tau)\Gamma(c-a+k\tau)}{\Gamma(c+k\tau)}.
\]
For \(k=0\), \(A_0(a)=1\).  For \(k\ge1\), \(A_k(a)>0\) on \((0,c)\).

For \(k\ge0\),
\[
\frac{d^2}{da^2}\log A_k(a)
=
\psi_1(a+k\tau)-\psi_1(a)
+\psi_1(c-a+k\tau)-\psi_1(c-a),
\]
where \(\psi_1=\psi'\) is the trigamma function.

Since
\[
\psi_1(x)=\sum_{m=0}^\infty\frac1{(x+m)^2}
\]
is strictly decreasing on \((0,\infty)\), each difference is nonpositive, and it is strictly negative for \(k\ge1\).  Therefore \(A_k\) is log-concave in \(a\), strictly so for \(k\ge1\).

This is a coefficientwise bridge only; it does not by itself prove that the whole sum is log-concave on \((0,c)\).

The coefficients are symmetric:
\[
A_k(c-a)=A_k(a).
\]
Thus
\[
A_k'(c/2)=0
\]
for every \(k\).  For \(k\ge1\), strict coefficientwise log-concavity gives
\[
A_k''(c/2)=A_k(c/2)(\log A_k)''(c/2)<0.
\]
The series converges absolutely for \(|z|<1\), and the differentiated series is locally uniformly convergent on compact subintervals of \((0,c)\), so termwise differentiation is valid.

For \(0<z<1\),
\[
F'(c/2,z)=\sum_{k=0}^\infty A_k'(c/2)\frac{z^k}{k!}=0,
\]
and
\[
F''(c/2,z)=\sum_{k=1}^\infty A_k''(c/2)\frac{z^k}{k!}<0.
\]
Since \(F(c/2,z)>0\), the second derivative of \(\log F\) at \(a=c/2\) is
\[
(\log F)''(c/2,z)=\frac{F''(c/2,z)}{F(c/2,z)}<0.
\]
Therefore \(a\mapsto {}_2\phi^\tau_1(a,c-a;c;z)\) is strictly locally log-concave at \(a=c/2\) for \(0<z<1\).

_Proof source: `private proof note`._

## Tags

`gamma-ratio`, `log-concavity`, `partial-progress`, `proved`, `tau-hypergeometric`, `theorem`, `trigamma`
