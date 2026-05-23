---
id: mrw-e3fec03bf987
type: proposition
title: Cross-terminal endpoint multiplicity fibers obey interval-shadow exclusions
aliases: ["mrw-e3fec03bf987", "Cross-terminal endpoint multiplicity fibers obey interval-shadow exclusions"]
status: proved
tags: [proposition, proved, erdos-536, squarefree-support, pair-link, endpoint-fiber, terminal-fiber, endpoint-multiplicity, cross-r, interval-shadow, cross-shadow, separator-forest, endpoint-residual, route-quarantine]
parents: [mrw-d83f21b84e5c, mrw-20ca89f696f2, mrw-baa182012831, mrw-88acf3940157]
refs: []
  - raw/20260523T074620Z-erdos-536-cross-r-endpoint-shadow-exclusion.md
  - raw/20260523T074620Z-erdos536-cross-r-endpoint-shadow-exclusion.md
  - theory/forage/requests/20260523T074620Z-erdos536-cross-r-endpoint-shadow-exclusion-request.md
  - theory/forage/responses/20260523T074620Z-erdos536-cross-r-endpoint-shadow-exclusion-response.md
  - oracle/requests/20260523T074620Z-erdos536-cross-r-endpoint-shadow-exclusion-oracle-request.md
  - oracle/responses/20260523T074620Z-erdos536-cross-r-endpoint-shadow-exclusion-oracle-response.md
---

# Proposition: Cross-terminal endpoint multiplicity fibers obey interval-shadow exclusions

## Statement

Let \(P=B\sqcup T\) be a finite disjoint decomposition.  For
\(A,B\subseteq X\), write
\[
I_X(A,B)=\{C\subseteq X:A\triangle B\subseteq C\subseteq A\cup B\}.
\]
For endpoint families \(\mathcal A,\mathcal B\subseteq2^B\), write
\[
I_B(\mathcal A,\mathcal B)
=
\bigcup_{a\in\mathcal A,\ b\in\mathcal B}I_B(a,b).
\]

Let \(\mathcal E\subseteq2^B\), and for each \(e\in\mathcal E\) let
\(\mathcal U_e\subseteq2^T\).  Define
\[
\mathcal F
=
\bigcup_{e\in\mathcal E}\{e\cup R:R\in\mathcal U_e\}
\subseteq2^P.
\]
For each \(R\subseteq T\), define the endpoint multiplicity fiber
\[
\mathcal E_R=\{e\in\mathcal E:R\in\mathcal U_e\}.
\]

Assume \(\mathcal F\) is pair-link-free.  Let
\(R_1,R_2,R_3\subseteq T\).  If
\[
R_3\in I_T(R_1,R_2),
\]
then there are no endpoints
\[
e_i\in\mathcal E_{R_i}\qquad(i=1,2,3)
\]
such that
\[
e_3\in I_B(e_1,e_2)
\]
and the three endpoint-terminal pairs
\[
(e_1,R_1),\qquad (e_2,R_2),\qquad (e_3,R_3)
\]
are pairwise distinct.  Equivalently, because \(B\sqcup T\) is disjoint, the
three ambient sets
\[
e_1\cup R_1,\qquad e_2\cup R_2,\qquad e_3\cup R_3
\]
cannot be pairwise distinct.

Consequently, cross-terminal endpoint multiplicity fibers satisfy the
following interval-shadow exclusions.

First, if \(R_1,R_2,R_3\) are pairwise distinct and
\[
R_3\in I_T(R_1,R_2),
\]
then
\[
\mathcal E_{R_3}\cap I_B(\mathcal E_{R_1},\mathcal E_{R_2})
=\emptyset.
\]

Second, if \(R_0\subsetneq R\), then
\[
\mathcal E_{R_0}
\cap
\bigcup_{\substack{e_1,e_2\in\mathcal E_R\\ e_1\ne e_2}}
I_B(e_1,e_2)
=\emptyset.
\]

Third, if \(R_0\subsetneq R\), \(e\in\mathcal E_R\), and
\(e_0\in\mathcal E_{R_0}\), then
\[
I_B(e,e_0)\cap\mathcal E_R\subseteq\{e\},
\qquad
I_B(e_0,e)\cap\mathcal E_R\subseteq\{e\}.
\]

In the fully diagonal terminal case \(R_1=R_2=R_3=R\), this recovers ordinary
endpoint pair-link-freeness of \(\mathcal E_R\), and not the stronger
nonconstant endpoint-interval shield.

## Proof

