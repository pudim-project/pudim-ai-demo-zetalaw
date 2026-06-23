---
id: "T-Szabo-psi-difference-alpha2-not-CM"
type: "theorem"
title: "Szabo psi difference endpoint alpha=2 is not completely monotone for all 0<d<1"
status: "proved"
tags: ["complete-monotonicity", "digamma", "laplace-obstruction", "partial", "proved", "szabo", "theorem"]
parents: ["T-Complete-monotonicity-closure-calculus-principle", "D-Complete-monotonicity-Bernstein-Stieltjes-language"]
refs: ["librarian/audits/LA-20260530T214500-szabo-psi-difference-alpha2-obstruction.json", "oracle/responses/ORACLE-FI-20260530T-elegance-039-oracle-forage-response.md", "raw/scout/FI-20260530T-elegance-039.md", "raw/student/20260530T214500-szabo-psi-difference-alpha2-obstruction.md", "wiki/notes/frontier-szabo-psi-difference-threshold.md"]
---

# Theorem: Szabo psi difference endpoint alpha=2 is not completely monotone for all 0<d<1

## Statement

For every \(0<d<1\), the function \(y\mapsto y^2\left[\psi(y+d)-\psi(y)-d/y\right]\) is not completely monotone on \((0,\infty)\).

## Dependencies

- [[wiki/nodes/T-Complete-monotonicity-closure-calculus-principle|Complete-monotonicity closure calculus principle]]
- [[wiki/nodes/D-Complete-monotonicity-Bernstein-Stieltjes-language|Complete monotonicity, Bernstein, and Stieltjes language]]

## Proof and provenance references

- `librarian/audits/LA-20260530T214500-szabo-psi-difference-alpha2-obstruction.json`
- `oracle/responses/ORACLE-FI-20260530T-elegance-039-oracle-forage-response.md`
- `raw/scout/FI-20260530T-elegance-039.md`
- `raw/student/20260530T214500-szabo-psi-difference-alpha2-obstruction.md`
- `wiki/notes/frontier-szabo-psi-difference-threshold.md`

## Proof

The standard digamma difference formula gives
\[
\psi(y+d)-\psi(y)=\int_0^\infty e^{-yt}\frac{1-e^{-dt}}{1-e^{-t}}\,dt
\]
and
\[
\frac{d}{y}=\int_0^\infty e^{-yt}d\,dt.
\]
Thus
\[
\phi_d(y)=\int_0^\infty e^{-yt}k_d(t)\,dt,\qquad
k_d(t)=\frac{1-e^{-dt}}{1-e^{-t}}-d.
\]
At the origin,
\[
k_d(t)=\frac{d(1-d)}2t+O(t^2),
\]
so \(k_d(0+)=0\) and \(k_d'(0+)=d(1-d)/2>0\).

In the sense of Laplace transforms of distributions,
\[
y^2\phi_d(y)
=\frac{d(1-d)}2+\int_0^\infty e^{-yt}k_d''(t)\,dt.
\]
Indeed, integrating by parts twice gives
\[
\mathcal L(k_d'')(y)=y^2\mathcal L(k_d)(y)-k_d'(0+),
\]
because \(k_d(0+)=0\).

As \(t\to\infty\),
\[
k_d(t)=1-d-e^{-dt}+O(e^{-t}),
\]
and hence
\[
k_d''(t)=-d^2e^{-dt}+O(e^{-t}).
\]
Since \(0<d<1\), the term \(e^{-dt}\) dominates \(e^{-t}\), so \(k_d''(t)<0\) for all sufficiently large \(t\).

If \(y^2\phi_d(y)\) were completely monotone on \((0,\infty)\), the Bernstein-Widder theorem would give a nonnegative representing measure. The inverse Laplace distribution computed above has an absolutely continuous tail with negative density, contradicting uniqueness of the Laplace transform. Therefore \(y^2\phi_d(y)\) is not completely monotone.

The shift \(y=x+a\) preserves the obstruction for the original function on \((-a,\infty)\): the representing distribution is multiplied by \(e^{-at}\), which does not change the eventual negative sign.

_Proof source: `raw/student/20260530T214500-szabo-psi-difference-alpha2-obstruction.md`._

## Tags

`complete-monotonicity`, `digamma`, `laplace-obstruction`, `partial`, `proved`, `szabo`, `theorem`
