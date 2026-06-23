---
id: "T-GT-BF-factorized-denominator-power-closure"
type: "theorem"
title: "Gomilko Tomilov finite Bernstein factor denominator fractional power closure subclass"
status: "proved"
tags: ["bernstein-function", "complete-monotonicity", "fractional-power", "gomilko-tomilov", "not-staging-application", "partial-source-answer", "proved", "theorem", "theory-growth"]
parents: ["T-Complete-monotonicity-closure-calculus-principle", "D-Complete-monotonicity-Bernstein-Stieltjes-language"]
refs: ["attack-plans/AP-20260531T114200-gt-bf-power-factor-subclass.json", "librarian/audits/LA-20260531T114200-gt-bf-factor-subclass.json", "oracle/responses/ORACLE-OS-20260531T-gt-bf-factor-subclass-oracle-response.md", "raw/scout/sources/gomilko-tomilov-bf-fractional-power-open.md", "raw/student/20260531T114200-gt-bf-factor-subclass.md", "wiki/notes/frontier-gt-bf-fractional-power-closure.md"]
---

# Theorem: Gomilko Tomilov finite Bernstein factor denominator fractional power closure subclass

## Statement

Let \(0<\alpha<1\), let \(\psi\in BF\), and suppose \(x/\psi(x)=\prod_{j=1}^m f_j(x)\), where every \(f_j\) is a positive Bernstein function on \((0,\infty)\). Then \(\psi_\alpha(x)=[\psi(x^\alpha)]^{1/\alpha}\) is a Bernstein function.

## Dependencies

- [[wiki/nodes/T-Complete-monotonicity-closure-calculus-principle|Complete-monotonicity closure calculus principle]]
- [[wiki/nodes/D-Complete-monotonicity-Bernstein-Stieltjes-language|Complete monotonicity, Bernstein, and Stieltjes language]]

## Proof and provenance references

- `attack-plans/AP-20260531T114200-gt-bf-power-factor-subclass.json`
- `librarian/audits/LA-20260531T114200-gt-bf-factor-subclass.json`
- `oracle/responses/ORACLE-OS-20260531T-gt-bf-factor-subclass-oracle-response.md`
- `raw/scout/sources/gomilko-tomilov-bf-fractional-power-open.md`
- `raw/student/20260531T114200-gt-bf-factor-subclass.md`
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

_Proof source: `raw/student/20260531T114200-gt-bf-factor-subclass.md`._

## Tags

`bernstein-function`, `complete-monotonicity`, `fractional-power`, `gomilko-tomilov`, `not-staging-application`, `partial-source-answer`, `proved`, `theorem`, `theory-growth`
