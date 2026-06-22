---
id: "L-MellinQuotient-To-ProductFactor"
type: "lemma"
title: "Mellin quotient product-factor criterion"
status: "proved"
tags: ["bridge-lemma", "lemma", "log-characteristic-function", "mellin-transform", "product-factorization", "proved", "true"]
parents: ["D-Laplace-kernel-and-tilted-moment-language"]
refs: ["raw/student/20260614T1245-dytso-generalized-gaussian-product-factorization.md"]
---

# Lemma: Mellin quotient product-factor criterion

## Statement

Let \(Y,Z,V\) be positive random variables with \(V\) independent of \(Z\). If \(\mathbb E(VZ)^{it}=\mathbb E Y^{it}\) for every real \(t\), then \(VZ\stackrel d=Y\). In particular, an explicit positive \(V\) whose Mellin transform is the quotient of the Mellin transforms of \(Y\) and \(Z\) on the imaginary line realizes the desired product factorization.

## Dependencies

- [[wiki/nodes/D-Laplace-kernel-and-tilted-moment-language|Laplace kernels and tilted moment ratios]]

## Proof and provenance references

- `raw/student/20260614T1245-dytso-generalized-gaussian-product-factorization.md`

## Proof

For \(r>0\), use the identity
\[
x^{-r}=\frac1{\Gamma(r)}\int_0^\infty u^{r-1}e^{-ux}\,du,\qquad x>0.
\]
With \(x=S_\alpha\) and Fubini,
\[
\mathbb E S_\alpha^{-r}
=
\frac1{\Gamma(r)}\int_0^\infty u^{r-1}\mathbb E e^{-uS_\alpha}\,du
=
\frac1{\Gamma(r)}\int_0^\infty u^{r-1}e^{-u^\alpha}\,du.
\]
Substituting \(v=u^\alpha\) gives
\[
\mathbb E S_\alpha^{-r}
=
\frac{\Gamma(r/\alpha)}{\alpha\Gamma(r)}.
\]
The same formula holds for complex \(r\) with \(\Re r>0\) by the same absolutely convergent integral.

For \(\Re z>0\),
\[
\mathbb E W_0^z
=
\mathbb E S_\alpha^{-bz}
=
\frac{\Gamma(bz/\alpha)}{\alpha\Gamma(bz)}
=
\frac{\Gamma(az)}{\alpha\Gamma(bz)},
\]
because \(b/\alpha=a\). Since
\[
\mathbb E W_0=\frac{\Gamma(a)}{\alpha\Gamma(b)}<\infty,
\]
the size-biased law is well-defined. For \(\Re s>-1\),
\[
\mathbb E W^s
=
\frac{\mathbb E W_0^{s+1}}{\mathbb E W_0}
=
\frac{\Gamma(a(s+1))\Gamma(b)}
        {\Gamma(b(s+1))\Gamma(a)}.
\]
Therefore
\[
\mathbb E V^s
=
2^{(a-b)s}
\frac{\Gamma(a(s+1))\Gamma(b)}
     {\Gamma(b(s+1))\Gamma(a)}.
\]

Let \(Y_q=|X_q|\), independent of \(V\). For \(\Re s>-1\),
\[
\mathbb E (VY_q)^s
=
\mathbb E V^s\,\mathbb E |X_q|^s.
\]
Using the source moment formula for \(X_q\),
\[
\mathbb E |X_q|^s
=
2^{bs}\frac{\Gamma(b(s+1))}{\Gamma(b)}.
\]
Thus
\[
\mathbb E (VY_q)^s
=
2^{as}\frac{\Gamma(a(s+1))}{\Gamma(a)}
=
\mathbb E |X_p|^s.
\]
Taking \(s=it\) gives equality of the characteristic functions of
\[
\log(V|X_q|)
\quad\text{and}\quad
\log|X_p|.
\]
Hence
\[
V|X_q|\stackrel d=|X_p|.
\]
Both \(X_q\) and \(X_p\) have continuous symmetric laws about \(0\), and \(V>0\) is independent of \(X_q\). Multiplication by \(V\) preserves the sign symmetry of \(X_q\), and the absolute values agree in distribution. Therefore
\[
VX_q\stackrel d=X_p.
\]

For \(p=q\), take \(V=1\). For \(p>q\), first-contact verified that the source's Proposition 15 proves the Mellin-ratio candidate is not a characteristic function, so no such positive independent factor exists. This completes the source-aligned classification.

_Proof source: `raw/student/20260614T1245-dytso-generalized-gaussian-product-factorization.md`._

## Tags

`bridge-lemma`, `lemma`, `log-characteristic-function`, `mellin-transform`, `product-factorization`, `proved`, `true`
