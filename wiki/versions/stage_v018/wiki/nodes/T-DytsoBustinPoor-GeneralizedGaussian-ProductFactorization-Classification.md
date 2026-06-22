---
id: "T-DytsoBustinPoor-GeneralizedGaussian-ProductFactorization-Classification"
type: "theorem"
title: "Dytso-Bustin-Poor generalized-Gaussian product factorization classification"
status: "proved"
tags: ["application-candidate", "generalized-gaussian", "mellin-transform", "open-problem-solved", "positive-stable", "product-factorization", "proved", "size-bias", "source-solving", "strict-private-plus10", "theorem", "true"]
parents: ["O-DytsoBustinPoor-GeneralizedGaussian-ProductFactorization-source-gate", "D-GeneralizedGaussian-Np01", "L-PositiveStable-NegativeMoment", "D-InverseStable-SizeBiasFactor", "L-MellinQuotient-To-ProductFactor"]
refs: ["oracle/responses/OS-20260614T1240Z-oracle-response.md", "raw/student/20260614T1245-dytso-generalized-gaussian-product-factorization.md"]
---

# Theorem: Dytso-Bustin-Poor generalized-Gaussian product factorization classification

## Statement

For centered unit-scale generalized Gaussian random variables \(X_p\sim N_p(0,1)\) and \(X_q\sim N_q(0,1)\), there exists a positive random variable \(V\), independent of \(X_q\), such that \(X_p\stackrel d=V X_q\) if and only if \(p\le q\). The unresolved source branch is \(0<p<q\), where one may take \(V=2^{1/p-1/q}W\), with \(W\) the ordinary size-biased version of \(S_{p/q}^{-1/q}\) and \(S_{p/q}\) positive \(p/q\)-stable. The \(p>q\) nonexistence branch is imported from the source.

## Dependencies

- [[wiki/nodes/O-DytsoBustinPoor-GeneralizedGaussian-ProductFactorization-source-gate|Dytso-Bustin-Poor generalized-Gaussian product factorization source gate]]
- [[wiki/nodes/D-GeneralizedGaussian-Np01|Generalized Gaussian source normalization]]
- [[wiki/nodes/L-PositiveStable-NegativeMoment|Positive stable negative moment formula]]
- [[wiki/nodes/D-InverseStable-SizeBiasFactor|Inverse stable power size-biased factor]]
- [[wiki/nodes/L-MellinQuotient-To-ProductFactor|Mellin quotient product-factor criterion]]

## Proof and provenance references

- `oracle/responses/OS-20260614T1240Z-oracle-response.md`
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

## Do not claim

- Do not count the source-proved \(p>q\) nonexistence branch as fresh.
- Do not claim positive-stable negative moments or size-biasing are new standalone theorems.
- Do not claim public APP registry assignment.
- Do not public-stage without user request.

## Tags

`application-candidate`, `generalized-gaussian`, `mellin-transform`, `open-problem-solved`, `positive-stable`, `product-factorization`, `proved`, `size-bias`, `source-solving`, `strict-private-plus10`, `theorem`, `true`
