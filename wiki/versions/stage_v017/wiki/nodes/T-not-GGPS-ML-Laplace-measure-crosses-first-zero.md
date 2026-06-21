---
id: "T-not-GGPS-ML-Laplace-measure-crosses-first-zero"
type: "theorem"
title: "GGPS Mittag Leffler reciprocal Laplace measure cannot cross first negative zero finite exponential moment obstruction"
status: "proved"
tags: ["complete-monotonicity", "endpoint-obstruction", "laplace-transform", "mittag-leffler", "primitive", "primitive-growth", "proved", "route-kill", "theorem", "true"]
parents: []
refs: ["private librarian audit", "private Oracle response", "private proof note", "wiki/notes/frontier-ggps-ml-reciprocal-cm-conjecture25.md"]
---

# Theorem: GGPS Mittag Leffler reciprocal Laplace measure cannot cross first negative zero finite exponential moment obstruction

## Statement

For the GGPS Mittag-Leffler reciprocal-complete-monotonicity route, if \(b<0\) is a real zero of \(E_{\alpha,\beta}\) and \(E_{\alpha,\beta}(x)>0\) immediately to the right of \(b\), then the Bernstein-Widder measure representing \(1/E_{\alpha,\beta}(x)\) on \((0,\infty)\) has infinite exponential moment at \(b\). Hence the positive Laplace representation cannot cross the first negative zero as a finite-measure analytic-continuation proof of Conjecture 25.

## Proof and provenance references

- `private librarian audit`
- `private Oracle response`
- `private proof note`
- `wiki/notes/frontier-ggps-ml-reciprocal-cm-conjecture25.md`

## Proof

For \(x>b\), \(e^{-xt}\uparrow e^{-bt}\) pointwise as \(x\downarrow b\). By monotone convergence,
\[
\lim_{x\downarrow b}\int_0^\infty e^{-xt}\,d\mu(t)=\int_0^\infty e^{-bt}\,d\mu(t).
\]
But \(E(b)=0\) and \(E(x)>0\) from the right, so \(F(x)=1/E(x)\to+\infty\). Hence the integral at \(b\) is infinite. This refutes the overstrong route that tried to solve the remaining compact left-half-plane region by extending the positive Laplace representation through the first negative zero.

If the global inequality holds and \(\zeta\) is a non-real zero of \(E\), then
\[
E(\operatorname{Re}\zeta)\le0.
\]

If \(E(\operatorname{Re}\zeta)>0\), then at \(z=\zeta\) the global inequality gives
\[
0=|E(\zeta)|\ge E(\operatorname{Re}\zeta)>0,
\]
a contradiction.

Assume the global inequality holds. If \(x\in\mathbb R\) satisfies \(E(x)>0\), then
\[
\Delta(x):=(E'(x))^2-E(x)E''(x)\ge0.
\]

Near \(y=0\), define
\[
H_x(y)=\log |E(x+iy)|-\log E(x).
\]
The global inequality gives \(H_x(y)\ge0\) and \(H_x(0)=0\). Thus \(H_x''(0)\ge0\). Since \(E(x)>0\),
\[
H_x''(0)=\left(\frac{E'(x)}{E(x)}\right)^2-\frac{E''(x)}{E(x)}
=\frac{(E'(x))^2-E(x)E''(x)}{E(x)^2}.
\]
Therefore \(\Delta(x)\ge0\).

Let \(G\) be a positive analytic function on the right half-plane, and suppose \(\phi=\log G\) is a complete Bernstein function with representation
\[
\phi(z)=a+bz+\int_0^\infty \frac{z}{z+t}\,d\nu(t),
\]
where \(b\ge0\) and \(\nu\) is a positive measure satisfying the usual integrability conditions. Then for \(x>0\) and \(y\in\mathbb R\),
\[
|G(x+iy)|\ge G(x).
\]

The affine term has real part \(a+bx\) at both \(x\) and \(x+iy\). For the kernel term, with \(A=x+t\),
\[
\operatorname{Re}\frac{x+iy}{x+t+iy}-\frac{x}{x+t}
=\frac{t y^2}{(x+t)((x+t)^2+y^2)}\ge0.
\]
Integrating gives
\[
\operatorname{Re}\phi(x+iy)-\phi(x)\ge0.
\]
Exponentiating proves \(|G(x+iy)|=\exp(\operatorname{Re}\phi(x+iy))\ge \exp(\phi(x))=G(x)\).

This lemma supports the source's Conjecture 26 terminology, but it is not a proof of Conjecture 25 in the rhomboid because the source reports that \(\log E_{\alpha,\beta}\) is not a complete Bernstein function there except in the degenerate exponential case.

_Proof source: `private proof note`._

## Tags

`complete-monotonicity`, `endpoint-obstruction`, `laplace-transform`, `mittag-leffler`, `primitive`, `primitive-growth`, `proved`, `route-kill`, `theorem`, `true`
