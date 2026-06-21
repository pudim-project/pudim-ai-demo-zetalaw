---
id: "T-Bazhlekova-Wright-two-seed-small-x-positive"
type: "theorem"
title: "Bazhlekova Wright two seed small x positive up to one"
status: "proved"
tags: ["bazhlekova", "endpoint-bound", "partial-progress", "proved", "theorem", "wright-function"]
parents: ["T-endpoint-log-derivative-monotonicity-principle"]
refs: ["private librarian audit", "private proof note", "private proof artifact", "wiki/notes/frontier-bazhlekova-square-root-bf-gap.md"]
---

# Theorem: Bazhlekova Wright two seed small x positive up to one

## Statement

For the two no-cover seed Wright functions \(\mathcal W_{3/4,11/10}\) and \(\mathcal W_{11/20,21/20}\), one has \(\mathcal W_{\alpha,p}(x)>0\) on \(0\le x\le1\). The proof uses the alternating coefficient sign pattern, domination of all negative odd terms on \([0,17/20]\), and a sign-separated interval bound on \([17/20,1]\).

## Dependencies

- [[wiki/nodes/T-endpoint-log-derivative-monotonicity-principle|T-endpoint-log-derivative-monotonicity-principle]]

## Proof and provenance references

- `private librarian audit`
- `private proof note`
- `private proof artifact`
- `wiki/notes/frontier-bazhlekova-square-root-bf-gap.md`

## Proof

For \(m\ge1\), \(pm-\alpha>0\), so \(\Gamma(pm-\alpha)>0\). Also
\[
-\binom{1/2}{m}
\]
has sign \((-1)^m\). The \(m=0\) term is positive because \(\Gamma(-\alpha)<0\) for \(0<\alpha<1\). Thus
\[
\mathcal W_{\alpha,p}(x)=\sum_{m=0}^{\infty}(-1)^m A_m x^m,
\qquad A_m>0.
\]
For \(0\le x\le r=17/20\), discard all positive even terms except \(m=0\) and bound all negative odd terms at \(r\):
\[
\mathcal W_{\alpha,p}(x)
\ge
A_0-\sum_{\substack{m\ge1\\m\ \mathrm{odd}}}A_m r^m.
\]

The replay script computes the odd sum through \(m=39\), then bounds the remaining positive absolute tail from the ratio of consecutive absolute terms. The ratio bound after the cutoff is below \(0.017\) for both seeds, so the geometric tail estimate is far below the printed lower margin.

The certified lower bounds are:
\[
\mathcal W_{3/4,11/10}(x)\ge 0.0113443230451029\ldots
\quad(0\le x\le17/20),
\]
and
\[
\mathcal W_{11/20,21/20}(x)\ge 0.0120267215569343\ldots
\quad(0\le x\le17/20).
\]

On the remaining interval \(17/20\le x\le1\), the same sign-separated bound uses positive even terms at the left endpoint and negative odd terms at the right endpoint:
\[
\mathcal W_{\alpha,p}(x)
\ge
\sum_{\substack{m\le M\\m\ \mathrm{even}}}A_m\left(\frac{17}{20}\right)^m
-
\sum_{\substack{m\le M\\m\ \mathrm{odd}}}A_m
-\mathrm{Tail}_M.
\]
With \(M=100\), the replay script gives lower bounds
\[
0.0706857533831170\ldots
\]
for \((3/4,11/10)\), and
\[
0.0587188420482698\ldots
\]
for \((11/20,21/20)\). Hence the two seed functions are positive on all of \([0,1]\).

_Proof source: `private proof note`._

## Tags

`bazhlekova`, `endpoint-bound`, `partial-progress`, `proved`, `theorem`, `wright-function`
