---
id: "T-JKS-Alpha2-NotTN5-PSDWitness"
type: "theorem"
title: "JKS alpha-two kernel is not TN5 by a symmetric determinant witness"
status: "proved"
tags: ["application-candidate", "finite-determinant-certificate", "jks-kernel", "minor-obstruction", "open-problem-solved", "positive-semidefinite", "proved", "source-solving", "strict-private-plus10", "theorem", "total-nonnegativity", "true"]
parents: ["D-JKS-Kernel", "D-TNKernel-FiniteOrder", "L-PSD-Minor-Obstructs-TN", "O-JKS-Alpha2-TN5-source-gate"]
refs: ["librarian/audits/LA-20260613T2120-jks-alpha2-tn5-strict-app.json", "oracle/responses/OS-20260613T211549Z-oracle-response.md", "raw/student/20260613T2118-jks-alpha2-tn5-determinant.md"]
---

# Theorem: JKS alpha-two kernel is not TN5 by a symmetric determinant witness

## Statement

For the Jain--Karlin--Schoenberg kernel \(K_{JKS}(x,y)=\max(1+xy,0)\), the square kernel \(K_{JKS}^2\) is not \(TN_5(\mathbb R\times\mathbb R)\). More strongly, at \(x=y=(-2,-1,0,1,2)\), the symmetric evaluation matrix \((K_{JKS}(x_i,x_j)^2)_{i,j=1}^5\) has determinant \(-57\), so it is not positive semidefinite.

## Dependencies

- [[wiki/nodes/D-JKS-Kernel|Jain-Karlin-Schoenberg kernel]]
- [[wiki/nodes/D-TNKernel-FiniteOrder|Finite-order total nonnegativity for kernels]]
- [[wiki/nodes/L-PSD-Minor-Obstructs-TN|Negative symmetric minor obstructs PSD and finite-order total nonnegativity]]
- [[wiki/nodes/O-JKS-Alpha2-TN5-source-gate|Jain-Karlin-Schoenberg alpha-two TN5 source gate]]

## Proof and provenance references

- `librarian/audits/LA-20260613T2120-jks-alpha2-tn5-strict-app.json`
- `oracle/responses/OS-20260613T211549Z-oracle-response.md`
- `raw/student/20260613T2118-jks-alpha2-tn5-determinant.md`

## Proof

Take
\[
x=y=(-2,-1,0,1,2).
\]
This tuple is strictly increasing. The matrix of \(1+x_i x_j\) is
\[
\begin{pmatrix}
5&3&1&-1&-3\\
3&2&1&0&-1\\
1&1&1&1&1\\
-1&0&1&2&3\\
-3&-1&1&3&5
\end{pmatrix}.
\]
Applying \(t\mapsto \max(t,0)^2\) entrywise gives
\[
A=\bigl(K_{JKS}(x_i,x_j)^2\bigr)_{i,j=1}^5
=
\begin{pmatrix}
25&9&1&0&0\\
9&4&1&0&0\\
1&1&1&1&1\\
0&0&1&4&9\\
0&0&1&9&25
\end{pmatrix}.
\]

Write
\[
B=\begin{pmatrix}25&9\\9&4\end{pmatrix},\qquad
C=\begin{pmatrix}4&9\\9&25\end{pmatrix},\qquad
u=\begin{pmatrix}1\\1\end{pmatrix}.
\]
Then
\[
A=
\begin{pmatrix}
B&u&0\\
u^T&1&u^T\\
0&u&C
\end{pmatrix}.
\]
Both \(B\) and \(C\) have determinant \(19\). The Schur complement gives
\[
\det A=\det(B)\det(C)\left(1-u^T B^{-1}u-u^T C^{-1}u\right).
\]
Since
\[
u^T B^{-1}u=u^T C^{-1}u=\frac{11}{19},
\]
we get
\[
\det A=19^2\left(1-\frac{22}{19}\right)=-57.
\]

A positive semidefinite matrix has nonnegative principal determinants. Since
\(\det A=-57<0\), the symmetric evaluation matrix is not positive semidefinite.
Thus \(K_{JKS}^2\) fails the stronger symmetric PSD witness target from the

Also, \(TN_5\) requires every minor of order at most \(5\), formed from
increasing row and column nodes, to be nonnegative. The same determinant is an
admissible \(5\times5\) minor with increasing row and column tuple
\((-2,-1,0,1,2)\). Its negativity proves
\[
K_{JKS}^2\notin TN_5(\mathbb R\times\mathbb R).
\]

This proves only the \(\alpha=2\) branch of the source question. It does not
solve the full integer family and makes no claim about \(\alpha\ge3\).

_Proof source: `raw/student/20260613T2118-jks-alpha2-tn5-determinant.md`._

## Do not claim

- Do not claim any branch \(\alpha\ne2\) of Khare's integer-family question is solved.
- Do not claim public APP registry assignment.
- Do not public-stage without user request.

## Tags

`application-candidate`, `finite-determinant-certificate`, `jks-kernel`, `minor-obstruction`, `open-problem-solved`, `positive-semidefinite`, `proved`, `source-solving`, `strict-private-plus10`, `theorem`, `total-nonnegativity`, `true`
