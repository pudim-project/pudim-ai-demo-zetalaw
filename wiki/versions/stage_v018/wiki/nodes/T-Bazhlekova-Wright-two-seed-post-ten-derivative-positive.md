---
id: "T-Bazhlekova-Wright-two-seed-post-ten-derivative-positive"
type: "theorem"
title: "Bazhlekova Wright two seed derivative positive on ten twenty"
status: "proved"
tags: ["bazhlekova", "derivative-positivity", "finite-window-certificate", "proved", "theorem", "wright-function"]
parents: ["T-Exact-finite-certificate-verification-principle"]
refs: ["librarian/audits/LA-20260601T022000-bazhlekova-post-ten-wright-tail-student.json", "raw/student/20260601T022000-bazhlekova-post-ten-derivative-bridge-proof.md", "raw/student/20260601T022000-bazhlekova-post-ten-derivative-bridge.py", "wiki/notes/frontier-bazhlekova-square-root-bf-gap.md"]
---

# Theorem: Bazhlekova Wright two seed derivative positive on ten twenty

## Statement

For the two no-cover seed Wright functions \(\mathcal W_{3/4,11/10}\) and \(\mathcal W_{11/20,21/20}\), one has \(\mathcal W_{\alpha,p}'(x)>0\) on \(10\le x\le20\).

## Dependencies

- [[wiki/nodes/T-Exact-finite-certificate-verification-principle|Exact finite certificate verification principle]]

## Proof and provenance references

- `librarian/audits/LA-20260601T022000-bazhlekova-post-ten-wright-tail-student.json`
- `raw/student/20260601T022000-bazhlekova-post-ten-derivative-bridge-proof.md`
- `raw/student/20260601T022000-bazhlekova-post-ten-derivative-bridge.py`
- `wiki/notes/frontier-bazhlekova-square-root-bf-gap.md`

## Proof

For both no-cover seed Wright functions,
\[
\mathcal W_{3/4,11/10}'(x)>0,
\qquad
\mathcal W_{11/20,21/20}'(x)>0
\qquad
10\le x\le20.
\]
Together with the already true compact certificate on \(0\le x\le10\), this
proves
\[
\mathcal W_{3/4,11/10}(x)>0,
\qquad
\mathcal W_{11/20,21/20}(x)>0
\qquad
0\le x\le20.
\]

Write
\[
\mathcal W_{\alpha,p}(x)=\sum_{m=0}^\infty c_mx^m,
\qquad
c_m=-\binom{1/2}{m}\frac1{\Gamma(pm-\alpha)}.
\]
On each interval \([c-1,c+1]\), with
\[
c\in\{11,13,15,17,19\},
\]
the replay script expands
\[
\mathcal W_{\alpha,p}'(c+y)=\sum_{r=0}^{40} d_ry^r+E_{40}(y),
\qquad |y|\le1.
\]
The coefficients \(d_r\) are computed from the differentiated defining series:
\[
d_r
=
\sum_{m\ge r+1}
c_m\,m\binom{m-1}{r}c^{m-1-r}.
\]
The lower bound for the finite Taylor polynomial uses the interval rules
\[
y^{2j+1}\in[-1,1],
\qquad
y^{2j}\in[0,1],
\]
and subtracts two explicit absolute remainders:

the centered Taylor tail \(r>40\) for the included coefficients;
the omitted coefficient tail \(m\ge900\), bounded by a geometric ratio on
  the right endpoint of the interval.

The replay script
certifies the following minimum derivative lower bounds:
\[
\min_{10\le x\le20}\mathcal W_{3/4,11/10}'(x)
\ge
0.0201343226217\ldots,
\]
and
\[
\min_{10\le x\le20}\mathcal W_{11/20,21/20}'(x)
\ge
0.00299977163172\ldots.
\]
The second seed is the limiting case. The omitted coefficient tail is below
\(10^{-1231}\) even in the hardest interval, and the centered Taylor tail is
below \(1.2\cdot10^{-47}\).

_Proof source: `raw/student/20260601T022000-bazhlekova-post-ten-derivative-bridge-proof.md`._

## Tags

`bazhlekova`, `derivative-positivity`, `finite-window-certificate`, `proved`, `theorem`, `wright-function`
