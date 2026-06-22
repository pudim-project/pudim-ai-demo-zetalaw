---
id: "T-Yamazaki-GKE-operator-norm-conjecture-scalar-counterexample"
type: "theorem"
title: "Yamazaki generalized-Karcher operator-norm conjecture is false"
status: "proved"
tags: ["application-candidate", "finite-certificate", "generalized-karcher-equation", "open-problem-solved", "operator-monotone", "operator-norm", "proved", "scalar-counterexample", "source-solving", "strict-private-plus10", "theorem", "true"]
parents: ["L-Scalar-subcase-refutes-universal-operator-inequality", "L-Yamazaki-fractional-linear-GKE-scalar-certificate", "O-Yamazaki-GKE-Norm-Conjecture-source-gate"]
refs: ["librarian/audits/LA-20260613T1735-yamazaki-gke-strict-app.json", "oracle/responses/OS-20260613T172559Z-oracle-response.md", "raw/student/20260613T1730-yamazaki-gke-scalar-refutation.md"]
---

# Theorem: Yamazaki generalized-Karcher operator-norm conjecture is false

## Statement

Yamazaki's generalized-Karcher operator-norm conjecture is false. In the one-dimensional scalar case, with \(g_0(x)=2(x-1)/(x+1)\), \(\omega=(1/2,1/2)\), \(A_1=4\), and \(A_2=1\), the generalized Karcher solution is \(\sigma_{g_0}=2\), while the conjectured right-hand side is \(g_0^{-1}((g_0(4)+g_0(1))/2)=13/7\). Thus the conjectured inequality would require \(2\le13/7\), a contradiction.

## Dependencies

- [[wiki/nodes/L-Scalar-subcase-refutes-universal-operator-inequality|Scalar subcase refutes universal operator inequality]]
- [[wiki/nodes/L-Yamazaki-fractional-linear-GKE-scalar-certificate|Fractional-linear scalar GKE certificate]]
- [[wiki/nodes/O-Yamazaki-GKE-Norm-Conjecture-source-gate|Yamazaki generalized-Karcher operator-norm conjecture source gate]]

## Proof and provenance references

- `librarian/audits/LA-20260613T1735-yamazaki-gke-strict-app.json`
- `oracle/responses/OS-20260613T172559Z-oracle-response.md`
- `raw/student/20260613T1730-yamazaki-gke-scalar-refutation.md`

## Proof

Let
\[
g_0(x)=\frac{2(x-1)}{x+1}=2-\frac4{x+1}.
\]
Yamazaki lists this fractional-linear example among the normalized operator-monotone functions in \(L\). Independently, \(x\mapsto (x+1)^{-1}\) is operator-monotone decreasing on \((0,\infty)\), so \(g_0\) is operator-monotone increasing. Also
\[
g_0(1)=0,\qquad
g_0'(x)=\frac4{(x+1)^2},\qquad
g_0'(1)=1.
\]
Hence \(g_0\in L\).

Take \(H=\mathbb C\), equal weights \(\omega=(1/2,1/2)\), and scalar operators
\[
A_1=4,\qquad A_2=1.
\]
For a positive scalar \(X\), the generalized Karcher equation becomes
\[
\frac12 g_0(4/X)+\frac12 g_0(1/X)=0.
\]
Since
\[
g_0(a/X)=\frac{2(a-X)}{a+X},
\]
this is equivalent to
\[
\frac{4-X}{4+X}+\frac{1-X}{1+X}=0.
\]
The numerator is
\[
(4-X)(1+X)+(1-X)(4+X)=8-2X^2.
\]
The unique positive solution is \(X=2\). Therefore
\[
\sigma_{g_0}\bigl((1/2,1/2);4,1\bigr)=2.
\]

On the right-hand side of the conjectured inequality,
\[
g_0(4)=\frac65,\qquad g_0(1)=0,
\]
so
\[
\frac12 g_0(4)+\frac12 g_0(1)=\frac35.
\]
Solving \(u=2(x-1)/(x+1)\) gives
\[
g_0^{-1}(u)=\frac{2+u}{2-u}.
\]
Hence
\[
g_0^{-1}\left(\frac35\right)
=\frac{2+3/5}{2-3/5}
=\frac{13}{7}.
\]
Since the scalar operator norm is absolute value and all quantities here are positive, the conjectured inequality would require
\[
2\le \frac{13}{7},
\]
which is false.

Thus Yamazaki's displayed operator-norm conjecture is false.

This proof only refutes the universal conjecture by a scalar counterexample. It does not classify all \(g\in L\), all scalar pairs, all weights, or any positive validity region. It does not make claims about adjacent Yamazaki norm inequalities or unitarily invariant norm statements not covered by the displayed source conjecture.

_Proof source: `raw/student/20260613T1730-yamazaki-gke-scalar-refutation.md`._

## Do not claim

- Do not claim a classification of all \(g\in L\) or all scalar pairs.
- Do not claim anything about adjacent Yamazaki inequalities not covered by the displayed source conjecture.
- Do not public-stage without user request.

## Tags

`application-candidate`, `finite-certificate`, `generalized-karcher-equation`, `open-problem-solved`, `operator-monotone`, `operator-norm`, `proved`, `scalar-counterexample`, `source-solving`, `strict-private-plus10`, `theorem`, `true`
