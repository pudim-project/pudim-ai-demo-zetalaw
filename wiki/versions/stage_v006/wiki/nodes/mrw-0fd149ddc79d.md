---
id: mrw-0fd149ddc79d
type: theorem
title: APP-0009: Sharp threshold for reciprocal Gamma-product monotonicity
aliases: ["mrw-0fd149ddc79d", "Sharp threshold for reciprocal Gamma-product monotonicity", "APP-0009: Sharp threshold for reciprocal Gamma-product monotonicity"]
status: proved
tags: ["theorem", "proved", "gamma", "monotonicity", "sharp-threshold", "outside-route", "application", "app-0009", "source-grounded"]
parents: [mrw-1396775c6089]
refs: ["references/sources/20260518T153717Z-bulboaca-zayed-gamma-monotonicity.md"]
---

# Theorem: APP-0009: Sharp threshold for reciprocal Gamma-product monotonicity

## Statement

Let \(\psi=\Gamma'/\Gamma\), let \(\gamma\) be Euler's constant, and let \(\rho_*>0\) be the unique solution of
\[
\psi(1+\rho_*)=\gamma .
\]
For \(\rho>-1\), define
\[
\varphi_\rho(s)=\frac{1}{\Gamma(s+\rho)\Gamma(s)},\qquad s\ge 1.
\]
Then \(\varphi_\rho\) is strictly decreasing on \([1,\infty)\) if and only if
\[
\rho\ge \rho_*.
\]
Equivalently, \(W_\rho(s)=\Gamma(s+\rho)\Gamma(s)\) is strictly increasing on \([1,\infty)\) if and only if \(\rho\ge\rho_*\).  Numerically,
\[
\rho_*=1.2583969670859318174106234224981693941\ldots .
\]

More generally, let \(u:[1,\infty)\to(0,\infty)\) be differentiable and suppose
\[
J(s)=\frac{u'(s)}{u(s)}
\]
is nonincreasing on \([1,\infty)\).  Then
\[
\Phi_{\rho,u}(s)=\frac{u(s)}{\Gamma(s+\rho)\Gamma(s)}
\]
is strictly decreasing on \([1,\infty)\) if and only if
\[
\psi(1+\rho)\ge \gamma+J(1).
\]

## Proof

The digamma function is strictly increasing on \((0,\infty)\), since
\[
\psi'(x)=\sum_{k=0}^{\infty}\frac{1}{(x+k)^2}>0.
\]
Therefore the equation \(\psi(1+\rho)=\gamma\) has a unique solution \(\rho_*>0\).

For \(s\ge1\),
\[
\frac{d}{ds}\log W_\rho(s)=\psi(s+\rho)+\psi(s).
\]
The function
\[
g_\rho(s)=\psi(s+\rho)+\psi(s)
\]
is strictly increasing on \([1,\infty)\).  Its minimum is
\[
g_\rho(1)=\psi(1+\rho)+\psi(1)=\psi(1+\rho)-\gamma.
\]

If \(\rho\ge\rho_*\), then \(g_\rho(1)\ge0\), hence \(g_\rho(s)\ge0\) for \(s\ge1\), and \(g_\rho(s)>0\) for every \(s>1\).  Thus, for \(1\le a<b\),
\[
\log W_\rho(b)-\log W_\rho(a)=\int_a^b g_\rho(s)\,ds>0.
\]
So \(W_\rho\) is strictly increasing, and \(\varphi_\rho=1/W_\rho\) is strictly decreasing.

If \(\rho<\rho_*\), then \(g_\rho(1)<0\).  By continuity, \(g_\rho(s)<0\) on some interval \([1,1+\varepsilon)\).  Hence \(W_\rho\) decreases initially and \(\varphi_\rho\) increases initially, so the desired monotonicity fails.

This proves both necessity and sufficiency.

For the general statement, compute
\[
\frac{d}{ds}\log \Phi_{\rho,u}(s)
=J(s)-\psi(s+\rho)-\psi(s).
\]
The first term is nonincreasing by hypothesis, while \(\psi(s+\rho)+\psi(s)\) is strictly increasing.  Hence the maximum of this logarithmic derivative on \([1,\infty)\) is attained at \(s=1\), where it equals
\[
J(1)-\psi(1+\rho)-\psi(1)
=J(1)-\psi(1+\rho)+\gamma.
\]
Thus the logarithmic derivative is nonpositive everywhere, and negative except possibly at the left endpoint, exactly when \(\psi(1+\rho)\ge\gamma+J(1)\).  The same integral argument gives strict decrease.  If the inequality fails, the logarithmic derivative is positive near \(s=1\), so monotonicity fails.

## Depends on

- [[wiki/nodes/mrw-1396775c6089|Sharp reciprocal Gamma-product monotonicity threshold]]

## Used by

- [[wiki/nodes/mrw-0cb4eef49436|APP-0009 application record: sharp reciprocal Gamma-product monotonicity threshold]]
- [[wiki/nodes/mrw-6cd7f677ca40|Pointwise variational threshold for positive Gamma numerators]]
- [[wiki/nodes/mrw-82ac3282a187|Self-entropy Gamma-product threshold]]

## Notes

- This sharpens the source's sufficient condition for the base example by adding necessity and including the endpoint \(\rho=\rho_*\).
- The proof is local and uses only the standard positivity of \(\psi'\).
- The pointwise \(C^1\) threshold [[wiki/nodes/mrw-6cd7f677ca40|Pointwise variational threshold for positive Gamma numerators]] generalizes the same logarithmic-derivative comparison from endpoint-controlled \(J\) to a supremum over all \(s\ge1\).
- The self-entropy numerator theorem [[wiki/nodes/mrw-82ac3282a187|Self-entropy Gamma-product threshold]] extends the endpoint-control method to \(u(s)=e^{-cs}s^s\), where \(u'/u=\log s+1-c\) has derivative \(1/s\).
