---
id: mrw-ff32abc524eb
type: corollary
title: Finite separator iterations telescope
aliases: ["mrw-ff32abc524eb", "Finite separator iterations telescope"]
status: proved
tags: [corollary, proved, erdos-536, squarefree-support, endpoint-fiber, terminal-separator, separator-iteration, product-measure, telescoping, lower-light, upper-costly, terminal-residual, product-residual, route-quarantine, residual-obstruction]
parents: [mrw-789506d08385, mrw-58fd4a90babe]
refs: []
  - raw/20260523T054605Z-erdos-536-finite-separator-iteration.md
  - raw/20260523T054605Z-erdos536-finite-separator-iteration.md
  - raw/20260523T054605Z-scout-forage-ingest.md
  - theory/forage/requests/20260523T054605Z-erdos536-finite-separator-iteration-request.md
  - theory/forage/responses/20260523T054605Z-erdos536-finite-separator-iteration-response.md
  - oracle/requests/20260523T054605Z-erdos536-finite-separator-iteration-oracle-request.md
  - oracle/responses/20260523T054605Z-erdos536-finite-separator-iteration-oracle-response.md
---

# Corollary: Finite separator iterations telescope

## Statement
Let \(T_0\) be finite with product law \(\nu_{T_0}\) and coordinate
probabilities
\[
0<q_t<1.
\]
Let \(r\ge0\).  For \(1\le i\le r\), choose
\[
Z_i\subseteq T_{i-1},
\qquad
T_i=T_{i-1}\setminus Z_i.
\]
Each \(T_i\) carries the induced product law \(\nu_{T_i}\) with the original
coordinate probabilities \((q_t)_{t\in T_i}\).  Thus the separator blocks
\(Z_i\) are disjoint inside the original terminal core \(T_0\).

Set
\[
c_i=\prod_{z\in Z_i}(1-q_z),
\qquad
Q_i=\sum_{z\in Z_i}q_z,
\qquad
\Gamma_0=1,
\qquad
\Gamma_i=\prod_{j=1}^i c_j.
\]
For \(1\le i\le r\), define the first-hit layer
\[
E_i=
\{R\subseteq T_0:
R\cap Z_j=\emptyset\text{ for }j<i,\ R\cap Z_i\ne\emptyset\},
\]
and define the avoid-all residual
\[
U_r=
\{R\subseteq T_0:
R\cap Z_j=\emptyset\text{ for all }1\le j\le r\}.
\]
Then \(E_1,\ldots,E_r,U_r\) are disjoint and cover \(2^{T_0}\), and
\[
\nu_{T_0}(E_i)
=
\Gamma_{i-1}(1-c_i)
\le
\Gamma_{i-1}Q_i,
\]
while
\[
\nu_{T_0}(U_r)
=
\Gamma_r
\le
\exp\!\left(-\sum_{i=1}^r Q_i\right).
\]
Moreover,
\[
\sum_{i=1}^r\Gamma_{i-1}(1-c_i)=1-\Gamma_r.
\]

If \(\mathcal A_i\subseteq2^{T_{i-1}}\) is any lower branch whose members all
hit \(Z_i\), then for every real \(h\),
\[
\nu_{T_0}\!\left(
\{R:R\cap Z_j=\emptyset\ (j<i),\ R\cap T_{i-1}\in\mathcal A_i,\ |R|>h\}
\right)
\le
\Gamma_{i-1}(1-c_i)
\le
\Gamma_{i-1}Q_i.
\]
Equivalently, the exact factorization before applying the hit bound is
\[
\nu_{T_0}\!\left(
\{R:R\cap Z_j=\emptyset\ (j<i),\ R\cap T_{i-1}\in\mathcal A_i,\ |R|>h\}
\right)
=
\Gamma_{i-1}
\nu_{T_{i-1}}(\mathcal A_i\cap\{|W|>h\}).
\]

If \(\mathcal V_r\subseteq2^{T_r}\) is any final residual family, then for
every real \(h\),
\[
\nu_{T_0}\!\left(
\{R:R\cap Z_j=\emptyset\ (1\le j\le r),\
R\cap T_r\in\mathcal V_r,\ |R|>h\}
\right)
=
\Gamma_r\,\nu_{T_r}(\mathcal V_r\cap\{|W|>h\}).
\]
There is no support cutoff shift, because all removed separator coordinates
are required to be absent.

Consequently, finite separator iteration has two bookkeeping terms:
first-hit lower leakage
\[
\sum_{i=1}^r\Gamma_{i-1}(1-c_i),
\]
and final upper residual coefficient \(\Gamma_r\).  If the accumulated
separator intensity \(\sum_i Q_i\) is tiny, the first-hit leakage is tiny:
\[
\sum_{i=1}^r\Gamma_{i-1}(1-c_i)
\le
\sum_{i=1}^r\Gamma_{i-1}Q_i
\le
\sum_{i=1}^r Q_i.
\]
If instead \(\sum_i Q_i\ge L\), then
\[
\Gamma_r\le e^{-L}.
\]

