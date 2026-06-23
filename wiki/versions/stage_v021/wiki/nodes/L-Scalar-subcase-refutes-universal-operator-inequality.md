---
id: "L-Scalar-subcase-refutes-universal-operator-inequality"
type: "lemma"
title: "Scalar subcase refutes universal operator inequality"
status: "proved"
tags: ["bridge-lemma", "endpoint-obstruction", "finite-certificate", "lemma", "operator-inequality", "primitive-growth", "proved", "scalar-counterexample", "true"]
parents: ["D-Finite-dimensional-l1-dual-certificate-language", "D-Endpoint-obstruction-certificate-language", "T-Pointwise-obstruction-certificate-principle"]
refs: ["librarian/audits/LA-20260613T1735-yamazaki-gke-strict-app.json", "oracle/responses/OS-20260613T172559Z-oracle-response.md", "raw/student/20260613T1730-yamazaki-gke-scalar-refutation.md"]
---

# Lemma: Scalar subcase refutes universal operator inequality

## Statement

If an operator inequality is universally quantified over all Hilbert spaces and all tuples of positive invertible operators satisfying given hypotheses, then a one-dimensional scalar tuple satisfying those hypotheses and violating the resulting scalar inequality refutes the universal operator inequality.

## Dependencies

- [[wiki/nodes/D-Finite-dimensional-l1-dual-certificate-language|finite dimensional l1 primal representation coordinate atom dual linear functional certificate language]]
- [[wiki/nodes/D-Endpoint-obstruction-certificate-language|Endpoint and pointwise obstruction certificates]]
- [[wiki/nodes/T-Pointwise-obstruction-certificate-principle|T-Pointwise-obstruction-certificate-principle]]

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

## Tags

`bridge-lemma`, `endpoint-obstruction`, `finite-certificate`, `lemma`, `operator-inequality`, `primitive-growth`, `proved`, `scalar-counterexample`, `true`
