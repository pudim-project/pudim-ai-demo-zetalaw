---
id: mrw-6cd7f677ca40
type: proposition
title: Pointwise variational threshold for positive Gamma numerators
aliases: ["mrw-6cd7f677ca40", "Pointwise variational threshold for positive Gamma numerators", "Exact C1 Gamma numerator threshold"]
status: proved
tags: ["proposition", "proved", "gamma", "monotonicity", "sharp-threshold", "c1-numerator", "variational-threshold", "scout-audited", "theory-growth"]
parents: [mrw-1396775c6089, mrw-0fd149ddc79d, mrw-e0db175f66fc]
refs: []
---

# Proposition: Pointwise variational threshold for positive Gamma numerators

## Statement

Let \(u:[1,\infty)\to(0,\infty)\) be \(C^1\), and set
\[
J_u(s)=\frac{u'(s)}{u(s)}.
\]
For \(s\ge1\), define
\[
R_u(s)=\psi^{-1}\!\big(J_u(s)-\psi(s)\big)-s,
\qquad
\rho_u=\sup_{s\ge1}R_u(s)\in(-1,\infty],
\]
where \(\psi=\Gamma'/\Gamma\) and \(\psi^{-1}:\mathbb R\to(0,\infty)\) is the inverse of the strictly increasing digamma function.  For \(\rho>-1\), define
\[
\Phi_{\rho,u}(s)=\frac{u(s)}{\Gamma(s+\rho)\Gamma(s)}.
\]
Then \(\Phi_{\rho,u}\) is nonincreasing on \([1,\infty)\) if and only if
\[
\rho_u<\infty
\qquad\text{and}\qquad
\rho\ge\rho_u.
\]
If \(\rho>\rho_u\), then \(\Phi_{\rho,u}\) is strictly decreasing on \([1,\infty)\).  At the endpoint \(\rho=\rho_u<\infty\), it is strictly decreasing if and only if the contact set
\[
\{s\ge1:R_u(s)=\rho_u\}
\]
contains no nontrivial interval.

Equivalently, the general \(C^1\) numerator threshold gives an exact sharp set for weak monotonicity, while strict endpoint monotonicity requires excluding flat contact intervals.  This no-flat condition is automatic in the polynomial theorem [[wiki/nodes/mrw-e0db175f66fc|Variational threshold for admissible Gamma numerators]] by analyticity and the asymptotic mismatch.

## Proof

The digamma function is strictly increasing on \((0,\infty)\), since
\[
\psi'(x)=\sum_{k=0}^{\infty}\frac1{(x+k)^2}>0.
\]
Also \(\psi(x)\to-\infty\) as \(x\to0^+\) and \(\psi(x)\to\infty\) as \(x\to\infty\), so \(\psi^{-1}:\mathbb R\to(0,\infty)\) is well-defined.

For \(s\ge1\),
\[
\frac{d}{ds}\log\Phi_{\rho,u}(s)
=
J_u(s)-\psi(s+\rho)-\psi(s).
\]
At a fixed \(s\), this logarithmic derivative is nonpositive if and only if
\[
\psi(s+\rho)\ge J_u(s)-\psi(s).
\]
Since \(\psi\) is strictly increasing, this is equivalent to
\[
s+\rho\ge\psi^{-1}\!\big(J_u(s)-\psi(s)\big),
\]
and hence to
\[
\rho\ge R_u(s).
\]
Therefore the logarithmic derivative is nonpositive at every point of \([1,\infty)\) if and only if \(\rho\ge R_u(s)\) for every \(s\ge1\), i.e. if and only if \(\rho_u<\infty\) and \(\rho\ge\rho_u\).

If \(\rho<\rho_u\), or if \(\rho_u=\infty\), then some point \(s_*\ge1\) has \(\rho<R_u(s_*)\).  The logarithmic derivative is positive at \(s_*\), and by continuity \(\Phi_{\rho,u}\) increases on a nontrivial interval.  Thus nonincreasing monotonicity fails.  This proves the sharp weak-monotonicity criterion.

If \(\rho>\rho_u\), then \(\rho>R_u(s)\) for every \(s\ge1\), so the logarithmic derivative is strictly negative at every point and \(\Phi_{\rho,u}\) is strictly decreasing.

It remains to examine \(\rho=\rho_u<\infty\).  Then the logarithmic derivative is continuous and nonpositive.  It vanishes at \(s\) exactly when \(R_u(s)=\rho_u\).  If the contact set contains a nontrivial interval, then the logarithmic derivative vanishes throughout that interval and \(\Phi_{\rho,u}\) is constant there, so strict decrease fails.  Conversely, suppose the contact set contains no nontrivial interval.  For any \(1\le a<b\), the continuous nonpositive logarithmic derivative is not identically zero on \([a,b]\).  Hence
\[
\log\Phi_{\rho,u}(b)-\log\Phi_{\rho,u}(a)
=
\int_a^b
\bigl(J_u(s)-\psi(s+\rho)-\psi(s)\bigr)\,ds
<0.
\]
Thus \(\Phi_{\rho,u}(b)<\Phi_{\rho,u}(a)\) for every \(a<b\), proving strict decrease.

## Depends on

- [[wiki/nodes/mrw-1396775c6089|Sharp reciprocal Gamma-product monotonicity threshold]]
- [[wiki/nodes/mrw-0fd149ddc79d|APP-0009: Sharp threshold for reciprocal Gamma-product monotonicity]]
- [[wiki/nodes/mrw-e0db175f66fc|Variational threshold for admissible Gamma numerators]]

## Used by

## Notes

- This node audits Scout item `20260523T165716Z-scout-forage`, Candidate 1.  The promoted statement corrects the raw Scout endpoint claim by separating nonincreasing monotonicity from strict endpoint monotonicity.
- For arbitrary positive \(C^1\) numerators, the no-flat-contact condition cannot be omitted: one can prescribe \(J_u(s)=\psi(s+\rho)+\psi(s)\) on an interval, making \(\Phi_{\rho,u}\) locally constant at the endpoint threshold.
- The polynomial theorem [[wiki/nodes/mrw-e0db175f66fc|Variational threshold for admissible Gamma numerators]] remains stronger for admissible polynomial numerators because it proves finiteness, attainment, and strict endpoint decrease automatically.
- The self-entropy theorem [[wiki/nodes/mrw-82ac3282a187|Self-entropy Gamma-product threshold]] is a closed-form endpoint-controlled specialization with extra structure.
