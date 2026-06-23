---
id: "B-Cutoff-Column-Against-CorankOne-Gram"
type: "theorem"
title: "Cutoff column against a corank-one Gram block"
status: "proved"
tags: ["bridge-theorem", "cutoff-kernel", "determinant-obstruction", "divided-difference", "finite-certificate", "positive-semidefinite", "primitive-support", "proved", "theorem", "true"]
parents: ["L-PSD-Minor-Obstructs-TN", "D-Determinant-triangular-compression-language", "T-Exact-finite-certificate-verification-principle"]
refs: ["librarian/audits/LA-20260622T0139-jks-integer-family-strict-app.json", "oracle/responses/OS-20260622T013230Z-oracle-response.md", "raw/student/20260622T0138-jks-integer-family-cutoff-gram.md"]
---

# Theorem: Cutoff column against a corank-one Gram block

## Statement

Let \(A\succeq0\) be a real symmetric \(n\times n\) matrix of rank \(n-1\), and let \(q\ne0\) span \(\ker A\). If \(b\in\mathbb R^n\) satisfies \(q^Tb\ne0\), then for every real \(d\), the bordered matrix \(\begin{pmatrix}A&b\\ b^T&d\end{pmatrix}\) has negative determinant. In particular, when \(A\) is a singular polynomial Gram block and a cutoff column is not orthogonal to its divided-difference nullvector, the full symmetric evaluation determinant is negative.

## Dependencies

- [[wiki/nodes/L-PSD-Minor-Obstructs-TN|Negative symmetric minor obstructs PSD and finite-order total nonnegativity]]
- [[wiki/nodes/D-Determinant-triangular-compression-language|Determinant and triangular compression language]]
- [[wiki/nodes/T-Exact-finite-certificate-verification-principle|Exact finite certificate verification principle]]

## Proof and provenance references

- `librarian/audits/LA-20260622T0139-jks-integer-family-strict-app.json`
- `oracle/responses/OS-20260622T013230Z-oracle-response.md`
- `raw/student/20260622T0138-jks-integer-family-cutoff-gram.md`

## Proof

Put \(n=m+2\) and
\[
a_i=-(m+3-i),\qquad 1\le i\le n.
\]
Thus
\[
a_1=-(m+2)<a_2=-(m+1)<\cdots<a_{m+1}=-2<a_{m+2}=-1<0.
\]
Let \(t=2/3\), and order the witness as
\[
x=(a_1,\ldots,a_n,t).
\]

Write \(M_m\) in block form
\[
M_m=\begin{pmatrix}A&b\\ b^T&d\end{pmatrix},
\]
where
\[
A_{ij}=K_m(a_i,a_j),\qquad b_i=K_m(a_i,t),\qquad d=K_m(t,t).
\]
Since \(a_i a_j>0\), the cutoff is inactive on the negative block:
\[
A_{ij}=(1+a_i a_j)^m
=\sum_{k=0}^m \binom{m}{k}a_i^k a_j^k.
\]
Therefore \(A=VDV^T\), where \(V_{ik}=a_i^k\) for \(0\le k\le m\) and
\[
D=\operatorname{diag}\binom{m}{0},\binom{m}{1},\ldots,\binom{m}{m}.
\]
The \(a_i\)'s are distinct, so \(V\) has rank \(m+1\). Since \(A\) has size
\(m+2\), it is positive semidefinite of rank \(m+1\), hence corank one.

Let
\[
P(z)=\prod_{r=1}^n(z-a_r),\qquad q_i=\frac{1}{P'(a_i)}.
\]
The standard divided-difference identity gives
\[
\sum_{i=1}^n q_i p(a_i)=0
\]
for every polynomial \(p\) of degree at most \(n-2=m\). For each fixed \(j\),
the function \(z\mapsto(1+za_j)^m\) has degree at most \(m\), hence \(Aq=0\).
Thus \(q\) spans \(\ker A\).

Now compute the cutoff column. For \(i\le m+1\), one has \(a_i\le -2\), so
\[
1+\frac23 a_i\le 1-\frac43<0,
\]
and therefore \(b_i=0\). For \(i=n=m+2\), \(a_n=-1\), so
\[
b_n=\left(1-\frac23\right)^m=3^{-m}.
\]
Moreover
\[
P'(-1)=\prod_{j=1}^{n-1}(-1-a_j)=(m+1)!.
\]
Consequently
\[
q^T b=\frac{1}{3^m(m+1)!}\ne0.
\]

Since \(A\succeq0\) has rank \(n-1\), its adjugate is a nonzero positive
multiple of \(qq^T\):
\[
\operatorname{adj}(A)=\gamma qq^T,\qquad \gamma>0.
\]
Therefore
\[
\det M_m
=d\det A-b^T\operatorname{adj}(A)b
=-\gamma(q^Tb)^2<0.
\]
This is a symmetric principal determinant on the strictly increasing tuple
\[
-(m+2)<-(m+1)<\cdots<-2<-1<2/3.
\]
It refutes positive semidefiniteness of \(K_m\), and by the existing
finite-order TN obstruction lemma it also refutes \(TN_{m+3}\).

The symbolic proof was sanity-checked by exact rational determinant
calculations:

\(m=3\): determinant \(-16/9\).
\(m=4\): determinant \(-32768/27\).
\(m=5\): determinant \(-4096000000/81\).
\(m=6\): determinant \(-188743680000000\).

For \(3\le m\le8\), exact replay also confirmed
\[
q^T b=\frac{1}{3^m(m+1)!}.
\]

The reusable bridge is not JKS-specific:

If \(A\succeq0\) is a real symmetric \(n\times n\) matrix with rank \(n-1\),
and \(q\) spans \(\ker A\), then every bordered matrix
\[
\begin{pmatrix}A&b\\ b^T&d\end{pmatrix}
\]
with \(q^T b\ne0\) has negative determinant. A polynomial Gram block supplies
such an \(A\), and a cutoff column can force \(q^T b\ne0\).

The proof solves the source-open remaining family \(m\ge3\), not the already
closed/overlapping low cases. This is a strict private APP candidate:
APP-0081, pending only future public staging requested by the user.

_Proof source: `raw/student/20260622T0138-jks-integer-family-cutoff-gram.md`._

## Tags

`bridge-theorem`, `cutoff-kernel`, `determinant-obstruction`, `divided-difference`, `finite-certificate`, `positive-semidefinite`, `primitive-support`, `proved`, `theorem`, `true`
