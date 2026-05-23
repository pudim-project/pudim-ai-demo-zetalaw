---
id: mrw-740b9e5c6cff
type: corollary
title: Nonempty star escape triples split into terminal shadow exclusions
aliases: ["mrw-740b9e5c6cff", "Nonempty star escape triples split into terminal shadow exclusions"]
status: proved
tags: [corollary, proved, erdos-536, squarefree-support, pair-link, endpoint-fiber, endpoint-interval, star-assembly, endpoint-escape, ordered-triples, repeated-endpoints, comparable-pairs, terminal-shadow, cross-shadow, upper-mixed-shadow, nonempty-support, residual-obstruction, escaped-mass]
parents: [mrw-a3c54ddf4ae3, mrw-20ca89f696f2, mrw-88acf3940157]
refs: []
  - raw/20260523T010541Z-erdos-536-nonempty-star-escape-shadow-split.md
  - raw/20260523T010541Z-erdos536-nonempty-star-escape-shadow-split.md
  - raw/20260523T010541Z-scout-forage-ingest.md
  - theory/forage/requests/20260523T010541Z-erdos536-nonempty-star-escape-shadow-split-request.md
  - theory/forage/responses/20260523T010541Z-erdos536-nonempty-star-escape-shadow-split-response.md
  - oracle/requests/20260523T010541Z-erdos536-nonempty-star-escape-shadow-split-oracle-request.md
  - oracle/responses/20260523T010541Z-erdos536-nonempty-star-escape-shadow-split-oracle-response.md
---

# Corollary: Nonempty star escape triples split into terminal shadow exclusions

## Statement
Let \(P=B\sqcup T\), let
\[
\mathcal U\subseteq2^B\setminus\{\emptyset\},
\]
and let \(\mathcal R_u\subseteq2^T\) for \(u\in\mathcal U\).  For terminal
families \(\mathcal A,\mathcal B\), define
\[
\mathsf I_T(\mathcal A,\mathcal B)
=
\bigcup_{A\in\mathcal A,\ B\in\mathcal B}I_T(A,B),
\]
and
\[
\mathsf J_T(\mathcal A)
=
\bigcup_{\substack{A,B\in\mathcal A\\A\ne B}}I_T(A,B).
\]

The following endpoint-nonconstant condition is equivalent to the three
terminal shadow schemes below.

Endpoint-nonconstant condition: for every ordered nonconstant endpoint triple
\[
(u_1,u_2,u_3)\in\mathcal U^3,
\qquad
u_3\in I_B(u_1,u_2),
\]
there do not exist \(R_i\in\mathcal R_{u_i}\) such that
\[
R_3\in I_T(R_1,R_2)
\]
and the ambient sets \(u_i\cup R_i\) are pairwise distinct.

The equivalent terminal shadow schemes are:

1. If \(u_1,u_2,u_3\in\mathcal U\) are pairwise distinct and
   \[
   u_3\in I_B(u_1,u_2),
   \]
   then
   \[
   \mathcal R_{u_3}\cap
   \mathsf I_T(\mathcal R_{u_1},\mathcal R_{u_2})
   =
   \emptyset.
   \]

2. If \(f,u\in\mathcal U\) and \(f\subsetneq u\), then
   \[
   \mathcal R_f\cap\mathsf J_T(\mathcal R_u)=\emptyset.
   \]

3. If \(f,u\in\mathcal U\) and \(f\subsetneq u\), then for every
   \(A\in\mathcal R_f\) and \(B\in\mathcal R_u\),
   \[
   \mathcal R_u\cap I_T(A,B)\subseteq\{B\}.
   \]

If constant endpoint triples \((u,u,u)\) are included as well, then one must
also add individual terminal pair-link-freeness of every \(\mathcal R_u\), namely
\[
\mathcal R_u\cap I_T(A,B)\subseteq\{A,B\}
\qquad(A,B\in\mathcal R_u,\ A\ne B).
\]

Consequently, in the star criterion of `mrw-a3c54ddf4ae3`, the remaining
nonempty endpoint escape condition is exactly the conjunction of the three
displayed schemes.  The first two are full terminal shadow exclusions; the third
is an upper mixed-shadow exclusion in which only the repeated \(u\)-endpoint
parent \(B\) is harmless.

