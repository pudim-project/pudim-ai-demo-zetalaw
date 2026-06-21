---
id: "T-Bazhlekova-Wright-two-seed-Watson-tail-from-twenty-positive"
type: "theorem"
title: "Bazhlekova Wright two seed Watson tail positive from twenty"
status: "proved"
tags: ["asymptotic-remainder", "bazhlekova", "proved", "theorem", "watson-tail", "wright-function"]
parents: ["T-Polynomial-root-logderivative-localization-principle"]
refs: ["private librarian audit", "private proof note", "private proof artifact", "wiki/notes/frontier-bazhlekova-square-root-bf-gap.md"]
---

# Theorem: Bazhlekova Wright two seed Watson tail positive from twenty

## Statement

For the two no-cover seed Wright functions \(\mathcal W_{3/4,11/10}\) and \(\mathcal W_{11/20,21/20}\), one has \(\mathcal W_{\alpha,p}(x)>0\) for every \(x\ge20\), by a three-term Watson expansion with explicit algebraic-remainder and root-cut bounds.

## Dependencies

- [[wiki/nodes/T-Polynomial-root-logderivative-localization-principle|Polynomial root and logarithmic-derivative localization principle]]

## Proof and provenance references

- `private librarian audit`
- `private proof note`
- `private proof artifact`
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

_Proof source: `private proof note`._

## Tags

`asymptotic-remainder`, `bazhlekova`, `proved`, `theorem`, `watson-tail`, `wright-function`
