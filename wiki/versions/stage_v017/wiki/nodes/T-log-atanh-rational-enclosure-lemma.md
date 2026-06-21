---
id: "T-log-atanh-rational-enclosure-lemma"
type: "theorem"
title: "atanh series gives exact rational log interval bounds for positive rational r"
status: "proved"
tags: ["interval-arithmetic", "logarithm-control", "proved", "student", "theorem", "true-helper"]
parents: ["T-Complete-monotonicity-closure-calculus-principle"]
refs: ["private proof note"]
---

# Theorem: atanh series gives exact rational log interval bounds for positive rational r

## Statement

For any positive rational interval for \(r\) with a fixed sign of \(r-1\), the identity \(\log r=2\sum_{k=0}^{m}z^{2k+1}/(2k+1)+\epsilon_m\), where \(z=(r-1)/(r+1)\), gives exact rational upper and lower bounds with \(|\epsilon_m|\le2|z|^{2m+3}/((2m+3)(1-z^2))\).

## Dependencies

- [[wiki/nodes/T-Complete-monotonicity-closure-calculus-principle|Complete-monotonicity closure calculus principle]]

## Proof and provenance references

- `private proof note`

## Proof

The outside-bracket candidate remains open. This proof run did not produce a finite rational cover of
\[
(0,1)\setminus\left(\frac{1409}{5000},\frac{293}{1000}\right)
\]
with exact upper enclosures for \(Q_2\) below a certified bracket witness. The true tail gate
\[
L_2\le\frac{404}{173}
\]
remains useful as a strict ceiling, but it is still too coarse to determine the exact endpoint.

The following reusable lemma is proved locally.

Let \(r>0\) be rational and set
\[
z=\frac{r-1}{r+1}.
\]
Then \(|z|<1\) and
\[
\log r
=
2\operatorname{artanh} z
=
2\sum_{k=0}^{m}\frac{z^{2k+1}}{2k+1}
+\epsilon_m.
\]
The tail satisfies
\[
|\epsilon_m|
\le
\frac{2|z|^{2m+3}}{(2m+3)(1-z^2)}.
\]

This gives exact rational upper and lower bounds for \(\log r\), and more generally for \(\log\) over positive rational intervals after bounding \(r\) on the interval and applying monotonicity. The proof is the geometric-tail bound for the absolutely convergent series
\[
\operatorname{artanh}z=\sum_{k=0}^{\infty}\frac{z^{2k+1}}{2k+1}.
\]

This proves the claim.

Build rational Hurwitz-zeta enclosures for \(Z_s(x)\) and \(Z_s(1/x)\) on the tiny root interval
\[
\left[\frac{287345}{1000000},\frac{287346}{1000000}\right],
\]
then apply the exact log lemma to certify the sign of \(G\) at the interval endpoints and begin a finite subdivision proof.

_Proof source: `private proof note`._

## Tags

`interval-arithmetic`, `logarithm-control`, `proved`, `student`, `theorem`, `true-helper`
