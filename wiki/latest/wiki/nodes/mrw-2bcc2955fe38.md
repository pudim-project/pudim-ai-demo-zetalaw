---
id: mrw-2bcc2955fe38
type: proposition
title: Pair-link two-edge paths cast lower-core shadows
aliases: ["mrw-2bcc2955fe38", "Pair-link two-edge path shadow", "Cross-core path-shadow exclusion"]
status: proved
tags: [proposition, proved, erdos-536, squarefree-support, pair-link, hypergraph-independent-set, two-extension-slice, cross-core-coherence, path-shadow, lower-shadow, support-tail, patch-gate-audited]
parents: [mrw-3c39ca3d1973, mrw-354b105d4977, mrw-a32a6d3a5f20, mrw-55a8d9eddd2e]
refs: []
  - raw/20260520T110040Z-erdos-536-cross-core-mantel-defect-stability-and-coherence-f.md
  - references/sources/20260520T110040Z-cross-core-path-shadow-context.md
  - oracle/requests/20260520T110040Z-erdos536-cross-core-path-shadow-oracle-request.md
  - oracle/responses/20260520T110040Z-erdos536-cross-core-path-shadow-oracle-response.md
---

# Proposition: Pair-link two-edge paths cast lower-core shadows

## Statement

Let \(P\) be a finite set and let
\[
I(A,B)=\{C\subseteq P:A\triangle B\subseteq C\subseteq A\cup B\}.
\]
Let \(\mathcal F\subseteq2^P\) be pair-link-free: there are no pairwise
distinct \(A,B,C\in\mathcal F\) with \(C\in I(A,B)\).

Fix \(R\subseteq P\) and distinct \(x,y,z\in P\setminus R\).  Suppose
\[
R\cup\{x,y\}\in\mathcal F,
\qquad
R\cup\{y,z\}\in\mathcal F.
\]
Then
\[
D\cup\{x,z\}\notin\mathcal F
\qquad\text{for every }D\subseteq R\cup\{y\}.
\tag{1}
\]
Equivalently, the whole completion cylinder
\[
\{C\subseteq P:\{x,z\}\subseteq C\subseteq R\cup\{x,y,z\}\}
\]
is disjoint from \(\mathcal F\).

For fixed distinct \(x,z\in P\), put
\[
\mathcal E_{xz}
=
\{D\subseteq P\setminus\{x,z\}:D\cup\{x,z\}\in\mathcal F\}.
\]
For \(y\in P\setminus\{x,z\}\), put
\[
\mathcal P^y_{xz}
=
\{R\subseteq P\setminus\{x,y,z\}:
R\cup\{x,y\}\in\mathcal F,\ 
R\cup\{y,z\}\in\mathcal F\}.
\]
Define the \(y\)-augmented lower shadow
\[
\downarrow_y\mathcal P^y_{xz}
=
\{D\subseteq P\setminus\{x,z\}:
D\subseteq R\cup\{y\}\text{ for some }R\in\mathcal P^y_{xz}\}.
\]
Then
\[
\mathcal E_{xz}\cap\downarrow_y\mathcal P^y_{xz}=\varnothing.
\tag{2}
\]

In particular, if a two-extension slice over \(R\) contains a complete
bipartite subgraph \(K_{X,Y}\), then for every \(y\in Y\), every two distinct
\(x,z\in X\), and every \(D\subseteq R\cup\{y\}\),
\[
D\cup\{x,z\}\notin\mathcal F,
\]
and symmetrically with \(X\) and \(Y\) interchanged.  Hence every nontrivial
complete bipartite slice forbids all lower-core endpoint-pair edges inside each
side of the bipartition, obtained by restricting the display to \(D\subseteq R\).

## Proof

Let
\[
A=R\cup\{x,y\},
\qquad
B=R\cup\{y,z\}.
\]
Then
\[
A\triangle B=\{x,z\},
\qquad
A\cup B=R\cup\{x,y,z\}.
\]
If \(D\subseteq R\cup\{y\}\) and
\[
C=D\cup\{x,z\},
\]
then \(C\) contains \(A\triangle B\), and also
\[
C\subseteq R\cup\{x,y,z\}=A\cup B.
\]
Thus \(C\in I(A,B)\).  Moreover \(C\ne A\), because \(z\in C\setminus A\), and
\(C\ne B\), because \(x\in C\setminus B\).  The sets \(A\) and \(B\) are also
distinct.  Therefore, if \(C\in\mathcal F\), the three pairwise distinct
members \(A,B,C\) would violate pair-link-freeness.  This proves (1), and the
cylinder formulation is just the substitution \(C=D\cup\{x,z\}\) with
\(D\subseteq R\cup\{y\}\).

Now fix \(x,z\) and \(y\).  If
\[
D\in\mathcal E_{xz}\cap\downarrow_y\mathcal P^y_{xz},
\]
then \(D\cup\{x,z\}\in\mathcal F\), and for some
\(R\in\mathcal P^y_{xz}\) one has \(D\subseteq R\cup\{y\}\).  But the two sets
\(R\cup\{x,y\}\) and \(R\cup\{y,z\}\) lie in \(\mathcal F\), so (1) forbids
\(D\cup\{x,z\}\in\mathcal F\), a contradiction.  Hence (2) holds.

For the complete bipartite assertion, take any two distinct vertices on one
side and any vertex on the other side as the middle vertex \(y\).  The two
cross edges are present by the \(K_{X,Y}\) hypothesis, so (1) applies.  The
same argument with the parts interchanged proves the symmetric claim.

## Depends on

- [[mrw-3c39ca3d1973]] Pair-link shadow criterion for biased squarefree residuals
- [[mrw-354b105d4977]] Pair-link-free two-extension slices are triangle-free
- [[mrw-a32a6d3a5f20]] Weighted cross-core Mantel bound for pair-link-free families

## Notes

- The same-core triangle-free slice theorem [[mrw-354b105d4977]] is recovered
  from the special case \(D=R\): a two-edge path forbids the closing same-core
  edge \(R\cup\{x,z\}\).
- The new content is cross-core: the path forbids every endpoint-pair
  completion over every \(D\subseteq R\cup\{y\}\).  In particular, it forbids
  every lower-core edge \(D\cup\{x,z\}\) with \(D\subseteq R\).
- This is not a mass theorem and does not prove \(M_{P_k}(\theta)\to0\),
  \(U_k(\theta)\to0\), or any lift to \(R_P(\theta)\).  Its role is to replace
  pure weighted Mantel aggregation by a quantified shadow target: dense
  near-bipartite slices create many forbidden endpoint-pair lower shadows.
- The next useful theorem would show that, under the prime-biased product law,
  the lower shadows forced by many dense bipartite slices contribute a
  quadratic aggregate Mantel defect, or else expose a genuine positive-mass
  counterexample.
