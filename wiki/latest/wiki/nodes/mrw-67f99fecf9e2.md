---
id: mrw-67f99fecf9e2
type: proposition
title: Union-tilted boundary expansion and rank-layer obstruction
aliases: ["mrw-67f99fecf9e2", "Union-tilted boundary expansion and rank-layer obstruction"]
status: proved
tags: ["proposition", "proved", "erdos", "lcm", "squarefree", "biased-measure", "union-boundary", "lower-shadow", "rank-layer", "obstruction", "support-tail", "patch-gate-audited"]
parents: ["mrw-2a2c5551301e", "mrw-cc4f876149b7", "mrw-d0402aea6f58", "mrw-02dadc6b1bba", "mrw-3c39ca3d1973", "mrw-37dbc6aeedf9"]
refs: ["references/sources/20260519T093421Z-erdos-536-tilted-thinning-context.md"]
---

# Proposition: Union-tilted boundary expansion and rank-layer obstruction

## Statement

Let \(P\) be a finite set of primes and let \(\nu_P\) be the product law on
\(2^P\) with \(\nu_P(p\in A)=1/p\).  Let \(S_P=\sum_{p\in P}1/p\).  If
\(A,B\sim\nu_P\) are independent and \(C=A\cup B\), then \(C\) has the product
law \(\mu_P^\vee\) with
\[
\mu_P^\vee(p\in C)=\frac2p-\frac1{p^2}.
\]
For \(\mathcal G\subseteq2^P\), define the external incomparable-union boundary
\[
\partial^\vee\mathcal G
=
\{C\notin\mathcal G:\ \exists A,B\in\mathcal G,\ A\not\subseteq B,\ 
B\not\subseteq A,\ A\cup B=C\}.
\]
If \(\mathcal G\) is lower-shadow union-cover-free, then
\[
\nu_P(\mathcal G)^2
\le
2\prod_{p\in P}\left(1-\frac1p+\frac1{p^2}\right)
+
\mu_P^\vee(\partial^\vee\mathcal G)
\le
2e^{-S_P/2}+\mu_P^\vee(\partial^\vee\mathcal G).
\]
If \(\mathcal G=\mathcal F\cap H_{P,\theta}\), where
\(H_{P,\theta}=\{S: |S|>\theta S_P\}\), and \(\mathcal F\) is lower-shadow
union-cover-free, then
\[
\partial^\vee\mathcal G\subseteq H_{P,\theta}\setminus\mathcal F.
\]

However, global smallness of this external boundary is false.  For each \(r\),
the exact-rank layer
\[
\mathcal R_{P,r}=\{A\subseteq P:\ |A|=r\}
\]
is lower-shadow union-cover-free.  If \(P=P_k=\{p_1,\ldots,p_k\}\),
\(S_{P_k}\to\infty\), and
\[
r_k=\lceil(1+\varepsilon)S_{P_k}\rceil
\qquad(0<\varepsilon<1),
\]
then
\[
\mu_{P_k}^\vee(\partial^\vee\mathcal R_{P_k,r_k})\to1.
\]

## Proof

The coordinate law of \(C=A\cup B\) is independent across \(p\), and
\[
\Pr(p\in C)=1-\left(1-\frac1p\right)^2=\frac2p-\frac1{p^2}.
\]

Let \(\mathcal G\) be lower-shadow union-cover-free.  If
\(A,B\in\mathcal G\), then either \(A\subseteq B\), or \(B\subseteq A\), or
\(A\) and \(B\) are incomparable.  In the incomparable case set \(C=A\cup B\).
If \(C\in\mathcal G\), then \(A,B\subsetneq C\), \(A\ne B\), and
\(A\cup B=C\), contradicting lower-shadow union-cover-freeness.  Hence
\(C\in\partial^\vee\mathcal G\).  Therefore
\[
\nu_P(\mathcal G)^2
=
\Pr(A,B\in\mathcal G)
\le
\Pr(A\subseteq B)+\Pr(B\subseteq A)
+
\Pr(A\cup B\in\partial^\vee\mathcal G).
\]
Now
\[
\Pr(A\subseteq B)
=
\prod_{p\in P}\Pr(A_p\le B_p)
=
\prod_{p\in P}\left(1-\frac1p\left(1-\frac1p\right)\right)
=
\prod_{p\in P}\left(1-\frac1p+\frac1{p^2}\right),
\]
and the same formula holds for \(\Pr(B\subseteq A)\).  Since \(p\ge2\),
\[
\frac1p\left(1-\frac1p\right)\ge\frac1{2p},
\]
so the product is at most \(e^{-S_P/2}\).  This proves the boundary
inequality.

If \(\mathcal G=\mathcal F\cap H_{P,\theta}\), then the union of two members of
\(\mathcal G\) remains in \(H_{P,\theta}\).  The lower-shadow-free condition on
\(\mathcal F\) forbids the incomparable union from lying in \(\mathcal F\).
Thus every external incomparable-union boundary point lies in
\(H_{P,\theta}\setminus\mathcal F\).

For the rank-layer obstruction, \(\mathcal R_{P,r}\) is lower-shadow
union-cover-free because every proper subset of a rank-\(r\) set has rank
strictly less than \(r\).  If \(r<|C|\le2r\), then \(C\) is the union of two
distinct rank-\(r\) subsets of \(C\), and those two subsets are incomparable.
Therefore every such \(C\) belongs to
\(\partial^\vee\mathcal R_{P,r}\).

Under \(\mu_P^\vee\),
\[
\mathbb E|C|
=
\sum_{p\in P}\left(\frac2p-\frac1{p^2}\right)
=
2S_P-\sum_{p\in P}\frac1{p^2}
=
2S_P-O(1),
\]
and \(\operatorname{Var}(|C|)=O(S_P)\).  For
\(r_k=\lceil(1+\varepsilon)S_{P_k}\rceil\), the interval
\((r_k,2r_k]\) contains the mean with linear margins in \(S_{P_k}\).  Chebyshev's
inequality gives
\[
\mu_{P_k}^\vee(r_k<|C|\le2r_k)\to1,
\]
so \(\mu_{P_k}^\vee(\partial^\vee\mathcal R_{P_k,r_k})\to1\).

## Depends on

- [[mrw-cc4f876149b7]] and [[mrw-d0402aea6f58]] for the lower-shadow
  union-cover formulation.
- [[mrw-02dadc6b1bba]] for the earlier fact that rank-only high-support
  candidates have vanishing \(\nu_P\)-mass; the rank layers here obstruct only
  global boundary-smallness, not \(M_P(\theta)\to0\).

## Used by

- The next boundary-absorption target: prove that positive external boundary
  mass is either carried by rank-layer-like skeletons of vanishing \(\nu_P\)-mass
  or forces actual deletion-trace obstructions.

## Notes

- This proposition explains why a blanket theorem of the form "lower-shadow-free
  families have small tilted union boundary" is false.
- It does not refute the biased squarefree residual route.  The rank-layer
  obstruction is already quarantined under \(\nu_P\) by [[mrw-02dadc6b1bba]].
- The useful next theorem must be a boundary-absorption or structural
  decomposition result, not a boundary-smallness statement.
