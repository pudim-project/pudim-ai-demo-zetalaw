---
id: mrw-a3c54ddf4ae3
type: proposition
title: Empty-bottom star assemblies have residual envelopes and nonempty endpoint escape constraints
aliases: ["mrw-a3c54ddf4ae3", "Empty-bottom star assemblies have residual envelopes and nonempty endpoint escape constraints"]
status: proved
tags: [proposition, proved, erdos-536, squarefree-support, pair-link, endpoint-fiber, endpoint-interval, empty-endpoint, zero-gap, comparable-pairs, star-assembly, terminal-residual, shifted-window, cross-shadow, ordered-triples, endpoint-escape, product-measure, residual-envelope, residual-obstruction, escaped-mass]
parents: [mrw-03f08f291f7c, mrw-e75870a3c452, mrw-20ca89f696f2]
refs: []
  - raw/20260523T002549Z-erdos-536-empty-bottom-star-residual-envelope.md
  - raw/20260523T002549Z-erdos536-empty-bottom-star-residual-envelope.md
  - raw/20260523T002549Z-scout-forage-ingest.md
  - theory/forage/requests/20260523T002549Z-erdos536-empty-bottom-star-residual-envelope-request.md
  - theory/forage/responses/20260523T002549Z-erdos536-empty-bottom-star-residual-envelope-response.md
  - oracle/requests/20260523T002549Z-erdos536-empty-bottom-star-residual-envelope-oracle-request.md
  - oracle/responses/20260523T002549Z-erdos536-empty-bottom-star-residual-envelope-oracle-response.md
---

# Proposition: Empty-bottom star assemblies have residual envelopes and nonempty endpoint escape constraints

## Statement
Let \(P=B\sqcup T\) be finite.  Let
\(\mathcal U\subseteq2^B\setminus\{\emptyset\}\) be a finite collection of
nonempty endpoint patterns and set
\[
\mathcal E=\{\emptyset\}\cup\mathcal U.
\]
For each \(e\in\mathcal E\), let \(\mathcal R_e\subseteq2^T\), and define the
empty-bottom star assembly
\[
\mathcal F
=
\{R:R\in\mathcal R_{\emptyset}\}
\cup
\bigcup_{u\in\mathcal U}\{u\cup R:R\in\mathcal R_u\}.
\]
A family is pair-link-free if there are no three pairwise distinct members
\(F_1,F_2,F_3\) with \(F_3\in I_P(F_1,F_2)\).  For a terminal family
\(\mathcal A\), put
\[
\mathsf J_T(\mathcal A)
=
\bigcup_{\substack{A,B\in\mathcal A\\A\ne B}} I_T(A,B).
\]

Then \(\mathcal F\) is pair-link-free if and only if the following conditions
hold.

1. \(\mathcal R_{\emptyset}\) is pair-link-free in \(2^T\).

2. For every \(u\in\mathcal U\), the fiber \(\mathcal R_u\) is pair-link-free
   in \(2^T\).

3. For every \(u\in\mathcal U\),
   \[
   \mathcal R_{\emptyset}\cap\mathsf J_T(\mathcal R_u)=\emptyset.
   \]

4. For every \(u\in\mathcal U\), every \(A\in\mathcal R_{\emptyset}\), and every
   \(B\in\mathcal R_u\),
   \[
   \mathcal R_u\cap I_T(A,B)\subseteq\{B\}.
   \]

5. For every ordered nonconstant endpoint triple
   \[
   (u_1,u_2,u_3)\in\mathcal U^3,
   \qquad
   u_3\in I_B(u_1,u_2),
   \]
   where nonconstant means not \(u_1=u_2=u_3\), there do not exist
   \(R_i\in\mathcal R_{u_i}\) such that
   \[
   R_3\in I_T(R_1,R_2)
   \]
   and the three ambient sets \(u_i\cup R_i\) are pairwise distinct.

Equivalently, once the empty-bottom two-fiber constraints are enforced for each
\(u\in\mathcal U\), every remaining pair-link obstruction must be witnessed
entirely among nonempty endpoint patterns in \(\mathcal U\).

Consequently, if \(\nu_P=\pi_B\times\nu_T\) is a product law and
\[
\mathfrak M_T(a)
=
\sup\{\nu_T(\mathcal A\cap\{|R|>a\}):
\mathcal A\subseteq2^T,\ \mathcal A\text{ pair-link-free}\},
\]
then every pair-link-free star assembly satisfies, for every real \(L\),
\[
\nu_P(\mathcal F\cap\{|S|>L\})
\le
\pi_B(\emptyset)\mathfrak M_T(L)
+
\sum_{u\in\mathcal U}\pi_B(u)\mathfrak M_T(L-|u|).
\]
This is an upper envelope, not an exact variational identity in general:
independently optimal terminal fibers may violate the cross-fiber exclusions.

## Proof
For \(F_i=e_i\cup R_i\), the factorization in `mrw-20ca89f696f2` gives
\[
F_3\in I_P(F_1,F_2)
\quad\Longleftrightarrow\quad
e_3\in I_B(e_1,e_2)
\ \text{and}\
R_3\in I_T(R_1,R_2).
\]
Thus pair-link triples in \(\mathcal F\) can be classified by their endpoint
patterns.

