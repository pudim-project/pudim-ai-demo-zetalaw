---
id: "T-Tsallis2-heat-flow-entropy-derivative-CM"
type: "theorem"
title: "Tsallis 2 heat flow entropy derivative is completely monotone and increments are Bernstein"
status: "proved"
tags: ["bernstein-increment", "bridge-patch", "complete-monotonicity", "entropy", "heat-flow", "proved", "theorem", "tsallis"]
parents: ["D-Complete-monotonicity-Bernstein-Stieltjes-language", "T-Complete-monotonicity-closure-calculus-principle", "T-heat-flow-L2-energy-completely-monotone"]
refs: ["librarian/audits/LA-20260529T-next-loop-heat-flow-l2-student.json", "raw/student/20260529T-next-loop-heat-flow-l2.md", "wiki/notes/frontier-heat-flow-l2-spectral-laplace.md"]
---

# Theorem: Tsallis 2 heat flow entropy derivative is completely monotone and increments are Bernstein

## Statement

For \(S_2(t)=1-\int_{\mathbb R^d}(G_t*\mu)(x)^2\,dx\), the derivative \(S_2'(t)\) is completely monotone on \((0,\infty)\). Consequently each normalized increment \(S_2(t)-S_2(t_0)\), \(t\ge t_0>0\), is Bernstein on that half-line.

## Dependencies

- [[wiki/nodes/D-Complete-monotonicity-Bernstein-Stieltjes-language|Complete monotonicity, Bernstein, and Stieltjes language]]
- [[wiki/nodes/T-Complete-monotonicity-closure-calculus-principle|Complete-monotonicity closure calculus principle]]
- [[wiki/nodes/T-heat-flow-L2-energy-completely-monotone|heat flow L2 energy is completely monotone in heat time]]

## Proof and provenance references

- `librarian/audits/LA-20260529T-next-loop-heat-flow-l2-student.json`
- `raw/student/20260529T-next-loop-heat-flow-l2.md`
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

_Proof source: `raw/student/20260529T-next-loop-heat-flow-l2.md`._

## Tags

`bernstein-increment`, `bridge-patch`, `complete-monotonicity`, `entropy`, `heat-flow`, `proved`, `theorem`, `tsallis`
