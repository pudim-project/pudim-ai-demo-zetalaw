---
id: mrw-e0db175f66fc
type: theorem
title: Variational threshold for admissible Gamma numerators
aliases: ["mrw-e0db175f66fc", "Variational threshold for admissible Gamma numerators"]
status: proved
tags: ["theorem", "proved", "gamma", "monotonicity", "sharp-threshold", "polynomial", "admissible-numerator", "variational-threshold", "scout-audited", "source-grounded", "theory-growth"]
parents: [mrw-1396775c6089, mrw-0fd149ddc79d, mrw-37311e7a5a0f]
refs: ["theory/forage/inbox/20260523T151043Z-scout-forage-inbox.md", "references/sources/20260518T153717Z-bulboaca-zayed-gamma-monotonicity.md"]
---

# Theorem: Variational threshold for admissible Gamma numerators

## Statement

Call a real polynomial \(u\) an admissible Gamma numerator if
\[
u(s)>0\qquad (s\ge1).
\]
For such \(u\), define
\[
J_u(s)=\frac{u'(s)}{u(s)},\qquad
R_u(s)=\psi^{-1}\!\big(J_u(s)-\psi(s)\big)-s,
\qquad s\ge1,
\]
where \(\psi=\Gamma'/\Gamma\) and \(\psi^{-1}:\mathbb R\to(0,\infty)\) is the inverse of the strictly increasing digamma function.  Set
\[
\rho_u=\max_{s\ge1}R_u(s).
\]
Then \(\rho_u\) is finite and attained.  For every \(\rho>-1\), the function
\[
\Phi_{\rho,u}(s)=\frac{u(s)}{\Gamma(s+\rho)\Gamma(s)}
\]
is strictly decreasing on \([1,\infty)\) if and only if
\[
\rho\ge\rho_u.
\]

In particular, every polynomial numerator family that is positive on \([1,\infty)\) has an exact sharp Gamma-product monotonicity threshold in this variational form.  The earlier theorem [[wiki/nodes/mrw-37311e7a5a0f|Variational sharp threshold for polynomial Gamma-product monotonicity]] is the specialization \(u(s)=s^m+1\).

## Proof

Since \(u(s)>0\) on \([1,\infty)\), the logarithmic derivative \(J_u\) is continuous on \([1,\infty)\).  If \(d=\deg u\), then
\[
J_u(s)=\frac{d}{s}+O(s^{-2})
\qquad (s\to\infty),
\]
while
\[
\psi(s)=\log s+O(s^{-1}).
\]
Therefore
\[
J_u(s)-\psi(s)\to-\infty.
\]
Since \(\psi^{-1}(y)\to0^+\) as \(y\to-\infty\), it follows that
\[
R_u(s)=\psi^{-1}\!\big(J_u(s)-\psi(s)\big)-s\to-\infty.
\]
By continuity, \(R_u\) attains a finite maximum on \([1,\infty)\).

For \(s\ge1\), the logarithmic derivative of \(\Phi_{\rho,u}\) is
\[
\frac{d}{ds}\log\Phi_{\rho,u}(s)
=
J_u(s)-\psi(s+\rho)-\psi(s).
\]
Because \(\psi\) is strictly increasing on \((0,\infty)\), this derivative is nonpositive at a given \(s\) if and only if
\[
\psi(s+\rho)\ge J_u(s)-\psi(s),
\]
which is equivalent to
\[
s+\rho\ge\psi^{-1}\!\big(J_u(s)-\psi(s)\big),
\]
and hence to
\[
\rho\ge R_u(s).
\]
Thus the logarithmic derivative is nonpositive for every \(s\ge1\) if and only if \(\rho\ge\rho_u\).

If \(\rho<\rho_u\), then \(\rho<R_u(s_*)\) for some \(s_*\ge1\), so the logarithmic derivative is positive at \(s_*\).  By continuity, \(\Phi_{\rho,u}\) increases on a nontrivial interval and is not decreasing on \([1,\infty)\).

It remains to prove strict decrease when \(\rho\ge\rho_u\).  In this case the logarithmic derivative is everywhere nonpositive.  If \(\Phi_{\rho,u}\) were constant on a nontrivial interval, then
\[
J_u(s)=\psi(s+\rho)+\psi(s)
\]
on that interval.  Both sides are real analytic on \((1,\infty)\), so the equality would hold throughout \((1,\infty)\).  But as \(s\to\infty\), the left side is \(O(1/s)\), whereas
\[
\psi(s+\rho)+\psi(s)=2\log s+o(\log s),
\]
a contradiction.  Hence the logarithmic derivative cannot vanish on any nontrivial interval.  Its integral over every nondegenerate interval is strictly negative, so \(\Phi_{\rho,u}\) is strictly decreasing.

## Depends on

- [[wiki/nodes/mrw-1396775c6089|Sharp reciprocal Gamma-product monotonicity threshold]]
- [[wiki/nodes/mrw-0fd149ddc79d|APP-0009: Sharp threshold for reciprocal Gamma-product monotonicity]]
- [[wiki/nodes/mrw-37311e7a5a0f|Variational sharp threshold for polynomial Gamma-product monotonicity]]

## Used by

- [[wiki/nodes/mrw-6cd7f677ca40|Pointwise variational threshold for positive Gamma numerators]]
- [[wiki/nodes/mrw-82ac3282a187|Self-entropy Gamma-product threshold]]

## Notes

- This theorem was suggested by Scout item `20260523T151043Z-scout-forage` and promoted only after Advisor local audit.
- The positivity hypothesis \(u(s)>0\) on \([1,\infty)\) is essential for the quotient to be positive-valued and for \(J_u\) to be a real continuous logarithmic derivative on the whole interval.
- The theorem gives an exact variational threshold, not a closed-form evaluation.  Localization and asymptotic analysis of the maximizers of \(R_u\) remain separate structural problems.
- The later \(C^1\) pointwise threshold [[wiki/nodes/mrw-6cd7f677ca40|Pointwise variational threshold for positive Gamma numerators]] removes the polynomial hypothesis for weak monotonicity, but must add an explicit no-flat-contact condition for strict endpoint monotonicity.
- The self-entropy numerator \(u(s)=e^{-cs}s^s\) is not polynomial, but [[wiki/nodes/mrw-82ac3282a187|Self-entropy Gamma-product threshold]] gives a closed endpoint threshold because \(d(u'/u)/ds=1/s\) is exactly dominated by \(\psi'(s)\).