Suppose such \(R_i\) and \(e_i\) exist.  Since \(e_i\in\mathcal E_{R_i}\), we
have \(R_i\in\mathcal U_{e_i}\), hence
\[
S_i=e_i\cup R_i\in\mathcal F
\qquad(i=1,2,3).
\]
By the endpoint-terminal interval factorization `mrw-20ca89f696f2`,
\[
S_3\in I_P(S_1,S_2)
\]
if and only if
\[
e_3\in I_B(e_1,e_2)
\qquad\text{and}\qquad
R_3\in I_T(R_1,R_2).
\]
The displayed hypotheses give these two coordinate conditions.  If the pairs
\((e_i,R_i)\) are pairwise distinct, then the ambient sets \(S_i\) are
pairwise distinct, because \(B\) and \(T\) are disjoint.  Thus
\[
S_1,S_2,S_3\in\mathcal F,
\qquad
S_3\in I_P(S_1,S_2),
\]
form a forbidden pair-link triple, contradicting pair-link-freeness of
\(\mathcal F\).  This proves the main assertion.

For the first consequence, pairwise distinct terminal parts force the
endpoint-terminal pairs \((e_i,R_i)\) to be pairwise distinct for every
endpoint choice.  Therefore any element of
\(\mathcal E_{R_3}\cap I_B(\mathcal E_{R_1},\mathcal E_{R_2})\) would violate
the main assertion.

For the second consequence, \(R_0\subsetneq R\) implies
\[
R_0\in I_T(R,R).
\]
If \(e_1\ne e_2\) lie in \(\mathcal E_R\), the two parent pairs
\((e_1,R)\) and \((e_2,R)\) are distinct.  Any child endpoint
\(e_0\in\mathcal E_{R_0}\) gives a pair \((e_0,R_0)\) distinct from both
parents because \(R_0\ne R\).  Hence no such \(e_0\) can lie in
\(I_B(e_1,e_2)\).

For the one-sided consequences, use the terminal triples
\[
(R,R_0,R)
\qquad\text{and}\qquad
(R_0,R,R).
\]
The condition \(R_0\subsetneq R\) gives
\[
R\in I_T(R,R_0)
\qquad\text{and}\qquad
R\in I_T(R_0,R).
\]
The only possible ambient equality in either triple is equality between the
two terminal-\(R\) pairs, which forces the endpoint in the third position to
be exactly \(e\).  Thus
\[
I_B(e,e_0)\cap\mathcal E_R\subseteq\{e\},
\qquad
I_B(e_0,e)\cap\mathcal E_R\subseteq\{e\}.
\]

Finally, if \(R_1=R_2=R_3=R\), pairwise distinct ambient sets are exactly
pairwise distinct endpoint choices.  The main assertion therefore says that
\(\mathcal E_R\) has no pairwise distinct endpoint triple
\[
e_1,e_2,e_3\in\mathcal E_R,
\qquad
e_3\in I_B(e_1,e_2),
\]
which is ordinary endpoint pair-link-freeness, as in `mrw-baa182012831`.
Repeated-endpoint interval cases are not excluded in this fully diagonal
terminal fiber.

## Depends on

- `mrw-d83f21b84e5c`: endpoint-weighted separator forests route active mass to
  terminal averages of endpoint multiplicity fibers \(\mathcal E_R\).
- `mrw-20ca89f696f2`: endpoint-terminal interval factorization.
- `mrw-baa182012831`: the fully diagonal terminal case gives the earlier
  pointwise ordinary endpoint residual condition.
- `mrw-88acf3940157`: context for cross-fiber interval-shadow exclusions.

## Used by

- Future cross-\(R\) multiplicity analysis: pointwise endpoint residual
  certificates cannot be chosen independently over terminal points that form
  interval triples.
- Future separator-forest escape theorems: if large endpoint multiplicity
  persists over many terminal high-window points, the terminal interval
  geometry must either force endpoint mass loss or leave a shielded/tower-like
  endpoint obstruction.

## Notes

- This proposition is structural and uses no product-measure assumptions.
- It is not terminal Erdos 536 evidence by itself.  It only recovers the
  cross-\(R\) endpoint constraints lost by Fubini conditioning in the
  pointwise residual route.
- If one of the endpoint multiplicity fibers is empty, or if
  \(R_3\notin I_T(R_1,R_2)\), the assertion is vacuous.
- If \(\mathcal F=\emptyset\) or has fewer than three ambient sets, the
  assertion is vacuous.
- Oracle accepted the result and recommended recording equality exceptions as
  equality of pairs \((e_i,R_i)\), equivalent to ambient equality because
  \(B\sqcup T\) is disjoint.  Scout returned only a scaffold and was ingested
  raw-only.