## Proof
By the endpoint/terminal factorization in `mrw-20ca89f696f2`,
\[
u_3\cup R_3\in I_P(u_1\cup R_1,u_2\cup R_2)
\]
if and only if
\[
u_3\in I_B(u_1,u_2)
\qquad\text{and}\qquad
R_3\in I_T(R_1,R_2).
\]
Thus it remains only to classify equality patterns among the ordered endpoint
triple \((u_1,u_2,u_3)\).

If \(u_1,u_2,u_3\) are pairwise distinct, then the ambient sets
\[
u_i\cup R_i
\]
are pairwise distinct for every choice of terminal sets.  Therefore forbidding
all terminal witnesses is exactly
\[
\mathcal R_{u_3}\cap
\mathsf I_T(\mathcal R_{u_1},\mathcal R_{u_2})
=\emptyset,
\]
which is scheme 1.

If two parent endpoints repeat, the triple has the form
\[
(u,u,f),
\qquad f\ne u.
\]
Since
\[
I_B(u,u)=2^u,
\]
the endpoint condition \(f\in I_B(u,u)\) is equivalent to \(f\subsetneq u\).
The two parent ambient sets are pairwise distinct exactly when their terminal
parts \(A,B\in\mathcal R_u\) are distinct.  The child endpoint \(f\) is different
from \(u\), so the child ambient set is distinct from both parents even if its
terminal part equals \(A\) or \(B\).  Hence this equality pattern is excluded
exactly by
\[
\mathcal R_f\cap\mathsf J_T(\mathcal R_u)=\emptyset,
\]
which is scheme 2.

The remaining endpoint-nonconstant repeated cases have the form
\[
(f,u,u)
\quad\text{or}\quad
(u,f,u),
\qquad f\ne u.
\]
In either case the endpoint condition is equivalent to \(f\subsetneq u\).  Write
the \(f\)-endpoint parent terminal set as \(A\in\mathcal R_f\) and the
\(u\)-endpoint parent terminal set as \(B\in\mathcal R_u\).  A \(u\)-endpoint
child has terminal part
\[
C\in\mathcal R_u\cap I_T(A,B).
\]
The child is automatically distinct from the \(f\)-endpoint ambient set.  It
coincides with the other \(u\)-endpoint ambient set exactly when \(C=B\).  Thus
the only harmless terminal child is \(B\), and this equality pattern is excluded
exactly by
\[
\mathcal R_u\cap I_T(A,B)\subseteq\{B\},
\]
which is scheme 3.

These cases exhaust all ordered endpoint-nonconstant triples in \(\mathcal U^3\).
The constant triple \((u,u,u)\) is excluded precisely by terminal
pair-link-freeness of \(\mathcal R_u\), namely by forbidding
\[
C\in\mathcal R_u\cap I_T(A,B)\setminus\{A,B\}
\]
for distinct \(A,B\in\mathcal R_u\).  This proves the stated equivalences.

## Depends on
- `mrw-a3c54ddf4ae3` for the star criterion whose nonempty endpoint escape
  condition is being split.
- `mrw-20ca89f696f2` for endpoint/terminal interval factorization.
- `mrw-88acf3940157` for the full cross-shadow viewpoint in the pairwise
  distinct and repeated-parent cases.

## Used by
- Pending: charging the nonempty endpoint escape branch after empty-bottom star
  residual quarantine.

## Notes
- Items 1--3 are equivalent to the endpoint-nonconstant remainder alone.  Adding
  terminal pair-link-freeness covers the constant nonempty endpoint triples.
- Scheme 2 uses the full two-point shadow \(\mathsf J_T(\mathcal R_u)\); terminal
  endpoints are not removed because the child endpoint is \(f\ne u\).
- Scheme 3 removes only \(B\), not \(A\), because \(u\cup A\) and \(f\cup A\)
  are distinct ambient sets when \(f\subsetneq u\).
- This corollary is not terminal Erdos 536 evidence.  It localizes the remaining
  star escape branch into explicit terminal shadow exclusions that still need
  quantitative charging or structural classification.
- Oracle accepted the result after correcting the final equivalence wording.
- Scout returned only a scaffold response and was ingested raw-only.
