---
id: "T-Bazhlekova-Wright-two-seed-compact-zero-six-positive"
type: "theorem"
title: "Bazhlekova Wright two seed compact zero six positive"
status: "proved"
tags: ["bazhlekova", "compact-certificate", "partial-progress", "proved", "theorem", "wright-function"]
parents: ["T-Exact-finite-certificate-verification-principle"]
refs: ["private librarian audit", "private proof note", "private proof note", "private proof artifact", "wiki/notes/frontier-bazhlekova-square-root-bf-gap.md"]
---

# Theorem: Bazhlekova Wright two seed compact zero six positive

## Statement

For the two no-cover seed Wright functions \(\mathcal W_{3/4,11/10}\) and \(\mathcal W_{11/20,21/20}\), one has \(\mathcal W_{\alpha,p}(x)>0\) on \(0\le x\le6\). This is the first compact block of the larger sign-separated interval certificate, later extended to \([0,10]\).

## Dependencies

- [[wiki/nodes/T-Exact-finite-certificate-verification-principle|Exact finite certificate verification principle]]

## Proof and provenance references

- `private librarian audit`
- `private proof note`
- `private proof note`
- `private proof artifact`
- `wiki/notes/frontier-bazhlekova-square-root-bf-gap.md`

## Proof

For both no-cover seed pairs
\[
(\alpha,p)=\left(\frac34,\frac{11}{10}\right),
\qquad
(\alpha,p)=\left(\frac{11}{20},\frac{21}{20}\right),
\]
one has
\[
\mathcal W_{\alpha,p}(x)>0
\qquad
0\le x\le10.
\]

The interval proof uses the sign-separated form
\[
\mathcal W_{\alpha,p}(x)=\sum_{m=0}^{\infty}(-1)^mA_mx^m,
\qquad A_m>0.
\]
For an interval \([L,R]\), this gives the lower bound
\[
\mathcal W_{\alpha,p}(x)
\ge
\sum_{\substack{m\le M\\m\ \mathrm{even}}}A_mL^m
-
\sum_{\substack{m\le M\\m\ \mathrm{odd}}}A_mR^m
-
\mathrm{Tail}_M(R).
\]
The tail is bounded by the next absolute term times a geometric factor, using the verified post-cutoff ratio bound.

The replay script first proves \([0,1]\) as in the small-endpoint proof. It then adaptively subdivides \([1,10]\) until the sign-separated lower bound is positive on every subinterval.

The resulting certified covers were:

\((3/4,11/10)\): \(2647\) subintervals, minimum lower bound \(0.000171213409032\ldots\).
\((11/20,21/20)\): \(31535\) subintervals, minimum lower bound \(0.000000169665277363\ldots\).

The second seed is the limiting case. The sign-separated lower bound is much more conservative than the actual function near larger \(x\), so the proof uses many small subintervals even though point values are comfortably positive.

_Proof source: `private proof note`._

## Tags

`bazhlekova`, `compact-certificate`, `partial-progress`, `proved`, `theorem`, `wright-function`
