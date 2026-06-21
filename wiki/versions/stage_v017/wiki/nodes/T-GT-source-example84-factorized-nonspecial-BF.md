---
id: "T-GT-source-example84-factorized-nonspecial-BF"
type: "theorem"
title: "Gomilko Tomilov Example 8.4 covered by finite factor denominator subclass"
status: "proved"
tags: ["bernstein-function", "gomilko-tomilov", "nonspecial", "not-staging-application", "proved", "source-example", "theorem"]
parents: ["T-GT-BF-factorized-denominator-power-closure", "T-Complete-monotonicity-closure-calculus-principle", "D-Complete-monotonicity-Bernstein-Stieltjes-language"]
refs: ["private librarian audit", "private Oracle response", "private scout artifact", "private proof note", "wiki/notes/frontier-gt-bf-fractional-power-closure.md"]
---

# Theorem: Gomilko Tomilov Example 8.4 covered by finite factor denominator subclass

## Statement

For the non-special source example \(\psi(x)=1-(1+x)^{-2}=x(2+x)/(1+x)^2\), the quotient \(x/\psi(x)=(1+x)(1+x)/(2+x)\) is a finite product of positive Bernstein functions, so \([\psi(x^\alpha)]^{1/\alpha}\in BF\) for every \(0<\alpha<1\).

## Dependencies

- [[wiki/nodes/T-GT-BF-factorized-denominator-power-closure|Gomilko Tomilov finite Bernstein factor denominator fractional power closure subclass]]
- [[wiki/nodes/T-Complete-monotonicity-closure-calculus-principle|Complete-monotonicity closure calculus principle]]
- [[wiki/nodes/D-Complete-monotonicity-Bernstein-Stieltjes-language|Complete monotonicity, Bernstein, and Stieltjes language]]

## Proof and provenance references

- `private librarian audit`
- `private Oracle response`
- `private scout artifact`
- `private proof note`
- `wiki/notes/frontier-gt-bf-fractional-power-closure.md`

## Proof

Put
\[
\beta=\frac1\alpha-1>0.
\]
For \(x>0\), direct differentiation gives
\[
\psi_\alpha'(x)
=x^{\alpha-1}\psi'(x^\alpha)\psi(x^\alpha)^{1/\alpha-1}
=\psi'(x^\alpha)\left(\frac{\psi(x^\alpha)}{x^\alpha}\right)^\beta.
\]
Using the factorization of \(x/\psi(x)\), this becomes
\[
\psi_\alpha'(x)
=\psi'(x^\alpha)\prod_{j=1}^m f_j(x^\alpha)^{-\beta}.
\]

Since \(\psi\in BF\), \(\psi'\) is completely monotone. Since \(x^\alpha\in BF\), composition closure gives \(\psi'(x^\alpha)\in CM\).

For each \(j\), \(g_j(x)=f_j(x^\alpha)\) is Bernstein by BF composition closure. If \(g\) is a positive Bernstein function and \(\beta>0\), then
\[
g(x)^{-\beta}
=\frac1{\Gamma(\beta)}
\int_0^\infty t^{\beta-1}e^{-t g(x)}\,dt.
\]
For each \(t>0\), \(e^{-t g(x)}\) is completely monotone because \(y\mapsto e^{-ty}\) is completely monotone and \(g\in BF\). Hence \(g^{-\beta}\in CM\). Therefore every \(f_j(x^\alpha)^{-\beta}\) is completely monotone.

Finite products of completely monotone functions are completely monotone, so \(\psi_\alpha'\in CM\). Also \(\psi_\alpha\ge0\). Thus \(\psi_\alpha\) is a Bernstein function.

The full source problem remains open locally in the arbitrary non-special case, especially \(1/2<\alpha<1\), when no finite Bernstein-factor representation of \(x/\psi(x)\) is known. The next loop should rotate or look for a genuinely broader structural theorem/counterexample, not repeat this finite-factor subclass.

_Proof source: `private proof note`._

## Tags

`bernstein-function`, `gomilko-tomilov`, `nonspecial`, `not-staging-application`, `proved`, `source-example`, `theorem`
