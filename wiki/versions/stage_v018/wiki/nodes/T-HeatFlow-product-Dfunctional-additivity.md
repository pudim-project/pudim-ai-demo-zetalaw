---
id: "T-HeatFlow-product-Dfunctional-additivity"
type: "theorem"
title: "heat flow Fisher D functional additive under product densities"
status: "proved"
tags: ["barrier-lemma", "fisher-information", "heat-flow", "primitive", "primitive-growth", "product-additivity", "proved", "tensorization", "theorem", "true"]
parents: []
refs: ["librarian/audits/LA-20260612T1535-heatflow-dfunctional-route-lemmas.json", "oracle/responses/OS-20260612T1510Z-heatflow-fisher-dfunctional-negativity-oracle-response.md", "raw/student/20260612T1530-heatflow-dfunctional-route-lemmas.md", "wiki/notes/frontier-heatflow-fisher-dfunctional-negativity.md"]
---

# Theorem: heat flow Fisher D functional additive under product densities

## Statement

For product densities \(f(x,y)=f_1(x)f_2(y)\), the heat-flow Fisher functional satisfies \(D[f]=D[f_1]+D[f_2]\). Therefore product lifts from nonnegative factors cannot create a negative \(D\) example.

## Proof and provenance references

- `librarian/audits/LA-20260612T1535-heatflow-dfunctional-route-lemmas.json`
- `oracle/responses/OS-20260612T1510Z-heatflow-fisher-dfunctional-negativity-oracle-response.md`
- `raw/student/20260612T1530-heatflow-dfunctional-route-lemmas.md`
- `wiki/notes/frontier-heatflow-fisher-dfunctional-negativity.md`

## Proof

Log-concavity means \(\nabla^2 u\preceq0\), hence \(H_f=-\nabla^2u\succeq0\). Therefore all eigenvalues of \(H_f\) are nonnegative and \(\operatorname{tr}(H_f^3)\ge0\). Also \(|\nabla H_f|^2\ge0\). The integrand is pointwise nonnegative and \(f>0\), so \(D[f]\ge0\).

Let \(f(x,y)=f_1(x)f_2(y)\) on \(\mathbb R^{d_1+d_2}\), with both factors admissible. Then
\[
D[f]=D[f_1]+D[f_2].
\]

Write \(u=u_1+u_2\). Then \(H_f\) is block diagonal with blocks \(H_{f_1}\) and \(H_{f_2}\). Hence
\[
\operatorname{tr}(H_f^3)=\operatorname{tr}(H_{f_1}^3)+\operatorname{tr}(H_{f_2}^3),
\]
and the squared gradient norm splits as
\[
|\nabla H_f|^2=|\nabla H_{f_1}|^2+|\nabla H_{f_2}|^2.
\]
Integration against the product density gives the claimed additivity. Thus product or tensor lifts from known nonnegative factors cannot create a negative \(D\) example.

Let \(f(x)=Z^{-1}e^{-V(r)}\), \(r=|x|\), and set
\[
a(r)=V''(r),\qquad b(r)=\frac{V'(r)}r.
\]
Then \(H_f=\nabla^2V\) has eigenvalues \(a\) in the radial direction and \(b\) with multiplicity \(d-1\). Moreover
\[
|\nabla H_f|^2
=(a')^2+(d-1)(b')^2+2(d-1)\frac{(a-b)^2}{r^2},
\]
so
\[
D[f]=
\frac{\omega_{d-1}}{Z}\int_0^\infty
\left[
(a')^2+(d-1)(b')^2
+2(d-1)\frac{(a-b)^2}{r^2}
+2a^3+2(d-1)b^3
\right]e^{-V(r)}r^{d-1}\,dr.
\]

The Hessian of a radial potential is
\[
\nabla^2V=bI+(a-b)\hat x\otimes\hat x.
\]
This gives the eigenvalues and the cubic trace. Differentiating this decomposition and using the standard orthogonal splitting of derivatives of \(\hat x\) gives the displayed norm formula. Polar integration gives the \(D[f]\) formula.

Let \(u\) be smooth periodic on \(\mathbb T^d\), and define
\[
D_T[u]=
\frac{\int_{\mathbb T^d}\left(|\nabla H_T|^2+2\operatorname{tr}(H_T^3)\right)e^u\,dx}
{\int_{\mathbb T^d}e^u\,dx},
\qquad H_T=-\nabla^2u.
\]
If \(D_T[u]<0\), then there exists a smooth strictly positive Gaussian-decaying density \(F_R\) on \(\mathbb R^d\) with \(D[F_R]<0\).

Periodically extend \(u\) to \(\mathbb R^d\) and set
\[
F_R(x)=Z_R^{-1}\exp\left(u(x)-\frac{|x|^2}{2R^2}\right).
\]
Then \(F_R\) is smooth, strictly positive, and Gaussian-decaying. Its logarithmic Hessian satisfies
\[
H_{F_R}=H_T+R^{-2}I,\qquad \nabla H_{F_R}=\nabla H_T.
\]
Consequently the integrand differs from the torus integrand by
\[
6R^{-2}\operatorname{tr}(H_T^2)+6R^{-4}\operatorname{tr}(H_T)+2dR^{-6}.
\]
Because \(u\) and its derivatives are periodic and bounded, Gaussian-window averages of the periodic numerator and denominator converge to their Haar averages on \(\mathbb T^d\) as \(R\to\infty\). Hence \(D[F_R]\to D_T[u]\). If \(D_T[u]<0\), then \(D[F_R]<0\) for all sufficiently large \(R\).

_Proof source: `raw/student/20260612T1530-heatflow-dfunctional-route-lemmas.md`._

## Tags

`barrier-lemma`, `fisher-information`, `heat-flow`, `primitive`, `primitive-growth`, `product-additivity`, `proved`, `tensorization`, `theorem`, `true`
