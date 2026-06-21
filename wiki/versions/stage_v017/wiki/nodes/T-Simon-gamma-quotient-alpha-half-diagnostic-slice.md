---
id: "T-Simon-gamma-quotient-alpha-half-diagnostic-slice"
type: "theorem"
title: "Simon gamma quotient alpha half diagnostic slice is Bernstein"
status: "proved"
tags: ["bernstein", "diagnostic-slice", "gamma-quotient", "proved", "simon", "theorem"]
parents: ["T-Complete-monotonicity-closure-calculus-principle", "T-Simon-gamma-quotient-BF-alpha-window-open-problem", "D-Complete-monotonicity-Bernstein-Stieltjes-language"]
refs: ["private attack plan", "private librarian audit", "private Oracle response", "private proof note", "wiki/notes/frontier-simon-gamma-quotient-bernstein.md"]
---

# Theorem: Simon gamma quotient alpha half diagnostic slice is Bernstein

## Statement

The diagnostic slice \(F_{1/2}(x)=\Gamma(x+1/2)/(\Gamma(x)\sqrt{x})\) is a Bernstein function on \((0,\infty)\).

## Dependencies

- [[wiki/nodes/T-Complete-monotonicity-closure-calculus-principle|Complete-monotonicity closure calculus principle]]
- [[wiki/nodes/T-Simon-gamma-quotient-BF-alpha-window-open-problem|Simon gamma quotient is Bernstein for alpha in (0,1)]]
- [[wiki/nodes/D-Complete-monotonicity-Bernstein-Stieltjes-language|Complete monotonicity, Bernstein, and Stieltjes language]]

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

`bernstein`, `diagnostic-slice`, `gamma-quotient`, `proved`, `simon`, `theorem`
