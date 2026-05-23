---
id: mrw-d602b51accb8
type: corollary
title: Triangle-free endpoint pair shields obey the fractional bipartite envelope
aliases: ["mrw-d602b51accb8", "Triangle-free endpoint pair shields obey the fractional bipartite envelope"]
status: proved
tags: [corollary, proved, erdos-536, squarefree-support, pair-link, endpoint-fiber, occupancy-pattern, interval-shield, triangle-free, weighted-motzkin-straus, fractional-bipartite-envelope, endpoint-pairs, diffuse-limit, terminal-residual, variational-residual, support-tail, cross-core-coherence]
parents: [mrw-1b04240e9886, mrw-3161f39fd270, mrw-50bca8113dbf, mrw-3d6bb8271a4c]
refs: []
  - raw/20260522T000926Z-erdos-536-triangle-free-endpoint-profile-residual.md
  - raw/20260522T000926Z-erdos536-triangle-free-endpoint-profile-residual.md
  - raw/20260522T001618Z-scout-forage-ingest.md
  - theory/forage/requests/20260522T000926Z-erdos536-triangle-free-endpoint-profile-residual-request.md
  - theory/forage/responses/20260522T000926Z-erdos536-triangle-free-endpoint-profile-residual-response.md
  - oracle/requests/20260522T000926Z-erdos536-triangle-free-endpoint-profile-residual-oracle-request.md
  - oracle/responses/20260522T000926Z-erdos536-triangle-free-endpoint-profile-residual-oracle-response.md
---

# Corollary: Triangle-free endpoint pair shields obey the fractional bipartite envelope

## Statement

Let \(B\) be a finite endpoint coordinate set with independent product weights
\(0<q_b<1\).  Put
\[
P_0(B)=\prod_{b\in B}(1-q_b),
\qquad
r_b=\frac{q_b}{1-q_b},
\qquad
R_B=\sum_{b\in B}r_b.
\]
Let \(G\) be a triangle-free graph on \(B\).  Then, for every terminal core
\(T\) disjoint from \(B\), the supported endpoint-pair residual satisfies
\[
\mathcal R_G(L)
=
P_0(B)
\left(\sum_{uv\in E(G)}r_ur_v\right)
\mathfrak M_T(L-2)
\le
\frac{P_0(B)R_B^2}{4}\mathfrak M_T(L-2).
\]

Consequently, if \(B_n\) is a sequence of endpoint sets with
\[
\delta_n=\max_{b\in B_n}q_b\to0,
\qquad
Q_n=\sum_{b\in B_n}q_b\to\alpha\in(0,\infty),
\]
then every triangle-free endpoint-pair shield on \(B_n\) satisfies
\[
\Pi_G(B_n)\le e^{-\alpha}\frac{\alpha^2}{4}+o(1).
\]
Balanced complete bipartite shields, with the endpoint odds mass split
asymptotically equally between the two classes, attain this envelope in the
diffuse limit; for instance one may take \(|X_n|=|Y_n|=m_n\) and
\(q_b=\alpha/(2m_n)\).  For \(h\ge2\), balanced \(C_{2h+1}\)-blow-ups from
`mrw-3161f39fd270` have limiting endpoint mass
\[
e^{-\alpha}\frac{\alpha^2}{2h+1},
\]
and hence endpoint-profile deficit
\[
e^{-\alpha}\alpha^2
\left(\frac14-\frac1{2h+1}\right)
\]
from the fractional bipartite envelope.  For \(C_5\), this deficit is
\[
e^{-\alpha}\frac{\alpha^2}{20}.
\]

This is a fractional endpoint-profile envelope.  It does not say that every
triangle-free endpoint graph is a single actual one-from-each subtower on the
same endpoint coordinates, and it does not prove terminal-core residual decay
or any \(R_P(\theta)\) lift.

The endpoint-factor bound is sharp.  Exact finite equality is achieved, for
example, by a complete bipartite graph \(K_{X,Y}\) whose two sides have equal
odds mass \(R_X=R_Y=R_B/2\).  Positive odds mass on vertices outside such a
balanced complete bipartite support, or missing positive-weight cross-edges,
gives strict endpoint-factor inequality.  Residual equality may still occur
degenerately when \(\mathfrak M_T(L-2)=0\).

## Proof

