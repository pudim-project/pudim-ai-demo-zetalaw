---
id: "T-CM-Laplace-moment-ratio-monotonicity"
type: "theorem"
title: "positive Laplace tilted moments imply strict monotonicity of a_{n+1}/(a_n a_{n+2})"
status: "proved"
tags: ["bridge-layer", "complete-monotonicity", "laplace-moments", "moment-log-convexity", "proved", "student", "theorem"]
parents: ["T-positive-Laplace-kernel-complete-monotonicity-principle", "D-Laplace-kernel-and-tilted-moment-language"]
refs: ["attack-plans/AP-20260526T140000-Nielsen-k-beta.json", "raw/student/20260526T140500-nielsen-k-beta-moment-ratio.md", "wiki/notes/frontier-nielsen-k-beta-moment-ratio.md"]
---

# Theorem: positive Laplace tilted moments imply strict monotonicity of a_{n+1}/(a_n a_{n+2})

## Statement

Let \(a_j(x)=\int_0^\infty t^j e^{-xt}\,d\mu(t)>0\) be tilted moments of a positive Laplace measure for the needed indices. Then, for every \(n\ge0\), \(B_n(x)=a_{n+1}(x)/(a_n(x)a_{n+2}(x))\) is strictly increasing on its domain.

## Dependencies

- [[wiki/nodes/T-positive-Laplace-kernel-complete-monotonicity-principle|T-positive-Laplace-kernel-complete-monotonicity-principle]]
- [[wiki/nodes/D-Laplace-kernel-and-tilted-moment-language|Laplace kernels and tilted moment ratios]]

## Proof and provenance references

- `attack-plans/AP-20260526T140000-Nielsen-k-beta.json`
- `raw/student/20260526T140500-nielsen-k-beta-moment-ratio.md`
- `wiki/notes/frontier-nielsen-k-beta-moment-ratio.md`

## Proof

Let \(\mu\) be a positive Borel measure on \([0,\infty)\) with finite moments after the tilt \(e^{-xt}\). Define
\[
a_j(x)=\int_0^\infty t^j e^{-xt}\,d\mu(t)>0
\]
for the needed indices. For fixed \(n\ge0\), set
\[
B_n(x)=\frac{a_{n+1}(x)}{a_n(x)a_{n+2}(x)}.
\]
Then \(B_n\) is strictly increasing whenever \(a_{n+1}(x)>0\).

Indeed \(a_j'(x)=-a_{j+1}(x)\). Put
\[
r_j(x)=\frac{a_{j+1}(x)}{a_j(x)}.
\]
Moment log-convexity, equivalently Cauchy--Schwarz applied to
\[
\int t^j e^{-xt}\,d\mu(t),
\]
gives \(r_{j+1}(x)\ge r_j(x)\). Differentiating,
\[
\frac{d}{dx}\log B_n(x)
=-\frac{a_{n+2}}{a_{n+1}}
+\frac{a_{n+1}}{a_n}
+\frac{a_{n+3}}{a_{n+2}}
=r_n(x)-r_{n+1}(x)+r_{n+2}(x).
\]
Since \(r_{n+2}(x)\ge r_{n+1}(x)\) and \(r_n(x)>0\), the logarithmic derivative is positive. Hence \(B_n\) is strictly increasing.

Let
\[
f_k(x)=x\beta_k(x).
\]
From the integral representation of \(\beta_k\), integration by parts gives
\[
f_k(x)
=x\int_0^\infty e^{-xt}\frac{dt}{1+e^{-kt}}
=\frac12+\int_0^\infty e^{-xt}\frac{k e^{-kt}}{(1+e^{-kt})^2}\,dt.
\]
Thus \(f_k\) is the Laplace transform of a positive measure consisting of an atom \(1/2\) at \(0\) plus the positive density
\[
w_k(t)=\frac{k e^{-kt}}{(1+e^{-kt})^2}
\]
on \((0,\infty)\). All tilted moments are finite, and \(a_{j}(x)>0\) for \(j\ge1\).

For \(a_j(x)=(-1)^j f_k^{(j)}(x)\), the bridge lemma gives that
\[
B_{k,n}(x)=\frac{a_{n+1}(x)}{a_n(x)a_{n+2}(x)}
\]
is strictly increasing for every \(k>0\), \(n\ge0\), and \(x>0\). Since
\[
R_{k,n}(x)=(-1)^{n+1}B_{k,n}(x),
\]
we get the precise monotonicity law:

if \(n\) is odd, \(R_{k,n}\) is strictly increasing on \((0,\infty)\);
if \(n\) is even, \(R_{k,n}\) is strictly decreasing on \((0,\infty)\).

This solves the Yin--Zhang Nielsen \(k\)-beta derivative-ratio open problem in the parity-refined form.

_Proof source: `raw/student/20260526T140500-nielsen-k-beta-moment-ratio.md`._

## Tags

`bridge-layer`, `complete-monotonicity`, `laplace-moments`, `moment-log-convexity`, `proved`, `student`, `theorem`
