---
id: "T-Bazhlekova-Wright-finite-window-tail-bridge"
type: "theorem"
title: "Bazhlekova Wright finite window asymptotic tail bridge"
status: "proved"
tags: ["attack-plan", "bazhlekova", "finite-window-certificate", "proved", "theorem", "wright-function"]
parents: ["T-endpoint-log-derivative-monotonicity-principle"]
refs: ["attack-plans/AP-20260601T021500-bazhlekova-post-ten-wright-tail.json", "librarian/audits/LA-20260601T023000-bazhlekova-post-ten-wright-tail-student.json", "raw/student/20260601T023000-bazhlekova-watson-tail-certificate-proof.md", "theory/nodes/T-Bazhlekova-Wright-two-seed-Watson-tail-from-twenty-positive.json", "theory/nodes/T-Bazhlekova-Wright-two-seed-compact-zero-twenty-positive.json", "wiki/notes/frontier-bazhlekova-square-root-bf-gap.md"]
---

# Theorem: Bazhlekova Wright finite window asymptotic tail bridge

## Statement

For the seed functions \(\mathcal W_{3/4,11/10}\) and \(\mathcal W_{11/20,21/20}\), there are explicit rational endpoints \(10<X<\infty\), a faster certified finite-window positivity cover on \([10,X]\), and a rigorous asymptotic lower bound on \([X,\infty)\); together with the true \([0,10]\) theorem this proves all-x positivity.

## Dependencies

- [[wiki/nodes/T-endpoint-log-derivative-monotonicity-principle|T-endpoint-log-derivative-monotonicity-principle]]

## Proof and provenance references

- `attack-plans/AP-20260601T021500-bazhlekova-post-ten-wright-tail.json`
- `librarian/audits/LA-20260601T023000-bazhlekova-post-ten-wright-tail-student.json`
- `raw/student/20260601T023000-bazhlekova-watson-tail-certificate-proof.md`
- `theory/nodes/T-Bazhlekova-Wright-two-seed-Watson-tail-from-twenty-positive.json`
- `theory/nodes/T-Bazhlekova-Wright-two-seed-compact-zero-twenty-positive.json`
- `wiki/notes/frontier-bazhlekova-square-root-bf-gap.md`

## Proof

For both no-cover seed Wright functions,
\[
\mathcal W_{3/4,11/10}(x)>0,
\qquad
\mathcal W_{11/20,21/20}(x)>0
\qquad
x\ge20.
\]
Combined with the previous true node
the Bazhlekova Wright two seed compact zero twenty positive, this proves all-\(x\)
positivity for the two seed Wright functions.

Let
\[
\beta=\alpha-\frac p2.
\]
The three-term Watson polynomial is
\[
P_3(x)=A_0x^{1/2}+A_1x^{-1/2}+A_2x^{-3/2},
\]
where
\[
A_k
=
\binom{1/2}{k}\frac{\beta+kp}{\Gamma(1-\beta-kp)}
=
-\frac{\binom{1/2}{k}}{\Gamma(p/2-\alpha-kp)}.
\]

The replay script uses the branch-audited contour decomposition
\[
\mathcal W_{\alpha,p}(x)=P_3(x)+R_{\mathrm{alg}}(x)+R_{\mathrm{cut}}(x).
\]
Here \(R_{\mathrm{alg}}\) is the algebraic Watson remainder from the
negative-axis part of the Hankel deformation, and \(R_{\mathrm{cut}}\) is the
combined contribution of the two square-root branch cuts at
\[
x^{1/p}e^{\pm i\pi/p}.
\]

For \(x\ge20\), the algebraic remainder is bounded by splitting the
negative-axis integral at
\[
s=\eta x^{1/p},
\qquad
\eta=0.8.
\]
On the first piece, \(|r^p/x|\le \eta^p<1\), so the binomial remainder after
three terms is bounded by
\[
C_3(\eta^p)\,x^{-5/2}\Gamma(\beta+3p+1),
\]
where
\[
C_3(q)=\sum_{k\ge3}\left|\binom{1/2}{k}\right|q^{k-3}.
\]
On the second piece, the exact square-root factor and the first three
subtracted Watson integrands are bounded absolutely by incomplete-gamma tails.
The replay also checks that the relevant incomplete-gamma tail bounds are
decreasing for all \(x\ge20\). Thus the maximum bound occurs at \(x=20\).

The root-cut contribution is exponentially small because
\[
\cos(\pi/p)<0.
\]
The replay uses the conservative estimate
\[
|R_{\mathrm{cut}}(x)|
\le
\frac4\pi\,t^{-p/2}c^{-(\alpha+p/2+1)}
\Gamma(\alpha+p/2+1,ct),
\quad
t=x^{1/p},\quad c=-\cos(\pi/p),
\]
again evaluated at the threshold \(x=20\).

For \((\alpha,p)=(3/4,11/10)\), the threshold data are
\[
P_3(20)=0.7334040707348\ldots,
\]
\[
|R_{\mathrm{alg}}(20)|\le0.00102487268524\ldots,
\qquad
|R_{\mathrm{cut}}(20)|\le0.00000501719347\ldots,
\]
leaving margin
\[
0.732374180856\ldots.
\]

For the hard seed \((\alpha,p)=(11/20,21/20)\), the threshold data are
\[
P_3(20)=0.1011701494061\ldots,
\]
\[
|R_{\mathrm{alg}}(20)|\le0.000601818880498\ldots,
\qquad
|R_{\mathrm{cut}}(20)|\le0.000000234841234\ldots,
\]
leaving margin
\[
0.100568095684\ldots.
\]

The replay script is

_Proof source: `raw/student/20260601T023000-bazhlekova-watson-tail-certificate-proof.md`._

## Tags

`attack-plan`, `bazhlekova`, `finite-window-certificate`, `proved`, `theorem`, `wright-function`
