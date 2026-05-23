---
id: mrw-750fb7a7e30c
type: proposition
title: Robust corridor-overlap graphs have parity-consistent signatures
aliases: ["mrw-750fb7a7e30c", "Robust corridor-overlap graphs have parity-consistent signatures"]
status: proved
tags: [proposition, proved, erdos-536, squarefree-support, pair-link, complete-bipartite, nested-cores, signature-coherence, corridor-refinement, weighted-edge-bound, overlap-packing, parity-obstruction, cross-core-coherence, support-tail]
parents: [mrw-206678825c7a, mrw-36595780824f]
refs: []
  - raw/20260521T052939Z-erdos-536-robust-corridor-overlap-graphs-have-parity-consist.md
  - raw/20260521T052700Z-erdos536-corridor-family-overlap-defect.md
  - raw/20260521T053245Z-scout-forage-ingest.md
  - theory/forage/responses/20260521T052700Z-erdos536-corridor-family-overlap-defect-response.md
  - oracle/requests/20260521T052939Z-erdos536-overlap-parity-oracle-request.md
  - oracle/responses/20260521T052939Z-erdos536-overlap-parity-oracle-response.md
---

# Proposition: Robust corridor-overlap graphs have parity-consistent signatures

## Statement

Use the common ancestor-signature setting of [[mrw-206678825c7a]].  Thus all
corridors below use one finite vertex set \(V\), one nonnegative weight
function \(w\), one lower core \(Q\), and one common list of ancestor upper
complete-bipartite cuts, giving signature classes \(V_\tau\) with
\(\tau\in\{0,1\}^m\) and \(m\ge1\).

Let \(i\in I\) index a finite family of near-complete lower corridors
\[
U_i|W_i .
\]
For each \(i\), assume positive side masses
\[
A_i=w(U_i)>0,\qquad B_i=w(W_i)>0
\]
and a parameter \(1/2\le\lambda_i\le1\) such that
\[
M_Q(U_i,W_i)\ge \lambda_i A_iB_i .
\tag{1}
\]
Choose an ancestor signature \(\tau_i\) supplied by [[mrw-36595780824f]], so
that
\[
w(U_i\cap V_{\tau_i})\ge\lambda_iA_i,\qquad
w(W_i\cap V_{\bar\tau_i})\ge\lambda_iB_i .
\tag{2}
\]

Write the two oriented sides of corridor \(i\) as
\[
S_i^0=U_i,\qquad S_i^1=W_i,
\]
with side masses
\[
M_i^0=A_i,\qquad M_i^1=B_i
\]
and side defects
\[
D_i^0=(1-\lambda_i)A_i,\qquad
D_i^1=(1-\lambda_i)B_i.
\]
The selected pure signature of side \(S_i^b\) is
\[
\tau_i^b=
\begin{cases}
\tau_i,&b=0,\\
\bar\tau_i,&b=1.
\end{cases}
\]

Let \(H\) be a finite multigraph whose vertices lie in \(I\).  Each edge
\(e=ij\) of \(H\) is labelled by a pair of side bits
\[
(b_e,c_e)\in\{0,1\}^2,
\]
meaning that \(e\) tests the overlap \(S_i^{b_e}\cap S_j^{c_e}\).  Say that
\(e\) is robust if
\[
w(S_i^{b_e}\cap S_j^{c_e})
>
D_i^{b_e}+D_j^{c_e}.
\tag{3}
\]
Then every robust edge forces the parity relation
\[
\tau_j=
\begin{cases}
\tau_i,& b_e+c_e\equiv0\pmod2,\\
\bar\tau_i,& b_e+c_e\equiv1\pmod2.
\end{cases}
\tag{4}
\]

Consequently, if every edge of \(H\) is robust, then every cycle \(C\) of
\(H\) has even total side parity:
\[
\sum_{e\in C}(b_e+c_e)\equiv0\pmod2.
\tag{5}
\]
Equivalently, an odd-parity cycle cannot be fully robust.  For every cycle
\(C\) with
\[
\sum_{e\in C}(b_e+c_e)\equiv1\pmod2,
\]
there is an edge \(e=ij\in C\) for which
\[
w(S_i^{b_e}\cap S_j^{c_e})
\le
D_i^{b_e}+D_j^{c_e}.
\tag{6}
\]

In the complete case \(\lambda_i=1\) for all vertices of an odd-parity cycle,
at least one tested side overlap on that cycle has zero weight.

## Proof

Fix an edge \(e=ij\) with side label \((b,c)\).  By the side-overlap forms of
[[mrw-206678825c7a]], if the selected pure side signatures are incompatible,
\[
\tau_i^b\ne\tau_j^c,
\]
then
\[
w(S_i^b\cap S_j^c)\le D_i^b+D_j^c.
\tag{7}
\]
Thus the strict robustness condition (3) implies the contrapositive:
\[
\tau_i^b=\tau_j^c.
\tag{8}
\]
If \(b=c\), equality (8) says \(\tau_i=\tau_j\).  If \(b\ne c\), equality
(8) says \(\tau_j=\bar\tau_i\).  This proves (4).

Now assume every edge of a cycle
\[
i_0i_1,\ i_1i_2,\ldots,\ i_{r-1}i_0
\]
is robust.  Applying (4) along the cycle gives
\[
\tau_{i_{k+1}}
=
\operatorname{comp}^{p_k}(\tau_{i_k}),
\qquad
p_k=b_k+c_k\pmod2,
\]
where \(\operatorname{comp}\) denotes coordinatewise complement on
\(\{0,1\}^m\).  Composing around the cycle gives
\[
\tau_{i_0}
=
\operatorname{comp}^{p_0+\cdots+p_{r-1}}(\tau_{i_0}).
\tag{9}
\]
Since \(m\ge1\), no signature equals its coordinatewise complement.  Therefore
the exponent in (9) must be even, which proves (5).

The contrapositive of (5) gives the odd-cycle assertion: if a cycle has odd
total side parity, then not all of its edges are robust.  An edge that is not
robust is exactly an edge satisfying (6).

If all \(\lambda_i=1\) on the cycle, then every defect \(D_i^b\) on that
cycle is zero.  Inequality (6) then says that at least one tested side overlap
has weight zero.

## Depends on

- [[mrw-206678825c7a]] Incompatible near-pure inherited signatures have small side overlap
- [[mrw-36595780824f]] Near-complete lower corridors concentrate on one ancestor signature pair

## Used by

## Notes

- This proposition is a signed-graph consistency test for coherent
  signature-tree assemblies.  Robust same-side overlap edges impose equality
  of selected signatures; robust cross-side overlap edges impose
  complementarity.
- The theorem does not produce the corridor family.  It says that once a
  candidate global argument produces a side-overlap graph, every odd-parity
  cycle must pay at least one near-purity defect edge.
- No \(M_{P_k}(\theta)\), \(U_k(\theta)\), or \(R_P(\theta)\) vanishing theorem
  is claimed.
