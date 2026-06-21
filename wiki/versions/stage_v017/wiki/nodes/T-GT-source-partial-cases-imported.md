---
id: "T-GT-source-partial-cases-imported"
type: "theorem"
title: "Gomilko Tomilov source partial cases alpha <= one half and special BF"
status: "proved"
tags: ["bernstein-function", "gomilko-tomilov", "not-staging-application", "partial-case", "proved", "source-import", "theorem"]
parents: ["T-Complete-monotonicity-closure-calculus-principle", "D-Complete-monotonicity-Bernstein-Stieltjes-language"]
refs: ["private librarian audit", "private Oracle response", "private scout artifact", "wiki/notes/frontier-gt-bf-fractional-power-closure.md"]
---

# Theorem: Gomilko Tomilov source partial cases alpha <= one half and special BF

## Statement

Gomilko--Tomilov prove that \(\psi_\alpha(x)=[\psi(x^\alpha)]^{1/\alpha}\) is Bernstein for every \(\psi\in BF\) when \(0<\alpha\le1/2\), and for every \(0<\alpha<1\) when \(\psi\) is a special Bernstein function.

## Dependencies

- [[wiki/nodes/T-Complete-monotonicity-closure-calculus-principle|Complete-monotonicity closure calculus principle]]
- [[wiki/nodes/D-Complete-monotonicity-Bernstein-Stieltjes-language|Complete monotonicity, Bernstein, and Stieltjes language]]

## Proof and provenance references

- `private librarian audit`
- `private Oracle response`
- `private scout artifact`
- `wiki/notes/frontier-gt-bf-fractional-power-closure.md`

## Proof

The source asks whether, for every \(0<\alpha<1\),
\[
\psi\in BF \quad\Longrightarrow\quad [\psi(x^\alpha)]^{1/\alpha}\in BF.
\]
The source proves the implication for all Bernstein functions when \(0<\alpha\le 1/2\), and for all \(0<\alpha<1\) when \(\psi\) is special, i.e. \(x/\psi(x)\in BF\). The full \(1/2<\alpha<1\), non-special case remains open locally.

\[
\frac{x}{\psi(x)}=\prod_{j=1}^m f_j(x),
\qquad f_j\in BF,\quad f_j>0.
\]
For \(\psi_\alpha(x)=[\psi(x^\alpha)]^{1/\alpha}\),
\[
\psi_\alpha'(x)
=\psi'(x^\alpha)
\left(\frac{\psi(x^\alpha)}{x^\alpha}\right)^{1/\alpha-1}
=\psi'(x^\alpha)\prod_{j=1}^m f_j(x^\alpha)^{-(1/\alpha-1)}.
\]
The factor \(\psi'(x^\alpha)\) is completely monotone because \(\psi'\) is completely monotone and \(x^\alpha\) is Bernstein. For any positive Bernstein function \(g\) and \(\beta>0\), \(g^{-\beta}\) is completely monotone by the Laplace-gamma identity
\[
g(x)^{-\beta}
=\frac{1}{\Gamma(\beta)}
\int_0^\infty t^{\beta-1}e^{-t g(x)}\,dt
\]
and the fact that \(e^{-t g}\) is completely monotone. Products of completely monotone functions are completely monotone. Hence \(\psi_\alpha'\) is completely monotone and \(\psi_\alpha\in BF\).

This is not a full solution of the source problem. It is a reusable sufficient mechanism for non-special Bernstein functions whose reciprocal quotient \(x/\psi(x)\) is a finite product of Bernstein factors.

_Proof source: `wiki/notes/frontier-gt-bf-fractional-power-closure.md`._

## Tags

`bernstein-function`, `gomilko-tomilov`, `not-staging-application`, `partial-case`, `proved`, `source-import`, `theorem`
