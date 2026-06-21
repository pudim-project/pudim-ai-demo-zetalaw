---
id: "T-Prabhakar-Q-density-mixture-formula"
type: "theorem"
title: "Prabhakar Q density is stable density mixture over Pollard density"
status: "proved"
tags: ["density-mixture", "mittag-leffler", "prabhakar", "proved", "stable-density", "theorem", "theory-growth"]
parents: ["T-positive-Laplace-kernel-complete-monotonicity-principle"]
refs: ["private librarian audit", "private Oracle response", "private proof note", "wiki/notes/frontier-prabhakar-q-stable-subordination.md"]
---

# Theorem: Prabhakar Q density is stable density mixture over Pollard density

## Statement

If the transform-normalized Pollard measure \(P^\gamma_{\alpha,\beta}\) has density \(p^\gamma_{\alpha,\beta}\) and \(S_\alpha\) has density \(f_\alpha\), then the non-atomic part of Sibisi's \(Q^\gamma_{\alpha,\beta}(\cdot\mid\lambda)\) has density \(q^\gamma_{\alpha,\beta}(t\mid\lambda)=\int_0^\infty (\lambda r)^{-1/\alpha}f_\alpha(t/(\lambda r)^{1/\alpha})p^\gamma_{\alpha,\beta}(r)\,dr\), with a matching pushed-forward atom at zero if \(P^\gamma_{\alpha,\beta}\) has one.

## Dependencies

- [[wiki/nodes/T-positive-Laplace-kernel-complete-monotonicity-principle|T-positive-Laplace-kernel-complete-monotonicity-principle]]

## Proof and provenance references

- `private librarian audit`
- `private Oracle response`
- `private proof note`
- `wiki/notes/frontier-prabhakar-q-stable-subordination.md`

## Proof

Let \(P\) be a finite positive measure on \([0,\infty)\), let
\[
F(u)=\int_0^\infty e^{-ur}\,dP(r),
\]
let \(0<\alpha<1\), \(\lambda>0\), and let \(S_\alpha\) be positive \(\alpha\)-stable:
\[
\mathbb E e^{-xS_\alpha}=e^{-x^\alpha}.
\]
Define a finite positive measure \(Q\) by
\[
Q(A)=\int_{[0,\infty)}
\Pr\{(\lambda r)^{1/\alpha}S_\alpha\in A\}\,dP(r).
\]
Then Tonelli's theorem gives, for \(x>0\),
\[
\int_0^\infty e^{-xt}\,dQ(t)
=\int_{[0,\infty)}
\mathbb E e^{-x(\lambda r)^{1/\alpha}S_\alpha}\,dP(r)
=\int_{[0,\infty)}e^{-\lambda r x^\alpha}\,dP(r)
=F(\lambda x^\alpha).
\]

Apply the lemma to Sibisi's transform-normalized \(P=P^\gamma_{\alpha,\beta}\) and
\[
F(u)=E^\gamma_{\alpha,\beta}(-u).
\]
For \(0<\alpha<1\), \(\gamma>0\), \(\beta>\alpha\gamma\), and \(\lambda>0\), set
\[
Q^\gamma_{\alpha,\beta}(A\mid\lambda)
=\int_{[0,\infty)}
\Pr\{(\lambda r)^{1/\alpha}S_\alpha\in A\}\,
dP^\gamma_{\alpha,\beta}(r).
\]
Then
\[
\int_0^\infty e^{-xt}\,dQ^\gamma_{\alpha,\beta}(t\mid\lambda)
=E^\gamma_{\alpha,\beta}(-\lambda x^\alpha).
\]
By uniqueness of finite Laplace transforms, this is Sibisi's \(Q^\gamma_{\alpha,\beta}(\cdot\mid\lambda)\).

If \(S_\alpha\) has density \(f_\alpha\), then the non-atomic density part is
\[
q^\gamma_{\alpha,\beta}(t\mid\lambda)
=\int_{(0,\infty)}
(\lambda r)^{-1/\alpha}
f_\alpha\!\left(\frac{t}{(\lambda r)^{1/\alpha}}\right)
dP^\gamma_{\alpha,\beta}(r),
\]
with an atom \(P^\gamma_{\alpha,\beta}(\{0\})\delta_0\) if \(P^\gamma_{\alpha,\beta}\) has an atom at zero. When \(P^\gamma_{\alpha,\beta}\) is represented by Sibisi's Pollard density \(p^\gamma_{\alpha,\beta}(r)\), this becomes
\[
q^\gamma_{\alpha,\beta}(t\mid\lambda)
=\int_0^\infty
(\lambda r)^{-1/\alpha}
f_\alpha\!\left(\frac{t}{(\lambda r)^{1/\alpha}}\right)
p^\gamma_{\alpha,\beta}(r)\,dr.
\]

Because
\[
E^\gamma_{\alpha,\beta}(0)=\frac1{\Gamma(\beta)},
\]
the representing measures \(P^\gamma_{\alpha,\beta}\) and \(Q^\gamma_{\alpha,\beta}(\cdot\mid\lambda)\) have total mass \(1/\Gamma(\beta)\). They are finite positive measures, not generally probability measures. The normalized probability version is
\[
\widehat Q^\gamma_{\alpha,\beta}=\Gamma(\beta)Q^\gamma_{\alpha,\beta},
\qquad
\mathcal L\widehat Q^\gamma_{\alpha,\beta}(x)
=\Gamma(\beta)E^\gamma_{\alpha,\beta}(-\lambda x^\alpha).
\]

The boundary \(\beta=\alpha\gamma\) is not included here because Sibisi's ordinary convolution density uses \(1/\Gamma(\beta-\alpha\gamma)\). A limiting treatment is a separate open frontier.

_Proof source: `private proof note`._

## Tags

`density-mixture`, `mittag-leffler`, `prabhakar`, `proved`, `stable-density`, `theorem`, `theory-growth`
