---
id: "T-heat-flow-L2-spectral-Laplace-normal-form"
type: "theorem"
title: "heat flow L2 energy has Fourier spectral positive Laplace representation"
status: "proved"
tags: ["bridge-patch", "entropy", "forage", "heat-flow", "laplace-transform", "plancherel", "proved", "theorem"]
parents: ["D-Laplace-kernel-and-tilted-moment-language", "T-positive-Laplace-kernel-complete-monotonicity-principle"]
refs: ["private attack plan", "private librarian audit", "private Oracle artifact", "private proof note", "private scout response", "wiki/notes/frontier-heat-flow-l2-spectral-laplace.md"]
---

# Theorem: heat flow L2 energy has Fourier spectral positive Laplace representation

## Statement

Let \(\mu\) be a probability measure on \(\mathbb R^d\), let \(\widehat G_t(\xi)=e^{-t|\xi|^2}\), and put \(p_t=G_t*\mu\). Then \(N_2(t)=\int_{\mathbb R^d}p_t(x)^2\,dx\) has the spectral Laplace representation \(N_2(t)=\int_0^\infty e^{-2tr}\,d\nu_\mu(r)\), where \(\nu_\mu\) is the pushforward of \((2\pi)^{-d}|\widehat\mu(\xi)|^2\,d\xi\) under \(\xi\mapsto|\xi|^2\).

## Dependencies

- [[wiki/nodes/D-Laplace-kernel-and-tilted-moment-language|Laplace kernels and tilted moment ratios]]
- [[wiki/nodes/T-positive-Laplace-kernel-complete-monotonicity-principle|T-positive-Laplace-kernel-complete-monotonicity-principle]]

## Proof and provenance references

- `private attack plan`
- `private librarian audit`
- `private Oracle artifact`
- `private proof note`
- `private scout response`
- `wiki/notes/frontier-heat-flow-l2-spectral-laplace.md`

## Proof

Since \(|\widehat\mu(\xi)|\le1\), the function \(e^{-t|\xi|^2}\widehat\mu(\xi)\) is in \(L^2(\mathbb R^d)\) for every \(t>0\). Thus \(p_t\in L^2\), and Plancherel gives
\[
N_2(t)
=(2\pi)^{-d}\int_{\mathbb R^d}e^{-2t|\xi|^2}|\widehat\mu(\xi)|^2\,d\xi.
\]
Define \(\nu_\mu\) to be the locally finite positive pushforward of
\[
(2\pi)^{-d}|\widehat\mu(\xi)|^2\,d\xi
\]
under the map \(\xi\mapsto|\xi|^2\). Then
\[
N_2(t)=\int_0^\infty e^{-2tr}\,d\nu_\mu(r).
\]
The integral is finite for every \(t>0\), because \(|\widehat\mu|\le1\) and \(\int_{\mathbb R^d}e^{-2t|\xi|^2}\,d\xi<\infty\).

For \(k\ge0\), differentiation under the integral is justified at \(t>0\) by the Gaussian factor. It yields
\[
(-1)^kN_2^{(k)}(t)
=\int_0^\infty (2r)^k e^{-2tr}\,d\nu_\mu(r)\ge0.
\]
Therefore \(N_2\) is completely monotone.

Now \(S_2'(t)=-N_2'(t)\), and
\[
S_2'(t)=\int_0^\infty 2r e^{-2tr}\,d\nu_\mu(r),
\]
another positive Laplace transform. Hence \(S_2'\) is completely monotone. This implies that every normalized increment \(S_2(t)-S_2(t_0)\), \(t\ge t_0>0\), is a Bernstein function on that restricted half-line.

_Proof source: `private proof note`._

## Tags

`bridge-patch`, `entropy`, `forage`, `heat-flow`, `laplace-transform`, `plancherel`, `proved`, `theorem`
