---
id: "T-Tsallis-alpha-1-2-first-derivative-kernel"
type: "theorem"
title: "Tsallis alpha in (1,2) first entropy derivative has positive Laplace-kernel square-gradient representation"
status: "proved"
tags: ["first-derivative", "heat-flow", "positive-kernel", "proved", "theorem", "true-helper", "tsallis"]
parents: ["D-Laplace-kernel-and-tilted-moment-language", "T-positive-Laplace-kernel-complete-monotonicity-principle"]
refs: ["librarian/audits/LA-20260528T121500-tsallis-first-derivative-kernel.json", "raw/oracle/OS-20260528T120500-renyi-tsallis.md", "raw/student/20260528T120500-tsallis-alpha2-noise-stability.md", "wiki/notes/frontier-renyi-tsallis-heat-flow-cm.md"]
---

# Theorem: Tsallis alpha in (1,2) first entropy derivative has positive Laplace-kernel square-gradient representation

## Statement

For a one-dimensional positive heat-flow density \(p(x,t)=T_t f(x)\) and \(1<\alpha<2\), the first derivative of the Tsallis entropy has the positive-kernel representation \(\partial_t\hat h_\alpha(p)=\frac{\alpha}{2\Gamma(2-\alpha)}\int_0^\infty \lambda^{1-\alpha}\int e^{-\lambda p(x,t)}p_x(x,t)^2\,dx\,d\lambda\), equivalently \(\partial_t\hat h_\alpha(p)=\frac{2\alpha}{\Gamma(2-\alpha)}\int_0^\infty \lambda^{-1-\alpha}\|\partial_x e^{-\lambda p(\cdot,t)/2}\|_2^2\,d\lambda\).

## Dependencies

- [[wiki/nodes/D-Laplace-kernel-and-tilted-moment-language|Laplace kernels and tilted moment ratios]]
- [[wiki/nodes/T-positive-Laplace-kernel-complete-monotonicity-principle|T-positive-Laplace-kernel-complete-monotonicity-principle]]

## Proof and provenance references

- `librarian/audits/LA-20260528T121500-tsallis-first-derivative-kernel.json`
- `raw/oracle/OS-20260528T120500-renyi-tsallis.md`
- `raw/student/20260528T120500-tsallis-alpha2-noise-stability.md`
- `wiki/notes/frontier-renyi-tsallis-heat-flow-cm.md`

## Proof

Let \(p(x,t)=T_t f(x)\) be the one-dimensional heat-flow density with the source convention
\[
p_t=\frac12p_{xx}.
\]
Write
\[
p_m=\partial_x^m p.
\]
For \(t>0\), the Gaussian smoothing gives enough decay to integrate by parts without boundary terms in the following identities.

For \(\alpha=2\),
\[
\hat h_2(p)=\frac{1}{1-2}\left(\int p^2\,dx-1\right)
=1-\int p^2\,dx.
\]
The first derivative is
\[
\partial_t\hat h_2(p)
=-2\int pp_t\,dx
=-\int pp_{xx}\,dx
=\int p_x^2\,dx.
\]

Assume for some \(m\ge1\) that
\[
\partial_t^m\hat h_2(p)
=(-1)^{m-1}\int p_m^2\,dx.
\]
Then
\[
\begin{aligned}
\partial_t^{m+1}\hat h_2(p)
&=(-1)^{m-1}\int 2p_m(p_m)_t\,dx\\
&=(-1)^{m-1}\int p_m p_{m+2}\,dx\\
&=(-1)^m\int p_{m+1}^2\,dx.
\end{aligned}
\]
The induction gives
\[
\partial_t^k\hat h_2(p)
=(-1)^{k-1}\int (\partial_x^k p)^2\,dx
\]
for every \(k\ge1\). Therefore
\[
(-1)^{k-1}\partial_t^k\hat h_2(p)
=\int(\partial_x^kp)^2\,dx\ge0.
\]
This proves complete monotonicity in the source convention for the endpoint \(\alpha=2\).

The same helper has a direct positive Laplace form. With the Fourier convention suppressed into the measure constant, the heat semigroup gives
\[
\widehat{T_t f}(\xi)=e^{-t\xi^2/2}\hat f(\xi).
\]
Thus
\[
S_t^2(f)=\int (T_t f)^2\,dx
=\int_{\mathbb R}e^{-t\xi^2}\,|\hat f(\xi)|^2\,d\xi.
\]
Pushing the positive measure \(|\hat f(\xi)|^2\,d\xi\) forward by \(\lambda=\xi^2\) gives
\[
S_t^2(f)=\int_0^\infty e^{-t\lambda}\,d\mu_f(\lambda).
\]
Hence \(S_t^2\) is completely monotone in the ordinary Bernstein sense, and
\[
\hat h_2(p)=1-S_t^2(f)
\]
has the alternating derivative sign convention used by the entropy source.

This is the desired heat-flow analogue of the local entropy-defect Laplace bridge: the \(\alpha=2\) endpoint is controlled by a positive spectral measure. It does not extend to all \(\alpha\in(1,2)\) by itself, because \(\int p^\alpha\) is not a Hilbert-square norm except at \(\alpha=2\).

The bounded pass also gives one useful bridge for the open interval. For \(\alpha>1\),
\[
\hat h_\alpha(p)=\frac{1-\int p^\alpha\,dx}{\alpha-1}.
\]
Using \(p_t=\frac12p_{xx}\) and integrating by parts,
\[
\begin{aligned}
\partial_t\hat h_\alpha(p)
&=-\frac{\alpha}{\alpha-1}\int p^{\alpha-1}p_t\,dx\\
&=-\frac{\alpha}{2(\alpha-1)}\int p^{\alpha-1}p_{xx}\,dx\\
&=\frac{\alpha}{2}\int p^{\alpha-2}p_x^2\,dx.
\end{aligned}
\]
For \(1<\alpha<2\),
\[
p^{\alpha-2}=p^{-(2-\alpha)}
=\frac{1}{\Gamma(2-\alpha)}
\int_0^\infty \lambda^{1-\alpha}e^{-\lambda p}\,d\lambda.
\]
Therefore
\[
\partial_t\hat h_\alpha(p)
=\frac{\alpha}{2\Gamma(2-\alpha)}
\int_0^\infty \lambda^{1-\alpha}
\int e^{-\lambda p(x,t)}p_x(x,t)^2\,dx\,d\lambda.
\]
Equivalently, since
\[
\partial_x e^{-\lambda p/2}
=-\frac{\lambda}{2}e^{-\lambda p/2}p_x,
\]
we get
\[
\partial_t\hat h_\alpha(p)
=\frac{2\alpha}{\Gamma(2-\alpha)}
\int_0^\infty \lambda^{-1-\alpha}
\left\|\partial_x e^{-\lambda p(\cdot,t)/2}\right\|_2^2\,d\lambda.
\]
This proves a positive-kernel representation for the first time derivative on \(1<\alpha<2\). It does not prove complete monotonicity, because differentiating the kernel again introduces nonlinear heat-flow terms that are not sign-controlled by this argument.

_Proof source: `raw/student/20260528T120500-tsallis-alpha2-noise-stability.md`._

## Tags

`first-derivative`, `heat-flow`, `positive-kernel`, `proved`, `theorem`, `true-helper`, `tsallis`
