---
id: "L-DeterminantalPolynomial-SignConjugacy-Blindness"
type: "lemma"
title: "Two-by-two determinantal polynomial sign-conjugacy blindness"
status: "proved"
tags: ["bridge", "determinantal-stable-polynomial", "finite-certificate", "lemma", "principal-minor", "proved", "sign-conjugacy", "strict-private-post-v016", "true"]
parents: ["D-Determinant-triangular-compression-language", "D-Finite-dimensional-L1-certificate-language", "T-Exact-finite-certificate-verification-principle"]
refs: ["private Oracle response", "private proof note"]
---

# Lemma: Two-by-two determinantal polynomial sign-conjugacy blindness

## Statement

For a real symmetric matrix \(M=\begin{pmatrix}a&b\\ b&c\end{pmatrix}\) and \(Z=\operatorname{diag}(z_1,z_2)\), \(\det(I+MZ)=1+a z_1+c z_2+(ac-b^2)z_1z_2\). Hence the determinantal polynomial records the diagonal entries and determinant but not the sign of the off-diagonal entry.

## Dependencies

- [[wiki/nodes/D-Determinant-triangular-compression-language|Determinant and triangular compression language]]
- D-Finite-dimensional-L1-certificate-language
- [[wiki/nodes/T-Exact-finite-certificate-verification-principle|Exact finite certificate verification principle]]

## Proof and provenance references

- `private Oracle response`
- `private proof note`

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

_Proof source: `private proof note`._

## Do not claim

- Do not claim a full classification of all matrices with the same determinantal polynomial.
- Do not claim anything about quotient or sign-conjugacy repaired versions of BBL Question 4.1.
- Do not public-stage without user request.

## Tags

`bridge`, `determinantal-stable-polynomial`, `finite-certificate`, `lemma`, `principal-minor`, `proved`, `sign-conjugacy`, `strict-private-post-v016`, `true`
