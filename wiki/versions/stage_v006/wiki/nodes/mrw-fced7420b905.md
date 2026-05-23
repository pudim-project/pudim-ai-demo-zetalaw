---
id: mrw-fced7420b905
type: proposition
title: Nested path-shadow coherence for bipartite slice blocks
aliases: ["mrw-fced7420b905", "Nested path-shadow coherence for bipartite slice blocks"]
status: proved
tags: [proposition, proved, erdos-536, squarefree-support, pair-link, path-shadow, complete-bipartite, cross-core-coherence, nested-cores, signature-coherence, support-tail, scout-audited, patch-gate-audited]
parents: [mrw-2bcc2955fe38, mrw-c6d0c6fa4d30, mrw-f83b56a1aa89, mrw-c7c76faed872, mrw-3c39ca3d1973, mrw-354b105d4977]
refs: []
  - raw/20260521T001014Z-erdos-536-global-complete-bipartite-path-shadow-collapse-coh.md
  - raw/20260521T001727Z-scout-forage-ingest.md
  - theory/forage/responses/20260521T000655Z-erdos536-global-bipartite-collapse-coherence-response.md
  - oracle/responses/20260521T001014Z-erdos536-bipartite-blowup-coherence-oracle-response.md
  - references/sources/20260521T001014Z-complete-bipartite-blowup-coherence-context.md
---

# Proposition: Nested path-shadow coherence for bipartite slice blocks

## Statement

Let \(P\) be a finite set and let \(\mathcal F\subseteq2^P\) be
pair-link-free: there are no pairwise distinct \(A,B,C\in\mathcal F\) such
that
\[
A\triangle B\subseteq C\subseteq A\cup B.
\]
For \(R\subseteq P\), define the two-extension slice graph
\[
G_R^\mathcal F=(P\setminus R,E_R^\mathcal F),
\qquad
\{x,y\}\in E_R^\mathcal F
\Longleftrightarrow
R\cup\{x,y\}\in\mathcal F.
\]
For a graph \(G\), define its length-two endpoint graph by
\[
P_2(G)=
\{\{x,z\}: \text{there is }y\notin\{x,z\}\text{ with }
\{x,y\},\{y,z\}\in E(G)\}.
\]

If \(Q\subseteq R\subseteq P\), then
\[
E_Q^\mathcal F\cap P_2(G_R^\mathcal F)=\varnothing.
\tag{1}
\]

Consequently, if \(Q\subseteq R\) and \(G_R^\mathcal F\) contains a
nondegenerate complete bipartite graph \(K_{X,Y}\) with
\(X,Y\subseteq P\setminus R\) and \(X,Y\ne\varnothing\), then
\[
E_Q^\mathcal F\cap\left(\binom X2\cup\binom Y2\right)=\varnothing.
\tag{2}
\]
Thus the lower graph \(G_Q^\mathcal F[X\cup Y]\) is bipartite with respect to
the same cut \(X|Y\).

More generally, let \(Q\subseteq R_i\subseteq P\) for \(1\le i\le m\), and let
\(V\subseteq P\setminus\bigcup_i R_i\).  Suppose each \(G_{R_i}^\mathcal F\)
contains the complete bipartite graph \(K_{X_i,Y_i}\) on the same vertex set
\[
V=X_i\sqcup Y_i,
\qquad X_i,Y_i\ne\varnothing.
\]
For \(v\in V\), define its bipartition signature
\[
\sigma(v)=(\mathbf 1_{v\in X_i})_{i=1}^m\in\{0,1\}^m.
\]
Then every edge \(\{u,v\}\in E_Q^\mathcal F\cap\binom V2\) satisfies
\[
\sigma(u)=\mathbf 1-\sigma(v).
\tag{3}
\]
Equivalently, with \(V_\tau=\{v\in V:\sigma(v)=\tau\}\),
\[
E_Q^\mathcal F\cap\binom V2
\subseteq
\bigcup_{\tau\in\{0,1\}^m}
\{\{u,v\}:u\in V_\tau,\ v\in V_{\mathbf 1-\tau}\}.
\tag{4}
\]

## Proof

First prove (1).  Suppose, for contradiction, that
\[
\{x,z\}\in E_Q^\mathcal F\cap P_2(G_R^\mathcal F).
\]
Then \(Q\cup\{x,z\}\in\mathcal F\), and there is
\(y\notin\{x,z\}\) such that
\[
R\cup\{x,y\},\qquad R\cup\{y,z\}
\]
also lie in \(\mathcal F\).  Since \(x,y,z\in P\setminus R\) and
\(Q\subseteq R\), the three sets
\[
A=R\cup\{x,y\},\qquad
B=R\cup\{y,z\},\qquad
C=Q\cup\{x,z\}
\]
are pairwise distinct.  Moreover
\[
A\triangle B=\{x,z\}\subseteq C
\]
and
\[
C=Q\cup\{x,z\}\subseteq R\cup\{x,z\}
\subseteq R\cup\{x,y,z\}=A\cup B.
\]
Thus \(C\in I(A,B)\), contradicting pair-link-freeness of \(\mathcal F\).
This proves (1).

If \(G_R^\mathcal F\) contains a nondegenerate \(K_{X,Y}\), then every pair of
distinct vertices in \(X\) has a common neighbor in \(Y\), and every pair of
distinct vertices in \(Y\) has a common neighbor in \(X\).  Hence
\[
\binom X2\cup\binom Y2\subseteq P_2(G_R^\mathcal F),
\]
and (2) follows from (1).  Statement (2) is exactly the assertion that the
induced lower graph on \(X\cup Y\) has no same-side edges for the cut \(X|Y\).

For the signature statement, let \(\{u,v\}\in E_Q^\mathcal F\cap\binom V2\).
Fix \(i\).  Since \(Q\subseteq R_i\), the bipartite lower-core conclusion for
\(R_i\) says that \(u\) and \(v\) cannot both lie in \(X_i\) and cannot both
lie in \(Y_i\).  Since \(V=X_i\sqcup Y_i\), they lie on opposite sides of the
\(i\)-th cut.  This holds for every \(i\), so
\[
\sigma(u)=\mathbf 1-\sigma(v).
\]
The containment (4) is the same statement grouped by signature classes.

## Depends on

- [[mrw-2bcc2955fe38]] Pair-link two-edge paths cast lower-core shadows
- [[mrw-c6d0c6fa4d30]] Path-shadow overlap bottleneck for endpoint-pair cores
- [[mrw-f83b56a1aa89]] Complete bipartite slices saturate path-shadow overlap
- [[mrw-c7c76faed872]] Complete bipartite blow-ups preserve pair-link freeness

## Used by

## Notes

- This proposition is the locally audited part of the Scout response
  `20260521T000655Z-erdos536-global-bipartite-collapse-coherence-response.md`.
  Scout also listed outside candidates; those remain raw-only and are not used
  as proof.
- The first assertion is a nested-core graph form of the path-shadow exclusion
  from [[mrw-2bcc2955fe38]]: an upper two-edge path over \(R\) forbids the
  same endpoint-pair edge over every lower core \(Q\subseteq R\).
- The signature corollary is not a mass theorem.  It says that many upper
  complete bipartite blocks constrain a lower slice to complementary signature
  classes.  A terminal theorem would still have to show that positive
  prime-biased high-support mass forces enough incompatible signatures, or else
  construct a coherent non-product assembly that survives the full pair-link
  interval criterion.
