---
id: "T-Szabo-psi-difference-alpha0-exact-one"
type: "theorem"
title: "Szabo psi difference exact alpha0 equals one"
status: "proved"
tags: ["application-bridge", "classification-theorem", "complete-monotonicity", "complete-monotonicity-criterion", "digamma", "exact-threshold-theorem", "proved", "szabo", "theorem"]
parents: ["T-Bernstein-derivative-complete-monotonicity-criterion", "D-Complete-monotonicity-Bernstein-Stieltjes-language"]
refs: ["attack-plans/AP-20260531T024200-szabo-alpha0-exact.json", "librarian/audits/LA-20260531T024200-szabo-alpha0-exact.json", "raw/source-cache/szabo-2411.17670/completethebib.tex", "raw/student/20260531T024200-szabo-alpha0-exact.md", "wiki/notes/frontier-szabo-alpha0-exact.md"]
---

# Theorem: Szabo psi difference exact alpha0 equals one

## Statement

For \(0<d<1\), the sharp cutoff for complete monotonicity of \(y^lpha[\psi(y+d)-\psi(y)-d/y]\) is \(lpha_0=1\).

## Dependencies

- [[wiki/nodes/T-Bernstein-derivative-complete-monotonicity-criterion|T-Bernstein-derivative-complete-monotonicity-criterion]]
- [[wiki/nodes/D-Complete-monotonicity-Bernstein-Stieltjes-language|Complete monotonicity, Bernstein, and Stieltjes language]]

## Proof and provenance references

- `attack-plans/AP-20260531T024200-szabo-alpha0-exact.json`
- `librarian/audits/LA-20260531T024200-szabo-alpha0-exact.json`
- `raw/source-cache/szabo-2411.17670/completethebib.tex`
- `raw/student/20260531T024200-szabo-alpha0-exact.md`
- `wiki/notes/frontier-szabo-alpha0-exact.md`

## Proof

Let \(0<d<1\), \(y>0\), and
\[
H_d(y)=\psi(y+d)-\psi(y)-\frac{d}{y}.
\]
Then
\[
y^\alpha H_d(y)
\]
is strictly completely monotone on \((0,\infty)\) if \(\alpha\le 1\), and is not completely monotone if \(\alpha>1\). Hence the sharp cutoff in Szabo Open Problem 1.5 is
\[
\alpha_0=1.
\]

As \(y\downarrow0\), the digamma Laurent expansion gives
\[
\psi(y)=-\frac1y-\gamma+O(y),
\qquad
\psi(y+d)=\psi(d)+O(y).
\]
Therefore
\[
H_d(y)=\psi(y+d)-\psi(y)-\frac{d}{y}
=\frac{1-d}{y}+O(1).
\]
Since \(0<d<1\), the leading coefficient is positive. Hence
\[
y^\alpha H_d(y)=(1-d)y^{\alpha-1}+O(y^\alpha).
\]
If \(\alpha>1\), then
\[
\frac{d}{dy}\left(y^\alpha H_d(y)\right)
=(1-d)(\alpha-1)y^{\alpha-2}+O(y^{\alpha-1})>0
\]
for all sufficiently small \(y>0\). A completely monotone function must be nonincreasing, so no \(\alpha>1\) can be completely monotone.

Combining this with the source-imported strict complete monotonicity for \(\alpha\le1\) proves \(\alpha_0=1\).

Szabo's original function is recovered by \(y=x+a\) and \(d=b-a\), where \(a\ge0\), \(b>0\), and \(0<b-a<1\). Translation from \((-a,\infty)\) to \((0,\infty)\) preserves complete-monotonicity sign tests.

_Proof source: `raw/student/20260531T024200-szabo-alpha0-exact.md`._

## Tags

`application-bridge`, `classification-theorem`, `complete-monotonicity`, `complete-monotonicity-criterion`, `digamma`, `exact-threshold-theorem`, `proved`, `szabo`, `theorem`
