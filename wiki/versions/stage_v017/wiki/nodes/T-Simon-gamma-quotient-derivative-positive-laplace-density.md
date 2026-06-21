---
id: "T-Simon-gamma-quotient-derivative-positive-laplace-density"
type: "theorem"
title: "Simon gamma quotient derivative is CM with positive Laplace density"
status: "proved"
tags: ["bernstein", "gamma-quotient", "laplace-density", "proved", "simon", "source-solving-tool", "theorem"]
parents: ["T-Simon-gamma-quotient-complement-CM", "T-Simon-gamma-quotient-BF-alpha-window-open-problem", "T-Complete-monotonicity-closure-calculus-principle", "D-Complete-monotonicity-Bernstein-Stieltjes-language", "D-Laplace-kernel-and-tilted-moment-language"]
refs: ["private attack plan", "private librarian audit", "private Oracle response", "private proof note", "wiki/notes/frontier-simon-gamma-quotient-bernstein.md"]
---

# Theorem: Simon gamma quotient derivative is CM with positive Laplace density

## Statement

For every \(0<\alpha<1\), the derivative of \(F_\alpha(x)=\Gamma(x+\alpha)/(\Gamma(x)x^\alpha)\) is completely monotone, with a positive Laplace-density representation obtained from the decreasing kernel \(J_\alpha\).

## Dependencies

- [[wiki/nodes/T-Simon-gamma-quotient-complement-CM|Simon gamma quotient complement is CM for alpha in (0,1)]]
- [[wiki/nodes/T-Simon-gamma-quotient-BF-alpha-window-open-problem|Simon gamma quotient is Bernstein for alpha in (0,1)]]
- [[wiki/nodes/T-Complete-monotonicity-closure-calculus-principle|Complete-monotonicity closure calculus principle]]
- [[wiki/nodes/D-Complete-monotonicity-Bernstein-Stieltjes-language|Complete monotonicity, Bernstein, and Stieltjes language]]
- [[wiki/nodes/D-Laplace-kernel-and-tilted-moment-language|Laplace kernels and tilted moment ratios]]

## Proof and provenance references

- `private attack plan`
- `private librarian audit`
- `private Oracle response`
- `private proof note`
- `wiki/notes/frontier-simon-gamma-quotient-bernstein.md`

## Proof

Thomas Simon's 2020 paper reduces the Bernstein character of the moment sequence \((n!)^t\), for \(0<t<1\), to the Bernstein character of
\[
\Phi_t(\lambda)=\frac{\Gamma(1-t+\lambda)}{\lambda^{1-t}\Gamma(\lambda)}.
\]
Equivalently, with \(\alpha=1-t\),
\[
F_\alpha(x)=\frac{\Gamma(x+\alpha)}{\Gamma(x)x^\alpha},
\qquad 0<\alpha<1.
\]

The source records this as unanswered and notes that \(1/\Phi_t\) is logarithmically completely monotone, but that this is not sufficient for \(\Phi_t\) to be Bernstein.

Local partial result:
\[
\frac{d}{dx}\log F_\alpha(x)
=
\int_0^\infty e^{-xt}
\left(
\frac{1-e^{-\alpha t}}{1-e^{-t}}-\alpha
\right)\,dt,
\]

_Proof source: `wiki/notes/frontier-simon-gamma-quotient-bernstein.md`._

## Tags

`bernstein`, `gamma-quotient`, `laplace-density`, `proved`, `simon`, `source-solving-tool`, `theorem`