## Proof
For any \(R\subseteq T_0\), either \(R\) avoids every separator block
\(Z_i\), in which case \(R\in U_r\), or there is a least \(i\) such that
\(R\cap Z_i\ne\emptyset\), in which case \(R\in E_i\).  The least index is
unique, so the layers and \(U_r\) are disjoint and exhaustive.

Because the \(Z_i\) are disjoint and the law is product,
\[
\nu_{T_0}(E_i)
=
\left(\prod_{j<i}c_j\right)(1-c_i)
=
\Gamma_{i-1}(1-c_i).
\]
The union bound gives
\[
1-c_i
=
\nu_{T_{i-1}}(W\cap Z_i\ne\emptyset)
\le
\sum_{z\in Z_i}q_z
=
Q_i,
\]
so \(\nu_{T_0}(E_i)\le\Gamma_{i-1}Q_i\).

Similarly,
\[
\nu_{T_0}(U_r)
=
\prod_{i=1}^r c_i
=
\Gamma_r.
\]
Since \(1-q_z\le e^{-q_z}\),
\[
\Gamma_r
\le
\exp\!\left(-\sum_{i=1}^r Q_i\right).
\]

The telescoping identity follows from
\[
\Gamma_{i-1}(1-c_i)=\Gamma_{i-1}-\Gamma_i.
\]
Summing over \(i\) gives
\[
\sum_{i=1}^r\Gamma_{i-1}(1-c_i)
=
1-\Gamma_r.
\]

For the lower-branch estimate, avoiding \(Z_1,\ldots,Z_{i-1}\) has probability
\(\Gamma_{i-1}\), and conditioned on that event the remaining random set on
\(T_{i-1}\) has law \(\nu_{T_{i-1}}\).  Hence the exact factorization is
\[
\Gamma_{i-1}
\nu_{T_{i-1}}(\mathcal A_i\cap\{|W|>h\}).
\]
Since every member of \(\mathcal A_i\) hits \(Z_i\),
\[
\nu_{T_{i-1}}(\mathcal A_i\cap\{|W|>h\})
\le
\nu_{T_{i-1}}(W\cap Z_i\ne\emptyset)
=
1-c_i
\le
Q_i.
\]

For the final residual, the event \(R\cap Z_i=\emptyset\) for all \(i\) has
probability \(\Gamma_r\).  On that event,
\[
R=R\cap T_r,
\qquad
|R|=|R\cap T_r|.
\]
Independence therefore gives
\[
\nu_{T_0}\!\left(
\{R:R\cap Z_j=\emptyset\ (1\le j\le r),\
R\cap T_r\in\mathcal V_r,\ |R|>h\}
\right)
=
\Gamma_r\,\nu_{T_r}(\mathcal V_r\cap\{|W|>h\}).
\]

## Depends on
- `mrw-789506d08385`: one separator branch is lower-light or upper-costly,
  with lower hit mass bounded by \(1-c(Z)\le Q(Z)\) and upper residual
  coefficient bounded by \(c(Z)\le e^{-Q(Z)}\).
- `mrw-58fd4a90babe`: terminal separators give the smaller-core product
  residual factorization with no support cutoff shift.

## Used by
- Future separator-chain arguments: any fixed finite separator chain is a
  first-hit filtration plus an avoid-all smaller-core residual.
- Future no-small-separator alternatives: persistent low-intensity chains must
  be classified as product residual structure, while large accumulated
  intensity forces exponential coefficient loss.

## Notes
- This is product-measure bookkeeping and route quarantine, not terminal
  Erdos 536 evidence.
- This proves a fixed finite separator-chain filtration.  A branching or
  adaptive separator tree would require applying the argument pathwise or
  proving a separate tree-indexed version.
- If \(r=0\), then \(T_r=T_0\), \(\Gamma_r=1\),
  \(U_0=2^{T_0}\), and there are no first-hit layers.  The telescoping identity
  reads \(0=1-\Gamma_0=0\), and the final residual identity is tautological.
- If \(Z_i=\emptyset\), then \(c_i=1\), \(Q_i=0\), and \(E_i=\emptyset\).  Any
  lower branch whose members hit \(Z_i\) is empty.
- Empty lower or final branches give zero contributions.
- If \(h<0\), the high-window cutoff is automatic.  If \(h\ge |T_0|\), all
  high-window events are empty.
- Endpoint weights are not part of this standalone corollary.  Endpoint-fiber
  applications multiply these terminal estimates by the relevant endpoint
  atom, and any later division requires that atom to be positive.
- Oracle accepted the corollary after adding the induced product-law
  convention, replacing individual small \(Q_i\) language by accumulated
  intensity, making \(r=0\) explicit, and adding the fixed-chain caveat.
  Scout returned only a scaffold response and was ingested raw-only.
