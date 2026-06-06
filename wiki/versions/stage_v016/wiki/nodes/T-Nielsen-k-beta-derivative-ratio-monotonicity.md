---
id: "T-Nielsen-k-beta-derivative-ratio-monotonicity"
type: "theorem"
title: "Nielsen k-beta derivative ratio has parity monotonicity: odd n increasing, even n decreasing"
status: "proved"
tags: ["app-0010", "bridge-patch", "complete-monotonicity", "nielsen-k-beta", "proved", "student", "theorem"]
parents: ["T-CM-Laplace-moment-ratio-monotonicity"]
refs: ["raw/scout/FI-20260526T140000Z.md", "raw/scout/RS-FI-20260526T140000Z.json", "raw/student/20260526T140500-nielsen-k-beta-moment-ratio.md", "wiki/notes/app-0010-nielsen-k-beta-moment-ratio.md", "wiki/notes/frontier-nielsen-k-beta-moment-ratio.md"]
---

# Theorem: Nielsen k-beta derivative ratio has parity monotonicity: odd n increasing, even n decreasing

## Statement

For \(k>0\), \(n\ge0\), and \(f_k(x)=x\beta_k(x)\), the ratio \(f_k^{(n+1)}(x)/(f_k^{(n)}(x)f_k^{(n+2)}(x))\) is strictly increasing on \((0,\infty)\) when \(n\) is odd and strictly decreasing on \((0,\infty)\) when \(n\) is even.

## Dependencies

- [[wiki/nodes/T-CM-Laplace-moment-ratio-monotonicity|positive Laplace tilted moments imply strict monotonicity of a_{n+1}/(a_n a_{n+2})]]

## Proof and provenance references

- `raw/scout/FI-20260526T140000Z.md`
- `raw/scout/RS-FI-20260526T140000Z.json`
- `raw/student/20260526T140500-nielsen-k-beta-moment-ratio.md`
- `wiki/notes/app-0010-nielsen-k-beta-moment-ratio.md`
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

`app-0010`, `bridge-patch`, `complete-monotonicity`, `nielsen-k-beta`, `proved`, `student`, `theorem`
