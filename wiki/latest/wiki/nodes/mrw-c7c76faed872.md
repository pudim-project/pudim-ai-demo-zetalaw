---
id: mrw-c7c76faed872
type: proposition
title: Complete bipartite blow-ups preserve pair-link freeness
aliases: ["mrw-c7c76faed872", "Complete bipartite blow-ups preserve pair-link freeness"]
status: proved
tags: [proposition, proved, erdos-536, squarefree-support, pair-link, complete-bipartite, blow-up, cross-core-coherence, product-measure, support-tail, patch-gate-audited]
parents: [mrw-f83b56a1aa89, mrw-c6d0c6fa4d30, mrw-3c39ca3d1973, mrw-354b105d4977, mrw-a32a6d3a5f20]
refs: ["references/sources/20260521T001014Z-complete-bipartite-blowup-coherence-context.md"]
  - raw/20260521T001014Z-erdos-536-global-complete-bipartite-path-shadow-collapse-coh.md
  - oracle/responses/20260521T001014Z-erdos536-bipartite-blowup-coherence-oracle-response.md
  - references/sources/20260521T001014Z-complete-bipartite-blowup-coherence-context.md
---

# Proposition: Complete bipartite blow-ups preserve pair-link freeness

## Statement

Let \(P\) be a finite set and let \(X,Y\subseteq P\) be disjoint nonempty
sets.  Put
\[
Z=P\setminus(X\cup Y).
\]
For \(\mathcal R\subseteq2^Z\), define the complete bipartite blow-up
\[
\mathcal B(\mathcal R;X,Y)
=
\{R\cup\{x,y\}:R\in\mathcal R,\ x\in X,\ y\in Y\}.
\]
Use the pair-link interval
\[
I(A,B)=\{C:A\triangle B\subseteq C\subseteq A\cup B\},
\qquad
I^\circ(A,B)=I(A,B)\setminus\{A,B\}.
\]
Then \(\mathcal B(\mathcal R;X,Y)\) is pair-link-free in \(2^P\) if and only
if \(\mathcal R\) is pair-link-free in \(2^Z\).

Moreover, for any product law \(\nu_P\) on \(2^P\) with coordinate
probabilities \(q_p\in(0,1)\), let \(\nu_Z\) be the restricted product law on
\(2^Z\), and put
\[
\alpha_X
=
\sum_{x\in X}q_x\prod_{u\in X\setminus\{x\}}(1-q_u),
\qquad
\alpha_Y
=
\sum_{y\in Y}q_y\prod_{v\in Y\setminus\{y\}}(1-q_v).
\]
Then
\[
\nu_P(\mathcal B(\mathcal R;X,Y))
=
\alpha_X\alpha_Y\,\nu_Z(\mathcal R).
\]
For every real \(L\),
\[
\nu_P\bigl(\mathcal B(\mathcal R;X,Y)\cap\{A:|A|>L\}\bigr)
=
\alpha_X\alpha_Y\,
\nu_Z\bigl(\{R\in\mathcal R:|R|+2>L\}\bigr).
\]

## Proof

First suppose \(\mathcal R\) is not pair-link-free in \(2^Z\).  Then there
are pairwise distinct \(R_1,R_2,R_3\in\mathcal R\) such that
\[
R_3\in I^\circ_Z(R_1,R_2).
\]
Choose \(x\in X\) and \(y\in Y\), and set
\[
A_i=R_i\cup\{x,y\}\qquad(i=1,2,3).
\]
The three sets \(A_1,A_2,A_3\) are pairwise distinct members of
\(\mathcal B(\mathcal R;X,Y)\).  Since the edge \(\{x,y\}\) is common to all
three sets,
\[
A_1\triangle A_2=R_1\triangle R_2,
\qquad
A_1\cup A_2=(R_1\cup R_2)\cup\{x,y\}.
\]
Thus \(A_3\in I^\circ_P(A_1,A_2)\).  Hence
\(\mathcal B(\mathcal R;X,Y)\) is not pair-link-free.

Conversely, assume that \(\mathcal R\) is pair-link-free and suppose, for
contradiction, that
\[
A_i=R_i\cup\{x_i,y_i\}\in\mathcal B(\mathcal R;X,Y)
\qquad(i=1,2,3)
\]
are pairwise distinct, with \(R_i\in\mathcal R\), \(x_i\in X\), \(y_i\in Y\),
and
\[
A_3\in I^\circ_P(A_1,A_2).
\]
If \(x_1\ne x_2\), then both \(x_1\) and \(x_2\) lie in
\(A_1\triangle A_2\), so every member of \(I_P(A_1,A_2)\) must contain both
of them.  But \(A_3\) contains exactly one point of \(X\), a contradiction.
Therefore \(x_1=x_2\).  The same argument on \(Y\) gives \(y_1=y_2\).
Write this common bipartite edge as \(e=\{x_1,y_1\}\).

The interval inclusions now reduce on \(Z\) to
\[
R_1\triangle R_2\subseteq R_3\subseteq R_1\cup R_2.
\]
Because the common edge \(e\) is present in all three \(A_i\), pairwise
distinctness of the \(A_i\) implies pairwise distinctness of the \(R_i\).
Thus \(R_3\in I^\circ_Z(R_1,R_2)\), contradicting pair-link-freeness of
\(\mathcal R\).  This proves the equivalence.

For the measure identities, membership in \(\mathcal B(\mathcal R;X,Y)\) is
exactly the conjunction of three independent events: the \(Z\)-section lies in
\(\mathcal R\), the \(X\)-section has exactly one point, and the \(Y\)-section
has exactly one point.  The probabilities of the latter two events are
\(\alpha_X\) and \(\alpha_Y\), respectively, so
\[
\nu_P(\mathcal B(\mathcal R;X,Y))
=
\alpha_X\alpha_Y\,\nu_Z(\mathcal R).
\]
Every member \(R\cup\{x,y\}\) of the blow-up has cardinality \(|R|+2\), so the
same factorization with the additional condition \(|R|+2>L\) gives the
threshold identity.

## Depends on

- [[mrw-3c39ca3d1973]] Pair-link shadow criterion for biased squarefree residuals
- [[mrw-f83b56a1aa89]] Complete bipartite slices saturate path-shadow overlap
- [[mrw-c6d0c6fa4d30]] Path-shadow overlap bottleneck for endpoint-pair cores

## Used by

## Notes

- This proposition is a coherence theorem for the most literal way of
  assembling many complete bipartite collapsed slices with common parts
  \(X,Y\).  Such an assembly is not a new positive-mass construction: it is
  exactly a copy of the original pair-link-free problem on the core coordinate
  set \(Z\), multiplied by the product-measure probability of selecting one
  vertex from each side of the bipartition.
- The result does not prove \(M_{P_k}(\theta)\to0\), \(U_k(\theta)\to0\), or a
  lift to \(R_P(\theta)\).  Its role is to quarantine the direct coherent
  complete-bipartite blow-up as a terminal counterexample route.
- The remaining global target is sharper: either prove that positive-mass
  high-support pair-link-free families cannot assemble many incompatible
  bipartite blow-ups across changing parts and cores, or construct such a
  non-product assembly and test it against every full pair-link interval.