If the endpoint triple is
\[
(\emptyset,\emptyset,\emptyset),
\]
then a forbidden ambient triple is exactly a terminal pair-link triple in
\(\mathcal R_{\emptyset}\).  This is excluded exactly by condition 1.

If the endpoint triple is
\[
(u,u,u)
\]
for some \(u\in\mathcal U\), then a forbidden ambient triple is exactly a
terminal pair-link triple in \(\mathcal R_u\).  This is excluded exactly by
condition 2.

If the endpoint triple is
\[
(u,u,\emptyset),
\]
then the two \(u\)-fiber parents must have distinct terminal parts
\(A,B\in\mathcal R_u\), and a lower child \(C\in\mathcal R_{\emptyset}\) creates
a forbidden triple exactly when
\[
C\in I_T(A,B).
\]
Because the child endpoint is \(\emptyset\), the lower child is distinct from
both top parents even if \(C=A\) or \(C=B\).  Thus these triples are excluded
exactly by condition 3.

If the endpoint triple is
\[
(\emptyset,u,u)
\quad\text{or}\quad
(u,\emptyset,u),
\]
write the lower parent as \(A\in\mathcal R_{\emptyset}\) and the top parent as
\(u\cup B\), \(B\in\mathcal R_u\).  Since
\[
I_B(\emptyset,u)=I_B(u,\emptyset)=\{u\},
\]
the child must lie in the \(u\)-fiber and has the form \(u\cup C\) with
\[
C\in\mathcal R_u\cap I_T(A,B).
\]
It is automatically distinct from the lower parent because \(u\ne\emptyset\),
and it equals the top parent exactly when \(C=B\).  Therefore the mixed
empty/top endpoint cases are excluded exactly by condition 4.

There are no other endpoint cases involving \(\emptyset\):
\[
u\notin I_B(\emptyset,\emptyset),
\qquad
\emptyset\notin I_B(\emptyset,u),
\]
and for \(u,v\ne\emptyset\),
\[
\emptyset\in I_B(u,v)
\]
forces \(u=v\), which is the already handled \((u,u,\emptyset)\) case.

All remaining endpoint triples are entirely contained in \(\mathcal U\).  The
constant case \((u,u,u)\) was already handled by condition 2.  Every
nonconstant ordered triple in \(\mathcal U^3\) with
\[
u_3\in I_B(u_1,u_2)
\]
is excluded exactly by condition 5, using the ambient-set pairwise distinctness
required in the definition of pair-link-free.  This proves both necessity and
sufficiency of the five conditions.

For the residual envelope, the endpoint slices are disjoint and the product law
factors, so
\[
\begin{aligned}
\nu_P(\mathcal F\cap\{|S|>L\})
&=
\pi_B(\emptyset)
\nu_T(\mathcal R_{\emptyset}\cap\{|R|>L\})\\
&\quad+
\sum_{u\in\mathcal U}
\pi_B(u)\nu_T(\mathcal R_u\cap\{|R|>L-|u|\}).
\end{aligned}
\]
By conditions 1 and 2, every terminal fiber is pair-link-free.  Therefore the
definition of \(\mathfrak M_T\) gives
\[
\nu_T(\mathcal R_{\emptyset}\cap\{|R|>L\})
\le
\mathfrak M_T(L)
\]
and
\[
\nu_T(\mathcal R_u\cap\{|R|>L-|u|\})
\le
\mathfrak M_T(L-|u|)
\]
for each \(u\in\mathcal U\).  Substitution proves the displayed envelope.

The envelope need not be sharp because terminal fibers that independently
maximize the summands may violate conditions 3, 4, or 5.  Thus this proposition
is a residual upper bound plus an exact localization of the remaining endpoint
escape constraints, not an exact variational formula.

## Depends on
- `mrw-03f08f291f7c` for the two-fiber empty-bottom residual criterion.
- `mrw-e75870a3c452` for the classification of zero shield gaps as
  empty-bottom comparable pairs.
- `mrw-20ca89f696f2` for endpoint/terminal interval factorization.

## Used by
- Pending: multi-branch empty-bottom residual quarantine and escape into
  nonempty endpoint interval triples.

## Notes
- Condition 5 is ordered and uses pairwise distinct ambient sets, not pairwise
  distinct endpoint patterns.  Repeated endpoint patterns such as \((u,u,v)\)
  or \((u,v,u)\) can still create ambient pair-link triples.
- No additional condition involving \(\mathcal R_u\cap\mathsf J_T(\mathcal R_{\emptyset})\)
  is needed, because \(I_B(\emptyset,\emptyset)=\{\emptyset\}\).
- This is not terminal Erdos 536 evidence.  It converts a star of empty-bottom
  zero-gap branches into an endpoint-weighted shifted terminal residual envelope
  plus explicitly localized nonempty endpoint escape constraints.
- Oracle accepted the proposition with the ordered-triple and ambient-distinct
  clarifications.
- Scout returned only a scaffold response and was ingested raw-only.
