---
id: "T-Szabo-psi-shift-alpha-gt1-endpoint-obstruction"
type: "theorem"
title: "Szabo psi shift alpha greater than one endpoint obstruction"
status: "proved"
tags: ["complete-monotonicity", "digamma", "endpoint-asymptotic", "obstruction", "proved", "szabo", "theorem"]
parents: ["T-Complete-monotonicity-closure-calculus-principle", "D-Complete-monotonicity-Bernstein-Stieltjes-language", "D-Endpoint-obstruction-certificate-language"]
refs: ["attack-plans/AP-20260531T024200-szabo-alpha0-exact.json", "librarian/audits/LA-20260531T024200-szabo-alpha0-exact.json", "raw/student/20260531T024200-szabo-alpha0-exact.md", "wiki/notes/frontier-szabo-alpha0-exact.md"]
---

# Theorem: Szabo psi shift alpha greater than one endpoint obstruction

## Statement

For \(0<d<1\) and \(lpha>1\), \(y^lpha[\psi(y+d)-\psi(y)-d/y]\) has positive derivative near \(0^+\), so it is not completely monotone on \((0,\infty)\).

## Dependencies

- [[wiki/nodes/T-Complete-monotonicity-closure-calculus-principle|Complete-monotonicity closure calculus principle]]
- [[wiki/nodes/D-Complete-monotonicity-Bernstein-Stieltjes-language|Complete monotonicity, Bernstein, and Stieltjes language]]
- [[wiki/nodes/D-Endpoint-obstruction-certificate-language|Endpoint and pointwise obstruction certificates]]

## Proof and provenance references

- `attack-plans/AP-20260531T024200-szabo-alpha0-exact.json`
- `librarian/audits/LA-20260531T024200-szabo-alpha0-exact.json`
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

`complete-monotonicity`, `digamma`, `endpoint-asymptotic`, `obstruction`, `proved`, `szabo`, `theorem`
