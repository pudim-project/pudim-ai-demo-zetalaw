---
id: "T-Tsallis-alpha-2-noise-stability-CM"
type: "theorem"
title: "alpha two Tsallis entropy along heat flow has square derivative identity and CM signs"
status: "proved"
tags: ["attack-plan", "diagnostic", "heat-flow", "mixed", "noise-stability", "proved", "theorem", "tsallis"]
parents: ["D-Complete-monotonicity-Bernstein-Stieltjes-language", "T-Complete-monotonicity-closure-calculus-principle"]
refs: ["private librarian audit", "private proof note", "wiki/notes/frontier-renyi-tsallis-heat-flow-cm.md"]
---

# Theorem: alpha two Tsallis entropy along heat flow has square derivative identity and CM signs

## Statement

For a one-dimensional heat-flow density \(p(x,t)=T_t f(x)\), the order-two Tsallis entropy satisfies \(\partial_t^k\hat h_2(p)=(-1)^{k-1}\int (\partial_x^k p)^2\,dx\) for every \(k\ge1\), and therefore the order-two Tsallis entropy is completely monotone in the source convention.

## Dependencies

- [[wiki/nodes/D-Complete-monotonicity-Bernstein-Stieltjes-language|Complete monotonicity, Bernstein, and Stieltjes language]]
- [[wiki/nodes/T-Complete-monotonicity-closure-calculus-principle|Complete-monotonicity closure calculus principle]]

## Proof and provenance references

- `private librarian audit`
- `private proof note`
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

_Proof source: `private proof note`._

## Tags

`attack-plan`, `diagnostic`, `heat-flow`, `mixed`, `noise-stability`, `proved`, `theorem`, `tsallis`
