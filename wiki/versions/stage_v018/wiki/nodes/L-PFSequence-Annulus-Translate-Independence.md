---
id: "L-PFSequence-Annulus-Translate-Independence"
type: "lemma"
title: "Non-geometric Polya-frequency sequences have independent translates"
status: "proved"
tags: ["bridge", "laurent-annulus", "lemma", "log-concavity", "polya-frequency", "proved", "strict-private-post-v016", "strictification", "toeplitz-kernel", "true"]
parents: ["D-Determinant-triangular-compression-language", "D-TNKernel-FiniteOrder"]
refs: ["raw/student/20260620T0755-pfseq-tp-density-positive.md"]
---

# Lemma: Non-geometric Polya-frequency sequences have independent translates

## Statement

Let \(a\neq0\) be a Polya-frequency sequence on \(\mathbb Z\). If \(a\) is not a bilateral geometric sequence \(a_n=C\rho^n\), then every finite family of distinct translates \(n\mapsto a_{n-j}\) is linearly independent. Equivalently, every finite set of Toeplitz columns of \(T_a\) is linearly independent.

## Dependencies

- [[wiki/nodes/D-Determinant-triangular-compression-language|Determinant and triangular compression language]]
- [[wiki/nodes/D-TNKernel-FiniteOrder|Finite-order total nonnegativity for kernels]]

## Proof and provenance references

- `raw/student/20260620T0755-pfseq-tp-density-positive.md`

## Proof

Belton--Guillot--Khare--Putinar Question 12.2 asks whether totally positive Polya-frequency sequences are dense in all Polya-frequency sequences. I prove the pointwise/product-topology version:

\[
\forall a\in PF,\quad \exists b^{(r)}\in TP\cap PF
\quad\text{such that}\quad b^{(r)}_n\to a_n\quad(n\in\mathbb Z).
\]

Here \(PF\) means the Toeplitz kernel \(T_a(i,j)=a_{i-j}\) is totally nonnegative on \(\mathbb Z\times\mathbb Z\), and \(TP\) means all ordered minors are strictly positive.

Fix \(0<q<1\) and set
\[
g_q(n)=q^{n^2}.
\]
For strictly increasing integer grids \(i_1<\cdots<i_m\) and \(j_1<\cdots<j_m\),
\[
\det[g_q(i_r-j_s)]_{r,s=1}^m
=
q^{\sum_r i_r^2+\sum_s j_s^2}
\det[(q^{-2i_r})^{j_s}]_{r,s=1}^m .
\]
The bases \(x_r=q^{-2i_r}\) are strictly increasing positive numbers. After factoring the positive powers \(x_r^{j_1}\), the remaining determinant is the generalized Vandermonde determinant with strictly increasing nonnegative integer exponents \(j_s-j_1\). It is positive. Hence \(g_q\) is a strictly totally positive Polya-frequency sequence.

Let \(a\neq0\) be a PF sequence that is not a bilateral geometric sequence \(a_n=C\rho^n\). Then every finite family of distinct integer translates \(n\mapsto a_{n-j_s}\) is linearly independent.

First, \(1\times1\) minors give \(a_n\ge0\), and \(2\times2\) Toeplitz minors give log-concavity on the support:
\[
a_n^2\ge a_{n-1}a_{n+1}.
\]
Thus the support is an interval and, on the positive part of the support, the ratios
\[
r_n=\frac{a_n}{a_{n-1}}
\]
are nonincreasing.

If the support is finite or one-sided, the Laurent series \(A(z)=\sum_n a_nz^n\) is nonzero and converges on a nonempty annulus. If the support is all of \(\mathbb Z\), the monotone ratio limits
\[
L_+=\lim_{n\to+\infty}r_n,\qquad L_-=\lim_{n\to-\infty}r_n
\]
exist in \([0,\infty]\) with \(L_-\ge L_+\). If \(L_-=L_+\), monotonicity forces all ratios to be equal, so \(a_n=C\rho^n\), contrary to the non-geometric assumption. Hence \(L_->L_+\), and \(A(z)\) converges on the nonempty annulus
\[
\frac1{L_-}<|z|<\frac1{L_+},
\]
with the usual interpretations when a limit is \(0\) or \(\infty\).

Suppose now that a nontrivial finite translate dependence holds:
\[
\sum_{s=1}^m c_s a_{n-j_s}=0\qquad(n\in\mathbb Z).
\]
Multiplying the Laurent series by the nonzero Laurent polynomial \(P(z)=\sum_s c_s z^{j_s}\) gives \(P(z)A(z)=0\) throughout a nonempty annulus. Since \(A\) is not identically zero and \(P\) is not the zero polynomial, this is impossible. The finite translate family is therefore independent.

Let \(a\) be a nonzero non-geometric PF sequence and put
\[
b^{(q)}_n=(g_q*a)_n=\sum_{k\in\mathbb Z}q^{k^2}a_{n-k}.
\]
The exponential bounds from Lemma 2 make this absolutely convergent, and \(b^{(q)}_n\to a_n\) for each fixed \(n\) as \(q\downarrow0\).

The Toeplitz kernels satisfy \(T_{b^{(q)}}=T_{g_q}T_a\). For finite increasing grids \(I,J\) of size \(m\), the absolutely convergent Cauchy--Binet expansion is
\[
\det T_{b^{(q)}}[I,J]
=
\sum_{K\in{\binom{\mathbb Z}{m}}}
\det T_{g_q}[I,K]\det T_a[K,J].
\]
Every summand is nonnegative, because \(T_{g_q}\) is TP and \(T_a\) is TN. Lemma 2 says the \(J\)-columns of \(T_a\) are independent, so some coordinate set \(K\) has \(\det T_a[K,J]\neq0\). Since \(T_a\) is TN, that determinant is positive. The corresponding \(T_{g_q}\)-minor is strictly positive, so the whole sum is strictly positive. Therefore \(b^{(q)}\) is TP.

If \(a_n=C\rho^n\) with \(C>0\) and \(\rho>0\), set
\[
b^{(\varepsilon)}_n=C\rho^n e^{-\varepsilon n^2}.
\]
Then
\[
b^{(\varepsilon)}_{i-j}
=
C\rho^i\rho^{-j}e^{-\varepsilon i^2}e^{-\varepsilon j^2}e^{2\varepsilon ij}.
\]
Every Toeplitz minor is a positive row/column rescaling of the generalized Vandermonde determinant
\[
\det[(e^{2\varepsilon i_r})^{j_s}]_{r,s=1}^m,
\]
which is positive for \(i_1<\cdots<i_m\) and \(j_1<\cdots<j_m\). Hence \(b^{(\varepsilon)}\) is TP and \(b^{(\varepsilon)}_n\to C\rho^n\) as \(\varepsilon\downarrow0\).

If \(a=0\), then \(\eta g_q\to0\) pointwise as \(\eta\downarrow0\), and \(\eta g_q\) is TP for each \(\eta>0\).

_Proof source: `raw/student/20260620T0755-pfseq-tp-density-positive.md`._

## Tags

`bridge`, `laurent-annulus`, `lemma`, `log-concavity`, `polya-frequency`, `proved`, `strict-private-post-v016`, `strictification`, `toeplitz-kernel`, `true`
