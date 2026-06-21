---
id: "T-KS-gamma-laplace-normalization-lemma"
type: "theorem"
title: "Gamma Laplace transform normalizes Boudabsa Simon KS lower bound to Laplace order"
status: "proved"
tags: ["gamma", "kilbas-saigo", "laplace-transform", "normalization", "proved", "student", "theorem", "true-helper"]
parents: ["T-positive-Laplace-kernel-complete-monotonicity-principle", "D-Laplace-kernel-and-tilted-moment-language"]
refs: ["private librarian audit", "private proof note", "wiki/notes/frontier-kilbas-saigo-boundary-hyperbolic.md"]
---

# Theorem: Gamma Laplace transform normalizes Boudabsa Simon KS lower bound to Laplace order

## Statement

For \(p=1+1/m\) and \(C_{\alpha,m}>0\), \((1+C_{\alpha,m}x)^{-p}\) is the Laplace transform of a Gamma random variable with shape \(p\) and scale \(C_{\alpha,m}\). Consequently, Boudabsa--Simon Conjecture 3 is equivalent to the Laplace-order normal form \(Z_{\alpha,m}\le_{Lt}X_{\alpha,m}\).

## Dependencies

- [[wiki/nodes/T-positive-Laplace-kernel-complete-monotonicity-principle|T-positive-Laplace-kernel-complete-monotonicity-principle]]
- [[wiki/nodes/D-Laplace-kernel-and-tilted-moment-language|Laplace kernels and tilted moment ratios]]

## Proof and provenance references

- `private librarian audit`
- `private proof note`
- `wiki/notes/frontier-kilbas-saigo-boundary-hyperbolic.md`

## Proof

Let
\[
p=1+\frac1m=\frac{m+1}{m}.
\]
If \(Z_{\alpha,m}\) is a Gamma random variable with shape \(p\) and scale \(C_{\alpha,m}\), then
\[
\mathbb E e^{-xZ_{\alpha,m}}
=
\int_0^\infty e^{-xz}\frac{z^{p-1}e^{-z/C_{\alpha,m}}}{\Gamma(p)C_{\alpha,m}^p}\,dz
=
(1+C_{\alpha,m}x)^{-p}.
\]
Therefore the source inequality is exactly the Laplace-transform order
\[
Z_{\alpha,m}\le_{Lt}X_{\alpha,m},
\]
where
\[
\mathbb E e^{-xX_{\alpha,m}}
=E_{\alpha,m,m-1/\alpha}(-x).
\]

This proves the local normalization lemma and justifies the admitted equivalence edge
the KS laplace order equivalent source. It does not prove the source conjecture itself.

The source records the boundary asymptotic
\[
E_{\alpha,m,m-1/\alpha}(-x)
\sim
(\alpha m)^{\alpha/m}D_{\alpha,m}x^{-1-1/m}
\qquad(x\to\infty).
\]
The Gamma comparison has leading coefficient
\[
C_{\alpha,m}^{-p}
=
\left((\alpha m)^{-\alpha/(m+1)}
D_{\alpha,m}^{-m/(m+1)}\right)^{-(m+1)/m}
=
(\alpha m)^{\alpha/m}D_{\alpha,m}.
\]
Thus the conjectured constant is asymptotically sharp at \(+\infty\) relative to the source asymptotic.

The source confirms that the proof of the general lower bound is difficult because the relevant Mellin transform is expressed through generalized Pochhammer/double-Gamma symbols. The extracted source text gives enough to identify the correct bridge vocabulary, but not enough for a quick positive-kernel certificate.

Under the user's no-stalling rule, the all-parameter Mellin bridge remains open. The next useful move is either:

choose one non-\(m=1\) slice and certify it quickly, or

_Proof source: `private proof note`._

## Tags

`gamma`, `kilbas-saigo`, `laplace-transform`, `normalization`, `proved`, `student`, `theorem`, `true-helper`
