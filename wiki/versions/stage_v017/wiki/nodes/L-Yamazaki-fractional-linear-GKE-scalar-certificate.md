---
id: "L-Yamazaki-fractional-linear-GKE-scalar-certificate"
type: "lemma"
title: "Fractional-linear scalar GKE certificate"
status: "proved"
tags: ["finite-certificate", "generalized-karcher-equation", "lemma", "operator-monotone", "proved", "rational-certificate", "scalar-certificate", "true"]
parents: ["L-Scalar-subcase-refutes-universal-operator-inequality", "D-Finite-dimensional-l1-dual-certificate-language", "T-Exact-finite-certificate-verification-principle"]
refs: ["private librarian audit", "private Oracle response", "private proof note"]
---

# Lemma: Fractional-linear scalar GKE certificate

## Statement

For \(g_0(x)=2(x-1)/(x+1)\), equal weights \((1/2,1/2)\), and scalar data \((A_1,A_2)=(4,1)\), the scalar generalized Karcher equation has unique positive solution \(X=2\), while \(g_0^{-1}((g_0(4)+g_0(1))/2)=13/7\).

## Dependencies

- [[wiki/nodes/L-Scalar-subcase-refutes-universal-operator-inequality|Scalar subcase refutes universal operator inequality]]
- [[wiki/nodes/D-Finite-dimensional-l1-dual-certificate-language|finite dimensional l1 primal representation coordinate atom dual linear functional certificate language]]
- [[wiki/nodes/T-Exact-finite-certificate-verification-principle|Exact finite certificate verification principle]]

## Proof and provenance references

- `private librarian audit`
- `private Oracle response`
- `private proof note`

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

_Proof source: `private proof note`._

## Tags

`finite-certificate`, `generalized-karcher-equation`, `lemma`, `operator-monotone`, `proved`, `rational-certificate`, `scalar-certificate`, `true`