The exact residual identity is precisely `mrw-1b04240e9886`.  It remains to
bound the weighted edge sum
\[
W_G(r):=\sum_{uv\in E(G)}r_ur_v.
\]
If \(R_B=0\), then there is nothing to prove.  Otherwise set
\[
\xi_b=\frac{r_b}{R_B}.
\]
Then \(\xi_b\ge0\) and \(\sum_b\xi_b=1\).  It is enough to prove
\[
\sum_{uv\in E(G)}\xi_u\xi_v\le\frac14.
\]

We use the standard merging proof of the triangle-free Motzkin-Straus bound in
its global simplex form.  For any probability vector \(x\) on \(B\), define
\[
F(x)=\sum_{uv\in E(G)}x_ux_v
\]
on the probability simplex.  Among maximizers \(y\) of \(F\), choose one whose
positive support is minimal.  Suppose two positive-support vertices \(a\) and
\(b\) of \(y\) are nonadjacent.  With all other coordinates fixed and with
\(s=y_a+y_b\) fixed, the part of \(F\) depending on \(y_a,y_b\) is
\[
y_a c_a+y_b c_b,
\qquad
c_a=\sum_{u\in N(a)}y_u,\quad c_b=\sum_{u\in N(b)}y_u,
\]
because there is no \(ab\) edge.  This expression is affine in \(y_a\).  Moving
all of the mass \(s\) to whichever of \(a\) or \(b\) has the larger coefficient
does not decrease \(F\); if \(c_a=c_b\), either endpoint move preserves \(F\).
The move removes at least one positive coordinate, contradicting the minimality
of the positive support.

Thus the positive support of a minimal maximizer is a clique.  Since \(G\) is
triangle-free, that support has size at most two.  A probability vector
supported on one vertex has value \(0\), and a probability vector supported on
two adjacent vertices has value \(t(1-t)\le1/4\).  Therefore every probability
vector, including \(\xi\), satisfies
\[
\sum_{uv\in E(G)}\xi_u\xi_v\le\frac14.
\]
Multiplying by \(R_B^2\) gives
\[
W_G(r)\le\frac{R_B^2}{4},
\]
and the residual bound follows.

For the diffuse assertion, first
\[
\log P_0(B_n)
=
\sum_{b\in B_n}\log(1-q_b)
=
-Q_n+O\left(\sum_b q_b^2\right).
\]
Since
\[
\sum_bq_b^2\le \delta_nQ_n\to0,
\]
we get \(P_0(B_n)\to e^{-\alpha}\).  Also
\[
R_{B_n}
=
\sum_b\frac{q_b}{1-q_b}
=
\sum_bq_b+O\left(\sum_b q_b^2\right)
\to \alpha.
\]
Hence
\[
\frac{P_0(B_n)R_{B_n}^2}{4}
\to
e^{-\alpha}\frac{\alpha^2}{4}.
\]
The complete bipartite attainability is the balanced case of
`mrw-50bca8113dbf`, and the odd-cycle masses are exactly
`mrw-3161f39fd270`.  Subtracting
\[
e^{-\alpha}\frac{\alpha^2}{2h+1}
\]
from the envelope gives the displayed deficit, with the \(C_5\) deficit
\[
e^{-\alpha}\alpha^2\left(\frac14-\frac15\right)
=
e^{-\alpha}\frac{\alpha^2}{20}.
\]

## Depends on

- [[mrw-1b04240e9886]] Triangle-free endpoint pair shields carry positive diffuse residuals
- [[mrw-3161f39fd270]] Odd-cycle endpoint pair shields give non-bipartite diffuse residuals
- [[mrw-50bca8113dbf]] Bipartite endpoint pair shields are one-from-each subtower residuals
- [[mrw-3d6bb8271a4c]] Interval-shielded endpoint mixtures reduce to endpoint variational residuals

## Used by

## Notes

- This corollary controls every two-uniform interval-shielded endpoint profile
  by the fractional complete-bipartite envelope.  It is not a terminal theorem
  for Erdos 536 because the factor \(\mathfrak M_T(L-2)\) is still untouched.
- The result does not identify a non-bipartite triangle-free graph, such as a
  \(C_5\)-blow-up, with a single actual one-from-each tower.  It only says that
  its endpoint mass is no larger than the fractional bipartite envelope.
- Balanced odd cycles therefore form controlled lower envelopes inside the
  triangle-free branch, not a larger endpoint-profile obstruction than the
  complete bipartite tower.
- The next live target is no longer two-uniform endpoint mass alone.  Progress
  must use terminal-core residual decay, cross-fiber exclusions, or move to
  higher-uniformity shielded endpoint supports such as cancellative
  3-uniform families.
