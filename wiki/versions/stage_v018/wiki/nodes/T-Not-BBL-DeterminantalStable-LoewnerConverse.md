---
id: "T-Not-BBL-DeterminantalStable-LoewnerConverse"
type: "counterexample"
title: "BBL determinantal stable Loewner converse is false"
status: "proved"
tags: ["application-candidate", "counterexample", "determinantal-stable-polynomial", "finite-certificate", "loewner-order", "open-problem-solved", "proper-position-order", "proved", "sign-conjugacy", "source-solving", "strict-private-post-v016", "true"]
parents: ["O-BBL-DeterminantalStable-LoewnerConverse-source-gate", "L-DeterminantalPolynomial-SignConjugacy-Blindness", "D-Determinant-triangular-compression-language", "T-Exact-finite-certificate-verification-principle"]
refs: ["oracle/responses/OS-20260621T0200Z-bbl-loewner-converse-oracle-response.md", "raw/student/20260621T0210-bbl-loewner-converse-counterexample.md"]
---

# Counterexample: BBL determinantal stable Loewner converse is false

## Statement

Borcea--Branden--Liggett Question 4.1 has a negative answer. For \(A=\begin{pmatrix}1&1/2\\1/2&2\end{pmatrix}\) and \(B=\begin{pmatrix}1&-1/2\\-1/2&2\end{pmatrix}\), both matrices are positive definite and the normalized determinantal stable polynomials \(\det(I+AZ)/\det(I+A)\) and \(\det(I+BZ)/\det(I+B)\) are identical, so the BBL order hypothesis holds. But \(B-A=\begin{pmatrix}0&-1\\-1&0\end{pmatrix}\) is indefinite, hence \(A\nleq B\) in Loewner order.

## Dependencies

- [[wiki/nodes/O-BBL-DeterminantalStable-LoewnerConverse-source-gate|Borcea-Branden-Liggett determinantal stable Loewner converse source gate]]
- [[wiki/nodes/L-DeterminantalPolynomial-SignConjugacy-Blindness|Two-by-two determinantal polynomial sign-conjugacy blindness]]
- [[wiki/nodes/D-Determinant-triangular-compression-language|Determinant and triangular compression language]]
- [[wiki/nodes/T-Exact-finite-certificate-verification-principle|Exact finite certificate verification principle]]

## Proof and provenance references

- `oracle/responses/OS-20260621T0200Z-bbl-loewner-converse-oracle-response.md`
- `raw/student/20260621T0210-bbl-loewner-converse-counterexample.md`

## Proof

Let
\[
A=\begin{pmatrix}1&1/2\\[2pt]1/2&2\end{pmatrix},
\qquad
B=\begin{pmatrix}1&-1/2\\[2pt]-1/2&2\end{pmatrix},
\qquad
Z=\operatorname{diag}(z_1,z_2).
\]
Both \(A\) and \(B\) are positive definite, since their leading principal minors are positive and
\[
\det A=\det B=2-\frac14=\frac74>0.
\]

For a real symmetric \(2\times2\) matrix
\[
M=\begin{pmatrix}a&b\\ b&c\end{pmatrix},
\]
one has
\[
\det(I+MZ)=1+a z_1+c z_2+(ac-b^2)z_1z_2.
\]
Therefore the sign of \(b\) is invisible to the determinantal stable polynomial. In the present example,
\[
\det(I+AZ)=\det(I+BZ)=1+z_1+2z_2+\frac74 z_1z_2,
\]
and also
\[
\det(I+A)=\det(I+B)=\frac{23}{4}.
\]
Hence the normalized polynomials are identical:
\[
\frac{\det(I+AZ)}{\det(I+A)}
=
\frac{\det(I+BZ)}{\det(I+B)}.
\]

The BBL order hypothesis holds immediately by equality. Equivalently, if one checks the stronger proper-position relation directly, \(p_A=p_B\) gives
\[
p_B+i p_A=(1+i)p_A,
\]
which is stable because \(p_A\) is a determinantal stable polynomial and multiplication by a nonzero constant preserves stability.

However,
\[
B-A=
\begin{pmatrix}0&-1\\ -1&0\end{pmatrix}
\]
has eigenvalues \(1\) and \(-1\). Thus \(B-A\) is indefinite and \(A\nleq B\) in Loewner order. Similarly \(A-B\) is indefinite, so the matrices are not Loewner-comparable.

For completeness, the example is not a commuting or diagonal case:
\[
AB=\begin{pmatrix}3/4&1/2\\ -1/2&15/4\end{pmatrix},
\qquad
BA=\begin{pmatrix}3/4&-1/2\\ 1/2&15/4\end{pmatrix},
\]
so \(AB\ne BA\).

The obstruction is the non-injectivity of \(M\mapsto\det(I+MZ)\). In dimension two, the polynomial records \(a\), \(c\), and \(ac-b^2\), but not the sign of \(b\). Diagonal sign conjugation \(M\mapsto DMD\), with \(D=\operatorname{diag}(1,-1)\), preserves all principal-minor data and hence the normalized determinantal stable polynomial, while literal Loewner comparison between \(M\) and \(DMD\) can fail.

This refutes the literal source question. It does not refute possible repaired quotient formulations modulo diagonal sign conjugacy.

_Proof source: `raw/student/20260621T0210-bbl-loewner-converse-counterexample.md`._

## Do not claim

- Do not claim this contradicts BBL Proposition 4.15, which proves the forward implication.
- Do not claim a classification modulo diagonal sign conjugacy.
- Do not claim public APP numbering until staging/registry promotion.
- Do not public-stage without user request.

## Tags

`application-candidate`, `counterexample`, `determinantal-stable-polynomial`, `finite-certificate`, `loewner-order`, `open-problem-solved`, `proper-position-order`, `proved`, `sign-conjugacy`, `source-solving`, `strict-private-post-v016`, `true`
