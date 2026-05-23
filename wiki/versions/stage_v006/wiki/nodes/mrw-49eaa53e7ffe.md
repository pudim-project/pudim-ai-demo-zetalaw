---
id: mrw-49eaa53e7ffe
type: proposition
title: Complete lower corridors inherit ancestor signatures
aliases: ["mrw-49eaa53e7ffe", "Complete lower corridors inherit ancestor signatures"]
status: proved
tags: [proposition, proved, erdos-536, squarefree-support, pair-link, complete-bipartite, nested-cores, signature-coherence, corridor-refinement, cross-core-coherence, support-tail]
parents: [mrw-fced7420b905]
refs: []
  - raw/20260521T033055Z-erdos-536-complete-coherent-corridors-inherit-ancestor-signa.md
  - raw/20260521T032658Z-erdos536-coherent-corridor-assembly.md
  - raw/20260521T033648Z-scout-forage-ingest.md
  - theory/forage/responses/20260521T032658Z-erdos536-coherent-corridor-assembly-response.md
  - oracle/requests/20260521T033055Z-erdos536-ancestor-signature-purity-oracle-request.md
  - oracle/responses/20260521T033055Z-erdos536-ancestor-signature-purity-oracle-response.md
---

# Proposition: Complete lower corridors inherit ancestor signatures

## Statement

Let \(P\) be a finite set and let \(\mathcal F\subseteq 2^P\) be
pair-link-free.  For \(R\subseteq P\), write
\[
G_R^\mathcal F=(P\setminus R,E_R^\mathcal F),
\qquad
\{x,y\}\in E_R^\mathcal F
\Longleftrightarrow
R\cup\{x,y\}\in\mathcal F .
\]

Let \(m\ge1\), and let \(Q\subseteq R_i\subseteq P\) for \(1\le i\le m\).  Let
\(V\subseteq P\setminus\bigcup_i R_i\), and suppose that for each \(i\) the
upper slice graph \(G_{R_i}^\mathcal F\) contains a nondegenerate complete
bipartite graph
\[
K_{X_i,Y_i}
\qquad\text{on}\qquad
V=X_i\sqcup Y_i .
\]
For \(v\in V\), define the ancestor signature
\[
\sigma(v)=(\mathbf 1_{v\in X_i})_{i=1}^m\in\{0,1\}^m .
\]

If \(U,W\subseteq V\) are nonempty disjoint sets and the lower slice contains
the complete bipartite graph \(K_{U,W}\), meaning
\[
\{u,w\}\in E_Q^\mathcal F
\qquad
\text{for every }u\in U,\ w\in W,
\]
then there is a signature \(\tau\in\{0,1\}^m\) such that
\[
U\subseteq V_\tau,
\qquad
W\subseteq V_{\mathbf 1-\tau},
\]
where \(V_\eta=\{v\in V:\sigma(v)=\eta\}\).

Consequently, a complete lower corridor cannot have positive support spread
over two ancestor signatures on either side.  In weighted form, if weights
\(a_u,b_w\ge0\) on \(U,W\) have positive side masses and
\[
\sum_{\substack{u\in U,\ w\in W\\ \{u,w\}\in E_Q^\mathcal F}} a_u b_w
=
\left(\sum_{u\in U}a_u\right)
\left(\sum_{w\in W}b_w\right),
\]
then the positive-weight support in \(U\) lies in one ancestor signature class
and the positive-weight support in \(W\) lies in its complementary class.

## Proof

By [[mrw-fced7420b905]], every lower edge
\(\{x,y\}\in E_Q^\mathcal F\cap\binom V2\) joins complementary ancestor
signatures:
\[
\sigma(x)=\mathbf 1-\sigma(y).
\tag{1}
\]

Choose \(u_0\in U\) and \(w_0\in W\).  Since \(K_{U,W}\subseteq G_Q^\mathcal F\),
the edge \(\{u_0,w\}\) lies in \(E_Q^\mathcal F\) for every \(w\in W\).  Applying
(1) gives
\[
\sigma(w)=\mathbf 1-\sigma(u_0)
\qquad(w\in W).
\]
Thus all vertices of \(W\) have the same ancestor signature.  Similarly, the
edge \(\{u,w_0\}\) lies in \(E_Q^\mathcal F\) for every \(u\in U\), so
\[
\sigma(u)=\mathbf 1-\sigma(w_0)=\sigma(u_0)
\qquad(u\in U).
\]
Taking \(\tau=\sigma(u_0)\) proves
\[
U\subseteq V_\tau,
\qquad
W\subseteq V_{\mathbf 1-\tau}.
\]

For the weighted assertion, let
\[
U^+=\{u\in U:a_u>0\},
\qquad
W^+=\{w\in W:b_w>0\}.
\]
If some pair \(u\in U^+\), \(w\in W^+\) were missing from \(E_Q^\mathcal F\),
the displayed edge-mass identity would lose the positive product \(a_ub_w\).
Hence \(K_{U^+,W^+}\subseteq G_Q^\mathcal F\), and the unweighted conclusion
applies to \(U^+,W^+\).

## Depends on

- [[mrw-fced7420b905]] Nested path-shadow coherence for bipartite slice blocks

## Used by

## Notes

- This is a global-assembly constraint to use with the equality/complete-corridor case
  of [[mrw-827094b15843]].  That earlier normal form is coherent for the cuts
  used to refine a fixed coarse corridor; this proposition says a complete
  lower corridor must also be pure for every ancestor upper bipartition present
  on the same ambient vertex set.
- The statement does not prove the terminal \(R_P(\theta)\) lift.  It narrows
  the remaining obstruction: a positive-mass coherent assembly must keep each
  complete lower corridor aligned with all ancestor signatures, or else the
  weighted lower corridor mass is strictly below the full product mass, with
  deficit equal to the total weight of missing incompatible positive-weight
  pairs.
- The proof is local and uses only the pair-link interval exclusion already
  proved in [[mrw-fced7420b905]]; it does not use direct weighted-Mantel
  aggregation, path-shadow disjointness alone, or a fixed blow-up construction
  as terminal evidence.
