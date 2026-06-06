---
id: "T-KS-boundary-endpoint-sharpness"
type: "theorem"
title: "Boudabsa Simon KS lower bound constant matches infinity asymptotic coefficient"
status: "proved"
tags: ["asymptotic", "double-gamma", "endpoint-sharpness", "kilbas-saigo", "proved", "student", "theorem", "true-helper"]
parents: ["T-endpoint-log-derivative-monotonicity-principle"]
refs: ["librarian/audits/LA-20260528T002000-kilbas-saigo-normalization-ingest.json", "raw/scout/sources/boudabsa-simon-2021-kilbas-saigo.pdf", "raw/student/20260528T002000-kilbas-saigo-normalization.md", "wiki/notes/frontier-kilbas-saigo-boundary-hyperbolic.md"]
---

# Theorem: Boudabsa Simon KS lower bound constant matches infinity asymptotic coefficient

## Statement

The Boudabsa--Simon Conjecture 3 constant is endpoint-sharp relative to the source asymptotic: if \(D_{\alpha,m}=\Gamma(1+\alpha)G(1-\alpha;\alpha m)G(1+\alpha;\alpha m)\), then \(C_{\alpha,m}^{-(1+1/m)}=(\alpha m)^{\alpha/m}D_{\alpha,m}\), matching the leading coefficient of \(E_{\alpha,m,m-1/\alpha}(-x)\) as \(x\to\infty\).

## Dependencies

- [[wiki/nodes/T-endpoint-log-derivative-monotonicity-principle|T-endpoint-log-derivative-monotonicity-principle]]

## Proof and provenance references

- `librarian/audits/LA-20260528T002000-kilbas-saigo-normalization-ingest.json`
- `raw/scout/sources/boudabsa-simon-2021-kilbas-saigo.pdf`
- `raw/student/20260528T002000-kilbas-saigo-normalization.md`
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

_Proof source: `raw/student/20260528T002000-kilbas-saigo-normalization.md`._

## Tags

`asymptotic`, `double-gamma`, `endpoint-sharpness`, `kilbas-saigo`, `proved`, `student`, `theorem`, `true-helper`
