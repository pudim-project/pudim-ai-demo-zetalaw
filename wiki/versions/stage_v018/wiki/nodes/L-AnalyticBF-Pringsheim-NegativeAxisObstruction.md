---
id: "L-AnalyticBF-Pringsheim-NegativeAxisObstruction"
type: "lemma"
title: "Analytic Bernstein functions have a Pringsheim negative-axis obstruction"
status: "proved"
tags: ["bernstein-functions", "bridge-lemma", "coefficient-signs", "complete-monotonicity", "lemma", "pringsheim", "proved", "singularity-obstruction", "true"]
parents: ["D-Complete-monotonicity-Bernstein-Stieltjes-language", "D-Endpoint-obstruction-certificate-language", "T-Polynomial-root-logderivative-localization-principle", "T-Pointwise-obstruction-certificate-principle"]
refs: ["librarian/audits/LA-20260613T2228-li-cubic-strict-app.json", "raw/student/20260613T2225-li-cubic-inverse-bf-discriminant.md"]
---

# Lemma: Analytic Bernstein functions have a Pringsheim negative-axis obstruction

## Statement

Let \(f(z)=\sum_{n\ge1}c_n z^n\) be analytic at \(0\) with finite radius of convergence \(R\). If \(f\) is a Bernstein function on \((0,\infty)\), then \((-1)^{n-1}c_n\ge0\). Consequently \(-f(-z)\) has nonnegative Taylor coefficients and, by Pringsheim's theorem, \(f\) has a singularity at the negative real point \(-R\).

## Dependencies

- [[wiki/nodes/D-Complete-monotonicity-Bernstein-Stieltjes-language|Complete monotonicity, Bernstein, and Stieltjes language]]
- [[wiki/nodes/D-Endpoint-obstruction-certificate-language|Endpoint and pointwise obstruction certificates]]
- [[wiki/nodes/T-Polynomial-root-logderivative-localization-principle|Polynomial root and logarithmic-derivative localization principle]]
- [[wiki/nodes/T-Pointwise-obstruction-certificate-principle|T-Pointwise-obstruction-certificate-principle]]

## Proof and provenance references

- `librarian/audits/LA-20260613T2228-li-cubic-strict-app.json`
- `raw/student/20260613T2225-li-cubic-inverse-bf-discriminant.md`

## Proof

Assume \(\Delta=a^2-3b\ge0\). Since \(b\ge0\), one has \(\sqrt{\Delta}\le a\). Put
\[
r_-=\frac{a-\sqrt{\Delta}}3,\qquad
r_+=\frac{a+\sqrt{\Delta}}3.
\]
Then \(0\le r_-\le r_+\), and
\[
P'(x)=3x^2+2ax+b=3(x+r_-)(x+r_+).
\]
Hence
\[
g(x)=\frac1{P'(x)}
\]
is completely monotone on \((0,\infty)\). Indeed, \(x\mapsto (x+r)^{-1}\) is completely monotone for \(r\ge0\), and products of completely monotone functions are completely monotone. The repeated-root and \(r=0\) endpoint cases follow by the same formula or by limits; for example \(1/(3x^2)\) is completely monotone.

The inverse satisfies
\[
\varphi'(\lambda)=g(\varphi(\lambda)).
\]
Li's Lemma 2.4 gives the inverse-ODE criterion: if \(g\) is completely monotone and a positive solution satisfies \(y'=g(y)\), then \(y\) is Bernstein. For completeness, the sign induction is short. The base \(y'>0\) is clear. If \((-1)^{j-1}y^{(j)}\ge0\) for \(1\le j\le n\), Faà di Bruno applied to \(y^{(n+1)}=(g\circ y)^{(n)}\) writes the derivative as a sum of Bell-polynomial terms. A term with \(k\) derivatives on \(g\) has sign
\[
(-1)^k(-1)^{n-k}=(-1)^n,
\]
because \(g^{(k)}\) has sign \((-1)^k\), and the product of \(y^{(j)}\)-terms has total sign \((-1)^{n-k}\). Thus \((-1)^n y^{(n+1)}\ge0\). Applying this to \(y=\varphi\) proves that \(\varphi'\) is completely monotone, so \(\varphi\) is Bernstein.

Assume \(a^2<3b\). Then \(b>0\), and
\[
P'(x)=3x^2+2ax+b>0
\]
for every real \(x\). Therefore \(P:\mathbb R\to\mathbb R\) is strictly increasing and onto, and its real inverse is real analytic in a neighborhood of every real \(\lambda\). In particular, the branch \(\varphi\) continued from \(0\) along the real axis has no singularity at any negative real point.

Because \(b>0\), \(\varphi\) is analytic at \(0\):
\[
\varphi(\lambda)=\sum_{n\ge1}c_n\lambda^n.
\]
The radius of this Taylor series is finite. If it were infinite, \(\varphi\) would be entire and would satisfy \(P(\varphi(\lambda))=\lambda\) for every \(\lambda\). For large \(|w|\), \(|P(w)|\ge |w|^3/2\), so this identity would imply
\[
|\varphi(\lambda)|\le C(1+|\lambda|)^{1/3}.
\]
Cauchy's estimate would then force \(\varphi'\equiv0\), contradicting \(P'(\varphi)\varphi'=1\). Let \(R<\infty\) be the radius of convergence.

Suppose for contradiction that \(\varphi\) is Bernstein. Since \(\varphi'\) is completely monotone and \(\varphi\) is analytic at \(0\),
\[
(-1)^{n-1}c_n\ge0,\qquad n\ge1.
\]
Define
\[
F(z)=-\varphi(-z)=\sum_{n\ge1}(-1)^{n-1}c_n z^n.
\]
Then \(F\) has nonnegative Taylor coefficients and the same finite radius \(R\). By Pringsheim's theorem, \(F\) has a singularity at \(z=R\). Equivalently, \(\varphi\) has a singularity at \(\lambda=-R\).

This contradicts the real-axis analyticity proved above, because \(-R<0\). Therefore \(\varphi\) is not Bernstein when \(a^2<3b\).

Combining the two directions gives the exact cubic criterion.

D-InversePolynomialBFProblem: Li's inverse-polynomial coefficient-condition vocabulary.
the QuadraticDenominator CM NonpositiveRoots: reciprocal quadratic with nonpositive real zeros is completely monotone.
the InverseODE CM to BF: Li Lemma 2.4 / Faà di Bruno inverse-ODE criterion.
the AnalyticBF Pringsheim NegativeAxisObstruction: analytic Bernstein functions with finite radius have the Pringsheim negative-axis obstruction for their Taylor branch.

_Proof source: `raw/student/20260613T2225-li-cubic-inverse-bf-discriminant.md`._

## Tags

`bernstein-functions`, `bridge-lemma`, `coefficient-signs`, `complete-monotonicity`, `lemma`, `pringsheim`, `proved`, `singularity-obstruction`, `true`
