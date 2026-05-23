---
id: mrw-0cb4eef49436
type: note
title: APP-0009 application record: sharp reciprocal Gamma-product monotonicity threshold
aliases: ["mrw-0cb4eef49436", "APP-0009 application record: sharp reciprocal Gamma-product monotonicity threshold"]
status: proved
tags: [note, proved, application, app-0009, gamma, monotonicity, sharp-threshold, source-grounded, outside-route, not-staged]
parents: [mrw-1396775c6089, mrw-0fd149ddc79d]
refs: ["references/sources/20260518T153717Z-bulboaca-zayed-gamma-monotonicity.md"]
  - raw/20260523T133726Z-app-0009-gamma-product-threshold-application.md
  - references/sources/20260518T153717Z-bulboaca-zayed-gamma-monotonicity.md
---

# Note: APP-0009 application record: sharp reciprocal Gamma-product monotonicity threshold

## Statement

`APP-0009` records the source-grounded application of the local Gamma/free-energy
calculus to the sharp reciprocal Gamma-product monotonicity threshold problem
from Bulboaca--Zayed 2026.

The external problem is the base sharp-constant question for
\[
\varphi_\rho(s)=\frac{1}{\Gamma(s+\rho)\Gamma(s)},\qquad s\ge1,
\]
equivalently for monotonicity of
\[
W_\rho(s)=\Gamma(s+\rho)\Gamma(s).
\]
The cited source proves strict decrease for \(\rho>\rho_*\), where
\[
\psi(1+\rho_*)=\gamma,
\]
and then states that finding the smallest positive \(\rho\)-values for the
examples is still an open problem.

The local solution is `mrw-0fd149ddc79d`: \(\varphi_\rho\) is strictly
decreasing on \([1,\infty)\) if and only if
\[
\rho\ge\rho_*.
\]
Thus the application closes the endpoint and necessity gap in the base
Bulboaca--Zayed example.  It also gives the general monotone-logarithmic-
derivative endpoint condition for
\[
\frac{u(s)}{\Gamma(s+\rho)\Gamma(s)}
\]
when \(u'/u\) is nonincreasing.

Application status: solved internally in `.math-wiki` and synthesized into
internal `THEORY_v006`; not public-staged, not pushed, and not sent to authors.

## Proof

The source-status part is recorded in
`references/sources/20260518T153717Z-bulboaca-zayed-gamma-monotonicity.md` and
raw log `raw/20260523T133726Z-app-0009-gamma-product-threshold-application.md`:
Bulboaca--Zayed prove a sufficient condition with the strict inequality
\(\rho>\rho_*\) and explicitly ask for the smallest positive values.

The mathematical solution is the proved theorem `mrw-0fd149ddc79d`.  Its proof
uses only the standard strict monotonicity of the digamma function,
\[
\psi'(x)=\sum_{n=0}^{\infty}\frac{1}{(x+n)^2}>0.
\]
For the base product
\[
W_\rho(s)=\Gamma(s+\rho)\Gamma(s),
\]
the logarithmic derivative is
\[
\frac{d}{ds}\log W_\rho(s)=\psi(s+\rho)+\psi(s).
\]
This is strictly increasing in \(s\), so its minimum on \([1,\infty)\) is
\[
\psi(1+\rho)+\psi(1)=\psi(1+\rho)-\gamma.
\]
Therefore \(W_\rho\) is strictly increasing on \([1,\infty)\), equivalently
\(\varphi_\rho=1/W_\rho\) is strictly decreasing, exactly when
\[
\psi(1+\rho)\ge\gamma.
\]
Since \(\psi\) is strictly increasing, this is equivalent to
\(\rho\ge\rho_*\).  If \(\rho<\rho_*\), the logarithmic derivative is negative
near \(s=1\), so \(W_\rho\) decreases initially and the desired monotonicity
fails.

This proves that the application is a solved source-grounded gap, not merely a
candidate.

## Depends on

- [[wiki/nodes/mrw-1396775c6089|Sharp reciprocal Gamma-product monotonicity threshold]]
- [[wiki/nodes/mrw-0fd149ddc79d|APP-0009: Sharp threshold for reciprocal Gamma-product monotonicity]]

## Used by

- Internal theory synthesis `THEORY_v006`.
- Future Publisher staging can promote this as public `APP-0009` once the user
  requests staging.

## Notes

- This application is independent of the Erdos #536 route.  It is a
  theory-growth yield from the Gamma/free-energy branch.
- The polynomial numerator thresholds mentioned in the same source remain only
  partially handled by `mrw-37311e7a5a0f` and `mrw-73218406186e`; `APP-0009`
  claims only the base sharp threshold and the monotone \(u'/u\) extension.
