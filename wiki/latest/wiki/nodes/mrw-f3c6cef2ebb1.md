---
id: mrw-f3c6cef2ebb1
type: theorem
title: Odd-order collapse for polygamma beta windows
aliases: ["mrw-f3c6cef2ebb1", "Odd-order collapse for polygamma beta windows"]
status: proved
tags: ["theorem", "proved", "polygamma", "beta-window", "open-problem-4", "qi-lim-nantomah", "odd-order", "hurwitz-zeta", "scout-audited", "source-grounded", "theory-growth"]
parents: [mrw-f0a031feea8e]
refs: ["theory/forage/inbox/20260523T153713Z-scout-forage-inbox.md", "references/sources/20260518T101945Z-qi-lim-nantomah-polygamma-open-problems.md"]
---

# Theorem: Odd-order collapse for polygamma beta windows

## Statement

For \(n\ge1\), define
\[
C_n(x)=\psi^{(n)}(x)+x\psi^{(n+1)}(x),
\qquad
P_n(x)=\psi^{(n)}(x)\psi^{(n)}(1/x),
\qquad x>0.
\]
Then
\[
(-1)^n C_n(x)>0\qquad(n\ge1,\ x>0).
\]
Consequently, if \(n\ge1\) is odd, then for every real \(\beta\) and every \(x>0\),
\[
x^\beta C_n(x)-P_n(x)<0.
\]
Thus the odd-order subfamily of the Qi--Lim--Nantomah higher-polygamma beta-window problem has admissible parameter range all of \(\mathbb R\).

## Proof

Use the standard polygamma expansion
\[
\psi^{(n)}(x)=(-1)^{n+1}n!\sum_{k=0}^{\infty}(x+k)^{-n-1}
\qquad(n\ge1,\ x>0).
\]
Put
\[
\Phi_n(x)=(-1)^{n+1}\psi^{(n)}(x)
=n!\sum_{k=0}^{\infty}(x+k)^{-n-1}>0.
\]
Then
\[
C_n(x)=(-1)^{n+1}\bigl(\Phi_n(x)-x\Phi_{n+1}(x)\bigr).
\]
It is enough to prove
\[
\Phi_n(x)<x\Phi_{n+1}(x).
\]

Let \(s=n+1\ge2\), and write
\[
Z_s(x)=\sum_{k=0}^{\infty}(x+k)^{-s}.
\]
The desired inequality is
\[
Z_s(x)<s x Z_{s+1}(x).
\]
Define a probability law on nonnegative integers by
\[
\Pr(K=k)=\frac{(x+k)^{-s-1}}{Z_{s+1}(x)}.
\]
Then
\[
\frac{Z_s(x)}{Z_{s+1}(x)}
=\mathbb E[x+K]
=x+\mathbb E K.
\]
By the tail-sum formula and the integral comparison for the decreasing function \(t\mapsto(x+t)^{-s-1}\),
\[
\begin{aligned}
\mathbb E K
&=\sum_{m=1}^{\infty}\Pr(K\ge m)\\
&=\frac1{Z_{s+1}(x)}
\sum_{m=1}^{\infty}\sum_{k=m}^{\infty}(x+k)^{-s-1}\\
&<
\frac1{Z_{s+1}(x)}
\sum_{m=1}^{\infty}\int_{m-1}^{\infty}(x+t)^{-s-1}\,dt\\
&=
\frac{Z_s(x)}{sZ_{s+1}(x)}
=\frac{x+\mathbb E K}{s}.
\end{aligned}
\]
Hence
\[
\mathbb E K<\frac{x}{s-1}.
\]
Since \(s\ge2\), this implies
\[
\mathbb E K<(s-1)x
\]
strictly.  Therefore
\[
\frac{Z_s(x)}{Z_{s+1}(x)}
=x+\mathbb E K
<sx,
\]
which proves \(Z_s(x)<s x Z_{s+1}(x)\), and hence \(\Phi_n(x)<x\Phi_{n+1}(x)\).  This gives
\[
(-1)^n C_n(x)>0.
\]

If \(n\) is odd, then \(\psi^{(n)}(x)>0\) for all \(x>0\), so
\[
P_n(x)=\psi^{(n)}(x)\psi^{(n)}(1/x)>0.
\]
The sign result gives \(C_n(x)<0\).  Since \(x^\beta>0\),
\[
x^\beta C_n(x)-P_n(x)
\]
is the sum of a strictly negative term and a strictly negative term.  It is therefore strictly negative for every \(x>0\) and every \(\beta\in\mathbb R\).  No parameter set can be larger than \(\mathbb R\), so the admissible range in the odd-order subfamily is all of \(\mathbb R\).

## Depends on

- [[wiki/nodes/mrw-f0a031feea8e|Higher-order monotonicity of polygamma products Pn]]

## Used by

- [[wiki/nodes/mrw-0241ab931d33|Even-order envelope reduction for polygamma beta windows]]
- [[wiki/nodes/mrw-201bbda2c917|Right endpoint theorem for even-order polygamma beta windows]]
- [[wiki/nodes/mrw-e497f41bfc07|Open Problem 4 reduction to the n=2 beta window]]

## Notes

- This theorem audits Scout Candidate 1 from `20260523T153713Z-scout-forage`.  Scout cited the Qi--Lim--Nantomah ratio theorem, but the local proof above avoids importing that theorem as a black box.
- The convention here is \(n\in\mathbb N=\{1,2,\ldots\}\).  The \(n=0\) beta-window is the separate reciprocal-digamma problem handled by [[wiki/nodes/mrw-0e9002ec3122|Pointwise reduction for reciprocal-digamma beta windows]] and [[wiki/nodes/mrw-ef08eba06fbe|Sign partition for reciprocal-digamma beta constraints]].
- The even-order case remains a genuine scalar-envelope problem because \(C_n(x)>0\) and \(P_n(x)>0\) when \(n\) is even.
- Together with the exact even-order theorem for \(n\ge4\), this leaves only the \(n=2\) case unresolved in Qi--Lim--Nantomah Open Problem 4; see [[wiki/nodes/mrw-e497f41bfc07|Open Problem 4 reduction to the n=2 beta window]].
